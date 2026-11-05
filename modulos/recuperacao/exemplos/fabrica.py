"""Procedimento de exemplo para uma cópia descartável da fábrica de prompts da central."""
from html.parser import HTMLParser
import json
from pathlib import Path
import subprocess
import sys


class Options(HTMLParser):
    def __init__(self):
        super().__init__()
        self.values = []

    def handle_starttag(self, tag, attrs):
        if tag == "option":
            self.values.append(dict(attrs).get("value"))


def main(stage, recipe):
    # Independent acceptance contract for this version of the factory.
    expected = {"auto", "assumir", "reestruturar", "retomar", "executar", "revisar",
                "auditar", "medir", "novo", "fabrica", "iniciar", "recuperar", "diagnosticar"}
    if set(json.loads(Path("fabrica/rotas.json").read_text())["modes"]) != expected:
        return 2  # A revisão precisa conter a rota antes de regenerar os derivados.
    out = Path("docs/fabrica")
    if stage == "repair" and recipe == "regenerar":
        return subprocess.run([sys.executable, "scripts/build_factory.py"], check=False).returncode
    if stage == "probe":
        actual = json.loads((out / "routes.json").read_text())["routes"]
        return int(set(actual) != expected)
    if stage == "holdout":
        for name in ("index.html", "index.en.html", "index.es.html"):
            parser = Options()
            parser.feed((out / name).read_text())
            if set(parser.values) != expected or len(parser.values) != len(expected):
                return 1
        return 0
    return 2  # Atestar reversão exige uma referência própria, registrada no ensaio.


if __name__ == "__main__":
    try:
        sys.exit(main(*sys.argv[1:]))
    except (OSError, ValueError, KeyError, TypeError):
        sys.exit(2)
