# Oracle Recruiting source workspace

This directory holds source records, compact navigation metadata, and documented retrieval rules for Oracle Recruiting. It does **not** hold the full downloaded Oracle PDF or the complete extracted guide.

## Contents

| File | Purpose |
| --- | --- |
| [DOC-001.md](DOC-001.md) | Source dossier for *Implementing Recruiting* (G34431-12), including checksum, edition caveat, and citation convention. |
| [topic-index.md](topic-index.md) | Compact guide chapter map with both Oracle printed pages and physical PDF pages. |
| [RETRIEVAL-SKILL.md](RETRIEVAL-SKILL.md) | Module-level rules for grounding answers and citing Oracle documentation. |

The full chapter Markdown, SQLite FTS index, and retrieval chunks are private/local artifacts. A generated PDF-derived corpus should live under `.local/oracle-docs/<DOC-ID>/`; this path is git-ignored. See the [documentation ingest contract](../../README.md) and [source registry](../../source-registry.md).

## Source coverage status

- One Recruiting implementation guide has been extracted locally and validated for page markers, topic links, retrieval chunk structure, and search-index integrity.
- The current Oracle catalogue identifies companion guides for Recruiting usage, Recruiting Booster, HCM security, security reference, and HCM REST APIs. The registry records those sources, but their complete bodies are not in this local corpus yet.
- The target tenant's quarterly HCM release and confirmed module scope remain unknown. Do not claim tenant-release validation until the Product Owner resolves `GAP-002`.
