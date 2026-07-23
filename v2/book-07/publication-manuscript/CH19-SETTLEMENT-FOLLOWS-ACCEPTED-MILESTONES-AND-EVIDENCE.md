# CH19 — Settlement Follows Accepted Milestones and Evidence

An invoice asks to be paid.

Settlement decides whether an amount has become payable under the accepted engagement, milestone, Evidence and commercial terms.

These are not the same event.

```text
invoice received
≠ milestone completed
≠ Evidence accepted
≠ settlement authorized
≠ settlement executed
```

MGSN therefore links settlement to accepted performance rather than to elapsed time, Provider assertion or payment pressure alone.

## 1. What settlement must answer

A settlement decision should answer:

- which engagement and package version applies;
- which milestone is under review;
- what the Provider promised;
- what Evidence was required;
- what was actually delivered;
- who reviewed and accepted it;
- whether correction remains open;
- whether scope or price changed;
- which amount is earned;
- which amount remains reserved, disputed or refundable.

Settlement is the commercial conclusion of a governed performance check.

## 2. Milestones need clear acceptance criteria

A milestone should define:

- name and purpose;
- expected output;
- required Evidence;
- deadline or timing assumption;
- responsible Provider;
- review authority;
- acceptance criteria;
- correction path;
- settlement amount or formula;
- holdback or exception rules.

Examples may include:

```text
Conflict and Intake Confirmed
Draft Prepared
Customer-approved Package Ready
Protected Action Performed
Official Acknowledgement Returned
Correction Completed
Registration-stage Action Completed
Certificate or Final Return Delivered
```

The milestone name must not claim more than its Evidence proves.

## 3. Evidence types

Depending on the service, Evidence may include:

- Provider acknowledgement;
- work product;
- filing copy;
- official receipt;
- payment receipt;
- official correspondence;
- tracking record;
- signed document;
- translated document with provenance;
- customer approval;
- correction report;
- certificate;
- structured Return.

Evidence has strength, scope and source.

```text
Provider statement
≠ official acknowledgement

uploaded document
≠ validated document
```

The acceptance process should identify what each item establishes.

## 4. Acceptance authority

Different milestones may require different reviewers.

- an operator may confirm completeness;
- a professional may review legal substance;
- a customer may approve final content;
- Finance may confirm cleared funds;
- the Owning Service may validate formal-state impact;
- MGSN may confirm Return completeness.

```text
one reviewer
≠ universal acceptance authority
```

The settlement record should name the authority that accepted the relevant milestone.

## 5. Accepted, conditionally accepted and rejected

Milestone review may produce:

```text
Accepted
Accepted with Minor Follow-up
Conditionally Accepted
Correction Required
Partially Accepted
Rejected
Disputed
Unknown Pending Evidence
```

Conditional acceptance should state what remains open and whether settlement may proceed in full, in part or not at all.

## 6. Partial settlement

An engagement can create value before final completion.

Partial settlement may be appropriate where:

- preparation was completed but filing was cancelled;
- one jurisdiction was completed and another failed;
- one class proceeded and another was removed;
- an official action was attempted but rejected for a correctable reason;
- a milestone was accepted while later work remains open.

Partial settlement requires a visible basis. It must not become an arbitrary compromise detached from scope and Evidence.

## 7. Holdbacks

A holdback reserves part of an amount until a later condition is satisfied.

Possible reasons include:

- official receipt pending;
- certificate not yet returned;
- correction window still open;
- Provider reimbursement not reconciled;
- final customer confirmation pending;
- dispute or complaint under review.

A holdback should specify amount, reason, release condition and review date.

## 8. Correction before settlement

Where a deliverable fails acceptance criteria, the normal response may be correction rather than immediate non-payment or termination.

The correction record should state:

- defect;
- responsible party;
- required correction;
- deadline;
- additional cost treatment;
- effect on the Matter deadline;
- new Evidence expected;
- whether settlement is paused.

```text
correction requested
≠ engagement failed permanently
```

Repeated or material correction may affect Trust, package admission and future eligibility.

## 9. Official action and formal state

