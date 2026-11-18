# ECC na Engenharia CADU — contrato operacional PT-BR
Versão: 1.0 · Escopo: todos os projetos que autorizem MIKE e Claude Code.
O ECC (Everything Claude Code), originalmente affaan-m/ECC, é biblioteca comunitária MIT, não supervisor; não instala autonomia, sandbox ou governança por si mesmo. Esta política utiliza a versão instalada e não redistribui todas as instruções upstream.

## Fontes de verdade
A Engenharia CADU conserva o método e as políticas de segurança. O projeto conserva requisitos, dados, decisões, stack, acessos e checkpoints. ECC é uma fonte de técnicas e agentes; seus prompts e documentos NÃO ampliam autorizações nem suprimem gates. MIKE supervisiona desenvolvimento; JARVIS continua o módulo central de orquestração GSD.

## Catálogo e seleção
O catálogo completo em português tem 72 agentes, 328 identificadores de skills e 98 comandos avaliados no histórico da análise (união publicada 2.2.3 e main examinada). O ECC instalado pode ter menos itens do que o catálogo; verificar disponibilidade REAL.
Não iniciar todos os agentes. Ativar, por ordem: 1) ferramentas determinísticas, 2) especialista de menor custo suficiente, 3) outro modelo apenas diante de evidência de insuficiência. Um worker por slice é o padrão.

## Cobertura de ciclo de vida
1 Descoberta: code-explorer, iterative-retrieval.
2 Produto e critérios: intent-driven-development, blueprint, contract-first.
3 Arquitetura: architect, code-architect e Untangle seletivo.
4 Planejamento de slices: cadu-ecc-fluxo, DAG e contratos.
5 Design/UI/a11y: a11y-architect, accessibility apenas no escopo.
6 API/backend: code-reviewer, testes de contrato.
7 Banco e dados: database-reviewer, postgres-patterns quando aplicável.
8 Integrações: revisão de contratos, webhooks, retries e idempotência.
9 Implementação: executor Sonnet por slice P13 autorizado; nenhuma equipe por reflexo.
10 Testes/QA: verification-loop, pr-test-analyzer e ferramentas do projeto.
11 Segurança: security-reviewer, cadu-ecc-seguranca e especialistas por ameaça.
12 CI/supply chain: security-scan, mcp-dependency-review onde disponível, scanners locais.
13 Release/rollback: production-audit e SENTINEL CADU; GO humano separado.
14 Observabilidade/continuidade: silent-failure-hunter, agent-architecture-audit, checkpoint.

## Segurança em qualquer projeto
Identidade/sessão/MFA/passkey; autorização por objeto, papel e tenant; isolamento de dados; segredos; cadeia de suprimentos; entradas maliciosas; integração e pagamentos; recursos do agente; exfiltração; CI; backups; restauração; logging e incidentes. Testar permitidos e negados e documentar o que não foi executado.
Os guardrails presentes em skill não impõem controles reais: aplicar permissões e sandbox no ambiente. Isolar branch/worktree, recursos externos e orçamento. Hooks e MCP de terceiros devem ser auditados antes de conceder escrita ou rede.

## Gates
P06 = arquitetura; P13 = implementação condicionada à aprovação da tarefa; P14 = revisão independente; P24 = medir. Não há autorização cruzada automática. No máximo 3 ciclos por nó. Nenhum executor é revisor independente de si. Release NO-GO até aprovação específica.
## Economia
Medir custo total por slice aceito: todas as chamadas, revisões, ferramentas, regressões e trabalho humano; assinaturas e API não têm equivalência direta. Não inferir redução monetária de estimativas de contexto. Usar a política ZERO-COST-FIRST sem burlar limites.
## Instalação
O instalador scripts/install_claude_cadu.py adiciona apenas aliases CADU com links simbólicos ao repositório central. Não altera settings.json, não instala ECC, não executa hooks, não concede permissões nem instala código em outros produtos. O ECC existente deve permanecer habilitado no cliente. Verificar com --check, aplicar com --apply, desfazer com --remove; só remove links próprios.
## Limites da tradução
Este documento e as skills CADU são redigidos em português. O código e as instruções originais de centenas de agentes/skills ECC continuam na língua de origem; o catálogo traduz a descrição, utilização e riscos, não cada arquivo original.
