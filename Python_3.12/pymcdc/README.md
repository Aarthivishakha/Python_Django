# pymcdc -- Python 3.12

MC/DC condition-coverage fixture for pymcdc 0.2.5 on Python 3.12.

- mcdc_decision.py -- a compound and/or decision
  (score >= 75 and (is_bonus or is_premium)).
- test_mcdc_decision.py -- test cases covering each independent condition's
  effect on the outcome (MC/DC requirements).
- run_pymcdc.sh -- runs pymcdc against the decision using the test file.
- trigger.yaml -- tool/version metadata for this fixture.

Run:
bash run_pymcdc.sh
