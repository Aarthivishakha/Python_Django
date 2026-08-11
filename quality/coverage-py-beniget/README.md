# coverage.py + beniget — Python 3.5

Combines branch coverage and dead-def detection against the real
`catalog/pricing.py` module.

Run from repo root:

```bash
coverage run --branch -m pytest catalog/tests/test_pricing.py
coverage report -m
python quality/beniget/run_beniget.py
```
