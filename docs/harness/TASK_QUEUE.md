# Fila canônica

Único bloco JSON consumido pelo roteador. Status e autorizações são declarações revisáveis, não credenciais. Sem READY autorizado no fechamento deste lote; os próximos gates são explícitos.

```json
{
  "version": 1,
  "mode": "CONTINUOUS_CONTROLLED_LOOP",
  "client": "CODEX",
  "environment": "CLOUD_CODE",
  "stop_requested": false,
  "critical_block": false,
  "max_in_progress": 1,
  "tasks": [
    {
      "id": "H-001",
      "title": "Conferir P0/P1 e evidências",
      "owner": "Carlos Eduardo do Amaral",
      "executor_id": "codex-implementation",
      "reviewer_id": "independent-review",
      "role": "architect",
      "squad": "software",
      "status": "IN_REVIEW",
      "priority": "P1",
      "depends_on": [],
      "inputs": [
        "docs/harness/PROJECT_STATE.md"
      ],
      "outputs": [
        "docs/harness/VALIDATION.md"
      ],
      "allowed_paths": [
        "docs/harness/"
      ],
      "acceptance": "Evidências recuperáveis e revisão independente do snapshot; runtime nunca declarado ativo sem prova.",
      "environment": "CLOUD_CODE",
      "attempts": 0,
      "no_progress": 0,
      "max_attempts": 3,
      "authorized": false,
      "evidence": [],
      "review": null,
      "next_action": "Revisar evidências e registrar decisão aplicável",
      "deadline": null
    },
    {
      "id": "H-002",
      "title": "Homologar um perfil de projeto",
      "owner": "Carlos Eduardo do Amaral",
      "executor_id": "codex-implementation",
      "reviewer_id": "independent-review",
      "role": "architect",
      "squad": "software",
      "status": "BLOCKED",
      "priority": "P1",
      "depends_on": [
        "H-001"
      ],
      "inputs": [
        "docs/harness/PROJECT_STATE.md"
      ],
      "outputs": [
        "docs/harness/VALIDATION.md"
      ],
      "allowed_paths": [
        "docs/harness/"
      ],
      "acceptance": "Evidências recuperáveis e revisão independente do snapshot; runtime nunca declarado ativo sem prova.",
      "environment": "CLOUD_CODE",
      "attempts": 0,
      "no_progress": 0,
      "max_attempts": 3,
      "authorized": false,
      "evidence": [],
      "review": null,
      "next_action": "Revisar evidências e registrar decisão aplicável",
      "deadline": null
    },
    {
      "id": "H-003",
      "title": "Aprovar arquitetura do worker persistente",
      "owner": "Carlos Eduardo do Amaral",
      "executor_id": "codex-implementation",
      "reviewer_id": "independent-review",
      "role": "architect",
      "squad": "software",
      "status": "APPROVAL_REQUIRED",
      "priority": "P1",
      "depends_on": [
        "H-002"
      ],
      "inputs": [
        "docs/harness/PROJECT_STATE.md"
      ],
      "outputs": [
        "docs/harness/VALIDATION.md"
      ],
      "allowed_paths": [
        "docs/harness/"
      ],
      "acceptance": "Evidências recuperáveis e revisão independente do snapshot; runtime nunca declarado ativo sem prova.",
      "environment": "CLOUD_CODE",
      "attempts": 0,
      "no_progress": 0,
      "max_attempts": 3,
      "authorized": false,
      "evidence": [],
      "review": null,
      "next_action": "Revisar evidências e registrar decisão aplicável",
      "deadline": null
    }
  ]
}
```
