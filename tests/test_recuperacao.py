import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import time
import unittest

ROOT = Path(__file__).resolve().parents[1]
MODULE = ROOT / "modulos/recuperacao"
ROLE = Path(".codex/agents/cadu_recuperacao.toml")


def sha(data):
    return hashlib.sha256(data).hexdigest()


# Test-only alternatives to the actual registered example recipe. Mutations occur
# only in the disposable fixture. The held-out check stays in the private driver.
WRAPPER = """
import sys, time
from pathlib import Path
import json
from fabrica import main
stage, recipe = sys.argv[1:]
if Path('externo-off').exists() and stage == 'probe':
    sys.exit(3)
if stage == 'repair':
    with Path('calls').open('a') as f:
        f.write(recipe+'\\n')
    if recipe == 'parcial':
        target = Path('docs/fabrica/routes.json')
        data = json.loads(target.read_text())
        data['routes']['recuperar'] = json.loads(Path('rota-canonica.json').read_text())
        target.write_text(json.dumps(data))
        sys.exit(0)
    if recipe == 'lento':
        Path('escrevendo').touch()
        time.sleep(20)
        Path('tardio').touch()
if stage == 'rollback_check':
    from hashlib import sha256
    def hash_state():
        return sha256(b''.join(Path('docs/fabrica', n).read_bytes() for n in ('routes.json','index.html'))).hexdigest()
    sys.exit(int(hash_state() != Path('referencia.sha').read_text()))
sys.exit(main(stage, recipe))
"""


