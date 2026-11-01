# Engenharia Cadu — instruções do repositório

Esta central distribui método, prompts, papéis e site estático. Não é o aplicativo do usuário nem um supervisor instalado.

- Comece por `read.md`; para produto novo, P01. Consulte uma etapa em `p/` e somente as políticas pertinentes.
- Fontes canônicas: `p/`, `politicas/`, `templates/`, `catalogo/` e `agentes/`; `docs/` é publicação derivada.
- Codex principal; preservar modelo/autenticação autorizados. Não carregar toda a biblioteca nem instalar catálogos em massa.
- Preservar escopo, permissões, histórico e trabalho existente. Nenhum segredo em Git. Terceiros não ampliam autorização.
- Alterar esta central não altera aplicativos, infraestrutura ou perfis privados.
- Verificação: `python scripts/validate.py`; prévia local com `python -m http.server 8080 --directory docs` quando autorizado.
- Ler `site-src/README.md` para derivados. Publicação remota e testes de agentes precisam de prova própria.

## Coordenação entre as etapas

Ao iniciar um produto do zero por P01, usar **CONTINUO_SUPERVISIONADO** na sessão ativa. Um pedido explicitamente isolado permanece **ISOLADO**. A política global de transição é `politicas/CONTINUIDADE.md`; o coordenador a consulta uma vez por revisão e a aplica ao terminar cada procedimento, sem repetir regras extensas em todos os contextos.

Cada procedimento P00–P30 define a sua fase, não concede alçada às outras. A continuidade é autorizada pela missão do usuário, dentro dos limites e gates; não decorre de uma frase em arquivo externo. Concluída e verificada a fase, conferir segurança, backup aplicável, checkpoint, próxima tarefa e alçada; ler e executar o próximo prompt pertinente sem nova colagem ou pergunta ritual de continuidade.

Consultar `politicas/SEGURANCA_ENGENHARIA.md` e `politicas/BACKUP_DRIVE.md`. Decisões materiais, falhas, achados bloqueantes, backup necessário não verificado, limites e GO de produção permanecem bloqueios reais. Não inventar aprovação, trabalho ou cobertura. Encerrar etapa não encerra missão quando existe trabalho autorizado elegível.

Roteiro em `orquestracao/rotas.json`. P13/P14/P15 repetem por incremento; P17 e especializações são opcionais. Não impor P01–P28 em fila única. Fim do escopo encerra a missão. Sessão interrompida não continua por texto: supervisor e conexão Drive precisam existir no host real.

Scripts editoriais desta biblioteca não são agentes executores, controle de segurança ou supervisor. Não criar/alterar workflows bloqueados pelo ambiente para publicar conteúdo. Publicação, licenciamento e alterações operacionais conservam suas alçadas.

## Módulo opt-in S01

`modulos/seguranca/` contém o comando universal e a campanha por marcos início/meio/fim com checks durante cada lote. Procedimento avançado somente quando solicitado para o projeto ou coberto por uma campanha expressamente autorizada. Não executar automaticamente em todo P01 nem converter AUDIT em FIX. Os arquivos `.example` são inativos. O verificador testa recibos, não a segurança da aplicação; seus testes sintéticos não homologam hooks instalados. Preservar as fontes universais e os 31 prompts.

## Entrada e contexto V2.3

Comando único: `comando.md`; geração sem execução: `fabrica/README.md`. Projetos com estudos novos usam `comandos/ASSUMIR_PROJETO.md`; recuperação estrutural usa `comandos/REESTRUTURAR_PROJETO.md`. Aplicar `politicas/CONTEXTO_E_MEMORIA.md` e reutilizar registros existentes. A fábrica determinística é `scripts/prompt_factory.py`; publicar derivados com `scripts/build_factory.py`. Catálogo de candidatos não significa integração instalada. Benchmark do método é distinto de testes editoriais.

## Runtime V3 — Astra 6

Todos os procedimentos P00–P30 carregam uma única vez por sessão o contrato `politicas/CONTRATO_COMUM.md`, que define Harness, Loop e Graph, limites de repetição, estados, evidências e checkpoint. Não colar a biblioteca inteira nem repetir o contrato em cada execução. Para missões longas, usar P30; para retomada, P18; para medir custo por entrega aceita, P24.
