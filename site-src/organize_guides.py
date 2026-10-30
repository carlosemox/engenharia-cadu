#!/usr/bin/env python3
"""Render public editorial guides; no model calls, credentials or deployment.

Run with the pinned editorial dependency in requirements.txt. Source policies
remain canonical. Does not change workflows or operate on application projects.
"""
from pathlib import Path
import hashlib,html,re,json,posixpath
from urllib.parse import urlsplit
from markdown_it import MarkdownIt
R=Path(__file__).resolve().parents[1]
G='https://github.com/carlosemox/engenharia-cadu/blob/main/'
BASE='https://carlosemox.github.io/engenharia-cadu/'
SPECS=[
 ('auditoria','modulos/seguranca/README.md','Segurança do primeiro passo ao release.','Três marcos, verificações durante o trabalho e evidências antes de avançar.'),
 ('continuidade','politicas/CONTINUIDADE.md','Um início. Próximos passos claros.','O Codex conduz as etapas autorizadas, com decisões e limites preservados.'),
 ('seguranca','politicas/SEGURANCA_ENGENHARIA.md','Segurança em cada etapa.','Revisão, casos negados e evidências antes de publicar. Sem promessa de invulnerabilidade.'),
 ('backup','politicas/BACKUP_DRIVE.md','Seu trabalho precisa de recuperação.','Arquivos, histórico e dados: cobertura explícita, cópias privadas e restauração comprovada.'),
 ('operacao','OPERACAO.md','Publicado não significa implantado.','Um mapa transparente do método, das capacidades e das condições de execução.'),
 ('contrato','politicas/CONTRATO_COMUM.md','Contrato comum','Escopo, preservação, autoridade e evidências para os procedimentos.')]
md=MarkdownIt('commonmark',{'html':False}).enable('table')
START='Read https://raw.githubusercontent.com/carlosemox/engenharia-cadu/main/p/P01.md\n\nInicie meu produto em CONTINUO_SUPERVISIONADO. Avance para a próxima etapa autorizada após verificar entrega, segurança, backup pertinente e checkpoint. Mantenha decisões materiais comigo.'
def e(s):return html.escape(s,quote=True)
def write(path,text):
 p=R/path;p.parent.mkdir(parents=True,exist_ok=True);p.write_text(text,encoding='utf-8')
def nav(prefix):
 return ''.join(f'<a data-ops-nav="{slug}" href="{prefix}guia/{slug}/"><span aria-hidden="true">{symbol}</span>{label}</a>' for slug,symbol,label in [('continuidade','→','Fluxo contínuo'),('seguranca','◇','Segurança e revisão'),('backup','▤','Backup por projeto'),('operacao','◉','Implantação e limites')])
# The standard prompt shell supplies the same navigation, CSP and local assets.
standard=(R/'docs/prompts/P02/index.html').read_text()
prefix=standard.split('<main id="main">',1)[0]
suffix=standard.split('</main>',1)[1]
def shell(title,body):
 head=re.sub(r'<title>.*?</title>',f'<title>{e(title)} | Engenharia Cadu</title>',prefix,count=1)
 head=re.sub(r'<link rel="canonical" href="[^"]*">','',head)
 if 'data-ops-nav=' not in head:head=head.replace('</nav>',nav('../../')+'</nav>',1)
 head=head.replace('v2.1.0','v2.2.1')
 return head+'<main id="main">'+body+'</main>'+suffix

def render_source(src):
 text=(R/src).read_text();text=re.sub(r'^# [^\n]+\n','',text,count=1)
 def link(m):
  url=m.group(1);u=urlsplit(url)
  if u.scheme or u.netloc or url.startswith('#'):return m.group(0)
  path=posixpath.normpath(str(Path(src).parent / u.path))
  if path.startswith('../'):raise ValueError('Unexpected source link')
  return ']('+G+path+('#'+u.fragment if u.fragment else '')+')'
 text=re.sub(r'\]\(([^\s)]+)\)',link,text)
 rendered=md.render(text)
 return rendered.replace('<table>','<div class="ops-table"><table>').replace('</table>','</table></div>')

