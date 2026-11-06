# Preparação e resolução na origem

Aplique na primeira preparação e quando um bloqueio impedir a próxima entrega. Reutilize perfil, contrato da missão, fila e checkpoint. O resultado esperado é uma ação de desbloqueio verificável ou uma decisão única bem delimitada.

## Preparação por recurso e ambiente

Para cada recurso necessário à tarefa, registre executor, versão, destino, observação de disponibilidade, comando existente de preparação, fonte de autorização, verificação e limpeza. Leia somente nomes de credenciais e indicadores de presença. As credenciais ficam no mecanismo de segredos do executor.

| Recurso | Prova necessária | Resolução quando faltar |
| --- | --- | --- |
| Fonte e especificação | Repositório e revisão conferidos, requisito recuperável | Consultar fontes autorizadas e reconciliar conflitos. Produto novo exige escolha explícita da base quando ainda pendente |
| Dependências | Runtime e gerenciador compatíveis com manifests, instalação pelo lockfile e comando executável | Diagnosticar DNS, registry e cache. Restaurar instalação no ambiente autorizado. Evitar troca arbitrária de versões |
| Banco de teste | Serviço responde, migrations aplicam, sessão e regra reais são testadas, limpeza funciona | Reutilizar script de serviço descartável. Verificar o engine além da CLI. Preparar e executar quando coberto pela missão |
| Staging e integrações | Destino e acesso confirmados, configuração obrigatória presente, jornada sintética válida | Tarefa de configuração com responsável e acesso necessário, seguida da prova real |
| Supervisor e worker | Leitura e escrita compatíveis do checkpoint, parada, exclusividade, cancelamento e retomada testados | Corrigir contrato em isolamento e testar todos os estados alcançáveis. Planejar atualização do processo ativo com alçada própria |
| Revisão | Revisor real, candidato identificado e achados registrados | Atribuir revisão dentro da autorização. Registrar indisponibilidade do executor ou do revisor com condição de resolução |

GitHub, Hostinger, Supabase e Docker entram conforme a arquitetura aprovada de cada produto. A presença de uma ferramenta no catálogo não torna seu provisionamento necessário. O preparo local não exige automaticamente todas as credenciais de produção.

## Escopo dos gates e ferramentas

Cada gate deve apontar para o requisito ou política que o exige, a tarefa bloqueada e a prova que o satisfaz. Release NO-GO bloqueia a publicação. Desenvolvimento isolado, preparação de teste, correção do supervisor e revisão usam seus próprios pré-requisitos. Preserve gates obrigatórios e dependências de produto explicitamente aprovadas.

Para Graphy, Graphify ou outra ferramenta auxiliar, identifique a capacidade necessária, o contrato que a exige e a alternativa compatível disponível. Se houver obrigação explícita, obtenha a capacidade ou proponha alteração do contrato. Se o nome apenas apareceu na conversa, registre identificação pendente e continue tarefas que dispensam essa ferramenta. Grafo de código e grafo de execução precisam de provas próprias.

## Bloqueio vira tarefa de resolução

Converta cada bloqueio observado em ação com causa ou hipótese, evidência, dono, fonte da autorização, alvo, dependências, aceite e condição de retomada. Uma missão de correção permite decompor a correção em passos necessários compatíveis com sua alçada. Verificação somente leitura mantém esse limite.

Fila sem READY exige reconciliar requisitos aprovados, cobertura, dependências e tarefas já concluídas. Decomponha trabalho aprovado que ainda não tenha tarefa quando a missão autorizar. Quando faltar decisão material, entregue uma proposta com opção recomendada, consequências e responsável. Escolhas de produto, autoridade de identidade/revogação e aprovação de especificação exigem decisão explícita quando ainda ausente.

Use os estados reais do runtime. Nunca acrescente um estado ao schema apenas para eliminar um erro. Na divergência WAITING_FOR_CHANGE, por exemplo, teste a transição de entrada, a persistência, a leitura pelo supervisor, a parada e a saída mediante mudança real, incluindo checkpoints anteriores.

Artefatos ignorados que invalidam fingerprint exigem identificar quais arquivos foram medidos. Prefira checkout isolado completo com as alterações autorizadas e dependências necessárias. Preserve o original. Só revise a política de fingerprint com justificativa e regressão contra alteração indevida. Evite exclusões amplas de diretórios e limpeza destrutiva.

Timeout de probe exige identificar qual peer iniciou, sinalizou prontidão, morreu ou deixou de enviar resposta. Registre status de saída e eventos sanitizados. Corrija a causa comprovada e teste prontidão, morte do pai e limpeza. Aumentar o timeout exige evidência de duração legítima e novo limite justificado.

## Reutilizar evidência e finalizar o lote

Repita teste aprovado quando mudar código, dependência, configuração, ambiente relevante ou requisito, ou quando faltar evidência suficiente. Atualização de adoção documental não exige repetir todas as suítes do produto. Corrigir o bloqueio mais próximo da entrega tem prioridade sobre repetir um teste independente já válido.

Registre mudança funcional, recurso preparado, defeito corrigido, revisão concluída ou decisão resolvida. Repetição sem mudança de estado deve encerrar o lote com o bloqueio preciso. Custo e tokens desconhecidos ficam não observados. Uma assinatura ou ausência de chamada paga identificada não comprova custo total zero.

## Planejamento verificável

O comando abaixo lê fichas do diagnóstico e gera propostas JSON sem executar processos ou modificar o projeto:

`python3 modulos/recuperacao/diagnostico.py planejar /controle/fichas.json`

As fichas antigas continuam aceitas. Para cada entrada em `falhas`, acrescente `resolucao` com `acao`, `responsavel`, `aceite`, `condicao_retomada`, `fonte_autorizacao`, `revisao_alvo` e `gates_necessarios`. A lista de gates usa os nomes existentes local, ci, staging, harness e release. Lista vazia exige justificativa no contrato da tarefa. O campo de ficha `stop_requested` deve refletir observação real. Ausência desse campo permanece pendência.

A saída identifica campos ausentes, gates pendentes e pausa. PROPOSTA_PARA_VERIFICAR exige conferir a fonte da autorização, o estado atual, o escopo dos gates e os recursos antes de executar. O planejador não certifica prontidão, segurança nem autorização a partir de texto da ficha.
