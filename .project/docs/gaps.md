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
**The complete Oracle HCM source set and tenant-release binding are not yet established.** Initial Recruiting intake is registered: DOC-001 (*Implementing Recruiting*, G34431-12) has a private local extraction; DOC-002–DOC-006 are catalogued official companion references, but they are not yet searchable in the local corpus. The target quarterly HCM release and final in-scope module list remain unknown.

- Blocks: completion of `HCM-010` and module design cards in the backlog (`HCM-020`–`HCM-035`).
- Owner: Product Owner (scope/target release) and Documentation Specialist (source intake/currency).
- Needed: confirmed module scope, target quarterly release, and a source manifest for each in-scope module; retrieve/parse companion references as needed.
- Working assumptions: `ASM-001`, `ASM-002`, `ASM-003` remain provisional and must not substitute for source validation.
- Target: `HCM-011` and the next intake batch.
- If unresolved: no module-specific design decision can meet the validation test in `decision-framework.md` §3. Scope, environment, success-criteria, and current-state cards remain separately actionable.

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

### GAP-008 · AMBIGUOUS · **High**
**Oracle Search reingest identifier must be confirmed for the relevant configuration context.** DOC-001 Chapter 1 gives `fa-hcm-job application` (with a space) for Oracle Search maintenance after P2T/T2T when advanced job-application filters are in use; Chapter 13 gives `fa-hcm-jobapplication` (without a space) for Configure Attachment Search and attachment-index reingest. The contexts differ and the source alone does not establish whether these names should differ or whether one is a source typo.

- Blocks: execution of the affected Oracle Search reingest and any runbook that would select one identifier without tenant/release confirmation.
- Owner: Solution Architect with Documentation Specialist; raise an Oracle Support question if the target UI/current guide does not resolve the distinction.
- Needed: inspect the target tenant's Configure Attachment Search row and run the current-release Oracle Search/P2T guidance before executing; retain the selected index name and evidence.
- Working assumption: none. Do not guess or substitute one identifier for the other.
- Target: before the next affected P2T/T2T or advanced attachment-search reingest.

### GAP-009 · AMBIGUOUS · **High**
**The TDS guide's active-rule limit statement appears to conflict with its multi-rule precedence example.** DOC-001 Chapter 35, physical PDF p. 443 / printed p. 425, states that only one rule can be active for an action at a time, then describes several rules for a specific action ordered by precedence. The source page has been visually checked; don't treat the issue as a text-extraction artifact.

- Blocks: TDS designs whose correctness depends on multiple simultaneously active rules for an action or on a definitive interpretation of rule precedence.
- Owner: Solution Architect with Documentation Specialist.
- Needed: inspect the TDS rule list in the target tenant and check current-release Oracle guidance; test only in non-production and raise an Oracle Support question if the source remains ambiguous.
- Working assumption: none. Do not guess whether the statements describe separate behaviors or a documentation inconsistency.
- Target: before approving a TDS design that depends on multiple active rules for an action.

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
- Expires: 2026-12-31.
- Renewal reason (2026-10-22): DOC-001 confirms the documentation concerns Oracle Fusion Cloud HCM, but it does not establish the actual target tenant/product topology. Product Owner confirmation remains pending in HCM-011.
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
- Expires: 2026-12-31.
- Renewal reason (2026-10-22): the Recruiting source intake does not establish whether cross-pillar ERP/SCM/EPM scope exists. Product Owner confirmation remains pending in HCM-011.
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
- Expires: 2026-12-31.
- Renewal reason (2026-10-22): guide edition identifiers do not establish the tenant's target quarterly update. Record that release in HCM-011 before claiming release validation.
- If wrong: the currency and regression cadence are wrong; sweep scheduling
  changes. Roughly half a day of rework, but a wrong cadence silently ages every
  registry entry.
- Resolved by: `HCM-010` (a Tier A/B citation retires this assumption).

## Expired / renewed

_None._
