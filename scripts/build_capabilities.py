#!/usr/bin/env python3
"""Publish selected licensed references and full trilingual operating guides.

Deterministic, offline generation. Does not execute upstream code or install skills.
"""
import hashlib
import html
import json
from pathlib import Path
import posixpath
from urllib.parse import urlsplit
import zipfile
from markdown_it import MarkdownIt

ROOT = Path(__file__).resolve().parents[1]
BASE = 'https://github.com/carlosemox/engenharia-cadu/blob/main/'
LANGS = {
    'pt': ('pt-BR', '', 'Capacidades selecionadas', 'Baixar fontes e guias', 'Comando completo', 'Biblioteca'),
    'en': ('en', '.en', 'Selected capabilities', 'Download sources and guides', 'Full command', 'Library'),
    'es': ('es', '.es', 'Capacidades seleccionadas', 'Descargar fuentes y guías', 'Comando completo', 'Biblioteca'),
}


def render(source, path):
    md = MarkdownIt('commonmark', {'html': False}).enable('table')
    tokens = md.parse(source)
    def rewrite(items):
        for token in items:
            if token.type == 'heading_open' and token.tag == 'h1':
                token.tag = 'h2'
            if token.type == 'heading_close' and token.tag == 'h1':
                token.tag = 'h2'
            if token.type == 'link_open':
                url = token.attrGet('href')
                if not urlsplit(url).scheme and not url.startswith(('#', '//')):
                    resolved = posixpath.normpath(str(path.parent) + '/' + url)
                    if resolved.startswith('../'):
                        raise ValueError('Link escapes repository')
                    token.attrSet('href', BASE + resolved)
            if token.children:
                rewrite(token.children)
    rewrite(tokens)
    return md.renderer.render(tokens, md.options, {})


def build(root=ROOT):
    root = Path(root)
    manifest = json.loads((root / 'catalogo/marketing-import.json').read_text())
    out = root / 'docs/capacidades'
    out.mkdir(parents=True, exist_ok=True)
    # Only the explicit licensed source inventory and first-party guides are exported.
    files = set(manifest['files'])
    for path, expected in manifest['files'].items():
        if hashlib.sha256((root / path).read_bytes()).hexdigest() != expected:
            raise ValueError('Upstream integrity mismatch: ' + path)
    files.update({'catalogo/marketing-import.json', 'scripts/marketing_profile.py'})
    for _, suffix, *_ in LANGS.values():
        files.update({f'modulos/marketing/README{suffix}.md', f'comandos/APLICAR_MARKETING{suffix}.md'})
    archive = out / 'marketing-capabilities-1.0.0.zip'
    with zipfile.ZipFile(archive, 'w', zipfile.ZIP_DEFLATED) as z:
        for name in sorted(files):
            info = zipfile.ZipInfo(name, (2026, 11, 10, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            z.writestr(info, (root / name).read_bytes())
    for code, (lang, suffix, title, download, command, library) in LANGS.items():
        source_paths = [Path(f'modulos/marketing/README{suffix}.md'),
                        Path(f'integracoes/mastra/README{suffix}.md')]
        body = ''.join(render((root / p).read_text(), p) for p in source_paths)
        cmd = root / f'comandos/APLICAR_MARKETING{suffix}.md'
        (root / f'docs/comandos/APLICAR_MARKETING{suffix}.txt').write_text(cmd.read_text())
        nav = ' · '.join(f'<a href="index{v[1]}.html" hreflang="{v[0]}">{k.upper()}</a>' for k, v in LANGS.items())
        markup = f'''<!doctype html><html lang="{lang}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{title} | Engenharia Cadu</title><link rel="stylesheet" href="../assets/factory.css"><link rel="stylesheet" href="../assets/capabilities.css"></head><body><main><nav class="topbar"><a href="../biblioteca/index{suffix}.html">{library}</a><span>{nav}</span></nav><h1>{title}</h1><p>1.0.0 · 10/11/2026 · 11:10 · America/Sao_Paulo</p><p><a href="{archive.name}" download>{download}</a> · <a href="../comandos/APLICAR_MARKETING{suffix}.txt" download>{command}</a></p><p>SHA-256 ZIP: <code>{hashlib.sha256(archive.read_bytes()).hexdigest()}</code></p>{body}</main></body></html>'''
        (out / f'index{suffix}.html').write_text(markup)
    return len(files)


if __name__ == '__main__':
    print(f'Capabilities generated: {build()} archived files; no runtime activation.')
