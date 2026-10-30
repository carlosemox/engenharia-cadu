"""Tests the receipt gate, never certifies an application or a scanner."""
import copy, importlib.util, json, pathlib, subprocess, sys, tempfile, unittest
R=pathlib.Path(__file__).resolve().parents[1]
SCRIPT=R/'modulos/seguranca/hooks/security_gate.py'
SPEC=importlib.util.spec_from_file_location('cadu_security_gate',SCRIPT)
gate=importlib.util.module_from_spec(SPEC);SPEC.loader.exec_module(gate)
NOW=1793394000
STAMP='2026-10-30T21:00:00Z'
def fixture():
 p={'schema_version':'1.0','template_only':False,'enabled':True,'project_id':'fixture',
    'events':{'module-complete':{'required_checks':['secrets','regression'], 'max_age_seconds':3600,
                               'require_independent_review':False,'require_verified_backup':False}}}
 r={'schema_version':'1.0','template_only':False,'project_id':'fixture','event':'module-complete',
    'snapshot':'fixture:abc','policy_sha256':gate.policy_hash(p),'created_at':STAMP,
    'checks':[{'id':x,'status':'PASS','snapshot':'fixture:abc','completed_at':STAMP,'evidence_ref':'fixture:'+x} for x in ['secrets','regression']],
    'findings':[], 'coverage_gaps':[]}
 return p,r
