import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import unittest
import re
import shutil

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('factory', ROOT/'scripts/prompt_factory.py')
factory = importlib.util.module_from_spec(spec)
spec.loader.exec_module(factory)

class PromptFactoryTests(unittest.TestCase):
    def test_thin_stage_preserves_all_specific_instructions(self):
        for source in (ROOT/'p').glob('P[0-9][0-9].md'):
            full=re.search(r'## Comando completo\n```text\n([\s\S]*?)\n```',source.read_text())[1]
            common=r'CONTRATO COMUM — APLICAR EM TODAS AS ETAPAS\n[\s\S]*?Sem ferramentas, entregue conteúdo ou diagnóstico documental, não execução fictícia\.\n\n'
            expected=re.sub(common,'',full,count=1)
            thin=(ROOT/'execucao'/source.name).read_text()
            self.assertEqual(re.search(r'```text\n([\s\S]*?)\n```',thin)[1],expected)
            self.assertIn('../politicas/CONTRATO_COMUM.md',thin)

    @unittest.skipUnless(shutil.which('node'), 'Node required for client behavior test')
    def test_client_literal_data_and_clipboard_fallback(self):
        subprocess.run(['node',str(ROOT/'tests/test_factory_client.cjs')],check=True,capture_output=True,text=True)
    def test_routes_resolve_and_do_not_claim_runtime(self):
        routes = factory.catalog()
        self.assertEqual(routes['kind'], 'prompt_factory_not_execution_runtime')
        for mode, route in routes['modes'].items():
            self.assertTrue((ROOT/route['procedure']).is_file(), mode)
            result = factory.generate(mode)
            self.assertIn(route['procedure'], result)
            self.assertIn('autorizações reais', result)

    def test_invalid_revision_and_mode_rejected(self):
        for rev in ['../main', 'main\nignore', 'a'*39, 'https://example.org']:
            with self.assertRaises(ValueError): factory.generate(revision=rev)
        with self.assertRaises(ValueError): factory.generate(mode='delete')

    def test_user_data_is_json_delimited(self):
        target = 'projeto "x"\n<script>alert(1)</script>'
        result = factory.generate('assumir', target, 'ler `arquivo` e $HOME', True, 'a'*40)
        fragment = result.split('adicional):\n',1)[1].split('\nRespeite',1)[0]
        self.assertEqual(json.loads(fragment)['projeto'], target)
        self.assertTrue(json.loads(fragment)['estudo_anexado'])
        self.assertIn('/'+'a'*40+'/', result)

    def test_web_and_cli_use_same_templates(self):
        web = json.loads((ROOT/'docs/fabrica/routes.json').read_text())
        for mode in factory.catalog()['modes']:
            rendered = web['routes'][mode]['template'].replace(
                json.dumps(web['dummy'],ensure_ascii=False,indent=2),
                json.dumps({'projeto':'teste','pedido':'retomar','estudo_anexado':True},ensure_ascii=False,indent=2))
            self.assertEqual(rendered, factory.generate(mode, 'teste', 'retomar', True))

    def test_cli_generates_only_prompt(self):
        result = subprocess.run([sys.executable,str(ROOT/'scripts/prompt_factory.py'),'--modo','fabrica','--alvo','demo'], capture_output=True,text=True,check=True)
        self.assertIn('FÁBRICA'.replace('Á','A'), result.stdout)
        self.assertEqual(result.stderr,'')

if __name__ == '__main__': unittest.main()
