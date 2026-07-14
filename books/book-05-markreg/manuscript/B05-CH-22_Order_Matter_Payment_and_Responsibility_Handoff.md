# B05-CH-22 — Order, Matter, Payment and Responsibility Handoff

**Status:** Complete Draft 1  
**Chapter Map:** B05-TOC-V0.1 — Owner Accepted  
**Part:** Part III — Commercial Journey and Formal Intake

## Chapter Purpose

CH21 produced purpose-specific readiness results. This chapter prepares `MR-A12 Handoff Envelope`, which requests formal Order, Matter, payment, responsibility and Execution contexts without renaming Product state as formal truth.

The `EMBERLOOP` reference step is `EL-15`.

```text
Handoff request
≠ formal object created
≠ provider instructed
≠ filing submitted
```

## 1. Product Question

> What happens after commercial confirmation, which formal records are requested, who becomes responsible, and what evidence must return?

Formalization must be visible as a controlled Handoff rather than an invisible transition to `filed`.

## 2. Handoff Envelope Contract

A conforming Handoff Envelope contains stable references to:

- accepted Quote and Commercial Instruction;
- Formal Intake and Requirement Set;
- Readiness Assessment;
- service, jurisdiction, route and filing unit;
- applicant or right holder;
- approved, unresolved and excluded scope;
- commercial and payment conditions;
- required formal objects;
- intended responsibility assignments;
- deadline context;
- provider or connector need;
- expected return identifiers and Evidence;
- idempotency key and reconciliation owner.

The Envelope carries references and Decisions. It does not create the formal objects itself.

## 3. Formal Object Boundaries

| Formal object or context | Primary meaning |
| --- | --- |
| Order | commercial commitment, price and terms |
| Matter | professional work context and confidentiality |
| financial record | invoice, receipt, payment, refund and reconciliation |
| responsibility assignment | accountable role, scope and trigger |
| Document | formal controlled Document record |
| Execution Context | governed work and protected-action entry context |

The applicable Owning Service creates each formal fact. MarkReg retains the returned reference and a Product Projection.

## 4. Commercial and Professional Decomposition

One commercial Order may support several Matters:

```text
one Order
→ US word Matter
→ US device Matter
→ EU word Matter
→ EU device Matter
→ UK word Matter
→ UK device Matter
```

Search, examination response or dispute work may require separate Matters and later commercial events.

```text
Order ≠ Matter
```

## 5. Payment Context

The Product distinguishes:

```text
Quote Amount
Invoice Amount
Amount Due
Amount Received
Amount Reconciled
Amount Remitted
Refund Amount
```

Payer, applicant and client may be different parties. Payment references must not alter applicant identity.

Financial Owning Services remain authoritative for invoices, receipts, reconciliation, refunds and accounting.

## 6. Responsibility Assignment

Responsibilities may include:

- commercial owner;
- Professional Owner;
- coordinator;
- reviewer and approver;
- deadline owner;
- Document owner;
- provider manager;
- client Decision owner;
- finance owner.

An assignment records actor or organization, role, authority, scope, start trigger, expected action, escalation and completion Evidence.

Copying someone on a Communication does not assign responsibility. AI cannot be the accountable professional.

## 7. Execution Entry

An Execution Context may reference formal Order and Matter IDs, accepted Product artifacts, Documents, deadlines, Permissions and responsibilities.

Book 03 governs coordinated Execution. Creating an Execution Context may permit Task formation; it does not automatically:

- instruct a provider;
- pay an official fee;
- send a Communication;
- submit a filing;
- create an official outcome.

Every protected action retains its own exact-version approval and Execution gate.

## 8. Idempotency, Partial Failure and Return

Every formalization request carries a stable idempotency key.

Possible results include:

```text
Order created; Matters pending
Matter created; payment pending
Payment received; reconciliation pending
Responsibility assigned; provider pending
Execution Context created; Filing Approval pending
Formalization rejected; no object created
Result unknown; reconciliation required
```

Partial success remains visible. A retry reconciles existing references rather than creating duplicate Orders, Matters, invoices, Tasks or later submissions.

`MR-SCN-25` applies when the same Handoff or Return Envelope is consumed twice. The receiving service returns the existing formal reference and creates no duplicate effect.

## 9. Return Evidence

The Handoff expects typed Return Evidence, including:

- formal object ID and creation time;
- accepted or rejected request;
- validation error;
- payment or reconciliation state;
- assigned accountable actor;
- Execution Context reference;
- source event and correlation ID.

MarkReg updates its projection from these events without becoming authority for the formal record.

## 10. Cross-Organization Boundary

Where client, agency and provider organizations participate:

- each retains its identity and records;
- access remains purpose-limited;
- responsibility requires explicit acceptance;
- private data is not broadly shared;
- one organization’s authority is not automatically transitive.

Provider discovery, selection, appointment, instruction and Provider Acceptance remain separate Part IV stages.

## 11. Reference Journey — `EL-15`

After deposit reconciliation, completion of the US declaration, Review of revised goods wording and passage of the permitted readiness gate, MarkReg prepares Handoff Envelope v1.

It references:

- Quote v3;
- Client Acceptance and Commercial Instruction v1;
- Formal Intake v4;
- Requirement Set v2;
- Readiness Assessment v5;
- responsible professional;
- one non-blocking warning;
- expected Order, six Matters and Execution Context references.

The Owning Services return Order and Matter identifiers. The journey is now ready for Filing Package preparation.

```text
formal references returned
≠ filed
≠ submitted
≠ officially acknowledged
```

## 12. User Surface

Show:

1. accepted scope and exact versions;
2. gates satisfied and unresolved warnings;
3. formal records requested;
4. responsibility assignments;
5. payment condition;
6. current result for each requested object;
7. failure, unknown and retry state;
8. expected Return Evidence;
9. a clear statement that filing has not occurred.

The primary action is `Authorize Permitted Handoff` or resolve the remaining gate.

## 13. AI Boundary

AI may decompose scope, prepare mappings, suggest responsibility roles, detect missing references, explain partial results and identify likely duplicates.

AI may not create authority, assign final accountability, reconcile funds as final, approve filing, instruct providers or submit externally.

## 14. Failure Modes

Reject:

```text
Product status renamed as Order
Order used as Matter
One Order forced into one Matter
Payment treated as Filing Approval
Payer treated as applicant
Communication recipient treated as responsibility owner
Retry creates duplicate formal objects
Partial formalization shown as complete
Matter creation sends provider instruction
Execution Context creation submits filing
```

## 15. Part III Output and Handoff to Part IV

Part III now produces:

```text
MR-A05 Proposal
→ source-backed price basis
→ MR-A06 Quote
→ MR-D01 Client Acceptance
→ MR-A07 Commercial Instruction
→ MR-A08 Formal Intake
→ MR-A09 Requirement Set
→ MR-A10 Readiness Assessment
→ MR-A12 Handoff Envelope
→ formal references returned
```

CH23 begins Part IV by preparing `MR-A11 Filing Package Candidate` from those exact versions and returned formal references.

Filing Package preparation still requires Professional Review, version-specific Filing Approval and governed Execution before any external submission.