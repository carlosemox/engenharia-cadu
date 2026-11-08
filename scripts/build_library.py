#!/usr/bin/env python3
"""Deterministic public library. Metadata only for third parties; no network/install."""
import html
import json
import re
from collections import Counter
from pathlib import Path
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[1]
ORIGINAL_FILES = ('coordenador', 'arquitetura', 'backend', 'frontend', 'qualidade',
                  'sentinel', 'guardian', 'release', 'produto', 'design')
LICENSE_URL = 'https://github.com/carlosemox/engenharia-cadu/blob/main/LICENCIAMENTO.md'
ATTRIBUTION = '© 2026 Carlos Eduardo do Amaral'
FIELDS = ('id', 'name', 'family', 'assessment', 'state', 'definition_hashes',
          'commit', 'sha256', 'risk_declared', 'frontmatter')
TEXT = {
 'pt': dict(title='Biblioteca de agentes e skills', intro='Catálogo público de referências e papéis documentados. Nenhum candidato é declarado instalado ou homologado. Downloads não executam nem instalam agentes.', search='Buscar por nome, ID ou metadados', category='Categoria', state='Estado', source='Origem', all='Todos', reset='Limpar filtros', results='resultados', empty='Nenhum resultado. Limpe os filtros ou altere a busca.', metadata='Baixar todos os metadados públicos (JSON)', bundle='Baixar os dez papéis originais (JSON)', originals='Papéis originais', inventory='Inventário de terceiros', rights='Licença não informada no inventário — revisão de direitos necessária antes de reutilizar.', upstream='Abrir origem canônica', missing='URL pública não informada', download='Baixar papel original (.md)', usage='Quando acionar', content='Conteúdo original completo (português)', paths='Caminhos permitidos', no_paths='Nenhum prefixo de escrita concedido por este papel.', note='Categorias derivadas da família ou do primeiro diretório da origem; não são classificações validadas. Registros são ocorrências, não agentes únicos. Metadados e conteúdo canônico preservam o idioma original.', noscript='Busca e filtros requerem JavaScript. Todos os registros e downloads permanecem disponíveis.', counts='registros de terceiros · 10 papéis originais', back='Engenharia Cadu', skip='Ir ao catálogo', squads='Esquadrões mapeados', permissions='Os caminhos documentados não concedem autorização de execução.'),
 'en': dict(title='Agent and skills library', intro='Public catalog of references and documented roles. No candidate is claimed to be installed or validated. Downloads do not execute or install agents.', search='Search name, ID or metadata', category='Category', state='State', source='Source', all='All', reset='Clear filters', results='results', empty='No results. Clear the filters or change your search.', metadata='Download all public metadata (JSON)', bundle='Download the ten original roles (JSON)', originals='Original roles', inventory='Third-party inventory', rights='License not recorded in the inventory — rights review required before reuse.', upstream='Open canonical upstream', missing='Public URL not recorded', download='Download original role (.md)', usage='When to use', content='Full original content (Portuguese)', paths='Allowed paths', no_paths='No write prefix granted by this role.', note='Categories derive from the family or first upstream directory; they are not validated classifications. Records are occurrences, not unique agents. Metadata and canonical content retain their original language.', noscript='Search and filters require JavaScript. All records and downloads remain available.', counts='third-party records · 10 original roles', back='Cadu Engineering', skip='Skip to catalog', squads='Mapped squads', permissions='Documented paths do not grant execution authorization.'),
 'es': dict(title='Biblioteca de agentes y skills', intro='Catálogo público de referencias y roles documentados. Ningún candidato se declara instalado ni homologado. Las descargas no ejecutan ni instalan agentes.', search='Buscar por nombre, ID o metadatos', category='Categoría', state='Estado', source='Origen', all='Todos', reset='Limpiar filtros', results='resultados', empty='Sin resultados. Limpie los filtros o cambie la búsqueda.', metadata='Descargar todos los metadatos públicos (JSON)', bundle='Descargar los diez roles originales (JSON)', originals='Roles originales', inventory='Inventario de terceros', rights='Licencia no registrada en el inventario — revisión de derechos necesaria antes de reutilizar.', upstream='Abrir origen canónica', missing='URL pública no registrada', download='Descargar rol original (.md)', usage='Cuándo utilizar', content='Contenido original completo (portugués)', paths='Rutas permitidas', no_paths='Este rol no concede ningún prefijo de escritura.', note='Las categorías derivan de la familia o del primer directorio de origen; no son clasificaciones validadas. Los registros son ocurrencias, no agentes únicos. Los metadatos y el contenido canónico conservan su idioma original.', noscript='La búsqueda y los filtros requieren JavaScript. Todos los registros y descargas siguen disponibles.', counts='registros de terceros · 10 roles originales', back='Ingeniería Cadu', skip='Ir al catálogo', squads='Escuadrones mapeados', permissions='Las rutas documentadas no conceden autorización de ejecución.'),
}


