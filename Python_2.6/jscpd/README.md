# jscpd — Python 2.6

Code-duplication fixture for jscpd 4.2.5 on Python 2.6.

- `retail_order_processor.py` / `wholesale_order_processor.py` — two small,
  self-contained files sharing one identical block (well over jscpd's
  `minLines: 5` / `minTokens: 50` thresholds), enough to genuinely trigger
  cross-file duplicate detection.
- `run_jscpd.sh` — runs jscpd against this folder.
- `trigger.yaml` — tool/version metadata for this fixture.

Run:
```
bash run_jscpd.sh
```
