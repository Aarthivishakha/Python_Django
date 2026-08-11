# Django_python

Python/Django project repository — `PYTHON_3.13` branch.

One real, buildable Django project, not a project + a parallel demo
folder. Every analysis tool triggers against the actual project source,
and the code uses Python 3.13 syntax where it fits naturally.

## Python 3.13 syntax used

- `catalog/pricing.py::classify_order_size` is a `match` statement
  (PEP 634).
- `calculate_order_total`'s `coupon_code` parameter uses the PEP 604
  `str | None` union syntax directly.
- `OrderQuote.from_request` is a classmethod returning `typing.Self`
  (PEP 673).
- `type Cents = int` is a PEP 695 `type` alias statement (3.12+).
- `QuoteCache[T = OrderQuote]` uses a PEP 696 generic type-parameter
  default (new in 3.13) — `QuoteCache()` with no explicit type argument
  defaults to caching `OrderQuote` instances, which is exactly how
  `views.py::quote` uses it as a real per-request quote cache.

## Layout

- `catalog/` — the real Django app (`pricing.py`, `admin.py`/`exports.py`
  duplication for jscpd-style tools, `integrations.py` + an old `requests`
  pin for pip-audit, a deliberately partial `tests/` suite).
- `config/settings.py` has a hardcoded `SECRET_KEY` — a real SAST finding.
- `quality/<tool>/` — all 14 tools from
  [Golden_Repo_Lite](https://github.com/testable-platform/Golden_Repo_Lite/tree/python)
  (not just the 9 that repo's own Python_3.13 folder lists): `beniget`,
  `cognitive-ast`, `cosmic-ray`, `coverage-py`, `coverage-py-beniget`,
  `crosshair`, `jscpd`, `pip-audit`, `pydriller`, `pylint`, `pymcdc`,
  `radon-lizard`, `semgrep-bandit`, `testmon`. Each holds `trigger.yaml`
  + `README.md` pointing at the real project code above.

## Build everything with one command

```bash
bash build.sh
# or: make build
```

Installs both dependency sets, runs `manage.py check` + `migrate` +
`test catalog`, then triggers every tool in `quality/` against the real
`catalog/` code. Non-zero exit on any failure.

## Running things individually

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
pip install -r quality/requirements.txt

python manage.py migrate
python manage.py runserver       # app at http://127.0.0.1:8000/catalog/products/
```
