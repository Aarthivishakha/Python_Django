#!/usr/bin/env bash
# Runs every tool's own trigger.yaml-defined check against its own fixture.
set -uo pipefail
ROOT="$(cd "$(dirname "$0")" && pwd)"

for dir in "$ROOT"/*/; do
    name="$(basename "$dir")"
    [ -f "$dir/trigger.yaml" ] || continue
    cmd=$(grep -A1 '^run:' "$dir/trigger.yaml" | grep 'command:' | sed -E 's/.*command: *"(.*)"/\1/')
    [ -z "$cmd" ] && continue
    echo "=== $name: $cmd ==="
    (cd "$dir" && eval "$cmd")
    echo
done
