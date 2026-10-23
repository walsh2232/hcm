# Oracle Search Indexing and P2T/T2T Refresh

**Source:** DOC-001, *Implementing Recruiting*, Chapter 1, “Maintaining Oracle Search for Oracle Recruiting” (PDF p. 31 / printed p. 13) and Chapter 13, “Enable Advanced Job Application Filters” (PDF p. 245 / printed p. 227). Use the [official PDF](https://docs.oracle.com/en/cloud/saas/talent-management/faimh/implementing-recruiting.pdf) before running jobs.

## Separate the scenarios

- **New provisioning:** use Chapter 1's initial sequential loads, then schedule the maintenance processes.
- **Ordinary quarterly upgrade:** Chapter 1 says there is no need to run or schedule any scheduled processes for Oracle Search as part of this specific guidance.
- **P2T/T2T environment refresh:** Chapter 1 says to cancel specified maintenance jobs, rerun the full sequence, and resume recurring jobs. This differs from an ordinary upgrade.

## P2T/T2T sequence in Chapter 1

1. Cancel **Maintain Candidates and Job Requisitions for Search** and **Index Candidate Attachments**.
2. Run these jobs once sequentially:
   - **Load and Index Master Geography Hierarchy** — no parameters.
   - **Load and Index Job Requisitions** — Drop and Recreate indexing mode.
   - **Load and Index Candidates** — Drop and Recreate Index indexing mode.
   - **Index Job Summary for Each Requisition** — Full mode.
3. Schedule these jobs to run every 15 minutes:
   - **Maintain Candidates and Job Requisitions for Search**.
   - **Index Candidate Attachments**.
   - **Index Job Summary for Each Requisition** — Incremental mode.

Chapter 1 describes the last job as required for Career Coach Search and Smart Search, and the requisition/candidate loads as supporting Standard Search and Smart Search. Verify applicable feature scope and job parameters for the target tenant before execution.

## Advanced job-application filters

Chapter 13 describes this separate setup:

1. Set site-level profile option ORA_IRC_JA_ORACLE_SEARCH_ENABLED to Y.
2. Enable attachment indexing through site-level ORA_FND_SEARCH_ATTACH_ENABLED; the source notes this option is not unique to Recruiting and may already be enabled.
3. In **Manage Global Search Configurations** > **Configure Attachment Search**, create the index row, enable File Search and Content Search, and set maximum file/content sizes according to the procedure.
4. Run **ESS job to create index definition and perform initial ingest to OSCS** for the feature's stated index.

## Do not silently harmonize the index names — GAP-008

Two visually checked source locations show different strings in different contexts:

| Context | Exact string shown in the guide | Location |
|---|---|---|
| Chapter 1: Oracle Search maintenance after P2T/T2T when advanced job-application filters are in use | **fa-hcm-job application** (contains a space) | PDF p. 31 / printed p. 13 |
| Chapter 13: Configure Attachment Search and reingest attachment-search index | **fa-hcm-jobapplication** (no space) | PDF p. 245 / printed p. 227 |

These contexts may require distinct index names, or the source may contain a naming inconsistency. The current evidence does not justify replacing either string or declaring them interchangeable. Inspect the relevant index in the target UI and consult current release-specific Oracle guidance/support before executing the affected reingest. See [Source Issues](../SOURCE-ISSUES.md).

## Validation checklist

- Confirm new provisioning versus ordinary upgrade versus P2T/T2T.
- Check current scheduled-process schedules before cancelling or restarting jobs.
- Confirm each sequential process completes successfully before starting the next.
- Verify advanced job-application filters and candidate attachment search scope.
- Resolve the index-name question with release-specific evidence before the affected reingest.
- Test candidate search, job/requisition search, application filters, attachment indexing, and Smart Search/Career Coach features actually used.
