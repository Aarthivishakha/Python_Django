# Django_python

Python/Django project repository — `PYTHON_3.7` branch.

One real, buildable Django project, not a project + a parallel demo
folder. Every analysis tool triggers against the actual project source.
Targets Django 3.0.

## Python 3.7 syntax used

- Variable annotations and f-strings carry over from the 3.6 branch.
- `OrderQuote` in `catalog/pricing.py` is a `@dataclass` (PEP 557,
  new exactly in Python 3.7) - the standard way to get
  `__init__`/`__repr__`/`__eq__` for free before `typing.Self` existed
  (added in 3.11, not usable here; `from_request` returns the literal
  `'OrderQuote'` forward-reference string instead).

## Layout

- `catalog/` — the real Django app: `pricing.py`, `admin.py`/`exports.py`
  duplication, `integrations.py` + an old `requests` pin,
  `management/commands/mine_history.py` (a real
  `python manage.py mine_history` command and pydriller's actual
  trigger source), and a deliberately partial `tests/` suite.
- `quality/<tool>/` — one folder per tool available for Python 3.7 in
  [Golden_Repo_Lite](https://github.com/testable-platform/Golden_Repo_Lite/tree/python/Python_3.7)
  (2 total, matching that repo's Python_3.7 folder exactly - drops
  `jscpd` versus the 3.6 branch): `beniget`, `pydriller`. Each holds
  `trigger.yaml` + `README.md` pointing at the real project code above.

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
