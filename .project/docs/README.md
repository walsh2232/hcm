# Documentation Ingest System

Oracle official documentation is the primary source of truth for this project.
This directory is how it enters, how it is tracked, and how it is cited.

| File | Purpose |
| --- | --- |
| [`source-registry.md`](source-registry.md) | **Documentation Source Registry** — every source we hold, tiered and release-bound. |
| [`gaps.md`](gaps.md) | Gap log and assumption register — what we do not hold, and what we are assuming meanwhile. |
| [`modules/README.md`](modules/README.md) | Module code index and per-module documentation coverage. |
| [`oracle/`](oracle/) | Normalised extracts, indexes, and notes derived from Oracle sources. |

Source tiering, precedence, and the validation test live in
[`../decision-framework.md`](../decision-framework.md).

## Storage contract

**Oracle documents are not committed to this repository as binaries.** Oracle
documentation carries licence terms, changes every quarter, and would make the
repository unusable in weeks. Instead:

| What | Where it lives | Committed? |
| --- | --- | --- |
| The original Oracle PDF / HTML / spreadsheet | The project document store named in the registry `Location` column | No |
| The registry entry (metadata, tier, release, location) | `source-registry.md` | Yes |
| A normalised extract — the specific passages a decision relies on, quoted with location | `oracle/<MODULE>/<DOC-ID>.md` | Yes |
| Our reading of an ambiguous passage | Registry `Notes` + an ADR | Yes |

The normalised extract is what makes the registry useful: it lets a reviewer
check a decision against the source text without re-downloading a 900-page PDF,
and it survives Oracle re-organising its documentation site.

Quote only what a decision depends on, always with a precise location
(`§4.3`, `Table 12`, `p. 214`), and never paraphrase a normative statement —
paraphrase is how a source quietly changes meaning.

## Intake

Intake is owned by the Documentation Specialist and runs as a Kanban card
(`HCM-010` for batch 1). One card per batch.

1. **Manifest.** The Product Owner supplies the documents plus a manifest listing,
   for each: title, Oracle document ID or URL, release it describes, and the
   modules it covers. A document without a stated release cannot be tiered A or B
   until the release is established.
2. **Register.** Each document is added to `source-registry.md` and assigned a
   `DOC-###`. IDs are never reused, even after retirement.
3. **Tier.** Assign tier A–D per `decision-framework.md` §1. Record who assigned it.
4. **Bind to release.** Record the release the document describes and the release
   it has been validated against. These are often not the same.
5. **Index by module.** Update `modules/README.md` so each in-scope module shows
   its covering documents — and, more importantly, shows when it has none.
6. **Assess coverage.** Every in-scope module with no Tier A/B source raises a
   `MISSING` gap in `gaps.md`.
7. **Detect conflict.** Where two registered sources disagree, raise an
   `AMBIGUOUS` gap immediately. Do not resolve it silently during intake.
8. **Summarise.** Record the batch using [`../templates/doc-intake.md`](../templates/doc-intake.md).

## Citing a source

Cite the identifier **and the location within it** — everywhere: commits, PRs,
ADRs, specs, test cases.

```
Source: DOC-000 §4.3            correct
Source: DOC-000                 rejected at review — no location
Source: Oracle documentation    rejected at review — not a citation
Source: NONE (GAP-000)          acceptable, gap is logged
Source: N/A — internal process  acceptable for non-product decisions
```

## Currency

Oracle Fusion Cloud HCM ships quarterly updates. A registry entry that has not
been validated against the deployed release is stale, and a decision resting on a
stale entry is a decision resting on nothing. The source currency sweep
(`decision-framework.md` §2) is a scheduled card each release, owned by the
Documentation Specialist.

## Current state

**No Oracle documentation has been received.** The registry is empty by design,
not by oversight — see `GAP-001` in [`gaps.md`](gaps.md). Every module design card
in the backlog is gated on intake batch 1.
