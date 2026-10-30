#!/usr/bin/env python3
"""Integrate documented flow into this toolkit only. No app/Drive/CLI execution.

Idempotent editorial migration; changes canonical prompts and their derivatives.
Run only in the Engenharia Cadu documentation repository after review.
"""
from pathlib import Path
import hashlib, html, json, re, subprocess, sys
R = Path(__file__).resolve().parents[1]
MARK = 'CONTINUIDADE SUPERVISIONADA — 2.2'
OLD = 'Trate este texto como procedimento da etapa solicitada, não como autorização para executar outras fases.'
NEW = ('Trate este texto como procedimento da etapa atual. Em ISOLADO, não execute outras fases. '
       'Em CONTINUO_SUPERVISIONADO, a missão pode cobrir etapas sucessivas; só avance quando '
       'o escopo seguinte já estiver autorizado e os gates atendidos, conforme politicas/CONTINUIDADE.md.')
ROUTES = {
 'version':'2.2.0', 'kind':'routing_reference_not_runtime', 'entry':'P01',
 'default_order':[f'P{i:02d}' for i in range(1,17)],
 'optional':{'P02':'Pesquisa apenas quando necessária; dispensa justificada.',
 'P07':'Pode ocorrer em paralelo se recursos/alçada independentes.',
 'P08':'Pode antecipar escolha de integração; revalidar P06 quando mudar arquitetura.'},
 'loops':{'P14':{'fix':'P13','new_scope':'P12','accepted_increment':'P15'},
          'P15':{'more_authorized_tasks':'P13','scope_complete':'P16'}},
 'on_scope_complete':None,
 'not_automatic':['P17','P18','P19','P20','P21','P22','P23','P24','P25','P26','P27','P28'],
 'required_before_transition':['acceptance_evidence','security_disposition','applicable_backup_receipt',
                               'checkpoint','next_scope_authority','resource_and_budget_limits'],
 'rules':['No permission expansion','No invented work','No self-certified approval',
          'No PASS for NOT_RUN','No unbounded retries','Release GO remains separate']}
BLOCK = '''CONTINUIDADE SUPERVISIONADA — 2.2
Preserve o modo da missão. Para iniciar um produto do zero pelo P01, use CONTINUO_SUPERVISIONADO na sessão ativa; pedido de apenas esta fase/análise permanece ISOLADO. Leia politicas/CONTINUIDADE.md, politicas/SEGURANCA_ENGENHARIA.md e politicas/BACKUP_DRIVE.md na mesma revisão, reutilizando a leitura válida e somente os detalhes pertinentes.
Quando esta etapa estiver aceita, verifique evidências, segurança, backup aplicável e limites; salve checkpoint e carregue/exe cute o próximo procedimento autorizado sem pedir que o usuário copie outro comando. Consulte orquestracao/rotas.json como mapa, não como autorização. Preserve gates de decisão, recursos, revisão independente e GO de produção. Falha ou backup obrigatório não verificado bloqueia a dependência; análise independente autorizada pode continuar. Não invente tarefa para manter atividade; P17 e especializações não são sequência obrigatória. Uma etapa concluída não encerra a missão contínua enquanto houver próximo trabalho autorizado. Sessão encerrada não continua sozinha; 24 horas exigem supervisor real e conexão Drive testada.
'''.replace('exe cute','execute')
EXTRA = {
 'P01':'NOVO PRODUTO: explique o modo contínuo uma vez, faça a entrevista normalmente e aguarde respostas materiais. Ao confirmar o entendimento, prossiga à pesquisa necessária e ao escopo sem exigir outra colagem de prompt. Não invente respostas para avançar.',
 'P04':'SEGURANÇA NO PRD: inclua autorização por objeto/tenant, dados sensíveis, abusos e testes negados pertinentes. Estabeleça cobertura ASVS proporcional, sem alegar certificação.',
 'P06':'SEGURANÇA NA ARQUITETURA: modele ativos, entradas e fronteiras; defina privilégios mínimos, isolamento, recuperação e responsabilidades. Transforme controles em testes.',
 'P13':'VERIFICAÇÃO POR ENTREGA: executar testes positivos e negativos, análise de dependências/segredos pertinente, revisão proporcional e backup dos artefatos aceitos. Não usar credencial administrativa como única prova de autorização.',
 'P14':'GATE DE SEGURANÇA: revisar a mesma versão em execução independente quando exigido; achado crítico/alto não resolvido ou não investigado impede parecer favorável para release. Não alterar código ou critério para autoaprovar.',
 'P15':'TESTE FINAL: conferir jornadas, acesso entre usuários/tenants e configuração de staging. Testes dinâmicos somente em alvos/intensidade autorizados. Novo commit invalida provas afetadas.',
 'P16':'GATE FINAL OBRIGATÓRIO: revisão de segurança da mesma versão; sem segredo exposto ou achado crítico/alto confirmado sem correção e reteste. Hipótese relevante pendente exige investigação/disposição antes de liberar. Exigir backup verificado e recuperação pertinente, configuração revisada e GO específico. Zero achados não garante ausência de invasões. Preparar manutenção e resposta a incidentes.',
 'P17':'BACKUP NA MISSÃO: cada host precisa de conector Drive autenticado e testado, com destino privado e recibos. As conexões do chat não se transferem automaticamente ao CLI. Antes de efeitos de risco, proteção prévia obrigatória.',
 'P18':'RETOMADA: confira checkpoint, último backup e snapshot; nunca repetir efeito externo incerto. Após reconciliar, retome a etapa pendente do modo contínuo, sem reiniciar P01.'}

