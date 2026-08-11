# Django_python

Python/Django project repository — `PYTHON_3.9` branch.

This branch contains two things side by side:

1. **A Django project** (`manage.py`, `config/`, `core/`) targeting Python 3.9,
   using Django 4.2 (the last LTS release that still supports 3.9).
2. **`Python_3.9/`** — the Python 3.9 tool suite pulled from
   [testable-platform/Golden_Repo_Lite](https://github.com/testable-platform/Golden_Repo_Lite/tree/python/Python_3.9):
   `beniget`, `cognitive-ast` (complexipy), `cosmic-ray`, `crosshair`,
   `pydriller`, and `radon-lizard`. Each subfolder is self-contained with its
   own README, sample code, run script, and `trigger.yaml` describing what the
   tool checks.

## Running the Django project

```bash
python -m venv .venv
source .venv/bin/activate   # or .venv\Scripts\activate on Windows
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Requires Python 3.9+ (tested against 3.9).

## Running the Python 3.9 tool suite

```bash
pip install -r Python_3.9/requirements.txt
bash Python_3.9/run_all.sh
```

Or run an individual tool from inside its folder per its own README, e.g.:

```bash
cd Python_3.9/radon-lizard
bash run_radon_lizard.sh
```
