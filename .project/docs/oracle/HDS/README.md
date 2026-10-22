# Oracle Help Desk — module knowledge base

**Module code:** HDS  
**Evidence baseline:** 2026-10-22  
**Reusable skill:** [Oracle HCM Expert](../../../../.agents/skills/oracle-hcm-expert/SKILL.md)

This folder contains the source manifest, module domain map and operational instructions for a source-grounded retrieval workflow. The manifest records official Oracle guide identities and URL provenance. Full PDF/HTML text and SQLite search indexes are fetched into Git-ignored local cache; they are not copied into this public repository.

## Official guides and readiness sources

| Guide/source | Document ID | Pages | Official source |
|---|---|---:|---|
| Implementing Help Desk | F77890-16 | 238 | [HTML](https://docs.oracle.com/en/cloud/saas/fusion-service/farhd/index.html) · [PDF](https://docs.oracle.com/en/cloud/saas/fusion-service/farhd/implementing-help-desk.pdf) |
| Using Help Desk | F77889-07 | 80 | [HTML](https://docs.oracle.com/en/cloud/saas/fusion-service/faurd/index.html) · [PDF](https://docs.oracle.com/en/cloud/saas/fusion-service/faurd/using-help-desk.pdf) |
| Release readiness context | — | HTML | [Oracle Fusion Service Cloud Readiness / What's New (includes Help Desk 26D)](https://docs.oracle.com/en/cloud/saas/fusion-service/cloud-readiness-whats-new.html) |
| Oracle guide/readiness catalog | — | HTML | [Official Oracle catalog](https://docs.oracle.com/en/cloud/saas/fusion-service/cloud-readiness-whats-new.html) |

See [source-manifest.json](source-manifest.json) for all source URLs, their roles, release metadata and freshness policy. See [domain-map.md](domain-map.md) for topic routing and domain-specific caveats.

## Build and query this module's local index

From the repository root, after `python -m pip install -r requirements-knowledge.txt`:

```bash
python scripts/oracle_hcm_knowledge.py status --manifest .project/docs/oracle/HDS/source-manifest.json
python scripts/oracle_hcm_knowledge.py refresh --manifest .project/docs/oracle/HDS/source-manifest.json
python scripts/oracle_hcm_knowledge.py ingest --manifest .project/docs/oracle/HDS/source-manifest.json
python scripts/oracle_hcm_knowledge.py search "exact product term or task name" --manifest .project/docs/oracle/HDS/source-manifest.json
```

## Important qualification

Help Desk source material sits in Oracle Fusion Service rather than the core Human Resources Books catalog. Validate available features, subscription, role privileges and the integration boundary with HCM; don't assume every generic service feature is enabled or licensed in a tenant.

An Oracle Help Center page being public does not prove that a feature is licensed, enabled, configured, or supported in a particular customer's environment. Verify the tenant release and exact source passage before prescribing configuration changes.
