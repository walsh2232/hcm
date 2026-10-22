# Gap Log & Assumption Register

What we do not know, who is finding out, and what we are assuming meanwhile.

Owner: Documentation Specialist (log integrity) · gap owners are named per row.
Process: [`../decision-framework.md`](../decision-framework.md) §4–§5.

Gap types: `MISSING` (Oracle documents it, we lack the document) · `SILENT`
(Oracle does not document it) · `AMBIGUOUS` (sources conflict or admit two
readings) · `SCOPE` (a business decision, not a documentation question) ·
`STALE` (source predates the deployed release).

## Open gaps

### GAP-001 · MISSING · **Critical**
**Thirteen public Oracle module source sets are registered, but local ingest and target-tenant validation have not yet been completed.**

- Progress: ORC, GHR, ABS, BEN, TIM, LRN, CMP, PAY, JRN, HDS, HSE, TAL and RPT now have module manifests and source maps using official Oracle guide/catalog and current or latest-located release readiness URLs. A local PDF/HTML download, extraction and SQLite FTS retrieval pipeline is committed, along with a weekly source-fingerprint/release-discovery workflow.
- Blocks: functional decisions still require local ingest, actual target-release verification and tenant-specific validation. Other HCM areas such as HCM Common, Security, Integrations, Data Conversion, and additional country-specific localization sources remain to be inventoried.
- Owner: Documentation Specialist.
- Needed: install requirements-knowledge.txt, run refresh/ingest for each of the thirteen manifests, inspect search results and page locators, then add further module manifests from their actual Oracle Books catalogs. Do not commit Oracle manuals or full-text extracts to this public repository.
- Working assumption: ASM-001 and ASM-003 remain open pending project scope and release decisions.
- Target: HCM-010 source-intake completion.
- If unresolved: the retrieval engine exists but recommendations remain bounded by public documentation and do not include customer configuration or Oracle Support material behind authentication.

### GAP-002 · SCOPE · **Critical**
**In-scope HCM modules, target release, and phasing are undefined.**

- Blocks: `HCM-011`, coverage assessment in `source-registry.md`, and the
  sequencing of every design card.
- Owner: Product Owner.
- Needed: module codes marked in-scope / phase 2 / out-of-scope; target quarterly
  release; go-live sequencing.
- Working assumption: `ASM-001`, `ASM-002`.
- Target: `HCM-011`.

### GAP-003 · SCOPE · High
**Country, legal employer, and localisation scope is undefined.**

- Blocks: `HCM-026`, `HCM-034`, and any payroll or absence design.
- Owner: Product Owner with Business Analyst.
- Needed: countries, legal employers, statutory reporting obligations, languages,
  and which localisations Oracle must cover versus which are handled elsewhere.
- Target: `HCM-011`.

### GAP-004 · SCOPE · High
**Environment and instance topology is unknown.**

- Blocks: `HCM-012`, `HCM-025`, test environment planning in `HCM-015`.
- Owner: Solution Architect.
- Needed: instance list, purpose, refresh cadence and source, data classification.
- Target: `HCM-012`.

### GAP-005 · SCOPE · High
**Success criteria and go-live exit criteria are undefined.**

- Blocks: `HCM-013`, `HCM-015`, and release acceptance.
- Owner: Product Owner.
- Needed: measurable business outcomes and per-release exit criteria with owners.
- Target: `HCM-013`.

### GAP-006 · SCOPE · High
**Current-state systems, interfaces, volumes, and constraints are unknown.**

- Blocks: `HCM-014`, `HCM-021`, `HCM-023`, `HCM-033`, `HCM-034`.
- Owner: Business Analyst with Solution Architect.
- Needed: system inventory, interface inventory, data volumes, retention and
  residency constraints, retire/retain/replace decisions.
- Target: `HCM-014`.

### GAP-007 · SCOPE · Medium
**Delivery constraints are undefined** — team composition, cadence, dates,
compliance regimes, audit obligations, and any partner or systems-integrator
involvement.

- Blocks: sprint sizing, `HCM-034`, and the realism of every forecast in the backlog.
- Owner: Product Owner.
- Needed: delivery model, cadence, key dates, applicable regimes.
- Target: refinement.

## Closed gaps

_None._

---

# Assumption Register

Every assumption carries an owner, an expiry, and the cost of being wrong.
**An expired assumption fails the build** (`scripts/project_lint.py`). Renew it
with new evidence and a reason, or resolve it — never let it drift.

### ASM-000 · _Reserved — illustrative example only_
Used in documentation examples. Never a real assumption.

### ASM-001 · Open
**The deployment is Oracle Fusion Cloud HCM (SaaS), not PeopleSoft HCM, E-Business
Suite HR, or a hybrid.**

- Basis: the project is named "Oracle HCM" with no product qualifier. No Tier A
  source. This is an inference, not a fact.
- Blocks / affects: the entire repository structure, module code index, HDL and
  extract tooling, quarterly-update process — effectively every artifact produced
  so far.
- Owner: Product Owner.
- Expires: 2026-09-30.
- If wrong: the module index, integration patterns, and data-loading approach are
  wrong for the platform. The project operating system (Kanban, ADRs, registry,
  decision framework) still stands; roughly 1–2 days of rework in
  `docs/modules/`, `integrations/`, and `data/`.
- Resolved by: `HCM-011`.

### ASM-002 · Open
**Scope is the HCM pillar only — no ERP, SCM, or EPM cross-pillar delivery in this
repository.**

- Basis: project framing. No Tier A source.
- Affects: module index, integration inventory boundary, role model.
- Owner: Product Owner.
- Expires: 2026-09-30.
- If wrong: cross-pillar integration and shared-security design enter scope; the
  module index and `integrations/` structure expand. Low rework cost, significant
  scope cost.
- Resolved by: `HCM-011`.

### ASM-003 · Open
**Oracle's quarterly update cadence applies to this environment, and the project
must absorb four feature releases per year.**

- Basis: standard Oracle Fusion Cloud SaaS behaviour. Tier D (model knowledge)
  pending a Tier A/B citation — it is treated as an assumption precisely because
  it is not yet cited.
- Affects: source currency sweep, regression strategy (`HCM-015`), release
  management (`HCM-025`), quarterly monitoring (`HCM-032`).
- Owner: Solution Architect.
- Expires: 2026-09-30.
- If wrong: the currency and regression cadence are wrong; sweep scheduling
  changes. Roughly half a day of rework, but a wrong cadence silently ages every
  registry entry.
- Resolved by: `HCM-010` (a Tier A/B citation retires this assumption).

## Expired / renewed

_None._