class SecurityGateTests(unittest.TestCase):
 def result(self,p,r,event='module-complete',snapshot='fixture:abc'):
  return gate.evaluate(p,r,event=event,snapshot=snapshot,now=NOW)
 def test_matching_fixture_passes(self):
  p,r=fixture();self.assertEqual(self.result(p,r)['decision'],'PASS')
 def test_disabled_policy_blocks(self):
  p,r=fixture();p['enabled']=False;self.assertEqual(self.result(p,r)['decision'],'BLOCKED')
 def test_template_policy_blocks(self):
  p,r=fixture();p['template_only']=True;self.assertEqual(self.result(p,r)['decision'],'BLOCKED')
 def test_template_receipt_blocks(self):
  p,r=fixture();r['template_only']=True;self.assertEqual(self.result(p,r)['decision'],'BLOCKED')
 def test_wrong_project_blocks(self):
  p,r=fixture();r['project_id']='other';self.assertEqual(self.result(p,r)['decision'],'BLOCKED')
 def test_wrong_event_blocks(self):
  p,r=fixture();r['event']='pre-release';self.assertEqual(self.result(p,r)['decision'],'BLOCKED')
 def test_unknown_event_blocks(self):
  p,r=fixture();self.assertEqual(self.result(p,r,event='unknown')['decision'],'BLOCKED')
 def test_wrong_snapshot_blocks(self):
  p,r=fixture();self.assertEqual(self.result(p,r,snapshot='fixture:new')['decision'],'BLOCKED')
 def test_changed_policy_blocks(self):
  p,r=fixture();p['events']['module-complete']['max_age_seconds']=3000;self.assertEqual(self.result(p,r)['decision'],'BLOCKED')
 def test_missing_check_blocks(self):
  p,r=fixture();r['checks'].pop();self.assertEqual(self.result(p,r)['decision'],'BLOCKED')
 def test_non_pass_states_block(self):
  for status in ['FAIL','NOT_RUN','ERROR','TIMEOUT','SKIPPED','N/A','pass',None]:
   with self.subTest(status=status):
    p,r=fixture();r['checks'][0]['status']=status;self.assertEqual(self.result(p,r)['decision'],'BLOCKED')
 def test_empty_rules_fail_closed(self):
  p,r=fixture();p['events']['module-complete']['required_checks']=[];r['policy_sha256']=gate.policy_hash(p);self.assertEqual(self.result(p,r)['decision'],'BLOCKED')
 def test_duplicate_check_rejected(self):
  p,r=fixture();r['checks'].append(copy.deepcopy(r['checks'][0]));self.assertEqual(self.result(p,r)['decision'],'BLOCKED')
 def test_missing_evidence_blocks(self):
  p,r=fixture();r['checks'][0]['evidence_ref']='';self.assertEqual(self.result(p,r)['decision'],'BLOCKED')
 def test_check_snapshot_mismatch(self):
  p,r=fixture();r['checks'][0]['snapshot']='fixture:old';self.assertEqual(self.result(p,r)['decision'],'BLOCKED')
 def test_old_check_cannot_be_refreshed_by_receipt_date(self):
  p,r=fixture();r['checks'][0]['completed_at']='2026-10-29T21:00:00Z';self.assertEqual(self.result(p,r)['decision'],'BLOCKED')
 def test_stale_receipt_blocks(self):
  p,r=fixture();r['created_at']='2026-10-29T21:00:00Z';self.assertEqual(self.result(p,r)['decision'],'BLOCKED')
 def test_future_and_naive_dates_block(self):
  for dt in ['2099-01-01T00:00:00Z','2026-10-30T21:00:00','invalid',None]:
   p,r=fixture();r['created_at']=dt;self.assertEqual(self.result(p,r)['decision'],'BLOCKED')
 def test_unreviewed_gaps_block(self):
  p,r=fixture();r['coverage_gaps']=['unreviewed'];self.assertEqual(self.result(p,r)['decision'],'BLOCKED')
 def test_confirmed_high_not_verified_blocks(self):
  for status in ['Open','Fixed, verification pending','Accepted risk']:
   p,r=fixture();r['findings']=[{'id':'SEC-001','severity':'High','priority':'Normal','confidence':'Confirmed','status':status}];self.assertEqual(self.result(p,r)['decision'],'BLOCKED')
 def test_emergency_blocks_even_if_severity_low(self):
  p,r=fixture();r['findings']=[{'id':'SEC-001','severity':'Low','priority':'Emergency','confidence':'Likely','status':'Open'}];self.assertEqual(self.result(p,r)['decision'],'BLOCKED')
 def test_verified_fix_needs_evidence(self):
  p,r=fixture();r['findings']=[{'id':'SEC-001','severity':'High','priority':'Normal','confidence':'Confirmed','status':'Verified'}];self.assertEqual(self.result(p,r)['decision'],'BLOCKED')
 def test_verified_fix_still_requires_current_checks(self):
  p,r=fixture();r['findings']=[{'id':'SEC-001','severity':'High','priority':'Normal','confidence':'Confirmed','status':'Verified','verification_ref':'fixture:test','verification_snapshot':'fixture:abc'}];self.assertEqual(self.result(p,r)['decision'],'PASS')
 def test_false_positive_needs_reason_and_review(self):
  p,r=fixture();r['findings']=[{'id':'SEC-001','severity':'High','priority':'Normal','confidence':'Confirmed','status':'False positive'}];self.assertEqual(self.result(p,r)['decision'],'BLOCKED')
 def test_severe_unvalidated_candidate_needs_triage(self):
  p,r=fixture();r['findings']=[{'id':'SEC-001','severity':'High','priority':'Normal','confidence':'Needs validation','status':'Open'}];out=self.result(p,r);self.assertEqual(out['decision'],'BLOCKED');self.assertIn('triage_pending',out['reasons'])
 def test_independent_review_required(self):
  p,r=fixture();p['events']['module-complete']['require_independent_review']=True;r['policy_sha256']=gate.policy_hash(p);self.assertEqual(self.result(p,r)['decision'],'BLOCKED')
 def test_self_review_rejected(self):
  p,r=fixture();p['events']['module-complete']['require_independent_review']=True;r['policy_sha256']=gate.policy_hash(p)
  r['review']={'status':'PASS','snapshot':'fixture:abc','completed_at':STAMP,'evidence_ref':'fixture:review','author_execution_id':'same','reviewer_execution_id':'same'}
  self.assertEqual(self.result(p,r)['decision'],'BLOCKED')
 def test_required_backup_missing_blocks(self):
  p,r=fixture();p['events']['module-complete']['require_verified_backup']=True;r['policy_sha256']=gate.policy_hash(p);self.assertEqual(self.result(p,r)['decision'],'BLOCKED')
 def test_both_additional_gates_present(self):
  p,r=fixture();p['events']['module-complete'].update(require_independent_review=True,require_verified_backup=True);r['policy_sha256']=gate.policy_hash(p)
  r['review']={'status':'PASS','snapshot':'fixture:abc','completed_at':STAMP,'evidence_ref':'fixture:review','author_execution_id':'worker1','reviewer_execution_id':'worker2'}
  r['backup']={'status':'VERIFIED','snapshot':'fixture:abc','evidence_ref':'fixture:backup','archive_sha256':'a'*64}
  self.assertEqual(self.result(p,r)['decision'],'PASS')
 def test_accepted_low_risk_can_have_separate_future_review_date(self):
  p,r=fixture();r['findings']=[{'id':'SEC-002','severity':'Low','priority':'Deferred','confidence':'Confirmed','status':'Accepted risk','exception':{'owner':'fixture-owner','approval_ref':'fixture:approval','reason':'bounded risk','expires_at':'2026-11-30T21:00:00Z'}}]
  self.assertEqual(self.result(p,r)['decision'],'PASS')
 def test_expired_risk_exception_blocks(self):
  p,r=fixture();r['findings']=[{'id':'SEC-002','severity':'Low','priority':'Deferred','confidence':'Confirmed','status':'Accepted risk','exception':{'owner':'fixture-owner','approval_ref':'fixture:approval','reason':'bounded risk','expires_at':'2026-10-29T21:00:00Z'}}]
  self.assertEqual(self.result(p,r)['decision'],'BLOCKED')
 def test_release_requires_disposition_for_nonblocking_vulnerability(self):
  p,r=fixture();p['events']={'pre-release':p['events']['module-complete']};r.update(event='pre-release',policy_sha256=gate.policy_hash(p))
  r['findings']=[{'id':'SEC-003','severity':'Medium','priority':'Normal','confidence':'Confirmed','status':'Open'}]
  self.assertEqual(self.result(p,r,event='pre-release')['decision'],'BLOCKED')
 def test_informational_is_not_counted_as_release_vulnerability(self):
  p,r=fixture();p['events']={'pre-release':p['events']['module-complete']};r.update(event='pre-release',policy_sha256=gate.policy_hash(p))
  r['findings']=[{'id':'SEC-INFO','severity':'Informational','priority':'Deferred','confidence':'Confirmed','status':'Open'}]
  self.assertEqual(self.result(p,r,event='pre-release')['decision'],'PASS')
 def test_invalid_types_block_without_stacktrace(self):
  for value in [None,[],True,{}, {'schema_version':'1.0','enabled':True,'events':[]}]:
   self.assertEqual(self.result(value,{})['decision'],'BLOCKED')
 def test_json_duplicate_keys_rejected(self):
  with tempfile.TemporaryDirectory() as d:
   p=pathlib.Path(d)/'in.json';p.write_text('{"enabled":false,"enabled":true}')
   with self.assertRaises(ValueError):gate.read_json(p)
 def test_no_subprocess_or_network_imports(self):
  import ast
  tree=ast.parse(SCRIPT.read_text());imports=[]
  for node in ast.walk(tree):
   if isinstance(node,ast.Import):imports.extend(n.name.split('.')[0] for n in node.names)
   if isinstance(node,ast.ImportFrom):imports.append((node.module or '').split('.')[0])
  self.assertFalse(set(imports)&{'subprocess','socket','requests','urllib','http'})
 def test_cli_missing_receipt_is_nonzero_no_sensitive_echo(self):
  with tempfile.TemporaryDirectory() as d:
   path=pathlib.Path(d)/'policy.json';p,_=fixture();path.write_text(json.dumps(p))
   cp=subprocess.run([sys.executable,str(SCRIPT),'--policy',str(path),'--receipt',str(path.parent/'SENSITIVE_PATH'),'--event','module-complete','--snapshot','fixture:abc'],capture_output=True,text=True)
   self.assertNotEqual(cp.returncode,0);self.assertNotIn('SENSITIVE_PATH',cp.stdout+cp.stderr);self.assertEqual(json.loads(cp.stdout)['decision'],'BLOCKED')
if __name__=='__main__':unittest.main()
