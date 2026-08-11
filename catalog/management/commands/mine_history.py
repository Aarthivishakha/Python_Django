"""Real Django management command: `python manage.py mine_history`.

Mines this project's own git commit history via pydriller and reports
per-file churn. This is genuine project tooling, and it's also pydriller's
trigger source - it reads git log directly, so no separate fixture file
is needed.
"""
from __future__ import annotations

import json
from collections import defaultdict
from pathlib import Path

from django.core.management.base import BaseCommand
from pydriller import Repository


class Command(BaseCommand):
    help = "Report per-file git churn for this project using pydriller."

    def add_arguments(self, parser):
        parser.add_argument("--max-commits", type=int, default=200)

    def handle(self, *args, **options):
        root = Path(__file__).resolve().parents[4]
        churn: dict[str, dict[str, int]] = defaultdict(lambda: {"commits": 0, "added": 0, "removed": 0})
        commits_seen = 0

        for commit in Repository(str(root)).traverse_commits():
            commits_seen += 1
            for mod in commit.modified_files:
                path = mod.new_path or mod.old_path
                if not path:
                    continue
                path = path.replace("\\", "/")
                churn[path]["commits"] += 1
                churn[path]["added"] += mod.added_lines
                churn[path]["removed"] += mod.deleted_lines
            if commits_seen >= options["max_commits"]:
                break

        top_churned = sorted(churn.items(), key=lambda kv: kv[1]["commits"], reverse=True)[:10]
        summary = {
            "commits_analyzed": commits_seen,
            "files_touched": len(churn),
            "top_churned_files": [{"path": p, **stats} for p, stats in top_churned],
        }
        self.stdout.write(json.dumps(summary, indent=2))
