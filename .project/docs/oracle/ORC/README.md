# Oracle Recruiting source workspace

This directory holds source records, compact navigation metadata, and documented retrieval rules for Oracle Recruiting. It does **not** hold the full downloaded Oracle PDF or the complete extracted guide.

## Contents

| File | Purpose |
| --- | --- |
| [DOC-001.md](DOC-001.md) | Source dossier for *Implementing Recruiting* (G34431-12), including checksum, edition caveat, and citation convention. |
| [topic-index.md](topic-index.md) | Compact guide chapter map with both Oracle printed pages and physical PDF pages. |
| [RETRIEVAL-SKILL.md](RETRIEVAL-SKILL.md) | Module-level rules for grounding answers and citing Oracle documentation. |
| [RECRUITING-BOOSTER-TOPIC-MAP.md](RECRUITING-BOOSTER-TOPIC-MAP.md) | Booster chapter map and implementation cross-links. |
| [SECURITY-NAVIGATION.md](SECURITY-NAVIGATION.md) | Routing across Recruiting security, Securing HCM, and the security reference book. |
| [CROSS-GUIDE-ROUTER.md](CROSS-GUIDE-ROUTER.md) | Select the best official guide for a Recruiting implementation or troubleshooting question. |
| [SOURCE-ISSUES.md](SOURCE-ISSUES.md) | Open source-level ambiguity log; SI-001/GAP-008 preserves two context-specific Oracle Search index names. |
| [playbooks/](playbooks/README.md) | Nineteen compact implementation/diagnostic playbooks derived from DOC-001. |

The full chapter Markdown, SQLite FTS index, and retrieval chunks are private/local artifacts. A generated PDF-derived corpus should live under `.local/oracle-docs/<DOC-ID>/`; this path is git-ignored. See the [documentation ingest contract](../../README.md) and [source registry](../../source-registry.md).

## Source coverage status

- One Recruiting implementation guide has been extracted locally and validated for page markers, topic links, retrieval chunk structure, and search-index integrity. The local corpus now has 751 retrieval chunks; 19 source-linked playbooks cover high-utility implementation and troubleshooting paths. A table-of-contents page map for the 220-page Using Recruiting guide has also been added; its body text is not locally indexed.
- The current Oracle catalogue identifies companion guides for Recruiting usage, Recruiting Booster, HCM security, security reference, and HCM REST APIs. Current Booster and HCM security editions now have compact topic/page maps; the full companion bodies are not in this local corpus yet.
- The target tenant's quarterly HCM release and confirmed module scope remain unknown. Do not claim tenant-release validation until the Product Owner resolves `GAP-002`.

## Intake status and validation

As of 2026-10-22, the private local corpus for **DOC-001** has 35 chapter files, 648 searchable SQLite topic headings, 650 CSV topic-index entries, 751 retrieval chunks, a SQLite FTS5 index, and 72 automated validation checks passing with no errors or warnings. Eleven lexical query tests cover candidate duplicates, vanity URLs, approvals, CSP actions, role/profile-option identifiers, interview-calendar privilege, and attachment indexing.

The companion-guide maps are navigation metadata only: **DOC-002** (*Using Recruiting*, G34440-08), **DOC-003** (*Using and Administering Recruiting Booster*, G34425-04), **DOC-004** (*Securing HCM*, G34732-10), and **DOC-005** (*Security Reference for HCM*, G34733-07) have not had their complete bodies ingested into the private corpus in this environment. Direct binary downloads failed, although Oracle's PDF viewer exposed page text/contents. Do not represent those books as locally searchable full-text sources.

The target tenant quarterly release and final project module scope remain unconfirmed. Guide-edition identifiers are not tenant-release validation.

## Playbook coverage

The playbook set now covers CSP automation, offer approvals/Move to HR, Recruiting security, career sites/application flows, candidate duplicates/search, Fast Formula contracts, candidate-data disposal and retention controls, Recruiting AI recommendations/data ingestion, requisition approvals, interview/calendar integration, partner provisioning, Oracle Search/P2T/T2T, notification templates, prescreening scoring/versioning, campaign opt-in/email operations, and agency portal access/privacy. They are concise source-linked pathways, not substitutes for the full chapter or tenant-specific release validation.

The Oracle Search source-string distinction is recorded as SI-001/GAP-008. A second visually verified issue in the TDS active-rule statement/precedence example is SI-004/GAP-009. Both are recorded in [SOURCE-ISSUES.md](SOURCE-ISSUES.md); do not silently harmonize the source statements.

## Companion ingestion fallback

A reusable [sequential HTML ingestor](../../../../scripts/oracle_docs/ingest_oracle_html.py) and [multi-source search tool](../../../../scripts/oracle_docs/search_corpus.py) are available for local use when Oracle's PDF endpoint is blocked. The HTML crawler retains source URLs and labels results by HTML sequence, not as PDF pages. It passed offline unit tests, but outbound DNS/network access in the current runtime prevented a full companion fetch. DOC-002–DOC-005 remain contents/page maps only, not full searchable corpora.
