# B05-CH-18 — Quote, Acceptance and Commercial Instruction

**Status:** Part III Draft  
**Chapter Map:** B05-TOC-V0.1  
**Part:** Part III — Commercial Journey and Formal Intake

## Chapter Purpose

A Proposal helps the user compare options.

A Quote expresses a specific commercial offer under defined terms.

Acceptance records agreement to those terms.

A Commercial Instruction records an authorized request to proceed with the stated service scope.

These are connected but distinct.

```text
Proposal Option
→ Quote
→ Acceptance
→ Commercial Instruction
→ Order Formation Request
```

```text
Quote
≠ Invoice
≠ Payment
≠ Filing Approval
≠ Provider Instruction
≠ Submission
```

---

## 1. A Quote Is a Versioned Commercial Offer

A Quote should identify:

- quoting organization;
- recipient;
- proposal option;
- scope;
- prices;
- currency;
- tax treatment;
- payment terms;
- included and excluded work;
- dependencies;
- validity;
- commercial terms;
- version.

It should be possible to reproduce exactly what the recipient accepted.

---

## 2. Proposal and Quote May Be Separate Artifacts

A proposal may explain strategy in detail.

A Quote may state the commercial offer.

They may be combined for usability, but the Product should preserve the logical difference.

The strategic recommendation may remain valid while the price expires. The price may remain valid while the strategy changes materially.

---

## 3. Quote Issuance Requires Commercial Authority

The Product should identify who may issue a Quote on behalf of the organization.

Issuance may require pricing approval, discount approval, provider-cost verification, tax review, credit approval, or scope review.

AI may draft a Quote. It may not bind the organization.

---

## 4. Quote Recipient Is Not Automatically the Applicant

The recipient may be a client, agent, procurement contact, finance contact, affiliate, intermediary, applicant, or payer.

The Quote should identify the commercial recipient without changing applicant identity.

---

## 5. Acceptance Must Identify the Exact Version

Acceptance should preserve:

- Quote identifier;
- version;
- accepting person;
- represented organization;
- authority basis;
- accepted scope;
- accepted price;
- timestamp;
- acceptance method;
- conditions or exceptions;
- evidence.

A generic “approved” message may be insufficient if scope has changed.

---

## 6. Partial and Conditional Acceptance Are Possible

A user may accept selected jurisdictions, filing units, classes, stages, searches, or one wave of a portfolio plan.

Conditional acceptance may be subject to applicant confirmation, signed POA, provider availability, final search, budget approval, payment, or deadline verification.

The Product should preserve the accepted subset and outstanding conditions.

---

## 7. Acceptance Authority Must Be Verified

Account access does not prove authority.

Possible authority sources include organization role, contract, client instruction policy, delegated authority, named approver, procurement mandate, or engagement terms.

Unverified acceptance may remain pending.

---

## 8. Silence Is Not Acceptance

The Product should not treat viewing, downloading, opening an email, selecting an option, asking a question, or making a partial payment as acceptance unless agreed commercial rules clearly provide otherwise.

---

## 9. Acceptance Evidence Must Be Preserved

Evidence may include:

- signed document;
- authenticated click;
- email;
- portal action;
- purchase order;
- recorded instruction;
- contract execution.

The evidence should link to the exact Quote version.

---

## 10. Commercial Instruction Adds an Operational Request

Commercial Instruction answers:

> What does the authorized client or organization now ask the service organization to do under the accepted commercial terms?

It may identify accepted scope, start condition, priority, target date, payer, communication channel, required participants, known dependencies, and authorized variations.

---

## 11. Acceptance and Instruction May Occur Together or Separately

Some organizations use one action:

```text
Accept and Instruct
```

Others require:

```text
Accept Commercial Terms
→ Procurement or Payment Step
→ Issue Work Instruction
```

The Product may support both patterns while preserving both records.

---

## 12. Commercial Instruction Does Not Authorize Filing

A Commercial Instruction may authorize the organization to begin professional work.

It does not necessarily authorize final applicant details, final specification, final filing unit, final route, signature, payment of official fees, provider instruction, or filing submission.

```text
Commercial Instruction
≠ Filing Approval
```

---

## 13. Commercial Instruction May Request Formal Object Creation

The Product may prepare a request to create:

- Order;
- Matter;
- Customer relationship reference;
- service engagement;
- responsibility assignment;
- payment request;
- Execution Context.

The applicable Owning Service creates and records the formal object. MarkReg retains the reference.

---

## 14. Scope Change After Acceptance Requires Governance

A change may affect price, provider, deadline, class count, filing unit, applicant, route, documents, professional risk, or later-stage inclusion.

The Product should classify the change as:

```text
Non-material clarification
Commercial amendment
Professional-scope amendment
New Quote required
New acceptance required
New filing approval required
```

---

## 15. Cancellation and Withdrawal Must Be Explicit

The record should identify who requested cancellation, authority, affected scope, timing, work already performed, fees earned or refundable, external commitments, provider cancellation, official-fee recoverability, and deadline consequences.

Cancellation of commercial work is not cancellation of an official application unless an authorized external action occurs.

---

## 16. Quote Expiry Before Acceptance

When a Quote expires, the Product may refresh price, revalidate strategy, recheck deadline, reconfirm provider, and issue a replacement version.

The expired version remains auditable.

An attempted acceptance after expiry may be pending revalidation, rejected, accepted under an authorized exception, or require a replacement Quote.

---

## 17. Purchase Order Is Not Universal Proof of Scope

A purchase order may identify amount, reference, procurement authority, payer, and cost center.

It may not contain the full trademark scope or filing authority.

The Product should reconcile the purchase order with the Quote and Commercial Instruction.

---

## 18. Payment Does Not Cure Missing Acceptance

A payment may support evidence of commercial intent.

It does not automatically resolve scope mismatch, wrong Quote version, applicant uncertainty, filing approval, legal authority, or document deficiency.

Payment and acceptance should be reconciled, not collapsed.

---

## 19. AI May Support Commercial Reconciliation

AI may compare accepted scope to Quote, identify conditions, extract purchase-order details, detect version mismatch, prepare amendments, and summarize open dependencies.

AI should not infer authority without evidence, accept on behalf of a party, waive expired terms, expand scope, create filing approval, or interpret ambiguous payment as complete instruction.

---

## 20. Failure Modes to Reject

```text
Proposal selection treated as acceptance
Acceptance linked to wrong Quote version
Expired Quote accepted silently
Payment treated as filing approval
Commercial instruction treated as provider instruction
Account owner assumed authorized
Partial acceptance expanded to full scope
Scope changed without amendment
Cancellation assumed to withdraw official rights
AI grants commercial exception
```

---

## 21. Minimum Quote and Instruction Lock

```text
A Quote is a versioned commercial offer.

Acceptance identifies the exact version,
scope, party, authority, method, and conditions.

Commercial Instruction requests work
under the accepted terms.

Quote, acceptance, payment,
commercial instruction, Order,
Matter, filing approval,
provider instruction, submission,
and official outcome remain distinct.

Authorized humans and organizations bind.

MarkReg prepares, records, and hands off.
```

---

## 22. Handoff to Formal Intake

A commercially instructed journey can now enter Formal Intake.

The next chapter defines what information must be collected, verified, versioned, and declared sufficient for the selected service without forcing every user through one universal form.
