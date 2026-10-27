---
id: PRD-ORCH-001
title: Oracle Product Reference Library and Change Tracker
artifact_type: product-requirements-document
status: PROPOSED
version: 1.0.0
owner_role: BA
accountable_role: PO
reviewer_roles: [PO, SA, QA]
last_reviewed: 2026-10-27
related_work_item: HCM-036
related_specs: [SRS-ORCH-001, ARCH-ORCH-001, DATA-ORCH-001, TEST-ORCH-001, OPS-ORCH-001]
---

# PRD-001 — Oracle Product Reference Library & Change Tracker

## 1. Executive summary

Build a public, version-controlled library for Oracle product documentation that makes confirmed current guides easy to find and preserves superseded editions in an explicit archive. The initial delivery slice is Oracle Fusion Cloud HCM; the information architecture must also support future product families such as OCI and BI Publisher without repository renaming or a structural redesign. A weekly automation discovers sources, retrieves authorized official documents, converts them into source-traceable Markdown, validates the result, compares editions, and proposes repository changes through a pull request.

The initial product is a reliable documentation acquisition and lifecycle system, not an autonomous Oracle configuration expert. The core promise is that a reader or AI model can identify which guide and edition a passage came from, what changed, whether the corpus appears complete, and what is known versus unverified.

The current walsh2232/hcm repository is the existing HCM workbench and contains prototype ingestion tooling plus HCM project governance and implementation material. It is not the intended coworker-facing documentation library. The proposed public output repository is oracle-product-reference-library. Keep the existing processing scripts in walsh2232/hcm during the MVP to avoid unnecessary migration while validating the first vertical slice; extract them into a neutral tooling repository only if/when that separation has a clear benefit. The public output repository and weekly lifecycle are not yet implemented. See STATUS-001.

## 2. Problem statement

Oracle product knowledge is spread across product guides, module/service documentation, release-specific content, security references, API references, and update documentation. HCM is the initial delivery area; the catalogue should also accommodate OCI and BI Publisher when explicitly brought into scope. Practitioners need to retrieve the correct guide quickly and compare historical wording without repeatedly searching for PDFs or relying on model recollection.

Manual downloads and conversion become stale. A simple scraper is not enough: it can miss chapters, flatten tables incorrectly, mistake a newer guide edition for proof of a tenant release, or overwrite the known-good edition with an incomplete retrieval. A trustworthy library therefore requires provenance, completeness checks, explicit lifecycle states, safe failure behavior, reviewable changes, and model-friendly onboarding.

## 3. Product vision

A practitioner or fresh model can open one repository and determine:
- which official guides are tracked for each module and guide type;
- which edition the project currently treats as current, and why;
- which previous editions are archived;
- when a guide was last checked and successfully processed;
- where a statement came from, including guide edition and page/section or official HTML URL;
- what changed between editions and what failed validation;
- whether an apparent absence is a product fact or simply a source/indexing gap.

## 4. Users and use cases

| User | Need | Primary outcome |
|---|---|---|
| Oracle product practitioner / analyst | Quickly find the right product/module/service guide and exact passage | Citable, searchable Markdown |
| Implementation / support colleague | Compare current and older documented behavior | Edition-specific archive and content diff |
| Technical writer / documentation owner | Keep the catalogue complete and current | Scheduled checks, manifests and review queue |
| AI model with no prior conversation | Resume work from repository evidence | Model onboarding and explicit status/source contracts |
| Reviewer / maintainer | Prevent incomplete or unreviewed changes becoming current | Validation report and PR-first publication |

## 5. Goals and measurable outcomes

For the MVP:
1. Every in-scope guide has a unique stable guide ID, official canonical source, module association, guide type, latest observed edition, last-checked timestamp, last-success timestamp, and lifecycle status.
2. A successful ingest produces source metadata, a cryptographic source checksum, page/HTML-location provenance, extraction diagnostics, and a completeness result.
3. The index makes the current edition discoverable within two clicks from the repository front page and links to its archived editions.
4. A no-change weekly run produces no content update PR.
5. A detected edition/content change generates a reviewable PR with a machine-readable diff summary and validation report.
6. A failed or incomplete fetch never replaces a known-good current edition.
7. Prior current editions remain retrievable from an explicit archive path and Git history.
8. Every release candidate passes automated tests, manifest validation, source-link checks, and required human review before being accepted.
9. A fresh model can use MODEL_ONBOARDING.md and the product index to distinguish existing implementation from planned capabilities without relying on chat history.

