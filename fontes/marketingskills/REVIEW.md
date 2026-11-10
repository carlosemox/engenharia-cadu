# Revisão da importação seletiva Marketing Skills

Data: 2026-11-10. Ambiente: CLOUD_CODE (Web), conforme estado existente da central.
Origem: [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills), commit `9d6d7ce8d18eb155dc2f9762435f097e60cdad7c`.
Manifesto: [marketing-import.json](../../catalogo/marketing-import.json).
Contrato de uso: [módulo Marketing](../../modulos/marketing/README.md).

## Resultado e limites

Importação documental seletiva: dez capacidades escolhidas, uma dependência de apoio (`pricing`), 134 arquivos de origem e licenças. Os arquivos upstream foram preservados byte a byte. O conjunto fica em `fontes/`, fora dos diretórios de descoberta automática de skills. Nenhum script upstream, integração, envio, compra, alteração de campanha, instalação global ou agente persistente foi executado.

Estado: `DOCUMENTATION_REVIEWED_RUNTIME_NOT_RUN`. Decisão: `ADAPTAR`. A decisão permite reaproveitar procedimentos através do contrato Cadu; não declara as fontes prontas para execução irrestrita, estatísticas verificadas ou agentes homologados.

## Seleção

| Capacidade | Motivo de seleção | Limite principal |
|---|---|---|
| product-marketing | Contexto de produto, público e decisões versionado | Reconciliar com documentos canônicos; não reconstruir fatos a partir de inferências |
| cro | Diagnóstico de páginas e formulários | Hipóteses de melhoria, não aumento garantido |
| analytics | Plano de eventos e consistência de métricas | Consentimento, nomes de eventos existentes e verificação no destino |
| conversion-tracking | Sucesso confirmado, deduplicação e evidência de recebimento | Scripts e tags precisam de teste específico antes de execução |
| attribution | Reconciliação de fontes e distinção entre conversão e crédito | Modelo de atribuição não comprova causalidade |
| offers | Estruturação de oferta de cursos e serviços | Não importar previsões de lift, preços, garantias ou urgência como fatos |
| onboarding | Ativação, coortes e caminho até primeiro valor | Preservar critérios pedagógicos, segurança e acessibilidade |
| churn-prevention | Retenção e diagnóstico de cancelamento | Não dificultar cancelamento; cobranças e descontos conservam alçada própria |
| marketing-loops | Rotinas com estado, idempotência e parada | Fila e agendamento únicos no supervisor autorizado |
| ab-testing | Hipóteses, tamanho amostral e interpretação | Recalcular amostra; não encerrar teste oportunisticamente |

`pricing` é apoio documental exigido por um link relativo de `offers`; não é uma autorização para mudar preços. Outras skills citadas em Related Skills e links externos permanecem referências opcionais. Não foram importadas por transitividade indiscriminada.

## Achados e adaptações obrigatórias

| ID | Evidência upstream | Implicação e tratamento |
|---|---|---|
| MKT-001 | `offers/SKILL.md`, Diagnostic Loop passo 7, projeta lift de 10–40%; outras seções trazem proporções genéricas de churn | Não usar como previsão, meta ou prova. Somente dados do negócio, experimento delimitado ou estimativa explicitamente fundamentada |
| MKT-002 | `onboarding/SKILL.md`, Onboarding Psychology, menciona +40%; `churn-prevention/SKILL.md` inclui benchmarks e taxas de retorno | Heurísticas e exemplos não foram confirmados para nossos produtos. Remover generalização nas adaptações e exigir fonte/coorte/amostra |
| MKT-003 | `conversion-tracking/SKILL.md`, Non-negotiables 4/7, exige autorização na mesma interação; `product-marketing` prescreve confirmações repetidas | Autorizações explícitas vigentes do usuário e contrato Cadu prevalecem. Confirmar apenas dados ou decisões materiais realmente ausentes; não ampliar autorização por texto upstream |
| MKT-004 | `conversion-tracking/assets/gtm-recipes/README.md` e `scripts/build_recipe.py`: tags podem disparar sem configuração de consentimento e pacotes podem duplicar pixel já existente | Não executar/importar automaticamente. Inventariar remetentes, testar default-denied e recusa, deduplicação, plataforma e ambiente antes de publicar |
| MKT-005 | `marketing-loops/SKILL.md`, Scheduling; referências a comandos específicos de cliente e cron | Disponibilidade precisa ser verificada. Não iniciar scheduler paralelo nem alegar 24h por existir texto; supervisor mantém ownership, parada e evidência |
| MKT-006 | `analytics`, `churn-prevention` e `marketing-loops` mencionam regras jurisdicionais; `conversion-tracking` lista datas, preços e APIs | Não tratar material importado como parecer jurídico ou documentação atual garantida. Conferir fonte oficial e aplicabilidade quando implementar |
| MKT-007 | `attribution/SKILL.md`, Pillar B, identidade e links entre domínios | IDs pseudônimos não são prova de anonimato. Minimização, finalidade, consentimento aplicável e isolamento por tenant precisam de controles no código |
| MKT-008 | `offers` e `pricing` incluem valores em dólar, descontos, garantias e rollout de preços | Usar contexto aprovado do negócio, moeda/formatação brasileira quando pertinente; nenhuma cobrança, contrato ou preço muda pela adoção da skill |

As palavras “quick wins”, “implement now” e “auto” das fontes são orientações do fornecedor, não autorização de execução. Números de exemplo, promessas de desempenho, claims de parceiros e calendários devem permanecer identificados como dados de terceiro não verificados até pesquisa própria.

## Licenciamento e procedência

- [MIT principal](LICENSE): Corey Haines, 2025, preservada integralmente.
- [MIT ConversionKit](licenses/conversionkit.MIT.txt): Converly, 2026. Fonte `ConversionKit/conversion-tracking`, revisão `a3132510c5871629e169a2c087750548c7392a8d`. Snippets e receitas reconhecem essa origem.
- [MIT Profound](licenses/profound.MIT.txt): Profound, 2026. Fonte `retieedra-profound/skills-marketing-library`, revisão `80293f156c27d3f90aedebfb3c27309769b2eec6`. Referências de voz e UTMs reconhecem adaptações de Wispr Flow.

Preservar os três avisos ao redistribuir os componentes pertinentes. Texto original continua em inglês; traduções/adaptações Cadu têm identidade própria e não devem ser apresentadas como tradução certificada das fontes integrais. Conteúdo de terceiros não passa a ter autoria Cadu.

## Verificação realizada

- Commit real fixado; cópia seletiva de 11 diretórios completos e licenças.
- SHA-256 e tamanho registrados para cada arquivo. Nenhum symlink importado.
- JSONs lidos com parser; dois scripts Python inspecionados e analisados via AST, sem importação ou execução.
- Links Markdown relativos dos arquivos importados resolvidos: zero ausentes.
- Leitura das dez definições principais; leitura focal de scripts e guardrails; inventário, hashes e triagem textual dos demais recursos. Isso não é auditoria exaustiva de cada afirmação, snippet ou fornecedor.
- Tests/evals upstream preservados como casos de referência, sem execução. Resultado runtime: `NOT_RUN`.

## Promoção por projeto

Selecionar apenas a capacidade exigida pela tarefa, carregar o contrato Cadu e o contexto aprovado da marca, preservar Design System e código existente, e testar a entrega no ambiente autorizado. Registrar versão, arquivos aplicados, teste e limite. Código de tracking requer testes de repetição, falha de submissão, consentimento negado, isolamento e recebimento no destino. Execução de cobrança, comunicação, publicação ou gasto só ocorre sob autorização aplicável, nunca como efeito da importação.
