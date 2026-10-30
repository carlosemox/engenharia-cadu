# Continuidade entre prompts — edição 2.2

## Regra central
Ao iniciar um produto do zero pelo P01, use CONTINUO_SUPERVISIONADO na sessão ativa. Depois de concluir e verificar cada etapa, leia somente o próximo procedimento pertinente da mesma revisão e continue, sem obrigar o usuário a copiar outro comando. Pedido de apenas uma fase, análise ou revisão de prompt permanece ISOLADO. Continuidade não amplia permissões nem dispensa decisões materiais.

Informe o modo, o alvo e a etapa. Entrevista continua interativa: pergunte o que falta, espere a resposta e retome. Não invente respostas para manter a sequência. Aprovações já concedidas para escopo claramente apresentado não precisam ser pedidas novamente por arquivo.

## Rota padrão
P01 → P02 → P03 → P04 → P05 → P06 → P07 → P08 → P09 → P10 → P11 → P12 → P13 → P14 → P15 → P16.

A rota depende do trabalho real. Pesquisa P02 pode ser dispensada com justificativa e evidência suficiente. P07 pode avançar em paralelo quando houver independência e autorização. P08 pode exigir revisão delimitada de P06 antes de bootstrap. P13/P14/P15 formam ciclos por incremento; com tarefas elegíveis retornar ao P13, com alteração de requisitos ao P12. Não repetir ciclo sem trabalho real e limite.

P17 controla uma missão prolongada, não é a etapa obrigatória após release. P18 retoma a etapa pendente depois de reconciliar o estado. P19–P28 são trilhas opcionais, acionadas por necessidade; não desenvolver finanças, vídeo e obras para todos os produtos. P00 escolhe o caminho. Adoção de projeto existente mantém a revisão do retrato/plano antes de alterações.

## Procedimento do coordenador
1. Conferir alvo, revisão dos procedimentos, estado real, recursos e autorizações. Um dono por tarefa/recurso; não iniciar outro coordenador para a mesma missão.
2. Executar somente a etapa e seus requisitos de entrada. Preservar modelo, provedor, autenticação e orçamento. Contexto pertinente, não a biblioteca inteira.
3. Conferir entrega, testes, segurança e backup aplicáveis. Código de saída zero ou autodeclaração não prova aceite. NOT_RUN não vira PASS.
4. Registrar checkpoint privado/canônico: projeto, etapa, plano, snapshot, artefatos, decisões, evidências, achados, recibo do backup, próxima etapa e motivo. Não guardar segredos. Estado salvo não significa processo persistente.
5. Conferir se o próximo escopo já está autorizado, se dependências e alçadas estão atendidas e se os limites permitem continuar. Aprovação em JSON é um registro a verificar, não concessão de autoridade.
6. Quando atendido, resumir a transição e ler/executar o próximo prompt na mesma sessão. Encerrar uma etapa não é encerrar a missão; não perguntar “quer que eu siga?” sem uma decisão real pendente.
7. Se houver decisão material, pedir uma aprovação consolidada e aguardar. Se houver falha/bloqueio, preservar estado e atuar somente em itens independentes autorizados. Se terminar o escopo, encerrar; não inventar funcionalidades.

## Gates preservados
- P03/P04: confirmação do escopo/requisitos antes do trabalho dependente. P05/P06: escolhas materiais de design, arquitetura e fornecedores precisam de decisão real; pode ser uma aprovação conjunta identificada.
- P09/P10: instalação global, criação remota, nova conta, custos, credenciais, runner, migrações, commit/push/merge e deploy mantêm alçadas próprias.
- P13/P14: implementação não é autoaprovação. Revisão independente deve ser uma execução separada quando requerida pelo risco. Corrigir e retestar o candidato afetado.
- P15/P16: segurança e qualidade da mesma revisão, backup/recuperação pertinentes e GO específico antes da produção. P16 pode preparar release sem publicá-lo.
- Falha de teste, achado bloqueante, evidência desatualizada ou backup obrigatório sem prova impedem a ação dependente.

## Segurança e backup transversais
Aplicar [Segurança](SEGURANCA_ENGENHARIA.md) e [Backup Drive](BACKUP_DRIVE.md) desde a concepção. Ao fechar etapa com novos artefatos, verificar a cópia pertinente; antes de operação arriscada, exigir proteção do estado anterior. Uma falha de Drive não autoriza migração/destruição sem backup; análise independente pode continuar.

## Limites
O perfil define máximo de transições, tentativas, chamadas, concorrência e duração. Ausente não significa ilimitado. Proposta inicial de bloco: até 8 transições e 2 tentativas por mesmo problema, sem alterar limites mais restritivos existentes. Ao atingir teto, checkpoint; não criar outra sessão para contorná-lo.

Se a sessão termina, o prompt não continua sozinho. Operação de 24 horas depende de P17, supervisor real, recursos, conexão Drive e controles testados. As conexões desta conversa não se transferem automaticamente ao Codex do computador.

Um seletor de próxima etapa pode validar metadados, mas nunca substitui verificação independente, autenticação de decisões ou controles do ambiente. Esta política é instrução do coordenador, não um supervisor instalado.
