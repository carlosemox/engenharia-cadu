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


## LL-002 — PROPOSED

Tarefa H-004. Proponente: sessão Codex. Evidência: OPERATIONAL_EVIDENCE.md.
Erro: configuração de storage rejeitada e envio inicial de contexto antes do claim.
Causa: bridge manual sem preflight único do armazenamento e da transição de estado.
Prevenção proposta: testar diretórios irmãos fora de Git e confirmar claim antes de
qualquer despacho. Adapter programático deve tornar essa sequência obrigatória.
Não promovida a regra global; alterações de runtime exigem revisão independente.


## LL-003 — PROPOSED

Tarefa H-004; proponente: implementador; revisor identificou P2 depois corrigido.
Erro: mudança de fonte/evidência durante hashing do parecer podia escapar da checagem.
Causa: ordem das verificações sem rechecagem após o trabalho de hashing mais lento.
Prevenção proposta: revalidar entradas antes da transição e congelar escritores do
host durante a operação; teste de interleaving e limitação explícita de atomicidade.
Evidência: tests/test_supervisor_runtime.py e evidence/H-004/code-review.md.
Não aceita/promovida globalmente; aprendizado pendente de decisão.
