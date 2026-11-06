#!/usr/bin/env python3
"""Build the static, tri-lingual prompt factory without network or deployment."""
import html
import json
import re
from pathlib import Path

from prompt_factory import catalog, generate

ROOT = Path(__file__).resolve().parents[1]
DUMMY = {"projeto": "__CADU_TARGET__", "pedido": "__CADU_REQUEST__", "estudo_anexado": False}

CONTEXT_FIELDS = (
    ("repository", "repositorio"),
    ("checkout", "checkout"),
    ("branch", "branch"),
    ("code-revision", "sha_codigo"),
    ("requirement", "requisito_aprovado"),
    ("state", "estado_atual"),
    ("environment", "ambiente"),
    ("services", "servicos"),
    ("authorizations", "autorizacoes"),
    ("blockers", "bloqueios"),
)

TEXT = {
    "pt": {
        "html": "pt-BR", "title": "Fábrica de prompts | Engenharia Cadu",
        "back": "← Engenharia Cadu", "eyebrow": "UM PEDIDO · UM CAMINHO · CONTEXTO RECUPERÁVEL",
        "headline": "Escolha o caminho. Gere o comando.",
        "intro": "Preencha o contexto uma vez. A fábrica transforma as respostas em um comando rastreável para o agente continuar sem redescobrir o projeto.",
        "steps": "Como funciona", "step1": "1. Identifique o momento do projeto",
        "step2": "2. Registre o contexto disponível", "step3": "3. Copie o comando para a conversa do agente",
        "custom": "PERSONALIZAR", "need": "O que você precisa?", "project": "Projeto",
        "project_ph": "Nome, caminho ou repositório", "result": "Resultado desejado",
        "result_ph": "Ex.: reconciliar o estudo e retomar a implementação",
        "attach": "Vou anexar um estudo à conversa", "context": "CONTEXTO PARA RETOMADA",
        "context_intro": "Informe apenas o que já é conhecido. Não cole senhas, tokens, chaves, cookies ou dados pessoais.",
        "repository": "Repositório GitHub", "checkout": "Checkout ou diretório",
        "branch": "Branch de trabalho", "code-revision": "SHA/revisão do código",
        "requirement": "Requisito aprovado", "state": "Estado atual/checkpoint",
        "environment": "Ambiente e dependências", "services": "Serviços disponíveis",
        "authorizations": "Autorizações válidas", "blockers": "Bloqueios e pendências",
        "stop": "STOP_REQUESTED", "stop_unknown": "Não verificado", "stop_clear": "Ausente/limpo",
        "stop_requested": "Solicitado/preservado",
        "note": "A fábrica gera o comando. A execução acontece no agente, conforme as autorizações reais do projeto.",
        "download1": "Baixar comando completo para assumir projeto",
        "download2": "Baixar comando completo para reestruturar",
        "generated": "COMANDO PRONTO", "copy": "Copiar comando", "learn": "Entender o método",
        "noscript": "A personalização requer JavaScript. O comando padrão e os downloads continuam disponíveis.",
        "paths": [
            ("Assumir projeto", "Estudos, anexos ou código já existem. Reconcilie o estado real e continue com segurança.", "Começar por aqui"),
            ("Reestruturar", "O projeto está confuso, incompleto ou fora do método. Diagnostique e corrija a rota.", "Corrigir o caminho"),
            ("Retomar checkpoint", "Existe um estado salvo. Continue do próximo lote registrado, sem repetir o que já foi concluído.", "Retomar agora"),
            ("Escolha automática", "Você sabe o resultado, mas não sabe qual procedimento usar. A fábrica seleciona a rota suficiente.", "Escolher por mim"),
        ],
    },
    "en": {
        "html": "en", "title": "Prompt factory | Cadu Engineering",
        "back": "← Cadu Engineering", "eyebrow": "ONE REQUEST · ONE PATH · RECOVERABLE CONTEXT",
        "headline": "Choose the path. Generate the command.",
        "intro": "Fill in the context once. The factory turns your answers into a traceable command so the agent can continue without rediscovering the project.",
        "steps": "How it works", "step1": "1. Identify the project moment",
        "step2": "2. Record the available context", "step3": "3. Copy the command into the agent conversation",
        "custom": "CUSTOMIZE", "need": "What do you need?", "project": "Project",
        "project_ph": "Name, path or repository", "result": "Desired outcome",
        "result_ph": "Example: reconcile the study and resume implementation",
        "attach": "I will attach a study to the conversation", "context": "RESUMPTION CONTEXT",
        "context_intro": "Enter only what is known. Do not paste passwords, tokens, keys, cookies or personal data.",
        "repository": "GitHub repository", "checkout": "Checkout or directory",
        "branch": "Work branch", "code-revision": "Code SHA/revision",
        "requirement": "Approved requirement", "state": "Current state/checkpoint",
        "environment": "Environment and dependencies", "services": "Available services",
        "authorizations": "Valid authorizations", "blockers": "Blockers and pending items",
        "stop": "STOP_REQUESTED", "stop_unknown": "Not verified", "stop_clear": "Absent/clear",
        "stop_requested": "Requested/preserved",
        "note": "The factory generates the command. Execution happens in the agent according to the project's actual authorizations.",
        "download1": "Download full assume-project command",
        "download2": "Download full restructure-project command",
        "generated": "READY COMMAND", "copy": "Copy command", "learn": "Understand the method",
        "noscript": "Customization requires JavaScript. The default command and the downloads remain available.",
        "paths": [
            ("Assume project", "Studies, attachments or existing code are available. Reconcile the real state and continue safely.", "Start here"),
            ("Restructure", "The project is unclear, incomplete or off method. Diagnose and correct the route.", "Correct the route"),
            ("Resume checkpoint", "A saved state exists. Continue from the next recorded batch without repeating completed work.", "Resume now"),
            ("Automatic choice", "You know the outcome but not which procedure to use. The factory selects the sufficient route.", "Choose for me"),
        ],
    },
    "es": {
        "html": "es", "title": "Fábrica de prompts | Ingeniería Cadu",
        "back": "← Ingeniería Cadu", "eyebrow": "UNA SOLICITUD · UN CAMINO · CONTEXTO RECUPERABLE",
        "headline": "Elija el camino. Genere el comando.",
        "intro": "Complete el contexto una vez. La fábrica convierte sus respuestas en un comando trazable para que el agente continúe sin redescubrir el proyecto.",
        "steps": "Cómo funciona", "step1": "1. Identifique el momento del proyecto",
        "step2": "2. Registre el contexto disponible", "step3": "3. Copie el comando en la conversación del agente",
        "custom": "PERSONALIZAR", "need": "¿Qué necesita?", "project": "Proyecto",
        "project_ph": "Nombre, ruta o repositorio", "result": "Resultado deseado",
        "result_ph": "Ejemplo: reconciliar el estudio y retomar la implementación",
        "attach": "Adjuntaré un estudio a la conversación", "context": "CONTEXTO PARA RETOMAR",
        "context_intro": "Informe solo lo que ya conoce. No pegue contraseñas, tokens, claves, cookies ni datos personales.",
        "repository": "Repositorio GitHub", "checkout": "Checkout o directorio",
        "branch": "Rama de trabajo", "code-revision": "SHA/revisión del código",
        "requirement": "Requisito aprobado", "state": "Estado actual/checkpoint",
        "environment": "Entorno y dependencias", "services": "Servicios disponibles",
        "authorizations": "Autorizaciones válidas", "blockers": "Bloqueos y pendientes",
        "stop": "STOP_REQUESTED", "stop_unknown": "No verificado", "stop_clear": "Ausente/limpio",
        "stop_requested": "Solicitado/preservado",
        "note": "La fábrica genera el comando. La ejecución ocurre en el agente según las autorizaciones reales del proyecto.",
        "download1": "Descargar comando completo para asumir proyecto",
        "download2": "Descargar comando completo para reestructurar",
        "generated": "COMANDO LISTO", "copy": "Copiar comando", "learn": "Entender el método",
        "noscript": "La personalización requiere JavaScript. El comando predeterminado y las descargas siguen disponibles.",
        "paths": [
            ("Asumir proyecto", "Hay estudios, anexos o código existente. Reconcilie el estado real y continúe con seguridad.", "Comenzar aquí"),
            ("Reestructurar", "El proyecto está confuso, incompleto o fuera del método. Diagnostique y corrija la ruta.", "Corregir la ruta"),
            ("Retomar checkpoint", "Existe un estado guardado. Continúe desde el próximo lote registrado sin repetir lo concluido.", "Retomar ahora"),
            ("Elección automática", "Sabe el resultado, pero no qué procedimiento usar. La fábrica selecciona la ruta suficiente.", "Elegir por mí"),
        ],
    },
}

