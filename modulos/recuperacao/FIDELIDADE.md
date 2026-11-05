# Fidelidade e grafo de aceite

Use `verificar_entrega.py` para conciliar um recorte aprovado com recibos obtidos fora da escrita de quem implementa. No diretório privado de controle, guarde o contrato e a cópia da especificação aceita. O responsável pelo escopo confere que os critérios cobrem a versão aprovada, inclusive negativas e jornadas completas. Tire o digest do contrato dessa fonte confiável. Um arquivo preparado pelo executor não pode homologar o trabalho do próprio executor.

Exemplo de contrato (substituir os digests pelos valores reais):

```json
{"projeto":"demo","fonte":"especificacao.md","fonte_sha256":"SHA256_DA_FONTE","criterios":[
  {"id":"R1","aceite":"Titular cria um pedido pela interface","ambiente":"staging","depende":[]},
  {"id":"R2","aceite":"Outro tenant recebe acesso negado ao pedido","ambiente":"staging","depende":["R1"]}
]}
```

O coletor independente entrega a estrutura abaixo. Cada arquivo referenciado precisa existir dentro do controle privado. Cada artefato de prova é uma observação JSON extraída pelo verificador independente, por exemplo `{"projeto":"demo","revisao":"SHA_GIT","ambiente":"staging","origem":"ID do job/teste","verificacoes":{"R1":"PASS"}}`. Um resultado de suíte pode cobrir vários critérios somente quando os identifica individualmente. O verificador compara esses campos com o recibo. O responsável confere na origem a execução e a correspondência semântica com o requisito. Um checksum verifica integridade de bytes. A proveniência, a qualidade do teste e a completude da especificação exigem verificação separada.

```json
{"projeto":"demo","revisao":"SHA_GIT","contrato_sha256":"SHA256_DO_CONTRATO","recibos":[
  {"id":"R1","ambiente":"staging","revisao":"SHA_GIT","estado":"PASS","arquivo":"prova-r1.json","sha256":"SHA256_DA_PROVA"}
]}
```

Rode `python3 modulos/recuperacao/verificar_entrega.py --contrato /controle/contrato.json --sha256-contrato DIGEST --recibos /controle/recibos.json --revisao SHA`. O exemplo retorna PARCIAL até existir prova do R2. O grafo rejeita ciclo e ID desconhecido. Um nó sem evidência impede o aceite de seus descendentes; nós independentes permanecem elegíveis. A lista de próximos itens depende ainda de autorização e orçamento. COBERTO_POR_RECIBOS descreve somente os critérios declarados. Capacidade nova identificada pelo agente entra como proposta separada e só integra o escopo por decisão compatível com a alçada.
