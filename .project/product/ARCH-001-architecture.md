---
id: ARCH-ORCH-001
title: Proposed architecture and tool selection
artifact_type: architecture-design-specification
status: PROPOSED
version: 1.0.0
owner_role: SA
reviewer_roles: [PO, DEV, QA]
last_reviewed: 2026-10-27
related_work_item: HCM-036
---

# ARCH-001 — Architecture and Tool Choices

## 1. Architectural intent

Build a deterministic, source-traceable pipeline that retrieves official guide editions, extracts and normalizes content, validates completeness, compares versions, and proposes changes through pull requests. The tool shall fail closed: a candidate that is incomplete or invalid never replaces the last accepted current edition.

The existing walsh2232/hcm repository remains the development/tooling and project-governance location. The proposed end-user library is a separate public repository, currently only a candidate named oracle-hcm-reference-library. Neither the creation of that repository nor the weekly workflow is claimed complete by this architecture document.

## 2. Component model

The proposed flow is:

Source catalogue → discovery/check → fetch adapter → immutable source snapshot + checksum → PDF/HTML adapter → normalized Markdown + per-location records → validation → diff/archive planning → bot branch → CI → pull request → human review → accepted current edition.

Cross-cutting components:
- catalogue and lifecycle metadata;
- run log and per-guide status;
- version-aware source citations;
- allowlisted fetch policy and bounded retries;
- test fixtures and failure-injection coverage;
- onboarding/status documents that describe actual state.

## 3. Proposed repository layout for the dedicated output library

    README.md
    catalogue/
      modules.yml
      guides.yml
    guides/
      recruiting/
        implementing-recruiting/
          README.md
          current.md
      <module>/
        <guide-slug>/
          README.md
          current.md
    archive/
      <module>/
        <guide-slug>/
          <edition-id>.md
    metadata/
      manifests/
        <guide-id>/
          <edition-id>.json
      runs/
        <YYYY-MM-DD>/
          report.json
    changelog/
      weekly/
        <YYYY-MM-DD>.md
    scripts/
      oracle_docs/
    tests/
    .github/
      workflows/
        refresh-docs.yml

The exact guide folder names can evolve before the new repository is created. Once consumers depend on paths, use stable landing pages and do not rename current URLs unnecessarily. Archived files are versioned content; manifests are machine-readable provenance records. A guide README identifies the current edition, current-status evidence, latest successful refresh, and links to archives.

The existing development scripts remain under scripts/oracle_docs/ in walsh2232/hcm until the separate repository boundary and transfer strategy are accepted.

## 4. Tool choices

| Tool | Use | State and rationale |
|---|---|---|
| GitHub repositories and pull requests | Version control, public browsing, history, review and archival content | Existing and available; existing repo is walsh2232/hcm. Dedicated output repo is PROPOSED. |
| GitHub Actions | Weekly schedule, manual recovery, test gates, bot branch and PR creation | Existing project workflow is manual-only today. Scheduled workflow is PROPOSED. Official behavior: https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows |
| Python 3.11 in CI | Shared implementation and repeatable test environment | Existing project-lint workflow uses Python 3.11. Keep the new pipeline compatible with the declared Python support baseline. |
| Python urllib.request | HTTPS source retrieval in the existing HTML ingester | Already used. Add explicit host/path allowlisting, bounded timeout, retry/backoff, size limits and redirect checks before production use. |
| Python html.parser | HTML navigation and deterministic extraction | Already used by ingest_oracle_html.py. Its current anchor handling appears to reference an undefined variable; fix and test before relying on it. |
| PyMuPDF (fitz) | PDF text-layer extraction, page iteration and physical page markers | Already required by ingest_pdf.py. It is not OCR and does not guarantee reconstruction of complex visual layouts. |
| Existing normalize_markdown.py | Conservative deterministic formatting normalization | Already exists. Its scope is layout cleanup; it must not rewrite technical identifiers or resolve source contradictions. |
| SQLite FTS5 | Local search across normalized retrieval chunks | Already implemented by search_corpus.py and intentionally local in the current project. Hosted FTS is not required for MVP. |
| Python unittest | Offline regression tests for parsing, manifests, lifecycle and search | Existing tests use unittest. Avoid introducing pytest solely for the MVP. |
| Existing project_lint.py | Validate project governance and link consistency | Existing validator; current automatic invocation is not active because project-lint.yml is manual-only. |
| GitHub Markdown | Human-readable guides, manifests, status and onboarding | Avoid requiring a custom web application for MVP. |
| LLM service | No source conversion dependency in MVP | Deterministic tools preserve reproducibility. LLM-assisted summaries are a later optional layer, clearly attributed and reviewed. |

