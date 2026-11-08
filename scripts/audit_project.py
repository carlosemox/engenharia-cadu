#!/usr/bin/env python3
"""Bounded, read-only project triage. Never run target code, tests or hooks.

No processes are started. Git HEAD is read as metadata; dirty is NOT_VERIFIED.
Reports contain metadata and evidence hashes, never document excerpts or Git output.
POSIX no-follow directory descriptors protect reads and exclusive report creation.
"""
import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import stat

MAX_ENTRIES = 4000
MAX_DOCS = 160
MAX_BYTES = 65536
MAX_DEPTH = 4
SKIP = {'.git', 'node_modules', 'vendor', 'dist', 'build', '.venv', 'venv',
        '__pycache__', '.cache', 'coverage', 'secrets', 'credentials', 'backups'}
DOC_DIRS = {'docs', 'doc', 'documentation', 'harness', '.github', 'adr', 'decisions',
            'architecture', 'design', 'policies', 'politicas', 'runbooks', 'notes'}
SECRET = re.compile(r'-----BEGIN .*PRIVATE KEY|(?:gh[pousr]_|sk-proj-)[A-Za-z0-9_-]{20,}|'
                    r'AKIA[A-Z0-9]{16}|(?:password|secret|api[_-]?key|token)\s*[:=]\s*["\']?[^\s"\']{8,}', re.I)
# Name aliases and multilingual heading equivalents; matches are candidates, not compliance.
ARTIFACTS = {
    'instructions': ('agents|instructions|instrucoes|instrucciones', 'agent instructions|instruções do projeto|instrucciones del proyecto'),
    'profile': ('readme|perfil.projeto|project.profile|overview', 'project profile|perfil do projeto|perfil del proyecto'),
    'state': ('project.state|estado.fluxo|status|estado.projeto', 'project state|estado do projeto|estado del proyecto'),
    'decisions': ('decisions|decisoes|decisiones|adr', 'decisions|decisões|decisiones|architecture decision'),
    'queue': ('task.queue|backlog|tasks|tarefas|tareas', 'task queue|backlog|fila de tarefas|cola de tareas'),
    'stack': ('stack.decision|architecture|arquitetura|arquitectura|stack', 'stack|architecture|arquitetura|arquitectura'),
    'validation': ('validation|testing|tests|validacao|validacion', 'validation|test strategy|validação|validación|estratégia de testes'),
    'autonomy': ('production.control|supervisor|autonomy|autonomia|operating.runbook', 'autonomy|autonomia|autonomía|operating limits|limites operacionais'),
    'security': ('security|seguranca|seguridad', 'security|segurança|seguridad'),
    'checkpoint': ('checkpoint|handoff.evidencias|handoff|estado.fluxo|project.state', 'checkpoint|handoff|retomada|reanudación'),
    'design_system': ('design.system.contract|design.system|design|sistema.design', 'design system|sistema de design|sistema de diseño'),
}


class AuditError(Exception):
    """Public errors use fixed codes, never untrusted paths or exception messages."""


def directory_fd(path):
    """Open an absolute directory without following symlinks, including ancestors."""
    path = Path(path)
    if '..' in path.parts:
        raise AuditError('PATH_TRAVERSAL_REFUSED')
    path = Path(os.path.abspath(path))
    fd = os.open('/', os.O_RDONLY | os.O_DIRECTORY)
    try:
        for part in path.parts[1:]:
            new = os.open(part, os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW, dir_fd=fd)
            os.close(fd)
            fd = new
        return fd
    except OSError:
        os.close(fd)
        raise AuditError('DIRECTORY_UNAVAILABLE_OR_SYMLINK') from None


