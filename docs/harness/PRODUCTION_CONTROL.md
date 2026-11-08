# Controle de produção

| Ambiente | Branch | Banco | Secrets | Deploy | Uso |
|---|---|---|---|---|---|
| Web de desenvolvimento | chore/p0-harness-control-room | nenhum | nenhum | proibido | P0/P1 |
| Staging | não configurada | não configurado | nenhum recebido | bloqueado | futuro piloto |
| Produção | main | não aplicável à central estática | não acessados | exige gate | GitHub Pages existente |

Owner de autorização: Carlos Eduardo do Amaral. Coordenador: Codex. WIP=1 por checkout; domínios independentes podem ser paralelos somente em worktrees separados e sob orçamento explícito. Datas/prazos só entram quando acordados; sem calendário de release presumido.

Dez freios obrigatórios antes de ligar executor:
1. Stop flag persistente, consultada antes de cada ação; cancelamento cooperativo.
2. Prazo máximo por tarefa e por sessão.
3. Orçamento de tokens/custo autorizado e medição; desconhecido bloqueia execução paga autônoma.
4. Máximo de três ciclos; duas tentativas sem progresso geram REPEATED_FAILURE.
5. Dependências e gates satisfeitos; grafo acíclico.
6. Escopo de arquivos/ações deny-by-default, sandbox real e nenhum segredo montado.
7. Lease atômico, fencing, heartbeat e watchdog; trabalhador antigo perde autoridade.
8. Implementador diferente do revisor; evidência vinculada ao snapshot.
9. Circuit breaker para segredo, dados perdidos, regressão grave ou autorização ausente.
10. Idempotência, checkpoint e reconciliação de efeito externo incerto antes de retry.

Nesta entrega são contratos e validações estáticas. Freios 1/2/3/4/7/9/10 não são mecanismos ativos em servidor. Bloqueios locais não impedem tarefas independentes autorizadas. Produção, aprendizado central e campanhas reais não são efeitos automáticos da fila.
