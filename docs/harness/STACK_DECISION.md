# Decisão de stack

Central atual: GitHub, documentos, scripts Python stdlib e site estático. P0/P1 não adicionam banco, autenticação, filas externas nem dependências.

Projetos novos: GitHub como fonte e CI; Supabase e Hostinger são preferências sujeitas ao produto e métricas. Não migrar IRM, EmiLand ou outro projeto por padrão. Revisar stack, auth, storage, ambientes, custos, backup e rollback antes de executar.

Não há métricas dos aplicativos que comprovem travamento com 30 usuários. Diagnóstico: query plans, índices/RLS, conexões e pooling compatível, chamadas duplicadas, CPU/memória, locks, p95/p99 e carga representativa. Teste de carga: BLOCKED por ausência de ambiente e orçamento de teste definidos.
