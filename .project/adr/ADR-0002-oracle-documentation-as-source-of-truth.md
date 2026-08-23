# ADR-0002 — Oracle official documentation is the source of truth

## Status
Accepted — 2026-08-23

## Context

Oracle Fusion Cloud HCM is a large, opinionated, quarterly-updated SaaS product.
Most of what practitioners "know" about it is a mixture of official documentation,
behaviour observed on a different release, advice from other implementations, and
inference. Those sources are not equally reliable, and mixing them silently is how
an implementation acquires configuration nobody can justify.

Model knowledge and community material are especially dangerous here: they are
fluent, plausible, and frequently describe behaviour from a release that no longer
exists. They read exactly like documentation and are not documentation.

The Product Owner will supply the official Oracle documentation set for this
project. That set must be established as primary, with everything else explicitly
subordinate.

## Decision

We will treat Oracle official documentation as the primary source of truth, and
enforce it structurally rather than by good intentions.

1. **Registry.** Every usable source is registered in
   `.project/docs/source-registry.md` with an Oracle reference, the release it
   describes, a tier, and a status. An unregistered source may not be cited.
2. **Tiering with absolute precedence.** A (Oracle documentation for the deployed
   release, including the set supplied for this project) > B (My Oracle Support,
   release readiness material) > C (Cloud Customer Connect, Oracle PM blogs) >
   D (community, third-party, model knowledge). A lower tier never overrides a
   higher one.
3. **Tier C and D may only form a hypothesis.** They may never justify a decision,
   close a gap, or appear as a citation. External research supplements Oracle
   sources; it never substitutes for them.
4. **Citations name a location**, not just a document: `DOC-000 §4.3`.
5. **Release binding.** A source without a stated release cannot be tier A or B.
   Entries are re-validated each quarterly update; ADRs citing a changed source
   return to `Under review`.
6. **Gaps are raised, not filled.** Where the registered sources cannot answer a
   question, a `GAP-###` is logged and work proceeds under a logged assumption per
   `ADR-0005`.
7. **Normalised extracts.** The passages a decision rests on are quoted verbatim,
   with location, in `.project/docs/oracle/<MODULE>/DOC-###.md`, so a reviewer can
   check the citation without the original document.

Oracle documents themselves are not committed as binaries — licence terms,
quarterly churn, and repository size all argue against it. The registry records
where the original is held.

## Consequences

**Easier:** any decision can be checked against its evidence; a quarterly update
becomes a mechanical impact analysis; disagreements resolve by tier rather than by
seniority; the difference between "Oracle says" and "we believe" is visible.

**Harder:** work slows at exactly the points where guessing would have been fast.
Cards that would have proceeded on plausible knowledge now stop at the Definition
of Ready and raise a gap. Early in the project — before intake — this is very
visible: nearly the whole backlog is gated on `GAP-001`.

**Cost:** intake and registration effort per document, a currency sweep each
quarter, and the discipline to write `NONE (GAP-###)` rather than a confident
sentence.

**Accepted risk:** a genuinely correct piece of community knowledge will
occasionally be delayed while it is confirmed. This is the intended trade.

## Alternatives considered

- **Treat practitioner experience as equal to documentation** — rejected: it
  produces configuration nobody can justify at audit, and it silently encodes
  behaviour from other releases.
- **Register sources but skip tiering** — rejected: without precedence, conflicts
  resolve by whoever argues hardest.
- **Commit Oracle PDFs to the repository** — rejected: licence terms, size, and
  quarterly churn. Registry plus verbatim extract gives the reviewability without
  the liability.

## Sources
N/A — internal process decision. No Oracle source applies. This ADR establishes
how Oracle sources will be used; it does not itself rest on one.
