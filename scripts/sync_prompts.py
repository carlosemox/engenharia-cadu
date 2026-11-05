#!/usr/bin/env python3
"""Sync canonical commands to downloads and supported static presentation pages.

A page either embeds the full command or links explicitly to its generated TXT.
A missing embedding AND missing TXT link is an error, never silently ignored.
"""
import hashlib,html,re
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
GH='https://github.com/carlosemox/engenharia-cadu/blob/main/'
COMMON_PATTERN=r'CONTRATO COMUM — V3\nRead https://raw\.githubusercontent\.com/carlosemox/engenharia-cadu/main/politicas/CONTRATO_COMUM\.md[^\n]*\nAplique Harness, Loop e Graph:[^\n]*\n\n'
canonical_source=(ROOT/'p/P00.md').read_text()
canonical_common=re.search(COMMON_PATTERN,canonical_source)
if not canonical_common:raise ValueError('Canonical common header absent from P00')
for source in sorted((ROOT/'p').glob('P[0-9][0-9].md')):
 text=source.read_text();m=re.search(r'## Comando completo\n```text\n([\s\S]*?)\n```',text)
 pid=source.stem
 # Preserve the canonical fenced body verbatim in the thin execution form.
 stage_body=m.group(1) if m else text.strip()
 body=stage_body.strip()+'\n'
 # Thin execution form: same stage body, common contract loaded once per revision.
 common=re.search(COMMON_PATTERN,stage_body) if m else None
 # Keep any specialized contract verbatim rather than guessing equivalence.
 thin=stage_body[:common.start()]+stage_body[common.end():] if common and common.group(0)==canonical_common.group(0) else stage_body
 directory=ROOT/'execucao';directory.mkdir(exist_ok=True)
 digest=hashlib.sha256(source.read_bytes()).hexdigest()
 (directory/f'{pid}.md').write_text(f'# {pid} — execução com contexto sob demanda\n\nDerivado de [fonte canônica](../p/{pid}.md), SHA-256 `{digest}`. Não editar manualmente.\n\nAntes de executar, leia [contrato comum](../politicas/CONTRATO_COMUM.md) uma vez nesta sessão e revisão, incluindo saída comum, alçadas e coordenação. Reutilize enquanto válido; em sessão nova ou revisão diferente, recupere-o novamente. As instruções aplicáveis do projeto e a autorização real do usuário continuam prevalecendo.\n\n```text\n'+thin+'\n```\n')
 (ROOT/f'docs/comandos/{pid}.txt').write_text(body)
 mirror=re.sub(r'\]\(\.\./([^)]*)\)',lambda x:']('+GH+x.group(1)+')',text)
 (ROOT/f'docs/p/{pid}.md').write_text(mirror)
 page=ROOT/f'docs/prompts/{pid}/index.html'
 content,count=re.subn(r'(<pre id="full-command">)[\s\S]*?(</pre>)',lambda x:x.group(1)+html.escape(body)+x.group(2),page.read_text(),count=1)
 if count!=1 and f'href="../../comandos/{pid}.txt"' not in content:
  raise ValueError(f'Expected full-command block or explicit canonical TXT link: {page}')
 page.write_text(content)
print('Synced P00–P30 canonical bodies. Review metadata/navigation separately when changing titles or routes.')
