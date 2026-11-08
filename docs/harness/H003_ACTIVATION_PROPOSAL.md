# H-003 — piloto de IA fora da conversa

Versão 1.1 — 08/11/2026. Estado: ALTERNATIVA API, NÃO ATIVADA.

Direção posterior do usuário: priorizar Codex e avaliar Ollama local.
Ver [piloto Codex + Ollama](CODEX_OLLAMA_PILOT.md). O teto abaixo permanece
uma proposta alternativa; não é requisito nem gasto aprovado da rota local.
Base inspecionada: 29742b198c01c5b444211d05b3188c102966979f.
Ambiente preservado: Web/Codex, conforme D-001.

## Resultado e escopo para aprovação

Executar uma auditoria real e uma revisão independente da central Engenharia Cadu
em jobs descartáveis do GitHub Actions. Uma execução manual, até dez minutos de execução por job, dois jobs;
tempo de fila não incluído. Sem recorrência inicial. Supervisor coordena; executor produz; revisor confere.
Não instalar nem homologar em lote os 2566 registros externos.

Proposta de teto: R$ 50,00 para o piloto completo, incluindo API e eventual custo
incremental do runner; não é estimativa de consumo nem autorização vigente.
Sem renovação automática, recarga ou contratação de servidor. Reservar o custo
máximo antes de cada chamada, incluindo revisão e tentativas; falha ambígua mantém
a reserva até reconciliação. Parar antes de exceder o saldo. Preço do modelo,
câmbio, tributos aplicáveis e runner precisam ser registrados antes do primeiro
consumo. Se não for possível limitar o pior caso, NÃO iniciar o piloto pago.

Modelo candidato: gpt-5.3-codex via API, para executor e revisor em jobs distintos.
Referência: https://developers.openai.com/api/docs/models/gpt-5.3-codex
Disponibilidade na conta, compatibilidade com o SHA fixado da action e preços:
PENDENTES de verificação. A escolha é proposta; não alterar o modelo desta sessão.
Não substituir silenciosamente por outro modelo se houver indisponibilidade.

## Constatações do código

- `.github/workflows/codex-audit.yml` permanece bloqueado por `if: false` nos dois jobs.
- As condições de aprovação são flags; não implementam teto monetário.
- Timeout de dez minutos por job não é limite de gasto.
- `:read-only` e `drop-sudo` estão declarados; não constituem evidência de ensaio
  de isolamento neste host. Docker e Codex CLI não foram encontrados na inspeção inicial; o CLI foi
  instalado posteriormente conforme CODEX_OLLAMA_PILOT.md.
- O contrato proíbe rede ao agente; o bloqueio efetivo deve ser demonstrado.
- Dois jobs distintos separam execução e revisão; não dispensam revisão de
  identidade, permissões, artefatos e acesso às credenciais.

## Autenticação proposta

Projeto OpenAI dedicado ao piloto; credencial restrita às capacidades necessárias,
armazenada como secret em ambiente GitHub dedicado, sem conteúdo em chat, Git,
artefatos ou logs. Não reutilizar credenciais de produção. Validar conta/projeto,
permissões e revogação. Identificar a versão do segredo por metadados, nunca pelo
seu valor. Inspecionar como a action fixada disponibiliza a credencial e impedir
que processos do agente leiam o segredo ou executem chamadas fora do orçamento.
Se a action não permitir esta separação, adaptar a arquitetura antes de ativar.
Aprovação do plano não é prova de criação/instalação da credencial.

## Ensaios obrigatórios antes do primeiro job LLM

Usar credenciais falsas e fixtures descartáveis para testar:

| Ensaio | Resultado exigido |
| --- | --- |
| Escrita no checkout read-only | Negada pelo host |
| Escrita fora do workspace, symlink e traversal | Negada pelo host |
| Leitura de segredo sentinela e estado do supervisor | Negada |
| Rede arbitrária e exfiltração | Negadas; API apenas pela fronteira confiável |
| sudo, subprocessos fora da política e alteração do isolamento | Negados; subprocessos permitidos herdam as restrições |
| Falta de credencial/modelo/aprovação | Sem chamada paga |
| Saldo insuficiente e concorrência | Reserva atômica; sem ultrapassar teto |
| Timeout/falha após envio de chamada | Reserva preservada; sem retry cego |
| Stop e cancelamento de job ativo | Novos jobs bloqueados e job cancelado |
| Autoaprovação e relatório com instruções maliciosas | Rejeitados |
| Reinício/duplicidade/lease expirado | Sem repetir efeito concluído |

Recibo de cada ensaio: SHA, versão do runner/action, comando, exit code, data,
expectativa, resultado e evidência sanitizada. Revisão independente do mesmo SHA.
Testes locais de fila não substituem esses ensaios. Não remover `if: false`
apenas porque uma variável ou documento declara PASS.

## Ordem de execução após aprovação

1. Confirmar projeto/conta de cobrança e instalar credencial por canal seguro.
2. Resolver controle monetário e fronteira de credenciais; implementar e testar.
3. Executar ensaios de isolamento sem credencial real no runner descartável.
4. Revisar o SHA e habilitar somente dispatch manual do piloto; manter cron pago desativado.
5. Rodar auditor e revisor, registrar consumo real e reconciliar reservas.
6. Parar o piloto, preservar evidências e registrar decisão de homologação do perfil.
7. Preparar lote distinto para programação: sandbox com escrita restrita, branch
   descartável, revisão do diff, testes e proposta de PR. Sem merge/deploy automático.

## Homologação individual

Cada candidato externo precisa de origem e versão exata, licença, permissões,
limites, teste funcional, teste adversarial e revisor distinto. Registrar PASS/FAIL
por agente e perfil; não extrapolar auditoria documental para execução de código.
Começar por um executor e um revisor; ampliar apenas mediante evidência.

## EN — approval summary

Proposed one-shot read-only audit and separate review on disposable GitHub runners.
Maximum total pilot spend: BRL 50.00, not yet authorized or technically enforced.
Candidate API model: gpt-5.3-codex; account access and pinned action compatibility
remain unverified. Authentication, monetary enforcement and real isolation tests
must pass before activation. No paid schedule, autonomous coding or bulk agent
certification is enabled by this proposal.

## ES — resumen para aprobación

Se propone una auditoría puntual de solo lectura y una revisión separada en
runners desechables de GitHub. Tope total: BRL 50,00, aún no autorizado ni aplicado
técnicamente. Modelo API candidato: gpt-5.3-codex; acceso de la cuenta y
compatibilidad pendientes. Autenticación, control monetario y pruebas reales de
aislamiento deben aprobarse antes de activar. Sin programación periódica pagada,
código autónomo ni homologación masiva de agentes.

## Validação desta preparação

Executada em 08/11/2026 neste checkout:
- 176 testes Python: PASS após instalar markdown-it-py==4.2.0 em venv isolado.
- scripts/validate.py: PASS, 31 prompts, 62 páginas, 2571 links locais.
- scripts/supervisor.py --check: PASS; execução NOT_STARTED.
- tests/test_factory_client.cjs: PASS em DOM simulado.
- git diff --check: PASS.

Essas verificações cobrem a regressão existente e a integridade editorial. Não
comprovam isolamento do runner, autenticação API, custo, CI remoto ou agente ativo.

Revisão independente documental: dois ajustes solicitados (tempo por job e
restrições de subprocessos), incorporados nesta versão. Validação final do revisor
registrada separadamente; não é homologação operacional.
