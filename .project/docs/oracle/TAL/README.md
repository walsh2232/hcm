# Oracle Talent Management — module knowledge base

**Module code:** TAL  
**Evidence baseline:** 2026-10-22  
**Reusable skill:** [Oracle HCM Expert](../../../../.agents/skills/oracle-hcm-expert/SKILL.md)

This folder contains the source manifest, module domain map and operational instructions for a source-grounded retrieval workflow. The manifest records official Oracle guide identities and URL provenance. Full PDF/HTML text and SQLite search indexes are fetched into Git-ignored local cache; they are not copied into this public repository.

## Official guides and readiness sources

| Guide/source | Document ID | Pages | Official source |
|---|---|---:|---|
| Implementing Talent Management Base | G34432-02 | 276 | [HTML](https://docs.oracle.com/en/cloud/saas/talent-management/faitm/index.html) · [PDF](https://docs.oracle.com/en/cloud/saas/talent-management/faitm/implementing-talent-management-base.pdf) |
| Implementing Goal Management | G34428-01 | 76 | [HTML](https://docs.oracle.com/en/cloud/saas/talent-management/faigm/index.html) · [PDF](https://docs.oracle.com/en/cloud/saas/talent-management/faigm/implementing-goal-management.pdf) |
| Implementing Performance Management | G34430-04 | 188 | [HTML](https://docs.oracle.com/en/cloud/saas/talent-management/faipm/index.html) · [PDF](https://docs.oracle.com/en/cloud/saas/talent-management/faipm/implementing-performance-management.pdf) |
| Implementing Talent Review and Succession Management | G34433-01 | 122 | [HTML](https://docs.oracle.com/en/cloud/saas/talent-management/fatrs/index.html) · [PDF](https://docs.oracle.com/en/cloud/saas/talent-management/fatrs/implementing-talent-review-and-succession-management.pdf) |
| Using Goal Management | G34437-02 | — | [HTML](https://docs.oracle.com/en/cloud/saas/talent-management/faugm/index.html) |
| Using Performance Management | G34439-07 | — | [HTML](https://docs.oracle.com/en/cloud/saas/talent-management/faupm/index.html) |
| Using Talent Review and Succession Management | G34441-01 | — | [HTML](https://docs.oracle.com/en/cloud/saas/talent-management/fautr/index.html) |
| Release readiness context | — | HTML | [Talent Management 26D Feature Summary](https://docs.oracle.com/en/cloud/saas/readiness/hcm/26d/tama-26d/26D-talent-mgmt-wn-t78661.htm) |
| Oracle guide/readiness catalog | — | HTML | [Official Oracle catalog](https://docs.oracle.com/en/cloud/saas/talent-management/books.html) |

See [source-manifest.json](source-manifest.json) for all source URLs, their roles, release metadata and freshness policy. See [domain-map.md](domain-map.md) for topic routing and domain-specific caveats.

## Build and query this module's local index

From the repository root, after `python -m pip install -r requirements-knowledge.txt`:

```bash
python scripts/oracle_hcm_knowledge.py status --manifest .project/docs/oracle/TAL/source-manifest.json
python scripts/oracle_hcm_knowledge.py refresh --manifest .project/docs/oracle/TAL/source-manifest.json
python scripts/oracle_hcm_knowledge.py ingest --manifest .project/docs/oracle/TAL/source-manifest.json
python scripts/oracle_hcm_knowledge.py search "exact product term or task name" --manifest .project/docs/oracle/TAL/source-manifest.json
```

## Important qualification

Talent Management is a family of submodules, each with distinct guides. Use the matching submodule's guide and release item; do not apply a feature's 'setup required' or 'opt in' action blindly without confirming the actual release and enabled tenant configuration.

An Oracle Help Center page being public does not prove that a feature is licensed, enabled, configured, or supported in a particular customer's environment. Verify the tenant release and exact source passage before prescribing configuration changes.