for slug,src,title,desc in SPECS:
 digest=hashlib.sha256((R/src).read_bytes()).hexdigest()
 intro=f'<section class="prompt-header"><a class="back-link" href="../../index.html#operacao">← Central do método</a><span class="eyebrow">GUIA / {e(slug.upper())}</span><h1>{e(title)}</h1><p>{e(desc)}</p><div class="ops-pills"><span>Fonte canônica versionada</span><span>Aplicação por projeto</span></div></section>'
 command=''
 if slug=='continuidade':command=f'<section class="shortcut-box"><div class="shortcut-heading"><h2>Comece no P01</h2><button class="copy-button" data-copy-target="start-command">Copiar comando</button></div><pre id="start-command">{e(START)}</pre><p>Cole na conversa do agente, não no shell. A entrevista permanece interativa.</p></section>'
 body=intro+command+f'<article class="prose" data-source="{src}" data-source-sha256="{digest}">'+render_source(src)+f'<p><a href="{G+src}">Ler fonte no GitHub ↗</a></p></article>'
 write(f'docs/guia/{slug}/index.html',shell(title,body))
# Restore the complete P01 presentation, keeping its canonical prompt unchanged.
p01=(R/'p/P01.md').read_text();command=re.search(r'## Comando completo\n```text\n([\s\S]*?)\n```',p01).group(1).strip()+'\n'
body=f'''<section class="prompt-header"><a class="back-link" href="../../index.html#comecar">← Central da engenharia</a><span class="eyebrow">P01 / PRODUTO E CONTINUIDADE</span><h1>Comece pelo produto.<br>Continue com controle.</h1><p>Entrevista, contexto e direção de design. Depois, a próxima etapa autorizada — sem copiar um novo prompt a cada passagem.</p></section><section class="shortcut-box"><div class="shortcut-heading"><h2>Comando de entrada</h2><button class="copy-button" data-copy-target="start-command">Copiar entrada</button></div><pre id="start-command">{e(START)}</pre><p>Cole na conversa do Codex aberto no projeto. Uma fase isolada continua isolada.</p></section><div class="ops-grid"><a class="ops-card" href="../../guia/continuidade/"><small>SEQUÊNCIA</small><h2>Avançar com autorização</h2><p>Conheça a rota e os motivos de parada.</p></a><a class="ops-card" href="../../guia/seguranca/"><small>PROTEÇÃO</small><h2>Revisar para prosseguir</h2><p>Verificação durante o desenvolvimento.</p></a><a class="ops-card" href="../../guia/backup/"><small>RECUPERAÇÃO</small><h2>Backup por projeto</h2><p>Destino privado, integridade e cobertura.</p></a></div><section class="prompt-instructions"><h2>Antes de executar</h2><p>Conversa e documentação não autorizam gastos, migrações ou produção. As conexões do terminal e o supervisor de 24 horas precisam existir e ser testados separadamente. Leia <a href="../../guia/operacao/">implantação e limites</a>.</p></section><section class="command-panel"><div class="command-heading"><h2>Procedimento completo</h2><div class="command-actions"><button class="copy-button" data-copy-target="full-command">Copiar procedimento completo</button><a class="text-link" href="../../comandos/P01.txt" download>Baixar .txt</a></div></div><pre id="full-command">{e(command)}</pre></section><section class="prev-next"><a href="../P00/">← P00 · Escolher a trilha</a><a href="../P02/">P02 · Pesquisa quando necessária →</a></section>'''
write('docs/prompts/P01/index.html',shell('P01 — Começar e continuar',body))
# Idempotent organization block in the home; all basic access works without JS.
p=R/'docs/index.html';s=p.read_text()
s=re.sub(r'<!-- CADU-OPS-START -->[\s\S]*?<!-- CADU-OPS-END -->','',s)
block='''<!-- CADU-OPS-START --><section id="operacao" class="section ops-section"><div class="section-heading"><div><span class="eyebrow">CONTINUIDADE + SEGURANÇA + RECUPERAÇÃO</span><h2>Comece uma vez.<br>Avance com critério.</h2><p>A próxima etapa já tem um caminho. Decisões importantes continuam com você.</p></div><a class="text-link" href="guia/operacao/">Ver implantação e limites ↗</a></div><div class="ops-grid"><a class="ops-card" href="guia/continuidade/"><small>01 / CONTINUIDADE</small><h3>Do P01 à próxima entrega</h3><p>Etapa aceita, próxima ação autorizada. Sem colar todos os comandos.</p><span>Entender o fluxo →</span></a><a class="ops-card" href="guia/seguranca/"><small>02 / SEGURANÇA</small><h3>Revisar antes de avançar</h3><p>Controles no produto, no código e antes da publicação.</p><span>Conferir a política →</span></a><a class="ops-card" href="guia/backup/"><small>03 / BACKUP</small><h3>Preservar por projeto</h3><p>Projetos 2026 / Backup / nome do projeto, com cobertura e recibo.</p><span>Organizar a recuperação →</span></a></div><div class="notice"><strong>Método publicado não é automação instalada.</strong> Conexão Drive, auditoria dos aplicativos e supervisor de 24 horas exigem implantação e testes próprios. Nenhuma garantia de invulnerabilidade.</div></section><!-- CADU-OPS-END -->'''
s=s.replace('<section id="comecar"',block+'<section id="comecar"',1)
if 'data-ops-nav=' not in s:s=s.replace('</nav>',nav('')+'</nav>',1)
s=s.replace('Método público · v2.1.0','Método público · v2.2.1')
s=re.sub(r'<section class="quick-command">[\s\S]*?</section>',f'<section class="quick-command"><div><span class="eyebrow">PROJETO NOVO / CONTINUIDADE SUPERVISIONADA</span><h2>Um comando de entrada.<br>Etapas conectadas.</h2><p>Cole na conversa do Codex e descreva seu produto. O coordenador preserva suas decisões e carrega somente o próximo procedimento necessário.</p></div><div class="terminal"><div class="terminal-bar"><span class="terminal-dots">● ● ●</span><span>P01 · READ</span><button class="copy-button" data-copy-target="home-start-command">Copiar</button></div><pre id="home-start-command" class="ops-command">{e(START)}</pre><small>Sem avanço sobre falhas, gastos ou produção não autorizizados.</small></div></section>',s,count=1).replace('não autorizizados','não autorizados')
# Only the P01 shortcut changes; the other buttons remain isolated entry points.
s=re.sub(r'(data-copy=")[^"]*P01\.md[^"]*(" aria-label="Copiar atalho P01")',lambda m:m.group(1)+e(START)+m.group(2),s,count=1)
s=s.replace('<h2>Um comando. Uma etapa.</h2>','<h2>Cada etapa sabe o seu papel.</h2>')
s=s.replace('Da ideia ao briefing, com uma pergunta por vez.','Comece no P01. Avance pelas etapas autorizadas, com uma pergunta por vez.')
# Add an adoption card as a prominent but distinct route, preserving diagnosis.
if 'ops-adoption' not in s:
 s=s.replace('</div></section><section class="quick-command">','</div><p class="notice ops-adoption">Já existe um aplicativo e você quer reorganizá-lo por completo? <a href="https://carlosemox.github.io/engenharia-cadu-adocao/">Abra a trilha de adoção</a>: retrato do projeto, plano revisável e aplicação por lotes.</p></section><section class="quick-command">',1)
