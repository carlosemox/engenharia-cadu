#!/usr/bin/env python3
"""Coleta metadados Git locais e consolida diagnósticos sem chamar modelos."""
import argparse
from collections import Counter
from datetime import datetime, timezone
import json
import os
from pathlib import Path
import re
import subprocess
import shutil
from decimal import Decimal, InvalidOperation

SCHEMA = "cadu.diagnostico.v1"
GATES = ("local", "ci", "staging", "harness", "release")
CLASSES = ("CODIGO", "AMBIENTE", "ACESSO", "FONTE", "DECISAO", "FILA",
           "CI", "SUPERVISOR", "CUSTO", "LIBERACAO", "NENHUM", "DESCONHECIDO")


def git(root, *args):
    try:
        result = subprocess.run(
            ["git", "--no-optional-locks", "-c", "core.fsmonitor=false", "-C", str(root), *args],
            env={**os.environ, "GIT_TERMINAL_PROMPT": "0"},
            stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, timeout=15)
    except (OSError, subprocess.TimeoutExpired):
        return None
    if result.returncode:
        return None
    return result.stdout.decode("utf-8", errors="replace").strip()


def collect(root):
    top = git(root, "rev-parse", "--show-toplevel")
    if not top or Path(top).resolve() != root.resolve():
        raise ValueError(f"Indique a raiz de um checkout Git: {root.name}")
    changes = git(root, "status", "--porcelain=v1", "-z", "--untracked-files=normal",
                  "--ignore-submodules=all")
    tracked = git(root, "ls-files", "-z", "--", ".github/workflows/*", "*Dockerfile*",
                  "*compose.y*ml", "supabase/config.toml", ":(glob)**/supabase/config.toml")
    names = set(tracked.split("\0")) if tracked is not None else None
    indicators = {
        "github_actions": lambda n: n.startswith(".github/workflows/") and n.endswith((".yml", ".yaml")),
        "docker": lambda n: "Dockerfile" in Path(n).name or Path(n).name.endswith(("compose.yml", "compose.yaml")),
        "supabase": lambda n: n.endswith("supabase/config.toml"),
    }
    return {
        "sinais_versionados": {
            key: None if names is None else any(match(n) for n in names) for key, match in indicators.items()
        },
        "clientes_no_path": {name: shutil.which(name) is not None for name in ("gh", "docker", "supabase")},
        "hostinger_remoto": "NAO_VERIFICADO",
        "schema": SCHEMA, "projeto": root.resolve().name,
        "observado_em": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "janela": None, "branch": git(root, "symbolic-ref", "--short", "-q", "HEAD"),
        "sha": git(root, "rev-parse", "--verify", "HEAD"),
        "alteracoes_locais": None if changes is None else bool(changes),
        "entrega_aceita": None, "falhas": [],
        "gates": {g: {"estado": "NAO_VERIFICADO", "evidencia": None} for g in GATES},
        "entregas_aceitas_na_janela": None, "custo_medido": None,
        "tarefa_elegivel": None, "acao_humana": None,
    }


def cell(value):
    return "—" if value is None else " ".join(str(value).split()).replace("|", r"\|")


def validate(item):
    if not isinstance(item, dict) or item.get("schema") != SCHEMA:
        raise ValueError(f"Schema esperado: {SCHEMA}")
    for k in ("projeto", "observado_em"):
        if not isinstance(item.get(k), str) or not item[k].strip():
            raise ValueError(f"Campo obrigatório ausente: {k}")
    gates = item.get("gates")
    if not isinstance(gates, dict) or any(not isinstance(gates.get(k), dict) for k in GATES):
        raise ValueError("Mantenha a estrutura dos cinco gates da ficha")
    for gate in gates.values():
        if not isinstance(gate, dict) or not isinstance(gate.get("estado"), str):
            raise ValueError("Gate sem estado textual")
        if gate["estado"] not in ("PASS", "FAIL", "RUNNING", "BLOCKED", "INCONCLUSIVE", "NOT_RUN", "NAO_VERIFICADO", "NAO_APLICAVEL"):
            raise ValueError("Estado de gate desconhecido")
        if gate["estado"] not in ("NOT_RUN", "NAO_VERIFICADO") and (
                not isinstance(gate.get("evidencia"), str) or not gate["evidencia"].strip()):
            raise ValueError(f"Gate {gate['estado']} sem evidência")
    fails = item.get("falhas")
    if not isinstance(fails, list):
        raise ValueError("falhas deve ser uma lista")
    for failure in fails:
        if not isinstance(failure, dict) or failure.get("classe") not in CLASSES:
            raise ValueError("Classe de falha inválida")
        sig = failure.get("assinatura")
        if not isinstance(sig, str) or not re.fullmatch(r"[a-z0-9_.-]{1,100}", sig):
            raise ValueError("Use uma assinatura curta em minúsculas, sem nomes privados")
        if not isinstance(failure.get("evidencia"), str) or not failure["evidencia"].strip():
            raise ValueError("Falha sem evidência")
    count = item.get("entregas_aceitas_na_janela")
    if count is not None and (type(count) is not int or count < 0 or not item.get("janela")):
        raise ValueError("Contagem de entregas exige janela e inteiro não negativo")
    cost = item.get("custo_medido")
    if cost is not None:
        if not isinstance(cost, dict) or not cost.get("fonte") or not cost.get("moeda"):
            raise ValueError("O custo medido exige valor, moeda e fonte")
        try:
            amount = Decimal(str(cost.get("valor")))
        except InvalidOperation:
            raise ValueError("Use um valor numérico para o custo") from None
        if not amount.is_finite() or amount < 0:
            raise ValueError("Custo inválido")
    return item


