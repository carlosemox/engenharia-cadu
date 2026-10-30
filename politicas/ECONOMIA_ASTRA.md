# Economia de tokens — Astra econômico, aplicada a todo o método

**Definição:** a política de eficiência é aplicada a 100% das etapas. Isso não significa economia de 100%, garantia de custo mínimo absoluto ou dispensa de qualidade. O padrão é Codex como principal, preservando o modelo escolhido pelo usuário. Colaboradores e modelos econômicos só entram dentro da seleção autorizada.

## O que otimizar

O alvo é custo total por entrega aceita: chamadas principais e de colaboradores, entrada, saída, cache quando observável, raciocínio quando exposto, ferramentas, compute, tentativas, revisão e retrabalho. Uma fatura de API não é equivalente à cota de assinatura. Em ambiente sem métrica monetária, registrar quota/consumo observado ou “não observado”; nunca inferir desconto medido da redução de texto.

## Contexto e instruções

Dar objetivo, fronteiras, entradas e aceites suficientes. Usar índice e busca para chegar à fonte correta, sem leitura integral do repositório a cada etapa. Reutilizar leituras quando o conteúdo continua disponível e válido; reler após mudança, dúvida material, perda de contexto ou requisito de segurança. Evitar ordens redundantes de “leia tudo”, “revise tudo” e “raciocine ao máximo”.

Manter documentos completos fora do contexto corrente e carregar detalhes quando necessários. Um comando de 900 palavras bem delimitado pode evitar retrabalho; não há limiar universal de tamanho ideal. Não cortar critérios técnicos apenas para reduzir tokens de entrada.

Manter instruções estáveis quando isso é coerente com o trabalho. Cache depende de cliente, provedor, modelo, prefixo e configuração. Não preservar contexto inútil ou ampliar prompts artificialmente apenas para tentar cache. Troca de cliente/provedor não cria memória ou cache compartilhado. Conferir comportamento na integração real.

## Ferramentas e saída

Usar scripts/verificadores determinísticos para busca, contagem, cálculo, parsing, lint, testes, comparação e acompanhamento de processos. Conferir scripts antes de executar. Uma ferramenta não dispensa autorização para seus efeitos.

RTK é candidato para filtros de saída em mecanismos suportados. Preservar exit code e diagnóstico, evitar wrappers duplicados e acessar saída original quando a decisão depende de detalhe. A redução informada pelo filtro não é economia total do modelo. Não ocultar stack trace necessário, warning ou dado para reduzir o relatório.

## Execução e delegação

Executar diretamente o trabalho simples. Delegar quando isola contexto relevante, traz especialização ou permite paralelismo real. Um dono por arquivo/recurso; operadores de Git coordenados. Não iniciar agentes para cumprir elenco nem rodadas de revisão sem objetivo. Cada colaborador recebe contrato suficiente e retorna resultado/evidência, não transcript completo.

Preservar o modelo autorizado. Menor esforço suficiente é uma hipótese operacional, não uma configuração universal. Arquitetura, segurança, dados e causas ambíguas precisam de capacidade adequada desde o início quando o risco exigir. Falta de credencial não se resolve elevando esforço.

## Verificação, repetição e espera

Definir aceites e riscos antes de mudar. Testar focalmente durante a iteração e executar os gates obrigatórios no marco pertinente. Não reduzir testes críticos nem repetir suíte completa por um ajuste documental que não a afeta. Reuso de evidência exige versão e justificativa de validade.

Duas tentativas sem informação nova acionam reavaliação da hipótese; não são autorização de tentativas pagas nem obrigação de gastar ambas. O contrato pode ser mais restritivo. Não continuar com fundamento falho ou esconder regressão.

Esperas por CI e ferramentas usam eventos/polling limitado implementado pelo controlador. Não fazer chamadas de LLM periódicas só para consultar status. Fila sem tarefa elegível encerra ou aguarda conforme política, sem geração artificial de backlog.

## Aprovação da política na prática

Medir P24 em tarefas comparáveis. Registrar baseline, candidato, versões, modelos, critérios, resultado e limites. A política está redigida; percentuais de economia e confiabilidade só poderão ser alegados depois dos respectivos testes.

Fontes oficiais consultadas: [revisão de prompts/skills para Astra](https://developers.openai.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra), [guia de modelos](https://developers.openai.com/api/docs/guides/latest-model), [cache](https://developers.openai.com/api/docs/guides/prompt-caching). Consulta: 29/10/2026. As regras acima são a adaptação proposta para o caso Cadu, não uma reprodução de resultados de benchmark.
