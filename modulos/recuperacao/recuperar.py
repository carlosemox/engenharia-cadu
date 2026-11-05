"""Executa uma receita local atestada em worktree de ensaio (Linux/macOS)."""
import argparse
from contextlib import closing
import fcntl
import hashlib
import json
import os
from pathlib import Path
import re
import signal
import sqlite3
import subprocess
import sys
import time


def digest(data):
    return hashlib.sha256(data).hexdigest()


def valid_id(value):
    return isinstance(value, str) and re.fullmatch(r"[a-z0-9][a-z0-9_.-]{0,79}", value)


def result(status, **fields):
    return {"estado": status, **fields}


def path_in(path, parent):
    return path == parent or parent in path.parents


def configure(profile, expected):
    raw = profile.read_bytes()
    if digest(raw) != expected:
        raise ValueError("Digest do perfil diverge da revisão autorizada.")
    cfg = json.loads(raw)
    if not isinstance(cfg, dict):
        raise ValueError("Perfil inválido.")
    root = Path(cfg["worktree"]).resolve(strict=True)
    control = profile.parent.resolve(strict=True)
    if not Path(cfg["worktree"]).is_absolute():
        raise ValueError("Indique a raiz Git absoluta no perfil.")
    if path_in(control, root) or path_in(root, control):
        raise ValueError("O controle privado e a worktree devem ser separados.")
    top = subprocess.check_output(["git", "-C", str(root), "rev-parse", "--show-toplevel"], text=True)
    if root != Path(top.strip()).resolve() or cfg.get("ambiente") != "ensaio-descartavel":
        raise ValueError("Worktree de ensaio obrigatória.")
    recipes = cfg["receitas"]
    if not isinstance(recipes, list) or not recipes or not all(map(valid_id, recipes)) or len(set(recipes)) != len(recipes):
        raise ValueError("Receitas inválidas.")
    if not valid_id(cfg["caso"]) or not valid_id(cfg["projeto"]):
        raise ValueError("Identidade inválida.")
    for key, maximum in (("tentativas", 3), ("segundos", 300)):
        if type(cfg[key]) is not int or not 1 <= cfg[key] <= maximum:
            raise ValueError(f"Limite inválido: {key}")
    driver = control / "procedimento.py"
    if driver.is_symlink() or digest(driver.read_bytes()) != cfg["sha256_procedimento"]:
        raise ValueError("Procedimento não corresponde ao digest fixado.")
    return cfg, root, control, driver


class Halt(Exception):
    pass


def phase(driver, stage, recipe, root, control, deadline, lock_fd):
    def check():
        if (control / "STOP").exists():
            raise Halt("PAUSED")
        if time.monotonic() >= deadline:
            raise Halt("TIMEOUT")
    check()
    # The surrounding supervisor owns the sandbox. Do not pass API credentials as environment.
    with subprocess.Popen([sys.executable, "-I", str(driver), stage, recipe],
                          cwd=root, env={"PATH": os.defpath}, stdin=subprocess.DEVNULL,
                          stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
                          start_new_session=True, pass_fds=(lock_fd,)) as child:
        try:
            while True:
                check()
                try:
                    return child.wait(timeout=0.1)
                except subprocess.TimeoutExpired:
                    continue
        finally:
            try:
                os.killpg(child.pid, signal.SIGKILL)
            except ProcessLookupError:
                pass


