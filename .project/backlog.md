# Product Backlog

Ranked. Rank is the Product Owner's decision and is the only ordering that
matters — dates are forecasts, rank is commitment order. Card bodies use
[`templates/story.md`](templates/story.md).

Board state: [`kanban.md`](kanban.md) · Gaps: [`docs/gaps.md`](docs/gaps.md)

## Rank

| Rank | ID | Title | Role | State | Blocked by |
| --- | --- | --- | --- | --- | --- |
| 1 | HCM-010 | Intake batch 1 — Oracle HCM documentation set | DOC | In Progress | GAP-001 |
| 2 | HCM-011 | Confirm in-scope modules, release, phasing | PO | Ready | — |
| 3 | HCM-013 | Success criteria and release exit criteria | PO | Ready | — |
| 4 | HCM-014 | Current-state systems & integration inventory | BA | Ready | — |
| 5 | HCM-012 | Environment & instance registry | SA | Ready | — |
| 6 | HCM-015 | Test strategy outline | QA | Ready | HCM-013 |
| 7 | HCM-020 | Fit/gap analysis framework | BA | Backlog | HCM-010, HCM-011 |
| 8 | HCM-026 | Workforce structures design (GHR) | BA | Backlog | HCM-010, HCM-011 |
| 9 | HCM-022 | Security & role design approach (SEC) | SA | Backlog | HCM-010 |
| 10 | HCM-021 | Integration architecture baseline | SA | Backlog | HCM-010, HCM-014 |
| 11 | HCM-023 | Data conversion strategy (DAT) | SA | Backlog | HCM-010, HCM-014 |
| 12 | HCM-025 | Environment refresh & release management | SA | Backlog | HCM-012 |
| 13 | HCM-030 | Extension policy — config vs. extension (EXT) | SA | Backlog | HCM-010 |
| 14 | HCM-031 | Approvals & workflow (BPM) design approach | BA | Backlog | HCM-010, HCM-026 |
| 15 | HCM-024 | HDL template library & validation harness | DEV | Backlog | HCM-023 |
| 16 | HCM-027 | Test data strategy | QA | Backlog | HCM-015 |
| 17 | HCM-029 | Reporting & analytics approach (RPT) | SA | Backlog | HCM-010, HCM-011 |
| 18 | HCM-033 | Non-functional requirements | QA | Backlog | HCM-014 |
| 19 | HCM-034 | Compliance & data residency assessment | SA | Backlog | HCM-011, HCM-014 |
| 20 | HCM-032 | Oracle quarterly update monitoring process | DOC | Backlog | HCM-010 |
| 21 | HCM-028 | Runbook set — cutover, hypercare, updates | DOC | Backlog | HCM-025 |
| 22 | HCM-035 | CI pipeline extension — per-module validation | DEV | Backlog | HCM-024 |
| — | HCM-001..006 | Sprint 000 inception batch | — | In Review | — |

---

# Cards

## Sprint 000 — inception (In Review)

### HCM-001
**Repository structure and contribution standards** · `[DOC]` · ~1d · In Review

Outcome: a contributor can tell, without asking, where any artifact belongs and
what standard it must meet. Root `README`, `CONTRIBUTING`, `.gitignore` with a PII
guard, and a `README` in every top-level directory stating what belongs there and
the naming convention that applies.

Acceptance: every top-level directory documented; branch, commit, and PR
conventions stated; `data/live/` and credential patterns excluded from git.
Source: `N/A — internal process decision` · `ADR-0003`.

### HCM-002
**Role charters, decision rights, RACI, escalation** · `[PO]` · ~1d · In Review

Outcome: each of the six roles knows what it decides outright, what it must
consult on, and where a decision is recorded. Produces `roles.md`.

Acceptance: decision-rights table covers all six roles; RACI covers every
recurring activity; each decision class has exactly one recording channel;
escalation path has three defined levels. Source: `N/A — internal process decision`.

### HCM-003
**Kanban workflow, DoR/DoD, and artifact templates** · `[PO]` · ~1d · In Review

Outcome: five-state board with WIP limits, transition gates, a Definition of Ready
and a Definition of Done, and a template for every artifact the project produces.

Acceptance: `workflow.md`, `kanban.md`, `backlog.md`, `templates/` (story, spec,
ADR, test case, sprint plan, retrospective, runbook, doc intake), `sprints/`
seeded with Sprint 000. Source: `N/A — internal process decision` · `ADR-0004`.

### HCM-004
**Documentation ingest system, source registry, gap log** · `[DOC]` · ~2d · In Review

Outcome: a defined intake path for Oracle documentation, a registry that records
what we hold and which release it describes, and a gap log for what we do not.

Acceptance: `docs/README.md` describes intake end to end; `source-registry.md`
carries the full column contract; `gaps.md` carries gap and assumption schemas;
`docs/modules/README.md` indexes module codes; intake template exists.
Source: `N/A — internal process decision` · `ADR-0002`.

