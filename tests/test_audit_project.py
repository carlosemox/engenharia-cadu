"""Regression/security tests use only disposable synthetic projects."""
import importlib.util
import json
import os
from pathlib import Path
import subprocess
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location('audit_project', ROOT / 'scripts/audit_project.py')
audit = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(audit)


class AuditTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.base = Path(self.temp.name)
        self.project = self.base / 'project'
        self.project.mkdir()

    def cli(self, *args):
        result = subprocess.run([os.sys.executable, str(ROOT / 'scripts/audit_project.py'),
                                 '--project', str(self.project), *map(str, args)],
                                capture_output=True, text=True)
        return result

    def git(self, *args):
        return subprocess.run(['git', '-C', str(self.project), *args], check=True,
                              stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    def init_git(self):
        self.git('init')
        self.git('config', 'user.email', 'synthetic@example.invalid')
        self.git('config', 'user.name', 'Synthetic')

    def test_default_json_success_with_findings(self):
        result = self.cli()
        self.assertEqual(result.returncode, 0, result.stderr)
        report = json.loads(result.stdout)
        self.assertTrue(report['findings'])
        self.assertFalse(report['git']['repository'])
        self.assertEqual(report['runtime']['graphy'], 'NOT_VERIFIED')
        self.assertEqual(report['runtime']['loop'], 'NOT_VERIFIED')
        self.assertEqual(report['verification']['target_tests'], 'NOT_RUN')
        for item in report['findings'] + report['proposed_tasks']:
            self.assertTrue({'priority', 'owner', 'input', 'output', 'acceptance', 'dependencies'} <= item.keys())
        self.assertTrue(all(t['state'] == 'BLOCKED' for t in report['proposed_tasks']))

    def test_equivalent_heading_reuses_existing_document(self):
        (self.project / 'docs').mkdir()
        (self.project / 'docs/handbook.md').write_text('# Project profile\nExisting project.\n## Architecture\nPython\n## Backlog\nOne task\n## Design system\nTokens\n')
        report = audit.audit(self.project)
        by_id = {a['artifact']: a for a in report['artifacts']}
        for name in ('profile', 'stack', 'queue', 'design_system'):
            self.assertEqual(by_id[name]['status'], 'FOUND_EQUIVALENT')
            self.assertEqual(by_id[name]['action'], 'REUSE_AND_REVIEW')
        self.assertEqual(len(list(self.project.rglob('*'))), 2)

    def test_ui_contract_is_conditional(self):
        report = audit.audit(self.project)
        self.assertIsNone(next(a for a in report['artifacts'] if a['artifact'] == 'design_system')['required'])
        (self.project / 'package.json').write_text('{"dependencies":{"react":"*"}}')
        report = audit.audit(self.project)
        self.assertTrue(next(a for a in report['artifacts'] if a['artifact'] == 'design_system')['required'])

    def test_git_unborn_clean_dirty_and_no_writes(self):
        self.init_git()
        self.assertIsNone(audit.audit(self.project)['git']['head'])
        (self.project / 'README.md').write_text('Synthetic project')
        self.git('add', '.')
        self.git('commit', '-m', 'synthetic baseline')
        before = {p.relative_to(self.project): (p.read_bytes(), p.stat().st_mtime_ns)
                  for p in self.project.rglob('*') if p.is_file()}
        report = audit.audit(self.project)
        self.assertEqual(report['git']['head'], self.git('rev-parse', 'HEAD').stdout.decode().strip())
        self.assertIsNone(report['git']['dirty'])
        self.assertEqual(report['git']['dirty_status'], 'NOT_VERIFIED')
        after = {p.relative_to(self.project): (p.read_bytes(), p.stat().st_mtime_ns)
                 for p in self.project.rglob('*') if p.is_file()}
        self.assertEqual(before, after)
        (self.project / 'README.md').write_text('Changed')
        self.assertIsNone(audit.audit(self.project)['git']['dirty'])
        self.git('checkout', '--', 'README.md')
        (self.project / 'untracked').write_text('x')
        self.assertIsNone(audit.audit(self.project)['git']['dirty'])

    def test_git_does_not_run_fsmonitor_or_target_commands(self):
        self.init_git()
        marker = self.base / 'executed'
        hook = self.base / 'hook'
        hook.write_text('#!/bin/sh\ntouch "' + str(marker) + '"\n')
        hook.chmod(0o700)
        self.git('config', 'core.fsmonitor', str(hook))
        self.git('config', 'core.hooksPath', str(self.base))
        (self.project / 'package.json').write_text(json.dumps({'scripts': {'test': str(hook)}}))
        (self.project / 'README.md').write_text('Run ' + str(hook))
        self.assertEqual(self.cli().returncode, 0)
        self.assertFalse(marker.exists())

    def test_external_git_metadata_not_followed(self):
        (self.project / '.git').write_text('gitdir: ../private')
        self.assertEqual(audit.audit(self.project)['git']['status'], 'NOT_VERIFIED')

    def test_git_config_include_and_symlink_are_refused(self):
        self.init_git()
        config = self.project / '.git/config'
        original = config.read_text()
        config.write_text(original + '\n[include]\n path = /private/config\n')
        with patch.object(subprocess, 'Popen', side_effect=AssertionError('must not invoke git')):
            self.assertEqual(audit.audit(self.project)['git']['status'], 'NOT_VERIFIED')
        config.write_text(original)
        (self.project / '.git/HEAD').unlink()
        (self.project / '.git/HEAD').symlink_to(self.base / 'private')
        with patch.object(subprocess, 'Popen', side_effect=AssertionError('must not invoke git')):
            self.assertEqual(audit.audit(self.project)['git']['status'], 'NOT_VERIFIED')

    def test_git_failure_is_unknown_not_clean(self):
        self.init_git()
        (self.project / '.git/HEAD').write_text('invalid private details')
        report = audit.audit(self.project)
        self.assertIsNone(report['git']['dirty'])
        self.assertEqual(report['git']['status'], 'NOT_VERIFIED')
        self.assertNotIn('private details', json.dumps(report))

    def test_git_clean_filter_cannot_execute(self):
        self.init_git()
        (self.project / 'README.md').write_text('Synthetic')
        self.git('add', '.')
        self.git('commit', '-m', 'baseline')
        marker = self.base / 'filter-executed'
        self.git('config', 'filter.untrusted.clean', 'touch ' + str(marker))
        (self.project / '.gitattributes').write_text('*.md filter=untrusted\n')
        (self.project / 'README.md').write_text('Different')
        with patch.object(subprocess, 'Popen', side_effect=AssertionError('must not invoke git')):
            report = audit.audit(self.project)
        self.assertEqual(report['git']['status'], 'NOT_VERIFIED')
        self.assertFalse(marker.exists())

    def test_manual_head_loose_packed_detached_and_unsafe(self):
        meta = self.project / '.git'
        meta.mkdir()
        oid = 'a' * 40
        (meta / 'HEAD').write_text('ref: refs/heads/example\n')
        (meta / 'packed-refs').write_text(oid + ' refs/heads/example\n')
        self.assertEqual(audit.audit(self.project)['git']['head'], oid)
        (meta / 'HEAD').write_text(oid + '\n')
        self.assertEqual(audit.audit(self.project)['git']['head'], oid)
        (meta / 'HEAD').write_text('ref: refs/../../private\n')
        self.assertIsNone(audit.audit(self.project)['git']['head'])
        (meta / 'HEAD').write_text('ref: refs/heads/example\n')
        (meta / 'refs').symlink_to(self.base, target_is_directory=True)
        self.assertIsNone(audit.audit(self.project)['git']['head'])

    def test_audit_starts_no_process_even_with_git_repository(self):
        self.init_git()
        with patch.object(subprocess, 'Popen', side_effect=AssertionError('process execution forbidden')):
            report = audit.audit(self.project)
        self.assertIsNone(report['git']['dirty'])

    def test_task_dependencies_resolve_without_cycles(self):
        (self.project / 'README.md').write_text('api_key=' + 'synthetic' * 4)
        tasks = {t['id']: t for t in audit.audit(self.project)['proposed_tasks']}
        seen = set()
        def visit(key, active):
            self.assertNotIn(key, active)
            for dependency in tasks[key]['dependencies']:
                visit(dependency, active | {key})
            seen.add(key)
        for key in tasks:
            visit(key, set())
        self.assertEqual(seen, set(tasks))

    def test_secrets_not_exported_and_candidate_blocks(self):
        value = 'gh' + 'p_' + 'A' * 40
        (self.project / '.env').write_text('SECRET=' + value)
        (self.project / 'README.md').write_text('# Project profile\n' + value)
        result = self.cli()
        self.assertNotIn(value, result.stdout)
        report = json.loads(result.stdout)
        self.assertEqual(report['findings'][0]['id'], 'SECRET_REVIEW')
        self.assertEqual(report['coverage']['secret_candidates'], 1)

    def test_symlinks_and_fifo_are_not_read(self):
        outside = self.base / 'outside.md'
        outside.write_text('# Architecture\nConfidential')
        (self.project / 'architecture.md').symlink_to(outside)
        (self.project / 'docs').symlink_to(self.base, target_is_directory=True)
        os.mkfifo(self.project / 'README.md')
        report = audit.audit(self.project)
        self.assertTrue(report['coverage']['limited'])
        self.assertFalse(any(a['evidence'] for a in report['artifacts']))

    def test_output_target_traversal_and_symlink_refused(self):
        for dest in (self.project / 'report.json', self.base / 'project/../report.json'):
            self.assertEqual(self.cli('--output', dest).returncode, 2)
            self.assertFalse(dest.exists())
        link = self.base / 'link'
        link.symlink_to(self.project, target_is_directory=True)
        self.assertEqual(self.cli('--output', link / 'report.json').returncode, 2)
        victim = self.project / 'victim'
        victim.write_text('preserve')
        dest = self.base / 'report.json'
        dest.symlink_to(victim)
        self.assertEqual(self.cli('--output', dest).returncode, 2)
        self.assertEqual(victim.read_text(), 'preserve')
        dest.unlink()
        os.link(victim, dest)
        self.assertEqual(self.cli('--output', dest).returncode, 2)
        self.assertEqual(victim.read_text(), 'preserve')

    def test_plan_outside_exclusive_private_report(self):
        dest = self.base / 'report.json'
        self.assertEqual(self.cli('--plan', '--output', dest).returncode, 0)
        self.assertEqual(json.loads(dest.read_text())['mode'], 'READ_ONLY_PLAN')
        self.assertEqual(dest.stat().st_mode & 0o777, 0o600)
        original = dest.read_bytes()
        self.assertEqual(self.cli('--plan', '--output', dest).returncode, 2)
        self.assertEqual(dest.read_bytes(), original)
        self.assertEqual(self.cli('--plan').returncode, 2)

    def test_invalid_project_and_symlink_ancestor(self):
        result = subprocess.run([os.sys.executable, str(ROOT / 'scripts/audit_project.py'),
                                 '--project', str(self.base / 'absent')], capture_output=True, text=True)
        self.assertEqual(result.returncode, 2)
        self.assertNotIn(str(self.base), result.stdout)
        link = self.base / 'link'
        link.symlink_to(self.project, target_is_directory=True)
        with self.assertRaises(audit.AuditError):
            audit.audit(link)

    def test_budgets_and_malformed_manifest(self):
        (self.project / 'README.md').write_text('x' * (audit.MAX_BYTES + 1))
        (self.project / 'package.json').write_text('[]')
        report = audit.audit(self.project)
        self.assertTrue(report['coverage']['limited'])
        self.assertTrue(all(a['status'] == 'NOT_VERIFIED' for a in report['artifacts']))
        with patch.object(audit, 'MAX_ENTRIES', 0):
            self.assertTrue(audit.audit(self.project)['coverage']['limited'])

    def test_translated_downloads_match_commands(self):
        for suffix in ('', '.en', '.es'):
            source = (ROOT / f'comandos/REGULARIZAR_PROJETO{suffix}.md').read_text()
            body = source.split('```text\n', 1)[1].split('\n```', 1)[0]
            self.assertEqual(body + '\n', (ROOT / f'docs/comandos/REGULARIZAR_PROJETO{suffix}.txt').read_text())


if __name__ == '__main__':
    unittest.main()
