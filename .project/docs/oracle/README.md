# Normalised Oracle Source Extracts

One file per registered source, organised by module code:

```
oracle/<MODULE-CODE>/DOC-###.md
```

An extract is **not** a copy of the Oracle document. It is the working record of
the passages this project's decisions actually rest on, so a reviewer can check a
citation without re-downloading the original.

## Extract format

```markdown
# DOC-### — <exact Oracle document title>

Oracle ref: <document ID / part number / URL>
Release described: 25B · Validated against: 25B
Tier: A · Status: ACTIVE · Registered: 2026-08-23
Original held at: <store location from the registry>

## Passages relied upon

### §4.3 Accrual processing
> "<verbatim quotation, unaltered>"

Relied on by: REQ-ABS-000, ADR-0000
Reading: <our interpretation, only where the text admits more than one>
Ambiguity: <GAP-### if raised, otherwise "none">
```

## Rules

1. **Quote verbatim.** Never paraphrase a normative statement — paraphrase is how
   a source quietly changes meaning between the document and the design.
2. **Always give the location.** `§4.3`, `Table 12`, `p. 214`. A quotation without
   a location is not evidence.
3. **Extract only what is relied upon.** This is not a mirror of Oracle's
   documentation, and copying it wholesale creates a licence problem and a
   maintenance problem at once.
4. **Separate text from reading.** The quotation is Oracle's. The `Reading:` line
   is ours, and it is challengeable at review.
5. **Re-validate every release.** Update `Validated against:` during the source
   currency sweep, or mark the entry `STALE`.

## Module skill and retrieval index

The reusable agent instructions live in the repository-level Oracle HCM Expert skill. The first populated module source map is ORC (Recruiting), under the ORC directory. Each further module must use real Oracle catalog pages and a verified manifest; do not populate it with guessed URLs or illustrative source rows.

The local retrieval CLI accepts a module manifest path for all commands. Select the correct manifest with the --manifest option, then run status, refresh, ingest, or search. Each module gets an isolated local index under .cache/oracle-hcm/<module-code>/ and a metadata-only source-status.json beside its manifest.

Downloaded manuals and extracted full text remain local and Git-ignored. This repository is public, so do not commit Oracle PDF files or wholesale guide extracts.

## Current state

ORC has verified official guide URLs and release-readiness entries registered. The first source freshness workflow is scheduled weekly. Running the local ingest command is required to create a searchable full-text index on a workstation. Other modules remain to be inventoried from their actual Oracle source catalogs; see GAP-001 and GAP-002.
