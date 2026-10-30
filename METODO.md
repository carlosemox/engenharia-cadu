# Método operacional — edição documental 2.0

## Decisões e alternativas

Objetivo: criar e recuperar produtos com qualidade, design coerente, contexto econômico e continuidade verificável. Cadu escolheu Codex como principal, colaboração dos demais clientes, estudo/documentação antes do GitHub e economia Astra transversal.

Alternativas consideradas: um único prompt gigante; quatro agentes ativos o tempo todo; ou biblioteca modular com coordenação única e colaboração por tarefa. Adotamos a terceira, porque preserva contexto, autoria, custo e clareza. Não pressupõe que multiagente seja sempre mais eficiente.

Antiobjetivos: outra plataforma infinita antes de entregar um produto; instalar tudo; resetar projeto existente; garantir “zero erro”; tratar um processo vivo como software concluído; inventar economia ou aprovação.

## 1. Fluxo do produto

Ideia/contexto → entrevista → pesquisa das hipóteses relevantes → briefing/escopo com D0 → PRD → fluxos/design D1 ↔ arquitetura/dados/integrações → plano em incrementos → bootstrap/preflight → implementação/testes/revisão → D2 e staging → release autorizado → operação.

É um mapa de dependências. Pesquisa técnica crítica e inventário podem ocorrer antes/em paralelo. Pequena alteração não exige refazer o PRD. Não congelar arquitetura dependente de API antes da prova de viabilidade necessária.

## 2. Serviços do produto versus ferramentas da engenharia

Codex, skills e testes ajudam a construir. Aula ao vivo, pagamento, identidade, comunicação e renderização são capacidades do produto, sujeitas a contratos próprios. O perfil seleciona as primeiras; o Mapa de Integrações registra as segundas.

No briefing, levantar necessidade/contas existentes. Na pesquisa, comparar construir, reutilizar, contratar, integrar ou adiar. No PRD, comportamento e limitações; no TRD, fornecedor aprovado, conexão, acesso, dados, erros, limites e saída. No bootstrap, configurar dentro da alçada. No preflight, comprovar.

Uma solução inicial pode permanecer se atender ao negócio. Não prometer substituição própria apenas por chamá-la de temporária. Uma fronteira simples de módulo evita espalhar dependência; microserviços/plugins não são obrigatórios.

## 3. Design desde o briefing

D0: contexto de uso, identidade, referências justificadas, dispositivos, interação, acessibilidade, estratégia visual e jornada de validação.

D1: tokens semânticos, componentes necessários, variantes, estados, conteúdo, responsividade e contratos. Biblioteca técnica é escolhida pela compatibilidade, não imposta universalmente.

D2: componentes em código e experiência renderizada verificados. Revisão visual, automação, acessibilidade e teste com usuários são evidências diferentes; não declarar que um teste humano ocorreu quando só foi proposto.

## 4. Autoridade e execução

Cadu decide produto, orçamento e alçadas. Codex coordena tecnicamente e integra. Supervisor determinístico aplica limites e estado fora do controle dos workers. Antigravity, Gemini e OpenCode executam contratos delimitados quando úteis; Claude não é obrigatório.

Papéis são responsabilidades, não processos permanentes. GUARDIAN significa controle de escopo/isolamento; QA significa verificações; SENTINEL significa revisão independente comprovada; release gate significa autorização externa. Esses nomes não afirmam software instalado.

Um escritor por recurso. Revisão independente recebe requisito, diff, contexto e evidências, não só a opinião do autor. Se outro cliente estiver indisponível, não inventar revisão. Registrar bloqueio quando ela é obrigatória, ou autorrevisão com limite quando a política da tarefa permite.

## 5. Documentação e memória

Uma fonte principal por decisão. Requisitos → fluxos → contratos → tarefas → testes → evidências. Histórico curto com origem de decisões, sem autobiografia do projeto. AGENTS.md e entradas dos clientes apontam para as mesmas fontes, sem copiar o estudo integral.

Estado operacional é durável; resumo de conversa não substitui fila/checkpoint. Atualizar somente documentos afetados. Nunca sobrescrever decisões aprovadas por uma sugestão gerada em outra sessão.

## 6. Preparação e prontidão

Preparação de máquina, bootstrap de projeto e integração de serviços são escopos distintos. Auditar primeiro. Alterações globais e serviços pagos exigem alçada. Preservar tecnologias existentes; não iniciar scaffold sobre código.

READY_LOCAL, READY_CI, READY_STAGING e READY_UNATTENDED são níveis demonstrados por checks próprios. READY_RELEASE não concede GO. Configuração não é funcionamento e mocks não demonstram serviço real.

## 7. Continuidade

Missão finita com tarefas elegíveis, recursos, limites, orçamento, TTL/expiração de autorizações e critérios de parada. Supervisor confirma propriedade das tarefas, registra eventos e resultados e reconcilia efeitos externos. Requisições repetidas precisam de idempotência/reconciliação. Polling de CI deve usar ferramenta, não chamadas vazias de IA.

Se Codex parar, preservar estado; não promover outro cliente sem política. Sem tarefas, sem limite ou sem alçada, parar/aguardar. Janela de 24 horas é teto, não obrigação de gerar trabalho. Antes de habilitar, executar casos de recuperação em ambiente descartável.

## 8. Recuperação e reuso

Recuperação: observar → preservar → reproduzir → demonstrar causa → corrigir mínimo → testar → revisar → adaptar o padrão. Restauração vem antes de modernização.

Reuso: preferir módulo, pacote, template ou serviço conforme contrato e consumidor. Verificar licença, dados, versão e atualização. Cada marca e cliente preserva contexto e credenciais.

## 9. Economia e melhoria

ASTRA_ECONOMICO governa todos os procedimentos. O critério é custo por entrega aceita, sem reduzir escopo ou controle. Avaliar mudanças no próprio harness com baseline, aceites fixos e uma hipótese, incluindo casos não usados no ajuste. O agente não altera o teste para se aprovar.

O uso de princípios inspirados em Harness² não equivale à instalação/execução do framework oficial nem à reprodução de seus resultados.

## 10. Estado desta edição

Documentos e prompts preparados; revisão humana de aceite pendente. Nenhum repositório remoto, instalação de cliente, benchmark, piloto de API ou supervisor foi executado. O próximo trabalho documental é revisar as entradas; a implantação terá contratos próprios.


## Publicação da central
Esta edição possui um site estático e catálogo público. Isso não implanta clientes nem supervisor. Consulte README para a entrada atual.
