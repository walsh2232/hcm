# Oracle Learning — domain map

**Scope:** source-grounded starting index, not a replacement for the official guides.  
**Validated source baseline:** 2026-10-22.  
**Main setup guide:** [Implementing Learning](https://docs.oracle.com/en/cloud/saas/talent-management/faiml/index.html)  
**Main operational guide:** [Using Learning](https://docs.oracle.com/en/cloud/saas/talent-management/fatul/index.html)  
**26D readiness:** [undefined](https://docs.oracle.com/en/cloud/saas/readiness/hcm/26d/lear-26d/26D-learning-wn-f50703.htm)  
**Source manifest:** [source-manifest.json](source-manifest.json)

## Topic map

- Learning items, courses, offerings, activities, specializations and learning communities
- Prerequisite, related and outcome skills/qualifications; questionnaires and evaluations
- Learner access and enrollment defaults, overrides, static/dynamic learner sets and assignments
- Profile options, lookups, descriptive flexfields, approval rules and notification tasks
- Background processes, completion certificates, external content providers and virtual classrooms
- Alerts, deep links, mobile behaviour, classroom locations and supported REST/service access
- Operational learner/administrator workflows and current 26D release-specific changes

## Retrieval and response protocol

1. Confirm the customer's actual release and functional area.
2. For new-feature or upgrade questions, retrieve the feature row from the 26D (or actual current release) readiness pages first and read the impact/action-to-enable notes.
3. Search the Implementing guide for the setup object, prerequisite, profile option, lookup, formula, scheduled process, privilege or migration step.
4. Search the Using guide for the corresponding operating workflow and expected results.
5. Retrieve adjacent prerequisites, notes, examples, and error-handling guidance before proposing a change.
6. Cite the precise guide chapter and PDF page or official HTML chapter URL. Never cite this map as proof of a detailed UI path.

## Source-age and tenant-specific caution

Current Learning guides are copyright 2026. Nevertheless, validate specific mobile/API, content provider, enrollment and access behaviour against current details and the customer's enabled configuration.

Do not assume a documented option is enabled in a given tenant. Where the answer depends on configuration, role assignment, country/legal employer, subscription, opt-in, data, or an Oracle Support defect, explicitly identify what must be confirmed.