def esc(value):
    return html.escape(str(value), quote=True)


def safe_url(value):
    """Only absolute public HTTP(S) references, never active or private Drive URLs."""
    if not isinstance(value, str) or re.search(r'[\s\\\x00-\x1f\x7f]', value):
        return ''
    try:
        parsed = urlsplit(value)
        host = (parsed.hostname or '').lower()
        if (parsed.scheme not in ('https', 'http') or not host or parsed.username
                or parsed.password or host in ('drive.google.com', 'docs.google.com')):
            return ''
        parsed.port  # Reject malformed ports.
        return value
    except ValueError:
        return ''


def public_entry(raw):
    # Explicit allowlist: never carry through arbitrary prompt/body/content fields.
    entry = {k: raw[k] for k in FIELDS if k in raw}
    url = safe_url(raw.get('source'))
    entry['source'] = url
    parts = urlsplit(url).path.strip('/').split('/') if url else []
    entry['source_group'] = '/'.join(parts[:2]) if urlsplit(url).hostname == 'github.com' and len(parts) >= 2 else (urlsplit(url).hostname or 'drive-metadata')
    entry['category'] = raw.get('family') or (parts[4] if len(parts) > 5 and parts[2] == 'blob' else 'Uncategorized')
    entry['category_basis'] = 'family' if raw.get('family') else 'upstream_directory'
    entry['rights'] = 'REVIEW_REQUIRED_LICENSE_NOT_RECORDED'
    return entry


def downloadable_content(content, source):
    """Keep original prose; resolve relative Markdown links for portable downloads."""
    from posixpath import normpath
    def replace(match):
        target = match.group(1)
        if target.startswith('#') or urlsplit(target).scheme or target.startswith('//'):
            return match.group(0)
        resolved = normpath(str(Path(source).parent) + '/' + target)
        return '](https://github.com/carlosemox/engenharia-cadu/blob/main/' + resolved + ')'
    portable = re.sub(r'\]\(([^\s)]+)\)', replace, content)
    return portable.rstrip() + '\n\n---\n' + ATTRIBUTION + '\n\n[LICENCIAMENTO.md](' + LICENSE_URL + ')\n'


def load_data(root):
    inventory = json.loads((root / 'catalogo/inventario-auditado.json').read_text(encoding='utf-8'))
    routing = json.loads((root / 'catalogo/esquadroes.json').read_text(encoding='utf-8'))
    entries = [public_entry(e) for e in inventory['entries']]
    entries.sort(key=lambda e: (e['name'].casefold(), e['id']))
    roles = []
    for role in routing['roles']:
        source = role['source']
        if source not in {f'agentes/{name}.md' for name in ORIGINAL_FILES}:
            raise ValueError('Not an authorized original agent: ' + source)
        content = (root / source).read_text(encoding='utf-8')
        usage = re.search(r'## Quando acionar\n(.*?)(?=\n## |\Z)', content, re.S)
        roles.append(dict(id=role['id'], name=content.splitlines()[0].lstrip('# '),
                          source=source, state=role['state'], allowed_paths=role['allowed_prefixes'],
                          usage=usage.group(1).strip() if usage else '', content=content,
                          download='originais/' + Path(source).name,
                          squads=[s['id'] for s in routing['squads'] if role['id'] in s['roles']]))
    for role in roles:
        role['translations'] = {}
        for lang, heading in [('en', 'When to use'), ('es', 'Cuándo utilizar')]:
            filename = Path(role['source']).stem + '.' + lang + '.md'
            source = 'agentes/i18n/' + filename
            content = (root / source).read_text(encoding='utf-8')
            usage = re.search(r'## ' + heading + r'\n(.*?)(?=\n## |\Z)', content, re.S)
            if not usage:
                raise ValueError('Missing translated usage: ' + source)
            role['translations'][lang] = dict(name=content.splitlines()[0].lstrip('# '),
                source=source, content=content, usage=usage.group(1).strip(),
                download='originais/' + filename)
    if len(roles) != 10 or len({r['source'] for r in roles}) != 10:
        raise ValueError('Expected ten distinct original roles')
    return dict(schema_version=1, attribution=ATTRIBUTION, licensing_notice=LICENSE_URL, date=inventory['date'], scope=inventory['scope'],
                entries=entries, roles=roles, squads=routing['squads'],
                counts={'inventory': len(entries), 'originals': len(roles),
                        **{key: dict(sorted(Counter(e[key] for e in entries).items()))
                           for key in ('category', 'state', 'source_group')}})


