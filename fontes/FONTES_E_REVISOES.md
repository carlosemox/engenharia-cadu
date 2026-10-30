# Fontes, revisões e limites

Consulta: 29/10/2026. Redação Cadu V2 preparada para revisão; não é edição oficial ou endossada pelo autor do toolkit.

## Toolkit Matheus Gomes

Revisão consultada: `790a895304e0c08b70a5b215c9d334f1c86b816c`. A consulta da branch main nesta sessão retornou essa revisão. As instruções foram adaptadas para o escopo Cadu; não se fez cópia integral do repositório, instalação de dependências ou execução de seus scripts.

- [Catálogo de prompts](https://github.com/soumatheusgomes/vibe-coding-toolkit/blob/790a895304e0c08b70a5b215c9d334f1c86b816c/docs/prompts/README.md) — Mapa dos 15 procedimentos; numeração distinta dos IDs Cadu.
- [Brainstorm para plano](https://github.com/soumatheusgomes/vibe-coding-toolkit/blob/790a895304e0c08b70a5b215c9d334f1c86b816c/docs/prompts/04-brainstorm-to-plan.md) — Entendimento, plano verificável e continuidade conforme autorização.
- [Ondas paralelas](https://github.com/soumatheusgomes/vibe-coding-toolkit/blob/790a895304e0c08b70a5b215c9d334f1c86b816c/docs/prompts/05-parallel-wave-dispatch.md) — Dependências, arquivos e recursos isolados; integração coordenada.
- [Memória](https://github.com/soumatheusgomes/vibe-coding-toolkit/blob/790a895304e0c08b70a5b215c9d334f1c86b816c/docs/prompts/06-memory-bootstrap.md) — Índice pequeno, consulta sob demanda, fonte/validade e handoff temporário separado.
- [Ambiente](https://github.com/soumatheusgomes/vibe-coding-toolkit/blob/790a895304e0c08b70a5b215c9d334f1c86b816c/docs/prompts/10-development-environment-setup.md) — Inventário, configuração e validação; autorizações globais não foram transportadas automaticamente.
- [Projeto novo](https://github.com/soumatheusgomes/vibe-coding-toolkit/blob/790a895304e0c08b70a5b215c9d334f1c86b816c/docs/prompts/11-next-project-bootstrap.md) — Atalho e comando completo; stack específica adaptada à seleção por produto.
- [Projeto existente](https://github.com/soumatheusgomes/vibe-coding-toolkit/blob/790a895304e0c08b70a5b215c9d334f1c86b816c/docs/prompts/12-existing-project-setup.md) — Preservação, cobertura do catálogo, capacidade por tarefa e evidência; dividido em diagnóstico/execução.
- [Revisão independente](https://github.com/soumatheusgomes/vibe-coding-toolkit/blob/790a895304e0c08b70a5b215c9d334f1c86b816c/docs/prompts/03-multi-agent-code-review.md) — Alvo fixado, cenários concretos, deduplicação e lentes por risco.
- [Segurança](https://github.com/soumatheusgomes/vibe-coding-toolkit/blob/790a895304e0c08b70a5b215c9d334f1c86b816c/docs/prompts/13-security-review.md) — Escopo em leitura, fronteiras, dados privados e prova de reachability.
- [Avaliação do harness](https://github.com/soumatheusgomes/vibe-coding-toolkit/blob/790a895304e0c08b70a5b215c9d334f1c86b816c/docs/prompts/14-harness-evaluation.md) — Cópias descartáveis e avaliador protegido; relato distinto de evidência.
- [Melhoria do harness](https://github.com/soumatheusgomes/vibe-coding-toolkit/blob/790a895304e0c08b70a5b215c9d334f1c86b816c/docs/prompts/15-harness-improvement.md) — Comparação delimitada nativa; laboratório oficial opcional.
- [Catálogo de ferramentas](https://github.com/soumatheusgomes/vibe-coding-toolkit/blob/790a895304e0c08b70a5b215c9d334f1c86b816c/docs/tools/README.md) — 23 frentes e decisão por aplicabilidade.
- [Licença](https://github.com/soumatheusgomes/vibe-coding-toolkit/blob/790a895304e0c08b70a5b215c9d334f1c86b816c/LICENSE) — MIT com aviso de copyright preservado.

## Guias oficiais OpenAI consultados

- [Rethinking skills and prompts for GPT-6 Astra](https://developers.openai.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra): tarefa clara, instruções focadas e contexto relevante.
- [Using GPT-6](https://developers.openai.com/api/docs/guides/latest-model): comportamento, esforço, instruções e verificação; nomes/disponibilidade não são fixados eternamente pelos prompts.
- [Prompt caching](https://developers.openai.com/api/docs/guides/prompt-caching): cache depende da integração e deve ser avaliado, não presumido como economia garantida.
- [Codex non-interactive](https://developers.openai.com/codex/noninteractive): interfaces programáticas; não substituem supervisor e controles próprios.

## Materiais do próprio projeto

Filosofia e fluxo Cadu V1 e biblioteca P00–P28 disponibilizados na conversa; decisões subsequentes de Codex principal, colaboração por tarefa, design no briefing, serviços/APIs, economia no Astra e definição antes de publicação. Os nomes dos procedimentos foram preservados em identidade, com expansão de escopo declarada no CHANGELOG.

As referências ao acervo Amanda são critérios oriundos da auditoria estática anterior, não nova auditoria ou homologação dos demais catálogos. Nenhum conteúdo restrito desses pacotes foi copiado nesta biblioteca.

## Limites

Os textos de cada procedimento são instruções propostas, não afirmações de que APIs, modelos, flags ou planos específicos estão disponíveis na conta do usuário. O executor deve conferir o cliente e a documentação da versão real antes de operar. Exemplos e templates não concedem autorização.

A análise de licenças aqui preserva a licença MIT do toolkit-base. Não presume que ela cubra todas as ferramentas externas citadas e não escolhe a licença do futuro repositório Cadu.
