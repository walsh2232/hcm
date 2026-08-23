# Scripts

Repository tooling. Standard library only — no dependencies to install.

| Script | Purpose |
| --- | --- |
| [`project_lint.py`](project_lint.py) | Validates the project operating system: identifiers, board↔backlog consistency, reference integrity, assumption expiry, ADR structure, WIP limits |

## Running

```bash
python3 scripts/project_lint.py            # from the repository root
python3 scripts/project_lint.py --quiet    # errors only
python3 scripts/project_lint.py --allow-expired   # deliberate override; see below
```

Runs in CI on every push and pull request. A failure is fixed, not bypassed —
`--allow-expired` exists for the case where an assumption renewal is genuinely in
flight in the same change, and its use should be visible in the pull request.
