# ADR-0004 — Five-state Kanban with no Blocked column

## Status
Accepted — 2026-08-23

## Context

The project runs six roles working concurrently on interdependent work, with a
hard external dependency: nothing downstream of documentation intake can meet the
Definition of Ready until Oracle sources arrive. A workflow that hides blockage
would make the project look busy while the critical path is stalled.

Boards commonly add a *Blocked* column. It reads as tidy and behaves badly: cards
move out of the flow, stop counting against WIP, and accumulate quietly. The
board then shows healthy throughput while the actual constraint is invisible.

## Decision

We will run a five-state board — Backlog, Ready, In Progress, In Review, Done —
with WIP limits, explicit transition gates, a Definition of Ready and a Definition
of Done, defined in `.project/workflow.md`.

There is **no Blocked column**. A blocked card stays in its current state, carries
a `🚧 BLOCKED` marker, and must name the blocker, the owner, and what is needed to
clear it. Blockage therefore consumes WIP, and a blocked critical path shows up as
pressure that stops new work being started rather than as a quiet parking bay.

WIP limits: Ready 6, In Progress 2 per role, In Review 6. Work is pulled from the
right-most available state first — finishing a card in review beats starting a new
one.

The board is maintained by hand in Markdown and kept honest by
`scripts/project_lint.py`, which runs in CI and enforces ID uniqueness,
board↔backlog consistency, reference integrity for `DOC`/`GAP`/`ASM`/`ADR`
identifiers, assumption expiry, ADR structure, and the WIP limits themselves.

## Consequences

**Easier:** the true constraint is visible at a glance; a blocked project cannot
disguise itself as a busy one; the board is diffable, reviewable, and versioned
with the work; automation prevents the board from decaying into fiction.

**Harder:** a hand-maintained board decays without discipline, so updating it is
part of the Definition of Done rather than an afterthought. WIP limits will feel
obstructive early on — when intake is blocked, the correct behaviour is to finish
or escalate rather than to start something new, and that will be uncomfortable.

**Cost:** board maintenance per card, and lint failures that must be fixed rather
than bypassed.

## Alternatives considered

- **Add a Blocked column** — rejected: it removes blocked work from WIP pressure
  and makes stalled critical paths invisible, which is precisely the failure this
  project is exposed to while `GAP-001` is open.
- **Scrum with fixed sprint commitment** — rejected for now: with the critical
  path gated on an external dependency, a fixed commitment would be fiction.
  Sprints are used for cadence and retrospective, not for commitment.
- **Hosted board tool** — rejected here; see `ADR-0003` alternatives. If one
  becomes the system of record, this ADR and `ADR-0003` are superseded together.
- **No WIP limits** — rejected: six roles with a shared dependency will
  self-organise into starting everything and finishing nothing.

## Sources
N/A — internal process decision. No Oracle source applies.
