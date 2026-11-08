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
