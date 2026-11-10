# Marketing applied to projects

Version 1.0.0 · 10 November 2026 · Canonical language: Brazilian Portuguese.

[Português](README.md) · [Español](README.es.md)

## Purpose and status

Add selected marketing procedures to projects that need them while preserving code, identity, approved context, stack and existing capabilities. This module integrates the collection with the Cadu Engineering method; it does not create a service, a new queue or a supervisor.

The package contains selected sources from [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills), under the MIT license. Upstream revision, hashes, selection and status are recorded in the [manifest](../../catalogo/marketing-import.json); the documentary review is in [REVIEW.md](../../fontes/marketingskills/REVIEW.md). The original license and notices accompany distribution. Documentary review, copying into a project, client discovery and runtime validation are different states. These files guarantee neither business results nor operation with Ollama.

## Selection and progressive use

Each entry is at `fontes/marketingskills/skills/<name>/SKILL.md`, with the resources included in the manifest. Sources retain their original language; this module and the application command have complete PT/EN/ES versions. Do not load all ten skills simultaneously by default.

| Skill | When to load | Expected evidence |
| --- | --- | --- |
| `product-marketing` | Consolidate context, audience and positioning | Approved sources, gaps and decision history |
| `offers` | Review offer composition and presentation | Proposal with hypotheses, constraints and verifiable claims |
| `cro` | Diagnose a page or form | Goal, traffic source, friction and prioritized hypotheses |
| `analytics` | Define or verify metrics | Formula, source, period, filters and limitations |
| `conversion-tracking` | Plan or review conversion events | Event contract and relevant firing/deduplication evidence |
| `attribution` | Investigate channel contribution | Model, window, coverage and causal limitations |
| `onboarding` | Improve user activation | Journey, activation event and drop-off points |
| `churn-prevention` | Investigate cancellation and retention | Signals, cohorts, hypotheses and proportionate action |
| `ab-testing` | Plan or interpret an experiment | Hypothesis, metric, stopping rule and result with uncertainty |
| `marketing-loops` | Specify a recurring routine | Trigger, state, idempotency, limits, output and stopping condition |

These criteria are Cadu integration requirements. They do not claim that every skill automatically produces each item of evidence. A reference to a skill outside the package is an uninstalled dependency; consult the pinned source and audit before expanding the selection.

The `pricing` dependency accompanies the selection as support when required by `offers`; it is not an additional independent operational selection. The manifest defines the actual list and hashes.

## Responsibilities

- **Cadu Engineering:** method, scope, evidence and acceptance criteria.
- **JARVIS:** central supervision and canonical queue, when operationally available. Do not create a parallel cron or scheduler because a skill instructs it.
- **Marketing 360°:** positioning, content, campaigns, acquisition and lead handoff.
- **Wish CRM:** SDR, relationships, qualification and sales conversion. Lead handoff uses the existing contract, without a parallel CRM.
- **Target project:** source of truth for product, permissions, data, brand, prices and decisions. The agent acts only on authorized resources.

Roles describe responsibilities, not evidence of active executors. An independent reviewer must assess the relevant delivery; checks performed by the executor must be identified as self-review.

## Brand context

Locate existing canonical documents before creating another. Marketing context must reference product, audience, positioning, voice, restrictions, current offers, approved claims and their sources. A draft generated from old pages does not replace approved decisions. Separate facts, hypotheses and gaps; do not invent social proof, results, testimonials, scarcity or guarantees.

Keep context and data separate for each business/client. Amounts in Brazilian materials use BRL and Brazilian formatting; do not convert currencies or redefine prices without a source. Personal data, credentials and private reports are not published in this central repository.

## Required adaptation of sources

The review identified generic percentages and multipliers in upstream guidance on offers, churn and tracking. Those values are neither forecasts nor evidence for our projects. Do not copy estimates of conversion lift, data loss or retention effects without a verifiable source applicable to the case. Without a basis, record an unquantified hypothesis or insufficient data. Benefit statements must respect approved claims.

