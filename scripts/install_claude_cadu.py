#!/usr/bin/env python3
"""Link CADU Claude Code assets into user scope without touching existing ECC/config."""
import argparse
import json
import os
import sys
from pathlib import Path

SKILLS = ("cadu-mike", "cadu-ecc-seguranca", "cadu-ecc-fluxo", "cadu-untangle")
AGENTS = ("cadu-scout", "cadu-architect", "cadu-slice-builder", "cadu-slice-reviewer", "cadu-security-gate")

def entries(source, dest):
    for skill in SKILLS:
        yield "skill", source / ".claude" / "skills" / skill, dest / "skills" / skill
    for agent in AGENTS:
        yield "agent", source / ".claude" / "agents" / (agent + ".md"), dest / "agents" / (agent + ".md")

def audit(source, dest, action):
    records = []
    for kind, target, link in entries(source, dest):
        if not target.exists():
            records.append({"item": link.name, "status": "SOURCE_MISSING"})
            continue
        # Never trust a directory or another user's custom file just because its name matches.
        own_link = link.is_symlink() and link.resolve() == target.resolve()
        if action == "remove":
            if own_link:
                link.unlink()
                state = "REMOVED"
            else:
                state = "SKIPPED_NOT_OWNED"
        elif own_link:
            state = "INSTALLED"
        elif link.exists() or link.is_symlink():
            state = "CONFLICT_PRESERVED"
        elif action == "apply":
            link.parent.mkdir(parents=True, exist_ok=True)
            os.symlink(str(target), str(link), target_is_directory=(kind == "skill"))
            state = "INSTALLED" if link.is_symlink() and link.resolve() == target.resolve() else "FAILED"
        else:
            state = "MISSING"
        records.append({"item": link.name, "kind": kind, "status": state})
    return records

def main():
    p=argparse.ArgumentParser(description="Install safe CADU aliases, never install duplicate ECC or edit Claude settings.")
    mode=p.add_mutually_exclusive_group(required=True)
    mode.add_argument("--plan", action="store_true")
    mode.add_argument("--apply", action="store_true")
    mode.add_argument("--check", action="store_true")
    mode.add_argument("--remove", action="store_true")
    p.add_argument("--source",type=Path,default=Path(__file__).resolve().parents[1])
    p.add_argument("--dest",type=Path,default=Path.home()/".claude")
    a=p.parse_args()
    act="remove" if a.remove else "apply" if a.apply else "check"
    records=audit(a.source.resolve(),a.dest,act)
    errors=[r for r in records if r["status"] in ("SOURCE_MISSING","CONFLICT_PRESERVED","FAILED")]
    missing=[r for r in records if r["status"]=="MISSING"]
    status="PASS" if not (errors or (a.check and missing)) else "BLOCKED"
    print(json.dumps({"status":status,"action":act,"source":str(a.source.resolve()),"destination":str(a.dest),"entries":records},ensure_ascii=False,indent=2))
    return 0 if status=="PASS" else 2

if __name__=="__main__":
    sys.exit(main())
