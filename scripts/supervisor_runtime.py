"""Durable, supervised read-only audit queue (Python standard library).

Trusted entry point: Runtime(db, project, evidence_dir), then
start_run(run_id, session_id=..., workers={id: ["auditor", "reviewer"]},
          deadline=<Unix seconds>, max_claims=..., lease_seconds=...,
          supervised=True, environment="CODEX_WEB").
The returned Session exposes enqueue/worker/stop/resume/status/reap; worker(id)
returns a bound Worker exposing claim/heartbeat/submit/review. Only the trusted
local session may create sessions or select workers. Never expose those entry
points to job payloads or accept worker identities from model output. Reopening
an existing run requires exactly the same configuration, including its roster.

Jobs have exactly id, capability="read_only_audit", paths (exact relative
files), depends_on (IDs). Snapshot = SHA256(canonical JSON path/hash manifest).
Evidence/artifact arguments are {relative_path: sha256}; files must already
exist under evidence_dir, outside project and Git. Submit includes the claim's
snapshot and fencing token; review includes the returned submission ID,
snapshot, PASS/FAIL, and an artifact manifest. Only an independent trusted
reviewer can attest progress=True on FAIL, resetting the no-progress counter.
Expiry always counts as failure without progress. Three attempts / two failures
without progress block further work. A later PASS proposes, never adopts, a
lesson linked to each earlier rejection.

No command execution, LLM calls, background loop, project writes or unattended
mode. SQLite is persistence and concurrency control, not process isolation.
The host/bridge must enforce read-only access for workers and authenticate real
identities; this in-process API does not protect against a malicious Python
caller or database owner. Directories and the clock must be host-controlled.
The host must serialize source/evidence writers for capture through review;
filesystem reads and SQLite commits are not one atomic transaction. Rechecks
detect observed changes, not malicious concurrent writers or change-and-restore.
Persistence survives process restarts on the same durable volume; it does not
make an ephemeral web workspace survive deletion. Status omits fencing secrets.
"""
import hashlib
import json
import math
import os
from pathlib import Path
import secrets
import sqlite3
import stat
import time
from contextlib import contextmanager


class RuntimeError(ValueError):
    """Rejected runtime operation; transaction has no partial effects."""


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"), allow_nan=False)


def digest(value):
    return hashlib.sha256(canonical(value).encode()).hexdigest()


def identifier(value):
    if not isinstance(value, str) or not value.strip() or len(value) > 256:
        raise RuntimeError("invalid identity")
    return value


def relative(value):
    if (not isinstance(value, str) or not value or
            any(c in value for c in "\\:\x00*?[]") or
            any(p in ("", ".", "..", ".git", "secrets") or p == ".env" or
                p.startswith(".env.") for p in value.split("/"))):
        raise RuntimeError("expected exact canonical relative file path")
    return value


def directory_fd(value):
    p = Path(value)
    if not p.is_absolute() or ".." in p.parts:
        raise RuntimeError("roots must be absolute, without traversal")
    # Check each directory with descriptor-relative O_NOFOLLOW, including roots.
    fd = os.open("/", os.O_RDONLY | os.O_DIRECTORY)
    try:
        for part in p.parts[1:]:
            nxt = os.open(part, os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW,
                          dir_fd=fd)
            os.close(fd)
            fd = nxt
    except OSError as exc:
        os.close(fd)
        raise RuntimeError("unsafe or missing directory") from exc
    return fd


def absolute(value):
    os.close(directory_fd(value))
    return Path(value)


