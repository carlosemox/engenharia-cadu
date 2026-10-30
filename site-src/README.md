# Site da central

Site estático em `docs/`, publicado pelo GitHub Pages. Sem banco, API, rastreadores, CDNs ou fontes externas. `docs/assets/site.js` fornece busca, filtros, cópia e menu móvel. Os textos dos procedimentos são derivados de `p/`.

Validação: `python scripts/validate.py`. Prévia: `python -m http.server 8080 --directory docs`.

Para alterar o conteúdo de um prompt, edite `p/Pxx.md` e rode `python scripts/sync_prompts.py` para atualizar comando, páginas e metadados derivados. Mudanças de título, categoria, rotas ou layout precisam de revisão dos índices e validação de navegação. Não mantenha cópias manuais divergentes.

A publicação deste site não executa os prompts. Não há login, contas ou credenciais de cliente no frontend.

## Guias e organização editorial

Fontes: `politicas/CONTINUIDADE.md`, `politicas/SEGURANCA_ENGENHARIA.md`, `politicas/BACKUP_DRIVE.md`, `politicas/CONTRATO_COMUM.md` e `OPERACAO.md`. O corpo das páginas carrega hash da fonte para checagem de divergência.

Em ambiente editorial isolado, com a dependência de `site-src/requirements.txt` instalada, executar `python site-src/organize_guides.py`, seguido de `python scripts/sync_prompts.py` e `python scripts/validate.py`. O gerador é idempotente; não usa rede, credenciais ou execução de prompts. O site final continua estático e sem dependências remotas. Nenhum workflow é criado ou alterado.

Atualizar o manifesto após revisão e conferir a publicação remota separadamente. Scripts de build não são controles operacionais do produto.
