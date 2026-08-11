# pymcdc — Python 3.10

Checks MC/DC condition coverage of `calculate_order_total`'s compound
boolean decision against the real `catalog/tests/test_pricing.py` suite.

Run from repo root:

```bash
python -m pymcdc --unittest catalog.tests.test_pricing catalog/pricing.py
```
