# Documentation Source Registry

The authoritative list of every source this project is allowed to cite. If it is
not here, it may not appear in a citation.

Owner: Documentation Specialist · Process: [`README.md`](README.md) ·
Tiering: [`../decision-framework.md`](../decision-framework.md) §1

## Column contract

| Column | Meaning | Rule |
| --- | --- | --- |
| `ID` | `DOC-###`, assigned at intake | Never reused, never renumbered |
| `Title` | Oracle document title, verbatim | No abbreviation |
| `Oracle ref` | Oracle document ID, part number, MOS note ID, or canonical URL | Required for tier A/B |
| `Modules` | Module codes covered | From [`modules/README.md`](modules/README.md) |
| `Release` | The Oracle release the document describes | e.g. `25B`; `n/a` only for release-independent material |
| `Validated` | Release(s) we have confirmed it against | Blank means unvalidated — usable but flagged |
| `Tier` | A / B / C / D | Determines permitted use |
| `Status` | `ACTIVE` · `STALE` · `SUPERSEDED` · `RETIRED` | Superseded entries name their successor in Notes |
| `Received` | Date received | ISO date |
| `Location` | Where the original is held | Store reference, not a personal drive |
| `Extract` | Path to the normalised extract, if any | `oracle/<MODULE>/<DOC-ID>.md` |
| `Notes` | Interpretation notes, conflicts, caveats | Where our reading of an ambiguity is recorded |

## Registry

| ID | Title | Oracle ref | Modules | Release | Validated | Tier | Status | Received | Location | Extract | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DOC-000 | _Reserved — illustrative example only_ | — | — | — | — | — | RESERVED | — | — | — | Used in documentation examples. Never a real citation. |
| DOC-001 | Implementing Recruiting | G34431-12 | ORC | Rolling guide; validate target release | Source metadata confirmed 2026-10-22; functional release validation pending | A | ACTIVE | 2026-10-22 | https://docs.oracle.com/en/cloud/saas/talent-management/faimh/index.html | — (local retrieval index; not committed) | PDF part G34431-12; 448 pages observed. |
| DOC-002 | Using Recruiting | G34440-08 | ORC | Rolling guide; validate target release | Source metadata confirmed 2026-10-22; functional release validation pending | A | ACTIVE | 2026-10-22 | https://docs.oracle.com/en/cloud/saas/talent-management/faush/index.html | — (local retrieval index; not committed) | PDF part G34440-08; 220 pages observed. |
| DOC-003 | Using and Administering Recruiting Booster | G34425-04 | ORC | Rolling guide; validate target release | Source metadata confirmed 2026-10-22; functional release validation pending | A | ACTIVE | 2026-10-22 | https://docs.oracle.com/en/cloud/saas/talent-management/faarb/index.html | — (local retrieval index; not committed) | PDF part G34425-04; 70 pages observed. |
| DOC-004 | Oracle Fusion Cloud Recruiting 26D What's New | G61079-03 | ORC | 26D | 26D metadata confirmed 2026-10-22 | A | ACTIVE | 2026-10-22 | https://docs.oracle.com/en/cloud/saas/readiness/hcm/26d/recr-26d/ | — (retrieved at runtime) | Release-specific readiness source. |
| DOC-005 | Recruiting 26D Feature Summary | https://docs.oracle.com/en/cloud/saas/readiness/hcm/26d/recr-26d/26D-recruiting-wn-t78659.htm | ORC | 26D | URL and page identified 2026-10-22 | A | ACTIVE | 2026-10-22 | https://docs.oracle.com/en/cloud/saas/readiness/hcm/26d/recr-26d/26D-recruiting-wn-t78659.htm | — (retrieved at runtime) | Retrieve the current full feature row/detail before advising. |
| DOC-006 | Oracle Talent Management - All Books | https://docs.oracle.com/en/cloud/saas/talent-management/books.html | ORC, LRN | n/a | Catalog checked 2026-10-22 | A | ACTIVE | 2026-10-22 | https://docs.oracle.com/en/cloud/saas/talent-management/books.html | — | Official guide inventory; includes Implementing Learning and Using Learning; no standalone Administering Recruiting book listed. |

