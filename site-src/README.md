# Site da central

Site estático em `docs/`, publicado pelo GitHub Pages. Sem banco, API, rastreadores, CDNs ou fontes externas. `docs/assets/site.js` fornece busca, filtros, cópia e menu móvel. Os textos dos procedimentos são derivados de `p/`.

Validação: `python scripts/validate.py`. Prévia: `python -m http.server 8080 --directory docs`.

Para alterar o conteúdo de um prompt, edite `p/Pxx.md` e rode `python scripts/sync_prompts.py` para atualizar comando, páginas e metadados derivados. Mudanças de título, categoria, rotas ou layout precisam de revisão dos índices e validação de navegação. Não mantenha cópias manuais divergentes.

A publicação deste site não executa os prompts. Não há login, contas ou credenciais de cliente no frontend.