MODE_NAMES = {
    "pt": {"auto": "Comando único: escolher o caminho", "assumir": "Assumir projeto com estudo anexado", "reestruturar": "Diagnosticar, corrigir e reorganizar", "retomar": "Retomar do checkpoint", "executar": "Executar tarefa delimitada", "revisar": "Revisar entrega", "auditar": "Auditar segurança", "medir": "Comparar eficiência", "novo": "Iniciar produto novo", "fabrica": "Criar comando personalizado", "iniciar": "Preparar e operar o primeiro incremento", "recuperar": "Corrigir uma falha e retomar", "diagnosticar": "Diagnosticar bloqueios", "operar": "Preparar e operar por até 24 horas"},
    "en": {"auto": "Single command: choose the path", "assumir": "Assume project with attached study", "reestruturar": "Diagnose, correct and reorganize", "retomar": "Resume from checkpoint", "executar": "Execute bounded task", "revisar": "Review delivery", "auditar": "Audit security", "medir": "Compare efficiency", "novo": "Start a new product", "fabrica": "Create a custom command", "iniciar": "Prepare and operate the first increment", "recuperar": "Recover a failure and resume", "diagnosticar": "Diagnose project blockers", "operar": "Prepare and operate for up to 24 hours"},
    "es": {"auto": "Comando único: elegir el camino", "assumir": "Asumir proyecto con estudio adjunto", "reestruturar": "Diagnosticar, corregir y reorganizar", "retomar": "Retomar desde el checkpoint", "executar": "Ejecutar tarea delimitada", "revisar": "Revisar entrega", "auditar": "Auditar seguridad", "medir": "Comparar eficiencia", "novo": "Iniciar producto nuevo", "fabrica": "Crear comando personalizado", "iniciar": "Preparar y operar el primer incremento", "recuperar": "Recuperar un fallo y retomar", "diagnosticar": "Diagnosticar bloqueos", "operar": "Preparar y operar hasta 24 horas"},
}


