# Aprendizado revisado

Nenhuma lição ACCEPTED criada por inferência. Se houver falha corrigida após revisão, registrar candidato LL-### com status PROPOSED, tarefa, commit, erro, causa, prevenção, evidência e proponente.

Revisão semanal é cadência de governança, não agendamento instalado. ARCHITECT/SENTINEL ou responsável humano avalia utilidade, risco e escopo; revisor deve ser diferente do proponente. Regra aceita recebe referência em DECISIONS.md e mantém rastreabilidade aqui; regra rejeitada fica REJECTED com motivo.

Promoção central: proposta em PR, licença e aplicabilidade transversal verificadas, revisão independente, autorização de publicação. Não autoeditar agentes globais. Se o projeto já tem LESSONS_LEARNED.md, LESSONS_CANDIDATES.md e LESSONS_LEARNED_GLOBAL.md, apontar para as fontes existentes em vez de criar duplicatas.

## LL-001 — PROPOSED

Tarefa H-001. Proponente: codex-implementation. Origem: revisão independente desta branch.
Erro: valores truthy de tipo errado podiam liberar um candidato no roteador.
Causa: campos obrigatórios eram verificados por presença sem schema de tipos.
Prevenção proposta: validar tipos, strings não vazias, listas e raiz JSON antes de regras de estado; manter testes negativos.
Evidência: tests/test_supervisor.py, testes malformed_roots, malformed_required_fields e malformed_evidence; hashes em VALIDATION.md. Aceitação/promocão: pendente de revisão, sem alteração global.
