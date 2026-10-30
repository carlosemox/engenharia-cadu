#!/usr/bin/env python3
"""Validate static content, local routes and canonical prompt parity. Standard library only."""
import json,re,sys,html
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit,unquote
ROOT=Path(__file__).resolve().parents[1]
errors=[];links=0
def expected_language(path):
 relative=path.relative_to(ROOT).as_posix()
 if relative.startswith('docs/en/'):return 'en'
 if relative.startswith('docs/es/'):return 'es'
 return 'pt-BR'
class Links(HTMLParser):
 def __init__(self):super().__init__();self.urls=[];self.ids=set();self.lang=None;self.h1=0
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if tag=='html':self.lang=a.get('lang')
  if tag=='h1':self.h1+=1
  if 'id' in a:self.ids.add(a['id'])
  for attr in ('href','src'):
   if attr in a:self.urls.append(a[attr])
def check_link(source,url):
 global links
 u=urlsplit(url)
 if u.scheme or u.netloc or not u.path:return
 links+=1; p=(source.parent/unquote(u.path)).resolve()
 if not p.is_relative_to(ROOT):errors.append(f'Path outside root: {source.relative_to(ROOT)} -> {url}');return
 if p.is_dir():p=p/'index.html'
 if not p.exists():errors.append(f'Missing: {source.relative_to(ROOT)} -> {url}')
for p in ROOT.rglob('*.html'):
 parser=Links();parser.feed(p.read_text())
 if parser.lang!=expected_language(p):errors.append(f'Incorrect language: {p}')
 if parser.h1!=1:errors.append(f'Expected one h1: {p} ({parser.h1})')
 for u in parser.urls:check_link(p,u)
for p in ROOT.rglob('*.md'):
 text=re.sub(r'```[\s\S]*?```','',p.read_text())
 for url in re.findall(r'\]\(([^\s)]+)(?:\s+[^)]*)?\)',text):check_link(p,url)
prompts=list((ROOT/'p').glob('P[0-9][0-9].md'))
if len(prompts)!=29:errors.append('Expected 29 canonical prompts')
for p in prompts:
 m=re.search(r'## Comando completo\n```text\n([\s\S]*?)\n```',p.read_text())
 if not m:errors.append(f'Missing command: {p}');continue
 txt=(ROOT/f'docs/comandos/{p.stem}.txt').read_text()
 if txt.strip()!=m.group(1).strip():errors.append(f'Drift: {p.stem}')
for p in ROOT.rglob('*.json'):
 try:json.loads(p.read_text())
 except Exception as e:errors.append(f'Invalid JSON {p}: {e}')
# Pattern checks are triage, not a security certification.
for p in ROOT.rglob('*'):
 if not p.is_file() or p.suffix not in ('.md','.html','.json','.js','.css','.txt'):continue
 text=p.read_text()
 for pattern in (r'-----BEGIN (?:RSA |OPENSSH |EC )?PRIVATE KEY-----',r'ghp_[A-Za-z0-9]{30,}',r'sk-proj-[A-Za-z0-9_-]{40,}'):
  if re.search(pattern,text):errors.append(f'Potential credential in {p.relative_to(ROOT)}')
result={'status':'PASS' if not errors else 'FAIL','canonical_prompts':len(prompts),'html_pages':len(list(ROOT.rglob('*.html'))),'local_links_checked':links,'errors':errors,'browser_validation':'NOT_RUN: approved browser environment required','runtime_agents':'NOT_RUN'}
print(json.dumps(result,ensure_ascii=False,indent=2));sys.exit(bool(errors))
