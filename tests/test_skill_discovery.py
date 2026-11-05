import unittest
from pathlib import Path
R=Path(__file__).resolve().parents[1]
class SkillDiscoveryContracts(unittest.TestCase):
 def test_module_and_sources_exist(self):
  for p in ['modulos/descoberta-skills/README.md','modulos/descoberta-skills/read.md','modulos/descoberta-skills/FONTES.md']:
   self.assertTrue((R/p).exists(),p)
 def test_p08_and_p22_use_controlled_discovery(self):
  p08=(R/'p/P08.md').read_text();p22=(R/'p/P22.md').read_text()
  for x in ['npx skills find','D01','P22']:self.assertIn(x,p08)
  for x in ['D01/Find Skills','telemetria','skills check']:self.assertIn(x,p22)
 def test_three_languages_explain_discovery(self):
  checks={'README.md':'Descoberta de skills','i18n/README.en.md':'Skill discovery','i18n/README.es.md':'Descubrimiento de skills'}
  for p,label in checks.items():
   text=(R/p).read_text();self.assertIn(label,text);self.assertIn('npx skills find',text)
 def test_pinned_upstream_revision(self):
  text=(R/'modulos/descoberta-skills/FONTES.md').read_text()+(R/'fontes/FONTES_E_REVISOES.md').read_text()
  self.assertIn('9197d919034d19010ae303cf96bf19ad087dd4be',text)
if __name__=='__main__':unittest.main()
