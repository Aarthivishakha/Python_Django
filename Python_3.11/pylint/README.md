# pylint -- Python 3.11

Lint-violation fixture for pylint 4.0.6 on Python 3.11.

- lint_violations.py -- mixed naming conventions (getUserName camelCase
  vs get_user_age snake_case, C0103), an unused variable (temp, F841/
  W0612), and mixed quote styles, enough to genuinely trigger multiple
  pylint rule categories.
- run_pylint.sh -- runs pylint against the fixture.
- trigger.yaml -- tool/version metadata for this fixture.

Run:
bash run_pylint.sh
