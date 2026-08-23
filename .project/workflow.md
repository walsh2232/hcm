# Kanban Workflow

## States

Work moves left to right. A card sits in exactly one state and carries exactly one
owner at all times.

| # | State | Meaning | Owner | WIP limit |
| --- | --- | --- | --- | --- |
| 1 | **Backlog** | Identified but not refined. Includes research spikes and documentation gaps. | Product Owner | — |
| 2 | **Ready** | Refined, estimated, meets Definition of Ready. Can be started by anyone. | Product Owner | 6 |
| 3 | **In Progress** | Actively being worked. | The doing role | 2 per role |
| 4 | **In Review** | Work complete, awaiting validation by a *different* role. | The reviewing role | 6 |
| 5 | **Done** | Meets Definition of Done. Merged and documented. | — | — |

There is deliberately no *Blocked* column — a blocked card stays in its current
state with a `🚧 BLOCKED` marker and a stated blocker, so that blockage shows up
as WIP pressure instead of being parked out of sight (see `ADR-0004`).

## Card format

Cards live as one-line rows on the board, with detail in the linked artifact.
Illustrative — `-000` identifiers are reserved for examples and never denote real
work items:

```
- HCM-000 [SA] Design absence accrual integration pattern · REQ-ABS-000 · DOC-000 · ~3d
- HCM-000 [BA] 🚧 BLOCKED Payroll element mapping — awaiting DOC set for PAY (GAP-000)
```

Format: `HCM-###` · `[role]` · title · related `REQ`/`ADR` · backing `DOC-###` · estimate.
Full card body uses [`templates/story.md`](templates/story.md) and lives in the
backlog file or the PR description, never only in someone's head.

## Transition rules

| Transition | Gate |
| --- | --- |
| Backlog → Ready | Meets **Definition of Ready**. PO ranks it. |
| Ready → In Progress | Puller has capacity within the WIP limit; card gets an owner today. |
| In Progress → In Review | Work is complete *and self-checked*; PR open; `project_lint` green. |
| In Review → In Progress | Reviewer rejects. Reviewer states what is missing — never a bare rejection. |
| In Review → Done | Meets **Definition of Done**; reviewer of a *different role* approves. |
| Any → Backlog | Only the PO may de-scope a card, and must state why on the card. |

**Pull, don't push.** Work is pulled from the right-most available state first: a
card sitting in In Review is more valuable to finish than a new card is to start.

## Definition of Ready

A card may enter **In Progress** only when all of the following hold:

- [ ] Outcome is stated in business terms, not as an implementation instruction.
- [ ] Acceptance criteria are written and testable.
- [ ] The backing Oracle source is identified (`DOC-###`), **or** a `GAP-###` is
      raised and an `ASM-###` recorded with an owner and expiry.
- [ ] Affected module(s) identified by module code.
- [ ] Dependencies identified and either resolved or explicitly accepted.
- [ ] Sized (T-shirt or days). Anything larger than 5 days is split.
- [ ] QA has confirmed it is testable as written.

## Definition of Done

A card may enter **Done** only when all of the following hold:

- [ ] Acceptance criteria demonstrably met.
- [ ] Artifact committed to the repository in its correct directory.
- [ ] Traceability intact: source → requirement → artifact → test.
- [ ] Test cases written, executed, and passing; defects closed or accepted by PO.
- [ ] Any decision taken is recorded as an ADR or a registry annotation.
- [ ] Documentation updated: runbook, glossary, and module index as applicable.
- [ ] Reviewed and approved by a role other than the one that did the work.
- [ ] `scripts/project_lint.py` passes.
- [ ] No new undocumented assumption introduced.

## Cadence

| Ceremony | When | Output |
| --- | --- | --- |
| Daily flow check | Daily | Blockers named and owned; board reflects reality. |
| Refinement | Twice weekly | Cards move Backlog → Ready; gaps raised. |
| Sprint planning | Start of sprint | `sprints/sprint-###-*.md` with goal and committed cards. |
| Review / demo | End of sprint | PO accepts or rejects each card against acceptance criteria. |
| Retrospective | End of sprint | Actions recorded as cards, not as sentiments. |
| Source currency sweep | Every Oracle quarterly update | Registry re-validated; affected ADRs re-opened. |

## Automation

`scripts/project_lint.py` runs in CI on every pull request and enforces:

- Work item IDs are unique and well-formed across the board and backlog.
- Every card on the board exists in the backlog with a full body, and vice versa.
- Every `DOC-###` cited anywhere exists in the source registry and is not retired.
- Every `GAP-###` and `ASM-###` cited exists in the gap log; every open `ASM-###`
  has an owner and an expiry date, and expired assumptions fail the build.
- Every ADR has the required sections, a valid status, and at least one source
  citation or an explicit `NONE (GAP-###)`.
- WIP limits on the board are not exceeded.

Board state is maintained by hand in `kanban.md`; the lint keeps it honest.
