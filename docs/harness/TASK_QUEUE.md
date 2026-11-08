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
      "status": "DONE",
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
      "authorized": true,
      "evidence": [
        "docs/harness/VALIDATION.md",
        "https://github.com/carlosemox/engenharia-cadu/actions/runs/42501906470"
      ],
      "review": {
        "reviewer_id": "independent-review",
        "result": "PASS",
        "snapshot": "ea8f0c13a3674b91ea0751e0092caa879e1a2a9c"
      },
      "next_action": "Conferir incremento operacional H-004",
      "deadline": null
    },
    {
      "id": "H-002",
      "title": "Homologar perfil de auditoria documental supervisionada",
      "owner": "Carlos Eduardo do Amaral",
      "executor_id": "01a1bc31-d489-7195-b40a-c95e5e262037",
      "reviewer_id": "01a1bc31-d932-76c4-85f3-183d8d57c03e",
      "role": "architect",
      "squad": "software",
      "status": "DONE",
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
      "acceptance": "Somente contratos documentais dos arquivos de catálogo e DS: auditor e revisor distintos; hashes exatos no recibo H-004. Não homologa código ou catálogo inteiro.",
      "environment": "CLOUD_CODE",
      "attempts": 0,
      "no_progress": 0,
      "max_attempts": 3,
      "authorized": true,
      "evidence": [
        "docs/harness/OPERATIONAL_EVIDENCE.md"
      ],
      "review": {
        "reviewer_id": "01a1bc31-d932-76c4-85f3-183d8d57c03e",
        "result": "PASS",
        "snapshot": "ea8f0c13a3674b91ea0751e0092caa879e1a2a9c"
      },
      "next_action": "Preservar perfil read-only; ampliar somente com isolamento e aprovação",
      "deadline": null
    },
    {
      "id": "H-003",
      "title": "Ativar adapter Codex independente da sessão",
      "owner": "Carlos Eduardo do Amaral",
      "executor_id": "codex-implementation",
      "reviewer_id": "independent-review",
      "role": "architect",
      "squad": "software",
      "status": "BLOCKED",
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
      "next_action": "Cadu define autenticação segura, modelo e teto de gasto; depois teste real do adapter antes de remover if:false",
      "deadline": null
    },
    {
      "id": "H-004",
      "title": "Validar e registrar o incremento operacional supervisionado",
      "owner": "Carlos Eduardo do Amaral",
      "executor_id": "01a1bc2d-ec5d-779b-a19e-09112a9da00e",
      "reviewer_id": "01a1bc32-0470-7704-910d-fb7025d1f039",
      "role": "architect",
      "squad": "software",
      "status": "DONE",
      "priority": "P1",
      "depends_on": [
        "H-001"
      ],
      "inputs": [
        "scripts/supervisor_runtime.py",
        "tests/test_supervisor_runtime.py",
        "docs/harness/OPERATING_RUNBOOK.md"
      ],
      "outputs": [
        "docs/harness/VALIDATION.md",
        "docs/harness/OPERATIONAL_EVIDENCE.md"
      ],
      "allowed_paths": [
        "docs/harness/"
      ],
      "acceptance": "Dois jobs documentais reais, dependência respeitada, review independente, stop; testes de fila e parecer de código sem bloqueantes.",
      "environment": "CLOUD_CODE",
      "attempts": 0,
      "no_progress": 0,
      "max_attempts": 3,
      "authorized": true,
      "evidence": [
        "docs/harness/OPERATIONAL_EVIDENCE.md",
        "docs/harness/VALIDATION.md",
        "docs/harness/evidence/H-004/code-review.md",
        "https://github.com/carlosemox/engenharia-cadu/pull/5"
      ],
      "review": {
        "reviewer_id": "01a1bc32-0470-7704-910d-fb7025d1f039",
        "result": "PASS",
        "snapshot": "26fb3e1d6c6b15b13a8a3a9f1aef728f31461597",
        "snapshot_kind": "git_blob_runtime; full SHA256 list in VALIDATION.md"
      },
      "next_action": "Publicado pela PR5; serviço LLM fora da sessão permanece H-003",
      "deadline": null
    },
    {
      "id": "H-005",
      "title": "Registrar homologação e publicação da biblioteca, comandos e manutenção",
      "owner": "Carlos Eduardo do Amaral",
      "executor_id": "codex-implementation",
      "reviewer_id": "01a1bc44-be56-7547-bee9-15456d80903f",
      "role": "architect",
      "squad": "software",
      "status": "DONE",
      "priority": "P1",
      "depends_on": [
        "H-004"
      ],
      "inputs": [
        "docs/harness/AUTONOMY.md"
      ],
      "outputs": [
        "docs/harness/VALIDATION.md",
        "docs/harness/PROJECT_STATE.md",
        "docs/harness/RELEASE_CHECKLIST.md"
      ],
      "allowed_paths": [
        "docs/harness/"
      ],
      "acceptance": "176 testes, revisão independente, CI e Pages PASS; smoke público; terceiros sem homologação presumida e adapter LLM inativo.",
      "environment": "CLOUD_CODE",
      "attempts": 0,
      "no_progress": 0,
      "max_attempts": 3,
      "authorized": true,
      "evidence": [
        "docs/harness/evidence/H-005/library-review.md",
        "docs/harness/evidence/H-005/automation-review.md",
        "docs/harness/VALIDATION.md",
        "https://github.com/carlosemox/engenharia-cadu/actions/runs/42507613947"
      ],
      "review": {
        "reviewer_id": "01a1bc44-be56-7547-bee9-15456d80903f",
        "result": "PASS",
        "snapshot": "59d4d15a6b300441c843d89e4a9a2b2847da3cdd",
        "snapshot_kind": "reviewed code hashes in H-005 receipts; candidate CI"
      },
      "next_action": "Usar biblioteca e auditor; ativação LLM continua bloqueada em H-003",
      "deadline": null
    }
  ]
}
```
