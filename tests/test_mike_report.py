import importlib.util
import json
import os
from pathlib import Path
import tempfile
import unittest

SPEC = importlib.util.spec_from_file_location('mike_report', Path(__file__).resolve().parents[1]/'scripts/mike_report.py')
m = importlib.util.module_from_spec(SPEC); SPEC.loader.exec_module(m)

class MikeReportTests(unittest.TestCase):
    def test_missing_is_unknown_not_running_or_free(self):
        with tempfile.TemporaryDirectory() as d:
            r=m.report(d, now=100)
            self.assertEqual(r['heartbeat_status'], 'UNKNOWN')
            self.assertIsNone(r['observed_tokens']['prompt'])
            self.assertEqual(list(Path(d).iterdir()), [])

    def test_stale_and_review_are_not_live_or_accepted(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d);(p/'receipts').mkdir()
            (p/'heartbeat.json').write_text(json.dumps({'at':1,'status':'RUNNING','pid':123}))
            (p/'receipts/a.json').write_text(json.dumps({'status':'REVIEW_REQUIRED','tokens':{'prompt_eval_count':12,'eval_count':7}}))
            before={str(f):f.read_bytes() for f in p.rglob('*.json')}
            r=m.report(d,now=100)
            self.assertEqual(r['heartbeat_status'],'STALE')
            self.assertIsNone(r['accepted_count'])
            self.assertEqual(r['observed_tokens']['prompt'],12)
            self.assertEqual(before,{str(f):f.read_bytes() for f in p.rglob('*.json')})

    def test_corrupt_receipt_makes_coverage_partial(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d);(p/'receipts').mkdir()
            (p/'heartbeat.json').write_text(json.dumps({'at':99,'status':'IDLE'}))
            (p/'receipts/a.json').write_text(json.dumps({'status':'FAILED','tokens':{'prompt_eval_count':1,'eval_count':2}}))
            (p/'receipts/b.json').write_text('bad')
            self.assertEqual(m.report(d,now=100)['token_coverage'],'PARTIAL')

    def test_fifo_and_invalid_status_rejected(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)
            os.mkfifo(p/'heartbeat.json')
            self.assertEqual(m.report(d,now=100)['heartbeat_status'],'UNKNOWN')
            (p/'heartbeat.json').unlink()
            (p/'heartbeat.json').write_text(json.dumps({'at':99,'status':'APPROVED'}))
            self.assertEqual(m.report(d,now=100)['heartbeat_status'],'UNKNOWN')
