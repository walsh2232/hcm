# Recruiting Fast Formulas

**Source:** DOC-001, *Implementing Recruiting*, Chapter 30, printed pp. 371–378 / physical PDF pp. 389–396. [Official guide](https://docs.oracle.com/en/cloud/saas/talent-management/faimh/implementing-recruiting.pdf). This is a synthesized diagnostic aid; open the full source section before implementation.

## Choose by purpose

| Formula type | Use described by the guide |
|---|---|
| Recruiting Candidate Selection Process | CSP action conditions and move conditions |
| Recruiting Job Requisition | Conditions to automatically unpost requisitions |
| Recruiting Job Application Computed Field | Compute fields from data collected on an application |

Create formulas through the Setup and Maintenance work area using **Fast Formulas**.

## CSP return contract

- Set `CONDITION_RESULT`.
- The guide treats `Y`, `YES`, `TRUE`, and `1` as true (case-insensitive); another value is false.
- `CONDITION_MESSAGE` is optional, limited to 255 characters, and used for logging.
- Use only database items applicable to this formula type; the source points to MOS 2723251.1 for the complete Recruiting Fast Formula database-item list.

## Timing trap

When an application is moved, the guide says destination-phase/state actions execute before the application status is updated to the new phase/state. A formula on a destination action that reads the current phase/state may therefore observe the pre-move values.

## Test plan

Test true/false branches, default and missing data, unexpected values, action ordering, and destination-state conditions. Validate the formula's exact type and database items for the target release. Keep the formula and its condition attachment versioned with expected outcomes and regression tests.
