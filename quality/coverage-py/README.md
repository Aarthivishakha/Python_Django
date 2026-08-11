# coverage.py — Python 3.12

Runs branch coverage against the real `catalog/pricing.py` module, using
its deliberately partial test suite so the coverage gaps reported are
genuine.

Run from repo root:

```bash
coverage run --branch -m pytest catalog/tests/test_pricing.py
coverage report -m
```
