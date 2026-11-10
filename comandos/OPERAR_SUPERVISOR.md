# Operar Supervisor em auditoria

## Comando completo
```text
COMANDO: OPERAR_SUPERVISOR
Usar Codex no ambiente já confirmado. Ler estado, decisões e OPERATING_RUNBOOK.md.
Operar apenas capacidade read_only_audit, com arquivos exatos, aceite, dependências,
prazo e limite de claims registrados. Não instalar agentes ou trocar fornecedor.
Usar scripts/supervisor_runtime.py para estado transacional; a sessão é a bridge
confiável que convoca as ferramentas de agentes realmente disponíveis. Sem bridge,
retornar BLOCKED_ADAPTER, não simular a execução.
Entregar somente snapshots aprovados ao especialista. Registrar a identidade real
retornada pela ferramenta; renovar lease enquanto houver progresso. O resultado é
um relatório, não instruções para executar comandos. Submeter evidência com hash;
convocar revisor diferente, conferir o mesmo snapshot e registrar PASS/FAIL.
Continuar somente para dependências liberadas e dentro de orçamento/prazo. Ao fim,
parar o run e salvar recibo sanitizado e checkpoint. Não versionar banco ou tokens.
Lições permanecem PROPOSED até revisão. Escrita de código, campanha, banco, rede,
produção e operação 24 horas não são autorizadas por este comando de auditoria.
Retornar estado real, tarefas, evidências, revisão, bloqueios e próximo passo.
```

## Mike

Coordenação: **Mike**. Aplicar a política compartilhada uma vez por revisão; preservar os limites deste comando. [Mike](../politicas/MIKE.md).