def esc(value):
    return html.escape(str(value), quote=True)


def make_page(lang, routes):
    t = TEXT[lang]
    default = esc(generate())
    options = "".join(
        f'<option value="{esc(mode)}">{esc(MODE_NAMES[lang].get(mode, route["label"]))}</option>'
        for mode, route in routes.items()
    )
    paths = []
    for index, (title, description, action) in enumerate(t["paths"]):
        mode = ("assumir", "reestruturar", "retomar", "auto")[index]
        primary = " pathway-primary" if index == 3 else ""
        paths.append(f'<div class="pathway{primary}"><span class="path-number">0{index + 1}</span><h2>{esc(title)}</h2><p>{esc(description)}</p><button class="path-button" type="button" data-mode="{mode}">{esc(action)}</button></div>')
    fields = []
    for field_id, _ in CONTEXT_FIELDS:
        cls = "wide" if field_id in {"environment", "services", "authorizations", "blockers"} else ""
        control = f'<textarea id="{field_id}" rows="3"></textarea>' if cls else f'<input id="{field_id}" type="text" autocomplete="off">'
        fields.append(f'<label class="{cls}" for="{field_id}">{esc(t[field_id])}{control}</label>')
    stop = f'<label for="stop-requested">{esc(t["stop"])}<select id="stop-requested"><option value="unknown">{esc(t["stop_unknown"])}</option><option value="clear">{esc(t["stop_clear"])}</option><option value="requested">{esc(t["stop_requested"])}</option></select></label>'
    language_links = []
    for current, filename, code in (("pt", "index.html", "PT"), ("en", "index.en.html", "EN"), ("es", "index.es.html", "ES")):
        current_attr = 'aria-current="page"' if current == lang else ""
        language_links.append(f'<a href="{filename}" {current_attr}>{code}</a>')
    languages = "".join(language_links)
    return f'''<!doctype html><html lang="{t["html"]}" data-language="{lang}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{esc(t["title"])}</title><meta http-equiv="Content-Security-Policy" content="default-src 'self'; script-src 'self'; style-src 'self'; connect-src 'self'; object-src 'none'; base-uri 'self'; form-action 'none"><link rel="stylesheet" href="../assets/factory.css"><script defer src="../assets/factory.js"></script></head><body><main><nav class="topbar"><a href="../index.html">{esc(t["back"])}</a><span class="languages">{languages}</span></nav><p class="eyebrow">{esc(t["eyebrow"])}</p><h1>{esc(t["headline"])}</h1><p class="intro">{esc(t["intro"])}</p><section class="how"><p class="section-kicker">{esc(t["steps"])}</p><div><strong>{esc(t["step1"])}</strong><strong>{esc(t["step2"])}</strong><strong>{esc(t["step3"])}</strong></div></section><section class="pathways" aria-label="{esc(t["steps"])}">{"".join(paths)}</section><div class="grid"><section aria-label="{esc(t["custom"])}"><p class="section-kicker">{esc(t["custom"])}</p><label for="mode">{esc(t["need"])}</label><select id="mode">{options}</select><label for="target">{esc(t["project"])}</label><input id="target" placeholder="{esc(t["project_ph"])}"><label for="request">{esc(t["result"])}</label><textarea id="request" rows="5" placeholder="{esc(t["result_ph"])}"></textarea><label class="check"><input id="attachment" type="checkbox"> {esc(t["attach"])}</label><p class="small">{esc(t["note"])}</p><p><a href="../comandos/ASSUMIR_PROJETO.txt" download>{esc(t["download1"])}</a></p><p><a href="../comandos/REESTRUTURAR_PROJETO.txt" download>{esc(t["download2"])}</a></p></section><section class="context-panel" aria-label="{esc(t["context"])}"><p class="section-kicker">{esc(t["context"])}</p><p class="context-intro">{esc(t["context_intro"])}</p><div class="context-grid">{"".join(fields)}{stop}</div></section><section aria-label="{esc(t["generated"])}"><p class="section-kicker">{esc(t["generated"])}</p><textarea id="output" rows="24" readonly>{default}</textarea><button id="copy" type="button">{esc(t["copy"])}</button><p id="status" role="status" aria-live="polite"></p></section></div><noscript><p>{esc(t["noscript"])}</p></noscript><p class="small">Método 2.3 · <a href="https://github.com/carlosemox/engenharia-cadu/blob/main/fabrica/README.md">{esc(t["learn"])}</a></p></main></body></html>'''


