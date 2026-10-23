# Agency Portal Access and Candidate Data Minimization

**Source:** DOC-001, *Implementing Recruiting*, Chapter 19, printed pp. 261–266 / physical PDF pp. 279–284. [Official PDF](https://docs.oracle.com/en/cloud/saas/talent-management/faimh/implementing-recruiting.pdf).

## Control candidate-profile visibility

The guide describes **Hide Candidate Data** under Enterprise Recruiting and Candidate Experience Information > **Agency Hiring**. When enabled, agency agents can see only the candidate profile's **Attachments** tab; when disabled, they see **Details** and **Attachments**. The source also distinguishes initial candidate creation from later access: the create action exposes fields for complete candidate entry, while an existing profile shows only the sections exposed to agents.

## Internal-candidate search is a two-part switch

To allow agencies to search internal candidates by email address, the guide requires both:

1. **Enterprise Recruiting and Candidate Experience Information > Agency Hiring > Allow Internal Candidate Search**.
2. The specific agency's **Recruiting Agencies > Basic Information > Allow Internal Candidate Search** setting under the Source Candidates functional area.

Enabling only one control doesn't complete the documented setup.

## Scheduled processes for agency hiring

- **Import User and Role Application Security Data:** one-time run when a new role is delivered in a release, as described by the source.
- **Retrieve Latest LDAP Changes:** run when each new agent is created and schedule to run frequently.
- **Send Requisition Posting Expiration Date Notification:** run daily to notify agents of requisition posting expiration dates.

## Regression cases

Test Hide Candidate Data on/off, create versus reopen existing candidate, the global and individual-agency internal-search settings individually and together, new agent plus LDAP refresh, and daily expiration notifications. Verify the actual candidate fields visible to an agent rather than inferring behavior from the switch label.

Source: Chapter 19, printed pp. 261–266 / PDF pp. 279–284.
