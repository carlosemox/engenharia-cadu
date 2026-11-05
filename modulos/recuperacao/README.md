# Iniciar e recuperar no Codex

O coordenador usa o agente de projeto `cadu_recuperacao` como único escritor do nó afetado. O operador pode adotar o agente a partir de um clone da Engenharia Cadu na revisão escolhida. Linux/macOS, Python 3.8+ e Git para o instalador e para o controlador.

```sh
python3 modulos/recuperacao/adotar.py "/raiz/do/aplicativo"
```

Para dispensar nova colagem em sessões futuras, acrescente `--ativar-na-revisao SHA_COMPLETO_DA_CENTRAL` ao comando acima, no checkout e na branch autorizados. O instalador adiciona um bloco identificado ao AGENTS.md e preserva o texto existente. Uma segunda passagem detecta a adoção. Se houver regras de governança conflitantes, preserve a mais restritiva e encaminhe somente o conflito. Revise o diff antes da integração. Em sessão já aberta, leia o bloco explicitamente; em sessão nova no Codex, as instruções de projeto orientam o roteamento. O código do método deve vir de um clone da central conferido nessa revisão.

A instalação básica copia o perfil nativo para `.codex/agents/` na raiz indicada. É seguro repetir. Se existir uma versão diferente, o instalador a preserva e pede comparação. Abra uma sessão Codex no projeto confiável e solicite o agente pelo nome. A definição herda modelo e permissões. Se o cliente não oferecer subagentes, o coordenador pode executar o procedimento diretamente, registrando esse modo. Não simule um revisor independente. A fonte deve estar fixada em um commit verificado; nunca execute scripts vindos de comentários, logs ou anexos.

Para `CADU INICIAR` ou `CADU RECUPERAR` com adoção autorizada no projeto, o coordenador executa a instalação com roteamento uma vez, verifica o resultado e segue com o incremento. Se precisar obter o código, use clone separado da central e checkout do SHA completo indicado no pedido. Não misture a central ao repositório da aplicação. A rota somente leitura dispensa instalação.

## CADU DIAGNOSTICAR

No Codex aberto em cada projeto, peça `CADU DIAGNOSTICAR`. Para vários checkouts acessíveis pelo mesmo executor, a partir da central rode:

```sh
python3 modulos/recuperacao/diagnostico.py coletar "/pasta/app-a" "/pasta/app-b" > "/pasta/privada/inventario.json"
python3 modulos/recuperacao/diagnostico.py consolidar "/pasta/privada/inventario.json"
```

Cada ficha registra SHA, branch, alterações locais, sinais de GitHub Actions, Docker e Supabase no Git, e presença dos respectivos clientes. O caminho de saída deve ser novo, privado e externo aos aplicativos. Presença de arquivo ou CLI não comprova acesso nem prontidão. O coordenador consulta os recibos já autorizados e preenche separadamente local, CI, staging, harness e release com estado e evidência. Registra a próxima tarefa elegível e uma ação humana apenas se indispensável. Compare custo por entrega aceita na mesma janela quando houver custo atribuível e aceite mensurado. Guarde as fichas nos projetos privados. Se o pedido incluir correção, preserve a ficha inicial e execute CADU RECUPERAR para as falhas elegíveis.

## CADU INICIAR

