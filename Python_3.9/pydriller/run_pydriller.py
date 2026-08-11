"""Mines this repo's own real git history with pydriller.

Repository('.').traverse_commits() walks every real commit reachable from
this branch and computes per-file churn (lines added/removed), proving
pydriller triggers against genuine repository history rather than
synthetic data. It reads git log directly, so it needs no source fixture
of its own.

Usage:
    python run_pydriller.py
"""
import json
from collections import defaultdict
from pathlib import Path

from pydriller import Repository

ROOT = Path(__file__).resolve().parents[2]


def main(max_commits=200):
    churn = defaultdict(lambda: {'commits': 0, 'added': 0, 'removed': 0})
    commits_seen = 0

    for commit in Repository(str(ROOT)).traverse_commits():
        commits_seen += 1
        for mod in commit.modified_files:
            path = mod.new_path or mod.old_path
            if not path:
                continue
            path = path.replace('\', '/')
            churn[path]['commits'] += 1
            churn[path]['added'] += mod.added_lines
            churn[path]['removed'] += mod.deleted_lines
        if commits_seen >= max_commits:
            break

    top_churned = sorted(churn.items(), key=lambda kv: kv[1]['commits'], reverse=True)[:10]
    summary = {
        'commits_analyzed': commits_seen,
        'files_touched': len(churn),
        'top_churned_files': [{'path': p, **stats} for p, stats in top_churned],
    }
    print(json.dumps(summary, indent=2))


if __name__ == '__main__':
    main()
