# Kanban Board

**Sprint:** 000 — Inception · **Updated:** 2026-08-23 · **Board rules:** [`workflow.md`](workflow.md)

Card format — `HCM-###` · `[role]` · title · linked artifacts · estimate.
Roles: `PO` Product Owner · `BA` Business Analyst · `SA` Solution Architect ·
`DEV` Developer · `QA` QA/Testing · `DOC` Documentation Specialist.
Full card bodies live in [`backlog.md`](backlog.md).

---

## Backlog

_No WIP limit. Ranked in [`backlog.md`](backlog.md); the top of that rank is what
gets refined next._

- HCM-020 [BA] Fit/gap analysis framework and worksheet · ~2d
- HCM-021 [SA] Integration architecture baseline — patterns catalogue · ~4d
- HCM-022 [SA] Security & role design approach (SEC) · ~4d
- HCM-023 [SA] Data conversion strategy — HDL load sequencing (DAT) · ~4d
- HCM-024 [DEV] HDL template library and validation harness (DAT/INT) · ~5d
- HCM-025 [SA] Environment refresh & release management approach · ~3d
- HCM-026 [BA] Workforce structures design — enterprise, legal, org (GHR) · ~5d
- HCM-027 [QA] Test data strategy — synthetic fixtures, no production PII · ~3d
- HCM-028 [DOC] Runbook set — cutover, hypercare, quarterly update · ~4d
- HCM-029 [SA] Reporting & analytics approach — OTBI vs BI Publisher (RPT) · ~3d
- HCM-030 [SA] Extension policy — configuration vs. Redwood/VBS extension (EXT) · ~3d
- HCM-031 [BA] Approvals & workflow (BPM) design approach · ~3d
- HCM-032 [DOC] Oracle quarterly update monitoring process · ~2d
- HCM-033 [QA] Non-functional requirements — performance, availability, volumes · ~3d
- HCM-034 [SA] Compliance & data residency assessment · ~3d
- HCM-035 [DEV] CI pipeline extension — artifact validation per module · ~3d

## Ready

_WIP limit 6 · currently 5_

- HCM-011 [PO] Confirm in-scope HCM modules, target release, and phasing · GAP-002 · ~1d
- HCM-012 [SA] Environment & instance registry · `config/` · GAP-004 · ~1d
- HCM-013 [PO] Define success criteria and release exit criteria · GAP-005 · ~1d
- HCM-014 [BA] Current-state systems & integration inventory · GAP-006 · ~3d
- HCM-015 [QA] Test strategy outline · HCM-013 · ~2d

## In Progress

_WIP limit 2 per role · currently 1 (DOC)_

- HCM-010 [DOC] Intake batch 1 — receive, register, and index the Oracle HCM documentation set · DOC-001–DOC-006 · GAP-001 · ~2d
  - Progress: DOC-001 (*Implementing Recruiting*, G34431-12) has been hashed, extracted, indexed, and smoke-tested in a private local corpus. DOC-002–DOC-006 have been catalogued from the official Oracle Help Center.
  - Remaining: confirm in-scope modules and target quarterly release; extract companion source content required for those modules; assess coverage and source currency.
  - The card remains in progress because the complete project source set and release binding are not established yet.
## In Review

_WIP limit 6 · currently 6 — Sprint 000 inception batch, single pull request_

- HCM-001 [DOC] Repository structure and contribution standards · ADR-0003 · ~1d
- HCM-002 [PO] Role charters, decision rights, RACI, escalation · `roles.md` · ~1d
- HCM-003 [PO] Kanban workflow, DoR/DoD, and artifact templates · ADR-0004 · ~1d
- HCM-004 [DOC] Documentation ingest system, source registry, gap log · ADR-0002 · ~2d
- HCM-005 [SA] Decision-making & source validation framework · ADR-0002, ADR-0005 · ~1d
- HCM-006 [DEV] Project lint and CI automation · ADR-0004 · ~1d

## Done

_Sprint 000 has not closed. Cards move here when the inception pull request is
merged and the Definition of Done is confirmed card by card._

_(empty)_

---

## Flow notes

- **Everything downstream of documentation intake is gated on HCM-010.** Module
  design cards stay in Backlog rather than Ready, because they cannot meet the
  Definition of Ready without a backing `DOC-###` — see
  [`docs/gaps.md`](docs/gaps.md) `GAP-001`.
- The five Ready cards were chosen because they are answerable by the Product
  Owner from project context rather than from Oracle documentation, so they
  unblock without the document set.