def file_hash(root, name):
    relative(name)
    fd = directory_fd(root)
    try:
        parts = name.split("/")
        for part in parts[:-1]:
            nxt = os.open(part, os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW,
                          dir_fd=fd)
            os.close(fd)
            fd = nxt
        target = os.open(parts[-1], os.O_RDONLY | os.O_NOFOLLOW | os.O_NONBLOCK,
                         dir_fd=fd)
        with os.fdopen(target, "rb") as stream:
            before = os.fstat(stream.fileno())
            if not stat.S_ISREG(before.st_mode) or before.st_nlink != 1:
                raise RuntimeError("expected regular, non-hardlinked file")
            h = hashlib.sha256()
            for chunk in iter(lambda: stream.read(65536), b""):
                h.update(chunk)
            after = os.fstat(stream.fileno())
            if (before.st_size, before.st_mtime_ns, before.st_ctime_ns) != (
                    after.st_size, after.st_mtime_ns, after.st_ctime_ns):
                raise RuntimeError("file changed during hashing")
            return h.hexdigest()
    except OSError as exc:
        raise RuntimeError("missing or unsafe file") from exc
    finally:
        os.close(fd)


def positive(value):
    return type(value) in (int, float) and math.isfinite(value) and value > 0


SCHEMA = """
CREATE TABLE IF NOT EXISTS config (id INTEGER PRIMARY KEY CHECK(id=1), value TEXT NOT NULL);
CREATE TABLE IF NOT EXISTS control (id INTEGER PRIMARY KEY CHECK(id=1), stopped INTEGER NOT NULL);
INSERT OR IGNORE INTO control VALUES(1, 0);
CREATE TABLE IF NOT EXISTS runs (id TEXT PRIMARY KEY, config TEXT NOT NULL, claims INTEGER NOT NULL DEFAULT 0);
CREATE TABLE IF NOT EXISTS jobs (
 id TEXT PRIMARY KEY, spec TEXT NOT NULL, state TEXT NOT NULL DEFAULT 'READY',
 attempts INTEGER NOT NULL DEFAULT 0, no_progress INTEGER NOT NULL DEFAULT 0,
 run_id TEXT, worker_id TEXT, token TEXT, expires REAL, snapshot TEXT, manifest TEXT,
 submission_id TEXT, evidence TEXT);
CREATE TABLE IF NOT EXISTS events (
 seq INTEGER PRIMARY KEY AUTOINCREMENT, at REAL NOT NULL, kind TEXT NOT NULL,
 job_id TEXT, data TEXT NOT NULL);
CREATE TRIGGER IF NOT EXISTS events_no_update BEFORE UPDATE ON events
 BEGIN SELECT RAISE(ABORT, 'append-only events'); END;
CREATE TRIGGER IF NOT EXISTS events_no_delete BEFORE DELETE ON events
 BEGIN SELECT RAISE(ABORT, 'append-only events'); END;
CREATE TABLE IF NOT EXISTS reviews (
 submission_id TEXT PRIMARY KEY, job_id TEXT NOT NULL, worker_id TEXT NOT NULL,
 result TEXT NOT NULL, snapshot TEXT NOT NULL, artifact TEXT NOT NULL,
 progress INTEGER NOT NULL, event_seq INTEGER NOT NULL);
CREATE TABLE IF NOT EXISTS lessons (
 rejection_id TEXT PRIMARY KEY, success_id TEXT NOT NULL, job_id TEXT NOT NULL,
 state TEXT NOT NULL CHECK(state='PROPOSED'));
"""


