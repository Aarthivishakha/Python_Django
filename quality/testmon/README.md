# testmon — Python 3.13

Records which tests cover which lines of `catalog/pricing.py`, for
selective re-running on future changes.

Run from repo root:

```bash
pytest --testmon catalog/tests/test_pricing.py
```
