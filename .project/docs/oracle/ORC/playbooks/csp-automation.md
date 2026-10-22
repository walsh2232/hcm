# CSP automation

Synthesized from DOC-001, Chapter 4; see the [source dossier](../DOC-001.md) and official [Implementing Recruiting PDF](https://docs.oracle.com/en/cloud/saas/talent-management/faimh/implementing-recruiting.pdf).

- Decide between Standard and Pipeline CSP before configuring. Oracle's guide describes Pipeline CSPs as excluding Offer and HR phases.
- Offer and HR are required phases; HR must be last. A custom phase between Offer and HR changes built-in progression from Offer — Accepted and therefore needs an explicitly designed manual or automatic route.
- Create/select the CSP under Setup and Maintenance > Recruiting and Candidate Experience > Candidate Job Applications > Candidate Selection Process Configuration.
- Use state actions for state-entry behavior and phase events for event-driven behavior during a phase.
- Multiple conditions on an action are conjunctive: all must be met.
- Order matters: if a Move or Move to HR action succeeds, later actions on the same event/state won't run after the application moves. Put dependent action/notification before the move or on a suitable destination state.
- Certain initial-state actions for external candidates can be queued until **Perform Recruiting Candidate Selection Process Actions** runs; the guide specifies exceptions for Move and Move to HR.
- Conditions marked "in error" refer to partner-returned errors, not generic configuration errors.

## Test before promotion

Test normal state entry, conditions unmet/met later, multiple action ordering, external candidate initial processing, partner failure status, and Offer-Accepted to HR progression. Inspect progress history, status, and any relevant scheduled-process output.

Page references: CSP creation PDF pp. 140–144 / printed pp. 122–126; automation/move behavior PDF pp. 145–148 / printed pp. 127–130. Do not treat this summary as a substitute for the full section.
