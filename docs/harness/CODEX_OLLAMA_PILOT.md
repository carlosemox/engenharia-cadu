# Codex + Ollama no Mac

[Português](CODEX_OLLAMA_PILOT.md) · [English](CODEX_OLLAMA_PILOT.en.md) · [Español](CODEX_OLLAMA_PILOT.es.md)

Versão / atualização: **1.3.0 · 2026-11-08T21:40:46-03:00 · America/Sao_Paulo**

**PREPARAÇÃO APROVADA — HOMOLOGAÇÃO OPERACIONAL PENDENTE.**

Cadu aprovou a preparação, organização, tradução e publicação deste incremento. O Mac foi escolhido como executor; está desligado e indisponível para instalação. Esta aprovação não transforma testes documentais em testes do modelo.

## Graphify — homologação delimitada

**CONEXÃO E INDEXAÇÃO VALIDADAS; HOMOLOGAÇÃO COMPLETA DO ECOSSISTEMA PENDENTE.**

A reinstalação iniciada pelo workspace e a verificação da conta administradora corrigiram o vínculo GitHub. O painel passou a reconhecer 69 repositórios da conta pessoal autorizada. Instalações em organizações separadas não foram comprovadas.

| Verificação | Resultado observado |
| --- | --- |
| Associação GitHub ao workspace Engenharia Cadu | PASS |
| Repositórios reconhecidos | 69; reconhecimento não equivale a indexação |
| Builds observados | 3 concluídos com sucesso, 0 falhas e 0 em execução |
| engenharia-cadu | Indexed; 493 nós; revisão c3a930148c73532af47cfa678065a1da0b977e40 |
| Total apresentado pelo painel | Aproximadamente 11,9 mil nós nos três builds |
| Consulta real por Codex/MCP | NOT_RUN; conexão de conta não comprova consulta |
| Indexação de todos os 69 | BLOCKED_PLAN; não concluída |
| Supervisor, Ollama e isolamento no Mac | Não instalados/testados nesta entrega |

O painel Free recusou ativações adicionais com limite de três repositórios e indicou limite de 25 mil nós por repositório. Não presumir que finalizar um build libera uma vaga: a mensagem também orienta desativar um repositório ou alterar o plano. Não desativamos índices válidos para contornar esse limite. Nenhum plano pago foi contratado. A instalação autorizada mantém acesso a todos os repositórios da conta, com leitura de issues/metadados e leitura/escrita de checks, código e pull requests; isso não autoriza alterações autônomas.

Evidência observada no navegador autenticado: [builds do workspace](https://app.graphify.com/engenharia-cadu/builds). A homologação vale para os resultados observados e a revisão identificada, não para o novo commit desta publicação, outros repositórios ou segurança integral do fornecedor. Nomes de repositórios privados e credenciais foram omitidos desta publicação pública.

Próximo gate: testar consulta autenticada pelo Codex/MCP sobre o índice pronto, conferindo símbolo e localização contra a revisão indexada. Depois, definir cobertura e orçamento antes de ampliar o plano. Agentes externos continuam candidatos, sem homologação individual presumida.

## Arquitetura e custos

Codex conduz as tarefas de programação; Ollama executa um modelo local; o supervisor coordena fila, limites, revisão independente e evidências. Um modelo local não é o mesmo modelo OpenAI usado pelo Codex com ChatGPT.

Não foi contratada API nem nova assinatura. A proposta anterior de R$ 50,00 fica como alternativa não ativada, sem aprovação de gasto. Inferência local não cobra tokens de API, mas utiliza hardware, energia e armazenamento. Sem fallback automático para cloud ou API paga. Modelo, licença e capacidade para usar ferramentas dependem de validação.

## Evidências e limites

| Item | Estado observado |
| --- | --- |
| Regressão da preparação | 184 testes Python aprovados |
| Revisão independente | Preparação revisada; ajustes incorporados |
| GitHub | Conta carlosemox confirmada; permissões admin/push/pull informadas pela API |
| Codex CLI | Versão 0.167.0 instalada apenas no ambiente temporário |
| Login ChatGPT | Credenciais reconhecidas; nenhum valor de segredo exportado |
| Acesso ao modelo OpenAI | Chamada mínima terminou em timeout de 60 segundos; acesso e quota não comprovados |
| Mac | Escolhido pelo usuário; hardware e macOS ainda não inspecionados; dispositivo não conectado |
| Ollama no Mac | Instalação, modelo e integração não verificados |
| Supervisor fora da conversa | Não ativado nem homologado |
| Agentes externos | Catalogados; sem homologação individual presumida |

O ambiente inspecionado nesta conversa é Linux temporário, com limite de 8 GiB de RAM e oito CPUs por quota, 57,7 GiB livres observados e nvidia-smi indisponível. Esses dados não descrevem o Mac. Ollama não estava instalado nesse ambiente. OPENAI_API_KEY e CODEX_API_KEY estavam ausentes ou vazias.

## Instalação posterior no Mac

1. Conectar o Mac e registrar processador, RAM/VRAM, espaço livre, macOS e instalações existentes.
2. Selecionar versões verificadas de Codex e Ollama e um modelo local com licença adequada, ferramentas e digest registrado.
3. Configurar somente loopback, cloud desativada e contexto compatível com a memória. A documentação Ollama recomenda ao menos 64k tokens para Codex; isso precisa caber na máquina.
4. Validar resposta local, ferramentas, isolamento, timeout, parada, retomada e ausência de efeitos duplicados em fixture sem segredos.
5. Resolver uma pequena correção em checkout descartável, executar testes e obter revisão independente do diff. Medir tempo e memória.
6. Integrar ao supervisor e testar persistência e agendamento somente depois dos gates. Este piloto não autoriza autoaprovação, merge/deploy de aplicativos nem homologação de todo o catálogo.

## Comandos preparados, ainda não executados no Mac

Iniciar apenas se não houver servidor existente. Se houver, conferir sua configuração e reiniciar o serviço adequado, sem duplicá-lo.

```sh
OLLAMA_NO_CLOUD=1 OLLAMA_HOST=127.0.0.1:11434 OLLAMA_CONTEXT_LENGTH=65536 ollama serve
```

Substituir MODEL_NAME pelo nome exato do modelo instalado. O contexto é uma meta de ensaio, não uma garantia de memória suficiente.

```sh
codex exec --oss --local-provider ollama --model MODEL_NAME --sandbox read-only -c 'web_search="disabled"' 'Reply CADU_OLLAMA_OK without using tools.'
```

Ollama local não é sandbox dos comandos do agente. O bloqueio real do sandbox deve ser testado no Mac. Não copiar autenticação pessoal ChatGPT para o workflow público de CI.

## Verificador de acesso

`python scripts/check_codex_access.py` consulta somente versão e login; aceita `--codex-bin` com executável confiável. Não lê auth.json diretamente, não exporta saída bruta, não chama modelo nem inicia serviço. Credencial presente não comprova conexão, quota, modelo ou isolamento. Esse diagnóstico é da rota ChatGPT; Ollama local não exige login OpenAI.

## Próximo marco

**MAC_CONNECTED → HARDWARE_CHECKED → LOCAL_MODEL_TESTED → ISOLATION_VERIFIED → PILOT_REVIEWED.** A publicação desta página encerra a preparação aprovada, não a homologação operacional.

## Referências

- https://learn.chatgpt.com/docs/auth
- https://learn.chatgpt.com/docs/non-interactive-mode
- https://learn.chatgpt.com/docs/cli/reference
- https://docs.ollama.com/integrations/codex
- https://docs.ollama.com/faq
