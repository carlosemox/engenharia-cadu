# TRD e decisões arquiteturais — template
Estado: A_PREENCHER.

## Escopo técnico
REQ atendidos; plataformas; módulos; runtime/stack existentes ou aprovados; contratos; trade-offs; requisitos operacionais. Não escolher stack por hábito do toolkit.

## Dados e acesso
Schema, invariantes, isolamento por organização, autorização servidor, migrações, seeds, retenção e recuperação; integrações INT e fronteiras de confiança.

## APIs e execução
Entradas/saídas/erros; autenticação; idempotência; callbacks/webhooks; timeouts/retries; filas e estados; fallback; observabilidade sanitizada. Distinguir serviço do produto de ferramenta do desenvolvedor.

## Decisões
ADR curto: contexto, alternativas, escolha, consequências, fonte/evidência e gatilho de revisão. Prova crítica pendente bloqueia apenas o incremento dependente.

## Operação
Ambientes, build/deploy, artefato, testes, orçamento, backups/restore, contingência. Nomes/referências de secrets, nunca valores. GO separado.
