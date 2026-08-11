# semgrep-bandit -- Python 3.10

SAST fixture for Semgrep OSS + Bandit on Python 3.10.

- sast_fixture.py -- a hardcoded admin password (B105), an MD5 weak hash
  (B303/B324), and a string-concatenated SQL query (B608/CWE-89) -- enough
  to genuinely trigger both scanners without the full multi-vulnerability
  gamut.
- run_sast.sh -- runs bandit then semgrep against the fixture.
- trigger.yaml -- tool/version metadata for this fixture.

Run:
bash run_sast.sh
