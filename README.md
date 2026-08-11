# Django_python

Python/Django project repository — `PYTHON_3.6` branch.

One real, buildable Django project, not a project + a parallel demo
folder. Every analysis tool triggers against the actual project source.
Targets Django 2.2 LTS.

## Python 3.6 syntax used

- Variable annotations (PEP 526) throughout `catalog/pricing.py`, e.g.
  `MEMBER_DISCOUNT_PCT: int = 10`.
- f-strings (PEP 498) in `calculate_order_total`'s error messages.
- `classify_order_size` is still plain if/elif - no `match` statement
  (added in 3.10).

## Layout

- `catalog/` — the real Django app: `pricing.py`, `admin.py`/`exports.py`
  duplication for jscpd, `integrations.py` + an old `requests` pin,
  `management/commands/mine_history.py` (a real
  `python manage.py mine_history` command and pydriller's actual
  trigger source), and a deliberately partial `tests/` suite.
- `config/urls.py` uses `path()`/`include()` (added in Django 2.0) -
  the first branch in this progression to use it, replacing the regex
  `url()` routing on the 2.6-3.5 branches.
- `quality/<tool>/` — one folder per tool available for Python 3.6 in
  [Golden_Repo_Lite](https://github.com/testable-platform/Golden_Repo_Lite/tree/python/Python_3.6)
  (3 total, matching that repo's Python_3.6 folder exactly): `beniget`,
  `jscpd`, `pydriller`. Each holds `trigger.yaml` + `README.md` pointing
  at the real project code above.

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
npx jscpd --config .jscpd.json    # requires Node.js
```
