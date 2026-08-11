#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")" && pwd)"
cd "$ROOT"
python -m pymcdc --unittest test_mcdc_decision.py mcdc_decision.py
