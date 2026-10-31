#!/usr/bin/env python3
"""Build three static editorial pages from the canonical READMEs. No network or deploy."""
from pathlib import Path
from urllib.parse import urlsplit
import hashlib, html, posixpath, re
from markdown_it import MarkdownIt
R=Path(__file__).resolve().parents[1]
BASE='https://carlosemox.github.io/engenharia-cadu/'
GITHUB='https://github.com/carlosemox/engenharia-cadu/blob/main/'
LANGS={'pt-BR':('README.md','docs/index.html',''),'en':('i18n/README.en.md','docs/en/index.html','en/'),'es':('i18n/README.es.md','docs/es/index.html','es/')}
TEXT={
 'pt-BR':{'skip':'Ir ao conteúdo','menu':'Abrir navegação','nav':'Explorar a engenharia','language':'Idioma da apresentação','label':'ENGENHARIA DE PRODUTO COM IA','lead':'Uma visão de negócio. Um caminho verificável.','primary':'Começar um produto','secondary':'Organizar projeto existente','copy':'Copiar comando','copied':'Comando copiado','copyfail':'Selecione o comando e copie manualmente.','library':'Biblioteca interativa · PT','git':'Abrir no GitHub','phase':'DO BRIEFING À PRÓXIMA ENTREGA','stages':[('Direção','Produto, escopo e experiência'),('Base','Arquitetura, serviços e ambiente'),('Construção','Incrementos e colaboração'),('Evidência','Testes, revisão e recuperação')],'note':'Um mapa do método. Não é um painel de execução.','tags':['Codex principal','Operação privada','Contexto sob demanda'],'jump':'Explore o método','search':'Buscar um prompt','searchhint':'Ex.: segurança, briefing, vídeo','count':'procedimentos','footer':'Defina com intenção. Construa com contexto. Evolua com evidência.','top':'Voltar ao topo','rights':'Direitos e atribuições','toc':['A história','Por onde começar','Produto e design','Serviços e APIs','Agentes','Continuidade','Conhecimento','Segurança e hooks','Backup','Economia','29 prompts','Global e local','Evidências e limites','Evolução']},
 'en':{'skip':'Skip to content','menu':'Open navigation','nav':'Explore the method','language':'Presentation language','label':'AI-ASSISTED PRODUCT ENGINEERING','lead':'A business vision. A verifiable path.','primary':'Start a product','secondary':'Organize an existing project','copy':'Copy command','copied':'Command copied','copyfail':'Select the command and copy it manually.','library':'Interactive library · PT','git':'Open on GitHub','phase':'FROM THE BRIEF TO THE NEXT DELIVERY','stages':[('Direction','Product, scope and experience'),('Foundation','Architecture, services and environment'),('Building','Increments and collaboration'),('Evidence','Tests, review and recovery')],'note':'A map of the method. Not an execution dashboard.','tags':['Codex leads','Private operations','Context on demand'],'jump':'Explore the method','search':'Find a prompt','searchhint':'E.g. security, brief, video','count':'procedures','footer':'Define with intent. Build with context. Evolve with evidence.','top':'Back to top','rights':'Rights and attribution','toc':['The story','Where to begin','Product and design','Services and APIs','Agents','Continuity','Knowledge','Security and hooks','Backup','Efficiency','29 prompts','Global and local','Evidence and limits','Evolution']},
 'es':{'skip':'Ir al contenido','menu':'Abrir navegación','nav':'Explorar el método','language':'Idioma de la presentación','label':'INGENIERÍA DE PRODUCTO CON IA','lead':'Una visión de negocio. Un camino verificable.','primary':'Iniciar un producto','secondary':'Organizar un proyecto existente','copy':'Copiar comando','copied':'Comando copiado','copyfail':'Selecciona el comando y cópialo manualmente.','library':'Biblioteca interactiva · PT','git':'Abrir en GitHub','phase':'DEL BRIEFING A LA SIGUIENTE ENTREGA','stages':[('Dirección','Producto, alcance y experiencia'),('Base','Arquitectura, servicios y entorno'),('Construcción','Incrementos y colaboración'),('Evidencia','Pruebas, revisión y recuperación')],'note':'Un mapa del método. No es un panel de ejecución.','tags':['Codex como principal','Operación privada','Contexto bajo demanda'],'jump':'Explorar el método','search':'Buscar un prompt','searchhint':'Ej.: seguridad, briefing, vídeo','count':'procedimientos','footer':'Define con intención. Construye con contexto. Evoluciona con evidencia.','top':'Volver al inicio','rights':'Derechos y atribuciones','toc':['La historia','Por dónde empezar','Producto y diseño','Servicios y API','Agentes','Continuidad','Conocimiento','Seguridad y hooks','Backup','Economía','29 prompts','Global y local','Evidencias y límites','Evolución']}}
