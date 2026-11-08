#!/usr/bin/env python3
"""Read-only CLI diagnostics. Never runs a model or exports raw auth output."""
import argparse
import json
import os
import re
import shutil
import subprocess


def check(binary="codex", *, runner=subprocess.run, locate=shutil.which, env=None):
    env = os.environ if env is None else env
    result = {
        "schema_version": 1,
        "status": "BLOCKED_CLI_MISSING",
        "cli_version": None,
        "auth_mode": "UNKNOWN",
        "api_environment_present": any(bool(env.get(k)) for k in
                                       ("OPENAI_API_KEY", "CODEX_API_KEY")),
        "model_access": "NOT_TESTED",
        "quota": "NOT_VERIFIED",
        "isolation": "NOT_TESTED",
        "unattended_ready": False,
        "model_calls": 0,
    }
    executable = locate(binary)
    if executable is None:
        return result
    try:
        version = runner([executable, "--version"], capture_output=True,
                         text=True, timeout=15, check=False)
        match = re.fullmatch(r"codex-cli (\d+\.\d+\.\d+(?:[-+][\w.-]+)?)",
                             (version.stdout or "").strip())
        if version.returncode != 0 or not match:
            result["status"] = "BLOCKED_CLI_VERSION"
            return result
        result["cli_version"] = match.group(1)
        login = runner([executable, "login", "status"], capture_output=True,
                       text=True, timeout=15, check=False)
        output = (login.stdout or "") + "\n" + (login.stderr or "")
        if login.returncode != 0:
            result["status"] = "BLOCKED_AUTH_OR_STATUS_ERROR"
        elif output.strip() == "Logged in using ChatGPT":
            result["auth_mode"] = "CHATGPT"
            result["status"] = ("BLOCKED_API_ENVIRONMENT" if
                                result["api_environment_present"] else
                                "CHATGPT_CREDENTIALS_PRESENT")
        elif "api key" in output.lower():
            result["auth_mode"] = "API_KEY"
            result["status"] = "BLOCKED_PAID_API_ROUTE"
        else:
            result["status"] = "BLOCKED_UNKNOWN_AUTH_MODE"
    except (OSError, subprocess.TimeoutExpired):
        result["status"] = "BLOCKED_CLI_CHECK_ERROR"
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--codex-bin", default="codex",
                        help="Trusted Codex executable, name or absolute path")
    args = parser.parse_args()
    result = check(args.codex_bin)
    print(json.dumps(result, indent=2))
    return 0 if result["status"] == "CHATGPT_CREDENTIALS_PRESENT" else 2


if __name__ == "__main__":
    raise SystemExit(main())
