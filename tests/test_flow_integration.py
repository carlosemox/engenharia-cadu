import pathlib,re,unittest,json
R=pathlib.Path(__file__).resolve().parents[1]
class FlowIntegrationTests(unittest.TestCase):
 def test_all_29_have_dispatch_contract(self):
  paths=list((R/'p').glob('P[0-9][0-9].md')); self.assertEqual(len(paths),29)
  for p in paths:
   with self.subTest(p=p.name):
    t=p.read_text();self.assertEqual(t.count('CONTINUIDADE SUPERVISIONADA — 2.2'),1)
    m=re.search(r'## Comando completo\n```text\n([\s\S]*?)\n```',t)
    self.assertIn('CONTINUIDADE SUPERVISIONADA — 2.2',m.group(1))
    self.assertIn('BACKUP_DRIVE.md',m.group(1))
    self.assertIn('SEGURANCA_ENGENHARIA.md',m.group(1))
 def test_p01_is_continuous_only_for_new_product(self):
  t=(R/'p/P01.md').read_text();self.assertIn('iniciar um produto do zero',t);self.assertIn('ISOLADO',t)
 def test_canonical_common_updated(self):
  t=(R/'politicas/CONTRATO_COMUM.md').read_text();self.assertIn('CONTINUO_SUPERVISIONADO',t)
 def test_state_template_disabled(self):
  s=json.loads((R/'templates/ESTADO_FLUXO.json').read_text());self.assertEqual(s['status'],'NOT_STARTED');self.assertFalse(s['next_scope_authorized']);self.assertIsNone(s['snapshot'])
 def test_routes_do_not_run_optional_automatically(self):
  s=json.loads((R/'orquestracao/rotas.json').read_text());self.assertEqual(s['entry'],'P01');self.assertNotIn('P17',s['default_order']);self.assertEqual(s['loops']['P14']['fix'],'P13');self.assertIsNone(s['on_scope_complete'])
 def test_guides_exist(self):
  for n in ['continuidade','seguranca','backup']:
   self.assertTrue((R/f'docs/guia/{n}/index.html').exists())
 def test_read_entry_routes_continuity(self):self.assertIn('CONTINUIDADE.md',(R/'read.md').read_text())
if __name__=='__main__':unittest.main()
