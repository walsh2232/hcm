---
id: PLAN-ORCH-001
title: Delivery plan, ownership and open decisions
artifact_type: delivery-plan-and-raci
status: PROPOSED
version: 1.0.0
owner_role: BA
accountable_role: PO
last_reviewed: 2026-10-27
related_work_item: HCM-036
---

# PLAN-001 — Delivery Plan, RACI and Open Decisions

## 1. Delivery approach

Deliver a vertical slice end-to-end before adding many guides. The critical risk is not whether a PDF can be downloaded; it is whether a changed or partially extracted guide can be misrepresented as complete/current. Demonstrate this through fixtures and failure-injection tests before enabling weekly publication.

Phases are ordered gates, not calendar promises. Estimates below are rough planning estimates and should be refined by the owning roles.

## 2. Phases and exit criteria

| Phase | Main work | Owner roles | Dependencies | Exit criteria | Status |
|---|---|---|---|---|---|
| P0 — Baseline and defect reconciliation | Re-run current tests, verify suspected HTML parser defect, fix parser and add regression coverage, reconcile documentation claims with current commit | DEV + QA; BA documents | Current code in scripts/oracle_docs and tests | Exact SHA has test and lint results; defects recorded and closed/accepted | PROPOSED |
| P1 — Contract and catalogue | Finalize guide catalogue, allowed-source scope, manifest schema and lifecycle states; seed Recruiting guide records | BA + DOC; PO approves scope | PRD/SRS/DATA review | Schema validates; first-wave catalogue agreed; no invented edition/tenant-release mapping | PROPOSED |
| P2 — Single-guide vertical slice | For a representative Recruiting guide: source discovery/check, fetch, convert, provenance, completeness check and reproducible output | DEV + DOC; QA validates | P0/P1 | Fixture-backed conversion; sampled source comparison; complete manifest and diagnostics | PROPOSED |
| P3 — Diff/archive lifecycle | Implement unchanged detection, edition/content diff, archive move, safe failure and PR body | DEV; QA independent tests | P2 | Lifecycle tests for unchanged, new edition, parser failure and network failure pass | PROPOSED |
| P4 — Reviewable CI and weekly schedule | Add default-branch workflow, least-privilege bot PR creation, weekly/manual triggers, reporting and recovery | DEV + QA; DOC operations | P0–P3 | Manual rehearsal and first scheduled run succeed; no direct default-branch write; operator report complete | PROPOSED |
| P5 — Module coverage expansion | Add official sources and guide records based on approved module scope; verify coverage table | DOC + PO; QA regression | P4 and scope confirmation | Every approved in-scope guide has current/archive state or explicit gap/error | PROPOSED |
| P6 — Optional semantic summaries | Evaluate model-assisted change explanation under source-grounded review | PO + BA + SA + QA | Stable deterministic pipeline | Proposal accepted separately; summaries attributed, linked to source, never replace diff or source | DEFERRED |
| P7 — Separate tenant-configuration evidence product | Use the guide library as reference input to a future evidence-backed configuration/answer validator | PO + SA + BA + DEV + QA | Separate PRD and security review | New scope approval, threat model and independent requirements | DEFERRED |

## 3. RACI

R = responsible for execution; A = accountable for outcome/decision; C = consulted; I = informed.

| Activity | PO | BA | SA | DEV | QA | DOC |
|---|---|---|---|---|---|---|
| Product scope, priority and acceptance | A | R | C | I | C | I |
| Requirement wording and traceability | A | R | C | C | C | C |
| Architecture and tool pattern | C | C | A | R | C | C |
| Catalogue, source registration and edition currency | I | C | C | C | I | A/R |
| Ingest/parser implementation | I | C | C | A/R | C | C |
| Test design and pass/fail | I | C | C | C | A/R | C |
| Archive/diff lifecycle | C | C | A | R | R | C |
| GitHub permissions and deployment | A for risk acceptance | I | C | R | C | I |
| Public content publication approval | A | C | C | I | C | R |
| Weekly operations and runbook | I | C | C | R | C | A/R |
| Fresh-model handoff/checkpoint review | A for product decisions | R | C | C | C | R |
| Release acceptance | A | C | C | I | R (quality verdict) | I |

