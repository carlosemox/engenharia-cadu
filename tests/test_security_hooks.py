"""Isolated hook tests: no Git hooks installed, no scanners run."""
import hashlib,importlib.util,json,os,pathlib,subprocess,sys,tempfile,unittest
from datetime import datetime,timezone
R=pathlib.Path(__file__).resolve().parents[1]
M=R/'modulos/seguranca';H=M/'hooks'
SPEC=importlib.util.spec_from_file_location('secgate',H/'security_gate.py')
gate=importlib.util.module_from_spec(SPEC);SPEC.loader.exec_module(gate)
EVENTS=['project-start','integration-review','module-complete','phase-exit','pre-commit','pre-push','pull-request','pre-release','scheduled']
class HookTests(unittest.TestCase):
 def fixture(self,root,event,pass_check=True):
  app=root/'app with spaces';app.mkdir()
  p={'schema_version':'1.0','template_only':False,'enabled':True,'project_id':'fixture','events':{event:{'required_checks':['test'],'max_age_seconds':60,'require_independent_review':False,'require_verified_backup':False}}}
  now=datetime.now(timezone.utc).isoformat()
  r={'schema_version':'1.0','template_only':False,'project_id':'fixture','event':event,'snapshot':'fixture:abc','policy_sha256':gate.policy_hash(p),'created_at':now,'checks':[{'id':'test','status':'PASS' if pass_check else 'ERROR','snapshot':'fixture:abc','completed_at':now,'evidence_ref':'fixture:test'}],'findings':[],'coverage_gaps':[]}
  pp=root/'private policy.json';rp=root/'private receipt.json';pp.write_text(json.dumps(p));rp.write_text(json.dumps(r))
  return {'PATH':'/usr/bin:/bin','CADU_SECURITY_PYTHON':sys.executable,'CADU_SECURITY_GATE':str(H/'security_gate.py'),'CADU_PROJECT_ROOT':str(app),'CADU_SECURITY_POLICY':str(pp),'CADU_SECURITY_RECEIPT':str(rp),'CADU_SECURITY_POLICY_SHA256':gate.policy_hash(p),'CADU_SECURITY_SNAPSHOT':'fixture:abc'}
 def test_all_events_have_inert_wrappers(self):
  for event in EVENTS:
   with self.subTest(event=event):
    p=H/(event+'.sh.example');self.assertTrue(p.is_file());self.assertIn('entrypoint.sh.example',p.read_text())
 def test_without_context_blocks(self):
  p=H/'entrypoint.sh.example';self.assertTrue(p.exists())
  cp=subprocess.run(['sh',str(p),'project-start'],env={'PATH':'/usr/bin:/bin'},capture_output=True,text=True)
  self.assertNotEqual(cp.returncode,0);self.assertEqual(json.loads(cp.stdout)['decision'],'BLOCKED')
 def test_unknown_event_blocks(self):
  p=H/'entrypoint.sh.example';self.assertTrue(p.exists())
  cp=subprocess.run(['sh',str(p),'wrong'],capture_output=True,text=True)
  self.assertNotEqual(cp.returncode,0);self.assertEqual(json.loads(cp.stdout)['decision'],'BLOCKED')
 def test_pass_and_fail_every_wrapper(self):
  for event in EVENTS:
   for ok in [True,False]:
    with self.subTest(event=event,ok=ok),tempfile.TemporaryDirectory() as d:
     p=H/(event+'.sh.example');self.assertTrue(p.exists())
     env=self.fixture(pathlib.Path(d),event,ok)
     cp=subprocess.run(['sh',str(p)],env=env,capture_output=True,text=True)
     self.assertEqual(cp.returncode,0 if ok else 1);self.assertEqual(json.loads(cp.stdout)['decision'],'PASS' if ok else 'BLOCKED')
 def test_policy_inside_app_blocks(self):
  with tempfile.TemporaryDirectory() as d:
   env=self.fixture(pathlib.Path(d),'module-complete');old=pathlib.Path(env['CADU_SECURITY_POLICY']);new=pathlib.Path(env['CADU_PROJECT_ROOT'])/'policy.json';new.write_bytes(old.read_bytes());env['CADU_SECURITY_POLICY']=str(new)
   cp=subprocess.run([sys.executable,str(H/'security_gate.py'),'--policy',str(new),'--receipt',env['CADU_SECURITY_RECEIPT'],'--event','module-complete','--snapshot',env['CADU_SECURITY_SNAPSHOT'],'--project-root',env['CADU_PROJECT_ROOT'],'--expected-policy-sha256',env['CADU_SECURITY_POLICY_SHA256']],capture_output=True,text=True)
   self.assertEqual(cp.returncode,2);self.assertNotIn(str(new),cp.stdout+cp.stderr)
 def test_digest_mismatch_blocks(self):
  with tempfile.TemporaryDirectory() as d:
   env=self.fixture(pathlib.Path(d),'module-complete');env['CADU_SECURITY_POLICY_SHA256']='0'*64
   p=H/'entrypoint.sh.example';self.assertTrue(p.exists());cp=subprocess.run(['sh',str(p),'module-complete'],env=env,capture_output=True,text=True)
   self.assertEqual(cp.returncode,2);self.assertEqual(json.loads(cp.stdout)['decision'],'BLOCKED')
 def test_templates_are_inactive(self):
  for f in ['GATE_POLICY.json','GATE_RECEIPT.json','SECURITY-FINDINGS.json']:
   self.assertIs(json.loads((M/'templates'/f).read_text())['template_only'],True)
 def test_campaign_covers_all_three_milestones(self):
  events=json.loads((H/'EVENTOS.json').read_text());self.assertEqual(events['milestones'],{'begin':'project-start','middle':'integration-review','end':'pre-release'})
 def test_no_workflow_or_installed_hooks_in_module(self):
  self.assertFalse((M/'.github').exists());self.assertFalse((M/'.git').exists());self.assertFalse((M/'.githooks').exists())
if __name__=='__main__':unittest.main()
