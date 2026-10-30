# Contrato de integração dos executores — especificação, não adaptador executável

## Papéis

| Cliente | Papel | Regra |
|---|---|---|
| Codex CLI | Coordenador e implementador principal | Astra autorizado como preferência; não ampliar alçada |
| Antigravity CLI | Executor/revisor delegado | Só contrato delimitado e mecanismo verificado |
| Gemini CLI | Pesquisa, análise ou execução delegada | Confirmar acesso/autenticação; não presumir modalidade incluída |
| OpenCode | Executor com modelo/provedor aprovado | Não habilitar provedor, proxy ou cobrança por inferência |

A capacidade de executar uma tarefa é observada, não deduzida da marca. Não atribuir superioridade universal de design ou pesquisa a um cliente. Uma tarefa simples pode ser executada diretamente pelo Codex.

## Interface comum proposta

Entrada: task_id, mission_id, projeto/raiz, base/snapshot, objetivo, entradas/referências, fontes canônicas, paths/resources permitidos, ambiente, autorizações, cliente/modelo desejados, limites, critérios de aceite e formato de retorno.

Saída: task_id, status, cliente/modelo observados, versão/snapshot, alterações, comandos/checks, evidências, efeitos externos, bloqueios, consumo exposto, incertezas e próxima ação. Dados ausentes são null/desconhecido, nunca zero inventado.

O supervisor normaliza eventos; não toma texto “feito” ou exit code zero como DONE. O aceite vem dos testes e revisão da versão correta. O modelo pode não poder ver todo o contexto: forneça o necessário e referências acessíveis, sem copiar conversa completa.

## Compatibilidade a verificar no host

Versão/binário realmente executados; descoberta de instruções; mecanismo de skills; hooks sem duplicidade; MCP e permissões; modelo disponível; modo de auth; modo não interativo; eventos/saída estruturada; cancelamento; resume; tratamento de ferramenta negada; custos/quotas observáveis. Não produzir flags de versões diferentes como se fossem equivalentes.

As fontes oficiais consultadas documentam interfaces não interativas: Codex (`codex exec`), Antigravity/Gemini headless e OpenCode (`opencode run`). A configuração concreta depende da versão instalada; não fornecemos aqui comandos automáticos de instalação ou bypass de sandbox. Fontes S05–S08 em [FONTES](../fontes/FONTES_E_REVISOES.md).

## Isolamento e autoridade

Um processo não herda automaticamente autenticação de outro. Não mover auth.json, tokens OAuth ou chaves para o kit. Não usar assinatura pessoal de CLI como backend multiusuário do produto por inferência.

Bloquear delegação circular e fan-out recursivo não autorizado. Uma integração indisponível não autoriza fabricar saída. Revisor é somente leitura; testes de escrita em cópia autorizada. Filas/locks/políticas/orçamentos não são arquivos livremente alteráveis por workers.

## Piloto mínimo a executar depois

Tarefa de leitura; tarefa delimitada em cópia descartável; ferramenta recusada; tentativa fora de escopo; resultado com exit code normal mas aceite falho; interrupção e retomada; modelo real divergente do desejado; cota esgotada; segredo sintético; conflito de escritor.

Estado: todos os testes acima NOT_RUN nesta edição. Não há comunicação entre terminais implementada pelo simples fato deste contrato existir.