IDS=['historia','comecar','metodo','integracoes','agentes','continuidade','documentos','auditoria','backup','economia','prompts','capacidades','operacao','evolucao']
def esc(s):return html.escape(str(s),quote=True)
def link_for(url,src,prefix):
 u=urlsplit(url)
 if u.scheme or u.netloc or url.startswith('#'):return url
 path=posixpath.normpath(posixpath.join(posixpath.dirname(src),u.path))
 if path.startswith('../'):raise ValueError('Link outside repository')
 m=re.fullmatch(r'p/(P\d\d)\.md',path)
 if m:return prefix+'prompts/'+m[1]+'/'
 pages={'politicas/CONTINUIDADE.md':'continuidade','politicas/SEGURANCA_ENGENHARIA.md':'seguranca','politicas/BACKUP_DRIVE.md':'backup','politicas/ECONOMIA_ASTRA.md':'economia','OPERACAO.md':'operacao','modulos/seguranca/README.md':'auditoria'}
 if path=='fabrica/README.md':return prefix+'fabrica/'
 if path in pages:return prefix+'guia/'+pages[path]+'/'
 return GITHUB+path+('#'+u.fragment if u.fragment else '')
def render_md(source,src,prefix):
 md=MarkdownIt('commonmark',{'html':False}).enable('table')
 tokens=md.parse(source)
 def rewrite(tokens):
  for token in tokens:
   if token.type=='link_open':token.attrSet('href',link_for(token.attrGet('href'),src,prefix))
   if token.children:rewrite(token.children)
 rewrite(tokens)
 text=md.renderer.render(tokens,md.options,{})
 return text.replace('<table>','<div class="table-scroll" tabindex="0"><table>').replace('</table>','</table></div>')