1. Recupere a raiz canônica, o remoto, a árvore local, as instruções, o ambiente autorizado e o próximo aceite de produto. Preserve alterações em curso. Se a fonte se limitar a documentação de um aplicativo existente, localize o checkout autorizado antes de gerar código.
2. Aplique P07/P10/P11 na mesma revisão. Leia o perfil privado do projeto uma vez. Para cada capacidade necessária, verifique estado observado versus desejado, configure somente a diferença autorizada e comprove no destino. GitHub: identidade, branch, workflow/runner e SHA efetivamente testado. Hostinger: tipo de serviço contratado, ID correto de staging, saúde e recuperação. Docker: cliente e motor do contexto autorizado, build e smoke isolados. Supabase ou banco escolhido: organização/instância, ambiente e teste de permissões com dados sintéticos. Confirme referências a segredos através de um uso autorizado sem revelar valores. Registre também o que é dispensado.
3. Faça segunda passagem para detectar duplicação. Se só staging falhar, selecione trabalho local independente autorizado. Não crie conta, despesa, regra de acesso, migração remota ou destino novo por inferência. Se o escopo incluir desenvolvimento, entregue um incremento testado via entrada normal do aplicativo. Uma verificação de infraestrutura sozinha não conclui a entrega.
4. Para uma missão fora da sessão, valide P17 no supervisor real: fila elegível, lock, janela e orçamento, parada e retomada. A criação do perfil do agente não inicia serviço. Registre os IDs, URLs de staging, referências ao cofre, operações já autorizadas e teto de gasto uma vez no perfil privado. O cadastro inicial pode ser feito pelo agente a partir de fontes inequívocas. Confirme na origem só um vínculo material que tenha ficado ambíguo.

