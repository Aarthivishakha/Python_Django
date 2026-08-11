#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")" && pwd)"
cd "$ROOT"
pytest --cov=calculator --cov-branch --cov-report=term-missing test_calculator.py
