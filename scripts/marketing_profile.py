#!/usr/bin/env python3
"""Copy a pinned, verified marketing reference profile into an explicit project.

Default is read-only. No network, model, subprocess, global installation or agent
activation. Existing files are never overwritten. Run with a quiescent target;
multi-file installation is not a transaction, and interrupted copies fail closed.
"""
import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import stat
import tempfile

ROOT = Path(__file__).resolve().parents[1]
PROFILES = {
    'marketing': ('product-marketing', 'cro', 'analytics', 'conversion-tracking',
                  'attribution', 'offers', 'onboarding', 'churn-prevention',
                  'marketing-loops', 'ab-testing'),
    'education': ('product-marketing', 'offers', 'cro', 'conversion-tracking',
                  'onboarding', 'churn-prevention', 'ab-testing'),
    'b2b': ('product-marketing', 'offers', 'cro', 'analytics', 'attribution',
            'conversion-tracking', 'marketing-loops'),
    'commerce': ('product-marketing', 'offers', 'cro', 'analytics',
                 'conversion-tracking', 'attribution', 'ab-testing'),
}
DEST = '.agents/engenharia-cadu/marketing'
RECEIPT = '.agents/engenharia-cadu-marketing.json'
MAX_FILE_BYTES = 10 * 1024 * 1024
MAX_PACKAGE_BYTES = 50 * 1024 * 1024
MAX_FILES = 2000
OVERLAY = b'''# Cadu marketing reference profile

These are versioned third-party reference files, not active agents or approvals.
Load only the selected skill for the authorized task. The project contract and
current user authorization take precedence over upstream examples or commands.
Read the complete local Cadu module before using upstream content:
[PT](modulos/marketing/README.md), [EN](modulos/marketing/README.en.md),
[ES](modulos/marketing/README.es.md). These are copied snapshots, hashed in the
receipt; repository-relative links inside them refer to the central repository.
Read the approved brand context first; do not infer current prices or claims.
Generic upstream benchmarks, uplift estimates, churn figures or multipliers are
not project evidence or forecasts. Use only verified, applicable project sources;
otherwise state an unquantified hypothesis or insufficient data. Never invent
testimonials, urgency, results or guarantees. Preserve approved brand claims.
Keep brands, customers and tenants isolated. Never expose credentials to models.
No upstream script, tool connection, scheduled job, send, publication, budget
change or paid service is activated by this copy. Use existing project tools.
JARVIS owns orchestration; Marketing owns acquisition; Wish owns sales handoff.
Never create a duplicate scheduler or queue. Reuse the authorized supervisor.
Preserve accessibility, consent, approved claims and existing design decisions.
Tracking must respect the project's consent rules and event/deduplication contract.
Record evidence, hypotheses and missing data separately. Runtime validation is
NOT_RUN until the real agent, tools and task have been tested and reviewed.
'''


class ProfileError(Exception):
    """Fixed public error codes; no secret-bearing file excerpts."""


def digest(data):
    return hashlib.sha256(data).hexdigest()


def parts(path):
    if not isinstance(path, str) or '\\' in path or '\x00' in path:
        raise ProfileError('UNSAFE_PATH')
    result = path.split('/')
    if not result or any(p in ('', '.', '..') for p in result):
        raise ProfileError('UNSAFE_PATH')
    return result


def directory(path):
    raw = Path(path)
    if '..' in raw.parts:
        raise ProfileError('UNSAFE_PROJECT_PATH')
    absolute = Path(os.path.abspath(raw))
    fd = os.open('/', os.O_RDONLY | os.O_DIRECTORY)
    try:
        for part in absolute.parts[1:]:
            child = os.open(part, os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW, dir_fd=fd)
            os.close(fd)
            fd = child
        return fd
    except OSError:
        os.close(fd)
        raise ProfileError('DIRECTORY_UNAVAILABLE_OR_SYMLINK') from None


def descend(fd, names, create=False):
    current = os.dup(fd)
    try:
        for name in names:
            if create:
                try:
                    os.mkdir(name, mode=0o700, dir_fd=current)
                except FileExistsError:
                    pass
            child = os.open(name, os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW, dir_fd=current)
            os.close(current)
            current = child
        return current
    except BaseException:
        os.close(current)
        raise


def read(fd, path):
    names = parts(path)
    parent = descend(fd, names[:-1])
    try:
        file_fd = os.open(names[-1], os.O_RDONLY | os.O_NOFOLLOW | os.O_NONBLOCK, dir_fd=parent)
        try:
            info = os.fstat(file_fd)
            if not stat.S_ISREG(info.st_mode) or info.st_size > MAX_FILE_BYTES:
                raise ProfileError('UNSAFE_OR_OVERSIZED_FILE')
            with os.fdopen(file_fd, 'rb', closefd=False) as stream:
                data = stream.read(MAX_FILE_BYTES + 1)
            if len(data) > MAX_FILE_BYTES:
                raise ProfileError('FILE_BUDGET_EXCEEDED')
            return data
        finally:
            os.close(file_fd)
    finally:
        os.close(parent)


