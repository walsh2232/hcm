# Oracle Global Human Resources — domain map

**Scope:** source-grounded starting index, not a replacement for the official guides.  
**Validated source baseline:** 2026-10-22.  
**Main setup guide:** [Implementing Global Human Resources](https://docs.oracle.com/en/cloud/saas/human-resources/faigh/index.html)  
**Main operational guide:** [Using Global Human Resources](https://docs.oracle.com/en/cloud/saas/human-resources/fawhr/index.html)  
**26D readiness:** [undefined](https://docs.oracle.com/en/cloud/saas/readiness/hcm/26d/hure-26d/)  
**Source manifest:** [source-manifest.json](source-manifest.json)

## Topic map

- Enterprise structures: enterprise, legal entities, business units and reference data sets
- Divisions, departments, worker unions, organization trees and locations
- Jobs, positions, grades, grade rates and grade ladders
- Person and employment records, seniority dates, document records and workforce records
- User/role administration and related HCM security references
- Current release readiness, deployment-specific Redwood or country/localization dependencies

## Retrieval and response protocol

1. Confirm the customer's actual release and functional area.
2. For new-feature or upgrade questions, retrieve the feature row from the 26D (or actual current release) readiness pages first and read the impact/action-to-enable notes.
3. Search the Implementing guide for the setup object, prerequisite, profile option, lookup, formula, scheduled process, privilege or migration step.
4. Search the Using guide for the corresponding operating workflow and expected results.
5. Retrieve adjacent prerequisites, notes, examples, and error-handling guidance before proposing a change.
6. Cite the precise guide chapter and PDF page or official HTML chapter URL. Never cite this map as proof of a detailed UI path.

## Source-age and tenant-specific caution

The Using guide is copyrighted 2025 while Implementing is copyrighted 2026. Use the current release readiness content for changed behaviour and keep tenant-level security and enterprise-structure assumptions separate from generic documentation.

Do not assume a documented option is enabled in a given tenant. Where the answer depends on configuration, role assignment, country/legal employer, subscription, opt-in, data, or an Oracle Support defect, explicitly identify what must be confirmed.
