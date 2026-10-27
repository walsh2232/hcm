---
id: SRS-ORCH-001
title: Software requirements specification for the documentation pipeline
artifact_type: software-requirements-specification
status: PROPOSED
version: 1.0.0
owner_role: BA
reviewer_roles: [PO, SA, QA, DEV]
last_reviewed: 2026-10-27
related_work_item: HCM-036
---

# SRS-001 — Documentation Pipeline Requirements

## 1. Purpose and conventions

This SRS defines testable behavior for the Oracle HCM Reference Library & Change Tracker described by PRD-001. Requirements are stable and individually verifiable. Do not renumber a requirement; mark it SUPERSEDED and reference its replacement.

Priority uses MoSCoW: MUST is required for MVP acceptance; SHOULD is important unless an explicit waiver is recorded; COULD is optional; LATER is outside the MVP.

Requirement statuses: PROPOSED, IMPLEMENTED-UNVERIFIED, LOCALLY-VERIFIED, CI-VERIFIED, ACCEPTED, BLOCKED, DEFERRED, SUPERSEDED. A requirement is not CI-VERIFIED unless the linked run is for the exact commit under review.

## 2. Functional requirements

| ID | Priority | Requirement | Acceptance / verification |
|---|---|---|---|
| FR-ORCH-001 | MUST | The system shall maintain a machine-readable catalogue of known guides, canonical source URLs, modules, guide types, languages, edition identifiers, and lifecycle state. | Schema validation rejects duplicate IDs, missing required fields, and invalid lifecycle statuses. |
| FR-ORCH-002 | MUST | The system shall support adding and retiring a guide through a catalogue change without rewriting the fetcher. | Fixture test adds a guide record; retired entries remain queryable and are not silently deleted. |
| FR-ORCH-003 | MUST | The system shall check tracked source pages on a weekly schedule and support an authorized manual run. | Workflow configuration contains weekly schedule and manual dispatch on the default branch; a test run logs its trigger. Schedule is not considered live until observed in GitHub Actions. |
| FR-ORCH-004 | MUST | The system shall retrieve only sources within an explicit approved host/path allowlist. | Unit tests reject a cross-host redirect, unrelated guide path, non-HTTPS URL, and unapproved host. |
| FR-ORCH-005 | MUST | The system shall support PDF ingestion and record physical PDF page numbers distinctly from printed page numbers. | A fixture PDF produces a manifest and physical-page citations; printed pagination is not inferred. |
| FR-ORCH-006 | MUST | The system shall support an HTML fallback where a guide is available as sequential official HTML pages. | Fixture test verifies same-guide Next-link traversal, URL provenance, link-loop detection, max-page handling, and explicit incomplete-state reporting. |
| FR-ORCH-007 | MUST | The system shall produce deterministic Markdown from a source document without silently rewriting technical identifiers or source meaning. | Golden tests compare stable outputs; known identifiers and capitalization survive; any source conflict is raised rather than normalized away. |
| FR-ORCH-008 | MUST | Each extracted page/section shall retain a resolvable source location. | Every indexed chunk resolves to a guide, edition, source hash, and PDF physical page or original HTML URL/sequence. |
| FR-ORCH-009 | MUST | Each ingest shall create a machine-readable manifest with source identity, hash, timestamps, tool versions, page counts, diagnostics, and validation result. | Schema and integrity checks pass for complete and intentionally incomplete fixtures. |
| FR-ORCH-010 | MUST | The system shall detect a no-change run and avoid opening a content-update PR when content and relevant metadata are unchanged. | Two identical fixture runs yield a no-change result and no proposed file diff. |
| FR-ORCH-011 | MUST | The system shall detect edition or content changes and summarize changed, added, and removed pages/sections. | Controlled old/new fixture produces deterministic diff output linked to both manifests. |
| FR-ORCH-012 | MUST | When a candidate edition is accepted for review, the prior current edition shall be preserved in an explicit archive path before the current pointer is changed. | Lifecycle test proves prior current content remains byte-retrievable in the archive and catalogue. |
| FR-ORCH-013 | MUST | The system shall not replace the last-known-good current edition if retrieval, parsing, completeness, schema validation, or CI fails. | Injected failure leaves the current file, manifest pointer, and archive state unchanged. |
| FR-ORCH-014 | MUST | The system shall propose public repository changes in a branch and pull request; scheduled jobs shall not directly push document updates to the default branch. | Workflow permissions and implementation show PR-only writes; integration test/mock verifies no direct default-branch update. |
| FR-ORCH-015 | MUST | A proposed update PR shall contain the source URL, candidate edition, old/new hashes, changed-content summary, completeness result, warnings, and test outcome. | PR-body fixture validator rejects missing fields. |
| FR-ORCH-016 | MUST | The current-guide index shall provide a consistent route from module → guide type → current edition, with archived editions linked. | Catalogue/index validator checks every current entry and archive reference. |
| FR-ORCH-017 | MUST | The system shall distinguish source-guide edition from the target tenant's quarterly release. | Schema uses separate fields; tests reject logic that maps one field to the other. |
| FR-ORCH-018 | MUST | The system shall surface incomplete, failed, skipped, and stale guide states rather than silently presenting them as current. | A deliberately failing source appears in the run report and remains marked stale/error, not current. |
| FR-ORCH-019 | SHOULD | The system should produce a chronological weekly report and per-guide change log. | Report includes run ID, timestamp, guide outcome, diff/PR link, warnings, and error details. |
| FR-ORCH-020 | SHOULD | The system should make the corpus usable by a fresh AI model without undocumented chat state. | Onboarding sequence and status register provide product, code paths, current validation evidence, owners, and next actions. |
| FR-ORCH-021 | SHOULD | The system should provide an optional local SQLite FTS5 search index using existing chunk metadata. | Search results display guide, edition, source location, and URL; they do not strip provenance. |
| FR-ORCH-022 | COULD | The system could generate LLM-assisted semantic change summaries. | If added, summaries are labeled generated, cite exact old/new source locations, record model/version, and are reviewed; they never replace deterministic diffs. |