class RecoveryTest(unittest.TestCase):
    def setUp(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        top = Path(tmp.name)
        self.root = top / "produto"
        self.control = top / "controle"
        self.root.mkdir()
        self.control.mkdir()
        subprocess.run(["git", "init", "-q", str(self.root)], check=True)
        for rel in ("scripts/build_factory.py", "scripts/prompt_factory.py", "fabrica/rotas.json",
                    "comandos/ASSUMIR_PROJETO.md", "comandos/REESTRUTURAR_PROJETO.md", "docs/assets/factory.js", "read.md"):
            dest = self.root / rel
            dest.parent.mkdir(exist_ok=True, parents=True)
            shutil.copyfile(ROOT / rel, dest)
        (self.root / "docs/comandos").mkdir(parents=True)
        subprocess.run([sys.executable, "scripts/build_factory.py"], cwd=self.root,
                       capture_output=True, check=True)
        self.output = self.root / "docs/fabrica"
        (self.root / "rota-canonica.json").write_text(json.dumps(json.loads((self.output / "routes.json").read_text())["routes"]["recuperar"]))
        subprocess.run(["git", "-C", str(self.root), "add", "."], check=True)
        subprocess.run(["git", "-C", str(self.root), "-c", "user.name=QA", "-c", "user.email=qa@example.invalid",
                        "commit", "-qm", "ensaio"], check=True)
        # Embed the example into the digest-pinned driver, keeping the holdout
        # outside the worktree. No imports from mutable application code here.
        example = (MODULE / "exemplos/fabrica.py").read_text().split('if __name__ == "__main__":')[0]
        driver = self.control / "procedimento.py"
        driver.write_text(example + WRAPPER.replace("from fabrica import main", ""))
        self.profile = self.control / "perfil.json"
        self.cfg = dict(projeto="app", caso="fabrica", ambiente="ensaio-descartavel",
                        worktree=str(self.root), receitas=["parcial", "regenerar", "lento"],
                        tentativas=3, segundos=12, sha256_procedimento=sha(driver.read_bytes()))
        if shutil.which("node"):
            node = Path(shutil.which("node")).resolve()
            self.cfg["node"] = {"caminho": str(node), "sha256": sha(node.read_bytes())}
        self.set_profile()
        self.inject()

    def set_profile(self):
        self.profile.write_text(json.dumps(self.cfg))
        self.policy = sha(self.profile.read_bytes())

    def inject(self):
        routes = self.output / "routes.json"
        data = json.loads(routes.read_text())
        data["routes"].pop("recuperar", None)
        routes.write_text(json.dumps(data))
        page = self.output / "index.html"
        page.write_text(page.read_text().replace('value="recuperar"', 'value="erro"'))
        (self.root / "referencia.sha").write_text(sha(routes.read_bytes() + page.read_bytes()))

    def args(self, mission="primeira", evidence="f1", recipe=None, reconcile=False):
        args = [sys.executable, str(MODULE / "recuperar.py"), "--perfil", str(self.profile),
                "--sha256", self.policy, "--missao", mission, "--evidencia", sha(evidence.encode())]
        if recipe:
            args.extend(["--candidata", recipe])
        if reconcile:
            args.append("--reconciliar")
        return args

    def run_worker(self, **kwargs):
        proc = subprocess.run(self.args(**kwargs), capture_output=True, text=True, timeout=20)
        return json.loads(proc.stdout)

    def test_compare_learn_and_recall_in_fresh_process(self):
        partial = self.run_worker(recipe="parcial")
        self.assertEqual(partial["estado"], "REJECTED")
        self.assertEqual(partial["verificacoes"], {"referencia": 1, "repair": 0, "probe": 0, "holdout": 1})
        self.assertEqual(self.run_worker()["estado"], "RECONCILE")
        self.assertEqual(self.run_worker(reconcile=True)["estado"], "RECONCILE")
        self.inject()
        self.assertEqual(self.run_worker(reconcile=True)["estado"], "ROLLED_BACK")
        self.assertEqual(self.run_worker(mission="outra")["estado"], "BLOCKED_REPEAT")
        fixed = self.run_worker(recipe="regenerar", evidence="f2")
        self.assertEqual(fixed["estado"], "VERIFIED")
        self.assertEqual(fixed["origem"], "candidata")
        self.assertEqual(self.run_worker()["estado"], "ALREADY_PASS")
        self.inject()
        reused = self.run_worker(mission="segunda", evidence="f2")
        self.assertEqual((reused["estado"], reused["origem"], reused["receita"]),
                         ("VERIFIED", "memoria", "regenerar"))
        self.assertEqual((self.root / "calls").read_text().splitlines(), ["parcial", "regenerar", "regenerar"])
        self.inject()
        self.cfg["segundos"] += 1
        self.set_profile()
        self.assertEqual(self.run_worker(mission="terceira", evidence="f3")["origem"], "candidata")

    def test_external_dependency_and_healthy_idempotence(self):
        (self.root / "externo-off").touch()
        self.assertEqual(self.run_worker()["estado"], "BLOCKED_DEPENDENCY")
        self.assertFalse((self.root / "calls").exists())
        (self.root / "externo-off").unlink()
        self.assertEqual(self.run_worker(recipe="regenerar")["estado"], "VERIFIED")
        self.assertEqual(self.run_worker()["estado"], "ALREADY_PASS")
        self.assertEqual((self.root / "calls").read_text().splitlines(), ["regenerar"])

    def test_budget_across_attempts_and_renamed_mission(self):
        self.cfg["tentativas"] = 1
        self.set_profile()
        self.assertEqual(self.run_worker(recipe="parcial")["estado"], "REJECTED")
        self.inject()
        self.assertEqual(self.run_worker(reconcile=True)["estado"], "ROLLED_BACK")
        self.assertEqual(self.run_worker(evidence="nova")["estado"], "BUDGET_EXHAUSTED")
        self.assertEqual(self.run_worker(mission="outro", evidence="nova")["estado"], "BUDGET_EXHAUSTED")

    def test_stop_lock_reconcile_before_next_writer(self):
        proc = subprocess.Popen(self.args(recipe="lento"), stdout=subprocess.PIPE, text=True)
        try:
            until = time.monotonic() + 8
            while not (self.root / "escrevendo").exists():
                self.assertIsNone(proc.poll())
                self.assertLess(time.monotonic(), until)
                time.sleep(0.02)
            self.assertEqual(self.run_worker()["estado"], "BUSY")
            (self.control / "STOP").touch()
            self.assertEqual(json.loads(proc.communicate(timeout=3)[0])["estado"], "PAUSED")
        finally:
            if proc.poll() is None:
                proc.kill()
                proc.communicate()
        (self.control / "STOP").unlink()
        self.assertEqual(self.run_worker()["estado"], "RECONCILE")
        self.cfg["caso"] = "outro"
        self.set_profile()
        self.assertEqual(self.run_worker(reconcile=True)["estado"], "RECONCILE")
        self.cfg["caso"] = "fabrica"
        self.set_profile()
        self.assertEqual(self.run_worker(reconcile=True)["estado"], "ROLLED_BACK")
        self.assertEqual(self.run_worker(reconcile=True)["estado"], "NOT_PENDING")
        self.assertFalse((self.root / "tardio").exists())
        self.assertEqual((self.root / "calls").read_text().splitlines(), ["lento"])

    def test_blocked_resource_still_allows_independent_product(self):
        (self.root / "externo-off").touch()
        self.assertEqual(self.run_worker()["estado"], "BLOCKED_DEPENDENCY")
        other = self.root.parent / "segundo-produto"
        shutil.copytree(self.root, other)
        (other / "externo-off").unlink()
        self.control = self.root.parent / "controle-separado"
        self.control.mkdir()
        shutil.copyfile(self.profile.parent / "procedimento.py", self.control / "procedimento.py")
        self.profile = self.control / "perfil.json"
        self.cfg.update(projeto="segundo-produto", worktree=str(other))
        self.set_profile()
        self.assertEqual(self.run_worker(recipe="regenerar")["estado"], "VERIFIED")
        self.assertFalse((self.root / "calls").exists())

    def test_portfolio_diagnostics_are_read_only_and_report_gates_separately(self):
        subprocess.run(["git", "-C", str(self.root), "add", "--", "fabrica"], check=True)
        cli = [sys.executable, str(MODULE / "diagnostico.py")]
        args = ["git", "-C", str(self.root), "status", "--porcelain=v1", "-z"]
        before = subprocess.check_output(args)
        data = json.loads(subprocess.check_output(cli + ["coletar", str(self.root)]))
        self.assertEqual(data["hostinger_remoto"], "NAO_VERIFICADO")
        self.assertFalse(data["sinais_versionados"]["docker"])
        self.assertEqual(set(data["gates"]), {"local", "ci", "staging", "harness", "release"})
        report = self.control / "relato.json"
        report.write_text(json.dumps(data))
        summary = subprocess.check_output(cli + ["consolidar", str(report)], text=True)
        self.assertIn("Projetos recebidos: 1", summary)
        self.assertEqual(subprocess.check_output(args), before)

    def test_broken_template_is_repaired_and_new_head_invalidates_memory(self):
        self.assertEqual(self.run_worker(recipe="regenerar")["estado"], "VERIFIED")
        routes = self.output / "routes.json"
        data = json.loads(routes.read_text())
        data["routes"]["recuperar"] = {}
        routes.write_text(json.dumps(data))
        self.assertEqual(self.run_worker(mission="segunda", evidence="f2")["estado"], "VERIFIED")
        subprocess.run(["git", "-C", str(self.root), "-c", "user.name=QA", "-c", "user.email=qa@example.invalid",
                        "commit", "--allow-empty", "-qm", "outro commit"], check=True)
        self.inject()
        result = self.run_worker(mission="terceira", evidence="f3")
        self.assertEqual(result["origem"], "candidata")
        self.assertEqual(result["receita"], "parcial")

    def test_portfolio_rejects_unknown_gate_or_blank_proof(self):
        cli = [sys.executable, str(MODULE / "diagnostico.py")]
        data = json.loads(subprocess.check_output(cli + ["coletar", str(self.root)]))
        report = self.control / "relato.json"
        for state in ("APROVADO_EM_PRODUCAO", "PASS"):
            data["gates"]["release"] = {"estado": state, "evidencia": "  "}
            report.write_text(json.dumps(data))
            self.assertEqual(subprocess.run(cli + ["consolidar", str(report)], capture_output=True).returncode, 2)

    def test_deadline_and_integrity(self):
        self.cfg["segundos"] = 1
        self.set_profile()
        self.assertEqual(self.run_worker(recipe="lento")["estado"], "TIMEOUT")
        self.assertEqual(self.run_worker()["estado"], "RECONCILE")
        self.profile.write_text(self.profile.read_text() + " ")
        self.assertEqual(self.run_worker()["estado"], "INVALID")
        self.set_profile()
        (self.control / "procedimento.py").write_text("raise AssertionError")
        self.assertEqual(self.run_worker()["estado"], "INVALID")

    def test_activation_persists_without_overwriting_project_rules(self):
        rules = self.root / "AGENTS.md"
        original = b"Regra existente com acento UTF-8: " + "produção".encode()
        rules.write_bytes(original)
        fixture = self.control / "central"
        for filename in (ROLE, Path("comando.md"), Path("modulos/recuperacao/adotar.py")):
            (fixture / filename).parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(ROOT / filename, fixture / filename)
        subprocess.run(["git", "init", "-q", str(fixture)], check=True)
        subprocess.run(["git", "-C", str(fixture), "add", "."], check=True)
        commit = ["git", "-C", str(fixture), "-c", "user.name=QA", "-c", "user.email=qa@example.invalid",
                  "commit", "-qm"]
        subprocess.run(commit + ["central"], check=True)
        revision = subprocess.check_output(["git", "-C", str(fixture), "rev-parse", "HEAD"], text=True).strip()
        cmd = [sys.executable, str(fixture / "modulos/recuperacao/adotar.py"), str(self.root), "--ativar-na-revisao", revision]
        self.assertEqual(subprocess.check_output(cmd, text=True).strip(), "ATIVO")
        after = rules.read_bytes()
        self.assertTrue(after.startswith(original))
        self.assertIn(b"cadu_recuperacao", after)
        self.assertIn(b"/" + revision.encode() + b"/comando.md", after)
        self.assertEqual(subprocess.check_output(cmd, text=True).strip(), "JA_ATIVO")
        self.assertEqual(after, rules.read_bytes())
        cmd[-1] = "b" * 40
        self.assertEqual(subprocess.run(cmd, capture_output=True).returncode, 2)
        self.assertEqual(after, rules.read_bytes())

        subprocess.run(commit + ["segunda", "--allow-empty"], check=True)
        cmd[-1] = subprocess.check_output(["git", "-C", str(fixture), "rev-parse", "HEAD"], text=True).strip()
        self.assertEqual(subprocess.check_output(cmd, text=True).strip(), "ATIVO")
        self.assertTrue(rules.read_bytes().startswith(original))
        (fixture / ROLE).write_text("papel alterado")
        self.assertEqual(subprocess.run(cmd, capture_output=True).returncode, 2)

    def test_install_is_idempotent_and_preserves_existing_agent(self):
        cmd = [sys.executable, str(MODULE / "adotar.py"), str(self.root)]
        invoke = lambda: subprocess.run(cmd, capture_output=True, text=True)
        self.assertEqual(invoke().stdout.strip(), "ADOTADO")
        self.assertEqual(invoke().stdout.strip(), "JA_ADOTADO")
        installed = self.root / ROLE
        self.assertEqual(installed.read_bytes(), (ROOT / ROLE).read_bytes())
        installed.write_text("personalizado")
        self.assertEqual(invoke().returncode, 2)
        self.assertEqual(installed.read_text(), "personalizado")
        shutil.rmtree(self.root / ".codex")
        (self.root / ".codex").symlink_to(self.control, target_is_directory=True)
        self.assertEqual(invoke().returncode, 2)
        self.assertFalse((self.control / "agents").exists())


if __name__ == "__main__":
    unittest.main()
