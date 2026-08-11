#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")" && pwd)"
cd "$ROOT"
pytest --cov=combined_analysis --cov-branch --cov-report=term-missing test_combined_analysis.py
python -c "
import gast as ast
from beniget import DefUseChains
src = open('combined_analysis.py').read()
module = ast.parse(src)
duc = DefUseChains(filename='combined_analysis.py')
duc.visit(module)
print('def-use chains:', len(duc.chains))
"