### HCM-005
**Decision-making & source validation framework** · `[SA]` · ~1d · In Review

Outcome: a written test that every design decision must pass before it is
recorded, with source tiering and precedence, release binding, provisional
decisions, and assumption expiry.

Acceptance: four source tiers with explicit permitted uses; A>B>C>D precedence
stated as absolute; five-point validation test; assumption record schema with
owner, expiry, and cost-of-being-wrong; conflict-resolution path with named
options. Source: `N/A — internal process decision` · `ADR-0002`, `ADR-0005`.

### HCM-006
**Project lint and CI automation** · `[DEV]` · ~1d · In Review

Outcome: the traceability rules are machine-checked, so the framework degrades
loudly rather than silently.

Acceptance: `scripts/project_lint.py` validates ID format and uniqueness,
board↔backlog consistency, `DOC`/`GAP`/`ASM` reference integrity, assumption
expiry, ADR structure and citations, and WIP limits; exits non-zero on error; runs
in GitHub Actions on every push and pull request. Source: `N/A — internal process decision`.

---

## Ready

### HCM-010
**Intake batch 1 — receive, register, and index the Oracle HCM documentation set**
· `[DOC]` · ~2d · In Progress

Outcome: the official Oracle sources needed for the in-scope HCM modules are
registered, edition-bound, retrievable, and indexed, so downstream work can cite
the source and prove which edition supports a claim.

Current intake: DOC-001 (*Implementing Recruiting*, G34431-12) is indexed in a
private local corpus with 35 chapter files, 648 searchable SQLite topic headings, 650 CSV topic-index entries, and 751 retrieval chunks,
a SQLite FTS5 search index, 19 source-linked playbooks, and page-level citations. DOC-002–DOC-006 are
catalogued official companion references but are not yet fully ingested locally.

Acceptance:
- Each selected source is registered with title, Oracle identifier/URL, edition,
  tier, retrieval date, location, and target-release validation state.
- Each in-scope module is indexed in `docs/modules/README.md`; missing coverage
  raises a `MISSING` gap.
- Extracted sources have a manifest, checksum, physical-page traceability, and
  validated search/retrieval output.
- Source conflicts are raised as `AMBIGUOUS` gaps rather than silently reconciled.
- Full derived text stays out of the public repository; scripts, metadata, compact
  source maps, and targeted evidence extracts may be committed.
- Intake summary is recorded using `templates/doc-intake.md`.

Source: intake process defined in ADR-0002; Oracle guide DOC-001 edition G34431-12.

### HCM-011
**Confirm in-scope HCM modules, target release, and phasing** · `[PO]` · ~1d · Ready

Outcome: an unambiguous scope statement — which Oracle Fusion Cloud HCM modules
are in scope, in which phase, against which quarterly release, for which legal
employers and countries.

Acceptance: module codes from `docs/modules/README.md` marked in-scope /
out-of-scope / phase 2; target release named (e.g. `25D`); country and legal
employer scope stated; localisation requirements named; each in-scope module has
an owner. Resolves `GAP-002`.

Why it is Ready without documentation: this is a business scope decision, not a
product question.

### HCM-012
**Environment & instance registry** · `[SA]` · ~1d · Ready

Outcome: `config/environments.md` records every Oracle HCM instance — purpose,
release, refresh source and cadence, data classification, and who may change it.
No credentials, no endpoints that constitute a secret.

Acceptance: every instance listed with purpose (DEV/TEST/UAT/PROD and any
training or conversion instances); refresh strategy per instance; data
classification and masking obligation per instance; change-control owner named.
Resolves `GAP-004`.

### HCM-013
**Define success criteria and release exit criteria** · `[PO]` · ~1d · Ready

Outcome: a written definition of what "done" means for the implementation, not
just for a card — the measurable conditions under which each release may go live.

Acceptance: business outcomes stated measurably; go-live exit criteria per
release (functional, data, integration, security, performance, training,
support); named owner per criterion; explicit statement of what is *not* success.
Resolves `GAP-005`.

### HCM-014
**Current-state systems & integration inventory** · `[BA]` · ~3d · Ready

Outcome: an inventory of the systems Oracle HCM must coexist with — what each
does, what data crosses the boundary, in which direction, at what frequency and
volume, and under what constraint.

Acceptance: every interface listed with source, target, payload, direction,
frequency, volume, latency tolerance, and owner; legacy systems marked
retire/retain/replace; data-quality and compliance constraints noted; feeds
`HCM-021`, `HCM-023`, `HCM-033`, `HCM-034`. Resolves `GAP-006`.

### HCM-015
**Test strategy outline** · `[QA]` · ~2d · Ready

Outcome: the shape of testing — levels, entry/exit criteria per level,
environments, data, roles, and defect management — sized to the scope agreed in
`HCM-011` and the criteria in `HCM-013`.

