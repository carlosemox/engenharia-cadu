"""Structural tests for documented coordination, not live-agent security certification."""
import json,pathlib,re,unittest
R=pathlib.Path(__file__).resolve().parents[1]
class FlowIntegrationTests(unittest.TestCase):
 def test_all_29_are_preserved(self):
  self.assertEqual({p.stem for p in (R/'p').glob('P[0-9][0-9].md')},{f'P{i:02d}' for i in range(29)})
 def test_routes_reference_existing_prompts(self):
  r=json.loads((R/'orquestracao/rotas.json').read_text());self.assertEqual(r['entry'],'P01')
  self.assertEqual(set(r['default_order'])|set(r['not_automatic'])|{'P00'},{f'P{i:02d}' for i in range(29)})
  for p in r['default_order']+r['not_automatic']:self.assertTrue((R/'p'/f'{p}.md').exists())
 def test_optional_mission_not_automatic(self):
  r=json.loads((R/'orquestracao/rotas.json').read_text());self.assertNotIn('P17',r['default_order']);self.assertIsNone(r['on_scope_complete']);self.assertEqual(r['loops']['P14']['fix'],'P13')
 def test_p01_loads_transversal_policies(self):
  p=(R/'p/P01.md').read_text()
  for s in ['CONTINUO_SUPERVISIONADO','ISOLADO','CONTINUIDADE.md','SEGURANCA_ENGENHARIA.md','BACKUP_DRIVE.md','orquestracao/rotas.json']:self.assertIn(s,p)
 def test_coordinator_applies_transition_to_all_phases(self):
  p=(R/'AGENTS.md').read_text();self.assertIn('P00–P28',p);self.assertIn('CONTINUO_SUPERVISIONADO',p);self.assertIn('backup',p)
 def test_entry_loads_policy(self):self.assertIn('politicas/CONTINUIDADE.md',(R/'read.md').read_text())
 def test_template_not_approval(self):
  s=json.loads((R/'templates/ESTADO_FLUXO.json').read_text());self.assertEqual(s['status'],'NOT_STARTED');self.assertIs(s['next_scope_authorized'],False);self.assertIsNone(s['snapshot']);self.assertIsNone(s['backup']['receipt'])
 def test_critical_guards_documented(self):
  t=(R/'politicas/CONTINUIDADE.md').read_text()
  for x in ['NOT_RUN','GO','backup','supervisor','limites']:self.assertIn(x,t)
 def test_security_no_absolute_claim(self):
  t=(R/'politicas/SEGURANCA_ENGENHARIA.md').read_text();self.assertIn('Nenhuma revisão ou ferramenta garante',t);self.assertIn('ASVS 5.0.0',t);self.assertIn('crítico/alto',t);self.assertIn('independente',t)
 def test_backup_verification_and_secrets(self):
  t=(R/'politicas/BACKUP_DRIVE.md').read_text()
  for x in ['SHA-256','VERIFICADO','criptografado','Storage','sobrescrever']:self.assertIn(x,t)
 def test_p01_download_parity(self):
  t=(R/'p/P01.md').read_text();m=re.search(r'## Comando completo\n```text\n([\s\S]*?)\n```',t);self.assertIsNotNone(m);self.assertEqual(m.group(1).strip(),(R/'docs/comandos/P01.txt').read_text().strip())
if __name__=='__main__':unittest.main()
