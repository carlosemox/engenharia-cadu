"""Procedimento de exemplo para uma cópia descartável da fábrica de prompts da central."""
from html.parser import HTMLParser
import json
import os
import hashlib
import shutil
from pathlib import Path
import subprocess
import sys


# Only the client under test comes from the disposable checkout. This oracle
# and the Node path belong to the pinned, trusted procedure.
NODE = os.environ.get("CADU_NODE", "node")
BASELINE = None  # Fixe no procedimento privado antes de assinar, se exigir restauração.
CLIENT_CHECK = r"""
const fs = require('node:fs'), vm = require('node:vm'), assert = require('node:assert/strict');
const catalog = JSON.parse(fs.readFileSync('docs/fabrica/routes.json', 'utf8'));
const nodes = {};
for (const id of ['status','mode','target','request','attachment','output','copy']) {
    nodes[id] = {value:'', textContent:'', events:{}, addEventListener(k,fn){this.events[k]=fn}};
}
nodes.mode.value = 'auto';
const document = {getElementById: id=>nodes[id], querySelectorAll: ()=>[]};
const fetch = async ()=>({ok:true,json:async()=>catalog});
vm.runInNewContext(fs.readFileSync('docs/assets/factory.js','utf8'), {document, fetch});
setImmediate(() => {
    assert.equal(nodes.status.textContent, '');
    assert.ok(nodes.output.value.includes('CADU'));
    nodes.target.value = 'demo';
    nodes.request.value = 'pedido "$&"\nsegunda linha';
    nodes.attachment.checked = true;
    for (const [mode, route] of Object.entries(catalog.routes)) {
        nodes.mode.value = mode;
        nodes.mode.events.input();
        const prompt = nodes.output.value;
        assert.ok(prompt.includes(route.procedure));
        assert.ok(prompt.includes(mode.toUpperCase()));
        const payload = prompt.split('adicional):\n')[1];
        assert.deepEqual(JSON.parse(payload), {projeto:'demo',pedido:nodes.request.value,estudo_anexado:true});
    }
});
"""


class Options(HTMLParser):
    def __init__(self):
        super().__init__()
        self.values = []
        self.in_mode = False

    def handle_starttag(self, tag, attrs):
        attributes = dict(attrs)
        if tag == "select" and attributes.get("id") == "mode":
            self.in_mode = True
        elif tag == "option" and self.in_mode:
            self.values.append(attributes.get("value"))

    def handle_endtag(self, tag):
        if tag == "select" and self.in_mode:
            self.in_mode = False


def main(stage, recipe):
    if stage in ("referencia", "rollback_check"):
        # build_factory writes only these outputs; hash absence explicitly.
        names = ("docs/fabrica/routes.json", "docs/fabrica/index.html", "docs/fabrica/index.en.html",
                 "docs/fabrica/index.es.html", "docs/comandos/ASSUMIR_PROJETO.txt",
                 "docs/comandos/REESTRUTURAR_PROJETO.txt", "docs/read.md")
        values = [(name, hashlib.sha256(Path(name).read_bytes()).hexdigest() if Path(name).is_file() else None)
                  for name in names]
        current = hashlib.sha256(json.dumps(values).encode()).hexdigest()
        if stage == "referencia":
            print(current)
            return 0
        return 0 if current == BASELINE else 2
    if stage == "probe" and not shutil.which(NODE):
        return 2
    # Independent acceptance contract for this version of the factory.
    expected = {"auto", "assumir", "reestruturar", "retomar", "executar", "revisar",
                "auditar", "medir", "novo", "fabrica", "iniciar", "recuperar", "diagnosticar", "operar"}
    canonical = json.loads(Path("fabrica/rotas.json").read_text())["modes"]
    if set(canonical) != expected:
        return 2  # A revisão precisa conter a rota antes de regenerar os derivados.
    out = Path("docs/fabrica")
    if stage == "repair" and recipe == "regenerar":
        return subprocess.run([sys.executable, "scripts/build_factory.py"], check=False).returncode
    if stage == "probe":
        try:
            published = json.loads((out / "routes.json").read_text())
            actual = published["routes"]
            dummy = json.dumps(published["dummy"], ensure_ascii=False, indent=2)
            if set(actual) != expected:
                return 1
            for key, expected_route in canonical.items():
                record = actual[key]
                if any(record.get(field) != value for field, value in expected_route.items()):
                    return 1
                template = record.get("template")
                if not isinstance(template, str) or template.count(dummy) != 1 or expected_route["procedure"] not in template:
                    return 1
            return 0
        except (FileNotFoundError, ValueError, TypeError, KeyError, AttributeError):
            return 1
    if stage == "holdout":
        for name in ("index.html", "index.en.html", "index.es.html"):
            parser = Options()
            parser.feed((out / name).read_text())
            if set(parser.values) != expected or len(parser.values) != len(expected):
                return 1
        try:
            return subprocess.run([NODE, "-e", CLIENT_CHECK], check=False).returncode
        except FileNotFoundError:
            return 2
    return 2  # Atestar reversão exige uma referência própria, registrada no ensaio.


if __name__ == "__main__":
    try:
        sys.exit(main(*sys.argv[1:]))
    except (OSError, ValueError, KeyError, TypeError):
        sys.exit(2)
