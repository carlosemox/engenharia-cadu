# Site da central

Site estático em `docs/`, publicado pelo GitHub Pages. Sem banco, API, rastreadores, CDNs ou fontes externas. A apresentação principal tem português brasileiro (`docs/index.html`), inglês (`docs/en/index.html`) e espanhol (`docs/es/index.html`).

## Fontes editoriais e idiomas

`README.md`, `i18n/README.en.md` e `i18n/README.es.md` são as fontes da narrativa trilíngue. O português brasileiro é a base editorial. A tradução cobre a apresentação, navegação, chamadas e descrições dos 29 procedimentos; não traduz nem altera os prompts canônicos ou guias vinculados. O prompt universal S01 continua em inglês.

`site-src/build_story.py` gera as três páginas completas e estáticas. `docs/assets/story.css` e `story.js` fornecem apresentação responsiva, navegação, busca e cópia progressivas. A leitura e os links continuam disponíveis sem JavaScript. Cada página inclui hash da fonte, idioma, canonical e alternates.

A biblioteca interativa anterior foi preservada integralmente em `docs/biblioteca.html`, em português, usando os assets `site.css` e `site.js`. Os endereços de prompts e guias anteriores permanecem estáveis. Não apagar ou sobrescrever essa cópia ao regenerar a narrativa.

## Regenerar sem criar versões divergentes

Em ambiente editorial isolado com as dependências revisadas de `site-src/requirements.txt`, executar nesta ordem:

```text
python site-src/organize_guides.py
python scripts/sync_prompts.py
python site-src/build_story.py
python -m unittest discover -s tests -q
python scripts/validate.py
```

O gerador da narrativa deve rodar por último entre os geradores: substitui a página inicial com a apresentação trilíngue, após o gerador legado organizar guias. Se estiver alterando somente a copy, executar `build_story.py` e as verificações pertinentes é suficiente. Os geradores não usam rede, credenciais, modelos ou deploy.

Para alterar um procedimento, editar `p/Pxx.md`; `sync_prompts.py` atualiza seus derivados. Títulos, categorias e rotas também exigem revisão dos índices. Preservar P00–P28, S01 e os limites operacionais.

## Verificação e publicação

O validador exige `lang=en` sob `docs/en/`, `lang=es` sob `docs/es/` e `pt-BR` nos demais HTMLs. Os testes trilíngues verificam cobertura editorial, links de entrada, hashes, idiomas, metadados, alvos de cópia e regeneração idempotente.

Prévia autorizada: `python -m http.server 8080 --directory docs`. Navegador, teclado, menu, busca, cópia e dimensões precisam de testes interativos próprios; revisão estática não os substitui. Não contornar bloqueios do ambiente. Atualizar o manifesto após a revisão e conferir commit e GitHub Pages separadamente.

Fontes dos guias existentes: políticas, `OPERACAO.md` e módulo S01. Seus corpos também carregam hashes para detectar divergência. O site não executa prompts, instala hooks, ativa backup nem inicia supervisores.
