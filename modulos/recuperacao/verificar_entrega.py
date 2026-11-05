"""Confronta um contrato privado fixado com os recibos, sem executar o aplicativo."""
import argparse
import hashlib
import json
from pathlib import Path
import re
import sys


def sha(data):
    return hashlib.sha256(data).hexdigest()


def checked_file(root, name, expected):
    if not isinstance(name, str) or not name or Path(name).is_absolute() or ".." in Path(name).parts:
        raise ValueError("Caminho de evidência inválido")
    path = root / name
    resolved = path.resolve(strict=True)
    if resolved != path or root not in resolved.parents or not path.is_file():
        raise ValueError("Arquivo de evidência fora do diretório protegido")
    data = path.read_bytes()
    if not isinstance(expected, str) or not data or sha(data) != expected:
        raise ValueError("Digest de evidência divergente")
    return data


def identifier(value):
    return isinstance(value, str) and re.fullmatch(r"[a-zA-Z0-9][a-zA-Z0-9_.-]{0,95}", value)


def verify(contract_path, expected, receipts_path, revision):
    if not re.fullmatch(r"[a-f0-9]{40}", revision):
        raise ValueError("SHA Git completo obrigatório")
    contract_path = contract_path.resolve(strict=True)
    root = contract_path.parent
    raw = contract_path.read_bytes()
    if sha(raw) != expected:
        raise ValueError("Contrato divergente")
    contract = json.loads(raw)
    checked_file(root, contract["fonte"], contract["fonte_sha256"])
    criteria = {}
    for row in contract["criterios"]:
        key = row["id"]
        deps = row["depende"]
        if (not identifier(key) or key in criteria or not identifier(row["ambiente"])
                or not isinstance(row["aceite"], str) or not row["aceite"].strip()
                or not isinstance(deps, list) or not all(map(identifier, deps)) or len(deps) != len(set(deps))):
            raise ValueError("Critério, dependência ou ID inválido")
        criteria[key] = row
    if not criteria or not identifier(contract["projeto"]):
        raise ValueError("Contrato vazio ou projeto inválido")
    plan = []
    remaining = set(criteria)
    while remaining:
        ready = sorted(key for key in remaining if set(criteria[key]["depende"]).issubset(plan))
        if not ready:
            raise ValueError("Dependência desconhecida ou ciclo no grafo do escopo")
        plan.extend(ready)
        remaining.difference_update(ready)
    receipts_path = receipts_path.absolute()
    if (receipts_path != receipts_path.resolve(strict=True) or root not in receipts_path.parents
            or receipts_path in (contract_path, root / contract["fonte"])):
        raise ValueError("O lote de recibos deve pertencer ao controle independente")
    receipts = json.loads(receipts_path.read_bytes())
    if (not isinstance(receipts.get("recibos"), list) or receipts["projeto"] != contract["projeto"]
            or receipts["contrato_sha256"] != expected or receipts["revisao"] != revision):
        raise ValueError("Lote de recibos incompatível com projeto, contrato ou revisão")
    records = {}
    for row in receipts["recibos"]:
        key = row["id"]
        if key not in criteria or key in records:
            raise ValueError("Recibo duplicado ou fora do escopo")
        # The receipt must itself carry the snapshot, preventing accidental reuse of a stale observation.
        if row["revisao"] != revision or row["ambiente"] != criteria[key]["ambiente"]:
            raise ValueError("Revisão ou ambiente da prova divergente")
        if row["estado"] not in ("PASS", "FAIL", "BLOCKED"):
            raise ValueError("Resultado de prova inválido")
        if root / row["arquivo"] in (receipts_path, contract_path, root / contract["fonte"]):
            raise ValueError("O controle administrativo não é uma prova de execução")
        observation = json.loads(checked_file(root, row["arquivo"], row["sha256"]))
        if (observation["projeto"] != contract["projeto"] or observation["revisao"] != revision
                or observation["ambiente"] != row["ambiente"] or observation["verificacoes"].get(key) != row["estado"]
                or not isinstance(observation["origem"], str) or not observation["origem"].strip()):
            raise ValueError("Prova sem vínculo com critério, resultado, origem, projeto, ambiente ou revisão")
        records[key] = row["estado"]
    accepted = set()
    status = {}
    for key in plan:
        if not set(criteria[key]["depende"]).issubset(accepted):
            status[key] = "DEPENDE"
        else:
            status[key] = records.get(key, "SEM_PROVA")
            if status[key] == "PASS":
                accepted.add(key)
    return {"estado": "COBERTO_POR_RECIBOS" if len(accepted) == len(criteria) else "PARCIAL",
            "revisao": revision, "criterios": status,
            "proximos": [key for key in plan if status[key] in ("SEM_PROVA", "FAIL")]}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--contrato", type=Path, required=True)
    parser.add_argument("--sha256-contrato", required=True)
    parser.add_argument("--recibos", type=Path, required=True)
    parser.add_argument("--revisao", required=True)
    args = parser.parse_args()
    try:
        result = verify(args.contrato, args.sha256_contrato, args.recibos, args.revisao)
    except (ValueError, OSError, KeyError, TypeError, AttributeError) as exc:
        result = {"estado": "INVALIDO", "motivo": str(exc)}
    print(json.dumps(result, ensure_ascii=False))
    return 0 if result["estado"] == "COBERTO_POR_RECIBOS" else 2


if __name__ == "__main__":
    sys.exit(main())
