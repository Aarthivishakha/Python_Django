# testmon -- Python 3.11

Selective-test-rerun fixture for pytest-testmon 2.2.0 on Python 3.11.

- util_functions.py / test_util_functions.py -- a minimal module + test
  pair; testmon records which tests depend on which lines so future changes
  only re-run affected tests.
- run_testmon.sh -- runs pytest with --testmon.
- trigger.yaml -- tool/version metadata for this fixture.

Run:
bash run_testmon.sh
