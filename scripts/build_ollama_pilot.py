#!/usr/bin/env python3
"""Render the approved Mac pilot in PT/EN/ES without network or activation."""
from pathlib import Path
from markdown_it import MarkdownIt
import hashlib
import html
import json

ROOT = Path(__file__).resolve().parents[1]
LANGS = [('pt-BR', '', 'Português', 'Preparação aprovada', 'Início'),
         ('en', '.en', 'English', 'Preparation approved', 'Home'),
         ('es', '.es', 'Español', 'Preparación aprobada', 'Inicio')]

def build():
    meta = json.loads((ROOT/'docs/harness/ollama-release.json').read_text())
    out = ROOT/'docs/supervisor-mac'
    out.mkdir(exist_ok=True)
    for lang, suffix, label, status, home in LANGS:
        source = ROOT/f'docs/harness/CODEX_OLLAMA_PILOT{suffix}.md'
        text = source.read_text()
        digest = hashlib.sha256(text.encode()).hexdigest()
        for _, other, _, _, _ in LANGS:
            text = text.replace(f'(CODEX_OLLAMA_PILOT{other}.md)', f'(index{other}.html)')
        body = MarkdownIt('commonmark', {'html': False, 'linkify': False}).enable('table').render(text)
        body = body.replace('<table>', '<div class="table-scroll"><table>').replace('</table>', '</table></div>')
        route = '../index.html' if not suffix else f'../{lang}/index.html'
        page = f'''<!doctype html>
<html lang="{lang}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="description" content="Codex + Ollama — {status}"><meta http-equiv="Content-Security-Policy" content="default-src 'self'; style-src 'self'; object-src 'none'; base-uri 'self'; form-action 'none'"><title>Codex + Ollama | Engenharia Cadu</title><link rel="stylesheet" href="../assets/ollama-pilot.css"></head>
<body><header><a href="{route}">Engenharia Cadu · {home}</a><span>{html.escape(meta['version'])}</span></header><main data-source-sha256="{digest}">{body}</main></body></html>'''
        (out/f'index{suffix}.html').write_text(page)

if __name__ == '__main__':
    build()
