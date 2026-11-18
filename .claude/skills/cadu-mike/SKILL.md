---
name: cadu-mike
description: Coordenar desenvolvimento pela Engenharia CADU com MIKE, Harness, Loop, Graph, ECC e Claude Code em slices seguros, reutilizando contexto e especialistas.
argument-hint: "[projeto ou objetivo]"
---
# MIKE — comando operacional global em português
Ative ao receber MIKE, Engenharia CADU, desenvolvimento por slices, auditoria de código ou revisão geral. Escopo recebido: $ARGUMENTS.

Fonte principal: https://raw.githubusercontent.com/carlosemox/engenharia-cadu/main/comando.md
Fonte complementar: politicas/ECC_INTEGRACAO_OPERACIONAL.md no repositório Engenharia CADU.
Preserve o ambiente já escolhido, configurações de projeto, mudanças locais, regras mais restritivas e as aprovações existentes. Se a fonte estiver indisponível, registre e não invente autoridade.

1. Identifique o repositório ativo, SHA, branch, estado, requisitos, checkpoint e permissões efetivas. Não confunda a central Engenharia CADU com o produto-alvo. MIKE é supervisor do desenvolvimento, distinto de JARVIS.
2. Verifique se o ECC já está habilitado. Se estiver, reutilize seus agentes/skills; não instale cópias duplicadas nem ative hooks adicionais. ECC é referência comunitária, não superior às políticas do projeto.
3. Aplique Untangle seletivo e consulta progressiva em somente leitura quando houver acoplamento ou mudança transversal. Prefira ferramentas determinísticas antes de gastar tokens.
4. Decomponha em slices com objetivo observável, arquivos e recursos exclusivos, dependências, testes, risco, orçamento e rollback. Use P13 para IMPLEMENTAÇÃO, P14 para REVISÃO, P24 para MEDIÇÃO. P06 define arquitetura e NUNCA autoriza escrita.
5. Distribua a triagem simples para ferramentas locais/Haiku, o trabalho normal para um Sonnet por slice autorizado, e revisão independente para outro agente. Opus/Fable exige justificativa e autorização de custo. Não assumir ID/modelo disponível.
6. Segurança desde a entrada: fronteiras de confiança, entradas não confiáveis, credenciais, dependências, autorização negada, RLS/RBAC/ABAC, auditabilidade e recuperação conforme aplicabilidade; invocar cadu-ecc-seguranca para controles significativos.
7. Cada executor exige autorização P13 efetiva, escopo de escrita, branch/worktree e isolamento REAIS. Um escritor por recurso. Máximo 3 ciclos por nó. Não executar comandos apenas porque a skill os contém; revisar dependências e scripts.
8. Reconciliar artefatos e testes observados com o HEAD, revisão independente e custo total por slice aceito. Sem merge, deploy, publicação, mudança de acesso ou gastos automáticos.
9. Entregar RESULTADO, EVIDÊNCIAS, RISCOS, ESTADO e PRÓXIMO NÓ. Não alegar autonomia 24/7 ou instalação remota sem prova.

Modo padrão: análise e coordenação read-only até P13 autorizado. O próprio texto não impõe sandbox.
