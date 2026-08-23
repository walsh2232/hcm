# Sprint 000 — Inception

**Dates:** 2026-08-23 → open (closes when the inception pull request merges)
**Product Owner:** <unassigned> · **Board:** [`../kanban.md`](../kanban.md)

## Sprint goal

Stand up the project operating system — decision rights, workflow, documentation
ingest, and traceability — and produce an honest, complete statement of everything
that blocks delivery work from starting.

Delivering the scaffolding is half the goal. The other half is that at the end of
this sprint nobody has to guess what is missing.

## Context

The repository was empty. No Oracle HCM documentation has been supplied, and the
module scope, target release, environment topology, success criteria, and
current-state landscape are all undefined. The correct response is not to start
designing modules on plausible assumptions — it is to build the machinery that
makes the missing inputs visible and then name them precisely.

## Committed cards

| ID | Title | Role | Estimate | Source | Risk |
| --- | --- | --- | --- | --- | --- |
| `HCM-001` | Repository structure and contribution standards | DOC | ~1d | N/A — internal | Conventions unused if not enforced at review |
| `HCM-002` | Role charters, decision rights, RACI, escalation | PO | ~1d | N/A — internal | Roles unassigned to real people |
| `HCM-003` | Kanban workflow, DoR/DoD, artifact templates | PO | ~1d | N/A — internal | Board decay without discipline |
| `HCM-004` | Documentation ingest system, registry, gap log | DOC | ~2d | N/A — internal | Registry stays empty if intake does not happen |
| `HCM-005` | Decision-making & source validation framework | SA | ~1d | N/A — internal | Framework bypassed under delivery pressure |
| `HCM-006` | Project lint and CI automation | DEV | ~1d | N/A — internal | Lint disabled rather than fixed |

## Explicitly not in this sprint

| ID | Why deferred |
| --- | --- |
| `HCM-020`–`HCM-035` | Every module design card is gated on `GAP-001`. None can meet the Definition of Ready without a backing `DOC-###`. Starting them would mean designing on assumption — precisely what `ADR-0002` exists to prevent. |
| `HCM-011`–`HCM-015` | Ready, but they need Product Owner and business input this sprint could not obtain. They are the first pull once inputs are available. |

## Blockers carried out of this sprint

| Blocker | Owner | Needed by | Impact if unresolved |
| --- | --- | --- | --- |
| `GAP-001` — no Oracle documentation | Product Owner | Next sprint | Nothing downstream of intake can start. This is the critical path. |
| `GAP-002` — module scope undefined | Product Owner | Next sprint | Coverage cannot be assessed; sequencing cannot be planned |
| `GAP-003`–`GAP-007` | PO / SA / BA | Next sprint | Design, testing, and forecasting all rest on these |

## Gaps opened

`GAP-001` through `GAP-007` — see [`../docs/gaps.md`](../docs/gaps.md).
All seven are open at sprint close. This is the sprint's primary output.

## Assumptions logged

`ASM-001`, `ASM-002`, `ASM-003` — all expiring 2026-09-30. The build fails if they
are neither resolved nor renewed by then, per `ADR-0005`.

## Exit criteria

- [x] Kanban board, backlog, and workflow defined and populated
- [x] Role charters with decision rights and escalation
- [x] Documentation ingest system with an empty-by-design registry
- [x] Gap log with every known blocker named and owned
- [x] Decision framework with source tiering and precedence
- [x] Five inception ADRs recorded
- [x] Template set for every artifact the project produces
- [x] Traceability rules machine-checked in CI
- [ ] Inception pull request reviewed and merged
- [ ] Roles assigned to named people

## Retrospective

Held at sprint close — `sprint-000-retro.md`.