p.write_text(s)
# Global progressive navigation on legacy pages. Links on the home/guides are static.
p=R/'docs/assets/site.js';s=p.read_text()
if '// CADU organization navigation' not in s:
 enhancement='''  // CADU organization navigation; creates links only, never runs a prompt.
  const scriptUrl = document.currentScript ? document.currentScript.src : null;
  const guideNav = document.querySelector('.sidebar nav');
  if (scriptUrl && guideNav && !guideNav.querySelector('[data-ops-nav]')) {
    [['continuidade', 'Fluxo contínuo'], ['seguranca', 'Segurança e revisão'], ['backup', 'Backup por projeto'], ['operacao', 'Implantação e limites']].forEach(([slug, label]) => {
      const link = document.createElement('a');
      link.href = new URL('../guia/' + slug + '/', scriptUrl).href;
      link.dataset.opsNav = slug; link.textContent = label; guideNav.appendChild(link);
    });
  }
'''
 s=s.replace("  const menu = $('.menu-toggle'), sidebar = $('#sidebar');",enhancement+"  const menu = $('.menu-toggle'), sidebar = $('#sidebar');")
 p.write_text(s)
p=R/'docs/assets/site.css';s=p.read_text()
if '/* CADU organization */' not in s:
 s+='''\n/* CADU organization */
.sidebar{overflow-y:auto}.ops-grid{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:18px;margin:24px 0}.ops-card{display:block;border:1px solid var(--line);border-radius:14px;padding:26px;text-decoration:none;color:inherit;background:rgba(126,229,168,.025)}.ops-card small{font-size:10px;letter-spacing:1.3px;color:#a2e8bc}.ops-card h2,.ops-card h3{font-size:22px;line-height:1.3;margin:18px 0 12px}.ops-card p{font-size:13px;line-height:1.8;color:#b2c3b9}.ops-card>span{display:block;font-size:12px;margin-top:22px;color:#a2e8bc}.ops-card:hover{border-color:#6a9a7c}.ops-pills{display:flex;flex-wrap:wrap;gap:10px;margin-top:20px}.ops-pills span{font-size:10px;border:1px solid var(--line);border-radius:20px;padding:6px 12px;color:#b2c3b9}.ops-command{padding:24px;white-space:pre-wrap;overflow-wrap:anywhere;font:12px/1.9 ui-monospace,monospace;color:#e0eee5;margin:0}.ops-table{overflow-x:auto;max-width:100%;margin:20px 0}.ops-table table{min-width:580px}.prose pre{overflow-wrap:anywhere;white-space:pre-wrap}.prose code{overflow-wrap:anywhere}.prose{padding-bottom:32px}.ops-section{scroll-margin-top:65px}.notice a{color:#a2e8bc;text-decoration:underline}.sidebar nav [data-ops-nav]{font-size:11px}.sidebar nav [data-ops-nav="continuidade"]{border-top:1px solid var(--line);margin-top:10px;padding-top:16px}
@media(max-width:980px){.ops-grid{grid-template-columns:1fr}.ops-card{padding:22px}.ops-card h2,.ops-card h3{font-size:22px}.sidebar nav [data-ops-nav]{font-size:10px}}
@media(max-width:720px){.ops-command{padding:18px;font-size:11px}.sidebar nav [data-ops-nav]{font-size:12px}.ops-table table{min-width:540px}}
'''
 p.write_text(s)
