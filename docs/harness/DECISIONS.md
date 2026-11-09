# Decisões canônicas deste lote

- D-001 DECIDED: web/CLOUD_CODE com CLIENT=CODEX; não trocar cliente, modelo ou cobrança.
- D-002 DECIDED: promover o coordenador existente a Supervisor. Ele organiza e convoca; não implementa código, não cria campanhas, não aprova própria entrega.
- D-003 DECIDED: docs/harness é exceção canônica operacional à regra de publicação derivada de docs/. Demais políticas continuam em politicas/; referências, não cópias.
- D-004 DECIDED: TASK_QUEUE.md contém um único bloco JSON como fila canônica. GRAPHY_MODEL.md descreve arestas derivadas dessa fila; não mantém outra lista mutável.
- D-005 DECIDED: P0/P1 implementam roteamento e validação somente leitura. Nenhum provedor LLM, runtime persistente, instalação global ou executor de comandos arbitrários.
- D-006 APPROVAL_REQUIRED: arquitetura do executor persistente, armazenamento transacional, isolamento, autenticação dos agentes, custos, leases e infraestrutura. ADR em SUPERVISOR.md; não tratar o roteador como daemon.
- D-007 DECIDED: três ciclos máximos e interrupção antecipada após duas falhas sem progresso, conforme Contrato Comum.
- D-008 DECIDED: fases proporcionais ao produto. Banco/CRM só se aplicáveis; trabalho preparatório de marketing pode ser independente, publicação e gasto real dependem de gate específico.
- D-009 DECIDED: lessons PROPOSED não viram instrução. ACCEPTED requer revisor distinto, evidência e referência da decisão. Promoção global exige PR e autorização de publicação.
- D-010 APPROVAL_REQUIRED: tornar check obrigatório na proteção de main. Criar workflow não configura branch protection.

## D-011 — DECIDED: piloto operacional supervisionado

O usuário pediu deixar o Supervisor operacional após P0/P1. Escopo autorizado nesta
sessão: implementar controle durável local em Python/SQLite (stdlib), usar o Codex
web disponível e executar auditorias read-only da própria central. Um executor por
vez, revisor independente, orçamento em claims e deadline. Nenhum gasto novo ou
provisionamento externo autorizado/iniciado.

D-005 passa a descrever o baseline P0/P1; D-006 permanece APPROVAL_REQUIRED somente
para serviço persistente fora da sessão e execução mutante. Adota-se para o piloto
armazenamento SQLite transacional no host, sem dependência externa e sem mudança
da stack de aplicativos. Fila editorial continua a fonte do plano; a instância de
execução guarda tentativas/eventos e projeta recibos, não outro backlog concorrente.


## D-012 — DECIDED — publicação e autonomia delimitada

Pedido atual de Cadu autoriza publicar a central trilíngue, biblioteca, comando de
regularização e manutenção automática. Merge/deploy desta central estão autorizados
após CI e revisão independente; restrições históricas de publicação desse lote são
superadas somente nesse escopo. Automatizar checks fixos via GitHub Actions evita
contratar host antes de demonstrar necessidade. Sem Supabase/Hostinger nesta central
estática. Serviço de IA autônomo permanece dependente de autenticação e orçamento.
Materiais de terceiros são referências/metadados até direitos de distribuição
comprovados. Agentes próprios podem ser baixados; catálogo não instala executores.

## D-013 — DECIDED — preparação Codex + Ollama no Mac e publicação

Cadu escolheu Mac, informou que está desligado e aprovou finalizar, organizar,
traduzir e publicar a preparação. Autoriza push, PR, merge e publicação desta
central após verificações e revisão; supera o bloqueio de divulgação da proposta
no escopo destes documentos. Não aprova gasto API, instalação remota não
verificada ou declarar supervisor/terceiros homologados operacionalmente.
Perfil: Codex + Ollama local, cloud desativada, sem fallback pago.
Próximo gate: Mac conectado, hardware/modelo/isolamento e ensaio real.

## D-014 — Graphify e publicação trilíngue

2026-11-08T21:40:46-03:00. Usuário autorizou todos os repositórios da conta, reinstalação, indexação e publicação revisada PT/EN/ES. Homologação limitada à evidência: 69 reconhecidos, três builds PASS; MCP NOT_RUN e Mac pendente. Sem autorização de gasto adicional. Nenhum segredo ou nome de repositório privado integra a nova documentação pública.