class Runtime:
    def __init__(self, db, project, evidence_dir):
        self.project = absolute(project)
        self.evidence_dir = absolute(evidence_dir)
        db = Path(db)
        if not db.is_absolute() or db.name in ("", ".", ".."):
            raise RuntimeError("absolute database filename required")
        parent = absolute(db.parent)
        for directory in (parent, self.evidence_dir):
            if (directory == self.project or self.project in directory.parents or
                    directory in self.project.parents):
                raise RuntimeError("runtime storage must be outside project")
            if any((p / ".git").exists() for p in (directory, *directory.parents)):
                raise RuntimeError("runtime storage must be outside Git")
            mode = directory.stat()
            if mode.st_uid != os.getuid() or mode.st_mode & 0o022:
                raise RuntimeError("storage directory must be owned and private to writer")
        if self.evidence_dir == parent or self.evidence_dir in parent.parents or parent in self.evidence_dir.parents:
            raise RuntimeError("database and evidence directories must be separate")
        for suffix in ("", "-wal", "-shm", "-journal"):
            candidate = Path(str(db) + suffix)
            if candidate.is_symlink() or (candidate.exists() and (
                    not candidate.is_file() or candidate.stat().st_nlink != 1)):
                raise RuntimeError("unsafe database file")
        self._db = sqlite3.connect(str(db), timeout=10, isolation_level=None)
        self._db.row_factory = sqlite3.Row
        try:
            self._db.execute("PRAGMA journal_mode=WAL")
            self._db.execute("PRAGMA synchronous=FULL")
            self._db.executescript(SCHEMA)
            config = canonical({"version": 1, "project": str(self.project),
                                "evidence_dir": str(self.evidence_dir)})
            with self._transaction():
                row = self._db.execute("SELECT value FROM config WHERE id=1").fetchone()
                if row and row[0] != config:
                    raise RuntimeError("database root/config mismatch")
                if not row:
                    self._db.execute("INSERT INTO config VALUES(1,?)", (config,))
                    self._event("INIT", None, json.loads(config))
        except BaseException:
            self._db.close()
            raise

    def close(self):
        self._db.close()

    @contextmanager
    def _transaction(self):
        self._db.execute("BEGIN IMMEDIATE")
        try:
            yield
            self._db.execute("COMMIT")
        except BaseException:
            self._db.execute("ROLLBACK")
            raise

    def _event(self, kind, job_id=None, data=None):
        return self._db.execute(
            "INSERT INTO events(at,kind,job_id,data) VALUES(?,?,?,?)",
            (time.time(), kind, job_id, canonical(data or {}))).lastrowid

    def start_run(self, run_id, *, session_id, workers, deadline, max_claims,
                  lease_seconds=60, supervised=False, environment="CODEX_WEB"):
        """Trusted host configuration, never fields imported from the queue."""
        identifier(run_id)
        identifier(session_id)
        if supervised is not True or environment != "CODEX_WEB":
            raise RuntimeError("only supervised CODEX_WEB sessions are authorized")
        if (not positive(deadline) or type(max_claims) is not int or max_claims < 1
                or not positive(lease_seconds)):
            raise RuntimeError("invalid run budget")
        if not isinstance(workers, dict) or not workers:
            raise RuntimeError("trusted worker roster required")
        roster = {}
        for worker, roles in workers.items():
            identifier(worker)
            if (not isinstance(roles, (list, tuple)) or not roles or
                    any(r not in ("auditor", "reviewer") for r in roles)):
                raise RuntimeError("invalid worker roles")
            roster[worker] = sorted(set(roles))
        cfg = canonical(dict(session_id=session_id, workers=roster, deadline=deadline,
                             max_claims=max_claims, lease_seconds=lease_seconds,
                             supervised=True, environment=environment))
        with self._transaction():
            row = self._db.execute("SELECT config FROM runs WHERE id=?", (run_id,)).fetchone()
            if row and row[0] != cfg:
                raise RuntimeError("run configuration is immutable")
            if not row:
                if deadline <= time.time():
                    raise RuntimeError("run deadline elapsed")
                self._db.execute("INSERT INTO runs(id,config) VALUES(?,?)", (run_id, cfg))
                self._event("RUN_STARTED", data={"run_id": run_id, **json.loads(cfg)})
        return Session(self, run_id)

    def _snapshot(self, spec):
        manifest = {p: file_hash(self.project, p) for p in spec["paths"]}
        return digest(manifest), manifest

    def _evidence(self, manifest):
        if not isinstance(manifest, dict) or not manifest:
            raise RuntimeError("nonempty evidence manifest required")
        for path, expected in manifest.items():
            if not isinstance(expected, str) or file_hash(self.evidence_dir, path) != expected:
                raise RuntimeError("evidence hash mismatch")
        return canonical(manifest)


