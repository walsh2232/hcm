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
| DOC-006 | Oracle Talent Management - All Books | https://docs.oracle.com/en/cloud/saas/talent-management/books.html | ORC | n/a | Catalog checked 2026-10-22 | A | ACTIVE | 2026-10-22 | https://docs.oracle.com/en/cloud/saas/talent-management/books.html | — | Official guide inventory; no standalone Administering Recruiting book listed. |

**Initial populated module: ORC (Recruiting).** Six official source entries have been registered and the local retrieval engine is implemented. Full text is downloaded and indexed at runtime in a Git-ignored local cache; it is not committed to this public repository. Functional validity still needs to be checked against the customer's actual quarterly release and tenant configuration.

## Coverage summary

| In-scope or candidate module | Tier A/B sources | Status |
| --- | --- | --- |
| ORC — Recruiting (scope remains TBC under GAP-002) | 6 | Official source metadata registered; local ingest runs on demand. Target-release validation pending. |
| Other HCM modules | 0 registered here | Source inventory and module scope still need to be confirmed under GAP-002. |

Coverage cannot be assessed until the in-scope module list is confirmed. Once it
is, every in-scope module with zero Tier A/B sources raises a `MISSING` gap
automatically at intake.

## Retirement

Sources are retired, never deleted — a retired entry is the only way to explain a
decision that was correct when it was made. Set `Status: RETIRED`, keep the row,
and record in Notes what replaced it and which ADRs were re-opened.
