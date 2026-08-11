# Django_python

Python/Django project repository — `PYTHON_3.9` branch.

One real, buildable Django project, not a project + a parallel demo
folder. Every analysis tool triggers against the actual project source.

## Layout

- `catalog/` — the real Django app.
  - `pricing.py` — real order-pricing logic (`calculate_order_total` has
    4 independent boolean inputs, a genuine MC/DC and mutation-testing
    target; `classify_order_size` has real branching complexity).
  - `admin.py` duplicates `exports.py`'s CSV logic — a real copy-paste
    anti-pattern for jscpd, not staged.
  - `integrations.py` uses the `requests` dependency pinned in
    `requirements.txt` to an old release with published CVEs — a real
    pip-audit target.
  - `management/commands/mine_history.py` — a real Django management
    command (`python manage.py mine_history`), and pydriller's actual
    trigger source (it reads this repo's own git history).
  - `tests/` — a deliberately partial test suite; coverage and MC/DC
    gaps are genuine, not manufactured.
- `config/settings.py` has a hardcoded `SECRET_KEY` — a real SAST finding
  for bandit/semgrep.
- `quality/<tool>/` — one folder per tool (14 total, everything from
  [Golden_Repo_Lite](https://github.com/testable-platform/Golden_Repo_Lite)'s
  python tool set), each holding `trigger.yaml` + `README.md` describing
  the exact command run against the real project above:
  `beniget`, `cognitive-ast`, `cosmic-ray`, `coverage-py`,
  `coverage-py-beniget`, `crosshair`, `jscpd`, `pip-audit`, `pydriller`,
  `pylint`, `pymcdc`, `radon-lizard`, `semgrep-bandit`, `testmon`.

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

python manage.py mine_history    # pydriller, against this repo's real git log
```

Or run a single tool per its own README, e.g.:

```bash
radon cc catalog/pricing.py -s -a
```

Note: `jscpd` requires Node.js (`npx`); everything else only needs
`quality/requirements.txt`.
