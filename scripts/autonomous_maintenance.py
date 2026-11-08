#!/usr/bin/env python3
"""Run a finite allowlisted maintenance loop. Never executes task-supplied commands.

This is deterministic automation, not an LLM adapter. GitHub schedules the runs;
artifacts retain receipts. No commits, external mutations, paid API or background
processes. Tests may regenerate derived files inside the disposable checkout;
no Git commit or push is performed. Only run reviewed trusted code: tests/validators
are repository code.
"""
import argparse
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import time

ROOT = Path(__file__).resolve().parents[1]
ACTIONS = {
    'project_audit': [sys.executable, str(ROOT/'scripts/audit_project.py'), '--project', str(ROOT)],
    'editorial_check': [sys.executable, str(ROOT/'scripts/validate.py')],
    'queue_check': [sys.executable, str(ROOT/'scripts/supervisor.py'), '--check'],
    'regression_tests': [sys.executable, '-m', 'unittest', 'discover', '-s', str(ROOT/'tests')],
}


def validate(config):
    if not isinstance(config, dict) or config.get('version') != 1 or type(config.get('enabled')) is not bool:
        raise ValueError('invalid configuration')
    if type(config.get('max_tasks')) is not int or not 1 <= config['max_tasks'] <= 10:
        raise ValueError('invalid task budget')
    if type(config.get('timeout_seconds')) is not int or not 1 <= config['timeout_seconds'] <= 600:
        raise ValueError('invalid deadline')
    tasks = config.get('tasks')
    if not isinstance(tasks, list) or len(tasks) > config['max_tasks']:
        raise ValueError('task budget exceeded')
    ids = set()
    for task in tasks:
        if not isinstance(task, dict) or set(task) != {'id', 'action', 'depends_on'}:
            raise ValueError('invalid task fields')
        if not isinstance(task['id'], str) or not task['id'] or task['id'] in ids:
            raise ValueError('invalid or duplicate task ID')
        if not isinstance(task['action'], str) or task['action'] not in ACTIONS:
            raise ValueError('unapproved action')
        if not isinstance(task['depends_on'], list) or any(not isinstance(d, str) for d in task['depends_on']):
            raise ValueError('invalid dependency')
        ids.add(task['id'])
    remaining = {t['id']:set(t['depends_on']) for t in tasks}
    if any(not deps <= ids for deps in remaining.values()):
        raise ValueError('unknown dependency')
    while remaining:
        ready={k for k,v in remaining.items() if not v}
        if not ready:raise ValueError('dependency cycle')
        remaining={k:v-ready for k,v in remaining.items() if k not in ready}


def run(config, runner=subprocess.run, clock=time.monotonic, stop=lambda:False):
    validate(config)
    started=clock();results={};events=[]
    if not config['enabled'] or stop():
        return {'status':'STOPPED','tasks':[],'events':[],'llm':'NOT_STARTED'}
    pending=list(config['tasks'])
    while pending:
        progress=False
        for task in pending[:]:
            if clock()-started >= config['timeout_seconds']:
                return {'status':'FAIL','reason':'DEADLINE_EXHAUSTED','tasks':list(results.values()),'events':events,'llm':'NOT_STARTED'}
            if stop():
                return {'status':'STOPPED','tasks':list(results.values()),'events':events,'llm':'NOT_STARTED'}
            deps=task['depends_on']
            if any(d not in results for d in deps):continue
            progress=True;pending.remove(task)
            record={'id':task['id'],'action':task['action'],'attempts':0}
            if any(results[d]['status']!='PASS' for d in deps):
                record.update(status='BLOCKED',reason='DEPENDENCY_FAILED')
            else:
                record['attempts']=1;events.append({'task':task['id'],'event':'STARTED'})
                try:
                    result=runner(ACTIONS[task['action']],cwd=ROOT,capture_output=True,text=True,
                                  timeout=max(0.01,config['timeout_seconds']-(clock()-started)))
                    # Do not publish stdout/stderr from tests or arbitrary repository contents.
                    out=(result.stdout or '')+(result.stderr or '')
                    record.update(status='PASS' if result.returncode==0 else 'FAIL',exit_code=result.returncode,
                                  output_sha256=hashlib.sha256(out.encode()).hexdigest())
                    if task['action']=='project_audit' and result.returncode==0:
                        try:
                            audit=json.loads(result.stdout)
                            if audit.get('schema_version') != 1:raise ValueError('schema')
                            record['audit']={k:audit[k] for k in ('coverage','artifacts','findings','proposed_tasks','runtime','limitations') if k in audit}
                        except (ValueError, AttributeError, TypeError):
                            record.update(status='FAIL',reason='INVALID_AUDIT_RECEIPT')
                except subprocess.TimeoutExpired:
                    record.update(status='FAIL',reason='TIMEOUT')
                except OSError:
                    record.update(status='FAIL',reason='EXECUTOR_UNAVAILABLE')
            results[task['id']]=record;events.append({'task':task['id'],'event':record['status']})
        if not progress:raise ValueError('no progress')
    return {'status':'PASS' if all(x['status']=='PASS' for x in results.values()) else 'FAIL',
            'tasks':list(results.values()),'events':events,'llm':'NOT_STARTED'}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',required=True,type=Path)
    args=parser.parse_args()
    output=args.output.absolute()
    if output.is_symlink() or output.parent.resolve()!=output.parent:
        raise SystemExit('unsafe receipt destination')
    if output==ROOT or ROOT in output.parents:
        raise SystemExit('receipt must be outside checkout')
    config=json.loads((ROOT/'automation/maintenance.json').read_text())
    stopped=lambda:os.environ.get('CADU_AUTONOMY_STOP','').lower()=='true'
    receipt=run(config,stop=stopped)
    receipt.update(mode='AUTONOMOUS_DETERMINISTIC_AUDIT',run_id=os.environ.get('GITHUB_RUN_ID','local'),
                   source_sha=os.environ.get('GITHUB_SHA','local'),token_usage=0,
                   meaning='PASS means checks ran successfully; project findings require their own assessment')
    output.write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(receipt,ensure_ascii=False))
    return int(receipt['status'] not in ('PASS', 'STOPPED'))

if __name__=='__main__':raise SystemExit(main())
