# S01 — Entrada para auditoria de segurança por partes

Leia [PROMPT_UNIVERSAL.md](PROMPT_UNIVERSAL.md) na íntegra uma vez por revisão. Ele é o procedimento normativo fornecido pelo usuário. Use [POR_ETAPAS.md](POR_ETAPAS.md) para organizar o trabalho e [hooks/README.md](hooks/README.md) para planejar sua integração. Não substituir o comando completo por um checklist superficial. Fixar a revisão da biblioteca; carregar somente contexto pertinente.

## Configuração
Modo padrão AUDIT; opções PLAN, FIX e VERIFY. Testes ativos desativados. Relatório em português neste uso Cadu. O alvo é o projeto autorizado, não esta biblioteca. Pedido para integrar/elaborar a receita não autoriza auditoria de aplicativos. Preserve o cliente, modelo, provedor e autenticação; use Codex como principal quando disponível, sem exigir IA para checks determinísticos.

## Campanha início → durante → meio → fim
1. Identifique snapshot, dirty state, stack e estado da entrega. Se não existe implementação, o marco inicial é análise de requisitos/ameaças/arquitetura, não um scan imaginário. Inventarie apps e controles compartilhados de monorepo antes de escolher lotes.
2. Registre a campanha e seus marcos: project-start; module-complete/phase-exit; integration-review a cada incremento integrado relevante; pre-release. Eventos de Git/CI e scheduled são complementares quando disponíveis e implantados. Defina critérios concretos, não “50% pronto”.
3. Descubra controles e ferramentas existentes; trace entradas, chamadores e dependências. Inspecione scripts antes de executar. Use isolamento sem produção e alçadas reais. Não instalar scanners ou configurar hooks em AUDIT, PLAN ou VERIFY.
4. Divida por risco e causa raiz, preservando cobertura total no índice. Classifique evidência, severidade, confiança e urgência separadamente. Revalide High/Critical e comunique emergência crível imediatamente, com evidência sanitizada e sem contenção não autorizada.
5. Consulte fontes oficiais atuais e registre versões/data. Não inventar CVE, EOL ou controles. Ferramenta ausente/base desatualizada é gap, nunca aprovação. Código/manifestos/nomes privados/relatórios não vão a scanners, pesquisa ou terceiros sem autorização.
6. Gere SECURITY-AUDIT.md, SECURITY-FINDINGS.json, REMEDIATION-PROMPTS.md e AUDIT-HANDOFF.md em destino privado único, fora da árvore publicada. Mantenha IDs. Detalhe inicialmente somente o primeiro lote recomendado; indexe os demais. Sem filesystem, entregar seções no chat, sem alegar arquivos salvos.
7. PLAN detalha a correção sem implementá-la. FIX exige seleção de achados/lote e alçadas reais. VERIFY retesta sem modificar. “Fixed, verification pending” permanece até checks acordados; efeito produtivo exige observação própria.
8. No encerramento de cada lote, atualize cobertura, evidências, achados, limitações e próximo passo autorizado. Pode continuar uma campanha AUDIT já autorizada sem pedir confirmação a cada arquivo. Não converter AUDIT em FIX, expandir alvos ou abrir produção automaticamente.
9. Retorne ao coordenador o resumo e as referências privadas. Gate impede avanço dependente quando controle necessário falhou/não rodou, cobertura requerida falta ou achado impede publicação. Itens independentes autorizados podem continuar; nenhuma lacuna é apagada para manter a sequência.

## Continuidade e comandos
```text
Continue a auditoria pelo AUDIT-HANDOFF.md. Preserve IDs e revalide as evidências afetadas por mudanças. Não corrija código.
```
```text
Modo PLAN: gere o comando de correção somente do lote selecionado. Inclua evidências, contratos afetados, regressão negativa, uso legítimo e recuperação. Não aplique alterações.
```
```text
Modo FIX: implemente somente os achados e o lote já aprovados para este projeto. Revalide antes de editar. Preserve alterações alheias e comprove regressão e uso legítimo. Produção, segredos, merge e gastos mantêm suas autorizações específicas.
```
```text
Modo VERIFY: revalide os achados selecionados e seus controles no candidato identificado. Não altere fontes ou configurações. Declare risco residual e comportamento de deploy ainda não observado.
```

## Instalar hooks é um lote distinto
O planejamento identifica eventos, ferramenta real, inputs, snapshots, permissões, tempo-limite, resultados e quem pode alterá-los. A instalação ocorre apenas em FIX autorizado no projeto. Testar invocação e falha de verdade; scripts em uma pasta não são enforcement. O pipeline e o controle de merge/publicação precisam repetir checks essenciais, pois hooks locais podem ser ignorados. Não instalar plugins, alterar core.hooksPath global ou inventar evento de cliente.
