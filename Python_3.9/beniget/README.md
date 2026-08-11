# beniget — Python 3.9

Data-flow (def-use chain) fixture for Beniget 0.5.0 on Python 3.9.

- `def_use_analysis.py` — a minimal module with intentional dead definitions
  (`unused_currency_symbol`, `_draft_notes`, `unused_prefix` are assigned but
  never read), enough to genuinely trigger Beniget's All-Defs / All-Uses
  dead-definition detection.
- `run_beniget.py` — runs `DefUseChains` over `def_use_analysis.py` and
  reports total def-use chains plus which definitions are dead.
- `trigger.yaml` — tool/version metadata for this fixture.

Run:
```
python run_beniget.py
```
