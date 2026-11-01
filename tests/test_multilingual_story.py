"""Editorial and static-page contracts; not an audit of applications."""
import hashlib, importlib.util, re, subprocess, sys, unittest
from pathlib import Path
from html.parser import HTMLParser
R=Path(__file__).resolve().parents[1]
LOCALES={'pt-BR':('README.md','docs/index.html'),'en':('i18n/README.en.md','docs/en/index.html'),'es':('i18n/README.es.md','docs/es/index.html')}
IDS=['historia','comecar','metodo','integracoes','agentes','continuidade','documentos','auditoria','backup','economia','prompts','capacidades','operacao','evolucao']
class Page(HTMLParser):
 def __init__(self):super().__init__();self.tags=[]
 def handle_starttag(self,t,a):self.tags.append((t,dict(a)))
class StoryTests(unittest.TestCase):
 def test_sources_cover_same_sections(self):
  for src,_ in LOCALES.values():self.assertEqual(re.findall(r'<!-- section:([a-z]+) -->',(R/src).read_text()),IDS)
 def test_sources_include_all_prompt_ids(self):
  for src,_ in LOCALES.values():
   text=(R/src).read_text()
   for i in range(31):self.assertIn(f'[P{i:02d}]',text)
 def test_sources_do_not_change_shortcuts(self):
  for src,_ in LOCALES.values():
   text=(R/src).read_text()
   for suffix in ['engenharia-cadu/main/p/P01.md','engenharia-cadu/main/p/P07.md','engenharia-cadu-adocao/main/read.md']:self.assertIn('https://raw.githubusercontent.com/carlosemox/'+suffix,text)
 def test_no_unapproved_guarantee_in_copy(self):
  for src,_ in LOCALES.values():
   text=(R/src).read_text();self.assertNotIn('100% secure',text);self.assertNotIn('segurança garantida',text);self.assertIn('NOT_RUN',text);self.assertIn('MIT',text)
 def test_generated_page_contracts(self):
  for lang,(src,dst) in LOCALES.items():
   with self.subTest(lang=lang):
    text=(R/dst).read_text();p=Page();p.feed(text)
    self.assertEqual([a.get('lang') for t,a in p.tags if t=='html'],[lang]);self.assertEqual(sum(t=='h1' for t,a in p.tags),1)
    ids=[a['id'] for t,a in p.tags if 'id'in a];self.assertEqual(len(ids),len(set(ids)))
    for section in IDS:self.assertIn(section,ids)
    alternates={a.get('hreflang') for t,a in p.tags if t=='link' and a.get('rel')=='alternate'};self.assertEqual(alternates,{'pt-BR','en','es','x-default'})
    self.assertIn(hashlib.sha256((R/src).read_bytes()).hexdigest(),text)
    self.assertTrue(any(a.get('rel')=='canonical' for t,a in p.tags if t=='link'))
    for t,a in p.tags:
     if t in ['script','img','link'] and ('src'in a or a.get('rel')=='stylesheet'):
      self.assertFalse(a.get('src',a.get('href','')).startswith('https://'))
 def test_no_script_needed_for_content(self):
  for _,dst in LOCALES.values():
   text=(R/dst).read_text()
   for word in ['P00','P30','S01','CONTINUO_SUPERVISIONADO','Projetos 2026/Backup/']:self.assertIn(word,text)
   self.assertIn('Content-Security-Policy',text);self.assertNotIn('onclick=',text)
 def test_copy_targets_resolve(self):
  for _,dst in LOCALES.values():
   p=Page();p.feed((R/dst).read_text());ids={a['id'] for _,a in p.tags if 'id'in a}
   targets=[a['data-copy-target'] for _,a in p.tags if 'data-copy-target'in a];self.assertGreaterEqual(len(targets),3)
   for target in targets:self.assertIn(target,ids)
 def test_legacy_home_anchors_remain(self):
  text=(R/'docs/index.html').read_text()
  for section in ['comecar','prompts','metodo','agentes','capacidades','economia','documentos','operacao','auditoria']:self.assertIn(f'id="{section}"',text)
 def test_generate_is_idempotent(self):
  outputs=[R/dst for _,dst in LOCALES.values()]
  before=[p.read_bytes() for p in outputs]
  subprocess.run([sys.executable,str(R/'site-src/build_story.py')],cwd=R,check=True,capture_output=True)
  self.assertEqual(before,[p.read_bytes() for p in outputs])
 def test_language_resolver_is_path_specific(self):
  import ast
  tree=ast.parse((R/'scripts/validate.py').read_text())
  fn=next(n for n in tree.body if isinstance(n,ast.FunctionDef) and n.name=='expected_language')
  namespace={'ROOT':R};exec(compile(ast.Module(body=[fn],type_ignores=[]),'language-resolver','exec'),namespace)
  for path,lang in [('docs/index.html','pt-BR'),('docs/en/index.html','en'),('docs/es/index.html','es'),('docs/prompts/P01/index.html','pt-BR'),('docs/enough/index.html','pt-BR')]:
   self.assertEqual(namespace['expected_language'](R/path),lang)
 def test_spanish_interface_uses_spanish_review(self):
  text=(R/'docs/es/index.html').read_text()
  self.assertIn('Pruebas, revisión y recuperación',text)
  self.assertNotIn('Pruebas, revisão',text)
if __name__=='__main__':unittest.main()
