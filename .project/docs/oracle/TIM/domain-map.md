# Oracle Time and Labor — domain map

**Scope:** source-grounded starting index, not a replacement for the official guides.  
**Validated source baseline:** 2026-10-22.  
**Main setup guide:** [Implementing Time and Labor](https://docs.oracle.com/en/cloud/saas/human-resources/faitl/index.html)  
**Main operational guide:** [Using Time and Labor](https://docs.oracle.com/en/cloud/saas/human-resources/fautl/index.html)  
**26D readiness:** [undefined](https://docs.oracle.com/en/cloud/saas/readiness/hcm/26d/tila-26d/26D-time-labor-wn-f51382.htm)  
**Source manifest:** [source-manifest.json](source-manifest.json)

## Topic map

- Setup/maintenance task sequence, profile options and workforce management lookups
- Time entry layouts, categories, layout sets, custom time attributes and data sources
- Absence, payroll and project-costing time attributes and units of measure
- Time processing rules, templates, formulas and exception handling
- Time-card reporting, approvals, calculation and transfer into downstream processes
- Worker, manager and administrator time-management workflows
- Scheduling objects, time collection devices/events, integrations and release regression

## Retrieval and response protocol

1. Confirm the customer's actual release and functional area.
2. For new-feature or upgrade questions, retrieve the feature row from the 26D (or actual current release) readiness pages first and read the impact/action-to-enable notes.
3. Search the Implementing guide for the setup object, prerequisite, profile option, lookup, formula, scheduled process, privilege or migration step.
4. Search the Using guide for the corresponding operating workflow and expected results.
5. Retrieve adjacent prerequisites, notes, examples, and error-handling guidance before proposing a change.
6. Cite the precise guide chapter and PDF page or official HTML chapter URL. Never cite this map as proof of a detailed UI path.

## Source-age and tenant-specific caution

Time results depend on the applicable worker, time-entry configuration, rule sets, approvals, date effectiveness and transfer/downstream configuration. Verify exact rules and process names in the indexed guide before acting.

Do not assume a documented option is enabled in a given tenant. Where the answer depends on configuration, role assignment, country/legal employer, subscription, opt-in, data, or an Oracle Support defect, explicitly identify what must be confirmed.
