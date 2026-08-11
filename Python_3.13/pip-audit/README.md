# pip-audit -- Python 3.13

Dependency-vulnerability fixture for pip-audit 2.10.1 on Python 3.13.

- requirements.txt -- pins requests==2.25.1 and urllib3==1.26.4,
  both with known published CVEs, enough to genuinely trigger findings.
- run_pip_audit.sh -- runs pip-audit against the requirements file.
- trigger.yaml -- tool/version metadata for this fixture.

Run:
bash run_pip_audit.sh
