import importlib.util
import json
from pathlib import Path
import subprocess
import unittest

spec = importlib.util.spec_from_file_location(
    "access", Path(__file__).resolve().parents[1] / "scripts/check_codex_access.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


class AccessTests(unittest.TestCase):
    def probe(self, auth="Logged in using ChatGPT", code=0, env=None):
        calls = []
        def runner(args, **kwargs):
            calls.append(args)
            self.assertEqual(kwargs["timeout"], 15)
            return subprocess.CompletedProcess(
                args, 0 if args[-1] == "--version" else code,
                "codex-cli 0.167.0" if args[-1] == "--version" else "", auth)
        result = module.check(runner=runner, locate=lambda _: "/trusted/codex",
                              env={} if env is None else env)
        self.assertEqual(calls, [["/trusted/codex", "--version"],
                                ["/trusted/codex", "login", "status"]])
        return result

    def test_subscription_is_not_runtime_verification(self):
        result = self.probe()
        self.assertEqual(result["status"], "CHATGPT_CREDENTIALS_PRESENT")
        self.assertFalse(result["unattended_ready"])
        self.assertEqual(result["model_access"], "NOT_TESTED")

    def test_no_binary_does_not_run(self):
        def forbidden(*args, **kwargs):
            self.fail("Missing binary must not run")
        self.assertEqual(module.check(locate=lambda _: None, runner=forbidden,
                                      env={})["status"], "BLOCKED_CLI_MISSING")

    def test_api_route_and_secret_never_exported(self):
        result = self.probe("Logged in using an API key: PRIVATE_SENTINEL")
        self.assertEqual(result["status"], "BLOCKED_PAID_API_ROUTE")
        self.assertNotIn("PRIVATE_SENTINEL", json.dumps(result))

    def test_ambient_api_key_blocks_subscription_route(self):
        result = self.probe(env={"OPENAI_API_KEY": "PRIVATE_SENTINEL"})
        self.assertEqual(result["status"], "BLOCKED_API_ENVIRONMENT")
        self.assertNotIn("PRIVATE_SENTINEL", json.dumps(result))

    def test_unknown_and_failed_auth_fail_closed(self):
        self.assertEqual(self.probe("new auth format")["status"],
                         "BLOCKED_UNKNOWN_AUTH_MODE")
        self.assertEqual(self.probe(code=1)["status"],
                         "BLOCKED_AUTH_OR_STATUS_ERROR")

    def test_negated_or_contradictory_auth_is_not_subscription(self):
        for output in ("Not logged in using ChatGPT",
                       "Logged in using ChatGPT\nLogged in using an API key",
                       "Logged in using ChatGPT\nUnexpected diagnostic"):
            self.assertNotEqual(self.probe(output)["status"],
                                "CHATGPT_CREDENTIALS_PRESENT")

    def test_timeout_does_not_export_exception(self):
        def runner(*args, **kwargs):
            raise subprocess.TimeoutExpired("PRIVATE_SENTINEL", 15)
        result = module.check(locate=lambda _: "/trusted/codex", runner=runner, env={})
        self.assertEqual(result["status"], "BLOCKED_CLI_CHECK_ERROR")
        self.assertNotIn("PRIVATE_SENTINEL", json.dumps(result))

    def test_unknown_version_fails_closed(self):
        def runner(*args, **kwargs):
            return subprocess.CompletedProcess([], 0, "PRIVATE_SENTINEL", "")
        result = module.check(locate=lambda _: "/trusted/codex", runner=runner, env={})
        self.assertEqual(result["status"], "BLOCKED_CLI_VERSION")
        self.assertNotIn("PRIVATE_SENTINEL", json.dumps(result))