# Index the new guides and preserve all prior sitemap entries.
p=R/'docs/sitemap.xml';s=p.read_text()
for slug,_,_,_ in SPECS:
 url=BASE+f'guia/{slug}/'
 if url not in s:s=s.replace('</urlset>',f'<url><loc>{url}</loc></url>\n</urlset>')
p.write_text(s)
print('Rendered guides and organized home/P01; no workflows or runtime configuration changed.')

# CADU S01 public navigation: links only; no runtime or scans are activated.
p=R/'docs/index.html';text=p.read_text()
text=re.sub(r'<!-- CADU-SECURITY-START -->[\s\S]*?<!-- CADU-SECURITY-END -->','',text)
block='''<!-- CADU-SECURITY-START --><section id="auditoria" class="section ops-section"><div class="section-heading"><div><span class="eyebrow">S01 / SEGURANÇA POR ETAPAS</span><h2>No início. Durante.<br>Antes de publicar.</h2><p>Revisão de desenho, verificação por lote e controle do candidato final. O problema descoberto vira correção delimitada e reteste, não uma aprovação automática.</p></div><a class="text-link" href="guia/auditoria/">Abrir auditoria e hooks →</a></div><div class="ops-grid"><a class="ops-card" href="guia/auditoria/"><small>01 / INÍCIO</small><h3>Desenhar a proteção</h3><p>Dados, ameaças, perfis e controles antes da implementação.</p></a><a class="ops-card" href="guia/auditoria/"><small>02 / DURANTE E MEIO</small><h3>Revisar cada incremento</h3><p>Checks de alteração, interfaces compartilhadas e revisão por risco.</p></a><a class="ops-card" href="guia/auditoria/"><small>03 / PRÉ-RELEASE</small><h3>Verificar antes do GO</h3><p>Candidato identificado, achados, testes, revisão e recuperação.</p></a></div><div class="notice">Módulo de procedimentos e exemplos de hooks. Não significa auditoria realizada ou controles instalados nos aplicativos. Sem promessa de invulnerabilidade.</div></section><!-- CADU-SECURITY-END -->'''
anchor='<section id="comecar"'
if anchor not in text:raise ValueError('Home anchor absent')
text=text.replace(anchor,block+anchor,1)
p.write_text(text,encoding='utf-8')
