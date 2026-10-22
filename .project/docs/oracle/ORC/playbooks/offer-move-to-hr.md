# Job-offer approval and Move to HR

Synthesized from DOC-001, Chapters 21 and 4; see [source dossier](../DOC-001.md) and official [Implementing Recruiting PDF](https://docs.oracle.com/en/cloud/saas/talent-management/faimh/implementing-recruiting.pdf).

Keep these separate: (1) offer content/lifecycle, (2) approval, and (3) Move to HR/person creation.

- Approval rules based on requisition information are configured through Tools > Transaction Console > Approval Rules > Approve Job Offer.
- Offer/requisition/assignment flexfield-based offer approval follows the Worklist task configuration route described for **OfferApprovalHumanTask**. Check the relevant subsection before choosing a rule editor; the mechanisms are not interchangeable.
- The Move to HR action may be placed on Offer — Accepted or eligible non-terminal states/phase events in custom phases between Offer and HR, according to the source.
- Candidate duplicate protection at Move to HR has a separate Recruiting setting from Person Creation Duplicate Check. Review duplicate match option, attribute availability, and the person types included.
- The source describes automatic internal-offer processing through **Perform Recruiting Candidate Selection Process Offer Actions** and a default seven-day lead time. Validate the configuration and release before relying on it.
- Decide separately whether candidates are withdrawn from other active applications or removed from pools at Move to HR.
- When movement fails, inspect CSP state/action conditions, duplicate-check settings, and the resulting application status/notification; don't infer the cause from the status alone.

Key source locations: approval rules beginning around printed p. 296 / PDF p. 314; duplicate check and Move-to-HR control settings, printed pp. 316–322 / PDF pp. 334–340.
