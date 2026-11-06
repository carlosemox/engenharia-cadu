# Preparar e operar desenvolvimento por até 24 horas

Entrada universal para projeto novo ou existente. Comando de conversa, aplicado ao executor real. A janela solicitada é um teto de operação. Aceites, quota, parada, recursos e fila elegível determinam quanto trabalho pode avançar.

## Comando completo
```text
ENGENHARIA CADU · PREPARAR E OPERAR

OBJETIVO
Entregue os incrementos já aprovados deste projeto, preparando antes os recursos necessários à sua execução e validação. Use o contexto e o método na revisão fixada. Siga o contrato comum uma vez por revisão e a preparação em modulos/recuperacao/PREPARACAO.md.

1. RECUPERAR E RECONCILIAR
Confirme produto, origem, checkout, revisão e alterações locais. Recupere especificação, decisões, backlog e checkpoint. Em produto novo, conclua as decisões materiais de P01–P06 e derive o primeiro incremento. Em produto existente, preserve requisitos aprovados e resolva somente as lacunas que mudam a execução. Reutilize registros, sem criar uma segunda fila.

2. PREPARAR A ENTREGA ANTES DE PROGRAMAR
Associe cada requisito do próximo incremento a ator, entrada, resultado permitido, resultado recusado e prova. Identifique dependências locais, banco, autenticação, callbacks, serviços externos e revisão. Para cada recurso registre ambiente, versão, destino, capacidade necessária, autorização, preparação, teste de disponibilidade e limpeza.
Execute P10 e P11 no nível exigido pela tarefa. Reutilize scripts e configurações existentes. Instalação e restauração de dependências, serviços descartáveis e configuração de desenvolvimento devem ser executadas quando cobertas pelo pedido e pelas permissões disponíveis.
Ao faltar recurso, abra e execute a tarefa de resolução dentro da alçada existente. Ao faltar decisão material, prepare a recomendação com consequências e consolide as decisões relacionadas em uma solicitação. Nunca peça novamente informação recuperável das fontes autorizadas.

3. PREPARAR O EXECUTOR CONTÍNUO
Identifique cliente, versão, modelo realmente selecionado, acesso, runtime e supervisor. Reutilize o controlador saudável e seu contrato. Verifique no cliente se existe mecanismo nativo de continuidade apropriado. Ative-o somente pela interface suportada e pela autorização da missão.
Se faltar supervisor, e sua construção estiver incluída no pedido, execute um incremento P12/P13 delimitado para integrar e testar um controlador disponível e compatível. Evite criar uma implementação paralela por projeto. Se houver incompatibilidade, corrija e teste o contrato antes de iniciar.
Um PID ativo exige verificar lease, estado do checkpoint e worker. Teste os estados reais do runtime, inclusive espera por mudança, parada, reinício e retomada. Preserve STOP_REQUESTED até haver autorização explícita para retomar aquele controlador.

4. FIXAR A MISSÃO E SEUS LIMITES
Use templates/CONTRATO_MISSAO.md no registro existente. Confirme uma janela de até 24 horas a partir do início observado, um escritor por recurso, limite de tentativas, orçamento/quota e mecanismo que aplica esses limites. Utilize os limites existentes mais restritivos.
Sem contador financeiro disponível, registre consumo financeiro não observado e exija controles observáveis compatíveis, como deadline, quota do provedor e quantidade limitada de execuções. Não converta assinatura em orçamento ilimitado nem estime economia como medição.
Mapeie os gates apenas às tarefas que governam. Liste os incrementos aprovados suficientes para a janela, sem inventar funcionalidades para preencher tempo. Se a fila terminar, encerre a missão ou aguarde mudança pelo mecanismo determinístico existente, sem consultar o modelo continuamente.

5. HOMOLOGAR A CONTINUIDADE
Execute um lote curto representativo no executor real antes da missão longa. Observe entrega, teste, checkpoint, escritor único, interrupção controlada, retomada sem repetir efeito e limite aplicado. Falha controlada deve permitir corrigir um pré-requisito e retomar o teste. Pausa e falha de acesso devem produzir o estado esperado.
Só registre READY_UNATTENDED para o escopo comprovado. Se houver falha, use CADU RECUPERAR e faça a correção autorizada, seguida da regressão pertinente. Falha em uma integração suspende seus dependentes e permite continuar tarefas independentes.

6. EXECUTAR
Com prontidão comprovada e ordem de início autorizada, inicie ou continue a missão no mecanismo real. Registre host, revisão, Run ID ou identificador nativo equivalente, estado e checkpoint. Um texto de instruções não comprova processo em execução.
Siga o grafo de execução para selecionar a próxima tarefa elegível. Em cada tarefa use objetivo, ação, observação, verificação e decisão. Integre pelo procedimento autorizado e preserve a prova da revisão realmente testada. Leve propostas de novas funcionalidades ao backlog de decisões.

7. ECONOMIA ASTRA 6
Preserve modelo e autenticação autorizados e confira a disponibilidade do modelo no executor. Não invente identificador de API a partir de um nome comercial.
Carregue o índice curto, contrato da tarefa, trechos de código relevantes e lições aplicáveis. Scripts determinísticos fazem inventário, checks, contagem e espera. Contexto inalterado e testes ainda válidos são reutilizados.
Reserve análise mais profunda para ambiguidade, arquitetura e falhas difíceis. Delegue somente quando autorizado e útil. Conte custo do ciclo completo, retrabalho e intervenções humanas. A meta é custo por entrega aceita menor, mantendo os aceites.

8. ENTREGAR E APRENDER
Registre funcionalidades aceitas, correções, recursos preparados, provas, pendências exatas, consumo observado e estado real da missão. Cada correção recorrente deve produzir prevenção verificável em teste, script, configuração ou contrato pertinente.
Uma lição inclui causa comprovada, condição de uso, revisão, teste e invalidação. Mantenha candidatas separadas de lições validadas. Reutilize evidência suficiente e atualize somente o que mudou.
```

## Fundamentação e limites

A documentação de tarefas longas do Codex descreve especificação estável, marcos verificáveis e memória durável. A avaliação comportamental descrita pelo Google orienta testar ações observáveis do agente, além do resultado agregado de testes. As regras acima aplicam esses princípios ao preparo e à retomada. O nome Harness2 não identifica, por si só, produto, versão ou executor instalado.

- https://developers.openai.com/blog/run-long-horizon-tasks-with-codex
- https://developers.googleblog.com/the-anatomy-of-harness-engineering-how-to-evaluate-iterate-and-guard-ai-coding-agents/
- https://developers.openai.com/cookbook/examples/codex/using_goals_in_codex

Goals é uma possibilidade a verificar no cliente. Sua disponibilidade e ativação precisam de evidência própria. Um objetivo persistido no cliente não demonstra todos os controles do supervisor ou a operação do host durante 24 horas.
