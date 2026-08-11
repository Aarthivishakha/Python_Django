#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")" && pwd)"
cd "$ROOT"
if ! command -v npx &>/dev/null; then
    echo "jscpd requires Node.js — install Node.js to enable (npx not found)." >&2
    exit 1
fi
npx jscpd --languages python --min-lines 5 --min-tokens 50 --reporters console,json .
