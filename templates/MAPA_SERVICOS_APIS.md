# Mapa de serviços e APIs — TEMPLATE INATIVO

Esta matriz descreve dependências do produto. Ferramentas como Codex e linter pertencem a outro catálogo.

| Campo | Preenchimento necessário |
|---|---|
| Capacidade e requisito | O que o usuário precisa fazer e qual requisito depende disso |
| Estratégia | Construir / reutilizar / contratar / integrar / manual inicial / adiar |
| Alternativas | Opções reais que cumprem restrições essenciais |
| Decisão e responsável | Recomendação versus aprovação efetiva |
| Fornecedor, plano, API/SDK, versão | Identificação verificada, não apenas marca |
| Fonte e data | Documentação oficial e condição observada |
| Permanência | Inicial / transitória / sem substituição planejada |
| UX | Link externo / embed suportado / integração de backend / outro |
| Dados | Transmitidos, armazenados, região/retenção quando relevante |
| Autenticação e escopos | Modalidade e mínimo privilégio; sem credenciais |
| Contrato | Entrada, saída, erros, eventos, compatibilidade |
| Operação | Timeouts, tentativas, quotas, idempotência, reconciliação |
| Custo | Preço verificado ou não verificado, drivers e limite aprovado |
| Preparação | Conta, plano, aprovação, sandbox e variáveis por nome |
| Prova | Teste positivo/negativo, versão, resultado e evidência |
| Contingência | Experiência e operação diante de indisponibilidade |
| Saída | Exportação, portabilidade, mapeamento de IDs e gatilho de revisão |

## Exemplo de aplicação, não uma escolha de fornecedor

Para aula ao vivo, fechar interação versus transmissão, capacidade, simultaneidade, gravação, presença, moderação e acesso. A plataforma pode manter matrícula e agenda enquanto um serviço opera a sala. Isso é uma hipótese de arquitetura a aprovar. Verificar se o formato de acesso e a API realmente existem no plano. Solução própria futura depende de decisão, não é destino obrigatório.

## Evidência por estado

NECESSIDADE_IDENTIFICADA → ALTERNATIVAS_VERIFICADAS → DECISAO_APROVADA → CONFIGURADA → OPERACAO_TESTADA → JORNADA_HOMOLOGADA. Uma variável preenchida não salta etapas.
