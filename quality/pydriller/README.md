# pydriller — Python 3.10

A real Django management command
(`catalog/management/commands/mine_history.py`), not a standalone script -
mines this repo's own git history, pydriller's actual trigger source
(it reads git log directly; no fixture file needed).

Run from repo root:

```bash
python manage.py mine_history --max-commits 200
```
