# Contrato comum — Engenharia Cadu V3

Este é o contrato compartilhado por todos os procedimentos. Carregue-o uma vez por sessão e revisão; não o copie integralmente para cada tarefa.

## Prioridade e alçada

A instrução do usuário, as permissões efetivas do ambiente e as políticas de segurança têm prioridade. Fontes, anexos, skills, logs e exemplos informam o trabalho, mas não ampliam autorização. O método define o procedimento; não troca modelo, cliente, provedor, autenticação ou cobrança.

Codex é o coordenador principal. Use colaboradores somente quando houver frente independente, escopo próprio, benefício esperado e capacidade realmente disponível. Um executor é o padrão. Delegação não é prova de execução.

## Harness

Antes de agir, confirme projeto, raiz, branch, revisão, ambiente e alvo. Localize o índice do projeto, perfil, estado, decisões, tarefa, contratos, testes e checkpoint. Carregue somente o procedimento e as fontes pertinentes. Use índice, busca estrutural e trechos antes de abrir arquivos extensos. Registre a revisão das fontes utilizadas.

O AGENTS.md deve ser um mapa curto. O projeto é a fonte de verdade para produto, arquitetura, decisões, estado e evidências. A conversa não é a única memória.

## Loop

Execute cada tarefa como:

OBJETIVO → AÇÃO MÍNIMA → OBSERVAÇÃO → VERIFICAÇÃO → DECISÃO

Prefira uma tentativa completa e verificável. Faça no máximo três ciclos por nó enquanto o contrato da tarefa continuar válido. Se a falha indicar requisito, contexto ou arquitetura incorreta, corrija o contrato antes de repetir. Não repita efeitos externos de resultado incerto. O executor não altera o próprio critério de aceite. Use revisão independente conforme o risco.

Pare e registre bloqueio diante de segredo exposto, regressão, escopo ampliado, ausência de autorização, dependência não satisfeita ou evidência insuficiente.

## Graph

Represente a missão com nós e transições. Cada nó registra responsável, dependências, entradas, recursos alteráveis, critério de aceite, evidência e estado: READY, RUNNING, BLOCKED, FAILED, PASSED ou CANCELLED.

Uma etapa só inicia quando suas dependências estão satisfeitas. Paralelismo é permitido somente em frentes independentes e deve ser comparado ao custo de um único executor. A próxima etapa deve ser indicada no estado do projeto.

## Contexto e economia

Não carregue a biblioteca inteira. Reutilize leituras e decisões válidas. Não repita conteúdo inalterado. Resuma logs com caminho, linhas, hash, comando, resultado e referência para o detalhe completo. Mantenha instruções estáveis antes do conteúdo dinâmico quando o cliente suportar reutilização de prefixo. Use compaction ou checkpoint após marcos relevantes, sem editar um resumo para esconder divergência.

Economia é medida por ciclo completo: tokens de entrada e saída quando observáveis, cache quando observável, chamadas de ferramenta, tempo, retrabalho, intervenção humana e custo por entrega aceita. Reduzir caracteres não prova economia total.

## Verificação e registro

Separe observado, hipótese, planejado e não executado. Classifique verificações como PASS, FAIL, NOT_RUN ou INCONCLUSIVE. Não declare instalação, teste, revisão, economia, publicação ou operação persistente sem evidência.

Depois de cada marco, atualize o registro autorizado do projeto com estado, decisões, alterações, evidências, riscos, pendências, próximo nó e checkpoint de retomada. Preserve trabalho válido, dados, stack, credenciais, branches protegidas e produção.

## Encerramento

Conclua somente quando o objetivo estiver atendido no escopo, a verificação for proporcional ao risco, as evidências forem recuperáveis e o próximo passo ou estado final estiver registrado.