Targets for ingest completeness, page-level confidence thresholds, and the number of guides in the first coverage set must be agreed before broad rollout; they are not silently assumed in this PRD.

## 6. Scope

### In scope — MVP
- A dedicated public repository for the shareable reference library; candidate name: oracle-product-reference-library. Name availability and creation are not yet verified. The repository taxonomy is product-family neutral, with HCM as the first populated family and room for OCI and BI Publisher.
- A catalogue of official Oracle guide sources, product family, module/service, guide type, locale, edition identifier, and official URL.
- Weekly scheduled source checks and a manual dispatch for recovery and testing.
- PDF ingestion using the existing PyMuPDF-based tooling, plus the existing HTML fallback where appropriate.
- Deterministic extraction/normalization, page or URL provenance, checksums, manifests, diagnostics, and validation.
- Stable guide landing pages that clearly link to the confirmed current edition.
- Explicit archival of superseded guide editions.
- Edition comparison and a changelog/report generated from source and normalized-text differences.
- Pull-request-only publication; no direct scheduled write to the default branch and no automatic merge.
- A model-friendly documentation contract, status register, and checkpoint/reconciliation process.
- Unit, fixture-based integration, lifecycle, and end-to-end validation.

### Out of scope — MVP
- Connecting to a customer Oracle HCM tenant or using tenant credentials.
- Collecting live tenant setup, profile options, security configurations, candidate/employee data, or production extracts.
- Automatically asserting that an edition is the edition deployed in a tenant.
- Autonomous Oracle technical advice, automatic configuration changes, or SQL generation.
- Full semantic interpretation of every change through an LLM. AI-generated summaries can be a later, explicitly labeled enhancement.
- Guaranteeing perfect reconstruction of scanned pages, complex diagrams, visual-only tables, or multi-column PDFs without visual review/OCR.
- Publishing secrets, tenant data, private local indexes, or anything not approved for the target repository.

## 7. Product principles

1. **Provenance before convenience.** Every published guide edition must identify its source, edition, retrieval time, checksum, and page/URL map.
2. **No silent gap filling.** Where extraction is ambiguous or validation fails, preserve raw evidence and report the gap rather than inventing a correction.
3. **Current does not mean tenant-current.** “Current in this library” means latest verified candidate in the source catalogue; it does not assert tenant release equivalence.
4. **Keep the last known good edition.** An incomplete download, parser error, URL loop, schema failure, or test failure cannot replace it.
5. **PR-first publication.** The automation proposes changes. A reviewer accepts them; it does not auto-merge.
6. **Deterministic first.** The MVP uses deterministic parsing/normalization for source text. LLM-generated interpretation is optional, labeled, and cannot become source text.
7. **History is a product feature.** Archive superseded editions explicitly instead of relying solely on Git archaeology.
8. **Trace status to evidence.** “Implemented”, “tested”, “CI passed”, and “accepted” are distinct statuses.
9. **Minimize external dependencies.** Reuse Python standard-library parsing/network components, existing PyMuPDF ingestion, GitHub Actions, Git, and SQLite FTS5 where fit.
10. **Open collaboration.** Organize the public library for coworkers to browse, review changes, and contribute using standard GitHub workflows.

## 8. Assumptions and constraints

| ID | Statement | Status / owner | Consequence if wrong |
|---|---|---|---|
| ASM-ORCH-001 | The Product Owner states that personal/organizational use and coworker sharing are authorized. Publication scope and evidence of approval should be recorded before the first automated public content publication. | Project-provided premise; PO owns confirmation | Change publication/storage policy; local tooling can still be developed |
| ASM-ORCH-002 | GitHub public repository and GitHub Actions are acceptable hosting and scheduling choices. | PROPOSED; PO confirms | Select another hosting/scheduler |
| ASM-ORCH-003 | The first live content slice is official Oracle Fusion Cloud HCM, starting with Recruiting. The repository taxonomy can support OCI and BI Publisher later, but their inclusion in the monitored source scope is not yet approved. | PROPOSED; PO owns | Adjust catalogue and discovery scope without renaming the repository |
| ASM-ORCH-004 | Existing scripts are reusable after defects and current tests are validated. | IMPLEMENTED-UNVERIFIED; DEV/QA | Repair, replace, or narrow the reusable surface |
| ASM-ORCH-005 | Guide edition IDs and tenant quarterly release are separate fields and must not be conflated. | Required design rule | Wrong currency claims and incorrect recommendations |

