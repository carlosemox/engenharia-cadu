# Ambientes e agentes de desenvolvimento — V1

## Gate obrigatório

Recupere a seleção do perfil/checkpoint e confira o executor efetivo. Em primeiro uso, aceite o ambiente aberto pelo responsável quando inequívoco. Pergunte só diante de destino ambíguo ou conflito. Os ambientes previstos são:

1. **Terminal** — execução direta por CLI, scripts, Git e testes.
2. **Aplicativo do computador/Mac** — IDE ou aplicativo local, com revisão visual e controle interativo.
3. **Cloud Code** — VS Code, IntelliJ/JetBrains ou Cloud Shell, especialmente para Cloud Run, Kubernetes, GKE, APIs e recursos Google Cloud.

A escolha do ambiente deve ser registrada no estado/checkpoint do projeto antes de escrever código.

## Papéis

| Capacidade | Uso principal | Limite |
|---|---|---|
| Codex | Coordenar a missão, interpretar requisitos, integrar mudanças, revisar evidências e decidir o próximo nó | Não pressupor que outro agente executou algo sem evidência |
| Cloud Code | Desenvolvimento, execução e depuração de aplicações cloud-native; configurações de Cloud Run/Kubernetes/GKE e integração com serviços Google Cloud | Não autoriza deploy, mudança de projeto, billing ou produção |
| Gemini Code Assist/Gemini CLI | Pair programming, explicação, geração assistida, revisão localizada e tarefas diretamente relacionadas ao ecossistema Google | Não deve editar a mesma branch simultaneamente com outro agente |
| Antigravity | Tarefas agentic multi-etapas, navegador, UI, artefatos, execução assíncrona e agentes paralelos | Usar projeto/branch/worktree isolado; revisar diff e artefatos antes de integrar |

Cloud Code é ambiente e integração de desenvolvimento; não deve ser tratado como um agente separado quando estiver usando Gemini Code Assist dentro dele.

## Regra de coordenação

Usar todos juntos somente com papéis distintos:

- um coordenador mantém o objetivo, o grafo e a branch de integração;
- um único executor é o dono da escrita em cada arquivo/feature;
- revisores trabalham em leitura ou em worktree/branch separado;
- cada entrega retorna diff, testes, riscos e evidências;
- a integração ocorre somente depois de revisão e verificação.

Nunca permitir dois agentes escrevendo simultaneamente no mesmo arquivo ou na mesma branch. Não iniciar paralelismo se a tarefa for pequena ou se o ganho não puder ser medido.

## Roteamento prático

- **Produto, domínio, contratos e integração geral:** Codex coordena; terminal ou aplicativo local executa.
- **Cloud Run, Kubernetes, GKE, Skaffold e APIs Google Cloud:** Cloud Code é o ambiente preferencial; Gemini pode auxiliar dentro do IDE.
- **Pesquisa de código, segunda opinião ou revisão de uma função:** Gemini em modo de revisão, sem autoridade para integrar.
- **UI, navegador, screenshots, fluxos completos e tarefas longas:** Antigravity em branch/worktree isolado, com artefatos verificáveis.
- **Release, produção, migrações e segredos:** somente após gate explícito, revisão independente e evidência operacional.

## Sequência recomendada

`IDENTIFICAR → ESCOLHER AMBIENTE → DEFINIR DONO → EXECUTAR → TESTAR → REVISAR → INTEGRAR`

Fontes oficiais consultadas:

- [Cloud Code](https://cloud.google.com/code)
- [Cloud Code para VS Code](https://docs.cloud.google.com/code/docs/vscode)
- [Gemini Code Assist agent mode](https://docs.cloud.google.com/gemini/docs/codeassist/use-agentic-chat-pair-programmer)
- [Google Antigravity](https://www.antigravity.google/docs)

## Versões de idioma

- [English](AMBIENTES_E_AGENTES.en.md)
- [Español](AMBIENTES_E_AGENTES.es.md)
