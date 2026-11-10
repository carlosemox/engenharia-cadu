"""Contract tests; these do not establish macOS sandbox or model qualification."""
import copy
import importlib.util
import math
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import time
import unittest
from unittest import mock


SOURCE = Path(__file__).resolve().parents[1] / "scripts" / "local_executor.py"
SPEC = importlib.util.spec_from_file_location("local_executor_under_test", SOURCE)
executor = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = executor
SPEC.loader.exec_module(executor)
REJECTED = (ValueError, OSError)


class LocalExecutorContractTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.base = Path(self.temp.name).resolve()
        self.root = self.base / "project"
        self.root.mkdir()
        self.state = self.base / "state"
        self.state.mkdir()
        (self.root / "solution.js").write_text("module.exports = 41;\n")

    def job(self):
        return {
            "id": "task-001",
            "project": "pilot",
            "root": str(self.root),
            "files": ["solution.js"],
            "instruction": "Correct the exported value to 42.",
            "checks": [["/usr/local/bin/node", "--check", "solution.js"]],
            "approved": True,
            "expires_at": time.time() + 600,
            "revision": 1,
        }

    def supervisor(self):
        return executor.Supervisor(self.state, model="qwen3:4b")

    def assert_bad_job(self, **changes):
        job = self.job()
        job.update(changes)
        with self.assertRaises(REJECTED):
            self.supervisor().validate_job(job)

    def test_reads_regular_utf8_file_without_modifying_it(self):
        path = self.root / "solution.js"
        before = path.read_bytes()
        self.assertEqual(executor.safe_read(self.root, "solution.js"), before.decode())
        self.assertEqual(path.read_bytes(), before)

    def test_missing_source_file_is_rejected_when_read(self):
        with self.assertRaises(REJECTED):
            executor.safe_read(self.root, "missing.js")

    def test_rejects_absolute_and_traversal_paths(self):
        outside = self.base / "outside.txt"
        outside.write_text("SYNTHETIC_CANARY")
        for name in (str(outside), "../outside.txt", "nested/../../outside.txt"):
            with self.subTest(path=name), self.assertRaises(REJECTED):
                executor.safe_read(self.root, name)

    def test_rejects_symlink_file(self):
        (self.root / "alias.js").symlink_to(self.root / "solution.js")
        with self.assertRaises(REJECTED):
            executor.safe_read(self.root, "alias.js")

    def test_rejects_symlink_ancestor(self):
        directory = self.base / "other-project"
        directory.mkdir()
        (directory / "source.js").write_text("SYNTHETIC_CANARY")
        (self.root / "linked").symlink_to(directory, target_is_directory=True)
        with self.assertRaises(REJECTED):
            executor.safe_read(self.root, "linked/source.js")

    def test_rejects_hardlinked_file(self):
        os.link(self.root / "solution.js", self.root / "alias.js")
        with self.assertRaises(REJECTED):
            executor.safe_read(self.root, "solution.js")

    def test_rejects_directory_instead_of_file(self):
        (self.root / "directory").mkdir()
        with self.assertRaises(REJECTED):
            executor.safe_read(self.root, "directory")

    @unittest.skipUnless(hasattr(os, "mkfifo"), "FIFO unavailable")
    def test_fifo_is_rejected_without_waiting_for_writer(self):
        os.mkfifo(self.root / "pipe")
        code = (
            "import importlib.util,sys; from pathlib import Path; "
            "s=importlib.util.spec_from_file_location('le',sys.argv[1]); "
            "m=importlib.util.module_from_spec(s);sys.modules[s.name]=m;"
            "s.loader.exec_module(m)\n"
            "try:m.safe_read(Path(sys.argv[2]),'pipe')\n"
            "except (ValueError,OSError):sys.exit(42)\n"
            "sys.exit(0)\n"
        )
        result = subprocess.run(
            [sys.executable, "-c", code, str(SOURCE), str(self.root)],
            capture_output=True, timeout=3,
        )
        self.assertEqual(result.returncode, 42, result.stderr.decode(errors="replace"))

    def test_rejects_secret_and_git_paths(self):
        for name in (".env", ".env.production", ".git/config", "src/.env"):
            path = self.root / name
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text("SYNTHETIC_CANARY")
            with self.subTest(path=name), self.assertRaises(REJECTED):
                executor.safe_read(self.root, name)

    def test_read_size_limit_is_bytes_not_characters(self):
        (self.root / "large.txt").write_text("é" * 32769)
        with self.assertRaises(REJECTED):
            executor.safe_read(self.root, "large.txt")

    def test_valid_patch_can_update_subset_of_allowed_files(self):
        patch = {"files": {"solution.js": "module.exports = 42;\n"}}
        before = copy.deepcopy(patch)
        result = executor.validate_patch(patch, ["solution.js", "other.js"])
        self.assertIsInstance(result, dict)
        self.assertEqual(patch, before)

    def test_patch_rejects_empty_or_wrong_envelope(self):
        for patch in ({}, {"files": {}}, {"files": []}, {"files": {"solution.js": "ok"}, "command": "anything"}):
            with self.subTest(patch=patch), self.assertRaises(REJECTED):
                executor.validate_patch(patch, ["solution.js"])

    def test_patch_cannot_expand_file_scope(self):
        with self.assertRaises(REJECTED):
            executor.validate_patch({"files": {"other.js": "text"}}, ["solution.js"])

    def test_patch_rejects_non_text_and_oversized_content(self):
        for content in (None, 42, ["code"], "é" * 32769):
            with self.subTest(kind=type(content).__name__), self.assertRaises(REJECTED):
                executor.validate_patch({"files": {"solution.js": content}}, ["solution.js"])

    def test_patch_rejects_total_over_256_kib(self):
        files = {f"part{i}.js": "x" * 65536 for i in range(5)}
        with self.assertRaises(REJECTED):
            executor.validate_patch({"files": files}, list(files))

    def test_patch_rejects_unsafe_paths_even_if_in_allowlist(self):
        for name in ("../escape", "/absolute", ".env", ".git/config"):
            with self.subTest(path=name), self.assertRaises(REJECTED):
                executor.validate_patch({"files": {name: "data"}}, [name])

    def test_valid_authorized_job_is_accepted(self):
        result = self.supervisor().validate_job(self.job())
        self.assertIsInstance(result, dict)

    def test_authorization_requires_literal_true(self):
        for value in (False, None, 1, "true"):
            with self.subTest(value=value):
                self.assert_bad_job(approved=value)

    def test_expired_and_invalid_deadlines_are_rejected(self):
        for value in (time.time() - 1, 0, math.nan, math.inf, True, "tomorrow"):
            with self.subTest(value=value):
                self.assert_bad_job(expires_at=value)

    def test_job_identifier_is_bounded_and_not_a_path(self):
        for value in ("", "../escape", "task/one", "x" * 65, "white space", 1):
            with self.subTest(value=value):
                self.assert_bad_job(id=value)

    def test_revision_requires_positive_integer(self):
        for value in (0, -1, True, "1", 1.5):
            with self.subTest(value=value):
                self.assert_bad_job(revision=value)

    def test_state_cannot_be_used_as_source_project(self):
        self.assert_bad_job(root=str(self.state))
        child = self.state / "source"
        child.mkdir()
        (child / "solution.js").write_text("ok")
        self.assert_bad_job(root=str(child))

    def test_source_cannot_contain_state(self):
        (self.base / "solution.js").write_text("ok")
        self.assert_bad_job(root=str(self.base))

    def test_file_list_must_be_nonempty_unique_and_bounded(self):
        for files in ([], ["solution.js", "solution.js"], "solution.js"):
            with self.subTest(files=files):
                self.assert_bad_job(files=files)
        names = [f"file{i}.js" for i in range(9)]
        for name in names:
            (self.root / name).write_text("ok")
        self.assert_bad_job(files=names)

    def test_job_rejects_unsafe_source_paths(self):
        for files in (["../escape"], [".env"]):
            with self.subTest(files=files):
                self.assert_bad_job(files=files)

    def test_check_executable_must_be_allowlisted(self):
        self.assert_bad_job(checks=[["/usr/bin/curl", "https://example.invalid"]])
        self.assert_bad_job(checks=[["node", "solution.js"]])

    def test_checks_must_be_explicit_argument_arrays(self):
        for checks in ([], "node solution.js", ["node solution.js"], [[]], [["/bin/sh", 3]]):
            with self.subTest(checks=checks):
                self.assert_bad_job(checks=checks)

    def test_unadmitted_project_rejected_before_any_source_read(self):
        supervisor = self.supervisor()
        executor.atomic(self.state / "model.json", {"digest": "0" * 64, "projects": {}})
        path = self.state / "jobs" / "unadmitted.json"
        executor.atomic(path, self.job())
        with mock.patch.object(executor.sys, "platform", "darwin"), mock.patch.object(executor, "safe_read") as reader:
            with self.assertRaisesRegex(ValueError, "not admitted"):
                supervisor.process(path)
            reader.assert_not_called()


if __name__ == "__main__":
    unittest.main()
