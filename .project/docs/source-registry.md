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

**The registry is empty.** No Oracle documentation has been supplied to this
project. See `GAP-001` in [`gaps.md`](gaps.md); intake is tracked as `HCM-010`.

## Coverage summary

| In-scope module | Tier A/B sources | Status |
| --- | --- | --- |
| _(unknown — module scope not yet confirmed, `GAP-002`)_ | 0 | Blocked on `HCM-011` |

Coverage cannot be assessed until the in-scope module list is confirmed. Once it
is, every in-scope module with zero Tier A/B sources raises a `MISSING` gap
automatically at intake.

## Retirement

Sources are retired, never deleted — a retired entry is the only way to explain a
decision that was correct when it was made. Set `Status: RETIRED`, keep the row,
and record in Notes what replaced it and which ADRs were re-opened.
