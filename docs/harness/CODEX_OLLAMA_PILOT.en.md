# Codex + Ollama on Mac

[Português](CODEX_OLLAMA_PILOT.md) · [English](CODEX_OLLAMA_PILOT.en.md) · [Español](CODEX_OLLAMA_PILOT.es.md)

Version / updated: **1.3.0 · 2026-11-08T21:40:46-03:00 · America/Sao_Paulo**

**PREPARATION APPROVED — OPERATIONAL VALIDATION PENDING.**

Cadu approved the preparation, organization, translation and publication of this increment. The Mac was selected as the executor; it is powered off and unavailable for installation. This approval does not turn documentation checks into model tests.

## Graphify — scoped validation

**CONNECTION AND INDEXING VALIDATED; FULL ECOSYSTEM VALIDATION PENDING.**

Reinstalling from the workspace and verifying the administrator account repaired the GitHub link. The dashboard now recognizes 69 repositories in the authorized personal account. Installations in separate organizations have not been verified.

| Check | Observed result |
| --- | --- |
| GitHub association with the Engenharia Cadu workspace | PASS |
| Recognized repositories | 69; recognition does not mean indexing |
| Observed builds | 3 successful, 0 failed and 0 in flight |
| engenharia-cadu | Indexed; 493 nodes; revision c3a930148c73532af47cfa678065a1da0b977e40 |
| Dashboard aggregate | Approximately 11.9 thousand nodes across the three builds |
| Real Codex/MCP query | NOT_RUN; account connection does not prove a query |
| Indexing all 69 repositories | BLOCKED_PLAN; not completed |
| Supervisor, Ollama and Mac isolation | Not installed/tested in this delivery |

The Free dashboard rejected additional activations with a three-repository limit and reported a 25,000-node limit per repository. Do not assume that completing a build frees a slot: the message also asks to disable a repository or change plans. We did not disable valid indexes to bypass this limit. No paid plan was purchased. The authorized installation retains access to all repositories in the account, with read access to issues/metadata and read/write access to checks, code and pull requests; this does not authorize autonomous changes.

Evidence observed in the authenticated browser: [workspace builds](https://app.graphify.com/engenharia-cadu/builds). Validation covers the observed results and identified revision, not this publication's new commit, other repositories or the provider's overall security. Private repository names and credentials are omitted from this public publication.

Next gate: test an authenticated Codex/MCP query against the ready index, checking the symbol and location against the indexed revision. Then define coverage and budget before upgrading the plan. External agents remain candidates without presumed individual validation.

## Architecture and costs

Codex handles coding tasks; Ollama runs a local model; the supervisor coordinates the queue, limits, independent review and evidence. A local model is not the OpenAI model used by Codex with ChatGPT.

No API or new subscription was purchased. The previous BRL 50.00 proposal remains an inactive alternative, with no spending approval. Local inference has no per-token API charge, but uses hardware, electricity and storage. No automatic fallback to cloud or paid APIs. Model, license and tool-use capability require validation.

## Evidence and limits

| Item | Observed status |
| --- | --- |
| Preparation regression suite | 184 Python tests passed |
| Independent review | Preparation reviewed; corrections incorporated |
| GitHub | carlosemox account confirmed; API reported admin/push/pull permissions |
| Codex CLI | Version 0.167.0 installed only in the temporary environment |
| ChatGPT login | Credentials recognized; no secret value exported |
| OpenAI model access | Minimal call timed out after 60 seconds; access and quota not verified |
| Mac | Selected by the user; hardware and macOS not inspected; device not connected |
| Ollama on Mac | Installation, model and integration not verified |
| Supervisor outside the conversation | Neither activated nor operationally validated |
| External agents | Cataloged; no presumed individual validation |

The environment inspected in this conversation is temporary Linux, limited to 8 GiB RAM and eight CPUs by quota, with 57.7 GiB free disk observed and nvidia-smi unavailable. These figures do not describe the Mac. Ollama was not installed there. OPENAI_API_KEY and CODEX_API_KEY were absent or empty.

## Later installation on Mac

1. Connect the Mac and record processor, RAM/VRAM, free space, macOS and existing installations.
2. Select verified Codex and Ollama versions and a local model with a suitable license, tools and recorded digest.
3. Configure loopback only, cloud disabled and a context window that fits memory. Ollama documentation recommends at least 64k tokens for Codex; the machine must support that requirement.
4. Validate local responses, tools, isolation, timeout, stop, recovery and absence of duplicate effects in a fixture without secrets.
5. Complete a small fix in a disposable checkout, run tests and obtain independent diff review. Measure time and memory.
6. Integrate with the supervisor and test persistence and scheduling only after the gates pass. This pilot does not authorize self-approval, application merges/deployments or certification of the entire catalog.

## Prepared commands, not yet run on Mac

Start only if no server already exists. Otherwise inspect its configuration and restart the appropriate service without creating a duplicate.

```sh
OLLAMA_NO_CLOUD=1 OLLAMA_HOST=127.0.0.1:11434 OLLAMA_CONTEXT_LENGTH=65536 ollama serve
```

Replace MODEL_NAME with the exact installed model name. Context size is a test target, not a guarantee of sufficient memory.

```sh
codex exec --oss --local-provider ollama --model MODEL_NAME --sandbox read-only -c 'web_search="disabled"' 'Reply CADU_OLLAMA_OK without using tools.'
```

Local Ollama does not sandbox agent commands. Actual sandbox enforcement must be tested on the Mac. Do not copy personal ChatGPT authentication into the public CI workflow.

## Access checker

`python scripts/check_codex_access.py` checks only version and login; it accepts `--codex-bin` for a trusted executable. It does not read auth.json directly, export raw output, call a model or start a service. Credentials do not prove connectivity, quota, model access or isolation. This diagnostic covers the ChatGPT route; local Ollama does not require OpenAI login.

## Next milestone

**MAC_CONNECTED → HARDWARE_CHECKED → LOCAL_MODEL_TESTED → ISOLATION_VERIFIED → PILOT_REVIEWED.** Publishing this page completes the approved preparation, not operational validation.

## References

- https://learn.chatgpt.com/docs/auth
- https://learn.chatgpt.com/docs/non-interactive-mode
- https://learn.chatgpt.com/docs/cli/reference
- https://docs.ollama.com/integrations/codex
- https://docs.ollama.com/faq
