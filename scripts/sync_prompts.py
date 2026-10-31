#!/usr/bin/env python3
"""Sync canonical commands to downloads and supported static presentation pages.

A page either embeds the full command or links explicitly to its generated TXT.
A missing embedding AND missing TXT link is an error, never silently ignored.
"""
import hashlib,html,re
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
GH='https://github.com/carlosemox/engenharia-cadu/blob/main/'
COMMON_PATTERN=r'CONTRATO COMUM — APLICAR EM TODAS AS ETAPAS\n[\s\S]*?Sem ferramentas, entregue conteúdo ou diagnóstico documental, não execução fictícia\.\n\n'
canonical_common=re.search(COMMON_PATTERN,(ROOT/'politicas/CONTRATO_COMUM.md').read_text())
if not canonical_common:raise ValueError('Canonical common contract absent')
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
 page.write_text(content)
print('Synced 29 canonical bodies. Review metadata/navigation separately when changing titles or routes.')
