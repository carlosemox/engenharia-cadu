# Mapeamento Matheus → Engenharia Cadu

Referência fixada em [toolkit-lock.json](../fontes/toolkit-lock.json). Cobertura do catálogo não é auditoria exaustiva de cada dependência. Nenhuma instalação foi realizada. A numeração do Matheus não substitui nossos IDs P00–P30.

## 15 prompts

| Referência Matheus | Destino Cadu | Adaptação |
|---|---|---|
| 01 — Sanitation | P20/P21 | Medir antes; refatorar só por causa/escopo aprovado |
| 02 — Warnings | P13/P21 | Correção focal; não silenciar regra para verde |
| 03 — Code review | P14 | Escopo congelado; revisor independente e limites |
| 04 — Brainstorm to plan | P01–P06/P12 | Produto, design D0 e serviços antes do código |
| 05 — Waves | P12/P17 | Somente recursos independentes e tarefa READY |
| 06 — Memory | P09/P18 | Fontes canônicas, atualização e recuperação seletiva |
| 07 — Complete ESLint | P08/P09/P21 | Compatibilidade da stack, não regra universal |
| 08 — Quality gates | P11/P13/P14 | Gates verificáveis e proporcionais |
| 09 — Large files | P20/P21 | Tamanho é sinal, não justificativa automática |
| 10 — Machine | P07 → P10(MAQUINA) → P11 | Inventário e autorização global explícita |
| 11 — New project | P01–P12 | Não impor Next/Drizzle ou todas as skills web |
| 12 — Existing project | P20 → P21 | Restaurar antes de modernizar; preservar dados/stack |
| 13 — Security review | P14/P06 | Achados privados por evidência; não autonomia de ataque |
| 14 — Harness evaluation | P11/P24 | Casos descartáveis e controle de avaliação externo |
| 15 — Harness improvement | P24 | Baseline, candidato limitado e reversão; sem lab pago implícito |

## 23 frentes de ferramentas

| ID | Frente | Decisão inicial |
|---|---|---|
| 01 | Superpowers | Método proporcional; não repetir etapas aprovadas; seleção/teste por projeto |
| 02 | Subagents | Delegação seletiva; um dono por recurso; seleção/teste por projeto |
| 03 | RTK | Piloto de saída reduzida; original/exit code preservados; seleção/teste por projeto |
| 04 | Ponytail | Menor solução completa; nunca menor segurança; seleção/teste por projeto |
| 05 | Caveman | Concisão legível; preservar incerteza real e documentação normal; seleção/teste por projeto |
| 06 | ESLint/Biome | Escolha conforme stack e regras já funcionais; seleção/teste por projeto |
| 07 | Graphify | Mapa somente se complexidade justificar; versão/cobertura; seleção/teste por projeto |
| 08 | Obsidian | Memória externa opcional; seleção/teste por projeto |
| 09 | Claude memory | Conceito de memória adaptado, sem copiar credenciais; seleção/teste por projeto |
| 10 | Hooks | Mecanismo nativo suportado e validado, não duplicado; seleção/teste por projeto |
| 11 | agent-browser | Jornadas autorizadas com dados de teste; seleção/teste por projeto |
| 12 | Context7 | Consulta pontual; fallback fonte oficial; seleção/teste por projeto |
| 13 | Anthropic Skills | Origem/licença por componente; não importar cópias restritas; seleção/teste por projeto |
| 14 | Chrome DevTools MCP | Diagnóstico seletivo de console/rede/performance; seleção/teste por projeto |
| 15 | Codex workflow | Coordenação principal; instruções e integrações verificadas; seleção/teste por projeto |
| 16 | Vercel skills | Conforme frontend; não impor hospedagem; seleção/teste por projeto |
| 17 | Next.js runtime/performance | Somente Next compatível e necessidade real; seleção/teste por projeto |
| 18 | PostgreSQL | Somente dados PostgreSQL; não impor provedor/ORM; seleção/teste por projeto |
| 19 | GitHub CI repair | Conferir run/job/SHA/runner antes de alterar aplicação; seleção/teste por projeto |
| 20 | Security review | Revisão de contrato/diff, limites de acesso; seleção/teste por projeto |
| 21 | shadcn/ui | Candidata quando adequada; não design universal; seleção/teste por projeto |
| 22 | Sentry MCP | Opcional por serviço/conta/alçada; não ativar custo; seleção/teste por projeto |
| 23 | Harness² | Adaptação medida; framework/lab oficial não instalado; seleção/teste por projeto |

## O que não foi copiado como padrão

O prompt de máquina upstream autoriza instalações/atualizações globais e configuração de acesso amplo em seu próprio escopo. Aqui, essa alçada não é herdada. Nosso P07 apenas audita e P10 executa um plano autorizado.

O bootstrap upstream apresenta uma fundação Next.js e um conjunto de dependências. Nossa fundação deriva do PRD/TRD/design e do ambiente; preserva stack existente. Também preservamos as decisões próprias de main/produção e PRs DRAFT, sem impor ao usuário regras externas conflitantes.

Concisão de estilo não é retirar hesitação factual necessária. Menor solução não dispensa testes obrigatórios. RTK não torna chamadas/modelos gratuitos. A adaptação de Harness² não instala seu framework nem comprova seus benchmarks.

Licença MIT do toolkit observada no snapshot e aviso preservado. Skills e serviços ligados pelo catálogo têm condições próprias. Ver [FONTES](../fontes/FONTES_E_REVISOES.md) e [licenciamento](../LICENCIAMENTO.md).
