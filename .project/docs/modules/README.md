# Module Index & Documentation Coverage

Module codes are the join key between requirements, cards, commits, directories,
and registry entries. Use the code, not the marketing name.

> **Scope is not yet confirmed** (`GAP-002`). The list below is the candidate set
> for an Oracle Fusion Cloud HCM implementation, held under `ASM-001` and
> `ASM-002`. `HCM-011` replaces the Scope column with real values.

| Code | Module | Scope | Tier A/B sources | Owner |
| --- | --- | --- | --- | --- |
| `GHR` | Global Human Resources (Core HR, workforce structures, person & employment) | TBC | 0 | — |
| `PAY` | Payroll (elements, balances, payroll flows, costing) | TBC | 0 | — |
| `ABS` | Absence Management (plans, accruals, entitlements) | TBC | 0 | — |
| `TIM` | Time and Labor | TBC | 0 | — |
| `BEN` | Benefits | TBC | 0 | — |
| `CMP` | Compensation (workforce compensation, individual comp, total comp statement) | TBC | 0 | — |
| `TAL` | Talent Management (goals, performance, career development, talent review, succession) | TBC | 0 | — |
| `ORC` | Recruiting (Oracle Recruiting Cloud) | TBC | 0 | — |
| `LRN` | Learning | TBC | 0 | — |
| `HSE` | Workforce Health & Safety | TBC | 0 | — |
| `JRN` | Journeys | TBC | 0 | — |
| `HDS` | HR Helpdesk | TBC | 0 | — |
| `SEC` | Security & role design (job, duty, data, abstract roles) | In scope | 0 | Solution Architect |
| `INT` | Integrations (HCM Extracts, HDL, REST, SOAP, ATOM, file) | In scope | 0 | Solution Architect |
| `DAT` | Data conversion & migration | In scope | 0 | Solution Architect |
| `RPT` | Reporting & analytics (OTBI, BI Publisher) | TBC | 0 | — |
| `EXT` | Extensions & personalisation (Redwood, Visual Builder, page configuration) | TBC | 0 | — |
| `WFL` | Approvals & workflow (BPM) | TBC | 0 | — |

`SEC`, `INT`, and `DAT` are marked in scope regardless of module selection: every
Oracle HCM implementation needs role design, interfaces, and conversion.

## Per-module documentation

Each in-scope module gets a directory under [`../oracle/`](../oracle/) holding the
normalised extracts for its registered sources:

```
.project/docs/oracle/<CODE>/DOC-###.md
```

A module with an empty directory and a confirmed in-scope status is a `MISSING`
gap, raised at intake.

## Adding a module code

Codes are three uppercase letters, added only by the Documentation Specialist,
never reused, and never renamed once cited. Add the row here first, then use it.
