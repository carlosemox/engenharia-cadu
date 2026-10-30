# Registro de revisão de segurança — template inativo

Estado inicial: **NOT_RUN**. Preencher não comprova uma avaliação nem substitui revisão independente. Salvar o relatório real em destino privado, sem segredos ou dados desnecessários.

## Alvo e cobertura
Projeto, revisão/artefato, ambiente, escopo, autorização, avaliador, data, modelo de ameaças, ferramentas/versões e limitações. Identificar revisão independente real ou autoavaliação. Testes dinâmicos somente no alvo e intensidade autorizados.

| Área | Aplicabilidade | Teste/evidência | PASS / FAIL / NOT_RUN | Limites |
|---|---|---|---|---|
| Identidade e sessão | A definir | | NOT_RUN | |
| Autorização de objeto/papel/tenant | A definir | | NOT_RUN | |
| Entradas, uploads e APIs | A definir | | NOT_RUN | |
| Dados, RLS e Storage | A definir | | NOT_RUN | |
| Segredos e dependências | A definir | | NOT_RUN | |
| CI, infraestrutura e agentes | A definir | | NOT_RUN | |
| Backup e recuperação | A definir | | NOT_RUN | |

## Achados
ID, severidade justificada, localização/revisão, precondições, cenário, impacto, evidência sanitizada, responsável, correção, reteste e riscos residuais. Não rebaixar achado para liberar publicação. Achado crítico/alto confirmado e explorável bloqueia release conforme a política; falso positivo exige investigação documentada.

## Parecer
Cobertura efetiva, evidências válidas, testes não executados, bloqueios, decisão do responsável e validade. Mudanças materiais invalidam as provas afetadas. Nenhum resultado significa ausência garantida de invasões. GO de produção é uma autorização distinta.

[Política de segurança](../politicas/SEGURANCA_ENGENHARIA.md)
