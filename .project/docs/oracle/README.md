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

Thirteen module source sets have been registered: ORC (Recruiting), GHR (Global Human Resources), ABS (Absence Management), BEN (Benefits), TIM (Time and Labor), LRN (Learning), CMP (Compensation), PAY (Global Payroll), JRN (Journeys), HDS (Help Desk), HSE (Workforce Health and Safety), TAL (Talent Management), and RPT (HCM Analytics and Reporting). Each has official guide URLs, source-age caveats, 26D readiness evidence, and a source manifest. The weekly GitHub Actions source-freshness workflow checks all module manifests.

The full-text index is deliberately built locally. For each module, run refresh and ingest; the GitHub status workflow does not commit or publish the manual text or full index. Other areas—Payroll, Compensation, Talent Management, Journeys, Help Desk, Security, Integrations and Analytics—remain to be researched and registered from their actual Oracle catalogs. See GAP-001 and GAP-002.