| DOC-007 | Oracle Human Resources - All Books | https://docs.oracle.com/en/cloud/saas/human-resources/books.html | GHR, ABS, BEN, TIM | n/a | Catalog checked 2026-10-22 | A | ACTIVE | 2026-10-22 | https://docs.oracle.com/en/cloud/saas/human-resources/books.html | — (retrieved at runtime/local index) | Official inventory for Human Resources pillar source sets. |
| DOC-008 | Implementing Global Human Resources | G34712-10 | GHR | Rolling guide; validate target release | Title, part and 390-page PDF confirmed 2026-10-22 | A | ACTIVE | 2026-10-22 | https://docs.oracle.com/en/cloud/saas/human-resources/faigh/index.html | — (retrieved at runtime/local index) | Copyright 2026; target-release/tenant validation pending. |
| DOC-009 | Using Global Human Resources | G34740-15 | GHR | Rolling guide; validate target release | Title, part and 368-page PDF confirmed 2026-10-22 | A | ACTIVE | 2026-10-22 | https://docs.oracle.com/en/cloud/saas/human-resources/fawhr/index.html | — (retrieved at runtime/local index) | Copyright 2025; target-release/tenant validation pending. |
| DOC-010 | Oracle Fusion Cloud Human Resources 26D What's New | G61073-04 | GHR | 26D | 26D title and document ID confirmed 2026-10-22 | A | ACTIVE | 2026-10-22 | https://docs.oracle.com/en/cloud/saas/readiness/hcm/26d/hure-26d/ | — (retrieved at runtime/local index) | Release-specific readiness source; validate against the tenant update. |
| DOC-011 | Implementing Absence Management | G34709-01 | ABS | Rolling guide; validate target release | Title, part and 192-page PDF confirmed 2026-10-22 | A | ACTIVE | 2026-10-22 | https://docs.oracle.com/en/cloud/saas/human-resources/faiam/index.html | — (retrieved at runtime/local index) | Copyright 2024; release staleness risk; cross-check 26D readiness. |
| DOC-012 | Using Absence Management | G34736-01 | ABS | Rolling guide; validate target release | Title, part and 40-page PDF confirmed 2026-10-22 | A | ACTIVE | 2026-10-22 | https://docs.oracle.com/en/cloud/saas/human-resources/fauam/index.html | — (retrieved at runtime/local index) | Copyright 2024; release staleness risk; cross-check 26D readiness. |
| DOC-013 | Absence Management 26D Feature Summary | https://docs.oracle.com/en/cloud/saas/readiness/hcm/26d/amg-26d/26D-absence-mgmt-wn-t78665.htm | ABS | 26D | Official Oracle feature-summary URL confirmed 2026-10-22 | A | ACTIVE | 2026-10-22 | https://docs.oracle.com/en/cloud/saas/readiness/hcm/26d/amg-26d/26D-absence-mgmt-wn-t78665.htm | — (retrieved at runtime/local index) | Read full feature detail, impact and action-to-enable; URL presence is not proof of tenant enablement. |
| DOC-014 | Implementing Benefits | G34710-01 | BEN | Rolling guide; validate target release | Title, part and 468-page PDF confirmed 2026-10-22 | A | ACTIVE | 2026-10-22 | https://docs.oracle.com/en/cloud/saas/human-resources/faibf/index.html | — (retrieved at runtime/local index) | Copyright 2025; target-release/tenant validation pending. |
| DOC-015 | Using Benefits | G34737-01 | BEN | Rolling guide; validate target release | Title, part and 150-page PDF confirmed 2026-10-22 | A | ACTIVE | 2026-10-22 | https://docs.oracle.com/en/cloud/saas/human-resources/facmb/index.html | — (retrieved at runtime/local index) | Copyright 2025; target-release/tenant validation pending. |
| DOC-016 | Benefits 26D What's New — Feature Detail | https://docs.oracle.com/en/cloud/saas/readiness/hcm/26d/benf-26d/26D-benefits-wn-f51263.htm | BEN | 26D | Official Oracle feature-detail URL confirmed 2026-10-22 | A | ACTIVE | 2026-10-22 | https://docs.oracle.com/en/cloud/saas/readiness/hcm/26d/benf-26d/26D-benefits-wn-f51263.htm | — (retrieved at runtime/local index) | Release-specific evidence; feature detail title and setup impacts must be reviewed. |
| DOC-017 | Implementing Time and Labor | G34726-01 | TIM | Rolling guide; validate target release | Title, part and 310-page PDF confirmed 2026-10-22 | A | ACTIVE | 2026-10-22 | https://docs.oracle.com/en/cloud/saas/human-resources/faitl/index.html | — (retrieved at runtime/local index) | Copyright 2025; target-release/tenant validation pending. |
| DOC-018 | Using Time and Labor | G34743-01 | TIM | Rolling guide; validate target release | Title, part and 54-page PDF confirmed 2026-10-22 | A | ACTIVE | 2026-10-22 | https://docs.oracle.com/en/cloud/saas/human-resources/fautl/index.html | — (retrieved at runtime/local index) | Copyright 2025; target-release/tenant validation pending. |
| DOC-019 | Time and Labor 26D What's New — Feature Detail | https://docs.oracle.com/en/cloud/saas/readiness/hcm/26d/tila-26d/26D-time-labor-wn-f51382.htm | TIM | 26D | Official Oracle feature-detail URL confirmed 2026-10-22 | A | ACTIVE | 2026-10-22 | https://docs.oracle.com/en/cloud/saas/readiness/hcm/26d/tila-26d/26D-time-labor-wn-f51382.htm | — (retrieved at runtime/local index) | Release-specific evidence; verify feature impacts and prerequisites. |
| DOC-020 | Implementing Learning | G34429-04 | LRN | Rolling guide; validate target release | Title, part and 44-page PDF confirmed 2026-10-22 | A | ACTIVE | 2026-10-22 | https://docs.oracle.com/en/cloud/saas/talent-management/faiml/index.html | — (retrieved at runtime/local index) | Copyright 2026; target-release/tenant validation pending. |
| DOC-021 | Using Learning | G34438-02 | LRN | Rolling guide; validate target release | Title, part and 100-page PDF confirmed 2026-10-22 | A | ACTIVE | 2026-10-22 | https://docs.oracle.com/en/cloud/saas/talent-management/fatul/index.html | — (retrieved at runtime/local index) | Copyright 2026; target-release/tenant validation pending. |
| DOC-022 | Learning and Development 26D What's New — Feature Detail | https://docs.oracle.com/en/cloud/saas/readiness/hcm/26d/lear-26d/26D-learning-wn-f50703.htm | LRN | 26D | Official Oracle feature-detail URL confirmed 2026-10-22 | A | ACTIVE | 2026-10-22 | https://docs.oracle.com/en/cloud/saas/readiness/hcm/26d/lear-26d/26D-learning-wn-f50703.htm | — (retrieved at runtime/local index) | Release-specific evidence; validate feature enablement and dependencies. |

