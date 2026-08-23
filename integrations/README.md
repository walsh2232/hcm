# Integrations

Inbound and outbound interface designs and code.

```
integrations/<MODULE>/<INT-name>/
    design.md        Interface specification (templates/spec.md, sections 1-9)
    contract/        Payload schemas, field mappings, sample messages (synthetic)
    src/             Implementation
    tests/           Interface tests and reconciliation checks
    runbook.md       Operational procedure (templates/runbook.md)
```

## Pattern selection

The approved pattern catalogue and the rule for choosing between HCM Extracts,
HDL, REST, SOAP, ATOM feeds, and file-based transfer is established by `HCM-021`
and recorded as an ADR. Until that ADR exists, no integration may be built —
choosing a pattern per-interface is how an estate acquires six ways of doing the
same thing.

## Every interface design states

- Source, target, direction, trigger, frequency, and expected volume
- The `DOC-### §location` establishing the Oracle-side constraint relied upon
- Payload contract and field-level mapping, with transformation rules
- Error handling: what is retried, what is dead-lettered, what alerts a human
- Reconciliation: how both sides are proven to agree, and how often
- Security: authentication approach (never credentials), data in transit, minimisation
- Failure impact on the business process, and the manual fallback

Interface inventory: `HCM-014`. Architecture baseline: `HCM-021`.
