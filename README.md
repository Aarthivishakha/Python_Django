# Django_python

Python/Django project repository — `PYTHON_3.5` branch.

One real, buildable Django project, not a project + a parallel demo
folder. Targets Django 1.11, the same LTS as the 2.7/3.4 branches -
it supports Python 2.7, 3.4, 3.5, and 3.6 in one release.

## Python 3.5 details

- No f-strings or variable annotations (both added in Python 3.6) -
  `%`-style formatting is used instead throughout `catalog/`.
- The `typing` module was introduced exactly in Python 3.5 (PEP 484),
  so `catalog/pricing.py::calculate_order_total` and
  `catalog/integrations.py::fetch_usd_rate` carry real type comments
  (`# type: (...) -> ...`) using `typing.Optional` - the standard way
  to add type hints to already-3.4-style code without variable
  annotation syntax (3.6+).
- `catalog/pricing.py::classify_order_size` is plain if/elif - no
  `match` statement (added in 3.10).
- `config/urls.py` and `catalog/urls.py` use `django.conf.urls` regex
  `url()` routing (`path()` wasn't added until Django 2.0).

## Layout

- `catalog/` — the real Django app (`pricing.py`, `admin.py`/`exports.py`
  duplication for jscpd, `integrations.py` + an old `requests` pin,
  `tests/`).
- `quality/jscpd/` — the one tool available for Python 3.5 in
  [Golden_Repo_Lite](https://github.com/testable-platform/Golden_Repo_Lite/tree/python/Python_3.5)
  (that repo's Python_3.5 folder has only `jscpd`). `trigger.yaml` +
  `README.md` point it at the real `admin.py`/`exports.py` duplication.

## Build everything with one command

```bash
bash build.sh
# or: make build
```

Installs dependencies, runs `manage.py migrate` + `test catalog`, then
triggers `jscpd` against the real duplicated code. Non-zero exit on any
failure. Requires an actual Python 3.5 interpreter and Node.js (`npx`)
for jscpd.

## Running things individually

```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver        # app at http://127.0.0.1:8000/catalog/products/
npx jscpd --config .jscpd.json
```
