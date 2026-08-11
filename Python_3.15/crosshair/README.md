# crosshair — Python 3.15

Symbolic-execution contract fixture for CrossHair on Python 3.15.

- `contract_examples.py` — two type-hinted functions with `pre:`/`post:`
  contracts in their docstrings (CrossHair's condition syntax), enough to
  genuinely trigger symbolic path exploration and contract verification.
- `run_crosshair.sh` — runs `crosshair check` against the fixture.
- `trigger.yaml` — tool/version metadata for this fixture.

Run:
```
bash run_crosshair.sh
```
