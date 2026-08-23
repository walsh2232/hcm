# Architecture Decision Records

An ADR records a decision that shaped the solution, the evidence behind it, and
what it costs. If a decision is hard to reverse — data model, security model,
integration contract, payroll setup, extension versus configuration — it belongs
here, not on a card and not in a conversation.

Template: [`../templates/adr.md`](../templates/adr.md)
Filename: `ADR-####-kebab-case-title.md`, numbered sequentially, never reused.

## Required sections

`scripts/project_lint.py` rejects an ADR missing any of:

| Section | Must contain |
| --- | --- |
| `## Status` | One of the statuses below, with a date |
| `## Context` | The forces at play, including the business need and the product constraint |
| `## Decision` | What was decided, stated actively — "we will…" |
| `## Consequences` | What this makes easier, what it makes harder, and what it costs |
| `## Sources` | `DOC-### §location`, or `NONE (GAP-###)`, or `N/A — internal process decision` |

`## Alternatives considered` is expected wherever an alternative genuinely
existed. An ADR with no rejected option is usually a decision that was never made.

## Statuses

| Status | Meaning |
| --- | --- |
| `Proposed` | Drafted, not yet agreed |
| `Accepted` | Agreed and in force |
| `Provisional` | In force, but resting on an open assumption (`ASM-###`). Must name it. |
| `Under review` | A source it cites changed — usually after a quarterly update sweep |
| `Superseded by ADR-####` | Replaced. The record stays; it explains past artifacts. |
| `Rejected` | Considered and declined. Kept so it is not re-proposed blind. |

ADRs are never deleted and never edited to change their meaning. A decision that
changes produces a new ADR that supersedes the old one.

## Index

| ADR | Title | Status | Sources |
| --- | --- | --- | --- |
| [ADR-0001](ADR-0001-record-architecture-decisions.md) | Record architecture decisions | Accepted | N/A — internal process |
| [ADR-0002](ADR-0002-oracle-documentation-as-source-of-truth.md) | Oracle official documentation is the source of truth | Accepted | N/A — internal process |
| [ADR-0003](ADR-0003-repository-structure.md) | Repository structure for enterprise-scale HCM delivery | Accepted | N/A — internal process |
| [ADR-0004](ADR-0004-kanban-workflow.md) | Five-state Kanban with no Blocked column | Accepted | N/A — internal process |
| [ADR-0005](ADR-0005-provisional-decisions-and-assumption-expiry.md) | Provisional decisions and assumption expiry | Accepted | N/A — internal process |
