---
id: STATUS-ORCH-001
title: As-built versus proposed status register
artifact_type: implementation-status-register
status: IMPLEMENTED-UNVERIFIED
version: 1.0.0
owner_role: BA
reviewer_roles: [DEV, QA]
last_reviewed: 2026-10-27
reference_commit: d8aea24231188a8a36a8dd5194640a87a7e652d3
---

# STATUS-001 — As-Built vs Proposed

## 1. How to read this register

This register is based on GitHub source inspection of walsh2232/hcm at feature-branch commit d8aea24231188a8a36a8dd5194640a87a7e652d3, plus review of the current workflow source. It is not a runtime test report. The PRD package is proposed; the existing code is real but the claims below distinguish implementation from verification.

Before updating any row, inspect the live repository and exact target commit. If a newer commit exists, reassess the relevant paths. Do not treat this file's reference commit as permanently current.

## 2. Summary

| Capability | Status | Evidence | Gap / next action |
|---|---|---|---|
| Project/source governance and source registry | IMPLEMENTED-UNVERIFIED | .project/docs/README.md, .project/docs/source-registry.md, .project/decision-framework.md, .project/docs/gaps.md | Existing governance documents are present; broader scope and tenant release remain unconfirmed in existing gap log. |
| PDF text-layer ingestion | IMPLEMENTED-UNVERIFIED | scripts/oracle_docs/ingest_pdf.py | Uses PyMuPDF, records SHA-256, physical page markers, low/empty-text diagnostics and chunks. Must test against current fixture and inspect complex-layout accuracy. No OCR is performed. |
| HTML ingestion fallback | IMPLEMENTED-UNVERIFIED — SUSPECT DEFECT | scripts/oracle_docs/ingest_oracle_html.py, function MarkdownParser.handle_starttag | Static inspection shows anchor handling refers to name attr although the function receives attrs. An anchor parse appears likely to raise NameError. Fix and execute the anchor/table/link test. |
| Markdown normalizer | IMPLEMENTED-UNVERIFIED | scripts/oracle_docs/normalize_markdown.py, tests/test_oracle_docs_normalizer.py | Deterministic rules exist. Re-run tests and check against the latest source pages; normalizer must not change technical identifiers or reconcile source conflicts. |
| Local SQLite FTS5 search | IMPLEMENTED-UNVERIFIED | scripts/oracle_docs/search_corpus.py, tests/test_oracle_external_search.py | Separate local index includes PDF/HTML provenance. Must rerun tests on exact current SHA and validate search hit citations. |
| Offline tests | IMPLEMENTED-UNVERIFIED | tests/test_oracle_docs_normalizer.py, tests/test_oracle_html_ingest.py, tests/test_oracle_external_search.py | PR #1 description claims 13 tests passed on an earlier revision. Current source has a likely defect exercised by the anchor test. No fresh execution result is established by this status inspection. |
| Project lint | IMPLEMENTED-UNVERIFIED | scripts/project_lint.py | Exists according to repository docs/workflow references. Must be run on the candidate documentation branch. |
| Project-lint GitHub Action | IMPLEMENTED-UNVERIFIED; MANUAL ONLY | .github/workflows/project-lint.yml | Current file uses workflow_dispatch only. There is no push/PR trigger or weekly schedule in this workflow. |
| Weekly guide discovery | PROPOSED | SRS FR-ORCH-003 | No end-to-end weekly source discovery/refresh workflow was found in the inspected paths. |
| Automated edition comparison | PROPOSED | SRS FR-ORCH-011 | No integrated catalogue-to-diff lifecycle established yet; existing normalizer is not a version comparison pipeline. |
| Explicit archive lifecycle | PROPOSED | SRS FR-ORCH-012 | Current repo keeps full source corpus local/ignored; no public guide edition archive lifecycle established. |
| Bot branch and PR generation | PROPOSED | SRS FR-ORCH-014, FR-ORCH-015 | No automated publication PR workflow established. |
| Dedicated public output repository | PROPOSED | PRD-001, ARCH-001 | Candidate name oracle-product-reference-library; repository creation has not been verified or performed in this work. |
| End-user current-guide catalogue and changelog | PROPOSED | PRD-001, DATA-001 | Existing source registry is an implementation-project registry, not the planned public library's full guide catalogue/edition landing pages. |
| Fresh-model onboarding and turn checkpoint | PROPOSED | MODEL_ONBOARDING.md | File has been added in this PR branch; it is not yet independently reviewed/accepted or enforced by automation. |

## 3. Existing implementation: exact locations and contracts

### PDF ingestion

Path: scripts/oracle_docs/ingest_pdf.py