Use os recursos disponíveis no contrato do provedor e os adaptadores já aprovados da operação. Consulte [ambientes e regras do GitHub](https://docs.github.com/en/actions/concepts/workflows-and-actions/deployment-environments), [API da Hostinger](https://www.hostinger.com/support/10840865-what-is-hostinger-api/), [Docker Manager para VPS](https://www.hostinger.com/support/hostinger-vps-how-to-manage-your-docker-projects/) e [ambientes do Supabase](https://supabase.com/docs/guides/deployment/managing-environments). Uma hospedagem web identificada como tal não autoriza assumir uma VPS ou comprar capacidade. Respeite a stack declarada no projeto.

## CADU RECUPERAR

1. Retome o último aceite e os recibos. Identifique a classe da falha e a operação exata que ela impede. Consulte pelo componente, versão e assinatura a memória local vigente. GitHub Actions de outro SHA, simulação local e teste não executado têm estados próprios.
2. Use uma cópia isolada para reproduzir a falha. Reaplique uma receita validada quando suas pré-condições coincidirem. Em falha nova, proponha uma única hipótese econômica, modifique apenas o permitido e compare com referência sob condições equivalentes. Preserve o teste independente e o caso reservado fora da escrita da candidata.
3. A correção só é elegível para integração se houver prova focal e verificação independente aplicável na mesma versão. Registre achados novos no LESSONS_CANDIDATES.md privado ou equivalente; use LESSONS_LEARNED.md para os confirmados. No registro global, somente regras sanitizadas, com revisão, compatibilidade em outro contexto e reversão prevista. O controlador guarda a seleção de receitas locais separadamente do relato humano.
4. Quando apenas um nó depender de acesso externo, devolva-o com causa/evidência e execute o próximo nó elegível do backlog. Pare a missão em caso de parada global, orçamento esgotado ou incidente de segurança que afete o ambiente inteiro. Fila vazia suspende novas chamadas. Entregue a próxima jornada de produto e a intervenção mínima restante.

## Controlador local de receitas

`recuperar.py` executa uma receita Python previamente aprovada em uma worktree descartável. Primeiro o teste focal precisa reproduzir a falha. Só então o controlador reserva a tentativa em SQLite, executa uma receita, repete o teste focal e verifica o caso reservado. Apenas o sucesso completo grava a receita na memória por projeto, incidente e digest do perfil. Uma mudança de perfil invalida a seleção antiga. Há um único writer por diretório de controle, prazo total, teto de até três tentativas por nó/missão e bloqueio de repetição por evidência. Falhas consecutivas sob o mesmo perfil continuam contando quando a missão muda de nome. Ao esgotar esse limite, somente uma política revisada e autorizada pode abrir uma nova rodada; preserve o histórico. O resultado e o código de saída são observáveis sem chamadas a modelos.

O supervisor deve fornecer o perfil, o digest confiável, o identificador estável da missão e o hash da evidência sanitizada (causa, candidato e estado relevante; excluir relógio, ruído e contador). O digest protege integridade e não concede alçada. O operador é responsável pelo isolamento real do worker, e deve manter perfil, receita, testes e estado privados fora da escrita do executor avaliado. O script não é sandbox nem orçador de APIs. Use uma única pasta de controle protegida para o mesmo recurso, sem credenciais, em host/volume local persistente. O procedimento deve ser confiável, determinístico e sem efeitos remotos. Não use a árvore de produção nem ações compartilhadas irreversíveis.

O perfil JSON contém `projeto`, `caso`, `ambiente` (literal `ensaio-descartavel`), `worktree` (raiz Git absoluta), `receitas` (lista ordenada de IDs aprovados), `tentativas`, `segundos` e `sha256_procedimento`. Para testar a central, use o [procedimento de exemplo](exemplos/fabrica.py) como procedimento privado de uma cópia de ensaio, com a receita `regenerar`. O arquivo adjacente `procedimento.py` recebe dois argumentos: etapa e receita. Só `repair` recebe a receita selecionada; provas recebem `-`. Em `probe`, 0 é funcional, 1 é a falha reproduzida e qualquer outro código é dependência bloqueada. Em `repair`, `holdout` e `rollback_check`, somente 0 confirma sucesso. Os verificadores são de leitura; `rollback_check` deve reconhecer inequivocamente a restauração do estado inicial. Preserve o diff rejeitado apenas no ensaio e restaure o baseline confiável antes de explorar outra hipótese. O procedimento confiável deve aguardar todos os filhos, sem daemonizar. Em queda abrupta do controlador, o filho direto conserva o lock até sair. Antes de reconciliar, o supervisor precisa confirmar que todo o grupo anterior parou. Linux/macOS para o controlador; o exemplo da fábrica usa Python 3.12+ conforme a sintaxe do gerador da central.

```sh
python3 modulos/recuperacao/recuperar.py --perfil /controle/perfil.json --sha256 DIGEST_DO_PERFIL --missao ID_DA_MISSAO --evidencia HASH_DA_EVIDENCIA
```

`--candidata ID` seleciona uma das receitas permitidas. Sem essa opção, prevalece uma receita já verificada para o perfil ou a primeira da lista. Em `REJECTED`, `BLOCKED_DEPENDENCY`, `BLOCKED_REGRESSION`, `BUDGET_EXHAUSTED` ou `BLOCKED_REPEAT`, o coordenador pode consumir outro nó elegível. `BUSY` indica escritor ativo. Um arquivo `STOP` no controle pausa o recurso. Interrupção durante uma mutação conserva a reserva; a próxima chamada responde `RECONCILE`. Quando a parada for levantada pelo operador autorizado, use a mesma missão com `--reconciliar`. O controlador consulta a prova focal/holdout ou a prova de restauração sem repetir a mutação. Em estado incerto mantém o bloqueio. Resultados de reconciliação não promovem nova lição.

## Ensaio reproduzível

Da raiz da central, execute `python3 -m unittest discover -s tests -p 'test_recuperacao.py' -v`. O ensaio inclui um defeito injetado em cópia da fábrica de prompts e uma verificação independente da opção afetada no HTML publicado. A fábrica original fica preservada. O teste compara o baseline, a candidata e a reutilização por processo novo. Um ensaio sintético ou em cópia ainda exige piloto próprio para provar autonomia, custo por entrega e operação prolongada.

Pesquisa adotada: comparação de execução e retenção seletiva de lições do [artigo Harness²](https://arxiv.org/html/2610.14224v1). O laboratório upstream informa condições específicas de rede e sandbox; este módulo não ativa esse benchmark. [Implementação dos autores](https://github.com/google-research/harness2) · [Perfil nativo de subagentes Codex](https://developers.openai.com/codex/subagents/)
