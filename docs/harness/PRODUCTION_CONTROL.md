# Controle de produção

| Ambiente | Branch | Banco | Secrets | Deploy | Uso |
|---|---|---|---|---|---|
| Web de desenvolvimento | chore/p0-harness-control-room | SQLite operacional fora do Git; produto sem banco | nenhum | proibido | auditoria supervisionada |
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

O runtime local implementa stop, prazo, teto de claims, limite de tentativas,
dependências, leases/fencing, heartbeat, revisão independente, idempotência e
registro transacional. `reap()` recupera expirados quando a bridge chama; não há
watchdog de servidor. WIP=1 inclui trabalho aguardando revisão.

Limites ainda não implementados: medição/teto monetário e de tokens, sandbox de
processo, detector automático de segredo/regressão e reconciliação de efeitos
externos. Por isso somente auditoria de contexto selecionado está habilitada;
workers de código, serviços externos e execução sem sessão permanecem bloqueados.
Stop impede novos claims/submits/reviews, mas não mata uma chamada de modelo já
iniciada: cancelamento do agente depende da bridge. Isso não é disjuntor físico. Bloqueios locais não impedem tarefas independentes autorizadas. Produção, aprendizado central e campanhas reais não são efeitos automáticos da fila.