def page(data, lang):
    t = TEXT[lang]
    filenames = {'pt': 'index.html', 'en': 'index.en.html', 'es': 'index.es.html'}
    nav = ''.join(f'<a href="{filename}" hreflang="{code}"'+(' aria-current="page"' if code == lang else '')+f'>{code.upper()}</a>' for code, filename in filenames.items())
    controls = ''
    for key, field in [('category', 'category'), ('state', 'state'), ('source', 'source_group')]:
        options = ''.join(f'<option value="{esc(v)}">{esc(v)} ({n})</option>' for v, n in data['counts'][field].items())
        controls += f'<div><label for="{key}">{t[key]}</label><select id="{key}"><option value="">{t["all"]}</option>{options}</select></div>'
    localized = {
        'pt': ('Conteúdo completo · original canônico em português', 'Português: original canônico. EN/ES: traduções dos dez papéis. Nomes e metadados de terceiros preservam o idioma da fonte.'),
        'en': ('Full content · English translation', 'Portuguese is the canonical original. EN/ES are translations of the ten roles. Third-party names and metadata retain their source language.'),
        'es': ('Contenido completo · traducción al español', 'El portugués es el original canónico. EN/ES son traducciones de los diez roles. Los nombres y metadatos de terceros conservan el idioma de origen.'),
    }[lang]
    t = {**t, 'content': localized[0], 'note': t['note'] + ' ' + localized[1]}
    license_label = {'pt': 'Autoria e condições de uso', 'en': 'Attribution and terms of use', 'es': 'Autoría y condiciones de uso'}[lang]
    license_notice = f'<p class="small">{ATTRIBUTION} · <a href="{LICENSE_URL}">{license_label} · LICENCIAMENTO.md</a></p>'
    content_lang = 'pt-BR' if lang == 'pt' else lang
    roles = []
    for original in data['roles']:
        r = {**original, **original['translations'].get(lang, {})}
        paths = ', '.join(r['allowed_paths']) or t['no_paths']
        roles.append(f'<article class="pathway"><h3>{esc(r["name"])}</h3><p class="small">{esc(r["state"])}</p><h4>{t["usage"]}</h4><p lang="{content_lang}">{esc(r["usage"])}</p><h4>{t["paths"]}</h4><p><code>{esc(paths)}</code></p><p>{t["permissions"]}</p><p>{t["squads"]}: {esc(", ".join(r["squads"]) or "—")}</p><details><summary>{t["content"]}</summary><pre lang="{content_lang}">{esc(r["content"])}</pre></details><p><a href="{esc(r["download"])}" download>{t["download"]}</a></p>{license_notice}</article>')
    client_text = {
        'pt': dict(previous='Anterior', next='Próxima', page='Página', loading='Carregando catálogo…', error='Não foi possível carregar o catálogo. Use o download de metadados.', noscript='Sem JavaScript: consulte os papéis originais acima ou baixe os metadados completos.', source_link='Consultar inventário de origem'),
        'en': dict(previous='Previous', next='Next', page='Page', loading='Loading catalog…', error='Could not load the catalog. Use the metadata download.', noscript='Without JavaScript: read the original roles above or download the complete metadata.', source_link='View source inventory'),
        'es': dict(previous='Anterior', next='Siguiente', page='Página', loading='Cargando catálogo…', error='No se pudo cargar el catálogo. Utilice la descarga de metadatos.', noscript='Sin JavaScript: consulte los roles originales arriba o descargue los metadatos completos.', source_link='Consultar inventario de origen'),
    }[lang]
    t = {**t, **client_text}
    labels = ' '.join(f'data-{key}="{esc(t[key])}"' for key in ('results', 'page', 'loading', 'error', 'rights', 'upstream', 'missing'))
    home = {'pt': '../index.html', 'en': '../en/index.html', 'es': '../es/index.html'}[lang]
    return f'''<!doctype html>
<html lang="{'pt-BR' if lang == 'pt' else lang}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{t['title']} | Engenharia Cadu</title><meta http-equiv="Content-Security-Policy" content="default-src 'self'; script-src 'self'; style-src 'self'; connect-src 'self'; object-src 'none'; base-uri 'self'; form-action 'none'"><link rel="stylesheet" href="../assets/factory.css"><link rel="stylesheet" href="../assets/library.css"><script defer src="../assets/library.js"></script></head>
<body><a class="skip" href="#catalog">{t['skip']}</a><main><nav class="topbar" aria-label="Languages"><a href="{home}">{t['back']}</a><span class="languages">{nav}</span></nav><h1>{t['title']}</h1><p class="intro">{t['intro']}</p><p><strong>{len(data['entries'])} {t['counts']}</strong> · {esc(data['date'])}</p><p>{t['note']}</p><p><a href="metadata.json" download>{t['metadata']}</a></p><p><a href="originais.json" download>{t['bundle']}</a></p>{license_notice}
<section aria-labelledby="roles-title"><h2 id="roles-title">{t['originals']}</h2><div class="library-grid">{''.join(roles)}</div></section>
<section id="catalog" aria-labelledby="catalog-title"><h2 id="catalog-title">{t['inventory']}</h2><div id="filters" hidden><label for="search">{t['search']}</label><input id="search" type="search"><div class="filters">{controls}</div><button id="reset" type="button">{t['reset']}</button></div><p id="result-count" role="status" aria-live="polite" {labels}>{len(data['entries'])} {t['results']}</p><p id="empty" hidden>{t['empty']}</p><noscript><p>{t['noscript']}</p></noscript><p><a href="https://github.com/carlosemox/engenharia-cadu/blob/main/catalogo/inventario-auditado.json">{t['source_link']}</a></p><div class="library-grid" id="records" aria-busy="false"></div><nav id="pagination" hidden aria-label="{t['page']}"><button id="previous" type="button" disabled>{t['previous']}</button><button id="next" type="button" disabled>{t['next']}</button></nav></section></main></body></html>\n'''


def build(root=ROOT):
    root = Path(root)
    data = load_data(root)
    out = root / 'docs/biblioteca'
    (out / 'originais').mkdir(parents=True, exist_ok=True)
    metadata = {**data, 'roles': [{**{k: v for k, v in r.items() if k not in ('content', 'translations')},
        'translations': {lang: {k: v for k, v in translation.items() if k != 'content'}
                         for lang, translation in r['translations'].items()}} for r in data['roles']]}
    for name, value in [('metadata.json', metadata), ('originais.json', {'schema_version': 1, 'attribution': ATTRIBUTION, 'licensing_notice': LICENSE_URL, 'roles': data['roles']})]:
        (out / name).write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    for original in data['roles']:
        for role in [original, *original['translations'].values()]:
            (out / role['download']).write_text(downloadable_content(role['content'], role['source']), encoding='utf-8')
    for lang, name in [('pt', 'index.html'), ('en', 'index.en.html'), ('es', 'index.es.html')]:
        (out / name).write_text(page(data, lang), encoding='utf-8')
    return data


if __name__ == '__main__':
    result = build()
    print(f"Library generated: {len(result['entries'])} metadata records, {len(result['roles'])} original roles. No installation or publication.")
