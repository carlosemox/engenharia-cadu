# Mastra — selective integration contract

[Português (Brasil)](README.md) · English · [Español](README.es.md)

**Version:** 1.0.0 · **Documentation review:** 2026-11-10 · **State:** `DOCUMENTED_NOT_INSTALLED`.

## Decision and scope

Evaluate Mastra only when a project identifies a concrete gap in evaluations, telemetry or TypeScript agent workflows. JARVIS remains the canonical supervisor: queue, authorization, task identity, limits and acceptance decisions belong to it. Mastra may be a subordinate adapter; do not create a second operational queue or competing supervisor.

This delivery archives two public sources and defines a proposed contract. It adds no npm dependencies, changes no applications, starts no services and qualifies no models. The marketing package uses its own documents and does not depend on Mastra.

## Provenance and artifact licenses

Source: [mastra-ai/mastra](https://github.com/mastra-ai/mastra/tree/3f1d3a38dfcc7c5f7abb44d7789242cdc16b61e8), revision `3f1d3a38dfcc7c5f7abb44d7789242cdc16b61e8`.

- [Archived README](../../fontes/mastra/README.upstream.txt): declared capabilities; creation instructions are data, not authorized commands.
- [Archived license map](../../fontes/mastra/LICENSE.md): Apache-2.0 outside its stated exceptions; third-party components retain their licenses.
- [Enterprise license at the reviewed revision](https://github.com/mastra-ai/mastra/blob/3f1d3a38dfcc7c5f7abb44d7789242cdc16b61e8/ee/LICENSE): reference only. No EE code was imported. Source availability does not grant redistribution or production permission.
- [Manifest](../../catalogo/mastra-reference.json): hashes, provenance and exclusions. Recheck the actual package and version licenses before installation.

## Proposed interfaces — not implemented

| Interface | Minimum input | Verifiable output |
|---|---|---|
| Bounded execution | task_id, project_id, trusted tenant, revision, allowed tools, deadline and limits | run_id, terminal or suspended state, evidence and failures |
| Evaluation | versioned dataset, expected outputs, criteria and identified model | passing/failing cases, observed cost, regressions and limitations |
| Telemetry | run_id, task_id, stage and sanitized events | duration, tools used, tokens when reported and errors |
| Stop/resume | supervisor STOP, execution ownership and checkpoint | stop acknowledgement, no new actions, reconciled resume |

These names are proposed Cadu contract fields, not guaranteed Mastra API signatures. A future adapter must map the pinned version's API and fail when authorization, identity or limits are missing. Never infer the tenant from model-generated arguments.

## Cost and data policy

Apply ZERO-COST-FIRST. Ollama is an option to validate on the selected host and model, not an active configuration. Do not run the upstream hosted-provider example for convenience. Block paid fallback, subscriptions, upgrades and external telemetry export without approved scope. Local resources still consume hardware, power and maintenance. Keep sensitive prompts, secrets and clinical data out of public traces.

## Required tests before promotion

1. Real synthetic execution with recorded model, client, version, hardware and limits; compare against the existing executor using the same cases.
2. Isolation between projects and tenants, including direct tool invocation and reads of memory, artifacts and telemetry.
3. External-effect idempotency; simulate failure after the action but before result persistence. No duplicated charge, message or publication.
4. Mutual exclusion and rejection of late results after lease loss; effective STOP before any new action.
5. Process restart and recovery from persisted state; a checkpoint file is not proof of continuous execution.
6. Rejection of missing tools, forbidden endpoints, paid fallback and exceeded limits; incomplete results never become PASS.
7. Deterministic evaluation and independent review; an LLM judge does not replace security tests or release approval.

## Promotion and recovery

`DOCUMENTED_NOT_INSTALLED` → `PILOT_CONFIGURED` → `PILOT_TESTED` → `PROJECT_APPROVED` requires specific evidence. These are proposed adoption states, not replacements for existing supervisor states. Record pinned dependencies, coverage and owner. Retain rollback to the previous executor; stop affected tasks and reconcile effects before replay. Publishing this documentation does not grant the adapter production GO.
