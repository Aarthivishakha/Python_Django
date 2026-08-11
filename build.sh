#!/usr/bin/env bash
# Single build entry point for this branch: builds/verifies the Django
# project AND the Python_3.9 tool suite (both against their own fixtures
# and against the real app code) as one unit. Exits non-zero on any failure.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")" && pwd)"
cd "$ROOT"

echo "### [1/5] Installing dependencies"
pip install -r requirements.txt
pip install -r Python_3.9/requirements.txt

echo "### [2/5] Django: migrate"
python manage.py migrate --noinput

echo "### [3/5] Django: test"
python manage.py test

echo "### [4/5] Python_3.9 tool suite: official per-tool checks"
bash Python_3.9/run_all.sh

echo "### [5/5] Python_3.9 tool suite: analysis against the real Django app"
bash Python_3.9/run_on_project.sh

echo "### BUILD OK"
