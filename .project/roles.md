# Role Charters, Decision Rights & Escalation

Six roles operate with authority in their own domain and coordinate through the
board, ADRs, and the documentation registry. Roles are *functions*, not
headcount — one person may hold several, but the decision rights still apply.

## Decision rights

Each role owns a class of decision outright. Owning a decision means: you decide,
you record it, and nobody re-opens it without new evidence or a superseding ADR.

| Role | Decides (owns) | Must consult | Cannot decide alone |
| --- | --- | --- | --- |
| **Product Owner / Manager** | Scope, priority, sequencing, release content, acceptance of Done, trade-offs between cost/date/scope | BA (impact), SA (feasibility) | Technical design, test sufficiency |
| **Business Analyst** | Requirement wording and acceptance criteria, process design, fit/gap classification, configuration intent | PO (priority), SA (feasibility) | Priority, technical pattern |
| **Solution Architect** | Integration patterns, extension vs. configuration, data model & conversion strategy, security architecture, environment/release strategy, non-functional targets | BA (intent), Dev (cost) | Scope, requirement meaning |
| **Developer** | Implementation approach within an agreed pattern, code structure, unit test design, technical debt calls inside a component | SA (pattern), QA (testability) | Deviating from an ADR'd pattern |
| **QA / Testing** | Test strategy, test case sufficiency, defect severity, pass/fail verdict, release readiness from a quality standpoint | BA (intent), PO (risk appetite) | Accepting a failing exit criterion |
| **Documentation Specialist** | Registry structure, source classification & tiering, doc currency, runbook standards, glossary | All roles | Whether a source is *technically* correct |

**Nobody may overrule the Documentation Specialist on whether a source is
registered and current, and nobody may overrule QA on a pass/fail verdict.**
Both can be escalated (below), but not silently ignored.

## RACI by activity

`R` responsible · `A` accountable · `C` consulted · `I` informed

| Activity | PO | BA | SA | Dev | QA | Doc |
| --- | --- | --- | --- | --- | --- | --- |
| Documentation intake & registration | I | C | C | I | I | **A/R** |
| Gap identification | C | R | R | C | C | **A** |
| Requirement definition | A | **R** | C | I | C | I |
| Fit/gap analysis | A | **R** | R | C | I | I |
| Solution design / ADR | I | C | **A/R** | C | C | C |
| Configuration & build | I | C | C | **A/R** | C | I |
| Integration design | I | C | **A/R** | R | C | I |
| Security role design | C | C | **A** | R | C | I |
| Test strategy & cases | I | C | C | C | **A/R** | I |
| Defect triage | A | C | C | R | **R** | I |
| Data conversion | C | R | **A** | R | C | I |
| Cutover & hypercare runbooks | A | C | R | R | C | **R** |
| Release acceptance | **A** | C | C | I | R | I |

## How decisions are communicated

There is one channel per decision class. Decisions made anywhere else are not
decisions.

| Decision class | Recorded as | Where |
| --- | --- | --- |
| Architectural / pattern / irreversible | **ADR** | `.project/adr/ADR-####-*.md` |
| Scope, priority, sequencing | Backlog rank + card note | `.project/backlog.md` |
| Requirement meaning / acceptance | Spec + acceptance criteria | module spec, `templates/spec.md` |
| Interpretation of an Oracle source | Registry annotation | `.project/docs/source-registry.md` |
| Working assumption pending evidence | `ASM-###` with owner + expiry | `.project/docs/gaps.md` |
| Quality verdict | Test result + defect | `tests/` |
| Anything discussed and *not* decided | Open question on the card | card `## Open questions` |

A role announcing a decision states, in one line: **what** was decided, **which
source** supports it (`DOC-###` / `NONE (GAP-###)`), **what it affects**, and
**who must act**. That line is the commit body, the PR summary, or the ADR
`Decision` section — not a separate message.

## Escalation

1. **Peer** — the two role owners resolve it, and the outcome is recorded in the
   owning artifact.
2. **Architect + PO** — technical feasibility vs. business need. Recorded as an ADR
   with the trade-off stated explicitly.
3. **Steering / sponsor** — cost, date, or scope change; compliance conflict; or a
   conflict between an Oracle source and a business requirement that cannot be
   configured away.

An escalation must always carry: the conflicting positions, the evidence for each
(`DOC-###`), the options, and a recommendation. Never escalate an open question
without a recommendation attached.

## Standing rule on sources

No role may assert an Oracle Fusion HCM behaviour as fact without a registered
source. "I have seen this in other implementations" is a *hypothesis* — it opens
a `GAP-###`, it does not close one.
