import importlib.util
from pathlib import Path
import subprocess
import unittest
s=importlib.util.spec_from_file_location('maintenance',Path(__file__).resolve().parents[1]/'scripts/autonomous_maintenance.py');m=importlib.util.module_from_spec(s);s.loader.exec_module(m)
class Tests(unittest.TestCase):
 def config(self):return {'version':1,'enabled':True,'max_tasks':3,'timeout_seconds':10,'tasks':[{'id':'a','action':'queue_check','depends_on':[]},{'id':'b','action':'editorial_check','depends_on':['a']},{'id':'c','action':'project_audit','depends_on':[]}]}
 def test_dependencies_and_independent_work(self):
  calls=[]
  def runner(cmd,**kw):calls.append(cmd);return subprocess.CompletedProcess(cmd,1 if len(calls)==1 else 0,'{"schema_version":1}' if len(calls)>1 else 'secret-not-exported','')
  x=m.run(self.config(),runner=runner);self.assertEqual([t['status'] for t in x['tasks']],['FAIL','BLOCKED','PASS']);self.assertEqual(len(calls),2);self.assertNotIn('secret-not-exported',str(x))
 def test_pass_once(self):
  calls=[]
  def runner(cmd,**kw):calls.append(cmd);return subprocess.CompletedProcess(cmd,0,'{"schema_version":1}','')
  x=m.run(self.config(),runner=runner);self.assertEqual(x['status'],'PASS');self.assertEqual(len(calls),3)
 def test_stop(self):self.assertEqual(m.run(self.config(),stop=lambda:True)['status'],'STOPPED')
 def test_disabled(self):
  c=self.config();c['enabled']=False;self.assertEqual(m.run(c)['status'],'STOPPED')
 def test_injection_cycle_budget(self):
  for change in ('action','cycle','budget','extra'):
   c=self.config()
   if change=='action':c['tasks'][0]['action']='shell; rm -rf'
   if change=='cycle':c['tasks'][0]['depends_on']=['b']
   if change=='budget':c['max_tasks']=1
   if change=='extra':c['tasks'][0]['command']='echo unsafe'
   with self.subTest(change=change),self.assertRaises(ValueError):m.validate(c)
 def test_timeout(self):
  def runner(cmd,**kw):raise subprocess.TimeoutExpired(cmd,1)
  x=m.run(self.config(),runner=runner);self.assertEqual(x['status'],'FAIL');self.assertEqual(x['tasks'][0]['reason'],'TIMEOUT')

 def test_deadline_exhaustion_is_failure(self):
  now=[0]
  def runner(cmd,**kw):
   now[0]=11
   raise subprocess.TimeoutExpired(cmd,10)
  x=m.run(self.config(),runner=runner,clock=lambda:now[0])
  self.assertEqual(x['status'],'FAIL');self.assertEqual(x['reason'],'DEADLINE_EXHAUSTED')
  self.assertEqual(len(x['tasks']),1)
