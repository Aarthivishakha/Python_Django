# Django_python

Python/Django project repository — `PYTHON_3.9` branch.

This branch contains two things integrated as one buildable repo:

1. **A Django project** (`manage.py`, `config/`, `core/`) targeting Python 3.9,
   using Django 4.2 (the last LTS release that still supports 3.9).
2. **`tools/`** — the unique set of Python-analysis tools pulled from
   [testable-platform/Golden_Repo_Lite](https://github.com/testable-platform/Golden_Repo_Lite/tree/python)
   (deduplicated across all Python-version folders in that repo, one copy
   per tool, relabeled for Python 3.9):
   `beniget`, `cognitive-ast` (complexipy), `cosmic-ray`, `coverage-py`,
   `coverage-py-beniget`, `crosshair`, `jscpd`, `pip-audit`, `pydriller`,
   `pylint`, `pymcdc`, `radon-lizard`, `semgrep-bandit`, `testmon`. Each
   subfolder is self-contained with its own README, sample code, run script,
   and `trigger.yaml` describing what the tool checks.

## Build everything with one command

```bash
bash build.sh
# or: make build
```

This installs both dependency sets, runs Django `migrate` + `test`, runs
every tool's official check against its own fixture (`tools/run_all.sh`),
and then runs the applicable tools a second time against the real Django
app code in `core/` (`tools/run_on_project.sh`). Non-zero exit on any
failure.

## Running things individually

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
pip install -r tools/requirements.txt

python manage.py migrate
python manage.py runserver       # Django app at http://127.0.0.1:8000/

bash tools/run_all.sh            # every tool's own check
bash tools/run_on_project.sh     # tools analyzing core/ directly
```

Or run a single tool from inside its folder per its own README, e.g.:

```bash
cd tools/radon-lizard
bash run_radon_lizard.sh
```

Note: `jscpd` requires Node.js (`npx`); `semgrep`/`bandit` and the other
pip-installable tools only need `tools/requirements.txt`.
