# semgrep + bandit — Python 3.6

Runs SAST against the real `catalog/` and `config/` code, including the
intentionally hardcoded `SECRET_KEY` in `config/settings.py`.

Run from repo root:

```bash
bandit -r catalog config
semgrep --config auto catalog config
```
