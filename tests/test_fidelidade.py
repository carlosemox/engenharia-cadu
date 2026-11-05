import hashlib
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

SCRIPT = Path(__file__).resolve().parents[1] / "modulos/recuperacao/verificar_entrega.py"
SHA = "b" * 40


def digest(data):
    return hashlib.sha256(data).hexdigest()


class FidelityTests(unittest.TestCase):
    def setUp(self):
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        self.root = Path(temp.name)
        self.spec = self.root / "spec.md"
        self.spec.write_text("R1 autenticar. R2 publicar. R3 trabalhar localmente.")
        self.contract = {"projeto": "app", "fonte": "spec.md", "fonte_sha256": digest(self.spec.read_bytes()),
                         "criterios": [{"id": k, "aceite": k + " exercitado", "ambiente": "ensaio", "depende": deps}
                                       for k, deps in [("R1", []), ("R2", ["R1"]), ("R3", [])]]}
        self.log = self.root / "prova"
        self.log.write_text(json.dumps({"projeto": "app", "revisao": SHA, "ambiente": "ensaio",
                                        "origem": "ensaio sintético 001",
                                        "verificacoes": dict.fromkeys(("R1", "R2", "R3"), "PASS")}))
        self.receipt = {"id": "R1", "arquivo": "prova", "estado": "PASS", "sha256": digest(self.log.read_bytes()),
                        "revisao": SHA, "ambiente": "ensaio"}

    def evaluate(self, rows):
        path = self.root / "contrato"
        path.write_text(json.dumps(self.contract))
        expected = digest(path.read_bytes())
        receipts = self.root / "recibos"
        receipts.write_text(json.dumps({"projeto": "app", "revisao": SHA, "contrato_sha256": expected, "recibos": rows}))
        run = subprocess.run([sys.executable, str(SCRIPT), "--contrato", str(path), "--sha256-contrato", expected,
                              "--recibos", str(receipts), "--revisao", SHA], text=True, capture_output=True)
        data = json.loads(run.stdout)
        self.assertEqual(run.returncode, 0 if data["estado"] == "COBERTO_POR_RECIBOS" else 2)
        return data

    def test_missing_dependency_leaves_independent_work(self):
        actual = json.loads(self.log.read_text())
        actual["verificacoes"]["R1"] = "BLOCKED"
        self.log.write_text(json.dumps(actual))
        self.receipt["sha256"] = digest(self.log.read_bytes())
        result = self.evaluate([dict(self.receipt, estado="BLOCKED"), dict(self.receipt, id="R2")])
        self.assertEqual(result["criterios"], {"R1": "BLOCKED", "R2": "DEPENDE", "R3": "SEM_PROVA"})
        self.assertEqual(result["proximos"], ["R3"])

    def test_only_complete_set_reconciles(self):
        self.assertEqual(self.evaluate([self.receipt])["estado"], "PARCIAL")
        rows = [dict(self.receipt, id=k) for k in ("R1", "R2", "R3")]
        self.assertEqual(self.evaluate(rows)["estado"], "COBERTO_POR_RECIBOS")

    def test_rejects_stale_extra_and_tampered_evidence(self):
        for edit in ({"id": "inventado"}, {"estado": "FAIL"}, {"revisao": "a" * 40}, {"ambiente": "prod"}, {"arquivo": "../prova"},
                     {"arquivo": "spec.md", "sha256": self.contract["fonte_sha256"]}, {"sha256": "0" * 64}):
            with self.subTest(edit=edit):
                self.assertEqual(self.evaluate([dict(self.receipt, **edit)])["estado"], "INVALIDO")
        self.log.write_text("outro conteúdo")
        self.assertEqual(self.evaluate([self.receipt])["estado"], "INVALIDO")

    def test_rejects_reference_drift_duplicate_and_cycle(self):
        self.assertEqual(self.evaluate([self.receipt, self.receipt])["estado"], "INVALIDO")
        self.contract["criterios"][0]["depende"] = ["R2"]
        self.assertEqual(self.evaluate([])["estado"], "INVALIDO")
        self.contract["criterios"][0]["depende"] = []
        self.spec.write_text("uma especificação diferente")
        self.assertEqual(self.evaluate([])["estado"], "INVALIDO")