Acceptance: test levels defined (unit/config, functional, integration, payroll
parallel where applicable, security/role, UAT, regression against quarterly
updates); entry and exit criteria per level; environment and data requirements
stated; defect severity/priority matrix agreed with the PO; regression approach
for Oracle quarterly updates named. Depends on HCM-013.

---

## Backlog

### HCM-020
**Fit/gap analysis framework and worksheet** · `[BA]` · ~2d

A repeatable worksheet that classifies each requirement as fit / configure /
extend / integrate / process-change / defer, with the Oracle source cited for the
classification and the cost of each non-fit stated. Feeds every module design
card. Depends on HCM-010, HCM-011.

### HCM-021
**Integration architecture baseline — patterns catalogue** · `[SA]` · ~4d

The set of approved integration patterns (HCM Extracts, HDL, REST, SOAP, ATOM
feeds, file-based) with the decision rule for choosing between them, error
handling, retry, monitoring, and reconciliation expectations. Each pattern cites
the Oracle source that establishes its constraints. Produces an ADR.
Depends on HCM-010, HCM-014.

### HCM-022
**Security & role design approach (SEC)** · `[SA]` · ~4d

Approach to job, duty, data, and abstract roles: what is inherited, what is
custom, how data security is scoped, how segregation of duties is evidenced, and
how role changes survive quarterly updates. Produces an ADR. Depends on HCM-010.

### HCM-023
**Data conversion strategy — HDL load sequencing (DAT)** · `[SA]` · ~4d

Object load order, dependency handling, key mapping and source-key strategy,
reconciliation, error correction cycle, and mock-conversion cadence. Produces an
ADR. Depends on HCM-010, HCM-014.

### HCM-024
**HDL template library and validation harness (DAT/INT)** · `[DEV]` · ~5d

Version-controlled HDL templates per business object with a local validator that
catches structural errors before upload. Synthetic fixtures only.
Depends on HCM-023.

### HCM-025
**Environment refresh & release management approach** · `[SA]` · ~3d

How configuration moves between instances, what is carried by configuration
migration versus rebuilt, refresh cadence and masking, and how quarterly updates
are absorbed and regression-tested. Depends on HCM-012.

### HCM-026
**Workforce structures design — enterprise, legal, organisation (GHR)** · `[BA]` · ~5d

Enterprise structure, legal employers, business units, divisions, departments,
locations, jobs, positions, and grades — the decisions that are expensive to
change later. Produces an ADR. Depends on HCM-010, HCM-011.

### HCM-027
**Test data strategy — synthetic fixtures, no production PII** · `[QA]` · ~3d

How representative test data is generated, masked, refreshed, and kept out of the
repository, including payroll-sensitive scenarios. Depends on HCM-015.

### HCM-028
**Runbook set — cutover, hypercare, quarterly update** · `[DOC]` · ~4d

Executable runbooks using `templates/runbook.md`: cutover sequence with timings
and rollback, hypercare triage and escalation, and the quarterly update
absorption procedure. Depends on HCM-025.

### HCM-029
**Reporting & analytics approach — OTBI vs BI Publisher (RPT)** · `[SA]` · ~3d

Decision rule for OTBI versus BI Publisher versus extract-and-warehouse, subject
area availability, security inheritance in reporting, and performance
constraints. Depends on HCM-010, HCM-011.

### HCM-030
**Extension policy — configuration vs. Redwood/VBS extension (EXT)** · `[SA]` · ~3d

When to configure, when to extend, and the maintenance cost accepted by
extending, including quarterly-update regression exposure. Produces an ADR.
Depends on HCM-010.

### HCM-031
**Approvals & workflow (BPM) design approach** · `[BA]` · ~3d

Approval hierarchies, delegation, notification design, and the rule for
representing organisational approval policy in BPM without unmaintainable
rule sprawl. Depends on HCM-010, HCM-026.

### HCM-032
**Oracle quarterly update monitoring process** · `[DOC]` · ~2d

Who reads *What's New* for each release, how affected registry entries and ADRs
are identified, and how the source currency sweep is scheduled and evidenced.
Depends on HCM-010.

### HCM-033
**Non-functional requirements — performance, availability, volumes** · `[QA]` · ~3d

Population volumes, transaction peaks (payroll runs, open enrolment, performance
cycles), availability windows, and the measurable targets each will be tested
against. Depends on HCM-014.

### HCM-034
**Compliance & data residency assessment** · `[SA]` · ~3d

Applicable data protection and employment regimes by country, residency
constraints, retention and erasure obligations, audit evidence requirements, and
their impact on integration and reporting design. Depends on HCM-011, HCM-014.

### HCM-035
**CI pipeline extension — per-module artifact validation** · `[DEV]` · ~3d

Extend CI beyond project lint: validate HDL templates, fast formula syntax where
tooling allows, report definitions, and configuration exports on every PR.
Depends on HCM-024.
