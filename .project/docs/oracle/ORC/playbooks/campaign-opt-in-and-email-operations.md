# Recruiting Campaign Opt-In and Email Operations

**Source:** DOC-001, *Implementing Recruiting*, Chapter 18, printed pp. 257–260 / physical PDF pp. 275–278. [Official PDF](https://docs.oracle.com/en/cloud/saas/talent-management/faimh/implementing-recruiting.pdf).

## Make campaign consent explicit

Create a **Campaign Opt In Statement** in the Recruiting Content Library, enter the statement text, and choose **Save and Activate**. In the job application flow, enable **Campaign Opt In** so the candidate may choose whether to receive recruitment marketing communications. The guide says candidates don't have to agree to proceed with their job application.

This is technical configuration guidance, not a complete legal/privacy analysis. Obtain the approved consent wording and withdrawal/retention requirements from the appropriate owner.

## Audience suppression settings

In Enterprise Recruiting and Candidate Experience Information > **Campaigns**, review:

- **Email Maximum Retry Count** (default 3 in this guide edition).
- **Don't send emails to candidates flagged as don't rehire**.
- **Don't send emails to audience members who already received emails in the last period** (guide options: 1 week, 2 weeks, or 1 month).
- **Exclude candidates who were included in a recent campaign** and **Recent campaign period**.

Confirm these controls against the target release and current business rules before campaign launch.

## Scheduled processes

The guide recommends scheduling each of the following every **30 minutes**:

- **Prepare Campaign Email**
- **Send Campaign Email**
- **Track Campaign Email Delivery**

Inspect all three stages separately. A successful preparation or send job alone doesn't prove all intended recipients received the campaign.

## HTML email templates

The guide names campaign purposes **Respond to Request**, **Refer Job**, and **Apply to Job**. Create an HTML template through **Manage HTML Email Templates**, select type **Campaign user email template**, choose the purpose and a Basic, Blank, or Multi-Column template, then customize/lock the template in the design editor as required.

## Regression cases

Test application submission with opt-in unchecked; statement link and active version; do-not-rehire and recent-email exclusions; correct purpose/template type; and preparation, send, retry, and delivery-tracking outcomes.

Source: Chapter 18, printed pp. 257–260 / PDF pp. 275–278.