def write(p, text):
 q=R/p;q.parent.mkdir(parents=True,exist_ok=True);q.write_text(text.rstrip()+'\n',encoding='utf-8')
def append_once(path, marker, text):
 q=R/path;t=q.read_text(encoding='utf-8')
 if marker not in t:write(path,t+'\n'+text)
def guide(policy, slug, title):
 source=R/policy
 shell=(R/'docs/guia/contrato/index.html').read_text(encoding='utf-8')
 parts=[]
 for block in source.read_text(encoding='utf-8').strip().split('\n\n'):
  if block.startswith('# '):continue
  if block.startswith('## '):parts.append('<h2>'+html.escape(block[3:])+'</h2>')
  else:parts.append('<p>'+html.escape(block).replace('\n','<br>')+'</p>')
 url='https://github.com/carlosemox/engenharia-cadu/blob/main/'+policy
 main='<main id="main"><section class="prompt-header"><a class="back-link" href="../../index.html">← Central da engenharia</a><span class="eyebrow">CONTINUIDADE · SEGURANÇA · RECUPERAÇÃO</span><h1>'+title+'</h1></section><article class="prose">'+''.join(parts)+'<p><a href="'+url+'">Abrir documento canônico</a></p></article></main>'
 shell=re.sub(r'<main id="main">[\s\S]*?</main>',lambda _:main,shell,count=1)
 shell=re.sub(r'<title>.*?</title>','<title>'+title+' — Engenharia Cadu</title>',shell,count=1)
 shell=re.sub(r'<link rel="canonical"[^>]*>','<link rel="canonical" href="https://carlosemox.github.io/engenharia-cadu/guia/'+slug+'/">',shell)
 write('docs/guia/'+slug+'/index.html',shell)

