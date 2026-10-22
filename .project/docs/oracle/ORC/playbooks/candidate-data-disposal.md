# Candidate search archiving and data disposal

**Source:** DOC-001, *Implementing Recruiting*, Chapter 31, printed pp. 379–384 / physical PDF pp. 397–402. [Official guide](https://docs.oracle.com/en/cloud/saas/talent-management/faimh/implementing-recruiting.pdf). This is a technical pathway, not a legal retention schedule.

## Do not conflate the three controls

| Control | Purpose and follow-up |
|---|---|
| Candidate Search Archiving | Records who searched, criteria, date/time, result candidates, and actions taken. The guide gives two-year query retention and a maximum of 500 candidates per query. Run **Convert Candidate Search Logs for Reporting Purposes** before relying on the Recruiting Real Time reporting data. |
| Remove Person Information | Removes/masks configured person data under a defined policy. The candidate must first be deleted in Recruiting; the source describes that delete as a soft delete. |
| Recruiting campaign metrics purging | Retention setting for campaign email metrics. The guide gives a 180-day default and a 1,000-day maximum; run **Purge Processed Internal Recruiting Data** after setting the duration. |

## Candidate data removal sequence

1. Confirm retention/disposal intent with the relevant privacy and records owners.
2. In My Client Groups > Data Exchange, configure a Person Information Removal Policy and explicitly review business objects, components, and rules.
3. Enable the policy only after rules for deletion versus masking are reviewed.
4. Soft-delete the candidate in Recruiting first.
5. In **Remove Person Information**, choose the policy, identify candidate numbers, choose Remove or Report mode as appropriate, and submit.
6. Review process status, mode, errors, and the results before closing the audit trail.

The guide names `HRC_CONFIGURE_PERSON_INFO_REMOVAL_POLICIES_PRIV` and `ORA_HRC_REMOVE_PERSON_INFORMATION` for the relevant actions.

Test in a controlled non-production environment. The guide discusses distinct treatment for external candidates versus ex-employees/ex-contingent workers; policy choices must be aligned with business and legal obligations, not copied as universal defaults.
