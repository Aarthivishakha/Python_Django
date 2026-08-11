# cosmic-ray — Python 3.11

Mutation-testing fixture for cosmic-ray 8.4.6 on Python 3.11.

- `calculator.py` — two tiny functions to mutate.
- `test_calculator.py` — tests tight enough to kill mutants (e.g. `+` -> `-`,
  `==` -> `!=`).
- `cosmic-ray.toml` — session config pointing at the module and test command.
- `run_cosmic_ray.sh` — init + exec + report.
- `trigger.yaml` — tool/version metadata for this fixture.

Run:
```
bash run_cosmic_ray.sh
```
