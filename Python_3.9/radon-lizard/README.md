# radon-lizard — Python 3.9

Cyclomatic-complexity fixture for radon and lizard on Python 3.9.

- `complexity_sample.py` — a single function with multiple branches
  (grade thresholds, bonus/premium/attendance modifiers), enough to
  genuinely trigger a CC score well above 1.
- `run_radon_lizard.sh` — runs both radon and lizard against the fixture.
- `trigger.yaml` — tool/version metadata for this fixture.

Run:
```
bash run_radon_lizard.sh
```
