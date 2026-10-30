#!/usr/bin/env python3
"""Sync full procedure bodies from canonical Markdown into existing generated pages."""
import html,re
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
GH='https://github.com/carlosemox/engenharia-cadu/blob/main/'
for source in sorted((ROOT/'p').glob('P[0-9][0-9].md')):
 text=source.read_text();m=re.search(r'## Comando completo\n```text\n([\s\S]*?)\n```',text)
 if not m:raise ValueError(f'Command absent: {source}')
 pid=source.stem;body=m.group(1).strip()+'\n'
 (ROOT/f'docs/comandos/{pid}.txt').write_text(body)
 mirror=re.sub(r'\]\(\.\./([^)]*)\)',lambda x:']('+GH+x.group(1)+')',text)
 (ROOT/f'docs/p/{pid}.md').write_text(mirror)
 page=ROOT/f'docs/prompts/{pid}/index.html'
 content,count=re.subn(r'(<pre id="full-command">)[\s\S]*?(</pre>)',lambda x:x.group(1)+html.escape(body)+x.group(2),page.read_text(),count=1)
 if count!=1:raise ValueError(f'Expected full-command block: {page}')
 page.write_text(content)
print('Synced 29 canonical bodies. Review metadata/navigation separately when changing titles or routes.')
