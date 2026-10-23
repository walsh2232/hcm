# Recruiting Notification Templates and Delivery

**Source:** DOC-001, *Implementing Recruiting*, Chapter 6, printed pp. 152–162 / physical PDF pp. 170–180. [Official PDF](https://docs.oracle.com/en/cloud/saas/talent-management/faimh/implementing-recruiting.pdf).

## Keep the mechanisms distinct

| Mechanism | Configuration |
|---|---|
| Automated job application notification | Recruiting Content Library category **Automated Job Application Notification** plus CSP **Send Notification** action |
| Candidate email template | Recruiting Content Library categories for candidate job application, pool member, candidate profile, or prospect; launched via **Send Email** |
| Hiring-team notification | Define collaborator types first, then create **Hiring Team Notification** templates used by **Send Message to Team** |
| Review notification | CSP **Send Notification** action plus the recruiter/hiring-manager message in Alerts Composer |
| Unposted-requisition notification | Seeded Alerts Composer message selected according to whether internal/external postings remain active |

## Source-grounded setup points

- Automated job-application notifications can be triggered when an application enters/exits a phase or enters a state; the source describes a configurable delay in supported cases. Check the message in the job application's **Interactions** tab.
- Candidate template availability depends on the context from which **Send Email** was launched. The guide names **IRC_UPDATE_EMAIL_CREATED_FROM_TEMPLATE** for **Update Email Created from Template**.
- Define hiring-team collaborator types before templates. The source names lookup type **ORA_IRC_COLLABORATOR_RESP_TYPE**; it warns against disabling the seeded **Collaborator** lookup because existing hiring teams may use it.
- Review notification message names in the source include **IRC_JobApp_Review_HM** and **IRC_JobApp_Review_Recruiter**.
- **Important action interaction:** the guide states **Send Notification** isn't working when **Move** is defined for the same state. Don't assume both actions execute.
- The guide says notifications are sent for events done in the UI; it does not promise the same notification behavior for REST-triggered events.
- For an unposted requisition, use the template matching the remaining internal/external posting state. Do not assume all unpost scenarios share one notification.

## Regression cases

Test external-only, internal-only, and dual postings; candidate language; phase/state action trigger; delayed notification; review notification with/without a Move action in the same state; candidate template availability across application/prospect/pool contexts; and custom collaborator recipient tokens.

Source: Chapter 6, printed pp. 152–162 / PDF pp. 170–180.
