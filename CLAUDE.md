# Engenharia CADU — entrada Claude Code (português)
Esta pasta é a biblioteca de método, não uma aplicação de produção. Preserve o trabalho existente; leia AGENTS.md, comando.md e apenas o contrato pertinente em politicas/CONTRATO_COMUM.md.

## Responsabilidade
Cadu aprova decisões e alçadas; MIKE supervisiona o desenvolvimento quando ativado; JARVIS continua separado; Codex é o coordenador técnico legado e Claude Code é executor/revisor autorizado. A existência deste arquivo não instala daemon ou libera gastos.

## Uso operacional
Com ECC já instalado, não duplicar agentes, skills ou hooks. Para coordenação por projetos acione /cadu-mike, para segurança use /cadu-ecc-seguranca e para desenho de execução use /cadu-ecc-fluxo. Fonte: politicas/ECC_INTEGRACAO_OPERACIONAL.md e comandos/MIKE_ECC_OPERAR.md.

Reconciliar repo/HEAD, instruções locais, autorizações, testes e checkpoint; Untangle read-only seletivo; contrato por slice, um escritor por recurso; avaliação de riscos e custo; implementar somente após aprovação P13, revisar em P14, medir P24. P06 é arquitetura, não é permissão de escrita. Até três ciclos por nó. Preferir verificações determinísticas e um Sonnet por slice aprovado; Haiku apenas para triagem apropriada; Opus/Fable somente com justificativa e orçamento aprovado. Preservar ambientes, serviços, dados e credenciais.

Nenhuma integração, merge, push, deploy, publicação, alteração de acesso ou cobrança automática sem alçada efetiva. Use testes positivos/negativos, rollback e revisão independente. Não presumir controles de segurança apenas porque estão descritos no prompt.
