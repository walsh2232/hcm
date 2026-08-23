# Testing

```
tests/strategy.md        Test strategy (owned by HCM-015)
tests/defects.md         Defect log
tests/<MODULE>/cases/    Test cases, one file per case (templates/test-case.md)
tests/<MODULE>/automation/  Automated checks, where automation is viable
```

## Levels

Established by `HCM-015`. Expected shape for an Oracle HCM implementation:
unit/configuration, functional, integration, payroll parallel (where payroll is in
scope), security and role testing, UAT, and regression against Oracle quarterly
updates.

Each level has written entry and exit criteria. **QA owns the pass/fail verdict**
and it is not overridable by another role (`../.project/roles.md`) — it is
escalatable, which is a different thing.

## Rules

- Every test case traces to a requirement (`REQ-<MOD>-###`), and every requirement
  has at least one case. A requirement with no test is a requirement nobody
  intends to verify.
- Expected results are observable. "Works correctly" is not an expected result.
- **Synthetic data only** (`../data/README.md`). Payroll and absence scenarios are
  the usual temptation and the usual breach.
- A defect is closed by a passing re-test, not by an explanation.
- Regression scope is decided per case, not assumed — see the `Regression` section
  of the test case template.
