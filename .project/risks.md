# Risk Register

Risks are about probability and impact. Assumptions (`ASM-###`, in
[`docs/gaps.md`](docs/gaps.md)) are about evidence. They are tracked separately
and cross-referenced — see `ADR-0005`.

Scoring: probability and impact each `L`/`M`/`H`. Exposure is the pair.
Review: every sprint retrospective.

| ID | Risk | Prob | Impact | Exposure | Response | Owner | Linked |
| --- | --- | --- | --- | --- | --- | --- | --- |
| RISK-001 | Oracle documentation is not supplied, or is supplied incomplete, leaving design decisions unsourced | H | H | **High** | Mitigate — intake card `HCM-010` prioritised rank 1; every uncovered module raises a `MISSING` gap at intake; escalate to sponsor if unresolved after one sprint | PO | `GAP-001` |
| RISK-002 | Scope is agreed informally and expands without re-planning | M | H | **High** | Mitigate — scope recorded in `HCM-011`; changes require a re-ranked backlog and a PO decision on the card | PO | `GAP-002` |
| RISK-003 | The decision framework is bypassed under delivery pressure, and undocumented configuration accumulates | M | H | **High** | Mitigate — Definition of Ready requires a source or a gap; `project_lint` enforces reference integrity; reviewers reject uncited design commits | SA | `ADR-0002` |
| RISK-004 | A quarterly Oracle update changes behaviour a design depends on | H | M | **High** | Mitigate — release binding in the registry; source currency sweep each release; ADRs citing changed sources return to `Under review` | DOC | `ASM-003`, `HCM-032` |
| RISK-005 | Production personal data reaches the repository via an extract, fixture, or screenshot | M | H | **High** | Prevent — `.gitignore` excludes extract outputs and `data/live/`; synthetic fixtures only (`HCM-027`); secret scanning in CI; treat any occurrence as an incident, not a cleanup | SA | `ADR-0003` |
| RISK-006 | Non-developer roles do not adopt git-based ways of working, so the board and specs drift from reality | M | M | Medium | Mitigate — templates for every artifact; board update is in the Definition of Done; provide support rather than assuming familiarity | PO | `ADR-0003` |
| RISK-007 | Assumptions are renewed indefinitely instead of resolved, and inference hardens into assumed fact | M | H | **High** | Detect — build fails on expiry; retrospective tracks renewals versus resolutions as a metric | SA | `ADR-0005` |
| RISK-008 | The platform assumption is wrong (not Fusion Cloud HCM SaaS) | L | H | Medium | Detect early — `HCM-011` resolves it; rework confined to module index, `integrations/`, `data/` | PO | `ASM-001` |
| RISK-009 | Environment topology or refresh cadence cannot support parallel design, conversion, and testing | M | M | Medium | Mitigate — `HCM-012` and `HCM-025` establish topology and refresh strategy before conversion begins | SA | `GAP-004` |
| RISK-010 | Data conversion volume and quality are discovered late, compressing the cutover window | M | H | **High** | Mitigate — current-state inventory `HCM-014` ranks early; conversion strategy `HCM-023` mandates mock conversions with reconciliation | SA | `GAP-006` |
| RISK-011 | Extensions accumulate and become a quarterly-update regression burden | M | M | Medium | Mitigate — extension policy `HCM-030` requires an ADR per extension stating its maintenance cost | SA | `ADR-0005` |
| RISK-012 | Compliance or data residency obligations surface after integration and reporting design is fixed | M | H | **High** | Mitigate — `HCM-034` ranks before integration build; residency constraints captured in `HCM-014` | SA | `GAP-006` |

## Closed risks

_None._
