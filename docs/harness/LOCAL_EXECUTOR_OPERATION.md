# Executor local — operação restrita

Versão 0.2.0 · 2026-11-10 · [English](LOCAL_EXECUTOR_OPERATION.en.md) · [Español](LOCAL_EXECUTOR_OPERATION.es.md)

## Estado e finalidade

Serviço `com.engenharia-cadu.local-executor` instalado no Mac, supervisionado pelo
método Engenharia-Cadu. Ollama local `qwen3:4b`, sem chave, download ou fallback
para API paga. O serviço executou a correção sintética de uma função de soma;
o candidato passou nas três asserções e exige revisão (`REVIEW_REQUIRED`).
Não equivale a um agente generalista nem libera os projetos de produto.

Base: `~/Library/Application Support/Engenharia-Cadu-Agent`.
Código: `scripts/local_executor.py`. Instalador: `scripts/install_local_executor.py`.
O instalador recusa sobrescrever uma instalação existente. A instalação usa
LaunchAgent do usuário: depende do Mac ligado e da sessão iniciada; não roda
com o Mac desligado e não prova disponibilidade por 24 horas.

## Política efetiva

- Um supervisor e uma tarefa por vez, lock exclusivo, heartbeat a cada cinco segundos em repouso.
- Uma tentativa por ID; até 240 s por tarefa, 90 s de cliente de inferência e 20 s por teste.
- Até oito arquivos existentes, 64 KiB por arquivo, 256 KiB no total.
- Projeto e raiz canônica precisam constar em `state/model.json` antes de qualquer leitura.
- Job em `state/jobs/` exige escopo, instrução, testes confiáveis, revisão e autorização com prazo máximo de 24 h.
- Somente `synthetic-acceptance` está admitido na instalação. A fila contém apenas o piloto já concluído.
- O modelo propõe conteúdo JSON; não recebe ferramentas, shell, credenciais ou MCPs.
- Fontes originais não recebem alterações. Candidatos ficam em `state/runs/<id>/work`.
- Testes têm candidato somente leitura, temporário próprio, sem rede ou novos processos.
- STOP, mudança de autorização/política e prazo interrompem o cliente; falha não é repetida automaticamente.
- Reinício marca recibos RUNNING como INTERRUPTED; nunca refaz efeitos incertos.
- Não há merge/deploy automático, autorevisão ou ativação de agentes externos.

## Operar

Os comandos abaixo são para o operador no Mac ou o conector autorizado. Não
precisam ser executados novamente para manter o serviço já iniciado.

```sh
# Estado do serviço
launchctl print "gui/$(id -u)/com.engenharia-cadu.local-executor"
# Estado da fila e trabalho atual
cat "$HOME/Library/Application Support/Engenharia-Cadu-Agent/state/heartbeat.json"
# Parada cooperativa (aguardar heartbeat STOPPED)
touch "$HOME/Library/Application Support/Engenharia-Cadu-Agent/state/STOP_REQUESTED"
# Retomada explícita depois de conferir recibos; remover STOP sozinho não inicia
rm -f "$HOME/Library/Application Support/Engenharia-Cadu-Agent/state/STOP_REQUESTED"
launchctl kickstart "gui/$(id -u)/com.engenharia-cadu.local-executor"
# Retirar serviço carregado; arquivos/evidências são preservados
launchctl bootout "gui/$(id -u)/com.engenharia-cadu.local-executor"
```

Para desabilitar também no próximo login, mover o plist
`~/Library/LaunchAgents/com.engenharia-cadu.local-executor.plist` para um arquivo
fora de `LaunchAgents`, após `bootout`. Não apagar recibos para repetir uma tarefa.

## Adoção por projetos e capacidades

O comando `CADU HOMOLOGAR AGENTE LOCAL` continua sendo a entrada de qualificação.
Recuperar backlog e regras do projeto, fixar revisão do método, definir uma tarefa
pequena, testes externos ao conteúdo editável e autorização persistente. Validar
compatibilidade dos testes com o sandbox antes de admitir a raiz. Builds que
exigem subprocessos ou rede não estão homologados neste executor.

Skills, agentes, MCPs e design systems são selecionados pelo supervisor conforme
o projeto, com origem, versão, permissões e validação. Catálogo não significa
instalação nem homologação. Esta versão não instala nem concede acesso automático
a essas integrações; o worker recebe somente a instrução e os arquivos permitidos.
Revisão de design, acessibilidade, testes de interface e revisão independente são
gates próprios. Nenhum requisito visual é dispensado por um teste unitário verde.

## Limites comprovados e residuais

Os probes bloquearam leitura/escrita externa, estado, symlink, Xcode, rede e spawn
destacado. Não representam prova de confinamento absoluto do macOS. A política
permite bibliotecas de sistema e leitura de metadados. Arquivos temporários têm
limite individual de 8 MiB; memória, threads e espaço agregado não têm quota forte.
STOP não comprova cancelamento instantâneo da geração dentro do servidor Ollama.
Digest é verificado antes/depois, sem imutabilidade atômica da tag. As autorizações
são arquivos privados do operador, sem autenticação de usuários externos.

Tokens são processados localmente; a inferência não usa API faturada. Energia,
hardware e a própria conversa de preparação não são contabilizados como gratuitos.

Evidências privadas: `evidence/acceptance-2026-11-10` sob a base instalada.
Resumo versionado: [recibo técnico](LOCAL_EXECUTOR_ACCEPTANCE_2026-11-10.md).
