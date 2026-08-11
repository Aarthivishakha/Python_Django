# radon + lizard — Python 3.10

Reports cyclomatic complexity for `catalog/pricing.py::classify_order_size`
(a `match` statement) and `calculate_order_total`.

Run from repo root:

```bash
radon cc catalog/pricing.py -s -a
lizard catalog/pricing.py
```