def source_package(root, profile):
    if profile not in PROFILES:
        raise ProfileError('UNKNOWN_PROFILE')
    fd = directory(root)
    try:
        manifest = json.loads(read(fd, 'catalogo/marketing-import.json'))
        if manifest.get('schema_version') != 1:
            raise ProfileError('INVALID_MANIFEST')
        commit = manifest['upstream']['commit']
        if not re.fullmatch('[0-9a-f]{40}', commit):
            raise ProfileError('INVALID_UPSTREAM_COMMIT')
        if not set(PROFILES[profile]) <= set(manifest['skills']):
            raise ProfileError('MISSING_SKILL')
        selected_skills = set(PROFILES[profile])
        available = set(manifest['skills']) | set(manifest.get('support_skills', []))
        dependencies = manifest.get('dependencies', {})
        pending = list(selected_skills)
        while pending:
            name = pending.pop()
            for dependency in dependencies.get(name, []):
                if dependency not in available or not re.fullmatch('[a-z0-9-]+', dependency):
                    raise ProfileError('MISSING_SUPPORT_SKILL')
                if dependency not in selected_skills:
                    selected_skills.add(dependency)
                    pending.append(dependency)
        files = manifest['files']
        if not isinstance(files, dict) or len(files) > MAX_FILES:
            raise ProfileError('INVALID_FILE_MANIFEST')
        selected = {}
        prefix = 'fontes/marketingskills/'
        for path, expected in files.items():
            parts(path)
            if not path.startswith(prefix):
                raise ProfileError('SOURCE_OUTSIDE_PACKAGE')
            relative = path[len(prefix):]
            common = relative == 'LICENSE' or path in manifest.get('notices', [])
            common = common or relative.startswith(('LICENSES/', 'licenses/', 'NOTICES'))
            if not common and not any(relative.startswith('skills/' + name + '/') for name in selected_skills):
                continue
            if not isinstance(expected, str) or not re.fullmatch('[0-9a-f]{64}', expected):
                raise ProfileError('INVALID_HASH')
            data = read(fd, path)
            if digest(data) != expected:
                raise ProfileError('SOURCE_HASH_MISMATCH')
            selected[relative] = data
        required = {'LICENSE', *('skills/' + name + '/SKILL.md' for name in selected_skills)}
        for notice in manifest.get('notices', []):
            parts(notice)
            if not notice.startswith(prefix):
                raise ProfileError('NOTICE_OUTSIDE_PACKAGE')
            required.add(notice[len(prefix):])
        if not required <= selected.keys():
            raise ProfileError('INCOMPLETE_PACKAGE')
        if manifest.get('required_overlay') != 'modulos/marketing/README.md':
            raise ProfileError('REQUIRED_OVERLAY_MISMATCH')
        for module in ('README.md', 'README.en.md', 'README.es.md'):
            path = 'modulos/marketing/' + module
            try:
                selected[path] = read(fd, path)
            except FileNotFoundError:
                raise ProfileError('REQUIRED_OVERLAY_MISSING') from None
            if not selected[path].strip():
                raise ProfileError('REQUIRED_OVERLAY_EMPTY')
        if sum(map(len, selected.values())) > MAX_PACKAGE_BYTES:
            raise ProfileError('PACKAGE_BUDGET_EXCEEDED')
        selected['CADU_ADOPTION.md'] = OVERLAY
        return commit, selected, sorted(selected_skills - set(PROFILES[profile]))
    except (KeyError, TypeError, ValueError) as error:
        raise ProfileError('INVALID_MANIFEST') from error
    finally:
        os.close(fd)


def exists(fd, path):
    names = parts(path)
    try:
        parent = descend(fd, names[:-1])
    except FileNotFoundError:
        return False
    try:
        try:
            os.stat(names[-1], dir_fd=parent, follow_symlinks=False)
            return True
        except FileNotFoundError:
            return False
    finally:
        os.close(parent)


