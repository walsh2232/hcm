# Job Requisition Rules and Approval Routing

**Source:** DOC-001, *Implementing Recruiting*, Chapter 9 — Job Requisitions. Open the relevant source section in the [official PDF](https://docs.oracle.com/en/cloud/saas/talent-management/faimh/implementing-recruiting.pdf) before changing configuration.

## Separate the controls first

| Need | Source-owned mechanism | Source location |
|---|---|---|
| Let hiring managers enter full requisition details without Update Job Requisition | Site profile option IRC_REQ_ALLOW_RULE_CONFIG_CUSTOMIZATION_ENABLED | PDF p. 190; printed p. 172 |
| Control requisition section visibility/requiredness | Transaction Design Studio (TDS), action Recruiting - Create Job Requisition | PDF pp. 204–206; printed pp. 186–188 |
| Automatically unpost a requisition | TDS unpost fields and a Job Requisition Fast Formula | PDF pp. 207–208; printed pp. 189–190 |
| Use requisition flexfields in approval rules | Deploy DFF, then synchronize RequisitionApprovalHumanTask | PDF pp. 213–214; printed pp. 195–196 |
| Select management hierarchy for approval | Transaction Console > Approval Rules > Approve Job Requisition | PDF p. 214; printed p. 196 |
| Auto-approve position-request/duplicate-position requisitions | Requisition Creation Source equals ORA_POSITION | PDF p. 191; printed p. 173 |

## Configure full requisition entry for hiring managers

The guide describes enabling IRC_REQ_ALLOW_RULE_CONFIG_CUSTOMIZATION_ENABLED at the **Site** level with value **Y**. It allows users without IRC_UPDATE_JOB_REQUISITION to enter all requisition details during creation. It does not grant the update privilege itself. Test create, save, edit-draft, and submit behaviors separately.

## Configure required sections carefully

The guide's TDS flow uses **Show questionnaire page** to expose the Required/Not Required configuration for requisition sections. Set it to **Yes** to edit those settings, then return it to **No** as the guide recommends. The guide states that the questionnaire page currently isn't available during requisition creation regardless of this setting; leaving it at Yes could expose the page if support is added in a future release.

A required section is automatically visible. Marking a section Required can disable built-in visibility rules for that section. Explicitly design visibility rules by role and context, then test interactions with screening-service behavior.

## Use flexfields in approval rules

1. In Setup and Maintenance, open **Job Requisition Descriptive Flexfields**.
2. Create the required global segments and click **Save and Close**.
3. Click **Deploy Flexfield**.
4. Open Notifications > Show All > Worklist > Administration > Task Configuration.
5. Search for **RequisitionApprovalHumanTask**, edit it, then click **Start Synchronization** when prompted.
6. Reopen the task, select **Assignees**, and open the relevant task rule.

This is distinct from general requisition approval-rule editing in Transaction Console. Confirm the intended rule type before changing routing.

## Choose the approval hierarchy

The guide describes **Approval Chain Of** choices **Hiring Manager**, **Requester**, **Recruiter**, and **User**. For Hiring Manager or Recruiter, the assignment hierarchy can use primary assignment (the documented default) or current assignment. Validate the intended owner, multiple assignments, recruiter inclusion, and fallback cases in non-production.

## Regression checklist

- Hiring Manager with and without IRC_UPDATE_JOB_REQUISITION.
- Role-, recruiting-type-, and country-scoped TDS rules, including fallback when no role is selected.
- Required section not visited, required field missing, and normal submit.
- Screening Services visibility when the section is required versus controlled by built-in rules.
- Flexfield value in approval conditions before and after task synchronization.
- Position-created ORA_POSITION path versus ordinary requisition creation.
- Approval chain for employees with multiple assignments and a recruiter role.
- Automatic unpost formula true/false outcomes and intended internal/external career-site targets.
