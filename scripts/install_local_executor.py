#!/usr/bin/env python3
"""Install reviewed local executor for one synthetic project, under user launchd.
Never opens product repositories. Refuses to overwrite any existing installation.
"""
import hashlib
import json
import os
from pathlib import Path
import plistlib
import shutil
import subprocess
import sys
import time


def main():
    if sys.platform != 'darwin':
        raise SystemExit('macOS required')
    source = Path(__file__).with_name('local_executor.py').resolve()
    sys.path.insert(0, str(source.parent))
    import local_executor as e
    model = next((m for m in e.local_request('/api/tags')['models'] if m['name'] == 'qwen3:4b'), None)
    show=e.local_request('/api/show', {'model':'qwen3:4b'}) if model else {}
    if not model or show.get('remote_host') or show.get('remote_model'):
        raise SystemExit('Existing local qwen3:4b required; no download')
    base = Path.home() / 'Library/Application Support/Engenharia-Cadu-Agent'
    label = 'com.engenharia-cadu.local-executor'
    plist = Path.home() / 'Library/LaunchAgents' / (label + '.plist')
    if base.exists() or base.is_symlink() or plist.exists() or plist.is_symlink():
        raise SystemExit('Installation already exists; reconcile before changing')
    os.umask(0o077)
    base.mkdir(parents=True, mode=0o700)
    (base/'bin').mkdir(); (base/'logs').mkdir()
    shutil.copy2(source, base/'bin/local_executor.py')
    fixture = base/'synthetic-project'; fixture.mkdir()
    (fixture/'sum.cjs').write_text('module.exports = (a,b) => a-b;\n')
    state = base/'state'; supervisor=e.Supervisor(state)
    e.atomic(state/'model.json', {'digest':model['digest'], 'projects':{'synthetic-acceptance':str(fixture)}})
    job = {'id':'installation-pilot','project':'synthetic-acceptance','root':str(fixture), 'files':['sum.cjs'],
      'instruction':'Fix addition: exported function returns a plus b. Preserve CommonJS export.',
      'checks':[['/usr/local/bin/node','-e',"const a=require('node:assert/strict'),f=require('./sum.cjs');a.equal(f(2,3),5);a.equal(f(-4,1),-3);a.equal(f(0,0),0);"]],
      'approved':True,'expires_at':time.time()+1800,'revision':1}
    e.atomic(state/'jobs/installation-pilot.json', job)
    config={'Label':label, 'ProgramArguments':[sys.executable,str(base/'bin/local_executor.py'),'serve',str(state)],
      'RunAtLoad':True, 'KeepAlive':{'SuccessfulExit':False}, 'ThrottleInterval':30, 'Nice':10,
      'WorkingDirectory':str(base), 'EnvironmentVariables':{'PATH':'/usr/bin:/bin:/usr/sbin:/sbin'},
      'StandardOutPath':str(base/'logs/stdout.log'), 'StandardErrorPath':str(base/'logs/stderr.log')}
    plist.parent.mkdir(exist_ok=True)
    with plist.open('xb') as f: plistlib.dump(config,f)
    receipt={'installed_at':time.time(),'source_sha256':hashlib.sha256((base/'bin/local_executor.py').read_bytes()).hexdigest(),
      'model_digest':model['digest'],'scope':'synthetic-only; candidate review required','label':label,'base':str(base)}
    e.atomic(base/'installation.json', receipt)
    subprocess.run(['/bin/launchctl','bootstrap','gui/'+str(os.getuid()),str(plist)],check=True)
    print(json.dumps(receipt))


if __name__=='__main__': main()