def read_file(root_fd, relative):
    parts = Path(relative).parts
    if not parts or any(p in ('.', '..') for p in parts) or Path(relative).is_absolute():
        raise AuditError('UNSAFE_READ')
    fd = os.dup(root_fd)
    try:
        for part in parts[:-1]:
            new = os.open(part, os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW, dir_fd=fd)
            os.close(fd)
            fd = new
        file_fd = os.open(parts[-1], os.O_RDONLY | os.O_NOFOLLOW | os.O_NONBLOCK, dir_fd=fd)
        try:
            info = os.fstat(file_fd)
            if not stat.S_ISREG(info.st_mode) or info.st_size > MAX_BYTES:
                raise AuditError('UNSAFE_OR_OVERSIZED_FILE')
            with os.fdopen(file_fd, 'rb', closefd=False) as stream:
                data = stream.read(MAX_BYTES + 1)
            if len(data) > MAX_BYTES:
                raise AuditError('FILE_BUDGET_EXCEEDED')
            return data
        finally:
            os.close(file_fd)
    except FileNotFoundError:
        raise AuditError('FILE_ABSENT') from None
    except OSError:
        raise AuditError('READ_UNAVAILABLE') from None
    finally:
        os.close(fd)


def sensitive_name(name):
    return (name.startswith('.env') or re.search(r'secret|credential|password|token|private|\.pem$|\.key$', name, re.I)
            or SECRET.search(name) or len(name) > 100)


def inventory(root_fd):
    documents, markers = [], set()
    counts = {'entries': 0, 'documents': 0, 'skipped': 0, 'limited': False, 'secret_candidates': 0}

    def walk(fd, parent='', depth=0):
        with os.scandir(fd) as entries:
            for entry in entries:
                counts['entries'] += 1
                if counts['entries'] > MAX_ENTRIES:
                    counts['limited'] = True
                    return
                name = entry.name
                rel = f'{parent}/{name}' if parent else name
                if sensitive_name(name):
                    counts['skipped'] += 1
                    continue
                if entry.is_symlink():
                    counts['skipped'] += 1
                    continue
                if entry.is_dir(follow_symlinks=False):
                    if name in SKIP or name.lower() not in DOC_DIRS:
                        continue
                    if depth >= MAX_DEPTH:
                        counts['limited'] = True
                        continue
                    try:
                        child = os.open(name, os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW, dir_fd=fd)
                        try:
                            walk(child, rel, depth + 1)
                        finally:
                            os.close(child)
                    except OSError:
                        counts['limited'] = True
                    continue
                if not parent and name in {'package.json', 'pyproject.toml', 'go.mod', 'Cargo.toml', 'index.html'}:
                    markers.add(name)
                if Path(name).suffix.lower() not in {'.md', '.txt', '.rst'} and name != 'package.json':
                    continue
                if counts['documents'] >= MAX_DOCS:
                    counts['limited'] = True
                    continue
                try:
                    data = read_file(root_fd, rel)
                    content = data.decode('utf-8')
                except (AuditError, UnicodeError):
                    counts['limited'] = True
                    continue
                counts['documents'] += 1
                if SECRET.search(content):
                    counts['secret_candidates'] += 1
                    continue
                if name == 'package.json':
                    try:
                        obj = json.loads(content)
                        for group in ('dependencies', 'devDependencies'):
                            deps = obj.get(group, {})
                            if isinstance(deps, dict):
                                markers.update(k for k in ('react', 'vue', 'svelte', 'next', 'angular') if k in deps)
                    except (ValueError, AttributeError):
                        counts['limited'] = True
                    continue
                if content.strip():
                    # Arbitrary filenames are not copied into a potentially shared report.
                    documents.append({'id': hashlib.sha256(rel.encode()).hexdigest()[:16],
                                      'sha256': hashlib.sha256(data).hexdigest(),
                                      'name': Path(name).stem.lower(),
                                      'headings': '\n'.join(line[:200] for line in content.splitlines()
                                                            if line.startswith('#'))})
    walk(root_fd)
    return documents, sorted(markers), counts


