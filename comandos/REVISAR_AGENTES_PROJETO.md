# Revisar agentes do projeto

## Comando completo
```text
COMANDO: REVISAR_AGENTES_PROJETO
MISSÃO: revisar o perfil de capacidades deste projeto antes de instalar ou executar agentes.
1. Confirmar projeto, raiz, branch, HEAD e ambiente. Reutilizar escolha registrada; cliente preferencial Codex. Não confundir web/CLOUD_CODE com Claude Code.
2. Ler seletivamente AGENTS, estado, fila, decisões, DS, stack e permissões reais. Não reler o catálogo inteiro.
3. Consultar catalogo/esquadroes.json e buscar metadados em catalogo/inventario-auditado.json. Identificar capacidade necessária, origem, commit/hash, licença, dependências, ferramentas e teste de aceite. Catálogo não significa instalação.
4. Distinguir software, engenharia civil, CRM, dashboard, marketing, Instagram, landing pages, tráfego, WhatsApp, operação, contabilidade, financeiro, pessoas e jurídico. Promover o coordenador existente a Supervisor; não criar coordenação concorrente.
5. Por necessidade, selecionar uma capacidade principal e somente apoios justificados. Resolver duplicatas por proveniência e conteúdo. Registrar USE_EXISTING, ADAPT, PILOT, EXCLUDE ou BLOCKED, com motivo e evidência.
6. Definir owner, executor_id, reviewer_id diferente, inputs, outputs, aceite, ambiente, dependências, allowed_paths, ações proibidas e orçamento. Pastas de origem não são identidades de agentes. Nenhum especialista visual altera banco.
7. Mapear fundação → produto → comunicação → escala conforme dependências reais. Não exigir banco/CRM em produto que não usa; publicação e gasto dependem de gate explícito.
8. Conferir fila/grafo, limite de três ciclos e parada após duas tentativas sem progresso. Verificar os dez freios em docs/harness/PRODUCTION_CONTROL.md. Sem sandbox, lease, orçamento e adapter homologados, READY_UNATTENDED=BLOCKED.
9. Consolidar no perfil/estado canônico existente. Lição de falha corrigida vira PROPOSED; revisor distinto aceita; promoção global exige PR e autorização. Não duplicar documentos de memória.
10. Entregar mapa por domínio, agentes selecionados/excluídos, dependências, riscos, testes e próximo nó. Não instalar, mudar fornecedor, secrets, banco, DNS, main, produção ou deploy por inferência.
SAÍDA: PROJECT, ENVIRONMENT, CLIENT, HEAD, SQUADS, SELECTED_CAPABILITIES, EXCLUDED_CAPABILITIES, EVIDENCE, BLOCKERS, APPROVAL_REQUIRED, NEXT_ACTION, RELEASE_STATUS.
```
