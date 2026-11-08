import copy
import importlib.util
import json
import unittest
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('supervisor',ROOT/'scripts/supervisor.py')
s=importlib.util.module_from_spec(spec);spec.loader.exec_module(s)

class SupervisorTests(unittest.TestCase):
    def setUp(self):
        self.r=json.loads((ROOT/'catalogo/esquadroes.json').read_text())
        self.q=s.load_queue(ROOT/'docs/harness/TASK_QUEUE.md')
        t=copy.deepcopy(self.q['tasks'][0]);t.update(status='READY',authorized=True,evidence=[],review=None,attempts=0,no_progress=0,depends_on=[])
        self.q['tasks']=[t];self.t=t
    def test_read_only_selection(self):
        before=copy.deepcopy(self.q)
        self.assertEqual(s.select_next(self.q,self.r)['status'],'CANDIDATE')
        self.assertEqual(before,self.q)
    def test_self_review(self):
        self.t['reviewer_id']=self.t['executor_id'];self.assertTrue(s.validate(self.q,self.r))
    def test_scope(self):
        self.t.update(role='frame',squad='dashboard',allowed_paths=['migrations/'])
        self.assertTrue(s.validate(self.q,self.r))
    def test_traversal_and_protected(self):
        for p in ['../db','/tmp/x','docs/../db','.git/config','.env','docs/.env.local','C:/x','docs\\x','docs//x']:
            with self.subTest(path=p),self.assertRaises(ValueError):s.clean_path(p)
    def test_prefix_boundary(self):
        self.assertFalse(s.within('docs-other/x','docs/'))
    def test_unknown_dependency(self):
        self.t['depends_on']=['missing'];self.assertTrue(s.validate(self.q,self.r))
    def test_cycle(self):
        self.t['depends_on']=[self.t['id']];self.assertTrue(s.validate(self.q,self.r))
    def test_stop(self):
        self.q['stop_requested']=True;self.assertEqual(s.select_next(self.q,self.r)['status'],'STOPPED')
    def test_boolean_flags(self):
        self.q['stop_requested']='false';self.assertTrue(s.validate(self.q,self.r))
    def test_retry(self):
        self.t['attempts']=3;self.assertTrue(s.validate(self.q,self.r))
    def test_no_progress(self):
        self.t['no_progress']=2;self.assertTrue(s.validate(self.q,self.r))
    def test_no_authority(self):
        self.t['authorized']=False;self.assertTrue(s.validate(self.q,self.r))
    def test_done_requires_receipt(self):
        self.t['status']='DONE';self.assertTrue(s.validate(self.q,self.r))
    def test_done_with_declared_receipt(self):
        self.t.update(status='DONE',evidence=['test-log'],review={'reviewer_id':self.t['reviewer_id'],'result':'PASS','snapshot':'a'*40})
        self.assertEqual(s.validate(self.q,self.r),[])
    def test_unknown_role(self):
        self.t['role']='imaginary-agent';self.assertTrue(s.validate(self.q,self.r))
    def test_wait_review(self):
        self.t['status']='IN_REVIEW';self.assertEqual(s.select_next(self.q,self.r)['status'],'WAITING_REVIEW_OR_WORK')
    def test_malformed_dependency(self):
        self.t['depends_on']=[{}];self.assertTrue(s.validate(self.q,self.r))
    def test_duplicate_ids(self):
        self.q['tasks'].append(copy.deepcopy(self.t));self.assertTrue(s.validate(self.q,self.r))

    def test_malformed_roots(self):
        for value in [[], None, 5]:self.assertTrue(s.validate(value,self.r))
    def test_malformed_required_fields(self):
        for key,value in [('executor_id',{'x':1}),('reviewer_id',['x']),('acceptance',True),('outputs',True),('owner',' ')]:
            q=copy.deepcopy(self.q);q['tasks'][0][key]=value
            self.assertTrue(s.validate(q,self.r),key)
    def test_malformed_evidence(self):
        self.t.update(status='DONE',evidence=True,review={'reviewer_id':self.t['reviewer_id'],'result':'PASS','snapshot':'a'*40})
        self.assertTrue(s.validate(self.q,self.r))
    def test_double_trailing_slash(self):
        with self.assertRaises(ValueError):s.clean_path('docs//')

if __name__=='__main__':unittest.main()
