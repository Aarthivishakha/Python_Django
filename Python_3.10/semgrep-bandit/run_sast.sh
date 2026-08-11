#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")" && pwd)"
cd "$ROOT"
bandit -r sast_fixture.py -f json
semgrep --config auto sast_fixture.py --json
