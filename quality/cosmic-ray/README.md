# cosmic-ray — Python 2.6

Runs mutation testing against the real `catalog/pricing.py` module,
using `python manage.py test catalog` (Django 1.5's own test runner,
via `catalog/tests.py`) as the killing test suite.

Run from repo root:

```bash
cosmic-ray init cosmic-ray.toml session.sqlite
cosmic-ray exec cosmic-ray.toml session.sqlite
cr-report session.sqlite
```
