[English](i18n/README.en.md) · **Português (Brasil)** · [Español](i18n/README.es.md)

# Engenharia Cadu

**Da ideia à entrega. Sem perder o caminho.**

Transforme sua visão de negócio em um produto que você entende, consegue revisar e pode evoluir. Uma engenharia de trabalho com agentes de IA: decisões antes da implementação, contexto que sobrevive à sessão e evidências antes de chamar algo de pronto.

Você traz o problema, o briefing e as referências. O método organiza a próxima decisão. O agente executa dentro do escopo autorizado. O projeto guarda os requisitos, o código e as provas do que foi feito.

[COMEÇAR UM PRODUTO →](p/P01.md) · [ORGANIZAR UM PROJETO EXISTENTE](https://github.com/carlosemox/engenharia-cadu-adocao) · [PREPARAR O AMBIENTE](p/P07.md) · [ABRIR O SITE](https://carlosemox.github.io/engenharia-cadu/)

Codex principal · colaboração seletiva · design desde o briefing · economia de contexto · segurança por etapas.

> A apresentação está disponível em três idiomas. O português brasileiro é a base editorial da Engenharia Cadu. Os procedimentos e guias mantêm seus idiomas atuais; o prompt universal de segurança S01 está em inglês. Escolher um idioma nesta página não traduz nem altera automaticamente os comandos.

<!-- section:historia -->
## 00 / Uma ideia não deveria se perder entre conversas

O projeto começa com uma visão clara. Depois chegam referências, telas, bibliotecas, integrações e novas decisões. O código cresce. Mas, quando a sessão termina ou outra ferramenta assume, surge a pergunta: **o que está decidido, o que realmente funciona e por onde continuar?**

A Engenharia Cadu foi estruturada para enfrentar esse problema: dar um lugar às decisões e um caminho ao desenvolvimento. Não pede que você abandone o que já fez. Pede que a intenção seja compreendida, que as mudanças tenham limites e que cada entrega possa ser conferida.

A proposta não é produzir mais arquivos por obrigação. É transformar conversas em conhecimento utilizável, ideias em requisitos e tarefas em resultados verificáveis. Uma mesma filosofia para começar do zero, recuperar projetos e desenvolver capacidades reutilizáveis.

**Seu negócio determina o produto. A engenharia organiza o trabalho. A ferramenta não decide sozinha o que a empresa deve ser.**

<!-- section:comecar -->
## 01 / Comece do ponto em que você está

**Novo: [fábrica de prompts](fabrica/README.md) e [comando único CADU](comando.md).** Para retomar um aplicativo com estudos anexados, use [Assumir projeto](comandos/ASSUMIR_PROJETO.md). Para corrigir e reorganizar, use [Reestruturar projeto](comandos/REESTRUTURAR_PROJETO.md). Os comandos reconciliam o estado antes de executar o autorizado.

| Seu momento | Entrada | O primeiro resultado |
|---|---|---|
| Tenho uma ideia ou um briefing | [P01 — Descoberta do produto](p/P01.md) | Entendimento compartilhado, lacunas relevantes e direção para a primeira versão. |
| Já existe uma aplicação | [Trilha de adoção](https://github.com/carlosemox/engenharia-cadu-adocao/blob/main/read.md) | Retrato do projeto e plano revisável antes de alterar código, estrutura ou banco. |
| Preciso preparar a máquina | [P07 — Ambiente e capacidades](p/P07.md) | Inventário do que existe e configuração do que estiver autorizado. |
| Preciso de uma tarefa específica | [P00 — Escolher a trilha](p/P00.md) | O procedimento pertinente, sem executar a engenharia inteira. |

### Projeto novo: um briefing é ponto de partida, não trabalho perdido

Cole na conversa do agente e descreva o produto na segunda linha. Se você já tem um briefing, disponibilize o texto ou arquivo nessa mesma conversa.

```text
Read https://raw.githubusercontent.com/carlosemox/engenharia-cadu/main/p/P01.md
Projeto: [nome, problema, público, jornada principal e restrições]. Use meu briefing existente, valide somente as lacunas e conduza as próximas etapas autorizadas em CONTINUO_SUPERVISIONADO.
```

Começar pelo P01 não significa repetir todas as perguntas. O agente aproveita decisões e pesquisas válidas, esclarece o que falta e encaminha o trabalho. Ele não pula a descoberta apenas porque encontrou um arquivo chamado briefing.

### Projeto existente: primeiro enxergar, depois mudar

```text
Read https://raw.githubusercontent.com/carlosemox/engenharia-cadu-adocao/main/read.md
Entenda este projeto, reconcilie briefing, PRD, TRD e fluxos e apresente o Retrato do Projeto e o Plano de Adoção antes de alterar código, arquivos ou banco.
```

Você deve enxergar o que o produto pretende fazer, o que foi implementado, o que foi comprovado e o que continua desconhecido. A arquitetura útil, a identidade, os contratos e o trabalho local são preservados. Reescrita ou migração não entram disfarçadas de organização.

### Ambiente: configurar não é presumir

```text
Read https://raw.githubusercontent.com/carlosemox/engenharia-cadu/main/p/P07.md
Inventarie este ambiente e prepare somente as configurações autorizadas para meu projeto. Diferencie instalado, configurado, acessível e verificado.
```

Os textos são instruções para um agente, não comandos do shell. Leitura, edição e execução dependem das ferramentas e permissões disponíveis. Nenhum desses atalhos publica automaticamente sua aplicação.

<!-- section:metodo -->
## 02 / Dê forma ao produto antes de dar volume ao código

A engenharia parte da pergunta que interessa ao negócio: **quem precisa realizar o quê, em qual situação e com qual resultado?** A resposta orienta escopo, interface, dados e operação.

| Entrega | Para que serve |
|---|---|
| Briefing e escopo | Fixar problema, público, valor, primeira versão, restrições e exclusões. |
| PRD — requisitos do produto | Definir comportamentos, regras, permissões, exceções e critérios de aceite. |
| Fluxos e design system | Desenhar jornadas coerentes, componentes, feedback e acessibilidade. |
| TRD — desenho técnico | Delimitar arquitetura, dados, contratos, integrações e recuperação. |
| Plano por incrementos | Escolher unidades úteis, dependências, responsáveis e verificações. |

**Design não é decoração adicionada no final.** A direção começa no briefing (D0), ganha regras e componentes na especificação (D1) e é conferida na interface implementada (D2). Uma tela bonita que não resolve a jornada ainda não concluiu a tarefa.

Referências de mercado ajudam a fazer escolhas, não aprovam funcionalidades automaticamente. Estudar um produto, integrar sua API e reutilizar código licenciado são decisões distintas. Registre fontes e limitações; construa uma proposta própria, adequada à sua operação.

<!-- section:integracoes -->
## 03 / Escolha as dependências antes de depender delas

Aula ao vivo, pagamentos, autenticação, mensagens e armazenamento não podem surgir como surpresas no meio da implementação. Primeiro definimos a capacidade necessária. Depois comparamos **construir, reutilizar, contratar, integrar ou adiar**.

O [P08](p/P08.md) separa ferramentas que ajudam a desenvolver de serviços que fazem parte do produto. Para cada serviço: requisitos, contrato, dados compartilhados, acesso, custo verificado ou pendente, limites, contingência e condição de substituição.

Uma plataforma de ensino, por exemplo, pode organizar matrículas e agenda enquanto um serviço externo realiza a aula. A integração pode ser a solução inicial — ou continuar sendo a melhor escolha. Infraestrutura própria não é um destino obrigatório.

Supabase pode compor a arquitetura quando escolhido. Isso não autoriza trocar autenticação, recriar bancos ou migrar dados existentes. Framework, banco e ORM seguem as necessidades e decisões do projeto, não uma stack imposta pela biblioteca.

<!-- section:agentes -->
## 04 / Um coordenador. Colaboração com responsabilidade.

**Codex é o executor principal do método.** Antigravity, Gemini CLI e OpenCode são colaboradores possíveis, selecionados pela tarefa e pelas capacidades realmente disponíveis. Não há obrigação de abrir quatro agentes para resolver uma mudança simples.

Cada delegação leva objetivo, contexto suficiente, arquivos e recursos permitidos, dependências, critérios de aceite e formato de retorno. Recursos compartilhados têm um responsável. Revisores trabalham em leitura; o coordenador confere a integração.

Produto, arquitetura, design, frontend, backend, qualidade, GUARDIAN, SENTINEL e release são responsabilidades documentadas, não uma equipe automaticamente instalada. Uma skill presente em um catálogo ainda precisa de procedência, licença, compatibilidade e teste no cliente escolhido.

[Conhecer os papéis](agentes/README.md) · [Selecionar capacidades](catalogo/README.md) · [Entender os clientes](integracoes/CLIENTES.md)

<!-- section:continuidade -->
## 05 / A próxima etapa não precisa de outra colagem

Em **CONTINUO_SUPERVISIONADO**, o coordenador conclui a fase, verifica entrega, segurança e backup pertinente, registra o estado e carrega o próximo procedimento autorizado. A entrevista continua interativa. Decisões materiais continuam com você.

```text
Entender → especificar → preparar → implementar → testar → revisar → homologar
                       ↑                         ↓
                       └──── corrigir e verificar ┘
```

P13, P14 e P15 formam ciclos por incremento. P17 é a preparação/execução de uma missão prolongada quando houver supervisor e condições comprovadas; não é a etapa obrigatória depois de toda entrega. Especializações entram por necessidade, não por número na lista.

Falha bloqueante, decisão pendente, risco grave, proteção necessária ausente ou limite atingido interrompem a ação dependente. Trabalho independente já autorizado pode continuar. O agente não inventa tarefas para manter a sessão ocupada.

**Um prompt não mantém o computador trabalhando depois que a sessão termina.** Autonomia prolongada precisa de processo real, fila, limites, exclusividade, checkpoint, parada e recuperação testados. [Ler as regras de continuidade](politicas/CONTINUIDADE.md).

<!-- section:documentos -->
## 06 / Faça o conhecimento sobreviver à sessão

Harness engineering, no nosso método, significa organizar o ambiente de trabalho do agente: instruções encontráveis, fontes claras, ferramentas acessíveis e feedback que possa ser verificado. O conhecimento importante fica no projeto, não apenas na memória de uma conversa.

| Informação | Onde manter |
|---|---|
| Como iniciar e executar | README do aplicativo. |
| O que o produto deve fazer | Briefing e PRD canônicos. |
| Como as partes se conectam | TRD, contratos e decisões arquiteturais. |
| Como o usuário percorre o produto | Fluxos e design system. |
| Como o agente deve trabalhar | AGENTS.md curto, apontando para detalhes. |
| O que mudou e como continuar | Evidências, decisões e handoff pertinente. |

Não é uma árvore obrigatória. Em um projeto existente, preserve documentos equivalentes e registre o mapeamento. Uma mudança de comportamento, schema ou comando deve atualizar sua fonte responsável. Não transforme AGENTS.md em uma enciclopédia.

O método público guarda receitas. Cada aplicativo guarda seu produto. A operação privada guarda perfis e registros internos — nunca senhas ou tokens em arquivos Git. [Explorar os templates](templates/README.md).

<!-- section:auditoria -->
## 07 / Segurança antes, durante e antes de publicar

Uma auditoria no fim não substitui boas decisões no começo. A engenharia prevê requisitos e ameaças desde o desenho, verificações durante os lotes e revisão do candidato antes de cada publicação.

| Marco | O que precisa ser examinado |
|---|---|
| Início | Dados, identidade, permissões, exposição, limites de confiança e controles necessários. |
| Durante | Alterações, chamadores, segredos, dependências, regressões e usos permitidos e negados. |
| Integração | Isolamento entre módulos/clientes, regras compartilhadas e efeitos externos. |
| Pré-publicação | Achados, cobertura, revisão, configuração e recuperação da mesma versão candidata. |

O **[S01](modulos/seguranca/README.md)** preserva o comando universal de auditoria. Seus modos são distintos: AUDIT examina; PLAN organiza correções; FIX altera somente o lote autorizado; VERIFY reavalia. A campanha avançada exige solicitação expressa. Testes ativos e produção têm autorização própria.

Os exemplos de hooks cobrem início, conclusão de módulo, saída de fase, integração, commit, push, pull request, pré-release e manutenção periódica. **Estão publicados como exemplos, não instalados nos aplicativos.** O verificador de recibos confere registros; não é scanner nem prova a honestidade de um resultado preenchido.

Nenhuma ferramenta garante ausência de invasões. Ausência de teste, erro, timeout ou evidência antiga não é aprovação. Controles essenciais precisam de implementação real, revisão e manutenção. [Hooks e limites](modulos/seguranca/hooks/README.md) · [Política de segurança](politicas/SEGURANCA_ENGENHARIA.md).

<!-- section:backup -->
## 08 / Preserve o trabalho. Comprove que consegue recuperá-lo.

O destino definido para cada projeto é `Projetos 2026/Backup/<nome-do-projeto>`. A proteção exige mais que uma pasta criada: cobertura explícita, gerações identificadas, integridade conferida e recuperação testada no escopo necessário.

Arquivos de trabalho e alterações locais, histórico Git, banco, uploads e segredos são classes diferentes. Um ZIP de código não comprova todas elas. Credenciais precisam de proteção específica; não entram em arquivo comum. Nenhuma limpeza automática das gerações anteriores está autorizada pelo método.

Backup deve anteceder mudanças arriscadas e acompanhar entregas com novos artefatos. Se a proteção indispensável não foi comprovada, a ação dependente não avança. **A integração automática com o Drive precisa ser configurada e testada em cada ambiente; a publicação desta página não a ativa.** [Política e cobertura](politicas/BACKUP_DRIVE.md).

<!-- section:economia -->
## 09 / Economize contexto, não critério

A política de economia no Astra é uma disciplina de trabalho: carregar somente o que a tarefa exige, reutilizar decisões válidas, usar scripts para verificações repetitivas e delegar quando houver benefício concreto.

O detalhe continua disponível na fonte. O implementador recebe requisitos e contratos relevantes, não todos os documentos. O revisor recebe o candidato e seu contexto, não o histórico inteiro. Esperar CI não exige chamadas sucessivas ao modelo.

Não prometemos um percentual de economia. Tokens, custo e retrabalho devem ser medidos quando observáveis. Não há troca silenciosa de modelo, provedor, autenticação ou cobrança. O objetivo é **menor custo por entrega aceita**, incluindo os testes e as correções necessários. [Política de economia](politicas/ECONOMIA_ASTRA.md).

[Biblioteca interativa em português](https://carlosemox.github.io/engenharia-cadu/biblioteca.html)

<!-- section:prompts -->
## 10 / Um comando para cada responsabilidade

Use a biblioteca completa como mapa, não como texto para colar de uma vez. Os IDs permanecem estáveis; cada procedimento informa finalidade, entradas, limites, entrega e critérios de conclusão.

| Prompt | Responsabilidade |
|---|---|
| [P00](p/P00.md) | Escolher a trilha e a próxima ação. |
| [P01](p/P01.md) | Entender o produto e validar o briefing inicial. |
| [P02](p/P02.md) | Pesquisar hipóteses, referências e viabilidade. |
| [P03](p/P03.md) | Consolidar primeira versão, escopo e exclusões. |
| [P04](p/P04.md) | Escrever requisitos, regras e critérios de aceite. |
| [P05](p/P05.md) | Especificar fluxos, experiência e design system. |
| [P06](p/P06.md) | Definir arquitetura, dados, contratos e segurança. |
| [P07](p/P07.md) | Inventariar e preparar máquina, contas e clientes. |
| [P08](p/P08.md) | Selecionar agentes, ferramentas, serviços e APIs. |
| [P09](p/P09.md) | Preparar a base e o repositório do produto novo. |
| [P10](p/P10.md) | Configurar ambientes, CI e integrações aprovadas. |
| [P11](p/P11.md) | Comprovar prontidão para o trabalho seguinte. |
| [P12](p/P12.md) | Transformar requisitos em tarefas delimitadas. |
| [P13](p/P13.md) | Implementar e verificar uma tarefa. |
| [P14](p/P14.md) | Revisar independentemente conforme risco e evidência. |
| [P15](p/P15.md) | Homologar jornadas e integrações em staging. |
| [P16](p/P16.md) | Preparar ou executar release autorizado. |
| [P17](p/P17.md) | Conduzir missão prolongada com supervisor comprovado. |
| [P18](p/P18.md) | Retomar sem perder nem duplicar trabalho. |
| [P19](p/P19.md) | Priorizar projetos em andamento ou parados. |
| [P20](p/P20.md) | Diagnosticar um projeto sem reescrevê-lo. |
| [P21](p/P21.md) | Corrigir e adotar o método incrementalmente. |
| [P22](p/P22.md) | Auditar agentes, skills e pacotes antes de ativá-los. |
| [P23](p/P23.md) | Estruturar módulos reutilizáveis com consumidores reais. |
| [P24](p/P24.md) | Avaliar melhorias no harness sem enfraquecer controles. |
| [P25](p/P25.md) | Desenvolver capacidades financeiras auditáveis. |
| [P26](p/P26.md) | Organizar conteúdo e publicação por marca. |
| [P27](p/P27.md) | Criar capacidades de vídeo programático. |
| [P28](p/P28.md) | Estruturar capacidades de engenharia e obras. |

<!-- section:capacidades -->
## 11 / Adote o necessário. Preserve o que funciona.

O catálogo é uma seleção de possibilidades, não uma instalação em massa. A escolha de cada skill, biblioteca ou integração deve considerar necessidade, procedência, licença, compatibilidade, custo e validação. Consultar documentação atual não autoriza enviar código ou informações privadas a terceiros.

| Local | Responsabilidade |
|---|---|
| Máquina e cliente | Runtime, ferramentas, autenticação e integrações globais autorizadas. |
| Aplicativo | Código, dependências, lockfiles, documentos, testes e configuração específica. |
| Central pública | Método, procedimentos, modelos e referências publicáveis. |
| Operação privada | Perfis, alçadas, destinos e evidências internas, sem segredos no Git. |

Projetos existentes preservam stack, banco, contratos e equivalentes funcionais. Mudanças incompatíveis exigem decisão própria. Monorepos precisam de inventário das fronteiras e recursos compartilhados. Novos serviços só entram quando existe função concreta no produto.

<!-- section:operacao -->
## 12 / Saiba o que está publicado — e o que precisa ser comprovado

**Documento disponível não significa instalação concluída. Teste local não significa integração em produção.** Esta central oferece receitas, templates e exemplos; cada ambiente precisa comprovar seu funcionamento.

| Capacidade | Situação e condição |
|---|---|
| P00–P28 e S01 | Biblioteca publicada; a eficácia no seu projeto precisa de execução e avaliação. |
| Continuidade entre etapas | Instrução do coordenador; depende de sessão, contexto e autorizações. |
| Hooks e controles de segurança | Exemplos e políticas; instalação e bloqueios reais precisam ser testados. |
| Backup automático | Política definida; conexão, cobertura e restauração precisam ser implantadas. |
| Missão de 24 horas | Depende de supervisor, limites, recursos e recuperação comprovados. |
| Página trilíngue | Apresentação traduzida; guias e comandos vinculados mantêm seus idiomas atuais. |

Sem acesso ao ambiente, o agente pode explicar e especificar, mas não comprovar configuração. Relatórios de execução devem separar PASS, FAIL, NOT_RUN e não aplicável, com justificativa. Segurança não é promessa de invulnerabilidade.

[Estado operacional](OPERACAO.md) · [Mapa da central](MAPA_DA_CENTRAL.md) · [Cenários de avaliação](avaliacoes/CENARIOS.md) · [Validação S01](modulos/seguranca/validacao/RESULTADOS.md)

<!-- section:evolucao -->
## 13 / Construa uma base que possa evoluir

Quando uma melhoria surge em um projeto, extraia a parte reutilizável, remova dados internos, confira a licença e revise antes de incorporá-la ao método público. Atualizações permanecem em suas fontes oficiais; assuntos novos recebem um lugar próprio. Não há espelhamento automático da operação privada.

A Engenharia Cadu se inspira na organização do **[Vibe Coding Toolkit, de Matheus Gomes](https://github.com/soumatheusgomes/vibe-coding-toolkit)** e adapta essa referência às decisões desta central. Não há afiliação ou endosso presumido. O aviso de licença do toolkit está preservado; os demais componentes mantêm seus próprios termos. A central não herda automaticamente uma licença MIT para todo o seu conteúdo. [Licenciamento e atribuições](LICENCIAMENTO.md).

O melhor ponto de partida é o próximo resultado útil: compreender o produto, recuperar um fluxo ou preparar uma base verificável. Escolha a entrada, disponibilize seu contexto e mantenha as decisões importantes visíveis.

**Defina com intenção. Construa com contexto. Evolua com evidência.**

[COMEÇAR PELO P01 →](p/P01.md) · [RECUPERAR UM PROJETO](https://github.com/carlosemox/engenharia-cadu-adocao) · [REPORTAR UM PROBLEMA](https://github.com/carlosemox/engenharia-cadu/issues)
