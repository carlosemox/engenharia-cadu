# S01 — Segurança no início, durante e antes da publicação

**Investigar → priorizar → planejar → corrigir o lote aprovado → verificar → prosseguir.**

Módulo adicional da Engenharia Cadu. O [prompt universal completo](PROMPT_UNIVERSAL.md), fornecido pelo usuário, permanece em inglês, sem redução de suas fronteiras; entrada e orientação de uso em português. Não pressupõe aplicação web, Node.js, GitHub, Supabase ou fornecedor de IA. Não renumera P00–P28.

## Três marcos e verificações durante o trabalho
| Momento | Objetivo | Evento lógico |
|---|---|---|
| INÍCIO — antes do primeiro lote de implementação | Escopo, ameaças, dados, permissões, stack, controles e plano de cobertura. Sem código ainda, revisar o desenho sem inventar varredura. | project-start |
| MEIO — primeiro incremento integrado, depois por marco relevante | Rever interfaces entre módulos, regras compartilhadas, regressões e cobertura acumulada. Não é uma porcentagem arbitrária do cronograma. | integration-review |
| FIM — antes de cada publicação | Rever o candidato exato, achados, testes, configuração, revisão independente e recuperação. | pre-release |
| DURANTE — cada lote/módulo e saída de etapa | Checks direcionados ao delta, chamadores e fronteiras afetadas; política do evento determina o que é obrigatório. | module-complete / phase-exit |
| DURANTE — versionamento e manutenção | Checks rápidos locais, CI na revisão proposta e atualização periódica de advisories. | pre-commit / pre-push / pull-request / scheduled |

**Não é uma auditoria total em cada edição de arquivo.** Checks rápidos usam ferramentas determinísticas. Uma revisão aprofundada usa S01, por risco e escopo. Isso reduz repetição e consumo sem dispensar controles.

## Comando de entrada
```text
Read https://raw.githubusercontent.com/carlosemox/engenharia-cadu/main/modulos/seguranca/read.md

Modo: AUDIT.
Organize a campanha de segurança deste projeto no início, nos marcos intermediários e antes de publicar. Comece pelo estado atual e pelas superfícies de maior risco.
Preserve o código; testes ativos desativados. Não instale ferramentas ou hooks durante a auditoria. Apresente evidências, cobertura e o primeiro lote recomendado.
```

A campanha avançada é opt-in: autorizar uma campanha para o projeto pode cobrir seus marcos e lotes definidos, sem novas colagens, mas não autoriza FIX, alvos adicionais, custos ou testes ativos. A segurança básica permanece transversal ao método. No onboarding, planejar os controles; não iniciar o workflow avançado silenciosamente. A solicitação para publicar esta biblioteca não inicia auditorias dos aplicativos.

## Modos distintos
| Modo | Ação | Muda o projeto? |
|---|---|---|
| AUDIT | Inventário, modelo de ameaças, análise e achados | Não |
| PLAN | Plano e comando detalhado do primeiro lote | Não |
| FIX | Correção dos achados/lotes explicitamente selecionados | Somente o autorizado |
| VERIFY | Reteste dos achados e comparação com o critério | Não |

Código alterado não é correção comprovada em produção. NOT_RUN, timeout, erro e job ignorado não viram PASS. Relatórios e recibos ficam privados. Sem garantia de ausência de invasões.

## Conteúdo do módulo
[Entrada S01](read.md) · [Roteiro e rastreabilidade](POR_ETAPAS.md) · [Hooks e implantação](hooks/README.md) · [Templates](templates/README.md) · [Fontes](FONTES.md) · [Validação](validacao/RESULTADOS.md)

O verificador de recibos e os wrappers foram feitos para integração posterior. Não contêm scanners, não iniciam modelos, não instalam ferramentas e não configuram CI. **PASS valida os campos do recibo; não autentica seu produtor nem certifica a aplicação.** Um job confiável precisa produzir e conferir a evidência real fora do alcance de quem implementou a mudança.

[Política transversal](../../politicas/SEGURANCA_ENGENHARIA.md) · [Central](../../README.md)
