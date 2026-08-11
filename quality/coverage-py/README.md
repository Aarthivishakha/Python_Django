# coverage.py — Python 2.6

Runs branch coverage against the real `catalog/tests.py` suite (wrapping
`manage.py test catalog`, Django 1.5's own runner).

Run from repo root:

```bash
coverage run --branch manage.py test catalog
coverage report -m
```