def git_probe(root):
    """Read bounded local HEAD metadata only; never invoke Git or inspect dirty state.

    Git status/diff can run clean filters. Even a clean-looking configuration is
    not a reason to execute Git against an untrusted target. Config is not read.
    """
    result = {'repository': False, 'head': None, 'dirty': None,
              'status': 'NOT_VERIFIED', 'dirty_status': 'NOT_VERIFIED',
              'head_status': 'NOT_VERIFIED', 'reason': 'WORKTREE_STATUS_NOT_PROBED'}
    meta = root / '.git'
    if meta.is_symlink() or meta.is_file():
        result['repository'] = True
        result['reason'] = 'EXTERNAL_OR_INDIRECT_GIT_METADATA'
        return result
    if not meta.is_dir():
        return result
    result['repository'] = True
    fd = None
    try:
        fd = directory_fd(meta)
        head = read_file(fd, 'HEAD').decode('ascii').strip()
        oid_pattern = r'[0-9a-f]{40}(?:[0-9a-f]{24})?'
        if re.fullmatch(oid_pattern, head):
            result.update(head=head, head_status='OBSERVED_METADATA')
        elif head.startswith('ref: '):
            ref = head[5:]
            if not re.fullmatch(r'refs/[A-Za-z0-9_./-]+', ref) or any(
                    part in ('', '.', '..') for part in ref.split('/')):
                raise AuditError('INVALID_HEAD_REFERENCE')
            try:
                oid = read_file(fd, ref).decode('ascii').strip()
            except AuditError as error:
                if str(error) != 'FILE_ABSENT':
                    raise
                # A packed ref is valid only when no loose ref exists.
                packed = read_file(fd, 'packed-refs').decode('ascii')
                for line in packed.splitlines():
                    fields = line.split(' ')
                    if len(fields) == 2 and fields[1] == ref and re.fullmatch(oid_pattern, fields[0]):
                        result.update(head=fields[0], head_status='OBSERVED_METADATA')
                        break
            else:
                if re.fullmatch(oid_pattern, oid):
                    result.update(head=oid, head_status='OBSERVED_METADATA')
    except (AuditError, OSError, UnicodeError):
        result['reason'] = 'HEAD_UNAVAILABLE_OR_UNSAFE'
    finally:
        if fd is not None:
            os.close(fd)
    return result


def audit(project):
    root = Path(os.path.abspath(project))
    fd = directory_fd(project)
    try:
        documents, stack, coverage = inventory(fd)
    finally:
        os.close(fd)
    findings, artifacts = [], []

    def finding(identifier, priority, owner, acceptance, deps=()):
        findings.append({'id': identifier, 'priority': priority, 'owner': owner,
                         'input': ['selected_document_metadata', 'project_authorization'],
                         'output': identifier.lower() + '_evidence', 'acceptance': acceptance,
                         'dependencies': list(deps), 'status': 'OPEN'})

    if coverage['secret_candidates']:
        finding('SECRET_REVIEW', 'P0', 'security_owner',
                'Privately triage possible credentials; contain confirmed exposure and verify remediation. Never copy values.')
    ui = bool(set(stack) & {'react', 'vue', 'svelte', 'next', 'angular', 'index.html'})
    for kind, (names, headings) in ARTIFACTS.items():
        matches = [d for d in documents if re.fullmatch(names, d['name'], re.I)
                   or re.search(r'(?im)^#+\s+(?:' + headings + r')\b', d['headings'])]
        required = True if kind != 'design_system' or ui else None
        status = 'FOUND_EQUIVALENT' if matches else ('NOT_VERIFIED' if coverage['limited'] or required is None else 'MISSING_IN_SELECTION')
        artifacts.append({'artifact': kind, 'required': required, 'status': status,
                          'action': 'REUSE_AND_REVIEW' if matches else 'LOCATE_BEFORE_CREATE',
                          'evidence': [{'document_id': d['id'], 'sha256': d['sha256']} for d in matches]})
        if not matches:
            finding('ARTIFACT_' + kind.upper(), 'P1' if required else 'P2', 'project_coordinator',
                    f'Locate and assess existing {kind} records; document applicability; adapt only confirmed gaps without duplicate sources.')
    git = git_probe(root)
    if git['dirty'] is not False:
        finding('BASELINE_REVIEW', 'P1', 'project_coordinator',
                'Reconcile local work and identify an isolated authorized candidate before changes.')
    finding('RUNTIME_EVIDENCE', 'P1', 'runtime_owner',
            'Verify actual Graphy/Loop adapters, identities, controls and receipts in separately authorized isolation; documents are not proof.')
    ids = {f['id'] for f in findings}
    for item in findings:
        item['dependencies'] = [gate for gate in ('SECRET_REVIEW', 'BASELINE_REVIEW')
                                if gate in ids and gate != item['id']
                                and item['id'] != 'SECRET_REVIEW']
    findings.sort(key=lambda f: (f['priority'], f['id']))
    tasks = [{'id': 'TASK_' + f['id'], 'finding_id': f['id'], 'priority': f['priority'],
              'owner': f['owner'], 'input': f['input'], 'output': f['output'],
              'acceptance': f['acceptance'], 'dependencies': ['TASK_' + dep for dep in f['dependencies']],
              'state': 'BLOCKED', 'blocked_by': ['SCOPE_AND_OWNER_CONFIRMATION'],
              'allowed_paths': [], 'allowed_actions': ['review_selected_evidence'],
              'budget': {'max_cycles': 3, 'stop_after_no_progress': 2, 'tokens': None, 'cost': None},
              'execution': 'NOT_RUN'} for f in findings]
    return {'schema_version': 1, 'mode': 'READ_ONLY_AUDIT', 'git': git,
            'coverage': dict(coverage, selection='root and named documentation directories only; no history, source-code or full secret scan'),
            'stack_markers': stack, 'artifacts': artifacts, 'findings': findings, 'proposed_tasks': tasks,
            'runtime': {'graphy': 'NOT_VERIFIED', 'loop': 'NOT_VERIFIED', 'agents': 'NOT_VERIFIED',
                        'ready_unattended': 'BLOCKED'},
            'verification': {'target_commands': 'NOT_RUN', 'target_tests': 'NOT_RUN', 'independent_review': 'NOT_RUN'},
            'limitations': ['Document candidates require human equivalence and content review.',
                            'Stack markers do not prove versions, architecture or deployment.',
                            'Git is never executed; dirty is always NOT_VERIFIED/null; HEAD is metadata, not object verification.',
                            'Submodule internals and indirect Git metadata are not traversed.',
                            'No repository contents, remotes, branches, filenames or secret values are exported.',
                            'Concurrent target changes can invalidate this non-atomic observation.']}


