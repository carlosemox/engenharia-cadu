**PASS — H-004-A, no escopo documental.**

| Critério de aceite | Evidência nas fontes fornecidas | Resultado |
|---|---|---|
| Software e civil distintos | `catalogo/esquadroes.json` declara squads separados, com IDs `software` e `civil`. | PASS |
| Supervisor não implementa | `agentes/coordenador.md`: “No papel Supervisor, nunca implementar código nem produzir campanhas.” | PASS |
| Catálogo não homologa executor | `kind: routing_policy_not_installed_agents`, papéis `DOCUMENTED_NOT_INSTALLED` e squads `MAPPED_NOT_HOMOLOGATED`. | PASS |
| Review independente exigido | Coordenador deve convocar revisor independente; conclusão depende de snapshot e review; aprovação da própria revisão independente é proibida. | PASS |

**Correção de atribuição:** a afirmação do relatório “O claim está confirmado pelo usuário” é inadequada. Conforme a informação fornecida nesta revisão, os dados de runtime foram verificados pela bridge via ferramenta, não pelo usuário.

Snapshot de referência informado: `11b5f3aa0168dccd56492f1258ccd4a33989b366b2406172110e79161ceb9c39`. Não realizei validação criptográfica nem verificação própria de runtime.

Documentos referenciados ausentes e `civil.roles: []` não impedem o aceite desses quatro contratos. O PASS não comprova instalação, homologação de executores ou aplicação dos controles em runtime.