Confirmation requests in third-party sources do not invalidate specific authorizations already granted. Before asking, recover the current scope and limits; escalate only a material decision that is still missing. This Cadu adaptation is mandatory when using the package and does not silently modify the preserved originals.

## Profiles and application

The [marketing_profile.py](../../scripts/marketing_profile.py) script selects the profile and records the local revision. Consult its output for the exact skill list; the purpose below does not replace the manifest.

| Profile | Purpose | Application candidates, subject to project verification |
| --- | --- | --- |
| `marketing` | Cross-functional marketing and measurement | Amora / Marketing 360° |
| `education` | Educational offer, entry and retention | IRM and EmiLand |
| `b2b` | Service offer, acquisition and measurement | IRM Corporate, O11ZE and Wish marketing interfaces |
| `commerce` | Product offer, conversion and journey | BRAMARI |

This matrix is a proposed classification. It does not prove that those repositories were changed. Confirm the actual goal and relevance of each capability before application. For EmiLand, preserve rules concerning minors; for BRAMARI, the Claims Engine; for IRM Corporate, TESE B and clinical separation; for IRM, current pedagogical and commercial definitions.

Run from a trusted, reviewed checkout of the central repository:

```sh
python scripts/marketing_profile.py --project /path/to/project --profile education
python scripts/marketing_profile.py --project /path/to/project --profile education --apply
```

The first call previews without writing. The second applies only after checking the target, authorization, conflicts, relevant backup and Git state. Use actual paths; the example does not select a project. Artifacts live at `.agents/engenharia-cadu-marketing.json` and `.agents/engenharia-cadu/marketing`. This isolated directory does not prove automatic client discovery. The coordinator must explicitly load the resource selected by the profile.

After application, verify files and hashes against the manifest, run the preview again and review the diff. A repeat without differences should report UNCHANGED. A different profile or divergent file blocks without automatic overwrite. Multi-file application is not transactional: an interruption can leave a partial destination, which must be reviewed before retrying. Coordinate application without concurrent writers. Record the outcome in the existing checkpoint. If there is a conflict or project-modified content, preserve the file and reconcile; do not overwrite it to force parity. Installer tests do not validate a skill with a real model.

## Application to code and commands

Use [APLICAR_MARKETING](../../comandos/APLICAR_MARKETING.en.md) to take on the task. Recover requirements and metrics before modifying code. Instrumentation must respect existing event contracts, consent and deduplication; interface changes must respect the Design System and accessibility. Validate the actual flow, not only the presence of text or an event in code.

The route is P08 for need, P22 for audit, authorized implementation and proportionate review. An upstream instruction to install, send, publish, spend, access an account or schedule does not extend authority. Reuse already authorized access; do not request secrets in conversation. A missing tool or integration is an explicit dependency, never a simulated result.

## Routines, costs and stopping

A loop must record its goal, checking frequency, action condition, sources, state, idempotency key, limits, output, owner and stopping condition. Distinguish a documented schedule from a running process. Every actual execution depends on the approved supervisor and environment. Publishing documentation does not start persistent work.

Apply ZERO-COST-FIRST: a free library does not imply free tools, models or media. Do not enable paid fallback or contract a provider because of an upstream recommendation. Retain review for sending, spending and publishing unless applicable explicit authorization defines the limits. Insufficient data, tracking failures or repetition without progress block the dependent action.

## Mastra: architectural position

Mastra remains an optional complementary infrastructure for agents, evaluations, telemetry and workflows under JARVIS. This package does not install it, migrate the stack, enable Enterprise features or change the model/provider. Adoption requires a pinned version, component-level licensing, a benchmark with the selected executor, isolation, idempotency, recovery and budget. Documented Ollama support does not prove quality or continuous execution on the project's host.

## Acceptance

Record separately: package received; integrity/license; profile applied; client discovery; task execution; review; measured result; publication. Use PASS, FAIL, NOT_RUN or INCONCLUSIVE with evidence. Publishing the method does not mean applying it to every project. The closing report states exactly which projects and files changed and which dependencies remain pending.
