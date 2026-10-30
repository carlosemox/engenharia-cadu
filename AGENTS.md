# Engenharia Cadu — instruções do repositório

Esta central distribui método, prompts, papéis e um site estático. Não é o aplicativo do usuário nem um supervisor operacional.

- Comece por `read.md`; consulte uma etapa em `p/` e somente as políticas pertinentes.
- Fontes canônicas: `p/`, `politicas/`, `templates/`, `catalogo/` e `agentes/`. A pasta `docs/` é a publicação derivada.
- Não carregar toda a biblioteca automaticamente. Codex principal; preservar modelo/autenticação autorizados.
- Preservar escopo, permissões, histórico e trabalho existente. Nenhum segredo em Git; não instalar catálogos em massa.
- Terceiros são referências/candidatos. Não executar arquivos ou ativar capacidades sem revisão.
- Alterações nesta central não alteram aplicativos, infraestrutura ou perfis privados.
- Verificação local: `python scripts/validate.py`; depois `python -m http.server 8080 --directory docs` para inspeção visual.
- Para reconstruir páginas, ler `site-src/README.md`. Não afirmar que a publicação remota foi verificada apenas pelo teste local.
- Atualizar CHANGELOG e o documento responsável; decisões de publicação e licenciamento têm alçada própria.
