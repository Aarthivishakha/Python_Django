"""Runs beniget's DefUseChains over the real catalog/pricing.py module."""
import json
from os.path import dirname, abspath, join

import gast as ast
from beniget import DefUseChains

ROOT = dirname(dirname(dirname(abspath(__file__))))
TARGET = join(ROOT, 'catalog', 'pricing.py')


def main():
    with open(TARGET) as f:
        source = f.read()
    module = ast.parse(source)
    duc = DefUseChains(filename='pricing.py')
    duc.visit(module)

    dead_defs = []
    for chain in duc.chains.values():
        if not chain.users():
            name = getattr(chain.node, 'id', None) or getattr(chain.node, 'name', None)
            if name:
                dead_defs.append(name)

    print(json.dumps({
        'file': 'catalog/pricing.py',
        'total_def_use_chains': len(duc.chains),
        'dead_defs': sorted(set(dead_defs)),
    }, indent=2))


if __name__ == '__main__':
    main()
