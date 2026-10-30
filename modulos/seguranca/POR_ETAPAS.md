# Campanha e cobertura por partes

## O que significa começo, meio e fim
**Começo:** antes do primeiro lote de código ou da primeira alteração em projeto existente. Levantar ameaças, dados, identidade, contratos, ferramentas, permissões e requisitos. No projeto vazio, concluir desenho/planejamento apropriado; verificações de runtime continuam NOT_RUN.

**Meio:** primeiro incremento integrado e os marcos que adicionem ou alterem fronteiras, permissões, regras críticas, serviços e dados. Rever também consumidores e helpers compartilhados. Não esperar “metade do prazo”; não tratar scan de diff como auditoria de todas as interfaces.

**Fim:** cada candidato de release, antes do GO. Revalidar a mesma revisão, cobertura global requerida, achados em aberto, revisão independente, backup e recuperação pertinentes. Depois do deploy, verificar configuração efetiva e controles operacionais autorizados; sucesso do build não prova produção segura.

**Durante:** after-batch/module-complete, phase-exit, local hooks quando usados, PR/CI e manutenção periódica. Eventos executam checks proporcionais ou exigem recibos atuais; não executam uma análise completa por IA a cada salvamento.

## Unidade de trabalho
Cada lote identifica projeto/snapshot; superfície e interfaces; diff/chamadores; atores/dados; controles e requisitos; testes e ferramentas permitidos; limites; revisor; dependências; saída e handoff. Uma fase do processo não é suficiente como escopo técnico. Em monorepo, inventariar todos os apps antes da priorização.

Cobertura: Reviewed / Partially reviewed / Not reviewed / N/A com fonte/motivo. Distinguir análise estática, configuração observada e teste real. Amostragem explícita; não extrapolar. Trabalho futuro fica no índice; lacuna obrigatória do lote atual bloqueia seu aceite. Mudança em controle compartilhado reabre consumidores afetados. Achados não somem porque saíram do diff.

## Fechamento e decisão
Concluir análise → reconciliar achados/contraevidências → registrar provas por revisão → emitir resumo e checkpoint → verificar controles/autorizações → continuar próximo lote elegível ou aguardar decisão material. Auditoria não aplica correções. Correção segue lote FIX aprovado e reteste. Nova tentativa exige informação/hipótese nova e limite; não reformar o produto para fazer teste passar.

Critical/High confirmados e exploráveis, segredo exposto, Emergency em aberto e checks essenciais ausentes impedem liberação conforme política da engenharia. Candidatos graves requerem triagem sem serem contados como confirmados. O gate de referência bloqueia conservadoramente High/Critical abertos e não oferece dispensa automática desses achados. Exceções possíveis na governança exigem decisão independente, motivo, escopo, responsável, prazo e controles adicionais; nunca rebaixar severidade para liberar.

## Custo e privacidade
Coletores/checks não precisam de LLM. Revisor recebe requisito, delta e contratos pertinentes. Registros integrais sanitizados privados; síntese na conversa. Não repetir leitura das mesmas fontes sem mudança. Relatório público de métodos não contém achados reais. Backup de relatórios de segurança requer autorização e proteção específica: não subir automaticamente nem para o Drive.

## Matriz inicial de eventos
Consultar [EVENTOS.json](hooks/EVENTOS.json): os nomes são contratos lógicos desta engenharia, não capacidades nativas presumidas de Codex/Gemini/Antigravity/OpenCode. O adaptador deve identificar mecanismo real e testar seu funcionamento. Mudança de cliente não elimina controles, mas também não transforma uma configuração desconhecida em instalada.
