# Handoff e evidências — TEMPLATE INATIVO

## Identidade da execução
Projeto; missão/tarefa; cliente/modelo observados; versão/snapshot; workspace; ambiente; execution ID; data; proprietário/lease e processos relacionados sem segredos.

## Estado verificável
O que foi concluído; alterações staged/unstaged/untracked relevantes; testes executados; evidências; falhas; o que não foi testado. Separar planejado de observado e incluir limites da conclusão.

## Recursos e efeitos
Portas, builds, containers/bancos de teste, logs e artefatos próprios; IDs de PR, deploy, migration, job, mensagem ou publicação quando houver. Resultado externo incerto deve ser conciliado antes de retry.

## Próxima ação
Menor etapa para retomar; entradas/dependências; autorização existente; decisão pendente; condição de parada. Não transferir secrets ou toda a transcrição.

## Validade
Como conferir estado real; quais mudanças invalidam cada evidência; qual registro canônico substituirá este handoff quando concluído. Handoff não é ordem de reset nem prova de que um processo continua vivo.