def recover(db, cfg, root, driver, control, mission, evidence, candidate, policy_sha, reconcile, lock_fd):
    case = (cfg["projeto"], cfg["caso"])
    task = (*case, mission)
    deadline = time.monotonic() + cfg["segundos"]
    if (control / "STOP").exists():
        return result("PAUSED")
    unresolved = db.execute(
        "SELECT id,project,incident,mission,policy FROM attempts WHERE state='IN_PROGRESS' LIMIT 1"
    ).fetchone()
    if unresolved:
        if not reconcile or unresolved[1:] != (*task, policy_sha):
            return result("RECONCILE", motivo="Tentativa interrompida; confira a árvore antes de novo efeito.")
        baseline = phase(driver, "probe", "-", root, control, deadline, lock_fd)
        if baseline == 0 and phase(driver, "holdout", "-", root, control, deadline, lock_fd) == 0:
            state = "RECONCILED_PASS"
        elif baseline == 1 and phase(driver, "rollback_check", "-", root, control, deadline, lock_fd) == 0:
            state = "ROLLED_BACK"
        else:
            return result("RECONCILE", motivo="Estado final ou restauração ainda sem prova.")
        db.execute("UPDATE attempts SET state=? WHERE id=?", (state, unresolved[0]))
        db.commit()
        return result(state)
    if reconcile:
        return result("NOT_PENDING")
    baseline = phase(driver, "probe", "-", root, control, deadline, lock_fd)
    if baseline == 0:
        reserved = phase(driver, "holdout", "-", root, control, deadline, lock_fd)
        return result("ALREADY_PASS" if reserved == 0 else "BLOCKED_REGRESSION",
                      referencia=0, holdout=reserved)
    if baseline != 1:
        return result("BLOCKED_DEPENDENCY", referencia=baseline)
    previous = db.execute(
        "SELECT mission,state FROM attempts WHERE project=? AND incident=? AND evidence=? "
        "ORDER BY id DESC LIMIT 1", (*case, evidence)).fetchone()
    if previous and (previous[0] == mission or previous[1] != "VERIFIED"):
        return result("BLOCKED_REPEAT", motivo="Mesmo incidente e mesma evidência.")
    failures = db.execute(
        "SELECT COUNT(*) FROM attempts WHERE project=? AND incident=? AND policy=? AND id > "
        "(SELECT COALESCE(MAX(id),0) FROM attempts WHERE project=? AND incident=? AND policy=? AND state='VERIFIED')",
        (*case, policy_sha, *case, policy_sha)).fetchone()[0]
    count = db.execute("SELECT COUNT(*) FROM attempts WHERE project=? AND incident=? AND mission=?", task).fetchone()[0]
    if max(count, failures) >= cfg["tentativas"]:
        return result("BUDGET_EXHAUSTED")
    if candidate and candidate not in cfg["receitas"]:
        raise ValueError("Receita fora do perfil.")
    learned = db.execute("SELECT recipe FROM lessons WHERE project=? AND incident=? AND policy=?", (*case, policy_sha)).fetchone()
    recipe = candidate or (learned[0] if learned else cfg["receitas"][0])
    source = "memoria" if learned and recipe == learned[0] else "candidata"
    cursor = db.execute("INSERT INTO attempts(project,incident,mission,evidence,state,recipe,policy) VALUES(?,?,?,?,'IN_PROGRESS',?,?)", (*task, evidence, recipe, policy_sha))
    db.commit()  # A crash after this point requires reconciliation, even in a new process.
    steps = {"referencia": baseline}
    status = "REJECTED"
    for stage in ("repair", "probe", "holdout"):
        steps[stage] = phase(driver, stage, recipe if stage == "repair" else "-", root, control, deadline, lock_fd)
        if steps[stage] != 0:
            break
    else:
        status = "VERIFIED"
    db.execute("UPDATE attempts SET state=?, checks=? WHERE id=?",
               (status, json.dumps(steps, sort_keys=True), cursor.lastrowid))
    if status == "VERIFIED":
        db.execute("INSERT OR REPLACE INTO lessons VALUES(?,?,?,?)", (*case, policy_sha, recipe))
    else:
        db.execute("DELETE FROM lessons WHERE project=? AND incident=? AND policy=? AND recipe=?", (*case, policy_sha, recipe))
    db.commit()
    return result(status, registro=cursor.lastrowid, origem=source, receita=recipe, verificacoes=steps, tentativa=count + 1)


def execute(args):
    cfg, root, control, driver = configure(args.perfil.resolve(strict=True), args.sha256)
    if not valid_id(args.missao) or not re.fullmatch(r"[0-9a-f]{64}", args.evidencia):
        raise ValueError("Missão estável e SHA-256 da evidência sanitizada são obrigatórios.")
    # All profiles for this worker use the same protected control directory.
    with (control / "worker.lock").open("a") as lock:
        try:
            fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError:
            return result("BUSY")
        with closing(sqlite3.connect(control / "recuperacao.sqlite3")) as db:
            db.executescript("""
            CREATE TABLE IF NOT EXISTS attempts(id INTEGER PRIMARY KEY, project TEXT, incident TEXT,
                mission TEXT, evidence TEXT, state TEXT, recipe TEXT, policy TEXT, checks TEXT);
            CREATE TABLE IF NOT EXISTS lessons(project TEXT, incident TEXT, policy TEXT, recipe TEXT,
                PRIMARY KEY(project,incident,policy));
            """)
            return recover(db, cfg, root, driver, control, args.missao, args.evidencia,
                           args.candidata, args.sha256, args.reconciliar, lock.fileno())


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--perfil", type=Path, required=True)
    parser.add_argument("--sha256", required=True)
    parser.add_argument("--missao", required=True)
    parser.add_argument("--evidencia", required=True)
    parser.add_argument("--candidata")
    parser.add_argument("--reconciliar", action="store_true")
    args = parser.parse_args()
    try:
        report = execute(args)
    except Halt as exc:
        report = result(str(exc))
    except (OSError, ValueError, KeyError, TypeError, sqlite3.Error, subprocess.SubprocessError) as exc:
        report = result("INVALID", motivo=str(exc))
    print(json.dumps(report, ensure_ascii=False))
    return 0 if report["estado"] in ("VERIFIED", "ALREADY_PASS", "RECONCILED_PASS", "ROLLED_BACK", "NOT_PENDING") else 2


if __name__ == "__main__":
    sys.exit(main())
