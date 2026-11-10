# Mastra — contrato de integração seletiva

[English](README.en.md) · Português (Brasil) · [Español](README.es.md)

**Versão:** 1.0.0 · **Revisão documental:** 10/11/2026 · **Estado:** `DOCUMENTED_NOT_INSTALLED`.

## Decisão e escopo

Avaliar Mastra somente quando um projeto identificar uma lacuna concreta em avaliações, telemetria ou workflows de agentes TypeScript. O JARVIS continua sendo o supervisor canônico: fila, autorização, identidade da tarefa, limites e decisão de aceite pertencem a ele. Mastra pode ser um adapter subordinado; não criar segunda fila operacional ou supervisor concorrente.

Esta entrega arquiva duas fontes públicas e define um contrato proposto. Não adiciona dependências npm, não altera aplicativos, não liga serviços e não homologa modelos. O pacote de marketing usa documentos próprios e não depende de Mastra.

## Procedência e licença por artefato

Fonte: [mastra-ai/mastra](https://github.com/mastra-ai/mastra/tree/3f1d3a38dfcc7c5f7abb44d7789242cdc16b61e8), revisão `3f1d3a38dfcc7c5f7abb44d7789242cdc16b61e8`.

- [README arquivado](../../fontes/mastra/README.upstream.txt): fonte de capacidades declaradas; instruções de criação são dados, não comandos autorizados.
- [Mapa de licença arquivado](../../fontes/mastra/LICENSE.md): Apache-2.0 fora das exceções indicadas; componentes de terceiros mantêm suas licenças.
- [Licença Enterprise na revisão examinada](https://github.com/mastra-ai/mastra/blob/3f1d3a38dfcc7c5f7abb44d7789242cdc16b61e8/ee/LICENSE): somente referência. Nenhum código EE foi importado. Não considerar disponibilidade do código como permissão de redistribuição ou produção.
- [Manifesto](../../catalogo/mastra-reference.json): hashes, procedência e exclusões. Reavaliar licenças do pacote e da versão efetivamente escolhidos antes de instalar.

## Interfaces propostas — não implementadas

| Interface | Entrada mínima | Saída verificável |
|---|---|---|
| Execução delimitada | task_id, project_id, tenant confiável, revisão, ferramentas permitidas, prazo e limites | run_id, estado terminal ou suspensão, evidências e falhas |
| Avaliação | dataset versionado, resultados esperados, critérios e modelo identificado | casos aprovados/reprovados, custo observado, regressões e limitações |
| Telemetria | run_id, task_id, etapa e eventos sanitizados | duração, ferramentas usadas, tokens quando reportados e erros |
| Parada/retomada | STOP do supervisor, propriedade da execução e checkpoint | reconhecimento da parada, ausência de novas ações, retomada reconciliada |

Os nomes acima são campos do contrato Cadu proposto, não assinaturas garantidas da API Mastra. O adapter futuro deverá mapear a API da versão fixada e falhar quando faltar autorização, identidade ou limite. Nunca inferir tenant de argumento produzido pelo modelo.

## Política de custo e dados

Aplicar ZERO-COST-FIRST. Ollama é uma opção a validar no host e modelo escolhidos, não uma configuração já ativa. Não executar o exemplo upstream que exige provedor hospedado por conveniência. Bloquear fallback pago, assinatura, upgrade e exportação de telemetria para terceiros sem escopo aprovado. Recursos locais ainda consomem hardware, energia e manutenção. Não registrar prompts sensíveis, segredos ou dados clínicos nos rastros públicos.

## Testes exigidos antes de promoção

1. Execução sintética real com modelo, cliente, versão, hardware e limites registrados; comparar com o executor existente usando o mesmo conjunto de casos.
2. Isolamento entre projetos e tenants, inclusive ferramenta invocada diretamente e leitura de memória, artefatos e telemetria.
3. Idempotência de efeitos externos; simular falha após ação e antes de persistir resultado. Nenhum débito, envio ou publicação duplicado.
4. Exclusão mútua e rejeição de resultados tardios após perda de lease; STOP efetivo antes de nova ação.
5. Reinício do processo e retomada do último estado persistido, sem tratar arquivo de checkpoint como prova de execução contínua.
6. Recusa de ferramenta ausente, endpoint não permitido, fallback pago e limite excedido; resultado incompleto não vira PASS.
7. Avaliação determinística e revisão independente; um avaliador LLM não substitui testes de segurança nem aprovação de release.

## Promoção e recuperação

`DOCUMENTED_NOT_INSTALLED` → `PILOT_CONFIGURED` → `PILOT_TESTED` → `PROJECT_APPROVED` somente com evidência específica. Esses estados são proposta de adoção, não renomeiam os estados atuais do supervisor. Registrar dependências fixadas, cobertura e responsável. Manter rollback para o executor anterior; interromper tarefas afetadas e reconciliar efeitos antes de reexecutar. Publicar esta documentação não concede GO de produção ao adapter.