**Initial populated module set: ORC, GHR, ABS, BEN, TIM, and LRN.** Official guides, release readiness sources, and catalog URLs are registered for six modules. The local full-text index is created at runtime in separate Git-ignored caches; the manuals and extracted guide text are not committed to this public repository. Functional validity still requires target-release and tenant validation.

## Coverage summary

| Candidate module | Tier A/B sources registered | Status |
| --- | ---: | --- |
| ORC — Recruiting | 6 | Source metadata registered; local ingest available; target-release validation pending. |
| GHR — Global Human Resources | 4 | Sources registered; current and 2025 guides; tenant validation pending. |
| ABS — Absence Management | 4 | Sources registered; core guides show 2024 copyright dates and need strong current-release cross-check. |
| BEN — Benefits | 4 | Sources registered; 2025 guides; tenant/plan validation pending. |
| TIM — Time and Labor | 4 | Sources registered; 2025 guides; calculation-rule and tenant validation pending. |
| LRN — Learning | 4 | Sources registered; 2026 guides; tenant/content-provider validation pending. |
| Other HCM modules | 0 registered here | Populate from actual Oracle catalogs; scope remains TBC under GAP-002. |

Counts include each module's source guides, current release evidence, and the shared Oracle catalog. They do not imply a completed source ingest or production validation. The release-discovery patterns are checked against Oracle's central readiness page; not all candidate quarterly releases necessarily exist yet.

A module with zero verified source entries and confirmed in-scope status must raise a `MISSING` gap at intake.

## Retirement

Sources are retired, never deleted — a retired entry is the only way to explain a
decision that was correct when it was made. Set `Status: RETIRED`, keep the row,
and record in Notes what replaced it and which ADRs were re-opened.
