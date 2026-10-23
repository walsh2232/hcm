# Candidate Referral Flexfields

**Source:** DOC-001, *Implementing Recruiting*, Chapter 17, printed pp. 255–256 / physical PDF pp. 273–274. [Official guide](https://docs.oracle.com/en/cloud/saas/talent-management/faimh/implementing-recruiting.pdf).

## What the extension changes

The guide describes referral flexfields as an extension point for collecting extra referral information from employees, agency users, and recruiters. When configured, the source describes the information as visible in the prospect/application's **Referral Additional Info** section, the agency portal's **Referral Info** section when agents use **Submit with Additional Info**, and the employee referral flow under **Me > Current Jobs > Referrals**.

Recruiting users need **Update Referral Additional Information** (`IRC_UPDATE_REFERRAL_ADDITIONAL_INFORMATION`) to update referral additional information in a prospect or job application.

## Configure the flexfield contexts

1. In Setup and Maintenance, open Recruiting and Candidate Experience > Source Candidates > **Referral Descriptive Flexfields**.
2. Open Edit and select **Manage Contexts**.
3. Search Context Code for `%REFERRAL`.
4. The guide identifies two seeded contexts: **Agency Referral** and **Employee Referral**.
5. Edit the intended seeded context, create the context-sensitive segments, then save and close.
6. Preserve the guide's note: display type is set to Hidden on the Referral Descriptive Flexfields page, and the guide recommends not changing it.

## Make fields visible in TDS

Referral flexfields are hidden by default. The guide lists these actions as relevant to displaying them:

- **Recruiting - Refer an Employee**
- **Recruiting - Refer a Candidate**
- **Recruiting - Referred Candidates by Agency**
- **Recruiting - Submit Candidates by Agency**

For the employee example, activate a sandbox/page editing at Site layer, open My Client Groups > Quick Actions > HCM Experience Design Studio > Transaction Design Studio, select **Recruiting - Refer an Employee**, add the rule, specify the intended legal employer and recruiting type, make the **Referral Descriptive Flexfield** visible, configure individual fields if required, and save/close.

## Regression cases

Test Employee Referral and Agency Referral contexts separately; confirm each referral action exposes only intended fields; test role/portal view versus recruiter view; confirm the update privilege; and check values persist from referral to prospect/application in the intended sections. Treat sensitive/referral fields as data-design decisions and use the appropriate privacy review.