class Session:
    """Trusted bridge control surface; no execution or background scheduling."""
    def __init__(self, runtime, run_id):
        self._r, self.run_id = runtime, run_id

    def _config(self):
        row = self._r._db.execute("SELECT * FROM runs WHERE id=?", (self.run_id,)).fetchone()
        if not row:
            raise RuntimeError("unknown run")
        return json.loads(row["config"]), row["claims"]

    def _gate(self, claim=False):
        cfg, claims = self._config()
        if self._r._db.execute("SELECT stopped FROM control").fetchone()[0]:
            raise RuntimeError("STOPPED")
        if time.time() >= cfg["deadline"]:
            raise RuntimeError("run deadline elapsed")
        if claim and claims >= cfg["max_claims"]:
            raise RuntimeError("claim budget exhausted")
        return cfg

    def worker(self, worker_id):
        cfg, _ = self._config()
        if worker_id not in cfg["workers"]:
            raise RuntimeError("worker not bound by trusted session")
        return Worker(self, worker_id)

    def enqueue(self, jobs):
        """Atomic batch import; exact canonical content is the idempotency key."""
        r = self._r
        if not isinstance(jobs, list):
            raise RuntimeError("jobs must be a list")
        with r._transaction():
            self._gate()
            existing = {row["id"]: json.loads(row["spec"])
                        for row in r._db.execute("SELECT id,spec FROM jobs")}
            added = {}
            for job in jobs:
                if not isinstance(job, dict) or set(job) != {"id", "capability", "paths", "depends_on"}:
                    raise RuntimeError("invalid job schema; mutation/unattended fields forbidden")
                jid = identifier(job["id"])
                if job["capability"] != "read_only_audit":
                    raise RuntimeError("capability forbidden")
                for key in ("paths", "depends_on"):
                    if not isinstance(job[key], list) or any(not isinstance(x, str) for x in job[key]):
                        raise RuntimeError("invalid job list")
                    if len(set(job[key])) != len(job[key]):
                        raise RuntimeError("duplicate list member")
                if not job["paths"]:
                    raise RuntimeError("exact file scope required")
                for path in job["paths"]:
                    relative(path)
                for dep in job["depends_on"]:
                    identifier(dep)
                if jid in existing:
                    if canonical(existing[jid]) != canonical(job):
                        raise RuntimeError("divergent job ID")
                    continue
                r._snapshot(job)
                existing[jid] = json.loads(canonical(job))
                added[jid] = existing[jid]
            # Iterative topological removal avoids recursion limits on large queues.
            remaining = {jid: set(spec["depends_on"]) for jid, spec in existing.items()}
            if any(dep not in remaining for deps in remaining.values() for dep in deps):
                raise RuntimeError("missing dependency")
            while remaining:
                ready = {jid for jid, deps in remaining.items() if not deps}
                if not ready:
                    raise RuntimeError("dependency cycle")
                remaining = {jid: deps - ready for jid, deps in remaining.items() if jid not in ready}
            for jid, spec in added.items():
                r._db.execute("INSERT INTO jobs(id,spec) VALUES(?,?)", (jid, canonical(spec)))
                r._event("ENQUEUED", jid, {"spec": spec, "run_id": self.run_id})
            self._gate()
            return len(added)

    def stop(self):
        with self._r._transaction():
            self._r._db.execute("UPDATE control SET stopped=1")
            self._r._event("STOP", data={"run_id": self.run_id})

    def resume(self):
        """Explicit trusted-session action; does not reset deadlines or budgets."""
        with self._r._transaction():
            self._config()
            self._r._db.execute("UPDATE control SET stopped=0")
            self._r._event("RESUME", data={"run_id": self.run_id})

    def _failure(self, row, progress=False):
        count = 0 if progress else row["no_progress"] + 1
        state = "BLOCKED" if row["attempts"] >= 3 or count >= 2 else "READY"
        self._r._db.execute("""UPDATE jobs SET state=?,no_progress=?,token=NULL,
            expires=NULL,submission_id=NULL,evidence=NULL WHERE id=?""",
                           (state, count, row["id"]))
        return state

    def reap(self):
        """Only expired read-only work; no external effect is retried."""
        r = self._r
        result = []
        with r._transaction():
            for row in r._db.execute("SELECT * FROM jobs WHERE state IN ('IN_PROGRESS','IN_REVIEW') AND expires<=?",
                                     (time.time(),)).fetchall():
                spec = json.loads(row["spec"])
                if spec["capability"] != "read_only_audit":
                    raise RuntimeError("unsafe retry capability")
                state = self._failure(row)
                r._event("EXPIRED", row["id"], {"run_id": row["run_id"],
                         "attempt": row["attempts"], "state": state})
                result.append(row["id"])
        return result

    def status(self):
        r = self._r
        with r._transaction():
            cfg, claims = self._config()
            return {"run_id": self.run_id, "config": cfg, "claims": claims,
                    "stopped": bool(r._db.execute("SELECT stopped FROM control").fetchone()[0]),
                    "jobs": [dict(row) for row in r._db.execute(
                        "SELECT id,state,attempts,no_progress,run_id,worker_id,expires,snapshot,submission_id FROM jobs ORDER BY id")],
                    "events": [dict(row) for row in r._db.execute("SELECT * FROM events ORDER BY seq")],
                    "lessons": [dict(row) for row in r._db.execute("SELECT * FROM lessons ORDER BY rejection_id")]}


