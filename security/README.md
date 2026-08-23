# Security & Role Design

Role design matrices and data security policy design for Oracle HCM.

```
security/role-matrix.md          Role-to-privilege mapping (owned by HCM-022)
security/data-security.md        Data security scoping and area-of-responsibility design
security/sod-matrix.md           Segregation of duties analysis
security/<MODULE>/               Module-specific role notes
```

## Principles pending the ADR

The role design approach is established by `HCM-022`. Until it exists, no custom
role is built. These principles apply to that design and to everything under it:

1. **Least privilege**, justified per privilege — not per role.
2. **Prefer inheritance from delivered roles** over building from scratch; record
   every deviation and its reason, because deviations are what break at each
   quarterly update.
3. **Data security is designed, not inherited by accident.** State explicitly
   which population each role can see and why.
4. **Segregation of duties is evidenced**, not asserted — a matrix that an auditor
   can read.
5. **No credentials in this repository**, in any form (`ADR-0003`, `RISK-005`).
6. **Reporting inherits the same model.** A report is not a licence to see rows a
   role cannot see in the application (`reports/README.md`).

Every role design decision cites the `DOC-### §location` establishing the Oracle
security behaviour relied upon. Security is the area where inference is most
common and most expensive.