The role system is defined in the existing project at .project/roles.md. ChatGPT may assist multiple roles but is not an independent reviewer of its own work; an assigned human role must perform the required independent review before the PR is accepted.

## 4. Responsibility by actor

- **Product Owner (user):** confirms the user problem, approves scope/priority, selects repository name and first-wave guides, confirms publication/organizational permission scope, appoints reviewers, and accepts/rejects releases.
- **ChatGPT / implementation agent:** reads current files first, drafts artifacts, performs repository operations when authorized, records paths/commits, checks requirements against evidence, runs available tests or states why they were not run, and updates this plan/status.
- **Developer:** fixes parser and workflow defects, implements adapters and lifecycle logic, and ensures tests reflect observed failures.
- **QA reviewer:** executes the exact regression suite, verifies requirements and negative cases, and owns pass/fail.
- **Documentation Specialist:** maintains source registry and edition metadata, verifies official source identities/currency, checks sampled conversion fidelity, and documents unresolved source gaps.
- **Solution Architect:** reviews repository boundary, security/permission design, lifecycle atomicity and future extensibility.

Named human assignees are not yet recorded. Do not invent personal owners.

## 5. Review gates and definition of done

A phase can close only when:
- required artifacts exist at their canonical paths;
- requirements have verification methods and traceability to tests;
- code/test results refer to the exact candidate commit;
- unresolved defects or source gaps are listed with owner and disposition;
- the runbook and model handoff describe actual behavior, not intended behavior;
- independent QA has recorded pass/fail;
- architecture decisions are recorded as ADRs when the existing workflow requires them;
- the Product Owner accepts scope/business outcome.

## 6. ChatGPT documentation checkpoint

After every two substantive turns, before a repository write or consequential decision, and before marking a milestone complete:
1. Compare the latest two substantive user/assistant work cycles with PRD-001, SRS-001, ARCH-001, DATA-001, STATUS-001, backlog and kanban.
2. Identify any new decision, new proposal, contradiction, implementation change, test result or unresolved point.
3. Update the canonical artifact and status register or explicitly state why no file change is justified.
4. Report the delta: accepted decision / still proposed / built / verified / blocked; exact files; next owner.
5. Never assume a decision was made solely because an assistant proposed it. The user has to decide where the role charter assigns the decision to the PO.

## 7. Open decisions

| ID | Decision/question | Owner | Current recommendation | Status |
|---|---|---|---|---|
| OPEN-ORCH-001 | Confirm the separate public repository boundary and name. | PO | Separate output library from the existing HCM implementation/tooling repository; proposed name oracle-hcm-reference-library. | PROPOSED |
| OPEN-ORCH-002 | Confirm the first-wave module/guide list. | PO + DOC | Start with the already registered Recruiting implementing guide as a vertical slice; do not infer whole-HCM coverage. | PROPOSED |
| OPEN-ORCH-003 | Confirm the intended expansion of “DEE” from the kickoff speech-to-text. | PO | Keep unresolved; do not silently interpret the acronym. The current package covers PRD, SRS, architecture, data contract, test strategy, runbook, delivery/RACI and ADR governance. | OPEN |
| OPEN-ORCH-004 | Select human independent QA and architecture reviewers. | PO | Name reviewers before acceptance of implementation PR. | OPEN |
| OPEN-ORCH-005 | Select completeness threshold for PDFs and HTML chains. | QA + DOC | Derive from representative guide measurements and visual spot-checks rather than inventing a universal percentage. | OPEN |
| OPEN-ORCH-006 | Define publication approval record and scope. | PO | Capture the supplied organizational permission scope before the first public automated content release; development and local testing can continue. | OPEN |
| OPEN-ORCH-007 | Confirm workflow bot/token policy and schedule. | DEV + PO | Use least-privilege GITHUB_TOKEN, scheduled plus manual dispatch, PR-only writes. | PROPOSED |

## 8. References

- Current work item HCM-036: .project/backlog.md and .project/kanban.md.
- Role decision rights/RACI: .project/roles.md.
- Definition of Ready/Done and transition rules: .project/workflow.md.
- Source rules: .project/decision-framework.md and .project/docs/README.md.
- Current source catalogue and unresolved intake gaps: .project/docs/source-registry.md and .project/docs/gaps.md.
- Existing code inventory and exact current-state findings: STATUS-001.
