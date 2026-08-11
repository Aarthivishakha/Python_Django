#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")" && pwd)"
cd "$ROOT"
radon cc complexity_sample.py -s -a
lizard complexity_sample.py
