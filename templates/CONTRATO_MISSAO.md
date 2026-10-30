# Contrato de missão — TEMPLATE INATIVO

Missão: A_DEFINIR. Produto/destino: A_DEFINIR. Resultado e backlog: A_DEFINIR. Não confundir a pasta do kit com o aplicativo.

## Aprovação
Responsável; registro da autorização; início/fim ou duração máxima; ambiente; operações permitidas por recurso; exclusões; política de alteração de escopo. Uma janela de 24h não é autorização global.

## Prontidão
Evidências READY_LOCAL/CI/STAGING pertinentes e READY_UNATTENDED. Identidade/versão do supervisor e adaptadores; host; persistência; exclusividade; prova de parada/retomada; política de cancelamento. Sem supervisor comprovado, P17 permanece NÃO_INICIADA.

## Execução
Codex principal; colaboradores habilitados; modelos/provedores permitidos; dados compartilháveis; ferramentas; slots de recursos; responsáveis por Git/lockfile/schema; revisor independente e política de integração.

## Limites
Teto financeiro quando houver faturamento; quota; tempo por tarefa/missão; tentativas; concorrência; margem de segurança operacional; forma de medição/enforcement. Não converter tokens de assinatura em custo de API. Não usar plano pago adicional ou trocar conta sem autorização.

## Continuidade
Checkpoint, heartbeat/lease, identificação de efeitos externos, retomada, idempotência, pausa, bloqueios, fila sem tarefa e indisponibilidade do coordenador. Esperas não devem consumir LLM em polling constante.

## Encerramento
Condição de escopo concluído, orçamento, quota, risco, falta de alçada e cancelamento. Relatório verificável; processos/recursos próprios; pendências; status de publicação separado.
