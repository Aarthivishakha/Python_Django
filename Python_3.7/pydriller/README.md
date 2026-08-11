# pydriller — Python 3.7

Code-churn fixture for PyDriller 2.9 on Python 3.7.

- `run_pydriller.py` — mines this repo's own real git commit history via
  `Repository('.').traverse_commits()` and reports per-file churn. PyDriller
  operates on git log, not source code, so this is the only file needed —
  there is no separate fixture source file.
- `trigger.yaml` — tool/version metadata for this fixture.

Run:
```
python run_pydriller.py
```
