#!/usr/bin/env python3
"""Read-only control plane. Does not execute agents or enforce an OS sandbox."""
import argparse
import json
import re
from pathlib import Path, PurePosixPath

ROOT = Path(__file__).resolve().parents[1]
STATES = {'READY', 'IN_PROGRESS', 'IN_REVIEW', 'BLOCKED', 'APPROVAL_REQUIRED',
          'RELEASE_CANDIDATE', 'RELEASE_BLOCKED', 'DONE', 'CANCELLED'}
ENVIRONMENTS = {'TERMINAL', 'COMPUTER_APP', 'CLOUD_CODE'}
DENIED = {'.git', '.env', 'secrets'}


def clean_path(value):
    if not isinstance(value, str) or not value or '\\' in value or ':' in value:
        raise ValueError('invalid relative path')
    p = PurePosixPath(value)
    if p.is_absolute() or any(x in {'', '.', '..'} for x in (value[:-1] if value.endswith('/') else value).split('/')):
        raise ValueError('non canonical path')
    if any(x in DENIED or x.startswith('.env.') for x in p.parts):
        raise ValueError('protected path')
    return value


def within(path, prefix):
    clean_path(path)
    clean_path(prefix)
    return path.startswith(prefix) if prefix.endswith('/') else path == prefix


def load_queue(path):
    blocks = re.findall(r'^```json\s*\n(.*?)\n```', path.read_text(), re.M | re.S)
    if len(blocks) != 1:
        raise ValueError('queue must contain exactly one JSON block')
    return json.loads(blocks[0])


def validate(queue, registry):
    """Validate declared contracts, not authenticity of reviewers or evidence."""
    errors = []
    if not isinstance(queue, dict):
        return ['queue root must be an object']
    roles = {x['id']: x for x in registry['roles']}
    squads = {x['id']: x for x in registry['squads']}
    tasks = queue.get('tasks')
    if not isinstance(tasks, list):
        return ['tasks must be a list']
    if queue.get('environment') not in ENVIRONMENTS:
        errors.append('environment undefined')
    if queue.get('max_in_progress') != 1:
        errors.append('P0 permits one task in progress')
    for flag in ('stop_requested', 'critical_block'):
        if type(queue.get(flag)) is not bool:
            errors.append(flag + ' must be boolean')
    by_id = {}
    for task in tasks:
        if not isinstance(task, dict) or not isinstance(task.get('id'), str):
            errors.append('invalid task identity')
            continue
        tid = task['id']
        if not tid or tid in by_id:
            errors.append(tid + ': duplicate/empty id')
        by_id[tid] = task
    required = ('title', 'owner', 'executor_id', 'reviewer_id', 'acceptance', 'inputs', 'outputs', 'next_action')
    for tid, task in by_id.items():
        def error(msg): errors.append(tid + ': ' + msg)
        for key in required:
            value = task.get(key)
            if key in {'inputs', 'outputs'}:
                if not isinstance(value, list) or not value or any(not isinstance(v, str) or not v.strip() for v in value):
                    error('invalid ' + key)
            elif not isinstance(value, str) or not value.strip():
                error('invalid ' + key)
        if task.get('executor_id') == task.get('reviewer_id'): error('self review')
        if task.get('status') not in STATES: error('unknown status')
        if task.get('environment') != queue.get('environment'): error('environment mismatch')
        if task.get('priority') not in ('P0', 'P1', 'P2', 'P3'): error('priority invalid')
        if type(task.get('authorized')) is not bool: error('authorization must be boolean')
        for key in ('attempts', 'no_progress', 'max_attempts'):
            if type(task.get(key)) is not int or task[key] < 0: error('invalid ' + key)
        if task.get('max_attempts') != 3: error('max_attempts must be 3')
        role = roles.get(task.get('role'))
        squad = squads.get(task.get('squad'))
        if role is None or squad is None or task.get('role') not in squad.get('roles', []):
            error('role not assigned to squad')
        paths = task.get('allowed_paths')
        if not isinstance(paths, list) or not paths: error('allowed_paths required')
        else:
            for path in paths:
                try:
                    clean_path(path)
                    if role is None or not any(within(path, prefix) for prefix in role['allowed_prefixes']):
                        error('scope exceeds role: ' + str(path))
                except (ValueError, TypeError): error('unsafe path')
        deps = task.get('depends_on')
        if not isinstance(deps, list) or any(not isinstance(x, str) for x in deps):
            error('dependencies must be identifiers')
            deps = []
        for dep in deps:
            if dep not in by_id: error('missing dependency ' + dep)
        if task.get('status') in {'READY', 'IN_PROGRESS', 'IN_REVIEW', 'DONE'}:
            for dep in deps:
                if dep in by_id and by_id[dep].get('status') != 'DONE': error('unsatisfied dependency ' + dep)
        if task.get('status') in {'READY', 'IN_PROGRESS'}:
            if task.get('authorized') is not True: error('task lacks authorization')
            if isinstance(task.get('attempts'), int) and task['attempts'] >= 3: error('retry exhausted')
            if isinstance(task.get('no_progress'), int) and task['no_progress'] >= 2: error('REPEATED_FAILURE')
        if task.get('status') == 'DONE':
            review = task.get('review') or {}
            if not isinstance(review, dict): error('review must be object'); continue
            if review.get('reviewer_id') != task.get('reviewer_id') or review.get('result') != 'PASS': error('review missing')
            if not re.fullmatch(r'[0-9a-f]{40}', str(review.get('snapshot', ''))): error('snapshot missing')
            evidence = task.get('evidence')
            if not isinstance(evidence, list) or not evidence or any(not isinstance(v, str) or not v.strip() for v in evidence):
                error('evidence missing or malformed')
    visiting, visited = set(), set()
    def visit(tid):
        if tid in visiting:
            errors.append('dependency cycle: ' + tid)
            return
        if tid in visited: return
        visiting.add(tid)
        deps = by_id[tid].get('depends_on', [])
        if isinstance(deps, list):
            for dep in deps:
                if isinstance(dep, str) and dep in by_id: visit(dep)
        visiting.remove(tid)
        visited.add(tid)
    for tid in by_id: visit(tid)
    if sum(t.get('status') == 'IN_PROGRESS' for t in by_id.values()) > 1:
        errors.append('WIP exceeded')
    return errors