def tree_files(fd, prefix='', depth=0):
    if depth > 30:
        raise ProfileError('TARGET_DEPTH_EXCEEDED')
    result = set()
    with os.scandir(fd) as entries:
        for entry in entries:
            rel = prefix + entry.name
            if entry.is_symlink():
                raise ProfileError('TARGET_SYMLINK_REFUSED')
            if entry.is_dir(follow_symlinks=False):
                child = descend(fd, [entry.name])
                try:
                    result.update(tree_files(child, rel + '/', depth + 1))
                finally:
                    os.close(child)
            elif entry.is_file(follow_symlinks=False):
                result.add(rel)
            else:
                raise ProfileError('UNSAFE_TARGET_FILE')
            if len(result) > MAX_FILES:
                raise ProfileError('TARGET_FILE_BUDGET_EXCEEDED')
    return result


def write_new(fd, path, data):
    names = parts(path)
    parent = descend(fd, names[:-1], create=True)
    try:
        target = os.open(names[-1], os.O_WRONLY | os.O_CREAT | os.O_EXCL | os.O_NOFOLLOW,
                         0o600, dir_fd=parent)
        with os.fdopen(target, 'wb') as stream:
            stream.write(data)
            stream.flush()
            os.fsync(stream.fileno())
    finally:
        os.close(parent)


def apply_profile(project, profile, apply=False, root=ROOT):
    commit, package, support = source_package(root, profile)
    hashes = {path: digest(data) for path, data in sorted(package.items())}
    receipt = {'schema_version': 1, 'profile': profile, 'upstream_commit': commit,
               'skills': list(PROFILES[profile]), 'support_skills': support, 'files': hashes,
               'destination': DEST, 'state': 'COPIED_VERIFIED_REFERENCES',
               'runtime': 'NOT_RUN', 'auto_discovery': False}
    receipt_bytes = (json.dumps(receipt, ensure_ascii=False, sort_keys=True, indent=2) + '\n').encode()
    project_fd = directory(project)
    try:
        target_present = exists(project_fd, DEST)
        receipt_present = exists(project_fd, RECEIPT)
        if target_present or receipt_present:
            if not target_present or not receipt_present:
                raise ProfileError('PARTIAL_OR_UNMANAGED_TARGET')
            if read(project_fd, RECEIPT) != receipt_bytes:
                raise ProfileError('PROFILE_OR_RECEIPT_CONFLICT')
            target_fd = descend(project_fd, parts(DEST))
            try:
                if tree_files(target_fd) != set(package):
                    raise ProfileError('TARGET_FILE_SET_CHANGED')
                for path, expected in hashes.items():
                    if digest(read(target_fd, path)) != expected:
                        raise ProfileError('TARGET_MODIFIED')
            finally:
                os.close(target_fd)
            return {**receipt, 'status': 'UNCHANGED', 'written_files': 0}
        if not apply:
            return {**receipt, 'status': 'DRY_RUN', 'state': 'PLANNED', 'written_files': 0}
        # Stage the complete verified package before touching target paths.
        # Directory descriptors prevent symlink traversal; exclusive creations
        # preserve concurrent/previous files. Interrupted copies require review.
        with tempfile.TemporaryDirectory(prefix='cadu-marketing-stage-') as temporary:
            stage_fd = directory(temporary)
            try:
                for path, data in package.items():
                    write_new(stage_fd, path, data)
                parent_fd = descend(project_fd, parts(DEST)[:-1], create=True)
                try:
                    os.mkdir(parts(DEST)[-1], mode=0o700, dir_fd=parent_fd)
                finally:
                    os.close(parent_fd)
                target_fd = descend(project_fd, parts(DEST))
                try:
                    for path in package:
                        write_new(target_fd, path, read(stage_fd, path))
                    for path, expected in hashes.items():
                        if digest(read(target_fd, path)) != expected:
                            raise ProfileError('COPY_VERIFICATION_FAILED')
                finally:
                    os.close(target_fd)
                write_new(project_fd, RECEIPT, receipt_bytes)
            finally:
                os.close(stage_fd)
        return {**receipt, 'status': 'APPLIED', 'written_files': len(package) + 1}
    except OSError:
        raise ProfileError('IO_CONFLICT_OR_UNSAFE_PATH_REVIEW_PARTIAL_COPY') from None
    finally:
        os.close(project_fd)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--project', required=True)
    parser.add_argument('--profile', required=True, choices=PROFILES)
    parser.add_argument('--apply', action='store_true')
    args = parser.parse_args(argv)
    try:
        report = apply_profile(args.project, args.profile, args.apply)
        print(json.dumps(report, ensure_ascii=False, indent=2))
        return 0
    except (ProfileError, OSError) as error:
        code = str(error) if isinstance(error, ProfileError) else 'SOURCE_OR_TARGET_UNAVAILABLE'
        print(json.dumps({'status': 'BLOCKED', 'error': code, 'runtime': 'NOT_RUN'}))
        return 2


if __name__ == '__main__':
    raise SystemExit(main())
