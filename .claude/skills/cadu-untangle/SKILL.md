---
name: cadu-untangle
description: Fazer diagnóstico estrutural seletivo em português, apenas leitura, e propor slices sob supervisão MIKE; nunca refatorar sem autorização P13.
argument-hint: "[área afetada]"
---
# Untangle Codebase — adaptação CADU
Escopo: $ARGUMENTS.
Proveniência: caldoai/skills, untangle-codebase, licença MIT, revisão fixada em catalogo/untangle-claude-source.json.
Esta é uma adaptação de DIAGNÓSTICO e não replica a instrução upstream de corrigir tudo.

1. Identifique repositório, SHA, ambiente, alterações existentes, autorização, testes e checkpoint.
2. Em modo read-only, liste vínculos ocultos (cópia de regras, globais e convenções implícitas), vínculos desnecessários (acoplamentos e dependência instável), excedentes comprovados (wrappers e código morto) e exceções justificadas de segurança e resiliência.
3. Anexe arquivo:linha/SHA, mapa de dependências e indícios de co-change; se houver dúvida, marque HIPÓTESE.
4. Divida propostas em slices verticais pequenos, cada um com dependências, dono exclusivo, testes permitidos e negados, orçamento e rollback. Consulte templates/MIKE_SLICE_CONTRACT.json.
5. Não editar arquivos, instalar pacotes, executar scripts externos nem remover testes ou comentários durante esta auditoria. Implementação exige autorização P13 separada e executor isolado.
6. Reporte PASS, FAIL, NOT_RUN ou INCONCLUSIVE, com a próxima decisão, sem inventar economia.
