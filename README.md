# Django_python

Python/Django project repository — `PYTHON_2.7` branch.

One real, buildable Django project, not a project + a parallel demo
folder. Targets Django 1.11, the final LTS release still supporting
Python 2.7.

## Python 2.7 / Django 1.11 details

- No f-strings or type-hint syntax (Python 3 only); `%`-style formatting
  is used throughout. `catalog/models.py` uses the
  `@python_2_unicode_compatible` decorator + `__str__` (the standard
  Django idiom for a model that works under both Python 2 and 3, since
  1.11 itself still runs on both).
- Every module opens with `from __future__ import unicode_literals` -
  standard Python 2/3-compatible-code practice from this era.
- Unlike the 2.6 branch, Django 1.11 already has `AppConfig` (added
  1.7), the migrations framework (added 1.7), and `DiscoverRunner`
  test-package discovery (default since 1.6) - so this branch does have
  `catalog/apps.py`, `catalog/migrations/`, and a `catalog/tests/`
  package, and the DB is set up with `manage.py migrate`.
- `config/urls.py` and `catalog/urls.py` still use `django.conf.urls`
  regex `url()` routing rather than `path()` - Django 2.0's `path()`
  didn't exist yet, and `patterns()` (used on the 2.6 branch) had
  already been removed in 1.10.
- `config/settings.py` already uses the modern `MIDDLEWARE` list and
  `TEMPLATES` dict (both predate 1.11).

## Layout

- `catalog/` — the real Django app (`pricing.py`, `admin.py`/`exports.py`
  duplication for jscpd, `integrations.py` + an old `requests` pin,
  `tests/`).
- `quality/jscpd/` — the one tool available for Python 2.7 in
  [Golden_Repo_Lite](https://github.com/testable-platform/Golden_Repo_Lite/tree/python/Python_2.7)
  (that repo's Python_2.7 folder has only `jscpd`). `trigger.yaml` +
  `README.md` point it at the real `admin.py`/`exports.py` duplication.

## Build everything with one command

```bash
bash build.sh
# or: make build
```

Installs dependencies, runs `manage.py migrate` + `test catalog`, then
triggers `jscpd` against the real duplicated code. Non-zero exit on any
failure. Requires an actual Python 2.7 interpreter and Node.js (`npx`)
for jscpd.

## Running things individually

```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver        # app at http://127.0.0.1:8000/catalog/products/
npx jscpd --config .jscpd.json
```