def build(lang):
 src,dest,route=LANGS[lang];t=TEXT[lang];prefix='' if lang=='pt-BR' else '../'
 source=(R/src).read_text(encoding='utf-8');digest=hashlib.sha256(source.encode()).hexdigest()
 pieces=re.split(r'<!-- section:([a-z]+) -->\n',source);intro=pieces[0]
 headline=re.search(r'^\*\*(.+)\*\*$',intro,re.M)[1]
 paras=[s.strip() for s in intro.split('\n\n')]
 headline_parts=headline.split('. ',1)
 h1=esc(headline_parts[0]+'.')+'<br><em>'+esc(headline_parts[1])+'</em>'
 lead=paras[3];support=paras[4];note=next(s[2:] for s in paras if s.startswith('> '))
 sections=[]
 for key,chunk in zip(pieces[1::2],pieces[2::2]):
  match=re.match(r'\s*## (\d+) / (.+)\n',chunk);num,title=match.groups();body=render_md(chunk[match.end():],src,prefix)
  if key=='comecar':
   serial=[0]
   def wrap(m):
    serial[0]+=1;cid=f'entry-{serial[0]}'
    return f'<div class="command"><div class="command-bar"><span>READ / {serial[0]:02d}</span><button type="button" data-copy-target="{cid}">{esc(t["copy"])}</button></div><pre id="{cid}"><code>{m[1]}</code></pre></div>'
   body=re.sub(r'<pre><code class="language-text">([\s\S]*?)</code></pre>',wrap,body)
  if key=='prompts':
   body='<label class="prompt-search">'+esc(t['search'])+f'<input id="prompt-search" type="search" placeholder="{esc(t["searchhint"])}" aria-controls="prompt-library"></label><p id="prompt-count" class="small" aria-live="polite">29 {esc(t["count"])}</p><div id="prompt-library">'+body+'</div>'
  sections.append(f'<section class="chapter" id="{key}"><div class="chapter-title"><span class="chapter-number">{num}</span><h2>{esc(title)}</h2></div><div class="chapter-body">{body}</div></section>')
 def languages():
  items=[]
  for l,label in [('pt-BR','Português (Brasil)'),('en','English'),('es','Español')]:
   href=prefix+LANGS[l][2]+'index.html'
   items.append(f'<a lang="{l}" hreflang="{l}" href="{href}"'+(' aria-current="page"' if l==lang else '')+'>'+label+'</a>')
  return f'<nav class="languages" aria-label="{esc(t["language"])}">'+''.join(items)+'</nav>'
 toc=''.join(f'<a href="#{key}"><span>{n:02d}</span>{esc(label)}</a>' for n,(key,label) in enumerate(zip(IDS,t['toc'])))
 stages=''.join(f'<li><span class="stage-number">{n:02d}</span><div><strong>{esc(label)}</strong><small>{esc(desc)}</small></div></li>' for n,(label,desc) in enumerate(t['stages'],1))
 alternates=''.join(f'<link rel="alternate" hreflang="{l}" href="{BASE+LANGS[l][2]}">' for l in LANGS)+f'<link rel="alternate" hreflang="x-default" href="{BASE}">'
 page=f'''<!doctype html>
<html lang="{lang}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="theme-color" content="#101915"><meta name="description" content="{esc(lead)}"><meta property="og:title" content="{esc(headline)} | Engenharia Cadu"><meta property="og:description" content="{esc(lead)}"><meta property="og:type" content="website"><meta property="og:url" content="{BASE+route}"><meta http-equiv="Content-Security-Policy" content="default-src 'self'; script-src 'self'; style-src 'self'; img-src 'self' data:; font-src 'self'; connect-src 'self'; object-src 'none'; base-uri 'self'; form-action 'none'"><meta name="referrer" content="strict-origin-when-cross-origin"><title>{esc(headline)} | Engenharia Cadu</title><link rel="canonical" href="{BASE+route}">{alternates}<link rel="icon" href="{prefix}assets/favicon.svg" type="image/svg+xml"><link rel="stylesheet" href="{prefix}assets/story.css"><script defer src="{prefix}assets/story.js"></script></head>
<body id="top" data-editorial="trilingual" data-copied="{esc(t['copied'])}" data-copy-error="{esc(t['copyfail'])}" data-count-label="{esc(t['count'])}"><a class="skip" href="#main">{esc(t['skip'])}</a><aside class="rail" id="rail"><a class="brand" href="#top"><span class="brand-mark" aria-hidden="true">EC</span><span>Engenharia<br><strong>Cadu<span>.</span></strong></span></a><p class="rail-label">{esc(t['nav'])}</p><nav class="toc" aria-label="{esc(t['nav'])}">{toc}</nav><div class="rail-bottom"><a href="{prefix}biblioteca.html">{esc(t['library'])} ↗</a><span class="live-dot"></span> {esc(t['lead'])}<a href="https://github.com/carlosemox/engenharia-cadu">{esc(t['git'])} ↗</a></div></aside>
<div class="workspace"><header class="topbar"><button class="menu" type="button" aria-label="{esc(t['menu'])}" aria-controls="rail" aria-expanded="false">☰</button><span class="top-label">ENGENHARIA CADU / 2026</span>{languages()}</header><main id="main" data-source="{src}" data-source-sha256="{digest}"><section class="hero"><div class="hero-copy"><span class="eyebrow"><i></i>{esc(t['label'])}</span><h1>{h1}</h1><p class="hero-lead">{esc(lead)}</p><div class="hero-actions"><a class="button primary" href="#comecar">{esc(t['primary'])} ↗</a><a class="button secondary" href="https://github.com/carlosemox/engenharia-cadu-adocao">{esc(t['secondary'])} ↗</a></div><div class="tags">{''.join('<span>'+esc(s)+'</span>' for s in t['tags'])}</div></div><aside class="method-card" aria-label="{esc(t['phase'])}"><span class="eyebrow">{esc(t['phase'])}</span><ol>{stages}</ol><p>{esc(t['note'])}</p></aside></section><div class="intro-strip"><p>{esc(support)}</p><span class="signature">Cadu Amaral<br><small>Engenharia Cadu</small></span></div><div class="language-note"><strong>PT · EN · ES</strong><p>{esc(note)}</p></div>{''.join(sections)}</main><footer><a class="footer-brand" href="#top">Engenharia Cadu<span>.</span></a><p>{esc(t['footer'])}</p><div><a href="{GITHUB+'LICENCIAMENTO.md'}">{esc(t['rights'])}</a><a href="#top">{esc(t['top'])} ↑</a></div>{languages()}</footer></div><div id="toast" role="status" aria-live="polite"></div></body></html>'''
 out=R/dest;out.parent.mkdir(parents=True,exist_ok=True);out.write_text(page,encoding='utf-8')
 return dest
if __name__=='__main__':
 for language in LANGS:print(build(language))
