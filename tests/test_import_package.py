import hashlib, importlib.util, json, tempfile, unittest, zipfile
from pathlib import Path
SPEC=importlib.util.spec_from_file_location('import_package',Path(__file__).parents[1]/'scripts/import_package.py')
mod=importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(mod)
class ImportTests(unittest.TestCase):
 def setUp(self):
  self.temp=tempfile.TemporaryDirectory();self.base=Path(self.temp.name);self.root=self.base/'repo';self.root.mkdir()
 def tearDown(self):self.temp.cleanup()
 def archive(self,files,extra=None):
  p=self.base/'package.zip';manifest={n:hashlib.sha256(b).hexdigest() for n,b in files.items()}
  with zipfile.ZipFile(p,'w') as z:
   for n,b in files.items():z.writestr('repo/'+n,b)
   z.writestr('repo/MANIFEST_SHA256.json',json.dumps(manifest))
   for n,b in (extra or {}).items():z.writestr(n,b)
  return p,hashlib.sha256(p.read_bytes()).hexdigest()
 def test_valid_import_preserves_other_files(self):
  (self.root/'existing.md').write_text('preserve');p,h=self.archive({'README.md':b'hello'})
  paths=mod.import_package(p,h,self.root,'repo');self.assertEqual((self.root/'README.md').read_text(),'hello');self.assertEqual((self.root/'existing.md').read_text(),'preserve');self.assertEqual(len(paths),2)
 def test_wrong_hash(self):
  p,h=self.archive({'README.md':b'hello'})
  with self.assertRaises(ValueError):mod.import_package(p,'0'*64,self.root,'repo')
  self.assertFalse((self.root/'README.md').exists())
 def test_path_traversal(self):
  p,h=self.archive({'../outside':b'bad'})
  with self.assertRaises(ValueError):mod.import_package(p,h,self.root,'repo')
 def test_no_workflow_injection(self):
  p,h=self.archive({'.github/workflows/write.yml':b'bad'})
  with self.assertRaises(ValueError):mod.import_package(p,h,self.root,'repo')
 def test_unlisted_file_rejected(self):
  p,h=self.archive({'README.md':b'ok'},{'repo/extra.txt':b'bad'})
  with self.assertRaises(ValueError):mod.import_package(p,h,self.root,'repo')
 def test_other_repo_rejected(self):
  p,h=self.archive({'README.md':b'ok'},{'other/README.md':b'bad'})
  with self.assertRaises(ValueError):mod.import_package(p,h,self.root,'repo')
 def test_symlink_destination_rejected(self):
  outside=self.base/'outside';outside.mkdir();(self.root/'docs').symlink_to(outside,target_is_directory=True);p,h=self.archive({'docs/index.html':b'bad'})
  with self.assertRaises(ValueError):mod.import_package(p,h,self.root,'repo')
 def test_tampered_manifest(self):
  p=self.base/'bad.zip'
  with zipfile.ZipFile(p,'w') as z:z.writestr('repo/README.md','ok');z.writestr('repo/MANIFEST_SHA256.json',json.dumps({'README.md':'0'*64}))
  with self.assertRaises(ValueError):mod.import_package(p,hashlib.sha256(p.read_bytes()).hexdigest(),self.root,'repo')
if __name__=='__main__':unittest.main()
