# cosmic-ray — Python 3.12

Runs mutation testing against the real `catalog/pricing.py` module, using
`catalog/tests/test_pricing.py` as the killing test suite (see
`cosmic-ray.toml` at the repo root).

Run from repo root:

```bash
cosmic-ray init cosmic-ray.toml session.sqlite
cosmic-ray exec cosmic-ray.toml session.sqlite
cr-report session.sqlite
```
