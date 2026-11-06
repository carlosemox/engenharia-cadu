import importlib.util
import json
from pathlib import Path
import tempfile
import unittest

MODULE = Path(__file__).resolve().parents[1] / "modulos/recuperacao/diagnostico.py"
spec = importlib.util.spec_from_file_location("diagnostico", MODULE)
diagnostico = importlib.util.module_from_spec(spec)
spec.loader.exec_module(diagnostico)


class PlanTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.path = Path(self.temp.name) / "ficha.json"
        self.report = {
            "schema": diagnostico.SCHEMA, "projeto": "fixture", "observado_em": "fixture",
            "stop_requested": False,
            "gates": {name: {"estado": "BLOCKED", "evidencia": "fixture"}
                      for name in diagnostico.GATES},
            "falhas": [{
                "classe": "SUPERVISOR", "assinatura": "checkpoint-incompativel",
                "evidencia": "fixture",
                "resolucao": {
                    "acao": "Testar contrato em cópia isolada", "responsavel": "executor",
                    "aceite": "Runtime e supervisor leem os mesmos estados",
                    "condicao_retomada": "Regressão passa",
                    "fonte_autorizacao": "missao-fixture", "revisao_alvo": "snapshot-fixture",
                    "gates_necessarios": [],
                },
            }],
        }

    def run_plan(self):
        self.path.write_text(json.dumps(self.report))
        return diagnostico.plan([self.path])

    def test_release_block_does_not_block_independent_repair_proposal(self):
        result = self.run_plan()
        self.assertFalse(result["executado"])
        self.assertEqual(result["tarefas"][0]["estado"], "PROPOSTA_PARA_VERIFICAR")

    def test_required_gate_blocks_proposal(self):
        self.report["falhas"][0]["resolucao"]["gates_necessarios"] = ["staging"]
        task = self.run_plan()["tarefas"][0]
        self.assertEqual(task["estado"], "PENDENTE")
        self.assertEqual(task["gates_pendentes"], ["staging"])

    def test_stop_overrides_proposal(self):
        self.report["stop_requested"] = True
        self.assertEqual(self.run_plan()["tarefas"][0]["estado"], "PAUSADA")

    def test_missing_stop_observation_is_not_clear(self):
        del self.report["stop_requested"]
        task = self.run_plan()["tarefas"][0]
        self.assertEqual(task["estado"], "PENDENTE")
        self.assertIn("stop_requested", task["campos_ausentes"])

    def test_legacy_report_stays_readable_but_has_no_complete_resolution(self):
        del self.report["falhas"][0]["resolucao"]
        self.assertIs(diagnostico.validate(self.report), self.report)
        self.assertEqual(self.run_plan()["tarefas"][0]["estado"], "PENDENTE")

    def test_unknown_gate_and_missing_authorization_require_resolution(self):
        resolution = self.report["falhas"][0]["resolucao"]
        resolution["gates_necessarios"] = ["graphy"]
        del resolution["fonte_autorizacao"]
        task = self.run_plan()["tarefas"][0]
        self.assertIn("gates_necessarios", task["campos_ausentes"])
        self.assertIn("fonte_autorizacao", task["campos_ausentes"])

    def test_duplicate_project_requires_reconciliation(self):
        self.run_plan()
        with self.assertRaises(ValueError):
            diagnostico.plan([self.path, self.path])


if __name__ == "__main__":
    unittest.main()
