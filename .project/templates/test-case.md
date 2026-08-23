# TC-REQ-<MOD>-###-## — <title>

**Requirement:** `REQ-<MOD>-###` · **Module:** `<CODE>` · **Type:** `<Functional|Integration|Security|Payroll parallel|Regression|Negative>`
**Level:** `<Unit/config|System|Integration|UAT>` · **Priority:** `<P1|P2|P3>`
**Environment:** `<instance from config/environments.md>` · **Author:** QA · **Date:** <ISO>

## Objective
<The single behaviour this case proves. One case, one behaviour.>

## Preconditions
- <Configuration state, data state, role/user, effective date>

## Test data
<Reference to synthetic fixtures. Never production data, never real personal data,
never a real national identifier.>

## Steps
| # | Action | Expected result |
| --- | --- | --- |
| 1 | <action> | <observable result — not "works correctly"> |

## Expected outcome
<The end state, stated so that pass/fail is unambiguous.>

## Source
`DOC-### §<location>` — <the Oracle source establishing the expected behaviour, or
`NONE (GAP-###)` where the expectation is a business rule rather than product
behaviour.>

## Result
| Run | Date | Release | Result | Defect | Tester |
| --- | --- | --- | --- | --- | --- |
| 1 | <ISO> | `<25B>` | Pass / Fail | `DEF-###` | <name> |

## Regression
<Whether this case joins the quarterly-update regression pack, and why.>
