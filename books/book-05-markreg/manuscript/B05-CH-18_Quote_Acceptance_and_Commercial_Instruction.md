# B05-CH-18 — Quote, Acceptance and Commercial Instruction

**Status:** Complete Draft 1  
**Chapter Map:** B05-TOC-V0.1 — Owner Accepted  
**Part:** Part III — Commercial Journey and Formal Intake

## Chapter Purpose

CH17 prepared the price basis. This chapter defines how the selected option becomes `MR-A06 Quote`, how the exact commercial offer receives `MR-D01 Client Acceptance`, and how `MR-A07 Commercial Instruction` authorizes preparation without becoming Filing Approval, provider instruction or submission authority.

The `EMBERLOOP` reference step is `EL-11`.

## 1. Product Question

> What exactly is being accepted, who is authorized to accept it, and what work may begin next?

The interface must distinguish viewing, selecting, accepting, paying and instructing.

```text
Proposal selection
→ Quote
→ Client Acceptance
→ Commercial Instruction
```

None of these actions alone creates Filing Approval or official effect.

## 2. Quote Contract

A conforming Quote identifies:

- quoting organization and commercial recipient;
- linked Proposal option and versions;
- exact jurisdictions, filing units, classes, items and stages;
- client price, currencies, tax and payment schedule;
- inclusions, exclusions and later-stage fees;
- official-fee and exchange-rate treatment;
- assumptions and dependencies;
- validity and expiry conditions;
- cancellation and refund policy;
- issuer and required commercial approvals;
- stable Quote ID and version.

The accepted offer must remain reproducible. A Quote is immutable after issuance; changes create a replacement or amendment.

## 3. Commercial Authority

Quote issuance may require pricing, tax, credit, provider-cost, discount, margin or unusual-scope approval.

AI may draft, compare and check a Quote. It may not issue binding terms, approve credit, waive exclusions or extend validity without an authorized actor or policy-controlled service.

## 4. Client Acceptance Contract

Client Acceptance retains:

| Field | Meaning |
| --- | --- |
| Quote reference | exact ID and version |
| accepted scope | full scope or exact subset |
| accepting actor | person and represented organization |
| authority basis | role, mandate, procurement process or delegation |
| method | authenticated portal, signed record, email, purchase order or other evidence |
| timestamp | effective acceptance time |
| conditions | outstanding dependencies or exceptions |
| evidence | source linked to the Quote |

Silence, page views, downloads, questions, option selection or unmatched payment are not acceptance.

`MR-SCN-06` requires an expired Quote to be blocked from silent acceptance and either revalidated through authorized extension or replaced.

## 5. Partial and Conditional Acceptance

The client may accept only selected jurisdictions, filing units, classes, items, search stages, service stages or portfolio waves.

Conditions may include:

- applicant confirmation;
- provider availability;
- final search;
- POA or declaration;
- payment;
- internal budget approval;
- deadline verification.

The accepted subset is recorded exactly. Partial acceptance must not expand to the full Proposal.

## 6. Commercial Instruction

Commercial Instruction answers:

> What preparation work is the organization authorized to begin under the accepted commercial scope?

It records:

- accepted Quote and scope;
- authorized instructor;
- requested start condition;
- priority and target date;
- payer and billing route;
- required participants;
- dependencies and permitted variations;
- requested formalization or workflow entry.

Commercial Instruction may authorize intake, document preparation or professional work. It does not authorize:

- the final Filing Package;
- official-fee payment;
- provider instruction;
- external submission;
- an official communication.

## 7. Payment Relationship

Payment is reconciled against the Quote, Order or financial reference. It does not cure:

- expired or missing acceptance;
- wrong scope;
- applicant uncertainty;
- incomplete Professional Review;
- missing Filing Approval;
- invalid Documents.

`MR-SCN-08` requires commercial, payment, professional and approval states to remain separate.

## 8. Change, Cancellation and Withdrawal

A change is classified as:

```text
Non-Material Clarification
Commercial Amendment
Professional-Scope Amendment
Replacement Quote Required
New Acceptance Required
New Filing Approval Required
```

The current accepted version remains immutable. Cancellation records the actor, authority, affected scope, work performed, committed costs, refund treatment and rights consequences.

Cancelling commercial work does not withdraw an official application. Withdrawal requires a separate authorized External Protected Action.

## 9. Reference Journey — `EL-11`

The client receives Quote v3 for `EMBERLOOP` Option B: word and device filings in US, EU and UK.

Quote v3 states:

- six filing-unit/jurisdiction combinations;
- class and item assumptions;
- official, professional and provider components;
- deposit requirement;
- validity and fee-variance treatment;
- excluded office-action and registration-stage fees;
- cancellation and refund terms.

An authorized client actor accepts Quote v3 and issues Commercial Instruction v1. One US declaration and final goods revision remain conditions.

Preparation may begin. Filing Approval has not occurred.

## 10. User Surface

Show:

1. exact Quote version;
2. accepted and excluded scope;
3. payable amount and schedule;
4. validity and conditions;
5. accepting organization and authority check;
6. effect of the action;
7. separate actions for `Accept`, `Accept and Instruct`, `Request Revision` and `Decline`;
8. gates that remain closed after instruction.

## 11. Failure Modes

Reject:

```text
Option selection treated as acceptance
Acceptance linked to the wrong Quote version
Expired Quote silently accepted
Partial acceptance expanded to full scope
Payment treated as Filing Approval
Commercial Instruction treated as provider instruction
Account login treated as authority
Scope changed without amendment
AI grants a commercial exception
```

## 12. Chapter Output and Handoff

CH18 produces:

```text
MR-A06 Quote
+ MR-D01 Client Acceptance
+ MR-A07 Commercial Instruction
```

CH19 uses these exact versions to request only the service-specific facts still required for `MR-A08 Formal Intake`.