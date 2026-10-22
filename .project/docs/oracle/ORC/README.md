# Oracle Recruiting — module knowledge base

Module code: ORC  
Evidence baseline checked: 2026-10-22  
Current release readiness source: Recruiting 26D What's New  
Skill: Oracle HCM Expert at .agents/skills/oracle-hcm-expert/SKILL.md

This is a source-aware knowledge layer, not a replacement for Oracle's complete manuals. It provides a domain map, official source links, release-aware answer rules, and a local retrieval pipeline.

## Verified official sources

| Source | Document ID | Purpose | PDF pages | Link |
|---|---|---|---:|---|
| Implementing Recruiting | G34431-12 | Setup and configuration | 448 | [HTML](https://docs.oracle.com/en/cloud/saas/talent-management/faimh/index.html) · [PDF](https://docs.oracle.com/en/cloud/saas/talent-management/faimh/implementing-recruiting.pdf) |
| Using Recruiting | G34440-08 | Recruiter and candidate processes | 220 | [HTML](https://docs.oracle.com/en/cloud/saas/talent-management/faush/index.html) · [PDF](https://docs.oracle.com/en/cloud/saas/talent-management/faush/using-recruiting.pdf) |
| Using and Administering Recruiting Booster | G34425-04 | Booster use and administration/configuration | 70 | [HTML](https://docs.oracle.com/en/cloud/saas/talent-management/faarb/index.html) · [PDF](https://docs.oracle.com/en/cloud/saas/talent-management/faarb/using-and-administering-recruiting-booster.pdf) |
| Recruiting 26D What's New | G61079-03 | Release-specific change analysis | HTML | [What's New](https://docs.oracle.com/en/cloud/saas/readiness/hcm/26d/recr-26d/) · [Feature summary](https://docs.oracle.com/en/cloud/saas/readiness/hcm/26d/recr-26d/26D-recruiting-wn-t78659.htm) |
| Oracle Talent Management - All Books | — | Guide inventory | HTML | [Oracle catalog](https://docs.oracle.com/en/cloud/saas/talent-management/books.html) |

Guide naming caveat: Oracle's catalog lists Implementing Recruiting, Using Recruiting, and Using and Administering Recruiting Booster. It does not list a standalone book titled “Administering Recruiting.” For core Recruiting administration, use the relevant current implementation/using chapter and official security, setup, and release pages. Do not invent a guide.

## Storage policy
- Committed: source metadata, links, concise authored findings, skill instructions, code and source fingerprints.
- Downloaded at execution time: current Oracle HTML chapters and PDFs.
- Local only: downloaded manuals, extracted full text and SQLite search index under .cache/oracle-hcm/; this path is ignored by Git.
- Not included: tenant-specific enabled-feature state, configuration, roles, production data or Oracle Support notes behind authentication. Those require an authorized source.

## Build and use the searchable index
From the repository root, create a Python virtual environment, install requirements-knowledge.txt, then run:
1. python scripts/oracle_hcm_knowledge.py status
2. python scripts/oracle_hcm_knowledge.py refresh
3. python scripts/oracle_hcm_knowledge.py ingest
4. python scripts/oracle_hcm_knowledge.py search "job application flow candidate selection"

Search results include the official source URL and PDF page or HTML chapter URL. Full manuals are not copied into Git.

## Release handling
1. Confirm the release running in the customer's environment.
2. Compare its What's New/readiness page with the rolling implementation and using guides.
3. Inspect feature impact, action to enable, dependencies, and role/process impacts before advising.
4. “Potential Setup” or “None” is not proof that a feature is enabled. Read the full feature row/details and confirm tenant state.
5. Refresh source fingerprints and rebuild the local index after a source change; retain Git revisions as the audit trail.
6. If public documentation does not explain tenant behaviour, consult authorized Oracle Support material rather than inventing a workaround.
