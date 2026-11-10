# Mike — revisar, relatar e assumir projetos

Versão 1.0.0 — 2026-11-10. Comando em linguagem natural para a sessão do projeto.

```text
Read https://raw.githubusercontent.com/carlosemox/engenharia-cadu/main/comando.md
MIKE: REVISAR E ASSUMIR.

Resolva a Engenharia-Cadu para um SHA e leia politicas/MIKE.md e o contrato comum
nessa revisão. Preserve a escolha de ambiente já informada e o trabalho existente.

PRIMEIRO: faça uma revisão somente leitura do projeto aberto. Identifique raiz,
remoto, branch, SHA, alterações locais, tarefas/processos e backlog; reconcilie
produto, arquitetura, código, dados, segurança, integrações, Design System,
testes/CI, deploy e documentação. Busque evidências; marque o que não foi verificado.
Não altere código nem ative jobs antes de apresentar o relatório.

RELATÓRIO DE ASSUNÇÃO: explique o que existe e funciona, o que está incompleto,
o que Mike assumirá e o que não assumirá, riscos/bloqueios, fontes e revisões,
plano ordenado por dependências, executores/revisores, critérios de aceite,
recuperação, limites de tempo/custo e primeira tarefa elegível.

Se a missão abranger vários projetos, inventarie somente os autorizados e
acessíveis, com um relatório por projeto e visão geral sem misturar dados.
Não considere todos os repositórios da conta automaticamente autorizados.
Projeto inacessível fica NÃO REVISADO; não interrompe a revisão dos demais.

MODELOS: Astra 6 em todo start e nas partes que exigem mais capacidade; depois de
resolver e verificar a parte complexa, 5.3 Luna para a continuidade econômica.
Registre modelo solicitado e efetivo, motivo de troca e checkpoint. Se o cliente
não permitir/confirmar a troca ou não oferecer o nome solicitado, declare isso;
não simule troca nem use API paga automaticamente. Ollama local permanece sujeito
à própria homologação; este pedido não troca seu modelo nem amplia seu escopo.

DEPOIS DO RELATÓRIO: prossiga nos lotes já autorizados, com Harness/Loop/Graph,
WIP=1 por padrão, contexto seletivo, testes proporcionais, revisão independente,
checkpoint e relatório após cada lote/bloqueio. Use skills/agentes/MCPs pertinentes
somente se disponíveis e qualificados; preservar Design System e segurança.
Não reinicie do zero nem invente tarefas. Pare por STOP, prazo, escopo concluído
ou bloqueio material; avance nos nós independentes autorizados.

Não crie segunda fila, não modifique JARVIS e não cadastre projetos reais no
executor sintético sem homologação específica. Não declare trabalho fora da
sessão sem serviço verificado. Distinguir IDLE, RUNNING, REVIEW_REQUIRED e aceito.
```

[Política Mike](../politicas/MIKE.md) · [Assumir projeto](ASSUMIR_PROJETO.md).
Enquanto a alteração estiver em PR, usar a revisão da branch publicada em vez
de presumir que `main` já contém este comando.
