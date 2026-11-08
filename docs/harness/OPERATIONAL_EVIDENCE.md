# Piloto operacional H-004 — 2026-11-08

Resultado observado: duas tarefas documentais executadas por agente real,
submetidas à fila SQLite e aprovadas por revisor real distinto. B foi adquirida
somente depois do DONE revisado de A. Run encerrado com stop persistido.

- Executor: `01a1bc31-d489-7195-b40a-c95e5e262037`.
- Revisor: `01a1bc31-d932-76c4-85f3-183d8d57c03e`.
- Bridge: sessão Codex web; IDs originados da ferramenta de agentes.
- A: separação software/civil, limites do Supervisor, catálogo sem homologação
  automática e revisão independente. PASS documental.
- B: contrato do Design System e lacunas declaradas. PASS documental.
- Claims: 2/2; tentativa 1 em cada tarefa; deadline e lease delimitados.
- Heartbeat real registrado em B. Stop ao fim. Não há serviço ativo.

[Recibo e eventos](evidence/H-004/receipt.json),
[auditor A](evidence/H-004/auditor-a.md), [revisor A](evidence/H-004/review-a.md),
[auditor B](evidence/H-004/auditor-b.md), [revisor B](evidence/H-004/review-b.md).
Hashes de fonte e relatório constam no recibo. Relatórios foram conferidos pelo
runtime ao submeter/revisar; os agentes não executaram hashing por conta própria.
O revisor corrigiu atribuição indevida do claim ao usuário no relatório A: a
confirmação foi da bridge via ferramenta.

## Limites e ocorrências

A inicialização bloqueou storage sob árvore Git ancestral e, depois, diretórios
de banco/evidência sobrepostos. Ambos corrigidos usando diretórios irmãos fora
do Git. Nenhum job foi adquirido nas tentativas rejeitadas. O texto inicial de A
foi entregue antes do claim por erro de sequência da bridge; solicitada e recebida
reavaliação após o claim antes de aceitar a entrega. Isso reforça a necessidade
de adapter programático antes de qualquer execução autônoma.

Os agentes receberam somente texto e instrução de não usar ferramentas. Isso é
protocolo supervisionado, não sandbox técnico de suas capacidades disponíveis.
Custos e tokens: NOT_MEASURED. Recibo comprova esta sessão, não disponibilidade
futura do host. Banco temporário fora do Git; perda do host exige reconciliação
pelo recibo. Teste de recuperação em produção e backup operacional externo: NOT_RUN.
O piloto não homologa agentes do catálogo para código, banco, campanhas ou produção.


## Recuperação local

[Ensaio de backup](evidence/H-004/recovery.json): PASS. Usada API SQLite backup
para banco separado no mesmo host; reabertura via Runtime preservou dois DONE,
dois claims e stop. Não alterou banco original, não testou perda de host e não
configurou backup externo. Relatórios permanecem no recibo versionado.


Nota de versão: o piloto ocorreu antes do reforço final de rechecagem de hashes
apontado pela revisão de código. O recibo fixa os snapshots documentais auditados,
não o hash do módulo runtime daquele instante. A revisão final e os testes de
regressão do módulo são registrados separadamente em VALIDATION.md.
