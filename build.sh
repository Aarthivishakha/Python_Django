#!/usr/bin/env bash
# Single build entry point: installs deps, builds/tests the real Django
# project (catalog/), then triggers every tool in quality/ against that
# same real project code. Exits non-zero on any failure.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")" && pwd)"
cd "$ROOT"

echo "### [1/3] Installing dependencies"
pip install -r requirements.txt
pip install -r quality/requirements.txt

echo "### [2/3] Django: migrate + test"
python manage.py migrate --noinput
python manage.py test catalog

echo "### [3/3] Triggering every tool in quality/ against catalog/"
for dir in quality/*/; do
    name="$(basename "$dir")"
    [ -f "$dir/trigger.yaml" ] || continue
    cmd=$(grep -A1 '^run:' "$dir/trigger.yaml" | grep 'command:' | sed -E 's/.*command: *"(.*)"/\1/')
    [ -z "$cmd" ] && continue
    echo "=== $name: $cmd ==="
    eval "$cmd"
    echo
done

echo "### BUILD OK"
