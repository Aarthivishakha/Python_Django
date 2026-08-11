#!/usr/bin/env bash
set -uo pipefail
ROOT="$(cd "$(dirname "$0")" && pwd)"

for dir in "$ROOT"/*/; do
    name="$(basename "$dir")"
    cmd=$(grep -A1 '^run:' "$dir/trigger.yaml" | grep 'command:' | sed -E 's/.*command: *"(.*)"/\1/')
    [ -z "$cmd" ] && continue
    echo "=== $name: $cmd ==="
    (cd "$dir" && eval "$cmd")
    echo
done