class Worker:
    """Bound by Session.worker in the trusted host, never by imported jobs."""
    def __init__(self, session, worker_id):
        self._s, self.worker_id = session, worker_id

    def _role(self, role, claim=False):
        cfg = self._s._gate(claim=claim)
        if role not in cfg["workers"].get(self.worker_id, []):
            raise RuntimeError("worker role forbidden")
        return cfg

    def _live(self, job_id, token=None, state=None):
        r = self._s._r
        row = r._db.execute("SELECT * FROM jobs WHERE id=?", (job_id,)).fetchone()
        if (not row or row["run_id"] != self._s.run_id or
                row["state"] not in ("IN_PROGRESS", "IN_REVIEW") or
                (state and row["state"] != state) or row["expires"] <= time.time()):
            raise RuntimeError("no live matching lease/state")
        if token is not None and (row["worker_id"] != self.worker_id or
                not isinstance(token, str) or not secrets.compare_digest(row["token"], token)):
            raise RuntimeError("stale fencing token or wrong worker")
        return row

    def claim(self):
        s, r = self._s, self._s._r
        with r._transaction():
            cfg = self._role("auditor", claim=True)
            # Global pilot WIP=1, including review and other sessions/runs.
            # Expired leases occupy the slot until an explicit reap records failure.
            if r._db.execute("SELECT 1 FROM jobs WHERE state IN ('IN_PROGRESS','IN_REVIEW') LIMIT 1").fetchone():
                return None
            done = {row[0] for row in r._db.execute("SELECT id FROM jobs WHERE state='DONE'")}
            for row in r._db.execute("SELECT * FROM jobs WHERE state='READY' AND attempts<3 AND no_progress<2 ORDER BY id").fetchall():
                spec = json.loads(row["spec"])
                if not set(spec["depends_on"]) <= done:
                    continue
                if spec["capability"] != "read_only_audit":
                    raise RuntimeError("capability forbidden")
                snapshot, manifest = r._snapshot(spec)
                self._role("auditor", claim=True)
                token = secrets.token_hex(32)
                expires = min(time.time() + cfg["lease_seconds"], cfg["deadline"])
                r._db.execute("""UPDATE jobs SET state='IN_PROGRESS',attempts=attempts+1,
                    run_id=?,worker_id=?,token=?,expires=?,snapshot=?,manifest=?,
                    submission_id=NULL,evidence=NULL WHERE id=?""",
                    (s.run_id, self.worker_id, token, expires, snapshot, canonical(manifest), row["id"]))
                r._db.execute("UPDATE runs SET claims=claims+1 WHERE id=?", (s.run_id,))
                r._event("CLAIMED", row["id"], {"run_id": s.run_id, "worker_id": self.worker_id,
                         "attempt": row["attempts"] + 1, "snapshot": snapshot, "manifest": manifest})
                return {"job": spec, "token": token, "expires": expires,
                        "snapshot": snapshot, "manifest": manifest, "attempt": row["attempts"] + 1}
            return None

    def heartbeat(self, job_id, token):
        r = self._s._r
        with r._transaction():
            cfg = self._role("auditor")
            if not isinstance(token, str):
                raise RuntimeError("token required")
            self._live(job_id, token)
            expires = min(time.time() + cfg["lease_seconds"], cfg["deadline"])
            r._db.execute("UPDATE jobs SET expires=? WHERE id=?", (expires, job_id))
            r._event("HEARTBEAT", job_id, {"expires": expires, "worker_id": self.worker_id})
            return expires

    def submit(self, job_id, token, *, snapshot, evidence):
        r = self._s._r
        with r._transaction():
            self._role("auditor")
            if not isinstance(token, str):
                raise RuntimeError("token required")
            row = self._live(job_id, token, "IN_PROGRESS")
            actual, manifest = r._snapshot(json.loads(row["spec"]))
            if snapshot != row["snapshot"] or actual != snapshot or canonical(manifest) != row["manifest"]:
                raise RuntimeError("snapshot mismatch")
            evidence = r._evidence(evidence)
            if r._snapshot(json.loads(row["spec"])) != (snapshot, manifest):
                raise RuntimeError("snapshot changed while hashing evidence")
            self._role("auditor")
            self._live(job_id, token, "IN_PROGRESS")
            submission = secrets.token_hex(32)
            r._db.execute("UPDATE jobs SET state='IN_REVIEW',submission_id=?,evidence=? WHERE id=?",
                          (submission, evidence, job_id))
            r._event("SUBMITTED", job_id, {"submission_id": submission, "snapshot": snapshot,
                     "evidence": json.loads(evidence), "worker_id": self.worker_id})
            return submission

    def review(self, job_id, submission_id, *, snapshot, result, artifact, progress=False):
        r = self._s._r
        with r._transaction():
            self._role("reviewer")
            row = self._live(job_id, state="IN_REVIEW")
            if row["worker_id"] == self.worker_id:
                raise RuntimeError("independent reviewer required")
            if result not in ("PASS", "FAIL") or type(progress) is not bool or (result == "PASS" and progress):
                raise RuntimeError("invalid review verdict/progress")
            if not isinstance(submission_id, str) or submission_id != row["submission_id"]:
                raise RuntimeError("stale submission/replay")
            actual, manifest = r._snapshot(json.loads(row["spec"]))
            if snapshot != row["snapshot"] or actual != snapshot or canonical(manifest) != row["manifest"]:
                raise RuntimeError("snapshot mismatch")
            r._evidence(json.loads(row["evidence"]))
            artifact = r._evidence(artifact)
            # Evidence/artifact hashing may be slow. Recheck the captured inputs
            # afterwards; the trusted host still must serialize filesystem writers.
            r._evidence(json.loads(row["evidence"]))
            if r._snapshot(json.loads(row["spec"])) != (snapshot, manifest):
                raise RuntimeError("snapshot changed while hashing review artifact")
            self._role("reviewer")
            self._live(job_id, state="IN_REVIEW")
            seq = r._event("REVIEWED", job_id, {"submission_id": submission_id,
                          "worker_id": self.worker_id, "implementer": row["worker_id"],
                          "snapshot": snapshot, "result": result,
                          "artifact": json.loads(artifact), "progress": progress})
            r._db.execute("INSERT INTO reviews VALUES(?,?,?,?,?,?,?,?)",
                          (submission_id, job_id, self.worker_id, result, snapshot, artifact, int(progress), seq))
            if result == "FAIL":
                return self._s._failure(row, progress)
            r._db.execute("UPDATE jobs SET state='DONE',token=NULL,expires=NULL WHERE id=?", (job_id,))
            for rejection in r._db.execute("SELECT submission_id FROM reviews WHERE job_id=? AND result='FAIL'", (job_id,)):
                r._db.execute("INSERT INTO lessons VALUES(?,?,?,'PROPOSED')",
                              (rejection[0], submission_id, job_id))
                r._event("LESSON_PROPOSED", job_id, {"rejection_id": rejection[0], "success_id": submission_id})
            return "DONE"