def summary(paths):
    reports = {}
    counts = Counter()
    for path in paths:
        value = json.loads(path.read_text(encoding="utf-8-sig"))
        for item in value if isinstance(value, list) else [value]:
            report = validate(item)
            key = report["projeto"].strip().casefold()
            if key in reports:
                raise ValueError(f"Projeto repetido: {report['projeto']}. Reconcilie o registro antes de contar.")
            reports[key] = report
            counts.update({(f["classe"], f["assinatura"]) for f in report["falhas"]})
    if not reports:
        raise ValueError("Nenhum projeto recebido")
    lines = [f"Projetos recebidos: {len(reports)}. Cobertura restrita às fichas fornecidas.", "",
             "| Projeto | SHA | Local | CI | Staging | Harness | Release | Próxima tarefa |",
             "|---|---|---|---|---|---|---|---|"]
    for key in sorted(reports):
        r = reports[key]
        fields = [r["projeto"], (r.get("sha") or "")[:12] or None]
        fields.extend(r["gates"][g]["estado"] for g in GATES)
        fields.append(r.get("tarefa_elegivel"))
        lines.append("| " + " | ".join(cell(v) for v in fields) + " |")
    lines.extend(["", "| Projeto | Janela | Entregas aceitas | Custo observado | Custo por entrega |",
                  "|---|---|---|---|---|"])
    for key in sorted(reports):
        r = reports[key]
        cost = r.get("custo_medido")
        count = r.get("entregas_aceitas_na_janela")
        measured = per_delivery = None
        if cost is not None:
            amount = Decimal(str(cost["valor"]))
            measured = f"{cost['moeda']} {amount:.2f}"
            if count and r.get("janela") and cost.get("atribuivel_mesma_janela") is True:
                per_delivery = f"{cost['moeda']} {amount / count:.2f}"
        lines.append("| " + " | ".join(cell(v) for v in
                     [r["projeto"], r.get("janela"), count, measured, per_delivery]) + " |")
    lines.extend(["", "Falhas observadas por número de projetos distintos:", ""])
    lines.extend(f"- {cls} / {sig}: {n}" for (cls, sig), n in counts.most_common())
    if not counts:
        lines.append("Nenhuma falha documentada nas fichas.")
    lines.extend(["", "Decisões ou acessos pendentes:", ""])
    manual = [f"- {cell(r['projeto'])}: {cell(r['acao_humana'])}" for r in reports.values()
              if r.get("acao_humana")]
    lines.extend(manual or ["Nenhuma ação humana informada nas fichas."])
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="mode", required=True)
    commands.add_parser("coletar").add_argument("pastas", type=Path, nargs="+")
    commands.add_parser("consolidar").add_argument("fichas", type=Path, nargs="+")
    args = parser.parse_args()
    try:
        if args.mode == "coletar":
            rows = [collect(root) for root in args.pastas]
            print(json.dumps(rows[0] if len(rows) == 1 else rows, ensure_ascii=False, indent=2))
        else:
            print(summary(args.fichas))
    except (OSError, ValueError) as error:
        parser.exit(2, f"Diagnóstico: {error}\n")


if __name__ == "__main__":
    main()