A Provider may return an official receipt or correspondence. MGSN can validate the Return for completeness and provenance.

The Owning Service remains responsible for deciding whether and how the formal Matter state changes.

```text
Return accepted by MGSN
≠ formal state updated
```

Settlement can be authorized for accepted Provider performance while a separate reconciliation issue remains open, if the accepted terms allow it. The two decisions should remain visible.

## 10. Provider invoice and accepted amount

An invoice should reference:

- engagement;
- milestone;
- package or approved change;
- cost layer;
- currency;
- taxes and disbursements;
- supporting Evidence;
- prior payments or credits.

The accepted amount may differ from the invoice because of:

- partial completion;
- unapproved additional work;
- duplicate billing;
- wrong fee version;
- unused official funds;
- approved correction;
- exchange-rate treatment;
- tax adjustment;
- dispute hold.

The difference must be explained.

## 11. Settlement sequence

A controlled sequence may be:

```text
Milestone Due
→ Provider Return Received
→ Evidence Validation
→ Acceptance Decision
→ Amount Calculation
→ Settlement Authorization
→ Payment Execution
→ Provider Receipt Confirmation
→ Finance Reconciliation
```

Each transition should be attributable and reversible only through a governed correction or reversal process.

## 12. Disputes

A settlement dispute may concern:

- whether work was in scope;
- whether the correct version was used;
- whether the milestone was completed;
- whether Evidence is sufficient;
- whether extra work was approved;
- whether official fees were paid;
- whether delay caused loss;
- whether a refund or credit is due.

The dispute record should preserve:

- claims by each party;
- relevant versions;
- communications;
- Evidence;
- funds state;
- deadlines;
- interim protective action;
- decision authority;
- resolution or continuing Unknown.

## 13. No automatic settlement from elapsed time

A Provider may expect payment after a number of days. The platform may use service-level expectations. Neither should convert silence into acceptance where material Evidence is required.

```text
review period elapsed
≠ milestone necessarily accepted
```

Where deemed acceptance is contractually used, it must be explicit, lawful and limited. High-risk or protected-action milestones should not rely on silent acceptance without careful review.

## 14. Trust and settlement

Settlement Evidence contributes to network Trust.

Useful signals include:

- on-time delivery;
- complete Evidence;
- low correction burden;
- accurate invoicing;
- official-fee reconciliation;
- responsive dispute handling;
- refund reliability.

Trust should use the specific service and context rather than one universal public score.

A disputed milestone should not automatically condemn the Provider. Patterns, materiality and resolution quality matter.

## 15. AI boundaries

AI may assist with:

- comparing required and returned Evidence;
- extracting invoice references;
- detecting duplicate charges;
- identifying missing receipts;
- proposing a reconciliation table;
- flagging scope or version mismatch.

AI must not:

- accept professional work;
- determine official truth;
- authorize settlement;
- decide liability;
- resolve a dispute;
- release funds.

## 16. Failure modes

### 16.1 Invoice triggers automatic payment

The required official receipt is missing.

Correct response: hold settlement pending the defined Evidence or approved exception.

### 16.2 Deliverable is accepted by the wrong role

An operator approves legal substance outside their authority.

Correct response: obtain the required professional or customer review.

### 16.3 Full payment after partial work

Only preparation was completed, but the invoice covers filing and registration.

Correct response: calculate the accepted milestone amount and preserve the remainder.

### 16.4 Correction history is erased

A corrected document replaces the defective version with no trace.

Correct response: preserve both versions, correction reason and acceptance decision.

### 16.5 MGSN Return acceptance updates formal state

A Provider Return is treated as official Matter truth without Owning Service validation.

Correct response: separate Return acceptance from formal-state reconciliation.

## 17. Product principle

Settlement should reward accepted performance while preserving correction, dispute and formal-state boundaries.

```text
clear milestone
+ required Evidence
+ correct acceptance authority
+ explicit amount calculation
+ Finance reconciliation
= accountable settlement
```

The next chapter explains how commercial exceptions—fee increases, scope changes, emergency costs, cancellations and substitutions—must be governed rather than absorbed through informal messages.