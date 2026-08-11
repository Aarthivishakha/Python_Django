# coverage-py — Python 3.11

Statement/branch coverage fixture for coverage.py 7.14.1 on Python 3.11.

- `calculator.py` — arithmetic functions including one raising branch
  (`divide` by zero).
- `test_calculator.py` — tests that exercise both the normal and the
  error branch.
- `run_coverage.sh` — runs pytest with `--cov-branch`.
- `trigger.yaml` — tool/version metadata for this fixture.

Run:
```
bash run_coverage.sh
```
