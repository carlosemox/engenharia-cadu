# Development environments and agents — V1

## Mandatory gate

At the start of a session or when taking over a project, confirm:

1. **Terminal** — direct CLI, Git, scripts and tests.
2. **Computer/Mac application** — local IDE or application with interactive editing and visual review.
3. **Cloud Code** — VS Code, IntelliJ/JetBrains or Cloud Shell, especially for Cloud Run, Kubernetes, GKE, APIs and Google Cloud resources.

Record the selected environment in the project state or checkpoint before writing code.

## Roles

| Capability | Primary use | Limit |
|---|---|---|
| Codex | Coordinate the mission, integrate changes, review evidence and decide the next node | Never assume another agent executed work without evidence |
| Cloud Code | Develop, run and debug cloud-native applications; configure Cloud Run/Kubernetes/GKE and Google Cloud services | Does not authorize deployment, project changes, billing or production |
| Gemini Code Assist/Gemini CLI | Pair programming, explanations, assisted generation, localized review and Google ecosystem tasks | Must not edit the same branch concurrently with another agent |
| Antigravity | Multi-step agentic tasks, browser, UI, artifacts, asynchronous execution and parallel agents | Use an isolated project/branch/worktree; review diff and artifacts before integration |

Cloud Code is an environment and integration layer; it is not a separate agent when Gemini Code Assist is used inside it.

## Coordination rule

Use all tools together only with distinct roles:

- one coordinator owns the objective, graph and integration branch;
- one executor owns writing each file or feature;
- reviewers work read-only or in a separate worktree/branch;
- every delivery returns diff, tests, risks and evidence;
- integrate only after review and verification.

Never allow two agents to write the same file or branch simultaneously. Do not start parallelism for a small task or when its gain cannot be measured.

## Practical routing

- **Product, domain, contracts and general integration:** Codex coordinates; terminal or local application executes.
- **Cloud Run, Kubernetes, GKE, Skaffold and Google Cloud APIs:** Cloud Code is the preferred environment; Gemini may assist inside the IDE.
- **Code research, second opinion or function review:** Gemini in review mode, without integration authority.
- **UI, browser, screenshots and complete flows:** Antigravity in an isolated branch/worktree, with verifiable artifacts.
- **Release, production, migrations and secrets:** only after an explicit gate, independent review and operational evidence.

## Recommended sequence

`IDENTIFY → CHOOSE ENVIRONMENT → ASSIGN OWNER → EXECUTE → TEST → REVIEW → INTEGRATE`

Official references: [Cloud Code](https://cloud.google.com/code), [Gemini Code Assist agent mode](https://docs.cloud.google.com/gemini/docs/codeassist/use-agentic-chat-pair-programmer), [Google Antigravity](https://www.antigravity.google/docs).
