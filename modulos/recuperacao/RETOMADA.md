# Retomar sem repetir o diagnóstico

O coordenador resolve capacidades por tarefa. Uma pasta de documentos, uma aba vazia, a ausência de Docker ou a falta de um processo em execução não encerram a missão.

Na retomada, recupere o [índice de contexto](../../templates/INDICE_CONTEXTO.md) do produto. Na primeira execução preencha os campos a partir das fontes observadas.

## Localizar o aplicativo

1. Recupere do pedido, perfil privado ou checkpoint a identidade owner/repo, PR ou branch e SHA do aplicativo. Mantenha o SHA do método separado. Se o nome estiver claro mas faltar o endereço, consulte o inventário GitHub autorizado. Confira identidade na especificação e no PR. Só peça uma decisão se houver destinos plausíveis conflitantes ou acesso realmente negado.
2. Se houver checkout, valide raiz, origin, branch, HEAD e alterações locais. Preserve o trabalho local. Compare o HEAD com o candidato do PR. Se divergirem, mantenha evidências separadas; nunca substitua um checkpoint local pelo remoto para obter um teste verde.
3. Sem checkout e com missão de implementação, obtenha a fonte autorizada em diretório isolado pelo mecanismo Git disponível. Confirme o SHA antes de executar código. Se o Git local não tiver acesso, use a conexão GitHub já autorizada para ler árvore, especificação, implementação e testes pelo mesmo SHA. Quando viável, materialize os arquivos de um ensaio mínimo, verifique os hashes dos blobs e execute só o escopo coberto. Registre PROVA_PARCIAL quando o ensaio usar um subconjunto. Auditoria somente leitura dispensa instalação ou alteração remota.
4. Abra um bloqueio somente para a operação impedida. Registre recurso, SHA, operação tentada, erro sanitizado e o artefato entregue pela alternativa. Não peça de novo URL, branch, especificação ou checkpoint que possam ser recuperados pelas fontes acima. Guarde a associação confirmada no perfil privado do produto.

## Quando faltar um serviço de teste

Inspecione o comando da suíte, testes de integração semelhantes, configuração de CI e serviços descartáveis já autorizados. O nome de uma variável, um binário de diagnóstico ausente ou um teste com mock não prova o estado de um banco. Verifique o destino sem exibir credenciais. Se houver executor autorizado com o serviço, execute a prova no candidato exato. Não acione workflow com deploy ou custo fora da alçada.

Se faltar o serviço mas houver fonte e autorização de implementação, escreva o teste de integração para a regra real e exercite as verificações locais cabíveis. Registre em separado o comportamento testado com mock, o teste integrado implementado e a execução integrada pendente. Skip não conta como PASS. Não troque o requisito por uma tarefa documental. A prova do agente instalado exige o perfil nativo no caminho efetivamente suportado; um playbook solto só comprova documentação.

STOP_REQUESTED prevalece para o supervisor correspondente. Um ensaio manual isolado depende de autorização própria e nunca limpa esse sinal. Comprove o fim com o diff ou artefato, ambiente, SHA, testes realmente executados e o próximo nó elegível.