def select_next(queue, registry):
    errors = validate(queue, registry)
    if errors: return {'status': 'FAIL', 'errors': errors}
    if queue['stop_requested'] or queue['critical_block']:
        return {'status': 'STOPPED', 'task': None}
    if any(t['status'] in {'IN_PROGRESS', 'IN_REVIEW'} for t in queue['tasks']):
        return {'status': 'WAITING_REVIEW_OR_WORK', 'task': None}
    tasks = sorted((t for t in queue['tasks'] if t['status'] == 'READY'), key=lambda t: (t['priority'], t['id']))
    return {'status': 'CANDIDATE' if tasks else 'IDLE', 'task': tasks[0] if tasks else None,
            'execution': 'NOT_STARTED', 'requires': 'trusted isolated executor; policy validation is not authorization proof'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--queue', type=Path, default=ROOT/'docs/harness/TASK_QUEUE.md')
    parser.add_argument('--check', action='store_true')
    parser.add_argument('--next', action='store_true')
    args = parser.parse_args()
    try:
        queue = load_queue(args.queue)
        registry = json.loads((ROOT/'catalogo/esquadroes.json').read_text())
        if args.next:
            result = select_next(queue, registry)
        else:
            errors = validate(queue, registry)
            result = {'status': 'FAIL' if errors else 'PASS', 'errors': errors, 'runtime': 'NOT_CONFIGURED'}
    except (ValueError, KeyError, TypeError, OSError, RecursionError) as exc:
        result = {'status': 'FAIL', 'errors': [str(exc)]}
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return int(result['status'] == 'FAIL')

if __name__ == '__main__':
    raise SystemExit(main())
