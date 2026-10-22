# Candidate search and duplicate checks

Synthesized from DOC-001, Chapters 13, 21, and 34; see [source dossier](../DOC-001.md).

Separate three mechanisms:
1. Candidate-search visibility/security.
2. Candidate-file duplicate detection and merge.
3. Person-creation duplicate validation on Move to HR.

For search visibility, review the Recruiting candidate-search security section and its profile-option dependency, then verify user/data role scope and reproduce the query under the affected user.

For Move to HR, inspect the Enterprise Recruiting and Candidate Experience Information task > Move to HR section:
- Duplicate Check in Move to HR choice;
- configured Person Creation Duplicate Check algorithm and available attributes;
- Include as Potential Duplicates choice.
The source describes options that disable validation or reuse Person Creation Duplicate Check for all candidates or candidates with DOB and national identifier.

Test a normal unique candidate and a controlled duplicate case in non-production. Matching outcomes depend on configured rule and supplied attributes; do not change matching behavior without documenting false-positive/false-negative trade-offs and obtaining appropriate privacy/business review.

Sources: Candidate Security for Candidate Search in Ch. 13; duplicate check and Move-to-HR settings in Ch. 21, printed pp. 316–322 / PDF pp. 334–340.
