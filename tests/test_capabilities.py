import hashlib
import importlib.util
import json
from pathlib import Path
import unittest
import zipfile

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('capabilities', ROOT/'scripts/build_capabilities.py')
build = importlib.util.module_from_spec(spec)
spec.loader.exec_module(build)

class CapabilitiesTests(unittest.TestCase):
    def test_archive_provenance_and_license(self):
        manifest = json.loads((ROOT/'catalogo/marketing-import.json').read_text())
        with zipfile.ZipFile(ROOT/'docs/capacidades/marketing-capabilities-1.0.0.zip') as archive:
            for path, expected in manifest['files'].items():
                self.assertEqual(hashlib.sha256(archive.read(path)).hexdigest(), expected)
            self.assertIn('scripts/marketing_profile.py', archive.namelist())
            self.assertIn('MIT License', archive.read(manifest['license_file']).decode())
            self.assertTrue(all(not n.startswith('/') and '..' not in Path(n).parts for n in archive.namelist()))

    def test_full_translations_and_command_downloads(self):
        for lang, suffix, *_ in build.LANGS.values():
            page = (ROOT/f'docs/capacidades/index{suffix}.html').read_text()
            self.assertIn(f'<html lang="{lang}">', page)
            self.assertEqual(page.count('<h1>'), 1)
            for source in [f'modulos/marketing/README{suffix}.md', f'integracoes/mastra/README{suffix}.md']:
                self.assertIn(build.render((ROOT/source).read_text(), Path(source)), page)
            self.assertEqual((ROOT/f'docs/comandos/APLICAR_MARKETING{suffix}.txt').read_bytes(), (ROOT/f'comandos/APLICAR_MARKETING{suffix}.md').read_bytes())

    def test_build_repeat_is_identical(self):
        folder=ROOT/'docs/capacidades'
        before={p.name:p.read_bytes() for p in folder.iterdir()}
        build.build()
        self.assertEqual(before,{p.name:p.read_bytes() for p in folder.iterdir()})

    def test_upstream_html_is_rendered_as_text(self):
        self.assertNotIn('<script>', build.render('<script>alert(1)</script>',Path('docs/example.md')))
