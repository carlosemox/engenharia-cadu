"""Instala o agente e opcionalmente registra o roteamento no checkout solicitado."""
import argparse
import fcntl
import os
import re
import stat
from pathlib import Path
import subprocess
import tempfile

ROLE = Path(".codex/agents/cadu_recuperacao.toml")
SOURCE = Path(__file__).resolve().parents[2] / ROLE


def install(root):
    root = root.resolve(strict=True)
    top = subprocess.check_output(["git", "-C", str(root), "rev-parse", "--show-toplevel"], text=True)
    if Path(top.strip()).resolve() != root:
        raise ValueError("Indique a raiz do aplicativo.")
    parent = root
    for part in ROLE.parent.parts:
        parent = parent / part
        if parent.is_symlink():
            raise ValueError("Destino simbólico recusado.")
        parent.mkdir(exist_ok=True)
    destination = root / ROLE
    content = SOURCE.read_bytes()
    with tempfile.NamedTemporaryFile(dir=parent) as tmp:
        tmp.write(content)
        tmp.flush()
        try:
            os.link(tmp.name, destination)
        except FileExistsError:
            if destination.is_symlink() or not destination.is_file() or destination.read_bytes() != content:
                raise ValueError("Agente local diferente. Compare as versões antes de atualizar.")
            return "JA_ADOTADO"
    return "ADOTADO"


BEGIN = "<!-- engenharia-cadu:recovery:begin -->"
END = "<!-- engenharia-cadu:recovery:end -->"


def attest_source(revision):
    central = SOURCE.parents[2]
    def read_git(*args):
        return subprocess.check_output(["git", "-C", str(central), *args], stderr=subprocess.DEVNULL)
    if read_git("rev-parse", "HEAD").decode().strip() != revision:
        raise ValueError("A revisão solicitada difere do checkout da central.")
    for path in (ROLE, Path("comando.md"), Path("modulos/recuperacao/adotar.py")):
        if read_git("show", f"{revision}:{path.as_posix()}") != (central / path).read_bytes():
            raise ValueError(f"Fonte da central divergente na revisão indicada: {path}")


def managed_block(revision):
    url = f"https://raw.githubusercontent.com/carlosemox/engenharia-cadu/{revision}/comando.md"
    return (f"{BEGIN}\n## Recuperação de desenvolvimento\n\n"
             f"Para desenvolvimento autorizado, use a [Engenharia Cadu fixada]({url}). "
             "Reutilize ambiente e checkpoint. Em falha técnica, use CADU RECUPERAR e o agente "
             "cadu_recuperacao quando disponível. Preserve as regras locais, alçadas e testes. "
             "Se um nó depender de acesso externo, continue a próxima tarefa independente autorizada. "
             "Pedidos de auditoria somente leitura preservam esse escopo.\n"
             f"{END}\n").encode()


def activate(root, revision):
    if not re.fullmatch(r"[0-9a-f]{40}", revision):
        raise ValueError("Indique o SHA completo da revisão verificada.")
    attest_source(revision)
    root = root.resolve(strict=True)
    top = subprocess.check_output(["git", "-C", str(root), "rev-parse", "--show-toplevel"], text=True)
    if Path(top.strip()).resolve() != root:
        raise ValueError("Indique a raiz do aplicativo.")
    git_dir = subprocess.check_output(["git", "-C", str(root), "rev-parse", "--absolute-git-dir"], text=True)
    block = managed_block(revision)
    dest = root / "AGENTS.md"
    with (Path(git_dir.strip()) / "cadu-adotar.lock").open("a") as lock:
        fcntl.flock(lock, fcntl.LOCK_EX)
        if dest.is_symlink() or (dest.exists() and not dest.is_file()):
            raise ValueError("AGENTS.md deve ser um arquivo regular.")
        previous = dest.read_bytes() if dest.exists() else None
        old = previous or b""
        old.decode("utf-8")
        if BEGIN.encode() in old or END.encode() in old:
            match = re.search(re.escape(BEGIN.encode()) + rb".*?/([a-f0-9]{40})/comando\.md.*?"
                              + re.escape(END.encode()) + rb"\n", old, re.DOTALL)
            if (old.count(BEGIN.encode()) != 1 or old.count(END.encode()) != 1 or not match
                    or match.group() != managed_block(match[1].decode())):
                raise ValueError("Roteamento local personalizado. Compare as versões antes de atualizar.")
            if match.group() == block:
                install(root)
                return "JA_ATIVO"
            updated = old[:match.start()] + block + old[match.end():]
        else:
            updated = old + (b"\n\n" if old else b"") + block
        install(root)
        mode = stat.S_IMODE(dest.stat().st_mode) if previous is not None else 0o644
        with tempfile.NamedTemporaryFile(dir=root, delete=False) as tmp:
            path = Path(tmp.name)
            tmp.write(updated)
        try:
            path.chmod(mode)
            if previous is None:
                os.link(path, dest)
            elif dest.is_symlink() or dest.read_bytes() != previous:
                raise ValueError("AGENTS.md mudou durante a adoção; releia o arquivo.")
            else:
                os.replace(path, dest)
        finally:
            path.unlink(missing_ok=True)
    return "ATIVO"


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("projeto", type=Path)
    parser.add_argument("--ativar-na-revisao", metavar="SHA",
                        help="Adota o agente e grava o roteamento persistente no AGENTS.md do projeto.")
    args = parser.parse_args()
    try:
        print(activate(args.projeto, args.ativar_na_revisao) if args.ativar_na_revisao else install(args.projeto))
    except (ValueError, OSError, subprocess.CalledProcessError) as exc:
        parser.exit(2, f"{exc}\n")
