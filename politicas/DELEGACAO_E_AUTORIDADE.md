# Delegação e autoridade

## Decisão humana, trabalho técnico, controle real

Cadu define produto, prioridades, alçadas e publicação. Codex coordena tecnicamente, implementa e integra. Supervisor e ambiente aplicam limites; texto do prompt não concede poderes nem implementa segurança. Antigravity, Gemini CLI e OpenCode são colaboradores selecionados por tarefa, condicionados a acesso, versão, mecanismo e licença efetivos. Claude Code não é dependência obrigatória.

## Contrato do colaborador

Enviar objetivo, requisito, base/snapshot, instruções pertinentes, fontes necessárias, arquivos autorizados, recursos mutáveis, proibições, aceites, checks, limites e formato de retorno. Compartilhar somente os dados permitidos para aquele provedor/cliente. Não copiar tokens ou sessões entre clientes.

O trabalhador modifica apenas seu escopo, verifica e devolve resultado. O revisor permanece somente leitura; testes com artefatos ou serviços precisam de ambiente próprio. Codex reconcilia resultados e não aceita autorrelato como prova. Nenhum colaborador delega circularmente ou assume direção sem política explícita.

## Ações separadas

Leitura autorizada não concede execução de scripts. Aprovação de briefing não concede criação de recurso. Implementação não concede commit. Commit não concede push. Push não concede merge. Merge não concede deploy. Deploy não concede migração destrutiva. Teste verde não concede produção. Gastos e alteração de segredos exigem alçadas próprias.

É possível pré-autorizar ações recorrentes: branch/destino/ambiente, arquivos, recurso, validade, teto e exclusões devem estar identificados. Não pedir a mesma autorização a cada passo; também não alargar seu alcance. Exemplo de contrato permanece inativo até o usuário aprová-lo.

## Controle de estado

Tarefa tem um proprietário e uma revisão de entrada. Lockfile, schema, Git, portas e bancos de teste são recursos coordenados. Worktree não isola rede, credenciais ou serviços. Um lease expirado exige confirmar parada ou bloquear escrita tardia antes de transferir posse.

Checkpoint contém identidade da execução, versão/snapshot, alterações, aceites, testes, recursos e IDs externos. Resumo não substitui registro durável. Retry externo exige reconciliar efeito; cancelamento local não garante cancelamento remoto.

## Estados

PLANEJADO, EM_EXECUCAO, AGUARDANDO_REVISAO, CONCLUIDO_NO_ESCOPO, BLOQUEADO, AGUARDANDO_DECISAO, CANCELADO. Verificações usam PASS, FAIL, BLOCKED, NOT_RUN, NAO_APLICAVEL. Readiness por ambiente continua separado do estado da tarefa e do GO.

## Substituição e falha

Codex indisponível não autoriza promoção automática de outro cliente. Trabalho já delegado pode concluir seu contrato; o supervisor preserva estado e aguarda/reencaminha apenas segundo política aprovada. Limite de quota não autoriza rodízio de contas, cobrança nova ou envio a modelo gratuito sem avaliar dados.