Observed behavior from source:
- accepts a local PDF input and document metadata;
- requires PyMuPDF;
- records a SHA-256 source hash;
- extracts the text layer per physical page;
- records empty pages, low-text pages and replacement characters;
- emits per-page Markdown, full-text Markdown, retrieval-chunks.jsonl and manifest.json;
- explicitly declares OCR is not performed and complex visual layouts may need inspection.

Not verified by this document:
- whether a live Oracle guide can be downloaded in the runtime;
- whether all tables, diagrams, columns and headings are preserved accurately;
- whether every PDF page satisfies the future completeness threshold.

### HTML ingestion

Path: scripts/oracle_docs/ingest_oracle_html.py

Observed behavior from source:
- uses urllib.request and Python html.parser;
- limits navigation to a same-guide directory and follows explicit Next navigation;
- has a maximum page count and request delay;
- records page URL/hash and an HTML sequence marker;
- emits full text, page files, chunks and a manifest that distinguishes HTML sequence from PDF pagination.

Static defect finding: MarkdownParser.handle_starttag receives an attrs argument, but the anchor branch references attr.get. Because attr is not defined in the function, handling an anchor appears to raise NameError. This was identified by source inspection, not by test execution in this session. The existing tests include HTML links, so the expected next action is to run the exact test suite and repair if confirmed. Do not claim current parser correctness before this is resolved.

### Local search

Path: scripts/oracle_docs/search_corpus.py

Observed behavior from source:
- collects retrieval-chunks.jsonl under a local corpus root;
- builds a SQLite FTS5 database;
- carries guide/edition/source-kind metadata;
- shows physical PDF pages or HTML sequence numbers and source URLs in rendered hits;
- stores outputs under local paths intended to be ignored by Git.

### Existing documentation intake governance

Paths:
- .project/docs/README.md
- .project/docs/source-registry.md
- .project/docs/gaps.md
- .project/decision-framework.md

Observed state in the source registry: DOC-001 (*Implementing Recruiting*, guide edition G34431-12) is described as extracted into a private local corpus; DOC-002–DOC-006 are official companion sources catalogued, but their complete bodies were not indexed in the recorded intake. The guide edition does not prove target tenant quarterly release. Do not claim full HCM coverage.

### GitHub workflow

Path: .github/workflows/project-lint.yml

Observed current triggers: workflow_dispatch only. The feature-branch workflow includes the offline unit test command, project lint, and production-data guard. The default-branch version inspected earlier did not include the offline test step and is also manual-only. Do not assume those branch files are identical.

Consequences:
- automatic PR checks are not triggered by the workflow as currently defined;
- weekly source refresh is not configured;
- the exact current workflow status must be verified after merging any changes to the default branch.

## 4. What is not built yet

The inspected repository does not establish an end-to-end weekly guide lifecycle comprising:
- discovery of all approved current Oracle HCM guide entries;
- per-guide edition candidate handling;
- validation-gated current pointer change;
- moving the prior current body to an explicit archive directory;
- stable current guide landing pages for coworkers;
- automatic unchanged detection and content diffs;
- complete run reports and failure notifications;
- automated candidate PRs using least-privilege credentials;
- weekly scheduled and manual-recovery triggers on the default branch;
- the dedicated public documentation output repository `oracle-product-reference-library`; it has not been created in this work.

These are requirements/proposals in PRD-001 and SRS-001, not existing capabilities.

## 5. Claims that require current evidence

| Claim | Evidence required before saying true |
|---|---|
| “All tests pass” | Exact command/output or CI run tied to the exact SHA; no failures hidden by old run |
| “HTML ingestion works” | Anchor, relative-link, table, loop, and incomplete-chain tests pass on current SHA |
| “The guide is complete” | Manifest completeness checks plus a source-chain/physical page review; a hit to a max-page cap is not success |
| “This is the latest guide” | Official source check and recorded edition metadata; not model memory or a guide filename alone |
| “This matches our tenant release” | Separate tenant release evidence; guide edition ID is insufficient |
| “Weekly refresh is live” | Workflow present on default branch, schedule enabled, and at least one successful scheduled run observed |
| “Old versions are archived” | Controlled lifecycle test and an existing archive file/manifest, not just Git commit history |
| “Changes are reviewed” | Human PR review/acceptance on the actual candidate SHA |

## 6. Immediate priorities

1. Run python3 -m unittest discover -s tests -p "test_oracle*.py" -v on the current candidate SHA.
2. Fix the suspected HTML anchor-parser defect and add/retain regression tests.
3. Run python3 scripts/project_lint.py and resolve all errors.
4. Agree the catalogue and manifest contract in DATA-001.
5. Implement a controlled one-guide vertical slice including new edition, unchanged run, parse failure, and incomplete-source tests.
6. Add archive/diff/PR generation.
7. Add weekly/manual triggers only once the default-branch test and publication controls are ready.
