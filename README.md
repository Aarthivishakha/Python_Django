# Django_python

Python/Django project repository — `PYTHON_3.16` branch.

One real, buildable Django project, not a project + a parallel demo
folder. Every analysis tool triggers against the actual project source,
and every analysis tool triggers against the actual project source.

## Python syntax used

Carries forward every feature confirmed through 3.13 (`match` statement,
PEP 604 unions, `typing.Self`, the PEP 695 `type` alias, and the PEP 696
generic default on `QuoteCache`). This branch was built after this
assistant's training cutoff, so no 3.14/3.15/3.16-specific language
feature is claimed here with confidence - any such addition isn't
reflected in this code and would need verifying against real release
notes.

## Layout

- `catalog/` — the real Django app (`pricing.py`, `admin.py`/`exports.py`
  duplication for jscpd-style tools, `integrations.py` + an old `requests`
  pin for pip-audit, a deliberately partial `tests/` suite).
- `config/settings.py` has a hardcoded `SECRET_KEY` — a real SAST finding.
- `quality/<tool>/` — all 14 tools from
  [Golden_Repo_Lite](https://github.com/testable-platform/Golden_Repo_Lite/tree/python)
  (not just the 2 - `coverage-py`, `coverage-py-beniget` - that repo's
  own Python_3.16 folder lists): `beniget`,
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
