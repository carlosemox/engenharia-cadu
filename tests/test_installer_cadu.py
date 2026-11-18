import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

HERE=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location("install_cadu",HERE/"scripts/install_claude_cadu.py")
mod=importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

class CaduInstallerTests(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.dest=Path(self.temp.name)/"claude"
    def test_install_check_remove_idempotent(self):
        src=HERE
        r=mod.audit(src,self.dest,"check")
        self.assertTrue(all(x["status"]=="MISSING" for x in r),r)
        r=mod.audit(src,self.dest,"apply")
        self.assertTrue(all(x["status"]=="INSTALLED" for x in r),r)
        self.assertTrue(all(x["status"]=="INSTALLED" for x in mod.audit(src,self.dest,"check")))
        self.assertTrue(all(x["status"]=="INSTALLED" for x in mod.audit(src,self.dest,"apply")))
        self.assertTrue(all(x["status"]=="REMOVED" for x in mod.audit(src,self.dest,"remove")))
        self.assertTrue(all(x["status"]=="MISSING" for x in mod.audit(src,self.dest,"check")))
    def test_preserves_collision_and_other_settings(self):
        self.dest.mkdir()
        (self.dest/"settings.json").write_text('{"enabledPlugins":{"ecc@ecc":true}}')
        (self.dest/"skills").mkdir()
        occupied=self.dest/"skills"/"cadu-mike"
        occupied.mkdir()
        (occupied/"SKILL.md").write_text("KEEP")
        r=mod.audit(HERE,self.dest,"apply")
        self.assertTrue(any(x["item"]=="cadu-mike" and x["status"]=="CONFLICT_PRESERVED" for x in r))
        self.assertEqual((occupied/"SKILL.md").read_text(),"KEEP")
        self.assertEqual((self.dest/"settings.json").read_text(),'{"enabledPlugins":{"ecc@ecc":true}}')
        mod.audit(HERE,self.dest,"remove")
        self.assertEqual((occupied/"SKILL.md").read_text(),"KEEP")
    def test_policy_p13_not_p06(self):
        policy=(HERE/"politicas/UNTANGLE_CLAUDE_SLICES.md").read_text()
        self.assertIn("P13 implementa", policy)
        contract=json.loads((HERE/"templates/MIKE_SLICE_CONTRACT.json").read_text())
        self.assertIn("p13_approved",contract["authorization"])
        self.assertNotIn("p06_approved",contract["authorization"])
        self.assertFalse(contract["authorization"]["p13_approved"])
    def test_portuguese_skills_and_nonwriting_reviewers(self):
        for name in mod.SKILLS:
            s=(HERE/".claude/skills"/name/"SKILL.md").read_text()
            self.assertTrue(s.startswith("---\n"))
            self.assertIn("description:",s)
        for name in ("cadu-scout","cadu-architect","cadu-slice-reviewer","cadu-security-gate"):
            s=(HERE/".claude/agents"/(name+".md")).read_text()
            self.assertNotIn("Edit, ",s)
            self.assertNotIn("Bash",s)

if __name__ == "__main__":
    unittest.main()
