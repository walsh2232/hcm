# Project Operating System

This directory is how the project runs. It is version-controlled alongside the
solution so that a decision, the evidence behind it, and the artifact it produced
always travel together.

| File / directory | Purpose |
| --- | --- |
| [`kanban.md`](kanban.md) | Current board state. The single view of work in flight. |
| [`backlog.md`](backlog.md) | Prioritized future work, refined top-down. |
| [`roles.md`](roles.md) | Role charters, decision rights, RACI, escalation paths. |
| [`workflow.md`](workflow.md) | Board states, WIP limits, transition rules, DoR/DoD. |
| [`decision-framework.md`](decision-framework.md) | How a decision is validated against official Oracle documentation. |
| [`risks.md`](risks.md) | Risk register. |
| [`glossary.md`](glossary.md) | Oracle HCM and project terminology. |
| [`docs/`](docs/) | Documentation ingest system, source registry, gap log, module index. |
| [`adr/`](adr/) | Architecture Decision Records. |
| [`sprints/`](sprints/) | Sprint plans and retrospectives. |
| [`templates/`](templates/) | Templates for every artifact this project produces. |

## Identifier conventions

All identifiers are stable and never reused. They are the join keys between the
board, the specs, the tests, and the documentation registry.

| Prefix | Meaning | Assigned in | Example |
| --- | --- | --- | --- |
| `HCM-###` | Work item (story / task / spike) | `backlog.md` | `HCM-014` |
| `ADR-####` | Architecture Decision Record | `adr/` | `ADR-0003` |
| `DOC-###` | Registered documentation source | `docs/source-registry.md` | `DOC-000` |
| `GAP-###` | Documentation or knowledge gap | `docs/gaps.md` | `GAP-002` |
| `ASM-###` | Logged assumption (has owner + expiry) | `docs/gaps.md` | `ASM-000` |
| `REQ-<MOD>-###` | Requirement | module spec | `REQ-ABS-000` |
| `TC-<REQ>-##` | Test case | `tests/` | `TC-REQ-ABS-000-01` |
| `DEF-###` | Defect | `tests/defects.md` | `DEF-000` |
| `RISK-###` | Risk | `risks.md` | `RISK-001` |
| `<MOD>` | Module code | `docs/modules/README.md` | `PAY` |

The numeric suffix `000` is **reserved across every identifier class** for
illustrative examples in documentation. It never denotes real work, a real
source, or a real gap, and tooling ignores it.

## The traceability chain

Nothing in this repository is allowed to float free of its evidence:

```
DOC-###  (Oracle official source, registered with version + release + retrieval date)
   └── REQ-<MOD>-###   (requirement, cites the source)
         ├── ADR-####  (decision, cites the source and the requirement)
         ├── HCM-###   (work item that implements it)
         │     └── commit / config artifact  (cites HCM-### and DOC-###)
         └── TC-<REQ>-##  (test that proves it)
```

`scripts/project_lint.py` enforces the links that can be checked mechanically.
Everything else is enforced at review, per [`roles.md`](roles.md).

## When something has no source

Do not guess, and do not quietly fill the hole with community knowledge. Raise a
`GAP-###`, log the working `ASM-###` with an owner and an expiry date, mark the
affected decision **Provisional**, and keep moving. See
[`decision-framework.md`](decision-framework.md).
