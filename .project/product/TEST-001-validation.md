---
id: TEST-ORCH-001
title: Test strategy and acceptance evidence for the documentation pipeline
artifact_type: test-strategy
status: PROPOSED
version: 1.0.0
owner_role: QA
reviewer_roles: [BA, DEV, PO]
last_reviewed: 2026-10-27
related_work_item: HCM-036
---

# TEST-001 — Validation Strategy

## 1. Purpose

This test strategy defines evidence required before the documentation pipeline is trusted to publish a guide as current. Tests must demonstrate preservation of source meaning and provenance, not merely that a parser exits with code zero.

The current code inspection found a likely defect in the HTML parser. No statement in this strategy claims that the current test suite has passed. Every result is recorded against an exact commit.

## 2. Required test levels

1. **Unit tests:** URL policy, parsing, Markdown conversion, hashing, manifest validation, identifier preservation, completeness classification and deterministic diff.
2. **Fixture-based integration tests:** run PDF/HTML fixtures through ingest → normalize → manifest → validation → index without network access.
3. **Lifecycle tests:** unchanged runs, candidate edition, current/archive transition, rejected candidate, fetch failure, parse failure, incomplete source chain and retry.
4. **Workflow tests:** validate YAML, minimum token permissions, scheduled/manual trigger presence, branch/PR-only behavior, no automatic merge.
5. **Live source smoke test:** perform a controlled fetch against an approved official source during a manual or scheduled run; record final URL, HTTP/content type, page count, hash and outcome. Live web availability is not required for offline unit-test pass.
6. **Human source review:** compare a sample of converted pages—including at least one table and one technical identifier—against the official original. Confirm source citations resolve and no printed/PDF page-number conflation.
7. **Publication acceptance:** reviewer verifies the generated PR contents and accepts/rejects them. Passing CI alone does not publish or accept an edition.

## 3. Test cases

| Test ID | Requirement mapping | Scenario | Expected result |
|---|---|---|---|
| TC-ORCH-001 | FR-001, FR-002 | Catalogue entry with missing ID, duplicate guide ID, or unknown state | Validator fails with file/field-specific errors |
| TC-ORCH-002 | FR-004 | Non-HTTPS source, unapproved host, cross-guide URL, external redirect | Fetch is rejected; current edition unchanged |
| TC-ORCH-003 | FR-005, NFR-001 | PDF fixture with multiple pages and a low-text page | Manifest records source hash, physical page count, page-level diagnostics, and no OCR claim |
| TC-ORCH-004 | FR-006 | HTML fixture with Next link, relative URL, link loop and max-page cap | Traversal follows only allowlisted Next links; loop/cap marks incomplete or fails loudly |
| TC-ORCH-005 | FR-007 | Markdown fixture with links, lists, tables, identifiers and conflicting wording | Stable deterministic output; identifiers and conflict remain unaltered |
| TC-ORCH-006 | FR-008, NFR-001 | Search result resolves to source location | Each result contains guide, edition, source location and URL |
| TC-ORCH-007 | FR-009, NFR-004 | Manifest missing tool version, hash or page diagnostics | Validation rejects incomplete manifest |
| TC-ORCH-008 | FR-010, NFR-003 | Run the same source and config twice | Second run reports unchanged; no content diff/PR |
| TC-ORCH-009 | FR-011 | Compare known old and new edition fixtures | Added, changed, and removed sections are reported reproducibly |
| TC-ORCH-010 | FR-012 | Supersede an accepted edition | Prior bytes and metadata remain under archive; new content is proposed as current |
| TC-ORCH-011 | FR-013, NFR-002 | Inject network, parse, completeness or schema failure | Last-known-good current edition and archive are not mutated |
| TC-ORCH-012 | FR-014, NFR-007 | Candidate publication run | Writes to a bot branch and opens/updates PR only; default branch is not written directly |
| TC-ORCH-013 | FR-015 | PR report has one required field omitted | PR-body validation fails or blocks publication |
| TC-ORCH-014 | FR-016 | Catalogue includes current and archived editions | Every guide has valid index/archive links; broken paths fail checks |
| TC-ORCH-015 | FR-017 | Guide edition is known but tenant quarterly release is unknown | Metadata keeps fields separate; no inferred tenant release |
| TC-ORCH-016 | FR-018, NFR-010 | One source returns 404 or an incomplete HTML chain | Run report records failure/incomplete; guide marked stale/error rather than current |
| TC-ORCH-017 | FR-019, NFR-010 | Weekly run with mixed success, no-change and failures | Report captures each guide outcome, timestamps, warning/error and PR link |
| TC-ORCH-018 | FR-020 | Fresh-model onboarding dry run | New reviewer locates requirements, source code, current status, test evidence and next owner from repository only |
| TC-ORCH-019 | NFR-005, NFR-006 | Scan tracked files and logs | No token, credentials, tenant exports, PII or ignored local corpus is published |
| TC-ORCH-020 | Existing defect control | HTML anchor parsing fixture | Parser handles a link without NameError; the current source must be fixed if this test fails |
| TC-ORCH-021 | Workflow operations | Check weekly workflow definition on default branch and manual recovery | Trigger config is correct; operator runbook documents schedule inactivity and recovery |
| TC-ORCH-022 | NFR-008 | Add a second guide by configuration only | Shared adapter runs it without copied guide-specific parser logic |

## 4. Existing regression tests to inspect and run

- tests/test_oracle_html_ingest.py — contains test_html_to_markdown_keeps_headings_lists_links_and_tables, which parses an anchor and should expose the suspected undefined-variable issue in scripts/oracle_docs/ingest_oracle_html.py.
- tests/test_oracle_external_search.py — checks separate PDF/HTML metadata and fails loudly on empty corpus.
- tests/test_oracle_docs_normalizer.py — covers deterministic PDF-derived Markdown normalization.

Run the actual command documented by the repository workflow after repairing any detected defects:

    python3 -m unittest discover -s tests -p "test_oracle*.py" -v

Then run project lint:

    python3 scripts/project_lint.py

Record command, environment, exit code, test count, failures, commit SHA and workflow/run URL. Do not reuse a pass result from a prior commit as proof for the current commit.

## 5. Evidence record template

Each verification record must state:
- Test ID and requirement IDs;
- commit SHA and branch;
- test command and environment;
- expected and actual result;
- PASS / FAIL / BLOCKED;
- supporting log or workflow URL;
- defect ID and owner for failures;
- QA reviewer and review date.

## 6. Acceptance rule

All MUST requirements from SRS-001 must map to tests and pass for the same candidate SHA. Any failed safety, completeness, traceability, source allowlist, archival or no-overwrite test blocks publication. The QA role owns test sufficiency and pass/fail; the PO owns business acceptance, not the technical test result.
