# Oracle Benefits — domain map

**Scope:** source-grounded starting index, not a replacement for the official guides.  
**Validated source baseline:** 2026-10-22.  
**Main setup guide:** [Implementing Benefits](https://docs.oracle.com/en/cloud/saas/human-resources/faibf/index.html)  
**Main operational guide:** [Using Benefits](https://docs.oracle.com/en/cloud/saas/human-resources/facmb/index.html)  
**26D readiness:** [undefined](https://docs.oracle.com/en/cloud/saas/readiness/hcm/26d/benf-26d/26D-benefits-wn-f51263.htm)  
**Source manifest:** [source-manifest.json](source-manifest.json)

## Topic map

- Implementation task sequence and responsive user experience setup
- Benefits relationships, lookups, regulations and reporting groups
- Eligibility profiles, derived factors, life events and enrollment opportunities
- Programs, plans, options, hierarchies, enrollment criteria and validation
- Dependents, beneficiary designations, certifications, action items and documents
- Rate profiles, benefit coverages, flex credits, billing and selling time off
- Benefits extracts, configuration imports/exports, integrated workbooks, formulas and diagnostics
- Participant and administrator enrollment workflows, Benefits Service Center and processing

## Retrieval and response protocol

1. Confirm the customer's actual release and functional area.
2. For new-feature or upgrade questions, retrieve the feature row from the 26D (or actual current release) readiness pages first and read the impact/action-to-enable notes.
3. Search the Implementing guide for the setup object, prerequisite, profile option, lookup, formula, scheduled process, privilege or migration step.
4. Search the Using guide for the corresponding operating workflow and expected results.
5. Retrieve adjacent prerequisites, notes, examples, and error-handling guidance before proposing a change.
6. Cite the precise guide chapter and PDF page or official HTML chapter URL. Never cite this map as proof of a detailed UI path.

## Source-age and tenant-specific caution

Eligibility, plan coverage, effective dates, legislation and relationship configuration drive the outcome. The guide is not a substitute for confirming a specific plan's actual configuration or applicable country rules.

Do not assume a documented option is enabled in a given tenant. Where the answer depends on configuration, role assignment, country/legal employer, subscription, opt-in, data, or an Oracle Support defect, explicitly identify what must be confirmed.
