# 2026-11-08 — Supervisor de auditoria supervisionada

- Fila SQLite transacional para auditorias read-only, com dependências, leases,
  heartbeat, parada, prazo, limite de claims e revisão por identidade distinta.
- Comando OPERAR_SUPERVISOR em português, inglês e espanhol e rota na fábrica.
- Piloto real Codex web: duas tarefas documentais revisadas, dependência e parada
  registradas em docs/harness/OPERATIONAL_EVIDENCE.md.
- Mantidos gates para sandbox, host persistente, custos, escrita de código,
  integração de produto Graphy e produção. Não há operação autônoma 24 horas.

# 2026-11-04 — Consolidação D01 / P00–P30

- D01 registrado nas rotas e no estado operacional.
- P29/P30 alinhados ao formato canônico e incluídos nas narrativas PT/EN/ES.
- Sincronizador e validador atualizados para reproduzir a biblioteca P00–P30 sem drift editorial.

# 2026-11-04 — D01 — Descoberta controlada de skills

- Integrado `find-skills`, `npx skills find`, `skills use`, `skills check` e o diretório skills.sh como mecanismos de descoberta, não instalação automática.
- P08 passa a descobrir candidatos por necessidade; P22 mantém a auditoria obrigatória antes de piloto/instalação.
- Escopo de projeto é preferido; instalação global, `-y`, `--all` e atualização automática não são padrão.
- Módulo D01 publicado em português, inglês e espanhol; narrativa trilíngue atualizada.
- Fonte upstream fixada para esta integração em `vercel-labs/skills@9197d919034d19010ae303cf96bf19ad087dd4be`; execução da CLI permanece NOT_RUN nesta atualização documental.

# 2026-11-01 — Runtime V3 Astra 6

- Modernizados P00–P30 com contrato comum V3, Harness, Loop e Graph.
- Catálogo, fábrica, comandos, espelhos publicados e site sincronizados para 31 prompts.
- Adicionados P29 anti-clonagem e P30 de execução econômica.

# Histórico

## 2.3.0 — 31/10/2026

- Entrada única CADU, fábrica local/web e comandos completos para assumir estudos e reestruturar projetos.
- Contexto por fontes e validade, contratos de tarefas, retomada e segurança integrados aos 31 procedimentos.
- Catálogo documental de candidatos e protocolo reproduzível do case de eficiência, ainda NOT_RUN.
- Kit de adoção conectado por revisão fixada; nenhuma instalação de terceiros ou migração de aplicativos por implicação.

## 2.1.0 — Central publicável
- Biblioteca V2 completa preservada com caminhos curtos `p/P00.md` a `p/P28.md`.
- Site estático com busca, filtros, explicação por etapa, atalhos Read e cópia do comando completo.
- Papéis originais da engenharia e catálogo de capacidades com estados explícitos.
- Estrutura híbrida: metodologia pública; operação e avaliações detalhadas privadas.
- Publicação documental não equivale a instalação de clientes, testes dos prompts ou supervisor de 24 horas.

## 2.0 — Biblioteca documental
- 31 procedimentos detalhados; economia de contexto, design desde o briefing e serviços/APIs planejados.

## 2.2.1 — organização editorial de 30/10/2026
Navegação única para continuidade, segurança, backup e implantação; página P01 integrada e comando completo copiável; mapa de fontes; templates de revisão e recibo. Preservados IDs P00–P30 e políticas operacionais. Esta publicação não ativa runtime, auditoria dos aplicativos ou backups automáticos.

## Módulo S01 — 30/10/2026
- Novo módulo de auditoria incremental, preservando o prompt universal fornecido pelo usuário.
- Três marcos (início, meio e pré-release) e nove eventos lógicos; modos AUDIT/PLAN/FIX/VERIFY separados.
- Verificador determinístico de recibos, wrappers inativos e testes sintéticos, sem scanners/CI instalados nos aplicativos.
- Políticas e índices existentes atualizados no mesmo caminho; P00–P30 e workflows preservados.

## Apresentação trilíngue — 30/10/2026
- Copy e narrativa próprias em português brasileiro, inglês e espanhol, com 14 capítulos equivalentes e descrições dos 31 procedimentos.
- README principal atualizado; traduções separadas em `i18n/`; páginas em `/`, `/en/` e `/es/`.
- Seletor de idioma, metadados por idioma, navegação responsiva e progressiva, busca e cópia de comandos sem serviços externos.
- Biblioteca interativa anterior preservada em `docs/biblioteca.html`; guias, prompts e S01 mantêm seus caminhos e idiomas originais.
- Gerador a partir das fontes editoriais, testes de consistência e verificação de idioma por caminho.
- Não ativa hooks, backups, scanners, supervisores ou configurações dos aplicativos. Verificações e limites em `avaliacoes/APRESENTACAO_TRILINGUE.md`.
