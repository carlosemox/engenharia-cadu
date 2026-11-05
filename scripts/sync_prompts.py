#!/usr/bin/env python3
"""Sync canonical commands to downloads and supported static presentation pages.

A page either embeds the full command or links explicitly to its generated TXT.
A missing embedding AND missing TXT link is an error, never silently ignored.
"""
import hashlib,html,re
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
GH='https://github.com/carlosemox/engenharia-cadu/blob/main/'
COMMON_PATTERN=r'CONTRATO COMUM — V3\nRead https://raw.githubusercontent.com/carlosemox/engenharia-cadu/main/politicas/CONTRATO_COMUM.md[^\n]*\n[\s\S]*?\n\n'
reference=(ROOT/'p/P00.md').read_text()
reference_command=re.search(r'## Comando completo\n```text\n([\s\S]*?)\n```',reference)
if not reference_command:raise ValueError('Reference command absent in P00')
canonical_common=re.search(COMMON_PATTERN,reference_command.group(1))
if not canonical_common:raise ValueError('Canonical common contract absent in P00')
for source in sorted((ROOT/'p').glob('P[0-9][0-9].md')):
 text=source.read_text();m=re.search(r'## Comando completo\n```text\n([\s\S]*?)\n```',text)
 if not m:raise ValueError(f'Command absent: {source}')
 pid=source.stem;body=m.group(1).strip()+'\n'
 # Thin execution form: same stage body, common contract loaded once per revision.
 common=re.search(COMMON_PATTERN,body)
 # Keep any specialized contract verbatim rather than guessing equivalence.
 thin=body[:common.start()]+body[common.end():] if common and common.group(0)==canonical_common.group(0) else body
 directory=ROOT/'execucao';directory.mkdir(exist_ok=True)
 digest=hashlib.sha256(source.read_bytes()).hexdigest()
 (directory/f'{pid}.md').write_text(f'# {pid} — execução com contexto sob demanda\n\nDerivado de [fonte canônica](../p/{pid}.md), SHA-256 `{digest}`. Não editar manualmente.\n\nAntes de executar, leia [contrato comum](../politicas/CONTRATO_COMUM.md) uma vez nesta sessão e revisão, incluindo saída comum, alçadas e coordenação. Reutilize enquanto válido; em sessão nova ou revisão diferente, recupere-o novamente. As instruções aplicáveis do projeto e a autorização real do usuário continuam prevalecendo.\n\n```text\n'+thin.rstrip()+'\n```\n')
 (ROOT/f'docs/comandos/{pid}.txt').write_text(body)
 mirror=re.sub(r'\]\(\.\./([^)]*)\)',lambda x:']('+GH+x.group(1)+')',text)
 (ROOT/f'docs/p/{pid}.md').write_text(mirror)
 page=ROOT/f'docs/prompts/{pid}/index.html'
 content,count=re.subn(r'(<pre id="full-command">)[\s\S]*?(</pre>)',lambda x:x.group(1)+html.escape(body)+x.group(2),page.read_text(),count=1)
 if count!=1 and f'href="../../comandos/{pid}.txt"' not in content:
  raise ValueError(f'Expected full-command block or explicit canonical TXT link: {page}')
 edition=re.search(r'\*\*Edição de publicação:\*\*\s*([^·\n]+)',text)
 if edition:content=re.sub(r'<span class="version">v[^<]+</span>',f'<span class="version">v{edition.group(1).strip()}</span>',content,count=1)
 content=content.replace('Biblioteca de prompts<b>29</b>','Biblioteca de prompts<b>31</b>')
 if 'href="../P29/"' not in content:
  extra=(f'<a class="{"selected" if pid=="P29" else ""}" href="../P29/"><span>P29</span> Proteção contra exposição e clonagem</a>'
         f'<a class="{"selected" if pid=="P30" else ""}" href="../P30/"><span>P30</span> Harness, Loop e Graph Engineering</a>')
  content=content.replace('</aside></div></main>',extra+'</aside></div></main>',1)
 page.write_text(content)
print('Synced P00–P30 canonical bodies and prompt-page metadata/navigation.')