Do not add these assumptions to the existing HCM project assumption register unless that register's scope is intentionally expanded; keep cross-project requirements IDs stable and traceable here.

## 9. End-to-end user experience

1. A weekly job checks the official source catalogue and relevant guide landing pages.
2. Each observed candidate is compared with the known edition metadata and prior checksums.
3. A candidate is fetched only from an approved source scope. Fetch errors, redirects outside scope, unexpected content types, and incomplete page chains are recorded.
4. The document is parsed and normalized using deterministic rules. The manifest records source hashes, page count, per-page metadata, diagnostics, and tool version.
5. Validation checks structural completeness, usable text coverage, source-location continuity, Markdown integrity, and known parser hazards.
6. If content is unchanged, the run records a successful no-change outcome without opening a content PR.
7. If a validated new edition is found, the previous edition is moved into the archive, the current guide landing page is updated, and a proposed changelog and manifest are added on a bot branch.
8. CI validates the proposed tree. The automation opens or updates a PR with the source/edition comparison, test summary, and warnings.
9. A human reviewer accepts, requests changes, or rejects the candidate.
10. On the next session, MODEL_ONBOARDING.md and STATUS-001 communicate exactly what is accepted and what remains proposed.

## 10. User-visible repository experience

The intended repository has:
- a front-page index grouped by product family, then HCM module / OCI service / BI Publisher area and guide type;
- a stable landing page per guide identifying the current edition and its metadata;
- readable Markdown with preserved source page/section or source-URL anchors;
- an explicit archive folder organized by module, guide and edition;
- a catalogue and machine-readable edition manifests;
- weekly change reports and links to the PR that introduced each edition;
- contributor instructions and model onboarding.

See ARCH-001 for a proposed directory layout and DATA-001 for the metadata contract.

## 11. Release strategy

- **MVP-0: reliability baseline.** Reconcile the current HTML parser defect and actual test results; define contracts and fixtures.
- **MVP-1: one-guide vertical slice.** Use the already registered Recruiting guide as a representative case; prove discovery, retrieval, conversion, provenance, validation, change detection, archive and PR lifecycle with controlled fixtures.
- **MVP-2: weekly operation.** Enable the weekly scheduler and manual recovery path only after the vertical slice passes.
- **MVP-3: catalogue expansion.** Add approved HCM guides first, then OCI and BI Publisher only when prioritized; use product-family metadata and shared adapters rather than copied code.
- **Later: semantic change summaries.** If LLM summarization is adopted, summaries remain attributed to a model/tool version and require reviewer acceptance.
- **Separate future product:** tenant configuration evidence and technical-answer validation. It may consume the reference library but is not part of this library MVP.

## 12. Acceptance and launch gate

The MVP is not accepted until all required checks in SRS-001 and TEST-001 pass on the same candidate commit, the intended source/edition scope is recorded, archives are exercised with a controlled test, PR-only publication is demonstrated, operational recovery is documented, and the Product Owner accepts the output.

## 13. Open questions

- Which modules and guide types are first-wave scope? Owner: PO.
- Approve the public repository name and topology. Recommendation: oracle-product-reference-library for published Markdown/archive; keep processing in walsh2232/hcm during the initial MVP. Owner: PO.
- What is the intended meaning of “DEE” in the speech-to-text transcript of the kickoff? The transcript alone does not establish whether this was a real acronym or transcription error. Owner: PO; no expansion is inferred in this specification.
- Which human will act as independent architecture reviewer and QA reviewer? Owner: PO.
- What page-text completeness threshold is acceptable per guide type? Owners: QA + DOC.
- Should full-text search be implemented only through GitHub Markdown initially, or also through a generated local/offline FTS bundle? Proposed MVP: GitHub browsing first; local FTS as a tool, not a required hosted service.
