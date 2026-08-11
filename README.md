# Django_python

Python/Django project repository — `PYTHON_3.4` branch.

One real, buildable Django project, not a project + a parallel demo
folder. Targets Django 1.11, the same LTS as the 2.7/3.5 branches -
it supports Python 2.7, 3.4, 3.5, and 3.6 in one release.

## Python 3.4 details

- No f-strings or variable annotations (both added in Python 3.6) -
  `%`-style formatting is used instead throughout `catalog/`.
- `catalog/models.py` uses plain `__str__` (no
  `@python_2_unicode_compatible` needed - unlike the 2.7 branch, this
  one only has to run under Python 3).
- `catalog/pricing.py::classify_order_size` is plain if/elif - no
  `match` statement (added in 3.10).
- `config/urls.py` and `catalog/urls.py` use `django.conf.urls` regex
  `url()` routing (`path()` wasn't added until Django 2.0, and this
  Django release - 1.11 - doesn't support it anyway).
- `config/settings.py` already uses the modern `MIDDLEWARE` list and
  `TEMPLATES` dict.

## Layout

- `catalog/` — the real Django app (`pricing.py`, `admin.py`/`exports.py`
  duplication for jscpd, `integrations.py` + an old `requests` pin,
  `tests/`).
- `quality/jscpd/` — the one tool available for Python 3.4 in
  [Golden_Repo_Lite](https://github.com/testable-platform/Golden_Repo_Lite/tree/python/Python_3.4)
  (that repo's Python_3.4 folder has only `jscpd`). `trigger.yaml` +
  `README.md` point it at the real `admin.py`/`exports.py` duplication.

## Build everything with one command

```bash
bash build.sh
# or: make build
```

Installs dependencies, runs `manage.py migrate` + `test catalog`, then
triggers `jscpd` against the real duplicated code. Non-zero exit on any
failure. Requires an actual Python 3.4 interpreter and Node.js (`npx`)
for jscpd.

## Running things individually

```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver        # app at http://127.0.0.1:8000/catalog/products/
npx jscpd --config .jscpd.json
```
