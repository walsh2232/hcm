# Transaction Design Studio Rule Context and Precedence

**Source:** DOC-001, *Implementing Recruiting*, Chapter 35, printed pp. 425–430 / physical PDF pp. 443–448. [Official guide](https://docs.oracle.com/en/cloud/saas/talent-management/faimh/implementing-recruiting.pdf).

## Choose the action before writing a rule

TDS actions are page/task-specific. Chapter 35 lists separate actions for creating a requisition, viewing/editing a non-draft requisition, creating/editing an offer, viewing an offer in the job application, viewing/managing an offer during HR, internal-candidate Apply, career-site requisition details, referral flows, interviews, and partner-specific extra fields. Select the action that owns the page being configured rather than assuming one generic Recruiting rule controls all pages.

## Context fields alter the scope

- **Recruiting type:** applies the rule only to requisitions, job applications, or offers with the matching recruiting type, depending on action.
- **Country:** for requisitions, the primary location or one of the other locations must be in the selected country; for offers, the guide describes country applicability through the legal employer.
- **Role:** when a role is selected, the rule applies to that role; when no role is selected, the guide says the rule applies to all roles.
- **Sections and attributes:** visibility and requiredness are separate controls in the rule design; setting a flexfield as required may limit later visibility configuration for that field.
- **Order:** the guide describes first-applicable rule precedence rather than merging the fields from every rule that might match.

## Source ambiguity — don't silently resolve

The visually inspected Chapter 35 source page states that only one rule can be active for an action at a time, while the same discussion describes several rules for an action, ordered by precedence, and explains behavior when users have multiple roles. Those statements appear to be in tension. This is recorded as SI-004 / GAP-009 in [Source Issues](../SOURCE-ISSUES.md).

Until current-release Oracle documentation or the target UI resolves that tension, don't base a design on an assumption about how many simultaneously active rules the tenant permits. Preserve the source statements, inspect the target TDS rule list, test in a non-production environment, and raise the ambiguity before implementing a multi-rule pattern.

## Regression cases

Test the correct action, recruiting type, country, role/no-role cases, users with more than one applicable role, rule order, hidden versus required fields, and flexfields. Record the actual target-release behavior with a screenshot or result and the source page.
