# Retomar sem repetir o diagnóstico

O coordenador resolve capacidades por tarefa. Uma pasta de documentos, uma aba vazia, a ausência de Docker ou a falta de um processo em execução não encerram a missão.

Na retomada, recupere o [índice de contexto](../../templates/INDICE_CONTEXTO.md) do produto. Na primeira execução preencha os campos a partir das fontes observadas.

## Localizar o aplicativo

1. Recupere do pedido, perfil privado ou checkpoint a identidade owner/repo, PR ou branch e SHA do aplicativo. Mantenha o SHA do método separado. Se o nome estiver claro mas faltar o endereço, consulte o inventário GitHub autorizado. Confira identidade na especificação e no PR. Só peça uma decisão se houver destinos plausíveis conflitantes ou acesso realmente negado.
2. Se houver checkout, valide raiz, origin, branch, HEAD e alterações locais. Preserve o trabalho local. Compare o HEAD com o candidato do PR. Se divergirem, mantenha evidências separadas; nunca substitua um checkpoint local pelo remoto para obter um teste verde.
3. Sem checkout e com missão de implementação, obtenha a fonte autorizada em diretório isolado pelo mecanismo Git disponível. Confirme o SHA antes de executar código. Se o Git local não tiver acesso, use a conexão GitHub já autorizada para ler árvore, especificação, implementação e testes pelo mesmo SHA. Quando viável, materialize os arquivos de um ensaio mínimo, verifique os hashes dos blobs e execute só o escopo coberto. Registre PROVA_PARCIAL quando o ensaio usar um subconjunto. Auditoria somente leitura dispensa instalação ou alteração remota.
4. Abra um bloqueio somente para a operação impedida. Registre recurso, SHA, operação tentada, erro sanitizado e o artefato entregue pela alternativa. Não peça de novo URL, branch, especificação ou checkpoint que possam ser recuperados pelas fontes acima. Guarde a associação confirmada no perfil privado do produto.

## Conferir o ensaio antes de corrigir o produto

Antes do primeiro teste, confira imports, leituras de arquivos, scripts chamados, fixtures, configuração, lockfile e runtime exigidos pela suíte. Em uma cópia parcial, registre quais arquivos foram obtidos e seus hashes no SHA escolhido.

Quando ocorrer ENOENT, módulo ausente ou comando indisponível, confronte primeiro o arquivo ou recurso com a árvore canônica. Se existir naquela revisão, recupere a dependência do ensaio e repita o mesmo teste. Se estiver ausente também na fonte completa, investigue um defeito do projeto. Dependência externa ausente exige preparar o executor autorizado ou registrar a pendência. Preserve as asserções. Nunca reescreva o produto para satisfazer uma cópia incompleta.

Uma falha na preparação mantém o aceite da funcionalidade pendente. Prova parcial deve identificar suíte, runtime, adaptação do executor, serviços simulados e cobertura. Registre CI por job e SHA, além da prova local. Um teste focal aprovado só satisfaz os critérios que efetivamente exercitou.

## Quando faltar um serviço de teste

Inspecione o comando da suíte, testes de integração semelhantes, configuração de CI e serviços descartáveis já autorizados. O nome de uma variável, um binário de diagnóstico ausente ou um teste com mock não prova o estado de um banco. Verifique o destino sem exibir credenciais. Se houver executor autorizado com o serviço, execute a prova no candidato exato. Não acione workflow com deploy ou custo fora da alçada.

Se faltar o serviço mas houver fonte e autorização de implementação, escreva o teste de integração para a regra real e exercite as verificações locais cabíveis. Registre em separado o comportamento testado com mock, o teste integrado implementado e a execução integrada pendente. Skip não conta como PASS. Não troque o requisito por uma tarefa documental. A prova do agente instalado exige o perfil nativo no caminho efetivamente suportado; um playbook solto só comprova documentação.

STOP_REQUESTED prevalece para o supervisor correspondente. Um ensaio manual isolado depende de autorização própria e nunca limpa esse sinal. Comprove o fim com o diff ou artefato, ambiente, SHA, testes realmente executados e o próximo nó elegível.


## Selecionar a próxima tarefa

Use o grafo existente do projeto. Uma tarefa READY precisa de requisito aprovado, dependências satisfeitas, recursos disponíveis, orçamento e autorização compatíveis. Priorize a tarefa que destrava uma entrega do usuário. Registre tentativas, assinatura da falha, hipótese nova e condição de retomada no próprio nó.

Um nó BLOCKED só volta a READY quando sua condição de retomada mudar. Dentro da mesma sessão, avance para a próxima tarefa independente elegível. Ao esgotar a fila elegível, salve o checkpoint com a operação externa ou decisão que falta. Evite consultas e tentativas repetidas sem mudança observável.

Para operação sem supervisão, prove no executor real a leitura do perfil do agente, exclusão de escritores concorrentes, checkpoint durável, retomada após interrupção, respeito ao sinal de parada e aos limites. Use um ensaio com falha controlada de preparação, recuperação pela fonte fixada e uma tarefa independente. Registre intervenção humana, ciclos e resultado. Uma execução assistida fornece evidência própria e deixa a homologação sem supervisão pendente.

## Evoluir funcionalidades e aprendizado

Entregue um comportamento aprovado por lote, pela entrada normal, com caso permitido e recusado quando aplicável. Vincule requisito, mudança e prova no checkpoint. Novas funcionalidades sugeridas ficam na fila de propostas para decisão de escopo. Guarde a lição comprovada com versão, pré-condições e regressão, usando os registros existentes. Uma hipótese nova fica como candidata até validação. Consulte apenas lições pertinentes ao componente e à falha atuais.


## Preparação na origem

Ao encontrar bloqueio recorrente, aplique [preparação e resolução na origem](PREPARACAO.md). Vincule cada bloqueio a uma tarefa de resolução, dono, alçada e aceite. Reutilize provas ainda válidas e aplique cada gate somente às tarefas que ele governa.
