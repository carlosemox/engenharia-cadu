# Site da central

Site estático em `docs/`, publicado pelo GitHub Pages. Sem banco, API, rastreadores, CDNs ou fontes externas. A apresentação principal tem português brasileiro (`docs/index.html`), inglês (`docs/en/index.html`) e espanhol (`docs/es/index.html`).

## Fontes editoriais e idiomas

`README.md`, `i18n/README.en.md` e `i18n/README.es.md` são as fontes da narrativa trilíngue. O português brasileiro é a base editorial. A tradução cobre a apresentação, navegação, chamadas e descrições dos 31 procedimentos; não traduz nem altera os prompts canônicos ou guias vinculados. O prompt universal S01 continua em inglês.

`site-src/build_story.py` gera as três páginas completas e estáticas. `docs/assets/story.css` e `story.js` fornecem apresentação responsiva, navegação, busca e cópia progressivas. A leitura e os links continuam disponíveis sem JavaScript. Cada página inclui hash da fonte, idioma, canonical e alternates.

A biblioteca interativa anterior foi preservada integralmente em `docs/biblioteca.html`, em português, usando os assets `site.css` e `site.js`. Os endereços de prompts e guias anteriores permanecem estáveis. Não apagar ou sobrescrever essa cópia ao regenerar a narrativa.

## Regenerar sem criar versões divergentes

Em ambiente editorial isolado com as dependências revisadas de `site-src/requirements.txt`, executar nesta ordem:

```text
python scripts/sync_prompts.py
python site-src/build_story.py
python site-src/organize_guides.py
python -m unittest discover -s tests -q
python scripts/validate.py
```

O gerador da narrativa substitui a página inicial com a apresentação trilíngue; executar `organize_guides.py` depois para completar a navegação operacional, como exige o teste de idempotência. Se estiver alterando somente a copy, executar `build_story.py`, `organize_guides.py` e as verificações pertinentes. Os geradores não usam rede, credenciais, modelos ou deploy.

Para alterar um procedimento, editar `p/Pxx.md`; `sync_prompts.py` atualiza seus derivados. Títulos, categorias e rotas também exigem revisão dos índices. Preservar P00–P30, S01 e os limites operacionais.

## Verificação e publicação

O validador exige `lang=en` sob `docs/en/`, `lang=es` sob `docs/es/` e `pt-BR` nos demais HTMLs. Os testes trilíngues verificam cobertura editorial, links de entrada, hashes, idiomas, metadados, alvos de cópia e regeneração idempotente.

Prévia autorizada: `python -m http.server 8080 --directory docs`. Navegador, teclado, menu, busca, cópia e dimensões precisam de testes interativos próprios; revisão estática não os substitui. Não contornar bloqueios do ambiente. Atualizar o manifesto após a revisão e conferir commit e GitHub Pages separadamente.

Fontes dos guias existentes: políticas, `OPERACAO.md` e módulo S01. Seus corpos também carregam hashes para detectar divergência. O site não executa prompts, instala hooks, ativa backup nem inicia supervisores.

## Fábrica V3

Após os geradores acima, execute `python scripts/build_factory.py`. O catálogo canônico fica em `fabrica/rotas.json`; o gerador atualiza a página, os templates do cliente web, os dois downloads e `docs/read.md`. Os assets `factory.js` e `factory.css` são fontes locais. A página apenas gera texto e não envia os campos. Testar CLI, paridade de templates e links; interação no navegador tem evidência separada.

`sync_prompts.py` também gera `execucao/Pxx.md`, mantendo todas as instruções específicas e referenciando o contrato comum uma vez por sessão/revisão. A forma completa em `p/` e seus downloads continua disponível.


## Biblioteca de agentes e skills

`python scripts/build_library.py` gera `docs/biblioteca/index.html`,
`index.en.html` e `index.es.html`, com busca local, filtros e downloads.
Não substituir `docs/biblioteca.html` (acervo legado de prompts).
Conteúdo original: arquivos em `agentes/`; terceiros: metadados do inventário
auditado e links de procedência, sujeitos a licença. Não copiar pacotes privados
para a página pública. Regerar biblioteca antes do validador de links.
Manutenção agendada não instala agentes nem chama IA paga: docs/harness/AUTONOMY.md.

## Piloto Codex + Ollama no Mac

Fontes integrais PT/EN/ES: `docs/harness/CODEX_OLLAMA_PILOT*.md`.
Metadados: `docs/harness/ollama-release.json`. Gerar com
`python scripts/build_ollama_pilot.py`; destinos: `docs/supervisor-mac/index*.html`.
Versão e timestamp são fixados na fonte, sem relógio variável no build.
Preparação aprovada não significa runtime instalado ou modelo homologado.
