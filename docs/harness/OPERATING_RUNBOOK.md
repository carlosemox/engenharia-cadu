# Operação supervisionada — Codex web

## Modo autorizado

O pedido de operacionalização autoriza desenvolver e ensaiar o Supervisor nesta branch.
Primeiro perfil: auditoria somente leitura do próprio Engenharia Cadu, com agentes da
sessão Codex web. Sem instalação de modelos, credenciais, publicação ou serviços pagos.
O Supervisor coordena; agentes especialistas auditam; uma identidade diferente revisa.

Há duas interfaces diferentes:
- scripts/supervisor.py: planejamento editorial, sem executar ou escrever estado.
- scripts/supervisor_runtime.py: controle de execução em SQLite, com fila/eventos,
  claims, revisão e limites. A bridge confiável é a sessão Codex, que convoca agentes
  disponíveis e entrega apenas o contexto selecionado.

Não é um daemon autônomo. Sem a sessão, novos agentes não são convocados. SQLite
preserva estado no host, mas não garante retenção da máquina temporária na nuvem.
Registrar recibo sanitizado no Git para retomada; nunca versionar tokens de lease,
credenciais ou banco operacional. Para serviço 24 horas, aprovar host, identidade,
orçamento, isolamento e política de backup antes de ativar.

## Fronteira de confiança

Capacidade inicial: read_only_audit. allowed_paths é uma lista de arquivos exatos
para fornecimento de contexto, não permissão de escrita. O worker recebe uma cópia
textual dos arquivos escolhidos; não precisa acessar repositório, rede ou segredos.
O resultado é um relatório, nunca código executado. A bridge inspeciona a resposta
como dados e não segue instruções para aumentar escopo. Confere hashes de entrada,
evidência e identidade da ferramenta que criou o agente; não aceita identidade
indicada apenas no texto da resposta.

A bridge deve congelar as entradas e evidências durante hashing, submit e review,
sem escritores concorrentes. SQLite serializa os registros da fila, não arquivos
do sistema operacional. Hashes detectam divergências observadas; não constituem
transação atômica entre filesystem e SQLite nem proteção contra o dono do host.

O código controla o protocolo, mas não é sandbox contra um operador hostil com
acesso ao SQLite ou à máquina. Autenticação e permissões do serviço remoto não estão
implementadas. Agentes com ferramentas gerais exigem supervisão; diffs posteriores
não substituem bloqueio preventivo. Escrita de código por workers: BLOCKED.

## Ciclo operacional

1. Validar contrato, capacidade, arquivos, dependências, prazo e limite de claims.
2. Iniciar banco fora de qualquer árvore Git, em diretório irmão ao de evidências; importar job sem sobrescrever IDs existentes.
3. Registrar identidade real retornada pela ferramenta de agentes na bridge.
4. Claim atômico: um responsável, prazo e fencing token por tentativa.
5. Enviar somente a tarefa e snapshots aprovados ao especialista; renovar lease
   enquanto houver sinal de progresso, sem ampliar o deadline do run.
6. Receber relatório, verificar integridade e submeter evidência.
7. Convocar revisor diferente, com entrada e evidência da tentativa identificada.
8. Registrar PASS/FAIL; apenas revisão PASS conclui. Falha não vira DONE por texto.
9. Repetir para a próxima dependência liberada dentro do orçamento.
10. Ao terminar a fila, solicitar parada, exportar recibo sanitizado e registrar
    checkpoint. Nenhum processo ativo deve ser inferido de um checkpoint antigo.

## Aprendizado e retomada

Rejeição seguida de sucesso produz candidato PROPOSED. Não editar automaticamente
DECISIONS.md ou agentes globais. Revisão semanal é cadência, não agendamento já ativo.
Na retomada, verificar existência/integridade do banco e seu deadline. Não reaproveitar
leases expiradas. Se o host foi perdido, usar recibos para reconstruir apenas trabalhos
confirmados e abrir novo run; reconciliação é obrigatória para estados ambíguos.

## Critérios para ampliar o modo

Auditoria de projeto adicional: autorização, arquivos e perfil daquele projeto.
Execução de código: sandbox real, operações permitidas, teste de escape, diff de
snapshot, revisão independente e rollback. Operação fora da sessão: host persistente,
adapter Codex autenticado, orçamento monetário e testes de recuperação. Banco SQLite
do Supervisor não substitui banco de produto, Supabase ou storage de clientes.

## API mínima para a bridge confiável

Criar previamente diretórios absolutos distintos, por exemplo `/var/lib/cadu/db`
e `/var/lib/cadu/evidence`, em host autorizado. Neste piloto são temporários.
Não colocar evidências dentro da pasta do banco nem o banco na pasta de evidências.
A inicialização rejeita árvore Git ancestral e diretórios sobrepostos.

```python
from supervisor_runtime import Runtime

runtime = Runtime(db_path, project_path, evidence_path)
session = runtime.start_run(
    run_id, session_id=session_id,
    workers={actual_executor_id: ["auditor"], actual_reviewer_id: ["reviewer"]},
    deadline=deadline_unix, max_claims=2, lease_seconds=300,
    supervised=True, environment="CODEX_WEB",
)
session.enqueue(approved_jobs)
worker = session.worker(actual_executor_id)
claim = worker.claim()
# A bridge entrega os arquivos exatos a esse agente e aguarda a saída real.
# Salvar relatório em evidence_path; evidence_manifest = {arquivo: sha256}.
submission = worker.submit(
    claim["job"]["id"], claim["token"],
    snapshot=claim["snapshot"], evidence=evidence_manifest,
)
# A bridge obtém um parecer real da identidade distinta antes de chamar review.
session.worker(actual_reviewer_id).review(
    claim["job"]["id"], submission,
    snapshot=claim["snapshot"], result=actual_verdict, artifact=review_manifest,
)
session.stop()
receipt = session.status()  # exclui tokens de fencing
runtime.close()
```

Este exemplo documenta a API; não fabrica pareceres nem chama modelos sozinho.
A bridge deve tratar claim vazio, timeout, interrupção e erro antes de avançar.
`session.reap()` é uma chamada explícita de recuperação; não existe watchdog daemon.
O orçamento implementado limita claims e tempo. Tokens/custo reais: NOT_MEASURED.


## Backup e reversão do piloto

Parar o run antes de copiar estado; usar API `sqlite3.Connection.backup` para
snapshot consistente em diretório privado fora do Git, junto de cópia dos arquivos
de evidência e seus hashes. Reabrir a cópia, conferir jobs/events/stop e validar
hashes antes de retomar. Reabrir não renova prazo nem recria agentes encerrados.
O ensaio local está em OPERATIONAL_EVIDENCE.md; retenção externa não configurada.
Para reverter código, preservar recibo e revisar revert do incremento na branch;
reversão em main/produção exige alçada própria. O piloto não tem efeitos externos
para desfazer. Não restaurar banco antigo sobre tentativas atuais sem reconciliar.
