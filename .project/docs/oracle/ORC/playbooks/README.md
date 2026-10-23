# Recruiting implementation playbooks

These short pathways summarize *Implementing Recruiting* (DOC-001) and link back to precise chapter/page references. They are synthesized working aids, not Oracle-published instructions or proof of tenant-specific configuration.

| Playbook | Purpose | Source |
|---|---|---|
| [CSP automation](csp-automation.md) | State transitions, action ordering, conditions, delayed processing | DOC-001, Ch. 4 |
| [Offer approval and Move to HR](offer-move-to-hr.md) | Approval route selection, duplicate check, HR hand-off | DOC-001, Ch. 21 and Ch. 4 |
| [Recruiting security foundation](recruiting-security.md) | Data roles, security profiles, visibility diagnosis | DOC-001, Ch. 34; security companions |
| [Career site and application flows](career-site-flow-boundaries.md) | Career-site setup, request-information/apply flow boundaries, Express Apply | DOC-001, Ch. 2–3 |
| [Candidate search and duplicates](candidate-duplicates.md) | Candidate visibility, merges, Move-to-HR duplicate checks | DOC-001, Ch. 13, 21, 34 |
| [Fast Formulas](fast-formulas.md) | Formula-type selection, return contract, phase/state timing | DOC-001, Ch. 30 |
| [Candidate data disposal](candidate-data-disposal.md) | Candidate-search archiving, person-info removal, metrics purge | DOC-001, Ch. 31 |
| [Recruiting AI recommendations](recruiting-ai-recommendations.md) | AI Apps activation, profile options, data synchronization | DOC-001, Ch. 25 |
| [Job requisition rules and approvals](job-requisition-rules-and-approvals.md) | TDS section rules, flexfield approvals, approval hierarchy, auto-unpost | DOC-001, Ch. 9 |
| [Interview schedules and calendar integrations](interview-schedules-and-calendar-integrations.md) | Notification recipients, Microsoft 365, Teams/Zoom, access types | DOC-001, Ch. 11 |
| [Third-party partner provisioning](third-party-partner-provisioning.md) | Package import, environment-specific provisioning, partner jobs, LBAC | DOC-001, Ch. 32 |
| [Oracle Search indexing and P2T/T2T](oracle-search-indexing-and-p2t.md) | Provisioning vs upgrade vs environment refresh; conflicting index-name strings | DOC-001, Ch. 1 and Ch. 13; GAP-008 |
| [Notification templates and CSP delivery](notifications-and-csp-delivery.md) | Candidate/hiring-team templates, review alerts, UI vs REST notification behavior | DOC-001, Ch. 6, printed pp. 152–162 / PDF pp. 170–180 |
| [Prescreening scoring and versioning](prescreening-scoring-and-versioning.md) | Disqualification scores, question context, versions, prefill and update process | DOC-001, Ch. 10, printed pp. 197–202 / PDF pp. 215–220 |
| [Campaign opt-in and email operations](campaign-opt-in-and-email-operations.md) | Optional consent, campaign suppression, email templates and process cadence | DOC-001, Ch. 18, printed pp. 257–260 / PDF pp. 275–278 |
| [Agency portal access and privacy](agency-portal-access-and-privacy.md) | Candidate data visibility, internal search, agent security-data jobs | DOC-001, Ch. 19, printed pp. 261–266 / PDF pp. 279–284 |

## How to use these playbooks

Open the full guide section before implementation. Verify target quarterly release, feature entitlement, privileges, data security, local configuration, and test outcomes. Preserve Oracle names and source ambiguity. The differing Oracle Search index strings are recorded in [SOURCE-ISSUES.md](../SOURCE-ISSUES.md) and tracked as GAP-008; do not silently harmonize them.

| [TDS rule context and precedence](tds-rule-precedence-and-context.md) | Action scope, role/country/recruiting-type context, order, unresolved active-rule statement | DOC-001, Ch. 35, PDF pp. 443–448 / printed pp. 425–430; GAP-009 |
| [Offer-letter template versioning and languages](offer-letter-template-versioning-and-languages.md) | Current-version impacts, separate template items, XDOLOCALE, resolved-token e-signature | DOC-001, Ch. 20, PDF pp. 285–296 / printed pp. 267–278 |
| [Candidate referral flexfields](candidate-referral-flexfields.md) | Referral contexts, TDS actions, agency/employee referral visibility and privilege | DOC-001, Ch. 17, PDF pp. 273–274 / printed pp. 255–256 |
