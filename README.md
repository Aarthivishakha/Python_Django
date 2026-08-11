# Django_python

Python/Django project repository — `PYTHON_2.6` branch.

One real, buildable Django project (not a project + a parallel demo
folder), written in genuine Python 2.6 / Django 1.5 style — the last
Django release to support Python 2.6.

## Python 2.6 / Django 1.5 era details

- No f-strings, type-hint syntax, or `__str__`-only convention (all
  Python 3 only) - `%`-style formatting and `__unicode__` are used
  instead, matching how Django itself worked at the time.
- No set/dict comprehensions (added in Python 2.7) anywhere in
  `catalog/`.
- Django 1.5 predates `AppConfig` (added in 1.7), the migrations
  framework (added in 1.7), and `DiscoverRunner`-based test packages
  (default from 1.6) - so there's no `catalog/apps.py`, no
  `catalog/migrations/`, and tests live in a single `catalog/tests.py`
  rather than a `tests/` package. The database is set up with
  `manage.py syncdb`, not `manage.py migrate`.
- `config/urls.py` and `catalog/urls.py` use the era's
  `django.conf.urls.patterns()` + regex `url()` routing (removed in
  Django 1.10, long before `path()` existed in 2.0).
- `config/settings.py` uses `MIDDLEWARE_CLASSES` (renamed to
  `MIDDLEWARE` in 1.10) and `TEMPLATE_DIRS` (superseded by the
  `TEMPLATES` dict in 1.8).

## Layout

- `catalog/` — the real Django app (`pricing.py`, `admin.py`/`exports.py`
  duplication for jscpd, `integrations.py` + an old `requests` pin,
  `tests.py`).
- `quality/jscpd/` — the one tool available for Python 2.6 in
  [Golden_Repo_Lite](https://github.com/testable-platform/Golden_Repo_Lite/tree/python/Python_2.6)
  (that repo's Python_2.6 folder has only `jscpd`). `trigger.yaml` +
  `README.md` point it at the real `admin.py`/`exports.py` duplication.

## Build everything with one command

```bash
bash build.sh
# or: make build
```

Installs dependencies, runs `manage.py syncdb` + `test catalog`, then
triggers `jscpd` against the real duplicated code. Non-zero exit on any
failure. Requires an actual Python 2.6 interpreter and Node.js (`npx`)
for jscpd - **GitHub-hosted Actions runners can no longer provision
Python 2.6**, so `.github/workflows/build.yml` is included for branch
consistency but will likely fail to set up its Python step there; run
`build.sh` locally under real Python 2.6 instead.

## Running things individually

```bash
pip install -r requirements.txt
python manage.py syncdb
python manage.py runserver        # app at http://127.0.0.1:8000/catalog/products/
npx jscpd --config .jscpd.json
```
