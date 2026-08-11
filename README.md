# Django_python

Python/Django project repository — `PYTHON_3.8` branch.

One real, buildable Django project, not a project + a parallel demo
folder. Every analysis tool triggers against the actual project source.
Targets Django 3.2 LTS.

## Python 3.8 syntax used

- `calculate_order_total`'s `quantity, unit_price_cents` are
  positional-only parameters (the `/` marker, PEP 570) - a real
  MC/DC-relevant detail the tests exercise directly
  (`test_quantity_is_positional_only`).
- The walrus operator (`:=`, PEP 572) computes and clamps the discount
  in the same expression: `if (discount := (subtotal * discount_pct) // 100) > subtotal:`.
- The f-string `=` debug specifier (new in 3.8) is used in the
  validation error messages: `f'{quantity=} must be positive'`.

## Layout

- `catalog/` — the real Django app: `pricing.py`, `admin.py`/`exports.py`
  duplication, `integrations.py` + an old `requests` pin,
  `management/commands/mine_history.py` (a real
  `python manage.py mine_history` command and pydriller's actual
  trigger source), and a deliberately partial `tests/` suite.
- `quality/<tool>/` — one folder per tool available for Python 3.8 in
  [Golden_Repo_Lite](https://github.com/testable-platform/Golden_Repo_Lite/tree/python/Python_3.8)
  (4 total, matching that repo's Python_3.8 folder exactly - drops
  `beniget`/`jscpd` and adds `cognitive-ast`/`crosshair`/`radon-lizard`
  versus the 3.7 branch): `cognitive-ast`, `crosshair`, `pydriller`,
  `radon-lizard`. Each holds `trigger.yaml` + `README.md` pointing at
  the real project code above.

## Build everything with one command

```bash
bash build.sh
# or: make build
```

Installs both dependency sets, runs `manage.py migrate` + `test catalog`,
then triggers every tool in `quality/` against the real `catalog/` code.
Non-zero exit on any failure.

## Running things individually

```bash
pip install -r requirements.txt
pip install -r quality/requirements.txt
python manage.py migrate
python manage.py runserver        # app at http://127.0.0.1:8000/catalog/products/
python manage.py mine_history     # pydriller, against this repo's real git log
```
