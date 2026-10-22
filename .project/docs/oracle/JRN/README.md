# Oracle Journeys — module knowledge base

**Module code:** JRN  
**Evidence baseline:** 2026-10-22  
**Reusable skill:** [Oracle HCM Expert](../../../../.agents/skills/oracle-hcm-expert/SKILL.md)

This folder contains the source manifest, module domain map and operational instructions for a source-grounded retrieval workflow. The manifest records official Oracle guide identities and URL provenance. Full PDF/HTML text and SQLite search indexes are fetched into Git-ignored local cache; they are not copied into this public repository.

## Official guides and readiness sources

| Guide/source | Document ID | Pages | Official source |
|---|---|---:|---|
| Implementing and Using Journeys | G34729-11 | 204 | [HTML](https://docs.oracle.com/en/cloud/saas/human-resources/faijh/index.html) · [PDF](https://docs.oracle.com/en/cloud/saas/human-resources/faijh/implementing-and-using-journeys.pdf) |
| Release readiness context | — | HTML | [Human Resources 26D What's New](https://docs.oracle.com/en/cloud/saas/readiness/hcm/26d/hure-26d/) (cross-functional release context; not a Journeys-only release guide) |
| Oracle guide/readiness catalog | — | HTML | [Official Oracle catalog](https://docs.oracle.com/en/cloud/saas/human-resources/books.html) |

See [source-manifest.json](source-manifest.json) for all source URLs, their roles, release metadata and freshness policy. See [domain-map.md](domain-map.md) for topic routing and domain-specific caveats.

## Build and query this module's local index

From the repository root, after `python -m pip install -r requirements-knowledge.txt`:

```bash
python scripts/oracle_hcm_knowledge.py status --manifest .project/docs/oracle/JRN/source-manifest.json
python scripts/oracle_hcm_knowledge.py refresh --manifest .project/docs/oracle/JRN/source-manifest.json
python scripts/oracle_hcm_knowledge.py ingest --manifest .project/docs/oracle/JRN/source-manifest.json
python scripts/oracle_hcm_knowledge.py search "exact product term or task name" --manifest .project/docs/oracle/JRN/source-manifest.json
```

## Important qualification

Oracle lists one combined Implementing and Using Journeys guide, not separate books with those titles. Retrieve the exact task chapter and validate actual security, task availability, transaction dependencies, and assignment eligibility before prescribing navigation.

An Oracle Help Center page being public does not prove that a feature is licensed, enabled, configured, or supported in a particular customer's environment. Verify the tenant release and exact source passage before prescribing configuration changes.
