# Local executor — restricted operation

Version 0.2.0 · 2026-11-10 · [Português](LOCAL_EXECUTOR_OPERATION.md) · [Español](LOCAL_EXECUTOR_OPERATION.es.md)

## Status and purpose

`com.engenharia-cadu.local-executor` is installed on the Mac under the Engenharia-Cadu
method. It uses local Ollama `qwen3:4b`, with no API key, download or paid fallback.
It completed a synthetic addition fix, passed three assertions and saved a candidate
as `REVIEW_REQUIRED`. This does not qualify a general coding agent or product projects.

Base: `~/Library/Application Support/Engenharia-Cadu-Agent`.
Source: `scripts/local_executor.py`; installer: `scripts/install_local_executor.py`.
Installation refuses overwrites. The user LaunchAgent requires the Mac to be on and
the user logged in. It cannot run on a powered-off Mac; 24-hour availability is unproven.

## Effective policy

- One supervisor and one task at a time, exclusive lock, idle heartbeat every five seconds.
- One attempt per ID; task/client inference/test deadlines: 240/90/20 seconds.
- At most eight existing files, 64 KiB each and 256 KiB total.
- Project and canonical root must match `state/model.json` before reading sources.
- Jobs in `state/jobs/` specify scope, instruction, trusted checks, revision and approval expiring within 24 hours.
- Only `synthetic-acceptance` is admitted; the queue contains the completed pilot only.
- Model output is JSON data. No shell, credentials, tools or MCP access is given to the model.
- Sources remain untouched; candidates are stored in `state/runs/<id>/work`.
- Tests see read-only candidates, a private writable temporary directory, no network and no process spawning.
- STOP, authorization/policy changes and deadlines stop the client. Failed jobs are not retried automatically.
- Restart marks RUNNING receipts INTERRUPTED without replaying uncertain effects.
- No automatic merge/deploy, self-review or activation of external agents.

## Operation

For an authorized Mac operator or connector; no need to repeat these to maintain the running service.

```sh
# Service status
launchctl print "gui/$(id -u)/com.engenharia-cadu.local-executor"
# Queue/current task
cat "$HOME/Library/Application Support/Engenharia-Cadu-Agent/state/heartbeat.json"
# Cooperative stop; wait for STOPPED
touch "$HOME/Library/Application Support/Engenharia-Cadu-Agent/state/STOP_REQUESTED"
# Explicit resume after checking receipts; removing STOP alone does not restart
rm -f "$HOME/Library/Application Support/Engenharia-Cadu-Agent/state/STOP_REQUESTED"
launchctl kickstart "gui/$(id -u)/com.engenharia-cadu.local-executor"
# Unload; retain files and evidence
launchctl bootout "gui/$(id -u)/com.engenharia-cadu.local-executor"
```

To disable next-login startup, after bootout move
`~/Library/LaunchAgents/com.engenharia-cadu.local-executor.plist` outside LaunchAgents.
Never delete receipts to repeat a task.

## Project and capability adoption

Use `CADU HOMOLOGAR AGENTE LOCAL` for qualification. Recover the project's backlog
and rules, pin the method revision, choose one small task, define checks independent
of editable content and persist authorization. Validate checks under this sandbox
before admitting the root. Builds requiring subprocesses or network are not qualified.

The supervisor selects skills, agents, MCPs and design systems per project, recording
origin, version, permissions and validation. Cataloguing is not installation or
qualification. This version does not install these integrations or grant them access;
the worker receives only instructions and allowed files. Design, accessibility,
UI tests and independent review remain separate gates; unit tests do not replace them.

## Evidence and limits

Probes denied external read/write, state access, symlinks, Xcode, networking and detached
spawn. This is not proof of absolute macOS confinement: system libraries and metadata
remain readable. Each temporary file is capped at 8 MiB; aggregate disk, memory and
threads have no strong quota. STOP does not prove instant cancellation inside Ollama.
Before/after digest checks do not make a model tag atomically immutable. Authorization
uses private operator files, not external-user authentication.

Local inference processes tokens without a billed API. Hardware, electricity and this
setup conversation are not included in a claim of zero cost.

Private evidence: `evidence/acceptance-2026-11-10` under the installed base.
[Technical receipt](LOCAL_EXECUTOR_ACCEPTANCE_2026-11-10.md).
