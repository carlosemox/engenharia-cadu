"""Synthetic filesystem tests; no upstream code, network or models execute."""
import importlib.util
import json
import os
from pathlib import Path
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location('marketing_profile', ROOT / 'scripts/marketing_profile.py')
profile = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(profile)


class MarketingProfileTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.base = Path(self.temp.name)
        self.source = self.base / 'source'
        self.project = self.base / 'project'
        self.project.mkdir()
        self.manifest = {'schema_version': 1, 'upstream': {'commit': 'a' * 40},
                         'required_overlay': 'modulos/marketing/README.md',
                         'skills': list(profile.PROFILES['marketing']),
                         'support_skills': ['pricing'], 'dependencies': {'offers': ['pricing']},
                         'files': {}}
        for skill in self.manifest['skills'] + ['pricing']:
            self.source_file('skills/' + skill + '/SKILL.md', '# Synthetic ' + skill)
        self.source_file('skills/offers/references/formats.md', 'See ../../pricing/SKILL.md')
        self.source_file('LICENSE', 'MIT synthetic notice')
        self.source_file('LICENSES/third-party.txt', 'Synthetic license')
        self.manifest['notices'] = ['fontes/marketingskills/LICENSE',
                                   'fontes/marketingskills/LICENSES/third-party.txt']
        (self.source / 'catalogo').mkdir()
        (self.source / 'modulos/marketing').mkdir(parents=True)
        for filename in ('README.md', 'README.en.md', 'README.es.md'):
            (self.source / 'modulos/marketing' / filename).write_text('# Complete local module ' + filename)
        self.save_manifest()

    def source_file(self, path, text):
        relative = 'fontes/marketingskills/' + path
        file = self.source / relative
        file.parent.mkdir(parents=True, exist_ok=True)
        file.write_text(text)
        self.manifest['files'][relative] = profile.digest(text.encode())

    def save_manifest(self):
        (self.source / 'catalogo/marketing-import.json').write_text(json.dumps(self.manifest))

    def run_profile(self, apply=False, name='marketing'):
        return profile.apply_profile(self.project, name, apply, self.source)

    def test_dry_run_does_not_create_directories(self):
        report = self.run_profile()
        self.assertEqual(report['status'], 'DRY_RUN')
        self.assertEqual(report['state'], 'PLANNED')
        self.assertEqual(list(self.project.iterdir()), [])

    def test_apply_copies_only_profile_and_support_with_license(self):
        (self.project / 'AGENTS.md').write_text('Preserve existing instructions')
        result = self.run_profile(True, 'education')
        self.assertEqual(result['status'], 'APPLIED')
        self.assertEqual(result['runtime'], 'NOT_RUN')
        self.assertFalse(result['auto_discovery'])
        self.assertEqual(result['support_skills'], ['pricing'])
        destination = self.project / profile.DEST
        self.assertTrue((destination / 'LICENSE').is_file())
        self.assertTrue((destination / 'LICENSES/third-party.txt').is_file())
        self.assertTrue((destination / 'skills/pricing/SKILL.md').is_file())
        self.assertFalse((destination / 'skills/marketing-loops').exists())
        self.assertEqual((self.project / 'AGENTS.md').read_text(), 'Preserve existing instructions')
        self.assertFalse((self.project / '.agents/skills').exists())
        for filename in ('README.md', 'README.en.md', 'README.es.md'):
            relative = 'modulos/marketing/' + filename
            self.assertEqual((destination / relative).read_bytes(), (self.source / relative).read_bytes())
            self.assertEqual(result['files'][relative], profile.digest((destination / relative).read_bytes()))

    def test_idempotent_apply_and_dry_run_preserve_mtimes(self):
        self.run_profile(True)
        before = {p: (p.read_bytes(), p.stat().st_mtime_ns) for p in self.project.rglob('*') if p.is_file()}
        self.assertEqual(self.run_profile(True)['status'], 'UNCHANGED')
        self.assertEqual(self.run_profile()['status'], 'UNCHANGED')
        after = {p: (p.read_bytes(), p.stat().st_mtime_ns) for p in self.project.rglob('*') if p.is_file()}
        self.assertEqual(before, after)

    def test_tampered_source_is_blocked_before_writes(self):
        (self.source / 'fontes/marketingskills/skills/cro/SKILL.md').write_text('tampered')
        with self.assertRaisesRegex(profile.ProfileError, 'SOURCE_HASH_MISMATCH'):
            self.run_profile(True)
        self.assertEqual(list(self.project.iterdir()), [])

    def test_modified_target_is_preserved_and_blocked(self):
        self.run_profile(True)
        target = self.project / profile.DEST / 'skills/cro/SKILL.md'
        target.write_text('user changes')
        with self.assertRaisesRegex(profile.ProfileError, 'TARGET_MODIFIED'):
            self.run_profile(True)
        self.assertEqual(target.read_text(), 'user changes')

    def test_existing_unmanaged_target_is_not_overwritten(self):
        target = self.project / profile.DEST
        target.mkdir(parents=True)
        (target / 'user.txt').write_text('preserve')
        with self.assertRaisesRegex(profile.ProfileError, 'PARTIAL_OR_UNMANAGED_TARGET'):
            self.run_profile(True)
        self.assertEqual((target / 'user.txt').read_text(), 'preserve')

    def test_existing_receipt_conflict_is_preserved(self):
        receipt = self.project / profile.RECEIPT
        receipt.parent.mkdir()
        receipt.write_text('existing')
        with self.assertRaisesRegex(profile.ProfileError, 'PARTIAL_OR_UNMANAGED_TARGET'):
            self.run_profile(True)
        self.assertEqual(receipt.read_text(), 'existing')

    def test_profile_switch_requires_review(self):
        self.run_profile(True, 'education')
        with self.assertRaisesRegex(profile.ProfileError, 'PROFILE_OR_RECEIPT_CONFLICT'):
            self.run_profile(True, 'marketing')

    def test_added_target_file_is_detected(self):
        self.run_profile(True)
        (self.project / profile.DEST / 'extra.md').write_text('local')
        with self.assertRaisesRegex(profile.ProfileError, 'TARGET_FILE_SET_CHANGED'):
            self.run_profile()

    def test_project_symlink_is_refused(self):
        alias = self.base / 'alias'
        alias.symlink_to(self.project, target_is_directory=True)
        with self.assertRaisesRegex(profile.ProfileError, 'DIRECTORY_UNAVAILABLE_OR_SYMLINK'):
            profile.apply_profile(alias, 'marketing', True, self.source)

    def test_target_parent_symlink_cannot_escape_project(self):
        external = self.base / 'external'
        external.mkdir()
        (self.project / '.agents').symlink_to(external, target_is_directory=True)
        with self.assertRaises(profile.ProfileError):
            self.run_profile(True)
        self.assertEqual(list(external.iterdir()), [])

    def test_source_symlink_is_refused(self):
        file = self.source / 'fontes/marketingskills/skills/cro/SKILL.md'
        external = self.base / 'external.md'
        external.write_bytes(file.read_bytes())
        file.unlink()
        file.symlink_to(external)
        with self.assertRaises(OSError):
            self.run_profile(True)
        self.assertEqual(list(self.project.iterdir()), [])

    def test_manifest_traversal_and_missing_support_are_refused(self):
        self.manifest['files']['fontes/marketingskills/../escape'] = '0' * 64
        self.save_manifest()
        with self.assertRaisesRegex(profile.ProfileError, 'UNSAFE_PATH'):
            self.run_profile(True)
        del self.manifest['files']['fontes/marketingskills/../escape']
        self.manifest['dependencies']['offers'] = ['absent']
        self.save_manifest()
        with self.assertRaisesRegex(profile.ProfileError, 'MISSING_SUPPORT_SKILL'):
            self.run_profile(True)

    def test_all_profiles_have_context_and_no_unknown_skills(self):
        for name, selected in profile.PROFILES.items():
            with self.subTest(profile=name):
                self.assertIn('product-marketing', selected)
                self.assertTrue(set(selected) <= set(self.manifest['skills']))
                result = self.run_profile(name=name)
                self.assertEqual(result['status'], 'DRY_RUN')

    def test_missing_required_license_notice_is_blocked(self):
        del self.manifest['files']['fontes/marketingskills/LICENSES/third-party.txt']
        self.save_manifest()
        with self.assertRaisesRegex(profile.ProfileError, 'INCOMPLETE_PACKAGE'):
            self.run_profile(True)
        self.assertEqual(list(self.project.iterdir()), [])

    def test_missing_module_translation_is_blocked_before_writes(self):
        (self.source / 'modulos/marketing/README.es.md').unlink()
        with self.assertRaisesRegex(profile.ProfileError, 'REQUIRED_OVERLAY_MISSING'):
            self.run_profile(True)
        self.assertEqual(list(self.project.iterdir()), [])

    def test_required_overlay_cannot_be_redirected(self):
        self.manifest['required_overlay'] = '../../other.md'
        self.save_manifest()
        with self.assertRaisesRegex(profile.ProfileError, 'REQUIRED_OVERLAY_MISMATCH'):
            self.run_profile(True)
        self.assertEqual(list(self.project.iterdir()), [])

    def test_module_change_requires_review_of_existing_profile(self):
        self.run_profile(True)
        (self.source / 'modulos/marketing/README.md').write_text('Changed local policy')
        with self.assertRaisesRegex(profile.ProfileError, 'PROFILE_OR_RECEIPT_CONFLICT'):
            self.run_profile(True)


if __name__ == '__main__':
    unittest.main()
