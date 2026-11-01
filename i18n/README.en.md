**English** · [Português (Brasil)](../README.md) · [Español](README.es.md)

# Engenharia Cadu

**From idea to delivery. Without losing direction.**

Turn your business vision into a product you can understand, review and improve. A way of working with AI agents: decisions before implementation, context that outlives a session, and evidence before anything is called done.

You bring the problem, the brief and the references. The method structures the next decision. The agent works within the authorized scope. Your project keeps the requirements, the code and the evidence of what happened.

[START A PRODUCT →](../p/P01.md) · [ORGANIZE AN EXISTING PROJECT](https://github.com/carlosemox/engenharia-cadu-adocao) · [PREPARE YOUR ENVIRONMENT](../p/P07.md) · [OPEN THE WEBSITE](https://carlosemox.github.io/engenharia-cadu/en/)

Codex leads · selective collaboration · design in the brief · context efficiency · security throughout the work.

> The presentation is available in three languages. Brazilian Portuguese is the editorial baseline for Engenharia Cadu. Linked procedures and guides retain their current languages; the S01 universal security prompt is in English. Selecting a language here does not automatically translate or change the underlying commands.

<!-- section:historia -->
## 00 / An idea should not get lost between conversations

A project begins with a clear vision. Then come references, screens, libraries, integrations and new decisions. The code grows. But when a session ends or another tool takes over, one question returns: **what has been decided, what actually works, and where do we continue?**

Engenharia Cadu is structured around that problem: give decisions a home and development a clear path. It does not ask you to discard what you have built. It asks for a shared understanding of the intent, boundaries for each change, and results that can be checked.

The goal is not to produce documents for their own sake. It is to turn conversations into useful knowledge, ideas into requirements, and tasks into verifiable outcomes. One philosophy for starting from scratch, recovering projects and developing reusable capabilities.

**Your business defines the product. Engineering organizes the work. The tool does not decide on its own what your company should become.**

<!-- section:comecar -->
## 01 / Start where you are

**New: [prompt factory](../fabrica/README.md) and [CADU universal entry](../comando.md).** Use the Portuguese procedures to reconcile attached studies, take over an existing project, or repair and restructure it within the authorized scope.

| Your situation | Entry point | First outcome |
|---|---|---|
| I have an idea or a brief | [P01 — Product discovery](../p/P01.md) | Shared understanding, material gaps and direction for the first version. |
| I already have an application | [Project adoption](https://github.com/carlosemox/engenharia-cadu-adocao/blob/main/read.md) | A project portrait and reviewable plan before changing code, structure or data. |
| I need to prepare my machine | [P07 — Environment and capabilities](../p/P07.md) | An inventory of what exists and configuration of what is authorized. |
| I need one specific task | [P00 — Choose a path](../p/P00.md) | The relevant procedure, without running the entire method. |

### New project: a brief is a starting point, not wasted work

Paste this into the agent conversation and describe your product on the second line. When you already have a brief, provide its text or file in that same conversation.

```text
Read https://raw.githubusercontent.com/carlosemox/engenharia-cadu/main/p/P01.md
Project: [name, problem, audience, main journey and constraints]. Use my existing brief, validate only the gaps and lead the next authorized stages in CONTINUO_SUPERVISIONADO. Respond in English.
```

Starting at P01 does not mean repeating every question. The agent reuses valid decisions and research, clarifies what is missing and moves the work forward. It does not skip discovery just because it finds a file named brief.

### Existing project: understand it before changing it

```text
Read https://raw.githubusercontent.com/carlosemox/engenharia-cadu-adocao/main/read.md
Understand this project, reconcile its brief, PRD, TRD and flows, and present the Project Portrait and Adoption Plan before changing code, files or databases. Respond in English.
```

You should see what the product is meant to do, what has been implemented, what has been demonstrated and what remains unknown. Useful architecture, identity, contracts and local work are preserved. A rewrite or migration must not be disguised as housekeeping.

### Environment: configuration is not an assumption

```text
Read https://raw.githubusercontent.com/carlosemox/engenharia-cadu/main/p/P07.md
Inventory this environment and prepare only the configurations authorized for my project. Distinguish installed, configured, accessible and verified. Respond in English.
```

These are instructions for an agent, not shell commands. Reading, editing and execution depend on available tools and permissions. None of these shortcuts automatically publishes your application.

<!-- section:metodo -->
## 02 / Shape the product before growing the codebase

Engineering starts with the business question: **who needs to do what, in which situation, and with what result?** The answer guides scope, interface, data and operations.

| Deliverable | Purpose |
|---|---|
| Brief and scope | Establish the problem, audience, value, first version, constraints and exclusions. |
| PRD — product requirements | Specify behavior, rules, permissions, exceptions and acceptance criteria. |
| Flows and design system | Define coherent journeys, components, feedback and accessibility. |
| TRD — technical design | Set architecture, data, contracts, integrations and recovery boundaries. |
| Incremental delivery plan | Choose useful units of work, dependencies, owners and checks. |

**Design is not decoration added at the end.** Direction begins in the brief (D0), becomes rules and components in the specification (D1), and is checked in the implemented interface (D2). A beautiful screen that does not serve the journey has not completed the task.

Market references inform choices; they do not automatically approve features. Studying a product, integrating its API and reusing licensed code are different decisions. Record sources and limitations, then build a distinct proposition that fits your operations.

<!-- section:integracoes -->
## 03 / Choose dependencies before relying on them

Live classes, payments, authentication, messaging and storage should not become surprises halfway through implementation. First define the capability. Then compare **building, reusing, buying, integrating or deferring**.

[P08](../p/P08.md) separates development tools from services that belong to the product. For each service, document requirements, the contract, shared data, access, verified or pending costs, limits, fallback behavior and replacement conditions.

A learning platform, for example, may manage enrollment and scheduling while an external service hosts the class. That integration may be the initial solution—or remain the better choice. Owning all the infrastructure is not a mandatory destination.

Supabase can be part of the architecture when selected. That does not authorize replacing authentication, recreating databases or migrating existing data. Frameworks, databases and ORMs follow product needs and decisions, not a stack imposed by this library.

<!-- section:agentes -->
## 04 / One coordinator. Accountable collaboration.

**Codex is the primary executor in this method.** Antigravity, Gemini CLI and OpenCode are potential collaborators, selected for the task and their observed capabilities. There is no requirement to open four agents for a simple change.

Every delegation carries an objective, sufficient context, allowed files and resources, dependencies, acceptance criteria and a return format. Shared resources have a responsible owner. Reviewers work read-only; the coordinator checks the integration.

Product, architecture, design, frontend, backend, quality, GUARDIAN, SENTINEL and release are documented responsibilities, not an automatically installed team. A catalogued skill still needs provenance, license review, compatibility and a test in the selected client.

[Explore the roles](../agentes/README.md) · [Select capabilities](../catalogo/README.md) · [Understand the clients](../integracoes/CLIENTES.md)

<!-- section:continuidade -->
## 05 / The next stage should not need another pasted command

In **CONTINUO_SUPERVISIONADO**—supervised continuous mode—the coordinator completes the stage, checks delivery, security and relevant backup evidence, records the state, and loads the next authorized procedure. The interview remains interactive. Material decisions remain yours.

```text
Understand → specify → prepare → implement → test → review → validate
                       ↑                      ↓
                       └──── fix and verify ──┘
```

P13, P14 and P15 form cycles for each increment. P17 covers an extended mission when a supervisor and its prerequisites have been demonstrated; it is not a mandatory step after every delivery. Specialized procedures are selected by need, not by their position in a list.

Blocking failures, pending decisions, serious risks, missing required protection or exhausted limits stop the dependent action. Independent, already-authorized work may continue. The agent does not invent tasks to keep the session busy.

**A prompt does not keep a computer working after the session ends.** Extended autonomy needs a real process, a queue, limits, exclusive ownership, checkpoints, stopping behavior and tested recovery. [Read the continuity policy](../politicas/CONTINUIDADE.md).

<!-- section:documentos -->
## 06 / Let knowledge outlive the session

In this method, harness engineering means organizing the agent's working environment: discoverable instructions, clear sources, accessible tools and verifiable feedback. Important knowledge belongs in the project, not only in the memory of a conversation.

| Information | Where it belongs |
|---|---|
| How to start and run | The application's README. |
| What the product must do | Canonical brief and PRD. |
| How the parts connect | TRD, contracts and architecture decisions. |
| How people use the product | Flows and design system. |
| How the agent should work | A short AGENTS.md that points to details. |
| What changed and how to continue | Relevant evidence, decisions and handoff. |

This is not a mandatory folder tree. For an existing project, preserve equivalent documents and record the mapping. A behavior, schema or command change should update its responsible source. Do not turn AGENTS.md into an encyclopedia.

The public method stores recipes. Each application stores its product. Private operations store profiles and internal records—never passwords or tokens in Git files. [Explore the templates](../templates/README.md).

<!-- section:auditoria -->
## 07 / Security before, during and before release

An audit at the end cannot replace good decisions at the beginning. The method includes requirements and threats in the design, checks throughout implementation batches, and a review of the candidate before each release.

| Milestone | What needs examination |
|---|---|
| Beginning | Data, identity, permissions, exposure, trust boundaries and required controls. |
| During development | Changes, callers, secrets, dependencies, regressions, allowed and denied behavior. |
| Integration | Isolation across modules or tenants, shared rules and external effects. |
| Before release | Findings, coverage, review, configuration and recovery for the same candidate version. |

**[S01](../modulos/seguranca/README.md)** preserves the universal audit prompt. Its modes are distinct: AUDIT inspects; PLAN prepares remediation; FIX changes only the authorized batch; VERIFY rechecks. The advanced campaign requires an explicit request. Active testing and production require their own authorization.

Hook examples cover project start, module completion, phase exit, integration, commit, push, pull requests, pre-release and periodic maintenance. **They are published examples, not hooks installed in your applications.** The receipt validator checks records; it is not a scanner and does not prove that submitted results are truthful.

No tool guarantees the absence of intrusion. Missing tests, errors, timeouts and stale evidence are not approval. Essential controls need real implementation, review and maintenance. [Hooks and limitations](../modulos/seguranca/hooks/README.md) · [Security policy](../politicas/SEGURANCA_ENGENHARIA.md).

<!-- section:backup -->
## 08 / Preserve the work. Prove you can recover it.

The designated location is `Projetos 2026/Backup/<project-name>`. Protection requires more than a created folder: explicit coverage, identifiable generations, checked integrity and tested recovery for the relevant scope.

Working files and local changes, Git history, databases, uploads and secrets are different recovery classes. A code ZIP does not demonstrate all of them. Credentials need specific protection; they do not belong in an ordinary archive. The method does not authorize automatically deleting previous generations.

Backups should precede risky changes and accompany deliveries with new artifacts. When required protection has not been demonstrated, the dependent action does not proceed. **Automatic Drive integration must be configured and tested in each environment; publishing this page does not activate it.** [Backup policy and coverage](../politicas/BACKUP_DRIVE.md).

<!-- section:economia -->
## 09 / Save context, not judgment

The Astra efficiency policy is a working discipline: load only what the task requires, reuse valid decisions, use scripts for repetitive checks and delegate when there is a concrete benefit.

Details remain available at the source. An implementer receives relevant requirements and contracts, not every document. A reviewer receives the candidate and its context, not the full history. Waiting for CI does not require repeated model calls.

We do not promise a savings percentage. Tokens, cost and rework should be measured when observable. There is no silent switch of model, provider, authentication or billing. The objective is **lower cost per accepted delivery**, including the necessary tests and corrections. [Efficiency policy](../politicas/ECONOMIA_ASTRA.md).

[Interactive library in Portuguese](https://carlosemox.github.io/engenharia-cadu/biblioteca.html)

<!-- section:prompts -->
## 10 / One command for each responsibility

Use the full library as a map, not as one enormous prompt. IDs stay stable; each procedure states its purpose, inputs, boundaries, deliverable and completion criteria.

| Prompt | Responsibility |
|---|---|
| [P00](../p/P00.md) | Choose the path and next action. |
| [P01](../p/P01.md) | Understand the product and validate the initial brief. |
| [P02](../p/P02.md) | Research hypotheses, references and feasibility. |
| [P03](../p/P03.md) | Consolidate the first version, scope and exclusions. |
| [P04](../p/P04.md) | Define requirements, rules and acceptance criteria. |
| [P05](../p/P05.md) | Specify flows, experience and the design system. |
| [P06](../p/P06.md) | Define architecture, data, contracts and security. |
| [P07](../p/P07.md) | Inventory and prepare the machine, accounts and clients. |
| [P08](../p/P08.md) | Select agents, tools, services and APIs. |
| [P09](../p/P09.md) | Prepare a new product's foundation and repository. |
| [P10](../p/P10.md) | Configure approved environments, CI and integrations. |
| [P11](../p/P11.md) | Demonstrate readiness for the next work. |
| [P12](../p/P12.md) | Turn requirements into bounded tasks. |
| [P13](../p/P13.md) | Implement and verify one task. |
| [P14](../p/P14.md) | Review independently according to risk and evidence. |
| [P15](../p/P15.md) | Validate journeys and integrations in staging. |
| [P16](../p/P16.md) | Prepare or execute an authorized release. |
| [P17](../p/P17.md) | Run an extended mission with a demonstrated supervisor. |
| [P18](../p/P18.md) | Resume without losing or duplicating work. |
| [P19](../p/P19.md) | Prioritize ongoing or stalled projects. |
| [P20](../p/P20.md) | Diagnose a project without rewriting it. |
| [P21](../p/P21.md) | Repair and adopt the method incrementally. |
| [P22](../p/P22.md) | Audit agents, skills and packages before activation. |
| [P23](../p/P23.md) | Structure reusable modules with real consumers. |
| [P24](../p/P24.md) | Evaluate harness improvements without weakening controls. |
| [P25](../p/P25.md) | Develop auditable financial capabilities. |
| [P26](../p/P26.md) | Organize content and publishing by brand. |
| [P27](../p/P27.md) | Build programmatic video capabilities. |
| [P28](../p/P28.md) | Structure engineering and construction capabilities. |

<!-- section:capacidades -->
## 11 / Adopt what you need. Preserve what works.

The catalog is a set of possibilities, not a bulk installation. Each skill, library or integration should be selected for need, provenance, license, compatibility, cost and validation. Consulting current documentation does not authorize sending private code or information to third parties.

| Location | Responsibility |
|---|---|
| Machine and client | Runtime, tools, authentication and authorized global integrations. |
| Application | Code, dependencies, lockfiles, documentation, tests and specific configuration. |
| Public central repository | Method, procedures, templates and publishable references. |
| Private operations | Profiles, authority limits, destinations and internal evidence, with no secrets in Git. |

Existing projects preserve their stack, database, contracts and working equivalents. Incompatible changes need a separate decision. Monorepos require an inventory of boundaries and shared resources. New services belong only where they have a concrete role in the product.

<!-- section:operacao -->
## 12 / Know what is published—and what still needs proof

**An available document is not a completed installation. A local test is not a production integration.** This central repository provides recipes, templates and examples; each environment must demonstrate its operation.

| Capability | Status and condition |
|---|---|
| P00–P30 and S01 | Published library (P00–P30); effectiveness in your project needs execution and evaluation. |
| Stage continuity | Coordinator instructions; depends on the session, context and authorization. |
| Security hooks and controls | Examples and policies; actual installation and blocking behavior need tests. |
| Automatic backup | Defined policy; connection, coverage and restoration need implementation. |
| 24-hour mission | Requires a demonstrated supervisor, limits, resources and recovery. |
| Three-language presentation | Translated presentation; linked guides and commands retain their current languages. |

Without environment access, an agent can explain and specify, but cannot prove configuration. Execution reports should separate PASS, FAIL, NOT_RUN and not applicable, with reasons. Security is not a promise of invulnerability.

[Operational status](../OPERACAO.md) · [Central map](../MAPA_DA_CENTRAL.md) · [Evaluation scenarios](../avaliacoes/CENARIOS.md) · [S01 validation](../modulos/seguranca/validacao/RESULTADOS.md)

<!-- section:evolucao -->
## 13 / Build a foundation that can evolve

When a project reveals an improvement, extract the reusable part, remove internal data, check the license and review it before adding it to the public method. Updates stay in their canonical sources; new subjects receive a distinct home. Private operations are not automatically mirrored.

Engenharia Cadu draws inspiration from the organization of **[Vibe Coding Toolkit, by Matheus Gomes](https://github.com/soumatheusgomes/vibe-coding-toolkit)** and adapts that reference to this central repository's decisions. No affiliation or endorsement is implied. The toolkit's license notice is preserved; other components retain their own terms. This repository does not automatically inherit an MIT license for all its content. [Licensing and attribution](../LICENCIAMENTO.md).

The best starting point is the next useful outcome: understand the product, recover a journey or prepare a verifiable foundation. Choose an entry point, provide your context and keep important decisions visible.

**Define with intent. Build with context. Evolve with evidence.**

[START WITH P01 →](../p/P01.md) · [RECOVER A PROJECT](https://github.com/carlosemox/engenharia-cadu-adocao) · [REPORT AN ISSUE](https://github.com/carlosemox/engenharia-cadu/issues)
