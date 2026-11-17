# MIKE — Untangle Codebase and Claude Code by Slices · V1.0
Updated 2026-11-17 · [Português](UNTANGLE_CLAUDE_SLICES.md) · [Español](UNTANGLE_CLAUDE_SLICES.es.md)

## Origin and governance
A governed adaptation of `caldoai/skills/skills/untangle-codebase/SKILL.md` (commit `bd73b2ea5eb854ab8f0553fb41f77c8786f28f82`, blob `102ff57803e504876f6eb9b412e4eb0f6c576350`, MIT, copyright 2026 Maze). It does NOT execute the original unrestricted “fix everything” instruction. This skill is an agent workflow, not a verified sandbox or independent analyzer.

Cadu authorizes product, scope, budget and release. **MIKE** is the development supervisor under Cadu's command, separate from JARVIS, maintaining the canonical queue, leases, owners, evidence and checkpoints. MIKE documentation does not prove a persistent daemon. Codex remains the technical default in existing Codex-led projects; Claude Code may execute approved work without replacing MIKE or introducing a second supervisor. Deny by default, least privilege, RBAC/ABAC/RLS as applicable, MFA/passkey, audit and rollback.

## Required workflow
1. **Harness:** verify repository, current HEAD/SHA, branch, previously agreed execution environment, decisions, tests, approvals, state and worktrees. Preserve existing work.
2. **Read-only selective Untangle:** inspect affected components only at project entry/resumption, when a new epic touches architecture, before a relevant PR or after recurrent structural incidents. Record hidden links, needless links, proven surplus and valid exceptions; show dependency graph with file:line/SHA evidence. Do not remove legitimate retries or security safeguards.
3. **Vertical slices:** each slice has a measurable outcome, interface contract, positive/negative tests, dependencies, exclusive ownership of files/schema/lockfiles/resources, estimated cost, approved ceiling and rollback. Use `templates/MIKE_SLICE_CONTRACT.json`.
4. **Graph:** READY runs only when dependencies PASSED; use a single executor by default. Parallel workers require disjoint resources and actual isolated worktrees/branches and services.
5. **P06 gate:** code changes require separate specific approval, worker isolation and verified permissions. Test/comment deletion needs separate explicit approval; this diagnostic skill grants no write authority.
6. **Loop:** GOAL → MINIMUM ACTION → OBSERVE → VERIFY → DECIDE; maximum three cycles per node, stop sooner on regression, secrets, budget or scope uncertainty.
7. **P07/P08:** authorized checks and independent read-only review of requirements, diff, evidence and rollback. No automatic merges, pushes, deployment, production changes, destructive migrations, billing or publishing.
8. **Checkpoint:** MIKE reconciles real diff/commit/PR, PASS/FAIL/NOT_RUN/INCONCLUSIVE results, observed cost, risk and next node. A worker's self-report is not proof.

## Model/cost routing
Deterministic tools first; Haiku 5.5 for bounded discovery; Sonnet 5.5 for ordinary slice planning, **one worker per approved slice**, and independent review. Escalate to Opus 5.5/Fable 5.2 only when necessary and separately budget-approved. Verified API IDs: `claude-haiku-5-5`, `claude-sonnet-5-5`, `claude-opus-5-5`, `claude-fable-5-2`. Validate client availability. Measure total **cost per accepted slice**, including review and retries. API prices, subscriptions and local Ollama are not interchangeable. ZERO-COST-FIRST; never bypass quotas or incur new costs without consent.

## Claude Code rollout
The central repository provides `CLAUDE.md`, `.claude/skills/cadu-untangle/SKILL.md` and `.claude/agents/`: Haiku scout/read-only; Sonnet architect/read-only; Sonnet 5.5 slice-builder (approved isolated edits only); Sonnet 5.5 independent reviewer/read-only. Use plan/default permissions, never bypass by default. Experimental agent teams are OFF unless proven beneficial and authorized; they are not MIKE's persistent runtime. Other repositories require their own inventoried, reviewed adoption and SHA; this central commit does not install anything there. No scheduled LLM polling is created.

Commands: [MIKE Claude Slices](../comandos/MIKE_CLAUDE_SLICES.en.md). Contract: [JSON template](../templates/MIKE_SLICE_CONTRACT.json). **State:** SPEC_CREATED; runtime and external adoption NOT_RUN.
