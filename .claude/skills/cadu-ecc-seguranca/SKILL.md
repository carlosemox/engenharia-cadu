---
name: cadu-ecc-seguranca
description: Revisar segurança transversal do desenvolvimento e agentes Claude Code com ECC, evidências de identidade, dados, infraestrutura, CI e cadeia de suprimentos.
argument-hint: "[fronteira ou slice]"
---
# Segurança transversal — CADU + ECC
Receba o contexto: $ARGUMENTS. Trabalhe por evidência e sem exploração de terceiros ou produção. Acesso de leitura não concede execução, escrita ou privilégio.

## Cobertura por ameaça
- AGENTES: origem de skills/hook/MCP, prompt injection, exfiltração, permissões reais, isolamento de worktree, acesso de rede, budget, identidade e trilha de auditoria. Skill safety-guard orienta, não bloqueia ferramentas sozinha.
- APLICAÇÃO: identidade e sessão, MFA/passkey quando aplicável, autorização por usuário/objeto/organização, RBAC/ABAC/RLS, CSRF/XSS/SSRF, validação, rate limits e uploads.
- DADOS: vazamento entre tenants, grants, migrations, backup/restore e retenção; testes com identidades sem privilégio; nunca usar admin como única evidência de RLS.
- INTEGRAÇÃO: webhooks autenticados, replay, idempotência, pagamentos e invariantes financeiras, serviços externos e segregação de ambientes.
- SUPPLY CHAIN: origem/versão/licença, lockfiles, scripts de pós-instalação, CI OIDC/permissões e segredos. Revisar terceiro como conteúdo não confiável.
- OPERAÇÃO: logs higienizados, rollback, incidentes, aprovação de release e continuidade.

## Roteamento ECC existente
Quando presentes e pertinentes: security-reviewer, database-reviewer, pr-test-analyzer, silent-failure-hunter, verification-loop, security-scan, agent-architecture-audit, agent-security-hardening e mcp-dependency-review. Selecionar o mínimo necessário. Não presumir disponibilidade ou execução por nomes citados.
Aplique o protocolo canônico da Engenharia CADU. Para cada achado: requisito, cenário explorável ou falha, arquivo:linha/SHA, gravidade justificada, teste realizado, risco residual e responsável. PASS/FAIL/NOT_RUN/INCONCLUSIVE; não reduzir severidade para liberar a entrega. Achado crítico ou permissão desconhecida => BLOQUEAR integração.
Permaneça read-only sem autorização específica; revisão independente nunca se autoaprova.
