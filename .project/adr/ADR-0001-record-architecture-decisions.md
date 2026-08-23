# ADR-0001 — Record architecture decisions

## Status
Accepted — 2026-08-23

## Context

An Oracle HCM implementation accumulates decisions that are cheap to make and
expensive to reverse: enterprise structure, legal employer design, position
management, element design, role model, integration contracts. Six months later
nobody remembers whether a configuration was a deliberate trade-off, a constraint
imposed by the product, or an accident — and the person who knew has rolled off.

Three failure modes follow. Decisions get silently re-opened and re-litigated. A
constraint that was accepted with eyes open gets treated as a defect. And a
configuration that was correct for release `25B` is left in place after `25D`
changes the underlying behaviour, because nothing recorded what it depended on.

## Decision

We will record every significant decision as an Architecture Decision Record in
`.project/adr/`, using the template in `.project/templates/adr.md`.

A decision is significant, and therefore requires an ADR, if any of the following
hold:

- It is hard or expensive to reverse.
- It constrains a later decision in another module.
- It accepts a product limitation, a delta from the business requirement, or a
  maintenance cost.
- It chooses between configuration, extension, and integration.
- It interprets an ambiguous Oracle source.

ADRs are immutable once accepted. A changed decision produces a new ADR that
supersedes the old one; the old record stays, because it is the only explanation
for artifacts built while it was in force. Every ADR cites its sources per
`ADR-0002`.

## Consequences

**Easier:** onboarding, audit, quarterly-update impact analysis (an ADR citing a
changed source is found mechanically), and resisting re-litigation without
evidence.

**Harder:** every significant decision now costs the time to write it down, and
reviewers must enforce that. ADRs that are written after the fact to satisfy the
process are worse than none, because they invent a rationale that was never used.

**Cost:** roughly 20–40 minutes per decision, and a standing review obligation.

## Alternatives considered

- **Decision log in a single file** — rejected: no room for context and
  consequences, and it becomes an unreadable append-only list within a quarter.
- **Decisions captured in the design specification** — rejected: specs describe
  the end state, not the rejected options or the reason. The reasoning is exactly
  what is needed later.
- **External wiki** — rejected: it drifts from the repository, is not reviewable
  in a pull request alongside the change it justifies, and is rarely versioned
  with the artifact.

## Sources
N/A — internal process decision. No Oracle source applies.
