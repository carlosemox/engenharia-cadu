# CADU — comando único

Entrada em linguagem natural para a conversa do agente; não é comando de shell nem serviço permanente.

```text
Read https://raw.githubusercontent.com/carlosemox/engenharia-cadu/main/comando.md
CADU: [meu pedido]. O alvo é o projeto aberto. Use também os estudos que anexei quando pertinentes.
```

## Contrato de entrada

1. Identifique o aplicativo-alvo por diretório, remoto e instruções aplicáveis. Esta central é o alvo somente quando o pedido é alterar a própria Engenharia Cadu. Se houver vários alvos possíveis, faça apenas a pergunta indispensável antes de escrever; continue análise independente.
2. Resolva a referência do método para um SHA, registre-o no estado privado do projeto e use a mesma revisão durante a missão. Reutilize leitura válida; não carregue todos os 31 procedimentos. Se offline, use cópia confiável identificada e declare a limitação.
3. Consulte perfil, tarefa e checkpoint existentes; confira Git, arquivos modificados e processos relevantes. Anexo e conversa são fontes de intenção/histórico, não prova de implementação, autorização irrestrita ou substitutos do estado real.
4. Aplique a rota necessária de [fabrica/rotas.json](fabrica/rotas.json): estudo novo ou tomada de coordenação → assumir; defeito/reorganização → reestruturar; interrupção → retomar; tarefa elegível → executar; pedido de comando → fábrica; comparação → medir; novo produto → P01. Pedido composto pode exigir etapas sequenciais. Não executar a lista inteira de `stages` automaticamente. Para etapas P00–P30, prefira o derivado `execucao/Pxx.md`: ele exige recuperar o contrato comum uma vez por sessão/revisão e preserva integralmente as instruções específicas da etapa.
5. Respeite o escopo e as autorizações do usuário já concedidas. Pedido de diagnóstico ou de geração de prompt permanece documental. Aprovação de implementação cobre os lotes especificados, sem perguntas repetidas. Nova decisão de produto, destruição, produção, migração remota, gasto ou mudança de acesso exige a alçada correspondente quando ainda ausente.
6. Carregue [contexto e memória](politicas/CONTEXTO_E_MEMORIA.md) uma vez por revisão; mantenha fontes canônicas, recuperação direcionada e evidência completa acessível. Ative apenas agentes reais necessários, com dono por recurso e resultado verificável.
7. Ao terminar um lote, atualize registros afetados, segurança, backup pertinente, evidências e próximo passo. Continue o trabalho elegível dentro da missão. Pare por limite, dependência bloqueada, decisão material ausente ou fim do escopo; não invente tarefas para manter o loop.

## Estado e resposta

Responda com objetivo recuperado, ação escolhida e resultado/evidência. Pergunte novamente somente o que não pôde recuperar e muda a decisão. `CADU STATUS` pede relatório do estado, sem iniciar tarefas. `CADU PARAR` interrompe apenas processos próprios abrangidos quando houver controle real e registra o resultado; texto não encerra supervisor remoto inacessível.

Fontes: [read.md](read.md), [continuidade](politicas/CONTINUIDADE.md), [segurança](politicas/SEGURANCA_ENGENHARIA.md) e [backup](politicas/BACKUP_DRIVE.md).


## Runtime obrigatório

A execução de qualquer prompt usa o Contrato Comum V3 uma vez por sessão. Organize a missão como Harness, Loop e Graph. Carregue apenas contexto pertinente, mantenha o prefixo estável quando houver reutilização de cache, limite ciclos, atualize checkpoint e registre o próximo nó. Use P30 para missões longas e não replique o contrato em cada prompt.
