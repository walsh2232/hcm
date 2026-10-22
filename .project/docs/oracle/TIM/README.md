# Oracle Time and Labor — module knowledge base

**Module code:** TIM  
**Source baseline checked:** 2026-10-22  
**Release reference:** Oracle Time and Labor 26D What's New/readiness page  
**Reusable skill:** [Oracle HCM Expert](../../../../.agents/skills/oracle-hcm-expert/SKILL.md)

This module has a real source manifest and locally searchable source pipeline. The condensed domain map is navigation and retrieval guidance; exact procedural answers must be based on freshly retrieved passages, exact chapter/page citations, the target quarterly release, and tenant-specific setup.

## Verified official sources

| Source | Document ID | PDF pages | Links |
|---|---|---:|---|
| Implementing Time and Labor | G34726-01 | 310 | [HTML](https://docs.oracle.com/en/cloud/saas/human-resources/faitl/index.html) · [PDF](https://docs.oracle.com/en/cloud/saas/human-resources/faitl/implementing-time-and-labor.pdf) |
| Using Time and Labor | G34743-01 | 54 | [HTML](https://docs.oracle.com/en/cloud/saas/human-resources/fautl/index.html) · [PDF](https://docs.oracle.com/en/cloud/saas/human-resources/fautl/using-time-and-labor.pdf) |
| Human Resources 26D What's New / readiness | — | HTML | [Current release page](https://docs.oracle.com/en/cloud/saas/readiness/hcm/26d/tila-26d/26D-time-labor-wn-f51382.htm) |
| Oracle Human Resources - All Books | — | HTML | [Oracle catalog](https://docs.oracle.com/en/cloud/saas/human-resources/books.html) |

## Retrieval instructions

The canonical source list is [source-manifest.json](source-manifest.json). Run from the repository root after installing [requirements-knowledge.txt](../../../../requirements-knowledge.txt):

```bash
python scripts/oracle_hcm_knowledge.py status --manifest .project/docs/oracle/TIM/source-manifest.json
python scripts/oracle_hcm_knowledge.py refresh --manifest .project/docs/oracle/TIM/source-manifest.json
python scripts/oracle_hcm_knowledge.py ingest --manifest .project/docs/oracle/TIM/source-manifest.json
python scripts/oracle_hcm_knowledge.py search "specific topic or exact Oracle label" --manifest .project/docs/oracle/TIM/source-manifest.json
```

PDFs, extracted text and the SQLite FTS index remain in the local, Git-ignored `.cache/oracle-hcm/tim/` directory. The public repository stores metadata and authored notes only.

## Caveats

Time results depend on the applicable worker, time-entry configuration, rule sets, approvals, date effectiveness and transfer/downstream configuration. Verify exact rules and process names in the indexed guide before acting.

A standalone book titled “Administering Time and Labor” is not assumed. The actual listed Using guide includes operational tasks; setup guidance uses the Implementing guide. Consult the source catalog for any separate administration/security guide relevant to the precise question.
