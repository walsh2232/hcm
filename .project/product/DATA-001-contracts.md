---
id: DATA-ORCH-001
title: Catalogue, edition manifest, run report and lifecycle contracts
artifact_type: data-contract-specification
status: PROPOSED
version: 1.0.0
owner_role: DEV
reviewer_roles: [SA, QA, DOC]
last_reviewed: 2026-10-27
related_work_item: HCM-036
---

# DATA-001 — Catalogue and Manifest Contracts

## 1. Design rules

The catalogue is the authoritative registry for tracked guide identities. A per-edition manifest describes what was observed and processed. A run report records the outcome of one attempt. These are related but not interchangeable.

- Use stable IDs. Never reuse a retired guide ID or edition record.
- Store guide-edition identifier separately from the quarterly release described by the document and the target tenant's deployed quarterly release.
- Keep official source URL, final retrieved URL and publication/output path as separate fields.
- A hash identifies bytes observed; it does not prove semantic equivalence, authenticity by itself, or tenant release applicability.
- A “current” state means accepted current content in this library. It does not mean verified against a specific tenant unless a separate validation field says so.
- Failed/incomplete attempts are retained as run records, not promoted to editions.
- No secret values, credentials, user tokens or tenant data belong in catalogue/manifest/run metadata.

## 2. Guide catalogue record

Required fields:

| Field | Type | Required | Meaning |
|---|---|---|---|
| guide_id | string | Yes | Stable project ID, e.g. GUIDE-ORC-001 |
| title | string | Yes | Official title as presented by Oracle |
| product_family | string | Yes | Product family, e.g. hcm, oci, bi-publisher; initial populated family is HCM |
| module_codes | array[string] | Yes | Controlled taxonomy for the product family: HCM module, OCI service, or BI Publisher area/component |
| guide_type | enum | Yes | Implementing, administering, using, security, REST/API, release notes, other |
| locale | string | Yes | Language/locale identifier |
| canonical_url | URI | Yes | Official source/landing URL |
| source_kind | enum | Yes | pdf, html-sequence, html-index, other-approved |
| allowed_scope | object | Yes | Approved scheme, host and path boundary |
| source_ids | array[string] | Yes | Links to DOC-### registry records if using existing project registry |
| latest_observed_edition | string/null | Yes | Most recently verified source edition identifier |
| current_edition | string/null | Yes | Edition accepted as current in the public library |
| status | enum | Yes | ACTIVE, STALE, ERROR, RETIRED, OUT_OF_SCOPE |
| last_checked_at | datetime/null | Yes | Last source discovery attempt |
| last_success_at | datetime/null | Yes | Last successful complete validated ingest |
| owner_role | string | Yes | Accountable role |
| notes | string | No | Human context; claims must cite sources |

latest_observed_edition and current_edition may differ while a candidate waits for validation/review. That difference must be visible, not silently reconciled.

## 3. Edition manifest

Every accepted or candidate edition has one manifest with:

- schema_version;
- guide_id and source registry ID(s);
- title, edition identifier, locale, guide type and module codes;
- official canonical URL and final retrieval URL;
- source kind and content type;
- retrieved_at_utc and processed_at_utc;
- source_sha256 and normalized_content_sha256;
- extractor name/version, normalizer version, and normalized configuration;
- input byte count, page/HTML sequence count, extracted character count, chunk count;
- page-level records with page number or HTML sequence, source URL, source hash, output path, extracted character count, and diagnostic flags;
- completeness_status: COMPLETE, INCOMPLETE, FAILED, NEEDS_VISUAL_REVIEW;
- validation status and the list of checks performed;
- warnings, errors, and terminal reason;
- predecessor edition ID/hash, if any;
- current/archive publication status and associated PR/commit reference after publication.

The source itself is the source of truth for contents. The manifest does not override the document.

## 4. Run report

A run report contains:
- run_id and run_started_at_utc / run_finished_at_utc;
- trigger: scheduled, manual, retry, or test;
- workflow run URL and commit SHA;
- source catalogue revision;
- per-guide outcome: UNCHANGED, CANDIDATE, FAILED, INCOMPLETE, SKIPPED, RETIRED;
- source response status, final URL, hash, response size, retry count;
- parse/validation outcomes and diagnostics;
- old/current/candidate edition identifiers and hashes;
- planned archive operation, diff summary and PR URL;
- error category, sanitized error detail, and next action.

A skipped source is not counted as successfully checked.

## 5. Lifecycle states and transition rules

Catalogue states:
- ACTIVE: tracked and expected to refresh.
- STALE: refresh did not complete within expected cadence or source currency is unresolved.
- ERROR: last check failed; current content, if any, remains untouched.
- RETIRED: intentionally removed from active monitoring; history retained.
- OUT_OF_SCOPE: known but explicitly not tracked in the current scope.

Edition states:
- DISCOVERED: metadata candidate only.
- DOWNLOADED: source bytes retrieved and hashed.
- EXTRACTED: conversion completed; not yet validated.
- VALIDATED: all automated checks passed; visual review may still be needed.
- IN_REVIEW: candidate appears in a pull request.
- CURRENT: accepted and published as current.
- ARCHIVED: superseded edition retained for history.
- REJECTED: candidate failed review; manifest/run report retained for audit.

Legal transitions are explicit. A failed candidate cannot transition to CURRENT. CURRENT changes only in an accepted PR. The prior CURRENT edition becomes ARCHIVED in that same merged PR or atomic publication change.

## 6. File naming and output path contract

Proposed library paths:
- guide landing page: products/<product-family>/<module-or-service>/<guide-slug>/README.md
- current normalized content: products/<product-family>/<module-or-service>/<guide-slug>/current.md
- historical edition: archive/<product-family>/<module-or-service>/<guide-slug>/<edition-id>.md
- edition manifest: metadata/manifests/<guide-id>/<edition-id>.json
- run report: metadata/runs/<date>/<run-id>.json
- weekly change report: changelog/weekly/<date>.md

The landing page links to current.md, records the current edition/hash and last successful validation, and links to all archived editions. Example product-family roots are products/hcm/, products/oci/, and products/bi-publisher/. These are taxonomy examples, not claims that those families are already populated. A new edition must not overwrite current content before tests and review have succeeded.

## 7. Schema evolution

All machine-readable files include schema_version. A breaking schema change increments the major version and provides a migration; additive optional fields increment the minor version. Older manifests must remain parseable or be migratable. Unknown enum values fail validation loudly.

## 8. Data examples

Use synthetic placeholders in tests, not live secrets or tenant exports. Example placeholders such as GUIDE-TEST-001, TEST-EDITION-A and https://docs.example.invalid/guide.html must never be treated as real Oracle documentation records.
