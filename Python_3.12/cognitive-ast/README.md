# cognitive-ast — Python 3.12

Cognitive-complexity fixture for complexipy on Python 3.12.

- `complexity_sample.py` — a single function with four levels of nested
  conditionals, enough to genuinely trigger a high cognitive-complexity
  score.
- `run_complexipy.sh` — runs complexipy against the fixture.
- `trigger.yaml` — tool/version metadata for this fixture.

Run:
```
bash run_complexipy.sh
```
