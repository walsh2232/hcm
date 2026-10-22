# Oracle HCM Analytics and Reporting — module knowledge base

**Module code:** RPT  
**Evidence baseline:** 2026-10-22  
**Reusable skill:** [Oracle HCM Expert](../../../../.agents/skills/oracle-hcm-expert/SKILL.md)

This folder contains the source manifest, module domain map and operational instructions for a source-grounded retrieval workflow. The manifest records official Oracle guide identities and URL provenance. Full PDF/HTML text and SQLite search indexes are fetched into Git-ignored local cache; they are not copied into this public repository.

## Official guides and readiness sources

| Guide/source | Document ID | Pages | Official source |
|---|---|---:|---|
| Administering Analytics and Reports for HCM | G34671-01 | 120 | [HTML](https://docs.oracle.com/en/cloud/saas/human-resources/fahca/index.html) · [PDF](https://docs.oracle.com/en/cloud/saas/human-resources/fahca/administering-analytics-and-reports-for-hcm.pdf) |
| Oracle Talent Management Books — Using Oracle Transactional Business Intelligence | — | HTML catalog | [Official catalog](https://docs.oracle.com/en/cloud/saas/talent-management/books.html) |
| Release readiness context | — | HTML | [Oracle HCM readiness catalog](https://docs.oracle.com/en/cloud/saas/readiness/hcm.html) (contains HCM Analytics / Fusion Data Intelligence references; not interchangeable with OTBI) |
| Oracle guide/readiness catalog | — | HTML | [Official Oracle catalog](https://docs.oracle.com/en/cloud/saas/human-resources/books.html) |

See [source-manifest.json](source-manifest.json) for all source URLs, their roles, release metadata and freshness policy. See [domain-map.md](domain-map.md) for topic routing and domain-specific caveats.

## Build and query this module's local index

From the repository root, after `python -m pip install -r requirements-knowledge.txt`:

```bash
python scripts/oracle_hcm_knowledge.py status --manifest .project/docs/oracle/RPT/source-manifest.json
python scripts/oracle_hcm_knowledge.py refresh --manifest .project/docs/oracle/RPT/source-manifest.json
python scripts/oracle_hcm_knowledge.py ingest --manifest .project/docs/oracle/RPT/source-manifest.json
python scripts/oracle_hcm_knowledge.py search "exact product term or task name" --manifest .project/docs/oracle/RPT/source-manifest.json
```

## Important qualification

Oracle lists Administering Analytics and Reports for HCM and separate OTBI guidance. Don't conflate transactional OTBI with Oracle Fusion Data Intelligence. The HCM analytics guide's copyright is 2025; retrieve exact subject-area/feature evidence and validate it against current role/data security.

An Oracle Help Center page being public does not prove that a feature is licensed, enabled, configured, or supported in a particular customer's environment. Verify the tenant release and exact source passage before prescribing configuration changes.
