# Validação editorial e funcional da fábrica V2.3

Data: 31/10/2026. Escopo: central de método, geradores, site estático e entradas de adoção. Aplicativos de clientes não foram migrados ou auditados nesta verificação.

- Suite Python: 91 testes passaram, incluindo rotas, revisão inválida, dados delimitados, paridade CLI/web, preservação literal dos procedimentos e cliente JavaScript via Node/DOM simulado.
- Validador: 31 procedimentos canônicos, 46 páginas HTML, 2.287 links locais, nenhum erro no momento da execução.
- JavaScript: 10 modos, caracteres literais de substituição (`$&`, `$$` e equivalentes), cópia e fallback. DOM simulado; não prova layout ou acessibilidade em navegador.
- Navegador real: NOT_RUN. Binário Chromium ausente; download retornou arquivo inválido. Não alegar verificação visual/interativa.
- Revisão independente SENTINEL: corrigidos links do espelho, localização das fontes nos comandos copiáveis e interpolação JavaScript. Os derivados removem somente contrato literalmente igual à fonte canônica; P01 especializado é preservado.
- Publicação GitHub e GitHub Pages requerem evidência própria; sucesso local não prova deploy.
- Agentes operacionais, instalação de ferramentas candidatas, auditoria dos aplicativos e benchmark de economia: NOT_RUN.

Reprodução: dependências editoriais fixadas em site-src/requirements.txt; gerar guias, sincronizar prompts, gerar narrativa e fábrica, executar `python -m unittest discover -s tests -q`, `node tests/test_factory_client.cjs` e `python scripts/validate.py`. O módulo markdown-it-py deve estar disponível no Python escolhido. Não é necessário instalar ferramentas de terceiros de eficiência para testar a fábrica.
