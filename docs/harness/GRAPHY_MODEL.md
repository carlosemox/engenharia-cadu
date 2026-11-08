# Grafo de trabalho

GRAPHY_RUNTIME=NOT_CONFIGURED. Modelo implementado pelo validador da fila, não integração com produto externo chamado Graphy.

Nó canônico: objeto tasks[] em TASK_QUEUE.md. Aresta depends_on aponta a ID existente; ciclos são inválidos. Gates são tarefas com aceite e evidência; arquivo, decisão e teste aparecem em inputs/outputs/evidence. Um task executor não pode reescrever o próprio aceite.

Estados: READY, IN_PROGRESS, IN_REVIEW, BLOCKED, APPROVAL_REQUIRED, RELEASE_CANDIDATE, RELEASE_BLOCKED, DONE, CANCELLED. Dependência satisfeita somente por DONE revisado com evidência; CANCELLED não libera consumidor. Owner, executor e revisor são identidades distintas de pastas/categorias.

| Etapa | Domínios | Gate |
|---|---|---|
| Fundação | software, security | stack, desenho de dados se aplicável e revisão de segurança |
| Produto | crm, dashboard | contratos aplicáveis da fundação e DS |
| Comunicação | whatsapp, operations | produto/consentimento/integração quando necessários |
| Vendas e escala | landing, instagram, paid_media | release gate para publicar ou gastar |

Mapeamento das oito origens do Drive em catalogo/esquadroes.json. Engenharia civil permanece civil; crm/dashboard são referências de aplicação. Marketing, comercial, WhatsApp, segurança, contabilidade, financeiro, jurídico e pessoas são esquadrões separados. Um domínio sem executor homologado recebe BLOCKED, nunca um agente inventado.