Dependency additions require a short rationale, compatibility/security review, and test coverage. Keep all source retrieval behind a single adapter interface so the source host or retrieval method can change without rewriting archive logic.

## 5. GitHub Actions behavior

The proposed refresh workflow has two triggers: a weekly schedule and workflow_dispatch. The schedule must run from the default branch; scheduled timing can be delayed and a public repository may have its schedule disabled after 60 days without repository activity. The operator runbook must include manual recovery and schedule-health checks. Place the cron minute away from the top of the hour to reduce contention risk.

Use least-privilege workflow permissions. A workflow that creates a branch and pull request will need content write and pull-request write permissions limited to the job that publishes a candidate. Do not use pull_request_target to execute untrusted PR code with write credentials. Do not log tokens. Pin third-party actions to reviewed full commit SHAs before treating the public workflow as production-ready.

References:
- Schedule, workflow_dispatch, and schedule limitations: https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows
- Workflow syntax and token permission controls: https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax
- Workflow recovery and schedule troubleshooting: https://docs.github.com/en/actions/how-tos/troubleshoot-workflows

## 6. Source and fetch policy

The guide catalogue defines approved canonical URLs and permitted host/path scope. A fetch adapter must:
- use HTTPS;
- reject unapproved domains, cross-guide paths, unsafe redirects and unexpected content types;
- apply connection/read timeout and response-size bounds;
- retry transient errors with bounded exponential backoff and respect server failure signals;
- apply a request delay when enumerating multiple pages;
- identify the tool with a meaningful User-Agent;
- record final URL, retrieval timestamp, byte count and SHA-256;
- stop on a failure and report incomplete state rather than fabricating an end of guide.

The existing HTML crawler already limits itself to a guide directory and follows an explicit Next link, but its host validation and parser behavior require further hardening as described in STATUS-001 and TEST-001.

## 7. Conversion and provenance

PDF adapter: record source PDF hash, physical page count, per-page extracted text length, empty/low-text pages and replacement characters. Physical PDF page numbering must not be represented as printed page numbering. No OCR is implied.

HTML adapter: record the canonical index URL, each resolved page URL, source hash, sequence number, content type, and terminal condition. HTML sequence numbers must not be presented as physical or printed PDF pages. A page-count cap is not proof of a complete crawl.

Normalizer: deterministic, with golden fixtures. Exact technical tokens, API names, SQL identifiers, option names, values, and contradictory statements must not be “corrected” by intuition.

## 8. Publication model

A run creates a candidate branch and a single reviewable PR or updates the existing bot PR for the same candidate. It never updates the default branch directly. PR contents include the candidate manifest, change report, validation output, warnings, and archive operation. Automatic merge is out of scope. A failed check marks the PR as blocked and retains last-known-good current content.

## 9. Architecture decisions still requiring acceptance

- Confirm separate public content repository and its name.
- Confirm host/path allowlist and first-wave catalogue.
- Confirm source-publication authorization record and publication scope.
- Confirm review policy and authorized bot identity/token model.
- Confirm whether manifests and weekly reports remain in the public output repo or are copied into a separate operational record.
- Formalize accepted choices as an ADR when the Product Owner/Solution Architect review them. This document records proposals, not final approval.
