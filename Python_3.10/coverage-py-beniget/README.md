# coverage-py-beniget — Python 3.10

Combined coverage + data-flow fixture on Python 3.10 — one minimal file
analyzed by both coverage.py (branch coverage via its test) and Beniget
(def-use chains, including the dead `unused_note`).

- `combined_analysis.py` — a branching function with one dead definition.
- `test_combined_analysis.py` — exercises both branches.
- `run_coverage_beniget.sh` — runs coverage.py, then Beniget, over the
  same file.
- `trigger.yaml` — tool/version metadata for this fixture.

Run:
```
bash run_coverage_beniget.sh
```
