# Oracle Absence Management — domain map

**Scope:** source-grounded starting index, not a replacement for the official guides.  
**Validated source baseline:** 2026-10-22.  
**Main setup guide:** [Implementing Absence Management](https://docs.oracle.com/en/cloud/saas/human-resources/faiam/index.html)  
**Main operational guide:** [Using Absence Management](https://docs.oracle.com/en/cloud/saas/human-resources/fauam/index.html)  
**26D readiness:** [undefined](https://docs.oracle.com/en/cloud/saas/readiness/hcm/26d/amg-26d/26D-absence-mgmt-wn-t78665.htm)  
**Source manifest:** [source-manifest.json](source-manifest.json)

## Topic map

- Implementation order and Absence integrations
- Responsive experience setup; lookups, value sets, flexfields and deep links
- Fast Formula use, compilation/runtime error handling and formula-specific rules
- Eligibility profiles, derived factors and rate definitions for absence payments
- Elements, effective dates, accrual and qualification plans
- Absence types, reasons, categories, certifications and approval/processing rules
- Worker and manager absence entry, balances, maintenance, troubleshooting and recurring processes

## Retrieval and response protocol

1. Confirm the customer's actual release and functional area.
2. For new-feature or upgrade questions, retrieve the feature row from the 26D (or actual current release) readiness pages first and read the impact/action-to-enable notes.
3. Search the Implementing guide for the setup object, prerequisite, profile option, lookup, formula, scheduled process, privilege or migration step.
4. Search the Using guide for the corresponding operating workflow and expected results.
5. Retrieve adjacent prerequisites, notes, examples, and error-handling guidance before proposing a change.
6. Cite the precise guide chapter and PDF page or official HTML chapter URL. Never cite this map as proof of a detailed UI path.

## Source-age and tenant-specific caution

The two core manuals currently show 2024 copyright dates. Treat them as implementation/operating references, not proof that a procedure is unchanged in 26D. Validate release-dependent behaviour against the current readiness pages.

Do not assume a documented option is enabled in a given tenant. Where the answer depends on configuration, role assignment, country/legal employer, subscription, opt-in, data, or an Oracle Support defect, explicitly identify what must be confirmed.
