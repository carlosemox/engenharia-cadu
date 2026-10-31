# Case de eficiência — protocolo V2.3

Estado: DESENHADO / NOT_RUN. Nenhuma redução de tokens ou superioridade demonstrada nesta publicação.

## Pergunta e hipóteses

A metodologia revisada entrega tarefas aceitas com menos consumo total e intervenção humana, preservando qualidade e retomada? H1: memória estruturada reduz repetição. H2: consulta direcionada reduz exploração. H3: filtro de saída reduz contexto sem ocultar erros. H4: delegação seletiva reduz tempo; tokens podem aumentar. Avaliar cada hipótese separadamente.

## Desenho proposto

18 tarefas em três projetos autorizados ou públicos, seis tipos por projeto: compreensão, bug, mudança pequena, mudança entre módulos, interrupção/retomada e revisão. Reservar ao menos uma tarefa de cada projeto sem usá-la no ajuste. Tamanho é proposta de piloto, não suficiência estatística demonstrada. Registrar o conjunto antes de executar.

Braços: A método atual; B prompts/memória revisados; C B + um mecanismo de consulta; D C + um filtro de saída. Comparar também execução com um agente e com delegação nas tarefas independentes. Não mudar modelo e ferramentas ao mesmo tempo sem braço específico. Usar a mesma revisão inicial, dados, critérios e ambiente; reiniciar estado mutável e isolar memórias entre braços. Registrar e separar cache frio/quente. Alternar ordem, repetir conforme orçamento definido antes do teste e registrar todas as tentativas, inclusive interrupções.

## Registro obrigatório

run_id, task_id, project_id sanitizado, revisão inicial/final, hash da configuração, versão do método, cliente/modelo observados, ferramentas, braço, repetição, condições de cache, custo/preparação/indexação, tokens e origem dos contadores, duração, minutos humanos, aceites fixos, falhas, regressões e evidências. Campos indisponíveis são null. Não publicar transcrições privadas, credenciais ou identificadores de clientes.

## Métricas e denominadores

- Taxa de aceite = tarefas aceitas / tentativas avaliadas, com unidade explicitada.
- Tokens por entrega aceita = consumo somado de todas as tentativas e agentes / entregas aceitas. Sem aceites, resultado indefinido; nunca zero.
- Custo por entrega aceita inclui preparação e falhas; reportar investimento inicial e recorrente separadamente, sem amortização arbitrária.
- Tempo até aceite, minutos humanos, regressões, leituras redundantes e sucesso de retomada.
- Normalizar contadores do provedor sem somar duas vezes cache/raciocínio incluídos em totais. Proxy bytes/4, estimativa financeira e cobrança real têm colunas distintas.

## Aceite e promoção

Definir margem de qualidade, orçamento, repetições e limiares antes da execução. O executor não altera avaliador, testes de referência ou aceites. Preferir evidência funcional e revisão cega quando possível; julgamento por LLM é complementar e tem seu custo contado. Apresentar por tarefa e agregado, mediana e dispersão; intervalos/estatística somente com método declarado e dados adequados. Resultado inconclusivo não é sucesso. Promover só o componente que adicionou benefício; rollback significa desativar o adaptador e preservar os dados do estudo.

## Casos obrigatórios de recuperação e segurança

Memória desatualizada por alteração local sem commit; anexo em conflito com decisão aprovada; índice ausente; saída filtrada omitindo erro relevante; dois workers disputando arquivo; execução interrompida após efeito externo; log com segredo; autorização expirada ou fora do alvo; estudo privado tentando ir à central pública. Usar fixtures sanitizadas e ambientes descartáveis, sem explorar produção.

## Publicação do case

Publicar protocolo prévio, revisões, tarefas autorizadas, aceites, resultados completos e limites. Fornecer comandos reproduzíveis e instruções de isolamento. Título baseado no resultado observado, sem promessa universal. Verificações editoriais da biblioteca não são benchmark dos agentes nem auditoria dos aplicativos.
