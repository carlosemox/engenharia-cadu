# Matheus → Cadu: o que foi preservado e o que foi adaptado

Base versionada e fontes em [FONTES_E_REVISOES.md](FONTES_E_REVISOES.md). O projeto original não define a autorização dos projetos Cadu. Prompt 10 do Matheus não é P10 Cadu.

## Diferenças deliberadas

| Referência | Princípio preservado | Decisão Cadu |
|---|---|---|
| 04 — Brainstorm to plan | Entender antes de implementar; plano com verificação | P01–P06 separam descoberta, D0, PRD, experiência e engenharia; informação já aprovada não é perguntada novamente |
| 10 — Environment setup | Inventário, backup, mecanismos oficiais e prova | P07 começa em leitura; configuração global somente com escopo aprovado; não transportar full access/no approvals indiscriminadamente |
| 11 — New project | Atalho, comando completo e foundation validada | P09 usa stack escolhida por produto; não impõe Next.js/Drizzle ou instala todas as skills web |
| 12 — Existing project | Preservar aplicação e adaptar catálogo | P20 diagnostica; P21 executa reparo e adoção por lotes; preserva proteções e alçadas Cadu |
| 05 — Waves | Dependências, arquivos e recursos isolados | P12/P13/P17 coordenam workers e Git; presença de quatro clientes não exige uso simultâneo |
| 06 — Memory | Índice pequeno e conhecimento por relevância | Handoff temporário separado de decisão durável; fontes e invalidação; nenhum vault novo obrigatório |
| 03/13 — Review | Alvo exato, leitura, cenário concreto, privacidade | P14 usa risco e evidência, não painel universal nem autoaprovação |
| 14 — Evaluation | Fixture e avaliador protegidos | P11/P24 definem provas; arquivo de avaliação presente não significa teste executado |
| 15 — Improvement | Experimento delimitado inspirado em Harness² | P24 mantém adaptação nativa separada do laboratório oficial; não inventa framework ativo |
| Produto/integrações | Não inventar serviços ou credenciais | P08 possui matriz própria de serviços/APIs, solução transitória, custo, contingência e saída |

## Cobertura das 23 frentes do catálogo

Esta tabela cobre seleção, não auditoria do código de todos os upstreams. Em cada projeto, a decisão concreta deve ser registrada em P08.

| Frente | Tratamento proposto |
|---|---|
| Superpowers | Método proporcional e sem cerimônias que repitam autorização existente |
| Subagentes | Delegação seletiva, contexto suficiente, dono por recurso |
| RTK | Filtragem suportada, saída original e métricas reais; sem wrappers duplicados |
| Ponytail | Menor solução completa, preservando requisitos |
| Caveman | Comunicação objetiva sem reduzir clareza de artefatos/código |
| ESLint/Biome | Ferramenta da stack, regras verificáveis e sem redundância |
| Graphify | Mapa quando necessário, com exclusões e validade; sem provider pago implícito |
| Obsidian | Memória externa opcional, não pré-requisito |
| Memória Claude/cliente | Adaptar conceitos ao cliente real; não copiar configuração incompatível |
| Hooks | Somente mecanismos suportados, escopados e comprovados |
| agent-browser | Jornadas autorizadas com dados/contas de teste |
| Context7 | Consulta de versão/conceito pertinente; fonte oficial alternativa quando necessário |
| Skills de artefatos/Anthropic | Procedência e licença por componente; nenhuma instalação em massa |
| Chrome DevTools MCP | Diagnóstico de console/rede/performance quando aplicável |
| Workflow Codex | Coordenador principal e configuração nativa validada |
| Vercel skills | Capacidade pertinente à stack; não impõe hospedagem |
| Next.js runtime/performance | Condicional a projeto e versão compatíveis |
| PostgreSQL | SQL/índices/migrações/pool/segurança quando adotado; não impõe Supabase |
| GitHub CI repair | Runner/evento/versão e causa, sem disparos ou despesas não aprovados |
| Security review | Relatório privado com evidência e escopo |
| shadcn/ui | Somente design system selecionado e compatível |
| Sentry MCP | Serviço, projeto e acesso autorizados; não cria conta/SDK por implicação |
| Harness² | Melhoria medida; laboratório oficial separado e opcional |

## Sem promessa de “prompt perfeito”

O comando deve ser completo e verificável. Sua robustez depende de alvo, dados, modelos, ferramentas, permissões e testes. Redação detalhada não elimina erro. A biblioteca deve ser ajustada por evidências de pilotos, não por adicionar adjetivos ou repetir regras.
