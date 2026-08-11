# coverage.py + beniget — Python 2.6

Combines branch coverage (via `manage.py test catalog`) and dead-def
detection against the real `catalog/pricing.py` module.

Run from repo root:

```bash
coverage run --branch manage.py test catalog
coverage report -m
python quality/beniget/run_beniget.py
```
