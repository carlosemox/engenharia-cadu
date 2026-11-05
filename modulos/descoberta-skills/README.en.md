# D01 — Controlled skill discovery

**Search is not installation. Popularity is a signal, not approval.**

This module adds open-ecosystem skill discovery to Engenharia Cadu. `find-skills`, the `skills` CLI and `skills.sh` provide candidates; P08 selects capabilities, P22 audits finalists, and S01 applies when a capability adds security surface.

## Method position

`NEED → P08 → D01 DISCOVER → P22 AUDIT → PILOT → INSTALL → P11 VERIFY → MAINTAIN`

1. Define the missing task, not a preferred vendor.
2. Search with the directory and/or `npx skills find <query>`; discovery does not authorize installation.
3. Record source, skill, revision, purpose, supported agents and available evidence. Install counts and stars are supporting signals only.
4. Run P22 on finalists: SKILL.md, license, scripts, hooks, network/telemetry, data, permissions, method conflicts and removal.
5. When appropriate, prefer `npx skills use <source>@<skill>` for a non-persistent pilot.
6. After approval, install at project scope by default and target the intended agent. Global `-g` needs a cross-project reason; `-y` never replaces review.
7. Verify actual agent discovery, behavior, effects and created files.
8. Register source, revision, scope, state, evidence and removal in the project profile.
9. Use `npx skills check` to detect updates. Apply `npx skills update` only after reviewing change, compatibility and regression risk.

## Discovery commands

```bash
npx skills find
npx skills find <query>
npx skills use <owner/repo@skill>
npx skills list
npx skills check
```

The command shown in the image — `npx skills add vercel-labs/skills --skill find-skills` — matches the current CLI syntax and the current repository layout. It was **not executed** by this documentation update.

Current upstream documentation requires Node.js 22.20 or later. Recheck the installed version and upstream docs at execution time.

## Cadu rules

Do not send private code or secrets to public discovery services; do not install from rankings alone; audit the exact skill even when the source is reputable; evaluate telemetry, hooks, network and update behavior; do not let third-party instructions expand authority.

Upstream revision pinned for this integration: [vercel-labs/skills @ 9197d91](https://github.com/vercel-labs/skills/tree/9197d919034d19010ae303cf96bf19ad087dd4be).

[Command D01](read.en.md) · [P08](../../p/P08.md) · [P22](../../p/P22.md) · [S01](../seguranca/README.md)