## 3. Non-functional requirements

| ID | Priority | Requirement | Acceptance / verification |
|---|---|---|---|
| NFR-ORCH-001 Traceability | MUST | Every published guide edition and extracted passage shall be traceable to an official source and exact edition. | Automated link/manifest checks; QA spot-checks a representative sample. |
| NFR-ORCH-002 Safe failure | MUST | A failed or incomplete run shall be non-destructive to the accepted current edition. | Failure-injection lifecycle tests pass. |
| NFR-ORCH-003 Idempotence | MUST | Re-running an unchanged source shall not create content churn. | Stable hashes and empty diff across repeated fixture runs. |
| NFR-ORCH-004 Reproducibility | MUST | The manifest shall identify the extractor/normalizer version and inputs sufficiently to reproduce the transformation. | Manifest test checks versions, input hash and configuration. |
| NFR-ORCH-005 Security | MUST | Workflow permissions shall follow least privilege; external fetches shall use approved HTTPS hosts; tokens shall not be logged. | Workflow review, URL-scope tests, log scan. |
| NFR-ORCH-006 Privacy | MUST | No tenant credentials, production HCM data, candidate/employee PII, local private corpus, or local FTS database may be published by this pipeline. | Repository guard and synthetic fixture scan pass. |
| NFR-ORCH-007 Human control | MUST | A human must review content publication; no automatic merge or default-branch document write. | PR-only path proven in the test environment. |
| NFR-ORCH-008 Maintainability | SHOULD | Adding a guide shall primarily require catalogue metadata, not copy-pasted guide-specific code. | Review shows shared adapter path for at least two guide records. |
| NFR-ORCH-009 Resource use | SHOULD | Weekly runs should fetch only what is needed to detect/verify change; avoid repeated full rebuilds of unchanged corpus where practical. | Run report shows source checks and content processing counts; no fixed runtime target until measured. |
| NFR-ORCH-010 Observability | MUST | Every run shall have a stable run identifier and a report of per-guide outcome, duration, warnings, and errors. | Test report schema and run artifacts are validated. |
| NFR-ORCH-011 Accessibility | SHOULD | Markdown should be readable in GitHub's standard renderer without requiring a proprietary viewer. | Markdown/link checks and manual render review. |
| NFR-ORCH-012 Dependency discipline | SHOULD | MVP should reuse existing Python standard-library components and current project dependencies; new dependencies require a documented reason. | Dependency diff review. |

## 4. Requirement traceability

Each requirement shall be linked to:
- implementation component/path in STATUS-001 or an implementation issue;
- one or more verification cases in TEST-001;
- evidence (test result, workflow run, and commit SHA) when its state advances beyond PROPOSED;
- an owner role and an acceptance role.

A requirement without a verification case cannot be marked ready for implementation. A requirement cannot be marked ACCEPTED merely because code exists.

## 5. Defect and exception handling

If a requirement cannot be met, create a defect or a gap, identify the affected requirement IDs, state user impact, assign an owner and severity, and record the disposition. Waivers require PO acceptance, a reason, and an expiry/revisit date. A waiver cannot waive provenance, safe failure, or human review.

## 6. Explicit MVP release gate

All MUST requirements must pass the test cases mapped in TEST-001 on the same candidate commit. No unreviewed parser, archive, or source-completeness warning may be represented as a successful current-edition update.
