# Validate an independent local agent
Version 0.2.0 — 2026-11-10 — qualification procedure.

A restricted synthetic installation is available: [operation and limits](../docs/harness/LOCAL_EXECUTOR_OPERATION.en.md). This procedure does not automatically admit real projects.

[Português](HOMOLOGAR_AGENTE_LOCAL.md) · [English](HOMOLOGAR_AGENTE_LOCAL.en.md) · [Español](HOMOLOGAR_AGENTE_LOCAL.es.md)

## Instructions for the Codex conversation on the Mac
Prepare and validate the current project's executor without depending on JARVIS.
Use the selected Mac app environment. Read applicable instructions, pin
Engenharia-Cadu to a SHA, and recover the existing code, state and backlog.
Do not read or modify JARVIS or create another central queue. Reuse an existing
independent executor; if none exists, report BLOCKED_EXECUTOR_NOT_FOUND and propose
the smallest integration before implementing it.

Incremental API budget: BRL 0.00. Inference must run locally through Ollama.
DeepSeek is only a candidate local model. No OpenAI/ChatGPT inference, DeepSeek API,
Ollama Cloud, paid search or remote fallback may power the pilot. Preparation in
this conversation does not prove this restriction. Local models process tokens
without API billing; hardware, electricity and storage remain necessary.

1. Inspect hardware, installed versions, processes, model/digest/license, tool
compatibility and effective configuration. Preserve working installations and
personal/global settings. Do not duplicate services or print secrets. Check the
installed CLI help before choosing commands.
2. Use a disposable fixture without real data. Persist scoped authorization,
expiry, limits and revocation. A worktree, prompt or path validator is not a
sandbox. Prove host controls for reads, writes, subprocesses and network.
Allow loopback inference only; deny worker internet during this pilot. Any model
download is a separate reviewed setup step.
3. Run the acceptance matrix, starting with negative boundary tests and synthetic
canaries. Failed isolation blocks real projects. Store sanitized evidence privately;
a completed receipt does not itself prove enforcement.
4. Pilot limits: one executor, one task, 15 minutes, 20 tool turns, no automatic
restart after failure. Use an existing fixture or the matrix's deduplication task.
The agent must edit code and pass unchanged tests. Capture diff, logs, exit codes,
duration, model and network observations. On timeout terminate the process tree
and confirm it stopped. Unobservable limits/network mean INCONCLUSIVE.
5. Request independent review of the same revision and evidence. Missing review
is NOT_RUN. Only after gates L01–L11 pass, run one small authorized backlog task in an
isolated branch. Recover the target from context; never substitute another project
or production to bypass a blocker.
6. Reuse existing continuity mechanisms; verify heartbeat, single lease,
checkpoint, STOP, revocation, crash and recovery without repeating uncertain
effects or failed runs. First observe a window of at most 60 minutes and three
approved tasks, WIP=1, keeping task limits. Empty queue ends execution.
Persistent operation requires this window to pass and an effective configuration,
stop and recovery record. Keeping a chat open does not prove 24-hour execution.
7. Update the checkpoint with PASS/FAIL/NOT_RUN/INCONCLUSIVE for every gate and
continue independent authorized work. No application merge/deploy in this pilot;
do not change acceptance criteria. Report the minimum remaining intervention.

This is a procedure, not a daemon. Mac access, executor and evidence must exist.
Chat connections do not transfer host credentials. Apply relevant backups before
editing real projects. See the [acceptance matrix](../docs/harness/LOCAL_AGENT_ACCEPTANCE.md)
for gate identifiers and the fixture specification.

