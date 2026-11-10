# Supervisor — contrato e ADR de execução

Liderança: agentes/coordenador.md. Codex coordena; papéis disponíveis não equivalem a processos ativos. Ler PROJECT_STATE.md, TASK_QUEUE.md, DECISIONS.md, DS e somente os arquivos da tarefa. Selecionar um domínio e uma tarefa, convocar um executor e depois um revisor independente. Nunca escrever código/campanha como Supervisor. Na construção desta central, a sessão Codex implementa as ferramentas sob papel de implementação; não representa um Supervisor implantado.

## Implementado P0/P1

scripts/supervisor.py valida a fila, as dependências, identidades declaradas, limites e prefixos; emite a próxima tarefa elegível como JSON. É puro/read-only: não executa shell, não usa rede, não chama modelos, não marca DONE e não escreve estado. A fila versionada persiste entre sessões. Esse planejador não administra leases; o controle operacional separado abaixo possui essa função.

## Controle operacional supervisionado — D-011

`scripts/supervisor_runtime.py` oferece API Python de fila SQLite transacional,
leases/fencing, heartbeat, stop, dependências, hashes e revisão independente.
Capacidade única: `read_only_audit`. A sessão Codex é a bridge que convoca agentes
reais; o módulo não executa shell, modelos, código de projeto nem campanhas.
A API exige roster confiável, tempo e quantidade de claims delimitados. Não fornece
sandbox ou autenticação para operadores hostis. Recuperação de lease é explícita
via `reap()`, sem vigia em segundo plano. Uso: [runbook](OPERATING_RUNBOOK.md).

## ADR-001 — APPROVAL_REQUIRED para serviço fora da sessão

Necessidade: continuar trabalho fora do chat com custo delimitado. Alternativas: execução supervisionada por sessão (atual), worker único persistente com armazenamento transacional, serviço distribuído (adiado). Escolha proposta: validar primeiro worker único em staging, adapter Codex disponível e autorizado, armazenamento com aquisição atômica e trilha de eventos. Não escolher serviço, modelo ou assinatura sem perfil aprovado.

Contrato do worker: allowlist de operações, checkout descartável, paths realmente isolados, rede negada por padrão, nenhum segredo fora da tarefa, lease/fencing, budget/timeout, stop flag, idempotência, checkpoint, revisor autenticado independente e revisão do diff completo. Identidades textuais diferentes não provam independência: futura camada autenticada deve verificá-las. O validador não é barreira contra código hostil.

Aceite do runtime: queda/reinício sem duplicar efeito; dois workers disputando a mesma tarefa; lease expirado; cancelamento; falta de credencial; tentativa de escrever banco por FRAME; rename/symlink/traversal; autoaprovação; orçamento esgotado; regressão. Sem todos: READY_UNATTENDED=BLOCKED.

## Identidade Mike

Mike nomeia este papel de coordenação. [Política atual](../../politicas/MIKE.md). O runtime local independente e restrito está documentado no [aceite](LOCAL_EXECUTOR_ACCEPTANCE_2026-11-10.md); não confundir com a API SQLite de auditoria nem criar outra fila.
