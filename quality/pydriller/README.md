# pydriller — Python 2.6

A real Django management command
(`catalog/management/commands/mine_history.py`), not a standalone script -
mines this repo's own git history, pydriller's actual trigger source
(it reads git log directly; no fixture file needed).

Run from repo root (requires a Python 3.6+ interpreter to run pydriller
itself, even though the target app is Python 2.6):

```bash
python manage.py mine_history --max-commits 200
```
