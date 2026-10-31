#!/usr/bin/env python3
"""Build static prompt factory; standard library, no network or deployment."""
import html
import json
import re
from pathlib import Path
from prompt_factory import catalog, generate

ROOT = Path(__file__).resolve().parents[1]
DUMMY = {'projeto': '__CADU_TARGET__', 'pedido': '__CADU_REQUEST__', 'estudo_anexado': False}

def build():
    routes = catalog()['modes']
    out = ROOT / 'docs/fabrica'
    out.mkdir(parents=True, exist_ok=True)
    data = {'dummy': DUMMY, 'routes': {}}
    options = []
    for mode, route in routes.items():
        data['routes'][mode] = {**route, 'template': generate(mode, DUMMY['projeto'], DUMMY['pedido'])}
        options.append(f'<option value="{html.escape(mode)}">{html.escape(route["label"])}</option>')
    (out / 'routes.json').write_text(json.dumps(data, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
    default = html.escape(generate())
    page = '''<!doctype html>
<html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Fábrica de prompts | Engenharia Cadu</title><meta http-equiv="Content-Security-Policy" content="default-src 'self'; script-src 'self'; style-src 'self'; connect-src 'self'; object-src 'none'; base-uri 'self'; form-action 'none'"><link rel="stylesheet" href="../assets/factory.css"><script defer src="../assets/factory.js"></script></head>
<body><main><nav class="topbar"><a href="../index.html">← Engenharia Cadu</a><span class="languages"><a href="https://github.com/carlosemox/engenharia-cadu/blob/main/i18n/README.en.md">EN</a><a href="https://github.com/carlosemox/engenharia-cadu/blob/main/i18n/README.es.md">ES</a><span aria-current="page">PT</span></span></nav><p class="eyebrow">UM PEDIDO · UM CAMINHO · CONTEXTO RECUPERÁVEL</p><h1>Escolha o caminho. Gere o comando.</h1><p>Comece pelo botão que descreve sua situação. Depois informe o projeto e copie o comando para a conversa do agente aberta no projeto.</p>
<section class="pathways" aria-label="Escolha rápida do caminho"><div class="pathway"><span class="path-number">01</span><h2>Assumir projeto</h2><p>Você tem estudos, anexos ou código existente e precisa retomar com o estado real.</p><button class="path-button" type="button" data-mode="assumir">Começar por aqui</button></div><div class="pathway"><span class="path-number">02</span><h2>Reestruturar</h2><p>O projeto está confuso, incompleto ou fora do método e precisa de diagnóstico e correção.</p><button class="path-button" type="button" data-mode="reestruturar">Corrigir o caminho</button></div><div class="pathway"><span class="path-number">03</span><h2>Retomar checkpoint</h2><p>Já existe um estado salvo e você quer continuar do próximo lote registrado.</p><button class="path-button" type="button" data-mode="retomar">Retomar agora</button></div><div class="pathway pathway-primary"><span class="path-number">04</span><h2>Não sei qual usar</h2><p>Descreva o objetivo e a fábrica seleciona a menor rota suficiente.</p><button class="path-button" type="button" data-mode="auto">Escolher por mim</button></div></section>
<div class="grid"><section aria-label="Personalizar comando"><p class="section-kicker">PERSONALIZAR</p><label for="mode">O que você precisa?</label><select id="mode">OPTIONS</select><label for="target">Projeto</label><input id="target" placeholder="Nome, caminho ou repositório"><label for="request">Resultado desejado</label><textarea id="request" rows="5" placeholder="Ex.: reconciliar o estudo novo e retomar a implementação"></textarea><label class="check"><input id="attachment" type="checkbox"> Vou anexar um estudo à conversa</label><p class="small">A fábrica gera texto. A execução acontece no agente, conforme as autorizações reais do projeto.</p><p><a href="../comandos/ASSUMIR_PROJETO.txt" download>Baixar comando completo para assumir projeto</a></p><p><a href="../comandos/REESTRUTURAR_PROJETO.txt" download>Baixar comando completo para reestruturar</a></p></section>
<section aria-label="Comando gerado"><label for="output">Comando para copiar</label><textarea id="output" rows="21" readonly>DEFAULT</textarea><button id="copy" type="button">Copiar comando</button><p id="status" role="status" aria-live="polite"></p></section></div>
<noscript><p>A personalização requer JavaScript. O comando padrão acima e os downloads completos continuam disponíveis para copiar manualmente.</p></noscript>
<p class="small">Método 2.3 · Memória e agentes dependem dos recursos disponíveis no projeto. <a href="https://github.com/carlosemox/engenharia-cadu/blob/main/fabrica/README.md">Ler o funcionamento</a></p></main></body></html>'''.replace('OPTIONS',''.join(options)).replace('DEFAULT',default)
    (out / 'index.html').write_text(page, encoding='utf-8')
    for name in ('ASSUMIR_PROJETO', 'REESTRUTURAR_PROJETO'):
        source = (ROOT / f'comandos/{name}.md').read_text(encoding='utf-8')
        body = re.search(r'## Comando completo\n```text\n([\s\S]*?)\n```', source).group(1)
        (ROOT / f'docs/comandos/{name}.txt').write_text(body+'\n', encoding='utf-8')
    mirror = (ROOT/'read.md').read_text(encoding='utf-8')
    def canonical_link(match):
        url = match.group(1)
        if ':' in url or url.startswith(('#', '//')):
            return match.group(0)
        return '](https://github.com/carlosemox/engenharia-cadu/blob/main/'+url+')'
    mirror = re.sub(r'\]\(([^\s)]+)\)', canonical_link, mirror)
    (ROOT / 'docs/read.md').write_text(mirror, encoding='utf-8')
    print('Fábrica e dois comandos completos gerados; nenhum projeto executado.')

if __name__ == '__main__':
    build()
