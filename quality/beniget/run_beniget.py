"""Runs beniget's DefUseChains over the real catalog/pricing.py module."""
import json
from pathlib import Path

import gast as ast
from beniget import DefUseChains

ROOT = Path(__file__).resolve().parents[2]
TARGET = ROOT / "catalog" / "pricing.py"


def main():
    source = TARGET.read_text(encoding="utf-8")
    module = ast.parse(source)
    duc = DefUseChains(filename=TARGET.name)
    duc.visit(module)

    dead_defs = []
    for chain in duc.chains.values():
        if not chain.users():
            name = getattr(chain.node, "id", None) or getattr(chain.node, "name", None)
            if name:
                dead_defs.append(name)

    print(json.dumps({
        "file": str(TARGET.relative_to(ROOT)),
        "total_def_use_chains": len(duc.chains),
        "dead_defs": sorted(set(dead_defs)),
    }, indent=2))


if __name__ == "__main__":
    main()
