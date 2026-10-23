# Third-Party Partner Provisioning and Diagnostics

**Source:** DOC-001, *Implementing Recruiting*, Chapter 32 — Third Party Integration. See the [official PDF](https://docs.oracle.com/en/cloud/saas/talent-management/faimh/implementing-recruiting.pdf); supported partners and partner-specific fields can differ by service.

## Separate the stages

| Stage | What it proves | What it does not prove |
|---|---|---|
| Partner package imported | Setup data was imported successfully | Integration is fully configured or active |
| TEST config completed | Environment-specific integration values were entered | PROD credentials work |
| Provisioning files moved | Configuration was transported | Correct keys, account, and activation are complete |
| Integration activated | Configuration is enabled | Candidate event or downstream job succeeded |
| Scheduled process completed | Named job ran | Partner accepted the business payload unless logs/status prove it |

## Load a partner implementation package

The guide assigns this process to a user holding both **Application Implementation Administrator** (ORA_ASM_APPLICATION_IMPLEMENTATION_ADMIN_ABSTRACT) and **Recruiting Administrator** (ORA_PER_RECRUITING_ADMINISTRATOR_JOB).

1. Obtain the partner's implementation project ZIP.
2. In Setup and Maintenance, open **Manage Configuration Packages** and click **Upload**.
3. Select the partner ZIP, click **Get Details**, verify the selected project, click **Submit**, and confirm the warning.
4. Refresh until upload status is **Completed successfully**.
5. Select the completed upload row and choose **Import Setup Data**.
6. Refresh until import status is **Completed successfully**. Verify that the partner shows **Provisioned** in Recruiting Category Enablement and Recruiting Category Provisioning and Configuration.

## Provision the integration

1. In TEST, open Setup and Maintenance > Recruiting and Candidate Experience > Recruiting and Candidate Experience Management > **Recruiting Category Provisioning and Configuration**.
2. Edit the relevant partner integration, fill required fields from the service-specific field table in Chapter 32, and save. Do not copy credentials or fields across partner types.
3. Give the partner the user account it will use for synchronization. The guide requires separate accounts for TEST and PROD. Grant only service-specific privileges documented for that partner.
4. Export provisioning files from the tested environment, import them in the target environment, and verify client ID/secret fields, reference key, activation, and partner account. The enablement file must already be loaded when this isn't a configuration refresh.
5. Run the Recruiting processes relevant to the enabled service.

## Scheduled-process checks

The guide names **Perform Recruiting Candidate Selection Process Actions** and **Send Candidate Screening Requests to Partners** in the partner-provisioning sequence. Validate job status and partner response/error detail. Assessment and background-check services also depend on CSP actions that determine the phase/state where the service is triggered.

## Security and network boundary

The guide warns that Location-Based Access Control (LBAC) can block task/data or REST access from external IPs. If LBAC is active and a partner calls REST from outside allowed locations, a Public custom role may be required for the partner user. Confirm the actual policy and partner-specific required privileges before changing roles.

## Triage order

1. Confirm the partner and service are currently supported and in scope.
2. Check package-upload status and **Import Setup Data** status separately.
3. Verify partner-specific configuration fields and reference key.
4. Verify activation and the correct account/environment; TEST values do not prove PROD readiness.
5. Check exact scheduled process, logs, candidate/application state, and partner response.
6. Check service privileges, LBAC/public-role requirements, and external connectivity.
7. Escalate with process IDs/status, redacted logs, integration type, and source page. Don't share passwords, client secrets, candidate PII, or unredacted payloads.

**Source locations:** Partner Enablement/provisioning, printed pp. 387–391 / PDF pp. 405–409; additional field tables and integration-specific procedures continue through Chapter 32.
