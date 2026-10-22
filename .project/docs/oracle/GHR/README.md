# Oracle Global Human Resources — module knowledge base

**Module code:** GHR  
**Source baseline checked:** 2026-10-22  
**Release reference:** Oracle Global Human Resources 26D What's New/readiness page  
**Reusable skill:** [Oracle HCM Expert](../../../../.agents/skills/oracle-hcm-expert/SKILL.md)

This module has a real source manifest and locally searchable source pipeline. The condensed domain map is navigation and retrieval guidance; exact procedural answers must be based on freshly retrieved passages, exact chapter/page citations, the target quarterly release, and tenant-specific setup.

## Verified official sources

| Source | Document ID | PDF pages | Links |
|---|---|---:|---|
| Implementing Global Human Resources | G34712-10 | 390 | [HTML]( https://docs.oracle.com/en/cloud/saas/human-resources/faigh/implementing-global-human-resources/index.html ) · [PDF](https://docs.oracle.com/en/cloud/saas/human-resources/faigh/implementing-global-human-resources.pdf) |
| Using Global Human Resources | G34740-15 | 368 | [HTML]( https://docs.oracle.com/en/cloud/saas/human-resources/fawhr/using-global-human-resources/index.html ) · [PDF](https://docs.oracle.com/en/cloud/saas/human-resources/fawhr/using-global-human-resources.pdf) |
| Human Resources 26D What's New / readiness | G61073-04 | HTML | [Current release page](https://docs.oracle.com/en/cloud/saas/readiness/hcm/26d/hure-26d/) |
| Oracle Human Resources - All Books | — | HTML | [Oracle catalog](https://docs.oracle.com/en/cloud/saas/human-resources/books.html) |

## Retrieval instructions

The canonical source list is [source-manifest.json](source-manifest.json). Run from the repository root after installing [requirements-knowledge.txt](../../../../requirements-knowledge.txt):

```bash
python scripts/oracle_hcm_knowledge.py status --manifest .project/docs/oracle/GHR/source-manifest.json
python scripts/oracle_hcm_knowledge.py refresh --manifest .project/docs/oracle/GHR/source-manifest.json
python scripts/oracle_hcm_knowledge.py ingest --manifest .project/docs/oracle/GHR/source-manifest.json
python scripts/oracle_hcm_knowledge.py search "specific topic or exact Oracle label" --manifest .project/docs/oracle/GHR/source-manifest.json
```

PDFs, extracted text and the SQLite FTS index remain in the local, Git-ignored `.cache/oracle-hcm/ghr/` directory. The public repository stores metadata and authored notes only.

## Caveats

The Using guide is copyrighted 2025 while Implementing is copyrighted 2026. Use the current release readiness content for changed behaviour and keep tenant-level security and enterprise-structure assumptions separate from generic documentation.

A standalone book titled “Administering Global Human Resources” is not assumed. The actual listed Using guide includes operational tasks; setup guidance uses the Implementing guide. Consult the source catalog for any separate administration/security guide relevant to the precise question.
