"""Checks documentation/site consistency, not live agents or app security."""
import hashlib,json,re,unittest
from pathlib import Path
from html.parser import HTMLParser
R=Path(__file__).resolve().parents[1]
GUIDES={'continuidade':'politicas/CONTINUIDADE.md','seguranca':'politicas/SEGURANCA_ENGENHARIA.md','backup':'politicas/BACKUP_DRIVE.md','operacao':'OPERACAO.md'}
class Page(HTMLParser):
 def __init__(self):super().__init__();self.sources={};self.h1=0
 def handle_starttag(self,t,a):
  d=dict(a)
  if t=='h1':self.h1+=1
  if 'data-source' in d:self.sources[d['data-source']]=d.get('data-source-sha256')
class OrganizationTests(unittest.TestCase):
 def test_four_guides_are_linked_from_home(self):
  s=(R/'docs/index.html').read_text()
  for slug in GUIDES:
   with self.subTest(slug=slug):self.assertIn(f'guia/{slug}/',s)
 def test_guides_match_canonical_source_hash(self):
  for slug,src in GUIDES.items():
   with self.subTest(slug=slug):
    p=Page();p.feed((R/f'docs/guia/{slug}/index.html').read_text())
    self.assertEqual(p.sources[src],hashlib.sha256((R/src).read_bytes()).hexdigest());self.assertEqual(p.h1,1)
 def test_index_connects_all_policies(self):
  s=(R/'MAPA_DA_CENTRAL.md').read_text()
  for src in GUIDES.values():self.assertIn(src,s)
 def test_start_command_has_continuity(self):
  s=(R/'docs/index.html').read_text();self.assertIn('CONTINUO_SUPERVISIONADO',s);self.assertIn('P01.md',s)
 def test_p01_keeps_complete_copyable_body(self):
  s=(R/'docs/prompts/P01/index.html').read_text();self.assertIn('id="full-command"',s);self.assertIn('data-copy-target="full-command"',s)
 def test_security_template_is_not_report(self):
  s=(R/'templates/REVISAO_SEGURANCA.md').read_text();self.assertIn('NOT_RUN',s);self.assertIn('independente',s)
 def test_backup_receipt_records_coverage(self):
  s=(R/'templates/RECIBO_BACKUP.md').read_text()
  for term in ['SHA-256','exclus','histórico','restauração']:self.assertIn(term,s)
 def test_operational_status_is_explicit(self):
  s=(R/'OPERACAO.md').read_text()
  for term in ['NÃO IMPLANTADO','backup','24 horas','NOT_RUN']:self.assertIn(term,s)
if __name__=='__main__':unittest.main()
