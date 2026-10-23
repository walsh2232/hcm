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
| DOC-001 | Oracle Fusion Cloud Talent Management — Implementing Recruiting | G34431-12 · https://docs.oracle.com/en/cloud/saas/talent-management/faimh/implementing-recruiting.pdf | ORC | Guide edition G34431-12; tenant quarterly release unconfirmed |  | A | ACTIVE | 2026-10-22 | Oracle Help Center; user-supplied PDF held locally, not committed | — (source dossier only; body corpus private/local) | SHA-256 f374da29dc88e5458046123cb262efc309f50c21b0d967bd46d87018212bb40f. 448 physical pages; local searchable corpus available separately. Official source; tenant-release currency not validated; source issues SI-001/GAP-008 and SI-004/GAP-009 are recorded in oracle/ORC/SOURCE-ISSUES.md. |
| DOC-002 | Oracle Fusion Cloud Talent Management — Using Recruiting | G34440-08 · https://docs.oracle.com/en/cloud/saas/talent-management/faush/using-recruiting.pdf | ORC | Guide edition G34440-08; tenant quarterly release unconfirmed |  | A | ACTIVE | 2026-10-22 | Oracle Help Center; online source, not archived locally | — | Official companion guide identified; a contents-level map is committed at oracle/ORC/using-recruiting-topic-map.md, but the body is not in the local retrieval corpus. Validate against the target tenant release before version-sensitive use. |
| DOC-003 | Oracle Fusion Cloud Talent Management — Using and Administering Recruiting Booster | G34425-04 · https://docs.oracle.com/en/cloud/saas/talent-management/faarb/using-and-administering-recruiting-booster.pdf | ORC | Guide edition G34425-04; tenant quarterly release unconfirmed |  | A | ACTIVE | 2026-10-22 | Oracle Help Center; online source, not archived locally | — | Relevant where Recruiting Booster is licensed/in scope; contents/page map committed at oracle/ORC/RECRUITING-BOOSTER-TOPIC-MAP.md; full body not extracted locally. |
| DOC-004 | Oracle Fusion Cloud HCM — Securing HCM | G34732-10 · https://docs.oracle.com/en/cloud/saas/human-resources/ochus/securing-hcm.pdf | ORC; SEC | Guide edition G34732-10; tenant quarterly release unconfirmed |  | A | ACTIVE | 2026-10-22 | Oracle Help Center; online source, not archived locally | — | Cross-module security implementation reference; recruiting-focused navigation map committed at oracle/ORC/SECURITY-NAVIGATION.md; full body not extracted locally. |
| DOC-005 | Oracle Fusion Cloud HCM — Security Reference for HCM | G34733-07 · https://docs.oracle.com/en/cloud/saas/human-resources/oawpm/security-reference-for-hcm.pdf | ORC; SEC | Guide edition G34733-07; tenant quarterly release unconfirmed |  | A | ACTIVE | 2026-10-22 | Oracle Help Center; online source, not archived locally | — | Role hierarchy, privileges, and data security reference; Recruiting role printed/physical page pointers committed at oracle/ORC/SECURITY-NAVIGATION.md; full body not extracted locally. |
| DOC-006 | REST API for Oracle Fusion Cloud HCM | https://docs.oracle.com/en/cloud/saas/human-resources/farws/index.html | ORC; INT | Live, versioned REST reference; target tenant/API version unconfirmed |  | A | ACTIVE | 2026-10-22 | Oracle Help Center; live versioned HTML, not archived locally | — | For API-level work, cite the specific resource and API version. Do not treat a general landing page as endpoint-level evidence. |

**Initial Recruiting intake is registered.** DOC-001 has been extracted into a private local corpus; DOC-002–DOC-006 are current official sources catalogued for follow-on intake, but their full content is not yet indexed locally. Project-wide coverage remains incomplete until the in-scope modules and target quarterly release are confirmed; see `GAP-001` and `GAP-002`.

## Coverage summary

| In-scope module | Tier A/B sources | Status |
| --- | --- | --- |
| ORC — Recruiting (scope TBC; `GAP-002`) | 6 official sources registered; one locally extracted | Source editions identified; tenant-release validation pending |
| Other modules (scope TBC; `GAP-002`) | 0 registered in this intake batch | Coverage cannot be assessed until scope is confirmed |

Coverage cannot be assessed until the in-scope module list is confirmed. Once it
is, every in-scope module with zero Tier A/B sources raises a `MISSING` gap
automatically at intake.

## Retirement

Sources are retired, never deleted — a retired entry is the only way to explain a
decision that was correct when it was made. Set `Status: RETIRED`, keep the row,
and record in Notes what replaced it and which ADRs were re-opened.
