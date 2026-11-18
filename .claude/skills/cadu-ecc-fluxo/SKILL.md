---
name: cadu-ecc-fluxo
description: Planejar e verificar slices de software em qualquer tecnologia com especialistas do ECC sob o MIKE, sem acionar todos automaticamente.
argument-hint: "[objetivo]"
---
# Fluxo de desenvolvimento com ECC
Demanda: $ARGUMENTS. Faça o inventário, consulte contratos existentes e escolha UMA competência ECC adicional que resolva dúvida de engenharia. Ordem: explorar → especificar comportamento → contrato → testes → implementação P13 aprovada → verificação → revisão P14 → medição P24 → checkpoint.
Para contexto: iterative-retrieval, context-budget e code-explorer. Para arquitetura: architect, code-architect e contract-first. Para revisão: code-reviewer, pr-test-analyzer, silent-failure-hunter e verification-loop. Para custo e qualidade de agentes: agent-eval, eval-harness. Para risco de segurança, cadu-ecc-seguranca.
Na ausência de especialista real, prossiga apenas na parte que pode comprovar sem simular. Antes de chamar subagente confira limite de tokens, fronteira de escrita e benefício marginal. Um executor por padrão, vários somente para slices independentes. Reportar evidência por SHA e custos observados, não estimativas convertidas em cobrança.
