# Extensions

Fast Formulas, Redwood/Visual Builder extensions, and page configurations.

```
extensions/<MODULE>/formulas/<FormulaName>.ff
extensions/<MODULE>/pages/<page>/            Configuration export + design notes
extensions/<MODULE>/vbs/<extension>/         Visual Builder extension source
```

## Extension policy

Every extension is a permanent maintenance liability: it must be regression-tested
against each Oracle quarterly update, and it can be broken by changes nobody on
this project controls. The policy for choosing configuration over extension is
established by `HCM-030` and recorded as an ADR.

**Each extension requires its own ADR** stating: the requirement it serves, why
configuration could not meet it (with the `DOC-###` establishing the product
limitation), the maintenance cost accepted, and the quarterly-update regression
exposure created.

An extension without an ADR is technical debt that nobody agreed to take on.

## Every artifact carries

A header comment naming: the requirement (`REQ-<MOD>-###`), the ADR authorising
it, the source establishing the product constraint, and the release last validated
against.
