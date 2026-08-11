"""Runs Beniget's DefUseChains over def_use_analysis.py and reports how many
def-use chains are dead (assigned but never read).

Usage:
    python run_beniget.py
"""
import json
from pathlib import Path

import gast as ast
from beniget import DefUseChains

TARGET = Path(__file__).resolve().parent / "def_use_analysis.py"


def analyze_file(path):
    source = path.read_text(encoding='utf-8')
    module = ast.parse(source)
    duc = DefUseChains(filename=path.name)
    duc.visit(module)

    dead_defs = []
    for chain in duc.chains.values():
        if not chain.users():
            name = getattr(chain.node, 'id', None) or getattr(chain.node, 'name', None)
            if name:
                dead_defs.append(name)
    return len(duc.chains), sorted(set(dead_defs))


def main():
    chains, dead = analyze_file(TARGET)
    summary = {
        'file': TARGET.name,
        'total_def_use_chains': chains,
        'dead_defs': dead,
    }
    print(json.dumps(summary, indent=2))


if __name__ == '__main__':
    main()
