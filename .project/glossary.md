# Glossary

Terms used in this repository. Oracle product terms are recorded here as the
project uses them; the authoritative definition is always the registered Oracle
source, and where this glossary and a Tier A source disagree, the source wins and
this file is corrected.

> Entries marked **(unsourced)** are working definitions pending a Tier A/B
> citation at documentation intake (`GAP-001`). They are usable for
> communication, and may not be cited in a design decision.

## Project terms

| Term | Meaning |
| --- | --- |
| **ADR** | Architecture Decision Record. A recorded decision with context, consequences, and sources. `ADR-0001` |
| **Assumption (`ASM-###`)** | A working belief with an owner, an expiry, and a stated cost of being wrong. Fails the build when expired. `ADR-0005` |
| **Definition of Done** | The conditions a card must meet to reach Done. `workflow.md` |
| **Definition of Ready** | The conditions a card must meet to be started. `workflow.md` |
| **Gap (`GAP-###`)** | A question the registered sources cannot answer. Typed `MISSING`/`SILENT`/`AMBIGUOUS`/`SCOPE`/`STALE`. |
| **Module code** | Three-letter key joining requirements, cards, directories, and sources. `docs/modules/README.md` |
| **Provisional** | An artifact in force but resting on an open assumption. |
| **Source (`DOC-###`)** | A registered document that may be cited. Unregistered material may not be. |
| **Source currency sweep** | Per-release re-validation of every registry entry. `decision-framework.md` §2 |
| **Tier (A–D)** | Source authority ranking with absolute precedence A > B > C > D. |
| **WIP limit** | The maximum cards allowed in a board state. `workflow.md` |

## Oracle HCM terms **(unsourced — pending intake)**

| Term | Working definition |
| --- | --- |
| **Fusion Cloud HCM** | Oracle's SaaS human capital management application suite. Assumed platform, `ASM-001`. |
| **HDL** | HCM Data Loader — the bulk data loading mechanism used for conversion and mass updates. |
| **HSDL** | HCM Spreadsheet Data Loader — spreadsheet-based loading for smaller volumes. |
| **HCM Extract** | The framework for defining and generating outbound data extracts. |
| **Fast Formula** | Oracle's rule/expression language used across payroll, absence, compensation, and benefits. |
| **OTBI** | Oracle Transactional Business Intelligence — ad-hoc analytics over transactional subject areas. |
| **BI Publisher** | Pixel-perfect and high-volume reporting, typically for statutory and document output. |
| **Redwood** | Oracle's current user experience; also the extension model associated with it. |
| **Visual Builder (VBS)** | The tooling used to extend and customise Redwood pages. |
| **Sandbox** | An isolated configuration workspace, published to make changes effective. |
| **Quarterly update** | Oracle's release cadence for Fusion Cloud applications. Assumed, `ASM-003`. |
| **Legal employer** | The legal entity that employs a worker; drives statutory and payroll behaviour. |
| **Business unit** | An organisational unit used to partition transactional data and security. |
| **Position management** | Managing employment through defined positions rather than jobs alone. |
| **Job / Grade** | Workforce structure objects describing the role and its level. |
| **Element** | A payroll object representing an earning, deduction, or information item. |
| **Balance** | A payroll accumulator over elements and time. |
| **Payroll flow** | An orchestrated sequence of payroll processes. |
| **Absence plan** | The rules governing accrual, entitlement, and consumption of absence. |
| **Duty / Job / Data / Abstract role** | The layers of the Oracle role-based security model. |
| **Area of responsibility** | An assignment mechanism used to scope certain responsibilities to a population. |
| **Approval rule (BPM)** | Workflow rules governing transaction approval routing. |

**Every definition in this section is provisional and must be replaced with, or
confirmed against, a Tier A source at intake.** Correcting them is part of
`HCM-010`.
