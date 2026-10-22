# Oracle Learning — module knowledge base

**Module code:** LRN  
**Source baseline checked:** 2026-10-22  
**Release reference:** Oracle Learning 26D What's New/readiness page  
**Reusable skill:** [Oracle HCM Expert](../../../../.agents/skills/oracle-hcm-expert/SKILL.md)

This module has a real source manifest and locally searchable source pipeline. The condensed domain map is navigation and retrieval guidance; exact procedural answers must be based on freshly retrieved passages, exact chapter/page citations, the target quarterly release, and tenant-specific setup.

## Verified official sources

| Source | Document ID | PDF pages | Links |
|---|---|---:|---|
| Implementing Learning | G34429-04 | 44 | [HTML](https://docs.oracle.com/en/cloud/saas/talent-management/faiml/index.html) · [PDF](https://docs.oracle.com/en/cloud/saas/talent-management/faiml/implementing-learning.pdf) |
| Using Learning | G34438-02 | 100 | [HTML](https://docs.oracle.com/en/cloud/saas/talent-management/fatul/index.html) · [PDF](https://docs.oracle.com/en/cloud/saas/talent-management/fatul/using-learning.pdf) |
| Learning and Development 26D What's New / readiness | — | HTML | [Current release page](https://docs.oracle.com/en/cloud/saas/readiness/hcm/26d/lear-26d/26D-learning-wn-f50703.htm) |
| Oracle Talent Management - All Books | — | HTML | [Oracle catalog](https://docs.oracle.com/en/cloud/saas/talent-management/books.html) |

## Retrieval instructions

The canonical source list is [source-manifest.json](source-manifest.json). Run from the repository root after installing [requirements-knowledge.txt](../../../../requirements-knowledge.txt):

```bash
python scripts/oracle_hcm_knowledge.py status --manifest .project/docs/oracle/LRN/source-manifest.json
python scripts/oracle_hcm_knowledge.py refresh --manifest .project/docs/oracle/LRN/source-manifest.json
python scripts/oracle_hcm_knowledge.py ingest --manifest .project/docs/oracle/LRN/source-manifest.json
python scripts/oracle_hcm_knowledge.py search "specific topic or exact Oracle label" --manifest .project/docs/oracle/LRN/source-manifest.json
```

PDFs, extracted text and the SQLite FTS index remain in the local, Git-ignored `.cache/oracle-hcm/lrn/` directory. The public repository stores metadata and authored notes only.

## Caveats

Current Learning guides are copyright 2026. Nevertheless, validate specific mobile/API, content provider, enrollment and access behaviour against current details and the customer's enabled configuration.

A standalone book titled “Administering Learning” is not assumed. The actual listed Using guide includes operational tasks; setup guidance uses the Implementing guide. Consult the source catalog for any separate administration/security guide relevant to the precise question.
