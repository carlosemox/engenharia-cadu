# Apresentação trilíngue — verificação editorial

Data: 30/10/2026. Base: `180a1980dac98b5a9356dcbd7a82cd7b408979ee`.

## Escopo
Copy e storytelling próprios em português brasileiro, inglês e espanhol. Mesmos 14 capítulos e 31 procedimentos descritos. A tradução é da apresentação e da navegação, não de todos os prompts/guias. Fontes: README principal e traduções em `i18n/`. Biblioteca interativa anterior preservada em `docs/biblioteca.html`.

## Verificações executadas
- 11 testes editoriais locais aprovados, incluindo idiomas, cobertura de seções, IDs, metadados, hashes das fontes, alvos de cópia, preservação de âncoras e regeneração idempotente.
- Testes iniciais registraram falha por ausência das páginas antes da geração; testes finais aprovados após implementação.
- Sintaxe JavaScript conferida com `node --check docs/assets/story.js`.
- 367 referências relativas dos novos conteúdos conferidas contra os arquivos preparados e os destinos conhecidos da central; nenhuma referência ausente nesse escopo. Isso não é uma nova varredura completa de todos os links da biblioteca.
- Português, inglês e espanhol renderizados integralmente em HTML estático: leitura e links não dependem de execução de JavaScript. Assets locais, sem fontes, rastreadores ou serviços externos.
- Validador existente adaptado apenas para exigir o idioma correto por caminho. Regras de prompts, JSON e triagem de credenciais preservadas.

## Limites
A abertura da prévia em navegador retornou `ERR_BLOCKED_BY_ADMINISTRATOR`. Não houve tentativa de contornar o bloqueio. Inspeção visual desktop/mobile, teclado e funcionamento interativo de busca/cópia/menu: NOT_RUN. Sintaxe e contratos estáticos não substituem esses testes.

A suíte completa anterior da central não foi reexecutada neste ambiente editorial parcial. Não somar seus resultados históricos aos 11 testes desta entrega. Não foram feitas auditorias de aplicativos, testes de invasão, ativação de hooks, configuração de backups, alterações de contas, workflows ou supervisor.

Publicação remota e deploy devem ser confirmados pelo commit e pela execução do GitHub Pages. Este documento não substitui essa verificação nem afirma implantação operacional dos produtos.
