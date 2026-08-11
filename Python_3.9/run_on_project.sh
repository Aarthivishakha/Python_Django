#!/usr/bin/env bash
# Runs the subset of Python_3.9/ tools that can meaningfully analyze source
# code against the real Django app (core/), not just each tool's own bundled
# fixture. Complements run_all.sh (which runs each tool's official
# trigger.yaml-defined check against its own fixture) rather than replacing it.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
TARGETS="$ROOT/core/models.py $ROOT/core/views.py $ROOT/core/urls.py $ROOT/core/admin.py $ROOT/core/apps.py"

echo "=== radon (cyclomatic complexity) on core/ ==="
radon cc $TARGETS -s -a

echo
echo "=== lizard on core/ ==="
lizard $TARGETS

echo
echo "=== complexipy (cognitive complexity) on core/ ==="
complexipy $TARGETS

echo
echo "=== beniget (def-use / dead defs) on core/ ==="
python "$ROOT/Python_3.9/beniget/run_on_core.py"
