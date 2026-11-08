# Autonomia operacional

## Autorização vigente

Cadu autorizou nesta sessão operacionalizar autonomia, criar biblioteca pública,
comando de regularização e publicar a central em português, inglês e espanhol.
Isso autoriza merge/deploy desta central após evidências. Não é migração automática
de aplicações, contratação de serviços, exposição de conteúdo privado ou gasto
ilimitado em modelos. Provedor preferencial de IA: Codex/OpenAI, sem troca silenciosa.

## Modos reais

| Modo | Executor | Escopo | Persistência |
|---|---|---|---|
| CODEX_WEB_SUPERVISED | agentes da sessão | auditoria delimitada + revisão distinta | SQLite local e recibo Git |
| AUTONOMOUS_DETERMINISTIC_AUDIT | GitHub Actions | auditoria estrutural, validação editorial, fila e testes | configuração Git + artifacts 30 dias |
| AUTONOMOUS_LLM | pendente | desenvolvimento por IA fora do chat | BLOCKED_AUTHENTICATION_AND_BUDGET |

O segundo modo funciona sem conversa aberta depois de publicado na main. Não chama
modelo e usa zero tokens LLM em seus scripts. Não substitui o julgamento do agente
nem conclui tarefas de produto. Cada ciclo termina; não há processo 24h residente.

`.github/workflows/autonomous-maintenance.yml` roda no push, manualmente e a cada
seis horas (minuto 17 UTC). Horários do GitHub podem atrasar; repositórios públicos
inativos podem ter schedule desabilitado. Não é SLA de execução exata.

A fila de manutenção é `automation/maintenance.json`, separada das tarefas humanas
por função: ações técnicas fixas M-001…M-004. Não aceita comandos vindos de prompts.
Falha bloqueia dependentes e permite checks independentes; uma tentativa por ciclo,
WIP=1, máximo quatro tarefas, prazo global cinco minutos e job dez minutos.
Testes podem regenerar derivados no checkout descartável, sem commit/push.
Relatórios recuperáveis ficam nos artifacts `maintenance-<run_id>`, por 30 dias.
Isso não equivale a backup de bancos ou arquivos dos aplicativos.

## Parar e retomar

Definir repository variable `CADU_AUTONOMY_STOP=true` impede novos jobs. Para job
já iniciado, usar Cancel workflow no GitHub; variável não é lida dinamicamente
por processo em execução. Desabilitar workflow também interrompe novos gatilhos.
Alterar `automation/maintenance.json` enabled=false impede execução no próximo
ciclo. Retomar preserva tarefas/versionamento e não apaga evidências anteriores.

## Próximo passo para agente de IA sem conversa

A integração oficial Codex GitHub Action usa autenticação de API própria. Nesta
sessão não há OPENAI_API_KEY no ambiente; secrets do repositório não foram lidos.
Ainda é necessário definir autenticação de serviço, modelo disponível, teto de
gasto e destino seguro da credencial. Nunca colar segredo no chat ou no Git.
Autorização genérica de autonomia não fornece essas credenciais nem define preço.

O perfil inicial deve separar executor e revisor em jobs isolados, permissões
mínimas, sem credenciais de produção, sem pull_request_target sobre código externo,
sem auto-merge de mudanças de segurança/banco. Ler o plano da tarefa, fornecer
contexto mínimo e registrar tokens/custo quando realmente observáveis. Um limite
de tempo não é teto financeiro. Não ativar modelo pago somente por schedule.

## Fontes verificadas

- https://github.com/openai/codex-action/blob/13e9c17417b29e9a276f73ec6ed7fb574137d3c3/README.md
- https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows

## Projetos em andamento

`comandos/REGULARIZAR_PROJETO.md` inicia auditoria seletiva por projeto.
`scripts/audit_project.py --project /caminho/do/projeto` gera diagnóstico sem executar
código do alvo. Documentos existentes equivalentes prevalecem. Depois do plano,
correções locais autorizadas usam branch isolada, DS existente, testes e revisão.
Não instalar todo catálogo. Registro cadastral de skill não é homologação.


### Adapter Codex preparado, ainda inativo

`.github/workflows/codex-audit.yml` contém executor e revisor em jobs separados,
action oficial fixada por SHA, perfil read-only, prazo e artifacts. Está bloqueado
por `if: false` além de flags de configuração. Não foi executado nem homologado.
Antes de remover esse bloqueio em PR: escolher modelo, fornecer autenticação por
secret, definir orçamento, testar isolamento e comprovar chamada/revisão reais.
Flags de orçamento são declarações, não limite financeiro imposto pelo provedor.
Este primeiro adapter produz auditoria/proposta textual; não implementa nem publica
código automaticamente. Ampliação para código exige perfil de escrita isolado e
gates próprios. A revisão em outro job não garante ausência de erro de modelo.
