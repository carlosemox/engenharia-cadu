"""Public-library boundary, safety, generated links and deterministic output."""
import importlib.util
import json
import re
from pathlib import Path
import subprocess
import tempfile
import unittest
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('build_library', ROOT / 'scripts/build_library.py')
lib = importlib.util.module_from_spec(spec)
spec.loader.exec_module(lib)


class Parser(HTMLParser):
    def __init__(self, source):
        super().__init__()
        self.links, self.ids, self.records, self.scripts = [], set(), 0, []
        self.feed(source)

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if 'id' in attrs:
            assert attrs['id'] not in self.ids, attrs['id']
            self.ids.add(attrs['id'])
        for key in ('href', 'src'):
            if key in attrs:
                self.links.append(attrs[key])
        if 'record' in attrs.get('class', '').split():
            self.records += 1
        if tag == 'script':
            self.scripts.append(attrs.get('src'))


class LibraryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = lib.load_data(ROOT)

    def test_all_occurrences_preserved(self):
        raw = json.loads((ROOT / 'catalogo/inventario-auditado.json').read_text())
        self.assertEqual(len(self.data['entries']), 2566)
        self.assertCountEqual([r['id'] for r in raw['entries']], [r['id'] for r in self.data['entries']])
        self.assertEqual(sum(self.data['counts']['category'].values()), 2566)
        self.assertEqual(sum(bool(e['source']) for e in self.data['entries']), 2298)
        self.assertTrue(all(e['rights'] == 'REVIEW_REQUIRED_LICENSE_NOT_RECORDED' for e in self.data['entries']))

    def test_metadata_boundary(self):
        entry = lib.public_entry({'id': 'drive:1', 'name': 'Example', 'state': 'NOT_HOMOLOGATED', 'prompt': 'PRIVATE', 'body': 'SECRET', 'content': 'HIDDEN', 'source': 'https://drive.google.com/file/d/private'})
        self.assertEqual(entry['source'], '')
        self.assertFalse({'prompt', 'body', 'content'} & entry.keys())
        public = json.loads((ROOT / 'docs/biblioteca/metadata.json').read_text())
        self.assertTrue(all('content' not in role for role in public['roles']))

    def test_safe_urls(self):
        for url in ['javascript:alert(1)', 'data:text/html,abc', '//evil.test', 'https://user:pass@example.org/a', 'https://good.test\\@evil.test', 'https://a.test/\nx', 'https://[', 'https://a.test:bad/', 'file:///tmp/a', 'https://docs.google.com/document/d/x']:
            self.assertEqual(lib.safe_url(url), '', url)
        self.assertEqual(lib.safe_url('https://github.com/a/b/blob/abc/SKILL.md'), 'https://github.com/a/b/blob/abc/SKILL.md')

    def test_html_escape_and_no_active_content(self):
        payload = '\"><img src=x onerror=alert(1)><script>alert(1)</script>'
        data = json.loads(json.dumps(self.data))
        data['entries'] = [lib.public_entry({'id': payload, 'name': payload, 'family': payload, 'state': payload, 'source': 'https://example.org/?q="<script>'})]
        data['roles'][0]['translations']['en']['content'] = payload
        page = lib.page(data, 'en')
        self.assertNotIn('<img', page)
        self.assertNotIn('<script>alert', page)
        self.assertIn('&lt;script&gt;', page)
        self.assertEqual(Parser(page).scripts, ['../assets/library.js'])

    def test_languages_links_assets_and_filters(self):
        for lang, filename in [('pt-BR', 'index.html'), ('en', 'index.en.html'), ('es', 'index.es.html')]:
            path = ROOT / 'docs/biblioteca' / filename
            source = path.read_text()
            self.assertIn(f'<html lang="{lang}">', source)
            parsed = Parser(source)
            self.assertEqual(parsed.records, 0)
            self.assertLess(len(source.encode()), 100_000)
            self.assertIn('2566', source)
            self.assertIn('<noscript>', source)
            self.assertIn(lib.ATTRIBUTION, source)
            self.assertEqual(source.count(lib.LICENSE_URL), 11)
            self.assertTrue({'search', 'category', 'state', 'source', 'reset', 'empty', 'result-count', 'filters', 'records', 'pagination', 'previous', 'next'} <= parsed.ids)
            for link in parsed.links:
                url = urlsplit(link)
                if url.scheme:
                    self.assertTrue(lib.safe_url(link), link)
                else:
                    target = path.parent / unquote(url.path) if url.path else path
                    self.assertTrue(target.exists(), str(target))
                    if url.fragment and target == path:
                        self.assertIn(url.fragment, parsed.ids)

    def test_originals_only_and_portable_links(self):
        folder = ROOT / 'docs/biblioteca/originais'
        self.assertEqual({p.name for p in folder.iterdir()}, {name + suffix + '.md' for name in lib.ORIGINAL_FILES for suffix in ('', '.en', '.es')})
        bundle = json.loads((ROOT / 'docs/biblioteca/originais.json').read_text())
        self.assertEqual(len(bundle['roles']), 10)
        self.assertEqual(bundle['attribution'], lib.ATTRIBUTION)
        self.assertEqual(bundle['licensing_notice'], lib.LICENSE_URL)
        for role in bundle['roles']:
            self.assertEqual((ROOT / 'docs/biblioteca' / role['download']).read_text(), lib.downloadable_content((ROOT / role['source']).read_text(), role['source']))
            self.assertEqual(role['content'], (ROOT / role['source']).read_text())
            self.assertIn('allowed_paths', role)
            self.assertTrue(role['usage'])

    def test_build_is_deterministic(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / 'catalogo').mkdir()
            (root / 'agentes/i18n').mkdir(parents=True)
            for path in [ROOT / 'catalogo/inventario-auditado.json', ROOT / 'catalogo/esquadroes.json', *[ROOT / f'agentes/{n}.md' for n in lib.ORIGINAL_FILES], *sorted((ROOT / 'agentes/i18n').glob('*.md'))]:
                (root / path.relative_to(ROOT)).write_bytes(path.read_bytes())
            lib.build(root)
            first = {str(p.relative_to(root)): p.read_bytes() for p in (root / 'docs').rglob('*') if p.is_file()}
            lib.build(root)
            second = {str(p.relative_to(root)): p.read_bytes() for p in (root / 'docs').rglob('*') if p.is_file()}
            self.assertEqual(first, second)
            for name, content in first.items():
                self.assertEqual(content, (ROOT / name).read_bytes(), name)

    def test_translation_completeness(self):
        for role in self.data['roles']:
            self.assertEqual(set(role['translations']), {'en', 'es'})
            original_procedures = re.findall(r'\[P\d+\]', role['content'])
            for lang, translated in role['translations'].items():
                self.assertEqual(re.findall(r'\[P\d+\]', translated['content']), original_procedures)
                self.assertEqual(translated['content'].count('\n## '), role['content'].count('\n## '))
                self.assertIn('NOT_RUN', translated['content'])
                self.assertTrue(translated['usage'])
                self.assertEqual(translated['content'], (ROOT / translated['source']).read_text())
                self.assertEqual((ROOT / 'docs/biblioteca' / translated['download']).read_text(), lib.downloadable_content(translated['content'], translated['source']))
                page = (ROOT / f'docs/biblioteca/index.{lang}.html').read_text()
                self.assertIn(lib.esc(translated['content']), page)
                self.assertIn(f'lang="{lang}"', page)
                for link in re.findall(r'\]\(([^)]+)\)', translated['content']):
                    self.assertTrue((ROOT / translated['source']).parent.joinpath(link).exists())

    def test_client_filter_behavior(self):
        # Exercise real async client code with DOM methods that reject HTML sinks.
        script = r'''
const assert = require('node:assert/strict');
const fs = require('node:fs');
const code = fs.readFileSync(process.argv[1], 'utf8');
class Node {
  constructor(tag) { this.tag=tag; this.children=[]; this.dataset={}; this.value=''; this.hidden=true; this.handlers={}; this.attrs={}; }
  set innerHTML(value) { throw Error('Unsafe HTML sink'); }
  set textContent(value) { this.text=String(value); this.children=[]; }
  get textContent() { return (this.text||'') + this.children.map(n=>n.textContent).join(''); }
  append(...nodes) { this.children.push(...nodes); }
  replaceChildren(...nodes) { this.children=nodes; }
  addEventListener(event, fn) { this.handlers[event]=fn; }
  setAttribute(key,value) { this.attrs[key]=value; }
  focus() { this.focused=true; }
}
async function init(entries, failure) {
  const nodes={};
  for (const id of ['search','category','state','source','reset','result-count','empty','filters','records','pagination','previous','next']) { nodes[id]=new Node('div'); nodes[id].id=id; }
  nodes['result-count'].dataset={results:'results',page:'Page',loading:'Loading',error:'Failed',rights:'Review required',upstream:'Upstream',missing:'Missing'};
  global.document={getElementById:id=>nodes[id],createElement:tag=>new Node(tag)};
  global.fetch=async (url, options)=> { assert.equal(url,'metadata.json'); assert.equal(options.credentials,'omit'); if(failure==='network')throw Error('Offline'); return {ok:failure!=='http',json:async()=>{if(failure==='json')throw Error('JSON');return {entries}}}; };
  await eval(code);
  return nodes;
}
(async()=>{
  const entries=Array.from({length:65},(_,i)=>({id:`id${i}`,name:i===0?'São <script>literal</script>':`Record ${i}`,category:i<40?'UI':'API',state:i%2?'STATIC':'NOT_HOMOLOGATED',source_group:i<40?'a':'b',source:'https://github.com/owner/repo/blob/sha/SKILL.md'}));
  const unsafe=['javascript:alert(1)','data:text/html,evil','//github.com/a','https://github.com.evil.test/a','https://evil.test/a','https://user:pass@github.com/a','https://github.com:444/a','https://github.com\\@evil.test/a','https://github.com/\nx'];
  unsafe.forEach((url,i)=>{entries[i].source=url});
  const n=await init(entries);
  assert.equal(n.filters.hidden,false); assert.equal(n.pagination.hidden,false);
  assert.equal(n.records.children.length,30);
  assert.equal(n['result-count'].textContent,'65 / 65 results · Page 1 / 3');
  assert.equal(n.previous.disabled,true); assert.equal(n.next.disabled,false);
  assert.equal(n.records.children[0].children[0].textContent,'São <script>literal</script>');
  for(let i=0;i<unsafe.length;i++) assert.equal(n.records.children[i].children[3].children.length,0);
  assert.equal(n.records.children[10].children[3].children[0].href,entries[10].source);
  n.next.handlers.click(); assert.equal(n.records.children[0].children[0].textContent,'Record 30');
  n.next.handlers.click(); assert.equal(n.records.children.length,5); assert.equal(n.next.disabled,true);
  n.previous.handlers.click(); assert.equal(n.records.children.length,30);
  n.category.value='UI';n.category.handlers.change();
  assert.equal(n['result-count'].textContent,'40 / 65 results · Page 1 / 2');
  n.next.handlers.click();assert.equal(n.records.children.length,10);
  n.search.value='sao literal';n.search.handlers.input();
  assert.equal(n.records.children.length,1);assert.equal(n.previous.disabled,true);
  n.source.value='b';n.source.handlers.change();assert.equal(n.records.children.length,0);assert.equal(n.empty.hidden,false);assert.equal(n.next.disabled,true);
  n.reset.handlers.click();assert.equal(n.records.children.length,30);assert.equal(n.search.focused,true);
  n.state.value='STATIC';n.state.handlers.change();assert.equal(n['result-count'].textContent,'32 / 65 results · Page 1 / 2');
  const empty=await init([]); assert.equal(empty.empty.hidden,false);assert.equal(empty.records.children.length,0);
  for(const failure of ['network','http','json']) {
    const failed=await init(entries,failure);assert.equal(failed['result-count'].textContent,'Failed');assert.equal(failed.filters.hidden,true);assert.equal(failed.records.attrs['aria-busy'],'false');
  }
})().catch(error=>{console.error(error);process.exitCode=1});
'''
        result = subprocess.run(['node', '-e', script, str(ROOT / 'docs/assets/library.js')], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        js = (ROOT / 'docs/assets/library.js').read_text()
        self.assertNotIn('innerHTML', js)
        self.assertNotIn('insertAdjacentHTML', js)


if __name__ == '__main__':
    unittest.main()