def main():
 paths=sorted((R/'p').glob('P[0-9][0-9].md'))
 if len(paths)!=29 or 'Engenharia Cadu' not in (R/'README.md').read_text():raise ValueError('Wrong toolkit root')
 for n in ['CONTINUIDADE.md','SEGURANCA_ENGENHARIA.md','BACKUP_DRIVE.md']:
  if not (R/'politicas'/n).is_file():raise ValueError('Missing policy: '+n)
 for p in paths:
  t=p.read_text(encoding='utf-8').replace(OLD,NEW).replace('**Edição de publicação:** 2.1.0','**Edição de publicação:** 2.2.0')
  if MARK not in t:
   t=t.replace('ENCERRAMENTO DA ETAPA\n',BLOCK+'\n'+EXTRA.get(p.stem,'')+'\n\nENCERRAMENTO DA ETAPA\n',1)
   if MARK not in t:raise ValueError('Missing command marker: '+p.name)
  write(str(p.relative_to(R)),t)
 common=(R/'politicas/CONTRATO_COMUM.md').read_text().replace(OLD,NEW)
 if MARK not in common:common+='\n## Transição ao concluir\n'+BLOCK
 write('politicas/CONTRATO_COMUM.md',common)
 append_once('AGENTS.md','CONTINUO_SUPERVISIONADO','''\n## Continuidade, segurança e backup
- Iniciar produto pelo P01 usa CONTINUO_SUPERVISIONADO; fase isolada continua isolada.
- Aplicar politicas/CONTINUIDADE.md, politicas/SEGURANCA_ENGENHARIA.md e politicas/BACKUP_DRIVE.md. Ler uma vez por revisão e detalhes por necessidade.
- Encerrar a fase aceita com checkpoint/recibo, conferir alçada e avançar; não encerrar a missão por hábito. Entrevista, decisões materiais e GO continuam humanos.
- Fluxo em orquestracao/rotas.json é referência, não runtime. Sem supervisor não há continuidade fora da sessão.
''')
 append_once('read.md','politicas/CONTINUIDADE.md','''\n## Avanço entre etapas
Para novo produto via P01, aplicar [Continuidade](politicas/CONTINUIDADE.md), [Segurança](politicas/SEGURANCA_ENGENHARIA.md) e [Backup](politicas/BACKUP_DRIVE.md), respeitando decisões e permissões. O próximo procedimento é carregado na sessão ativa após aceite/evidências e sem nova colagem. Para usar o atalho completo, leia [continuar.md](continuar.md). Pedido de fase isolada não vira missão integral.
''')
 append_once('README.md','## Continuidade, segurança e backup','''\n## Continuidade, segurança e backup
Comece no P01 e prossiga em CONTINUO_SUPERVISIONADO na sessão ativa. Ao aceitar cada etapa, o coordenador verifica segurança, backup pertinente e autorização, salva checkpoint e lê o próximo prompt. Não é necessário copiar todos os comandos. Entrevistas, mudanças materiais e GO de produção continuam exigindo decisão.

```text
Read https://raw.githubusercontent.com/carlosemox/engenharia-cadu/main/p/P01.md
Inicie meu produto em CONTINUO_SUPERVISIONADO e avance pelas etapas autorizadas após validar cada entrega. Aplique segurança e backup privado em Projetos 2026/Backup/<nome-do-projeto>.
```

[Comando e limites](continuar.md) · [Continuidade](politicas/CONTINUIDADE.md) · [Segurança](politicas/SEGURANCA_ENGENHARIA.md) · [Backup](politicas/BACKUP_DRIVE.md)

Segurança total contra invasões não pode ser garantida. Revisão, testes, correções, recuperação e manutenção são exigidos. Os backups preservam gerações; arquivo enviado não é backup verificado. Credenciais não vão em ZIP comum. Integrações Drive e supervisor precisam de homologação no host real, não são instalados por esta publicação.
''')
 write('orquestracao/rotas.json',json.dumps(ROUTES,ensure_ascii=False,indent=2))
 write('templates/ESTADO_FLUXO.json',json.dumps({'template_only':True,'mode':'CONTINUO_SUPERVISIONADO','project':None,'method_revision':None,'stage':'P01','status':'NOT_STARTED','snapshot':None,'evidence_snapshot':None,'evidence':[],'security_blockers':[],'security_review_reference':None,'backup_required':None,'backup':{'status':'PLANNED','snapshot':None,'receipt':None,'sha256':None},'next_stage':None,'next_scope_authorized':False,'transitions_remaining':8,'required_approvals':[],'observed_approval_refs':{},'notes':'Inativo. Campos não concedem autorização nem comprovam execução. Valores ausentes não significam ilimitado.'},ensure_ascii=False,indent=2))
 append_once('templates/README.md','ESTADO_FLUXO','\n[Estado de continuidade](ESTADO_FLUXO.json) — inativo, decisões e recibos precisam de prova externa ao autorrelato.\n')
 append_once('CHANGELOG.md','## 2.2.0','\n## 2.2.0 — 30/10/2026\nContinuidade supervisionada vinculada aos 29 prompts; segurança e backup transversais; rotas, estado inativo e guias no site. Nenhum supervisor ou conector de aplicativo é instalado por esta atualização.\n')
 subprocess.run([sys.executable,str(R/'scripts/sync_prompts.py')],check=True,cwd=R)
 gh='https://github.com/carlosemox/engenharia-cadu/blob/main/'
 read=(R/'read.md').read_text();write('docs/read.md',re.sub(r'\]\(([^:)]+)\)',lambda m:']('+gh+m.group(1)+')',read))
 guide('politicas/CONTINUIDADE.md','continuidade','Um comando. Etapas conectadas.')
 guide('politicas/SEGURANCA_ENGENHARIA.md','seguranca','Segurança durante toda a construção')
 guide('politicas/BACKUP_DRIVE.md','backup','Backup privado, por projeto')
 guide('politicas/CONTRATO_COMUM.md','contrato','Contrato comum')
 index=R/'docs/index.html';t=index.read_text()
 if 'id="continuidade"' not in t:
  block='<section class="section" id="continuidade"><div class="section-heading"><div><span class="eyebrow">DA ENTREVISTA À ENTREGA</span><h2>Um comando para começar.<br>Controle em cada etapa.</h2></div></div><div class="doc-grid">'
  for slug,title,desc in [('continuidade','Etapas conectadas','P01 inicia; o coordenador continua dentro da autorização.'),('seguranca','Segurança contínua','Revisão, testes e gate final. Sem promessa de invulnerabilidade.'),('backup','Backup por projeto','Drive privado, gerações, manifesto e recuperação verificável.')]:
   block+='<a class="doc-card" href="guia/'+slug+'/"><div><h3>'+title+'</h3><p>'+desc+'</p></div><span>↗</span></a>'
  block+='</div></section>'
  t=t.replace('<section class="section" id="documentos">',block+'<section class="section" id="documentos">',1)
  t=t.replace('<a href="index.html#documentos">','<a href="index.html#continuidade">Continuidade e proteção</a><a href="index.html#documentos">',1)
 write('docs/index.html',t)
 for p in (R/'docs').rglob('*.html'):
  t=p.read_text();p.write_text(t.replace('v2.1.0','v2.2.0'),encoding='utf-8')
 manifest={}
 for p in sorted(R.rglob('*')):
  if not p.is_file() or '.git' in p.parts or '__pycache__' in p.parts or p.suffix=='.pyc' or p.name=='MANIFEST_SHA256.json':continue
  manifest[str(p.relative_to(R))]=hashlib.sha256(p.read_bytes()).hexdigest()
 write('MANIFEST_SHA256.json',json.dumps(manifest,ensure_ascii=False,indent=2))
 print(json.dumps({'version':'2.2.0','canonical_prompts':len(paths),'manifest_files':len(manifest),'scope':'toolkit_only','runtime_agents':'NOT_RUN'}))
if __name__=='__main__':main()