def output_fd(project, output):
    raw = Path(output)
    if '..' in raw.parts or not raw.name or sensitive_name(raw.name):
        raise AuditError('UNSAFE_OUTPUT_PATH')
    destination = Path(os.path.abspath(raw))
    root = Path(os.path.abspath(project))
    if destination == root or root in destination.parents:
        raise AuditError('OUTPUT_INSIDE_TARGET')
    fd = directory_fd(destination.parent)
    try:
        # Never overwrite any existing file (also rejects hardlinks and symlinks).
        return os.open(destination.name, os.O_WRONLY | os.O_CREAT | os.O_EXCL | os.O_NOFOLLOW,
                       0o600, dir_fd=fd)
    except OSError:
        raise AuditError('OUTPUT_EXISTS_OR_UNAVAILABLE') from None
    finally:
        os.close(fd)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--project', required=True, help='Existing local project directory; no symlink ancestors.')
    parser.add_argument('--output', help='New JSON file outside project; existing parent required; never overwritten.')
    parser.add_argument('--plan', action='store_true', help='Write a proposed plan report; requires --output; never executes tasks.')
    args = parser.parse_args(argv)
    if args.plan and not args.output:
        parser.error('--plan requires --output outside the project')
    try:
        # Validate the original path before abspath can erase traversal.
        fd = directory_fd(args.project)
        os.close(fd)
        report = audit(args.project)
        report['mode'] = 'READ_ONLY_PLAN' if args.plan else 'READ_ONLY_AUDIT'
        payload = json.dumps(report, indent=2, ensure_ascii=True) + '\n'
        if args.output:
            fd = output_fd(args.project, args.output)
            with os.fdopen(fd, 'w', encoding='utf-8') as stream:
                stream.write(payload)
        else:
            print(payload, end='')
        return 0
    except (AuditError, OSError) as exc:
        print(json.dumps({'status': 'ERROR', 'error': str(exc) if isinstance(exc, AuditError) else 'IO_UNAVAILABLE'}))
        return 2


if __name__ == '__main__':
    raise SystemExit(main())
