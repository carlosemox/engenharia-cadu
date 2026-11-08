# Evidências

Baseline main cd17e123: scripts/validate.py PASS, 31 prompts, 59 páginas, 2409 links. Testes do lote serão registrados após execução. Nenhum teste documental certifica segurança da aplicação.

Roteador: python scripts/supervisor.py --check
Próxima tarefa, sem execução: python scripts/supervisor.py --next
Regressão: python -m unittest discover -s tests
Editorial: python scripts/validate.py
Cliente: node tests/test_factory_client.cjs

Browser visual, sandbox de executor, integração LLM, banco, carga, backup de produção e rollback de produção: NOT_RUN. Não promover runtime com base em testes sintéticos.

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
