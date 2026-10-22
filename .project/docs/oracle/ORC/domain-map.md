# Oracle Recruiting domain map

Evidence baseline: current official Recruiting guide indexes and 26D readiness page checked 2026-10-22.

## Implementing Recruiting (G34431-12)

The implementation guide contains the following chapter areas. This is navigation guidance; retrieve the exact chapter for steps.

| Chapter | Topic | Typical query |
|---:|---|---|
| 1 | Overview of Recruiting | Offerings, prerequisites, setup tasks, search |
| 2 | Career Sites | Site configuration, themes, assets, layout, search, SEO, cookies |
| 3 | Job Application Flows | Candidate flow blocks and behaviour |
| 4 | Candidate Selection Processes | Phases, states and move rules |
| 5 | Recruiting Content Library | Reusable content |
| 6 | Notifications | Notification configuration |
| 7 | Candidate Messaging | Messaging setup |
| 8 | Job Requisition Templates | Template configuration |
| 9 | Job Requisitions | Requisition configuration |
| 10 | Prescreening Questionnaires and Questions | Questionnaire setup |
| 11 | Candidate Interviews | Interview setup |
| 12 | Interview Feedback Questionnaires and Questions | Feedback setup |
| 13 | Candidates and Candidate Job Applications | Candidate/application records |
| 14 | Candidate Pools | Pool setup |
| 15 | Talent Community | Talent community configuration |
| 16 | Candidate Sources | Source configuration |
| 17 | Candidate Referrals | Referral setup |
| 18 | Recruiting Campaigns | Campaign setup |
| 19 | Recruiting Agencies | Agency configuration |
| 20 | Job Offer Letter Templates | Offer letter template setup |
| 21 | Job Offers | Offer configuration |
| 22 | Grid Views | Grid experience |
| 23 | Recruiting Activity Center | Activity Center |
| 24 | Recruiting Features Configuration Report | Feature setup verification |
| 25 | Oracle AI Apps in Recruiting | AI feature prerequisites |
| 26 | Dynamic Skills in Recruiting | Skills dependencies |
| 27 | Opportunity Marketplace | Cross-product setup/boundary |
| 28 | Lookups | Lookup setup |
| 29 | Geography Hierarchies | Geography configuration |
| 30 | Fast Formulas for Recruiting | Recruiting formula rules |
| 31 | Candidate Data Archiving and Disposal | Retention and lifecycle |
| 32 | Third Party Integration | Integration setup |
| 33 | Scheduled Processes for Recruiting | Background process inventory |
| 34 | Security for Recruiting | Role/privilege requirements |
| 35 | Personalization Using Transaction Design Studio | Transaction Design Studio |

Source: [Implementing Recruiting guide index](https://docs.oracle.com/en/cloud/saas/talent-management/faimh/index.html).

## Using Recruiting (G34440-08)
The guide covers requisition creation and states; posting and sourcing; prescreening questionnaires; screening services; candidate search; prospects/candidates; applications; candidate pools and talent community; campaigns; agencies; selection processes; interviews; offers; grid views; notifications/interactions; candidate messaging; Recruiting Activity Center; Opportunity Marketplace and candidate job search.

Source: [Using Recruiting index](https://docs.oracle.com/en/cloud/saas/talent-management/faush/index.html). Prefer it for operational workflows and expected user-visible behaviour; use the implementing guide for setup.

## Using and Administering Recruiting Booster (G34425-04)
This separate guide covers hiring events, interviews and interview coordination, two-way candidate messaging, Recruiting Assistant, Booster opt-in, setup/maintenance tasks, scheduled processes, and configuration for events/interviews/messaging/assistant.

Source: [Recruiting Booster guide index](https://docs.oracle.com/en/cloud/saas/talent-management/faarb/index.html).

## Recruiting 26D
Primary source: [Recruiting 26D What's New](https://docs.oracle.com/en/cloud/saas/readiness/hcm/26d/recr-26d/), document G61079-03. The [feature summary](https://docs.oracle.com/en/cloud/saas/readiness/hcm/26d/recr-26d/26D-recruiting-wn-t78659.htm) categorises features by impact and setup action.

Examples verified against official feature details:
- Customize and Improve the Candidate Application Experience: enhancements to flow background styling, visual consistency, spacing/typography, validation styling, keyboard focus, and responsive navigation across candidate-facing pages. [Feature details](https://docs.oracle.com/en/cloud/saas/readiness/hcm/26d/recr-26d/26D-recruiting-wn-f50318.htm).
- Configure Targeted Job Alerts for Candidates: supported saved alerts from search/profile/talent-community routes, per-alert email notifications and unsubscribe. [Feature details](https://docs.oracle.com/en/cloud/saas/readiness/hcm/26d/recr-26d/26D-recruiting-wn-f50317.htm).

These examples do not imply tenant enablement. Retrieve the full current feature row/detail, opt-in and setup action before advising.

## Cross-cutting dependency prompts
- Security: exact aggregate/duty privileges, job roles and data roles; cite the relevant chapter and official HCM security guide.
- Candidate experience: distinguish Redwood/classic and confirm tenant release, feature flag, profile option or setup path.
- Integrations: verify supported contract, authentication, timing, error handling and supported API/interface rather than inferring an endpoint.
- Data lifecycle: confirm candidate retention/archiving/disposal rules and tenant/legal policy.
- Quarterly updates: assess changes affecting candidate flows, career sites, selection, offers, messaging, interviews, integrations and security.
- Support defects: if official public docs cannot explain observed tenant behaviour, gather reproducible facts and consult authorized Oracle Support.

## Retrieval sequence
1. Open the current release's What's New/readiness page for release-sensitive questions.
2. Search the implementing guide for setup tasks, privileges, profile options and scheduled processes.
3. Search the using guide for workflow/state transitions and expected user-visible behaviour.
4. Search the Booster guide for Booster capabilities.
5. Retrieve adjacent prerequisites/notes and cite the exact page or chapter.
