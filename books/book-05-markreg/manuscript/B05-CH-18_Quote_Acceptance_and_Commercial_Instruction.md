# B05-CH-18 — Quote, Acceptance and Commercial Instruction

**Status:** Productized Draft  
**Chapter Map:** B05-TOC-V0.1 — Owner Accepted  
**Part:** Part III — Commercial Journey and Formal Intake

## Chapter Purpose

CH17 established a transparent price basis. This chapter defines how a selected option becomes a versioned `Quote`, how the exact commercial offer is accepted, and how an authorized `Commercial Instruction` requests work without becoming filing approval or provider instruction.

The canonical lineage is:

```text
Proposal Option
→ Quote
→ Client Acceptance
→ Commercial Instruction
→ Formalization Trigger Candidate
```

## 1. User Question

> What exactly am I accepting, who is authorized to accept it, and what work will begin next?

The interface must state the legal and operational effect of every action. Viewing, selecting, paying, accepting and instructing are not interchangeable events.

## 2. Quote Contract

A Quote must identify:

- quoting organization and commercial recipient;
- linked Proposal option and versions;
- exact jurisdictions, filing units, classes, items and stages;
- prices, currencies, tax and payment schedule;
- inclusions, exclusions and later-stage fees;
- official-fee and exchange-rate treatment;
- assumptions and dependencies;
- validity and expiry conditions;
- cancellation and refund policy;
- issuer and commercial approvals;
- stable Quote ID and version.

It must be possible to reproduce exactly what was offered and accepted.

## 3. Commercial Authority

Quote issuance may require:

- pricing approval;
- provider-cost verification;
- discount or margin approval;
- tax review;
- credit approval;
- unusual-scope approval.

AI may draft and check a Quote. It may not issue binding terms without the organization’s authorized actor or policy-controlled service.

## 4. Acceptance Contract

`Client Acceptance` must retain:

| Field | Meaning |
| --- | --- |
| Quote reference | exact ID and version |
| Accepted scope | full or selected subset |
| Accepting actor | person and represented organization |
| Authority basis | role, mandate, purchase process or delegated authority |
| Method | authenticated portal, signed document, email, PO or other evidence |
| Timestamp | effective acceptance time |
| Conditions | outstanding dependencies or exceptions |
| Evidence | source record linked to the Quote |

Silence, page views, downloads, questions, option selection or unmatched payment are not automatically acceptance.

## 5. Partial and Conditional Acceptance

The client may accept only selected:

- jurisdictions;
- filing units;
- classes or goods/services scope;
- search stages;
- portfolio waves;
- professional services.

Conditions may include applicant confirmation, provider availability, final search, POA, payment, internal budget approval or deadline verification.

MarkReg must preserve the accepted subset. It must not expand partial acceptance to the full Proposal.

## 6. Commercial Instruction

A `Commercial Instruction` answers:

> What work is the organization authorized to begin under the accepted commercial scope?

It should identify:

- accepted Quote and scope;
- authorized instructor;
- requested start condition;
- priority and target date;
- payer and billing route;
- required participants;
- dependencies and authorized variations;
- requested formal objects or workflow entry.

Commercial Instruction may authorize preparation work. It does not authorize the final Filing Package, official-fee payment, provider instruction or submission.

## 7. Payment Relationship

Payment is reconciled against the Quote, Order or other financial reference. It does not cure:

- expired or missing acceptance;
- wrong scope;
- applicant uncertainty;
- professional deficiency;
- missing filing approval;
- invalid documents.

The Product may show both commercial acceptance and payment state without combining them.

## 8. Scope Change After Acceptance

A requested change must be classified:

```text
Non-Material Clarification
Commercial Amendment
Professional-Scope Amendment
Replacement Quote Required
New Acceptance Required
New Filing Approval Required
```

The current accepted version remains immutable. A change creates a new version or amendment and identifies downstream artifacts affected.

## 9. Cancellation and Withdrawal

A cancellation record must identify:

- requesting actor and authority;
- affected scope;
- timing;
- work performed;
- official or provider commitments;
- refundable and non-refundable components;
- deadline or rights consequences.

Cancelling commercial work does not withdraw an official application unless a separately authorized external action occurs.

## 10. EMBERLOOP Reference Journey

The client receives Quote v3 for Proposal Option B: word and device filings in US, EU and UK.

The Quote states:

- exact six filing-unit/jurisdiction combinations;
- classes and item assumptions;
- official, professional and provider components;
- deposit requirement;
- quote validity;
- excluded office-action and registration-stage fees;
- fee-variance and cancellation treatment.

An authorized client actor accepts Quote v3 and issues Commercial Instruction v1. One US declaration and final goods revision remain conditions. The organization may begin preparation, but filing approval has not occurred.

## 11. Conformance Scenario — Expired Quote

**Given** a Quote has passed its validity date.  
**When** the client attempts to accept it.  
**Then** MarkReg prevents silent acceptance, preserves the attempted action, checks fee and scope validity, and requires an approved extension or replacement Quote.  
**Authority boundary:** the Product cannot extend commercial validity by itself.  
**Evidence retained:** expired Quote, attempted acceptance, revalidation, approver and replacement version.

## 12. User Surface

The acceptance surface must show:

1. exact Quote version;
2. selected scope and excluded scope;
3. payable amount and payment schedule;
4. validity and conditions;
5. accepting organization and authority check;
6. effect of the action;
7. separate controls for `Accept`, `Accept and Instruct`, `Request Revision` or `Decline`.

After instruction, the Product explains which preparation may start and which gates remain closed.

## 13. Failure Modes

The Product must reject:

```text
Option selection treated as acceptance
Acceptance linked to the wrong Quote version
Expired Quote silently accepted
Partial acceptance expanded to full scope
Payment treated as filing approval
Commercial instruction treated as provider instruction
Account login treated as authority
Scope changed without amendment
AI grants a commercial exception
```

## 14. Chapter Output

The output is an accepted, version-specific commercial scope and an authorized Commercial Instruction with explicit conditions.

The next chapter collects only the service-specific facts still required to prepare and review that accepted scope.