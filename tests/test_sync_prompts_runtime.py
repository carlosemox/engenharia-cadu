import subprocess,sys,unittest
from pathlib import Path
R=Path(__file__).resolve().parents[1]
class SyncPromptRuntime(unittest.TestCase):
 def test_sync_completes_for_p00_to_p30(self):
  p=subprocess.run([sys.executable,str(R/'scripts/sync_prompts.py')],cwd=R,capture_output=True,text=True)
  self.assertEqual(p.returncode,0,p.stderr+p.stdout)
if __name__=='__main__':unittest.main()
