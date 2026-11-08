# Evidências

Baseline main cd17e123: scripts/validate.py PASS, 31 prompts, 59 páginas, 2409 links. Resultados históricos abaixo; incremento operacional na seção final. Nenhum teste documental certifica segurança da aplicação.

Roteador: python scripts/supervisor.py --check
Próxima tarefa, sem execução: python scripts/supervisor.py --next
Regressão: python -m unittest discover -s tests
Editorial: python scripts/validate.py
Cliente: node tests/test_factory_client.cjs

Baseline P0/P1: browser visual, sandbox de executor, integração LLM, banco, carga, backup de produção e rollback de produção: NOT_RUN. Não promover runtime com base em testes sintéticos.

## Execução local P0/P1 — 2026-11-08

- Python unittest: 118 testes PASS, incluindo 22 testes do roteador.
- Validador editorial: PASS; 31 prompts, 59 páginas, 2417 links locais.
- Cliente JS: PASS em DOM simulado, incluindo o modo revisar-agentes.
- git diff --check: PASS.
- Dependência editorial existente markdown-it-py==4.2.0 instalada em venv isolado; CI declara a mesma dependência.
- Ajustes de regressão: comparar texto sem whitespace final conforme gerador; testar pipeline editorial completo; impedir ID auditoria duplicado no organizador.
- Revisão independente por agente distinto da implementação: quatro achados P2 de schema corrigidos; rechecagem independente PASS, incluindo 22 testes e probes negativos. Nenhum bloqueante no escopo revisado.

### Hashes dos arquivos revisados

- scripts/supervisor.py: `50ba44df4a53d644056552536e8d43f2ac25a24d40242f1d85f0527422179f73`
- tests/test_supervisor.py: `c7df0f9f64392e48ac9553978ea998c94fc3e4735ad1d5574436befd30ff8997`
- catalogo/esquadroes.json: `8e941d524a5ba65a15fe80ea8babcbcc06d5456b4a9c59fcc616406dd5684b44`
- docs/harness/SUPERVISOR.md: `e142c736a604826205e9f8295e21398196ff2e19a845679e509652a9383f6592`

## CI remoto observado

Commit validado: `86e49506dc4b091b34894ee9190bb3b292ac898a`.
CI_READ_ONLY: SUCCESS, run 42501820988.
Evidência: https://github.com/carlosemox/engenharia-cadu/actions/runs/42501820988
A árvore desse commit é idêntica à árvore local testada: `12083ec894963631a28ccb51721d7bc34b2f41a4`. Este checkpoint posterior não amplia a cobertura para runtime.


## Incremento operacional — 2026-11-08

- Suíte completa no venv editorial existente: **141 testes PASS**, dos quais 23
  do runtime. A execução sem venv do implementador encontrou dependência editorial
  ausente; a execução completa pelo coordenador usou a dependência existente e passou.
- Cobertura runtime: importação idempotente, rollback transacional, ciclos,
  dependências, concorrência/WIP1, identidade/replay, lease/fencing/heartbeat,
  stop/reap, retry, aprendizado PROPOSED, prazo/budget, caminhos e evidências.
- Regressão corrigida: alteração observada de fonte/evidência durante hashing de
  artefato de revisão é rechecada antes da transição. O host ainda deve serializar
  escritores; não se promete atomicidade filesystem/SQLite.
- Roteador --check: PASS. Alterado somente metadado para READ_ONLY_PLANNER;
  fixture de teste reseta recibos para não depender do status vivo de H-001.
- Editorial: PASS, 31 prompts, 59 páginas, 2428 links nesta execução.
- JS cliente: PASS em DOM simulado. git diff --check: PASS.
- Piloto real: duas auditorias documentais, agentes diferentes, dependência,
  heartbeat e stop; recibos em OPERATIONAL_EVIDENCE.md.
- Backup SQLite e reabertura em cópia no mesmo host: PASS; backup externo NOT_CONFIGURED.
- Sandbox, runtime 24h, benchmark de tokens, validação visual em navegador,
  carga, segurança de produção e deploy: NOT_RUN.

O campo runtime_agents=NOT_RUN do validador editorial descreve somente a cobertura
desse script; ele não executa nem certifica o piloto de agentes acima.

### Hashes atuais do código operacional

- `scripts/supervisor_runtime.py`: `b1c04aad93fa7776dff230efee790eec8039846f0c135e241d640b427573a676`
- `tests/test_supervisor_runtime.py`: `ffb9a7fcf38d45f23935935acce3242fd3e94b87b88032c5cc396a6c8a7fc79f`
- `scripts/supervisor.py`: `d599952ebeb45ff62142f162c9d0d8409a495c5a6e859c1e165ae330377bf8d3`
- `tests/test_supervisor.py`: `42ae7d125900ff1ba0098134e0d266555d6183dff3fcc98e41a690f6cc672586`


Revisão independente final: PASS no perfil `read_only_audit` em host confiável.
Revisor `01a1bc32-0470-7704-910d-fb7025d1f039` distinto do implementador
`01a1bc2d-ec5d-779b-a19e-09112a9da00e`; 45 testes de runtime/roteador conferidos.
Achado P2 corrigido, sem bloqueante restante nesse escopo. [Parecer](evidence/H-004/code-review.md).


## Biblioteca e manutenção — candidato de publicação

- Suíte completa: 176 testes PASS (inclui 19 auditor, 7 manutenção, 9 biblioteca).
- Manutenção local: M-001…M-004 PASS, zero chamadas LLM; recibo em evidências H-005.
- Biblioteca: 2566 registros, 10 originais e 20 traduções; HTML 25–28 KB por idioma,
  30 resultados por página, metadados externos somente em texto, links HTTPS GitHub.
- Revisão independente da biblioteca: PASS (Hilbert); 19 testes específicos de
  biblioteca/narrativa, sem achados bloqueantes. Browser pós-deploy pendente.
- Dois P1 identificados antes da publicação: Git clean filters no auditor e
  deadline com saída zero. Corrigidos com remoção de subprocessos Git e status
  FAIL em prazo esgotado; regressões adicionadas. Rechecagem independente PASS.
- Chromium local: download do navegador falhou como ZIP inválido. Navegador cloud
  abre página pública; não alcança localhost. Testes funcionais após deploy.
- Integração de IA agendada: CONFIGURED_INACTIVE, NOT_RUN; if:false em ambos jobs.
  Não há chamada paga, alteração de secret ou alegação de autonomia de código.


Pareceres do lote: [biblioteca](evidence/H-005/library-review.md),
[automação e auditor](evidence/H-005/automation-review.md).
Revisões fecham P1 por filtro Git e timeout; adapter LLM recebeu somente revisão
estática inativa. Nenhuma certificação de produção dos aplicativos foi emitida.