def build():
    routes = catalog()["modes"]
    out = ROOT / "docs/fabrica"
    out.mkdir(parents=True, exist_ok=True)
    data = {"dummy": DUMMY, "routes": {}}
    for mode, route in routes.items():
        data["routes"][mode] = {**route, "template": generate(mode, DUMMY["projeto"], DUMMY["pedido"])}
    (out / "routes.json").write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    for lang, filename in (("pt", "index.html"), ("en", "index.en.html"), ("es", "index.es.html")):
        (out / filename).write_text(make_page(lang, routes), encoding="utf-8")
    for name in ("ASSUMIR_PROJETO", "REESTRUTURAR_PROJETO"):
        source = (ROOT / f"comandos/{name}.md").read_text(encoding="utf-8")
        marker = chr(96) * 3
        body = re.search(r"## Comando completo\n" + marker + r"text\n([\s\S]*?)\n" + marker, source).group(1)
        (ROOT / f"docs/comandos/{name}.txt").write_text(body + "\n", encoding="utf-8")
    mirror = (ROOT / "read.md").read_text(encoding="utf-8")
    mirror = re.sub(
        r'\]\(([^\s)]+)\)',
        lambda match: match.group(0) if (":" in match.group(1) or match.group(1).startswith(("#", "//"))) else "](" + "https://github.com/carlosemox/engenharia-cadu/blob/main/" + match.group(1) + ")",
        mirror,
    )
    (ROOT / "docs/read.md").write_text(mirror, encoding="utf-8")
    print("Fábrica tri-língue e comandos completos gerados; nenhum projeto executado.")


if __name__ == "__main__":
    build()
