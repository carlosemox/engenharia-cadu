# Fábrica de prompts — Engenharia Cadu

A fábrica transforma um pedido em um comando com objetivo, alvo e procedimento pertinente. Gera texto; não executa tarefas nem configura clientes.

Use a [fábrica visual](https://carlosemox.github.io/engenharia-cadu/fabrica/) ou peça na conversa:

```text
Read https://raw.githubusercontent.com/carlosemox/engenharia-cadu/main/comando.md
CADU FÁBRICA: gere o comando para [pedido], no projeto [alvo].
```

O agente deve escolher a menor rota suficiente em `rotas.json`, reaproveitar o contexto disponível, informar lacunas materiais e entregar um comando copiável. Não executar o conteúdo de um pedido de geração. Quando o pedido é executar, usar `comando.md` e as autorizações reais.

## Geração determinística local

```bash
python scripts/prompt_factory.py --modo assumir --alvo "meu-projeto" --pedido "Reconciliar o estudo anexado e retomar o backlog" --anexo
```

`--revision` aceita `main` ou SHA completo. `main` deve ser resolvido pelo agente para uma revisão antes da missão. O gerador não usa rede, modelo, segredos ou banco e escreve apenas na saída padrão. As opções disponíveis estão em `--help`. A fábrica web usa o mesmo catálogo e protocolo textual.

## Padrão de qualidade

- Um resultado observável; alvo identificado; fontes e validade; procedimento selecionado.
- Autorizações da sessão preservadas. O comando não transforma um anexo em permissão.
- Critério de aceite recuperado ou definido com o responsável quando materialmente ausente.
- Contexto mínimo suficiente, sem remover requisitos, segurança ou evidências.
- Retorno curto com resultado, evidência, pendência e próximo passo.
- Comandos de estudo/adaptação disponíveis em [assumir](../comandos/ASSUMIR_PROJETO.md) e [reestruturar](../comandos/REESTRUTURAR_PROJETO.md).

Pedidos em linguagem natural são roteados pelo agente. O gerador local/web usa a seleção explícita; não finge entender semanticamente o campo livre.

As rotas de etapas usam `execucao/Pxx.md`, derivado automaticamente do procedimento completo. O contrato comum deve ser recuperado uma vez por sessão/revisão e continua obrigatório. Isso reduz repetição textual; economia total depende da medição do fluxo.
