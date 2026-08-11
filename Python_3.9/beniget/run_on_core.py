"""Runs Beniget's DefUseChains over the real Django app (core/) to report
dead definitions in project code, complementing run_beniget.py (which runs
the same analysis against this folder's own def_use_analysis.py fixture).

Usage:
    python Python_3.9/beniget/run_on_core.py
"""
import json
from pathlib import Path

import gast as ast
from beniget import DefUseChains

ROOT = Path(__file__).resolve().parents[2]
CORE = ROOT / "core"


def analyze_file(path):
    source = path.read_text(encoding="utf-8")
    module = ast.parse(source)
    duc = DefUseChains(filename=path.name)
    duc.visit(module)

    dead_defs = []
    for chain in duc.chains.values():
        if not chain.users():
            name = getattr(chain.node, "id", None) or getattr(chain.node, "name", None)
            if name:
                dead_defs.append(name)
    return len(duc.chains), sorted(set(dead_defs))


def main():
    targets = sorted(p for p in CORE.glob("*.py"))
    report = {}
    for path in targets:
        chains, dead = analyze_file(path)
        report[path.name] = {"total_def_use_chains": chains, "dead_defs": dead}
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
