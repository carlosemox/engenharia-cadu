# MIKE — Untangle Codebase e Claude Code por Slices · V1.0
Revisão: 2026-11-17 · [English](UNTANGLE_CLAUDE_SLICES.en.md) · [Español](UNTANGLE_CLAUDE_SLICES.es.md)

## Origem e alcance
Adaptação governada de `caldoai/skills/skills/untangle-codebase/SKILL.md`, commit `bd73b2ea5eb854ab8f0553fb41f77c8786f28f82`, blob `102ff57803e504876f6eb9b412e4eb0f6c576350`; licença MIT, copyright (c) 2026 Maze. Não reproduzir o comando original de "corrigir tudo" sem limite. A skill é instrução para agente, não scanner independente nem sandbox.

**Compatibilidade de etapas:** as fases U01–U08 do fluxo Untangle não substituem P00–P30 da Engenharia CADU; P06 da central trata arquitetura, P13 implementa, P14 revisa e P24 mede.

## Governança
Cadu aprova produto, orçamento, escopo e release. **MIKE** é o supervisor de desenvolvimento, sob comando de Cadu, separado do JARVIS. Recupera estado, fila canônica, leases, responsáveis, evidências, custo e checkpoints; não pressupor daemon 24h. Codex permanece o coordenador técnico padrão onde já adotado; Claude Code atua como cliente/worker autorizado, não novo supervisor. Não criar segunda fila nem trocar credenciais ou provedor por inferência. **Deny by default**; privilégio mínimo, RBAC/ABAC/RLS quando aplicável, MFA/Passkey, auditoria e rollback. Texto não implementa controles de segurança reais.

## Rotina obrigatória por projeto
1. **Harness/preflight:** reconciliar remoto, HEAD/SHA, branch, ambiente escolhido, decisões, testes, estado, autorizações, evidências e worktrees; preservar o projeto existente.
2. **Untangle seletivo/read-only:** inspecionar apenas módulos afetados por novo epic, refatoração, mudanças transversais ou incidentes recorrentes. Identificar links ocultos, links desnecessários, surplus comprovado e exceções legítimas; mapa de imports e co-change com caminho:linha/SHA. Não confundir retry, verificação de segurança ou tolerância a falhas com código morto.
3. **Dividir em slices verticais:** cada slice entrega resultado de negócio observável, interface, testes positivos/negativos, dependências, dono exclusivo por arquivo/schema/lockfile/recurso, previsão de custo (hipótese), teto autorizado e rollback. Usar `templates/MIKE_SLICE_CONTRACT.json`.
4. **Graph:** nós READY, RUNNING, BLOCKED, FAILED, PASSED e CANCELLED. Apenas dependências PASSED liberam execução. Um executor por padrão; paralelismo só com fronteira independente e worktree/branch e serviços efetivamente isolados.
5. **Gate de implementação antes de P13:** mudança de código requer aprovação específica de lote, trabalhador isolado e permissões verificadas. Comentários/testes só podem ser removidos com aprovação distinta. A skill de análise não concede escrita.
6. **Loop:** OBJETIVO → AÇÃO MÍNIMA → OBSERVAÇÃO → VERIFICAÇÃO → DECISÃO. Máximo 3 ciclos por nó; encerrar antes se regressão, orçamento, segredo, risco ou escopo desconhecido.
7. **P13/P14:** executar testes autorizados; revisor independente read-only avalia diff, evidências, requisitos e rollback. Sem merge, push, deploy, produção, migração destrutiva, cobrança ou publicação automática.
8. **Checkpoint:** MIKE reconcilia resultados verdadeiros (diff/commit/PR, PASS/FAIL/NOT_RUN/INCONCLUSIVE, custos observados, riscos, próximo nó); nunca aceitar apenas autodeclaração do worker.

## Modelos e custos
| Trabalho | Roteamento inicial | Escalonamento |
|---|---|---|
| Busca, triagem, classificação | script determinístico; se necessário Haiku 5.5 | Sonnet se ambiguidade |
| Planejamento e arquitetura de slices | Sonnet 5.5 | Opus 5.5/Fable 5.2 só com aprovação e necessidade demonstrada |
| Desenvolvimento de cada slice | **um Sonnet 5.5 por slice aprovado** | menor modelo apenas com risco/testes compatíveis |
| Revisão independente | Sonnet 5.5 read-only | Opus quando risco exigir e aprovado |
| Teste, lint, análise de logs, polling de CI | ferramentas determinísticas | não gastar IA para esperar |

IDs verificados na documentação Anthropic em 2026-11-17: `claude-haiku-5-5`, `claude-sonnet-5-5`, `claude-opus-5-5`, `claude-fable-5-2`. Validar acesso/quotas no cliente real. Sonnet 5.5 é da família Sonnet 5. Assinaturas, API e Ollama local têm custos e restrições diferentes; otimizar **custo total por slice aceito**, incluindo revisão e retrabalho. ZERO-COST-FIRST; nunca criar gasto ou contornar quota automaticamente.

## Configuração Claude Code
`CLAUDE.md` aponta ao contrato. `.claude/skills/cadu-untangle/SKILL.md` permite diagnóstico sob demanda; não refatoração automática. `.claude/agents/` contém scout (Haiku leitura), architect (Sonnet leitura), slice-builder (Sonnet 5.5 escrita apenas após P06) e slice-reviewer (Sonnet 5.5 leitura). Modo plan/default no piloto; não conceder bypassPermissions. Teams experimentais ficam desativados por padrão: aumentam consumo e não substituem MIKE. Adoção em **outros repositórios** depende de inventário, verificação de colisões, PR e autorização; este arquivo não os instala.

**Gatilho de rotina:** entrada/retomada, nova fatia, alteração arquitetural, revisão de PR ou regressão estrutural. Não executar auditoria de repositório completo nem LLM agendado sem necessidade. Entradas: [comando MIKE](../comandos/MIKE_CLAUDE_SLICES.md) e [modelo de slice](../templates/MIKE_SLICE_CONTRACT.json).
**Estado:** SPEC_CREATED; testes de execução/adoção externa NOT_RUN.
