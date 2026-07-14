# B05-CH-22 — Order, Matter, Payment and Responsibility Handoff

**Status:** Productized Draft  
**Chapter Map:** B05-TOC-V0.1 — Owner Accepted  
**Part:** Part III — Commercial Journey and Formal Intake

## Chapter Purpose

CH21 produced purpose-specific readiness decisions. This chapter prepares the `Handoff Envelope` used to request formal Order, Matter, payment, responsibility and Execution contexts without renaming Product state as formal truth.

The controlling rules are:

- `MR-CR-03` — Approval is not execution;
- `MR-CR-07` — Product-local artifacts do not silently become formal shared objects;
- `MR-CR-08` — every material artifact preserves lineage, responsibility and supersession.

## 1. User Question

> What happens after commercial confirmation, which formal records will be created, who becomes responsible, and what evidence should return?

The Product must explain formalization as a controlled handoff, not as an invisible transition to “filed.”

## 2. Handoff Envelope Contract

A `Handoff Envelope` must contain stable references to:

- accepted Quote and Commercial Instruction;
- Formal Intake and Requirement Set;
- Readiness Assessment;
- service, jurisdiction, route and filing unit;
- applicant or right holder;
- approved and unresolved scope;
- commercial and payment conditions;
- required formal objects;
- intended responsibility assignments;
- deadline context;
- provider or connector need;
- expected return identifiers and evidence;
- idempotency key and reconciliation owner.

It carries references and decisions. It does not itself create the formal objects.

## 3. Formal Object Boundaries

| Object or context | Primary meaning |
| --- | --- |
| Order | commercial commitment, price and terms |
| Matter | professional work context and confidentiality |
| Financial record | invoice, receipt, payment, refund and reconciliation |
| Responsibility assignment | accountable role, scope and trigger |
| Document | formal controlled document record |
| Execution Context | governed work and protected-action entry context |

The applicable Owning Service creates and records each formal fact. MarkReg retains the returned reference and Product projection.

## 4. Commercial and Professional Decomposition

A commercial package may create several professional Matters.

Examples:

```text
One Order
→ US word Matter
→ US device Matter
→ EU word Matter
→ EU device Matter
→ UK word Matter
→ UK device Matter
```

A search may be a separate Matter. A later office action may create new commercial events while remaining related to the filing Matter.

The Product must not force one Order to equal one Matter.

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

Material responsibilities may include:

- commercial owner;
- professional owner;
- coordinator;
- reviewer and approver;
- deadline owner;
- document owner;
- provider manager;
- client decision owner;
- finance owner.

Assignment must identify actor or organization, role, authority, scope, start trigger, expected action, escalation and completion evidence.

Copying someone on a message does not assign responsibility. AI cannot be the accountable professional.

## 7. Execution Entry

The Execution Context may reference formal Order and Matter IDs, accepted Product artifacts, documents, deadlines, permissions and responsibilities.

Book 03 governs coordinated Execution. Creation of an Execution Context may permit task formation; it does not automatically:

- instruct a provider;
- pay an official fee;
- send a communication;
- submit a filing;
- record an official outcome.

Protected actions retain their own approval and execution gates.

## 8. Idempotency and Partial Failure

Every formalization request must carry a stable idempotency key.

Possible outcomes include:

```text
Order created; Matters pending
Matter created; payment pending
Payment received; reconciliation pending
Responsibility assigned; provider pending
Execution Context created; Filing Approval pending
Formalization rejected; no object created
Result unknown; reconciliation required
```

Partial success must remain visible. A retry must reuse or reconcile existing references rather than create duplicate Orders, Matters, invoices, Tasks or later submissions.

## 9. Return Evidence

The handoff should expect typed return evidence such as:

- formal object ID and creation time;
- accepted or rejected request;
- validation error;
- payment or reconciliation state;
- assigned responsible actor;
- Execution Context reference;
- event source and correlation ID.

The Product updates its projection from these events without becoming the authority for the formal record.

## 10. Cross-Organization Boundary

When client, agency and provider organizations participate:

- each retains identity and records;
- permissions remain purpose-limited;
- responsibility is explicitly accepted;
- private data is not broadly shared;
- one organization’s authority is not automatically transitive.

Provider discovery, selection, appointment, instruction and acceptance remain separate stages for Part IV.

## 11. EMBERLOOP Reference Journey

After the deposit is reconciled, the US declaration is completed, the revised goods wording is reviewed, and the final readiness gate passes, MarkReg creates Handoff Envelope v1.

It references:

- Quote v3;
- Client Acceptance and Commercial Instruction v1;
- Formal Intake v4;
- Requirement Set v2;
- Readiness Assessment v5;
- responsible professional;
- one non-blocking warning;
- expected Order, six filing Matters and Execution Context references.

The returned Order and Matter identifiers become visible. The journey is now ready for filing-package preparation—not filed and not submitted.

## 12. Conformance Scenario — Duplicate Handoff

**Given** an Order-creation request succeeded but the response timed out.  
**When** the Product retries the Handoff Envelope.  
**Then** the Owning Service uses the idempotency key to return the existing Order reference or a reconciliation result instead of creating a duplicate.  
**Authority boundary:** MarkReg requests and reconciles; the Owning Service owns the Order.  
**Evidence retained:** both attempts, correlation key, formal reference, response state and reconciliation decision.

## 13. User Surface

The Handoff surface should show:

1. accepted scope and exact versions;
2. gates satisfied and unresolved warnings;
3. formal records requested;
4. responsibility assignments;
5. payment condition;
6. current handoff result per object;
7. failures and retry state;
8. expected next evidence;
9. clear statement that filing has not yet occurred.

The primary action is `Authorize Permitted Handoff` or resolve the remaining gate.

## 14. AI Boundary

AI may decompose commercial scope, prepare mappings, suggest responsibility roles, detect missing references, explain partial results and identify likely duplicates.

AI may not create authority, assign final accountability, reconcile funds as final, approve filing, instruct providers or submit externally.

## 15. Failure Modes

The Product must reject:

```text
Product status renamed as Order
Order used as Matter
One Order forced into one Matter
Payment treated as Filing Approval
Payer treated as applicant
Email copy treated as responsibility assignment
Retry creates duplicate formal objects
Partial formalization shown as complete
Matter creation sends provider instruction
Execution Context creation submits filing
```

## 16. Part III Output

Part III now produces the governed sequence:

```text
Proposal
→ Price Basis
→ Quote
→ Client Acceptance
→ Commercial Instruction
→ Formal Intake
→ Requirement Set
→ Readiness Assessment
→ Handoff Envelope
→ Formal References Returned
```

This sequence is ready to support Part IV, subject to the follow-up CH00–CH22 whole-draft review and explicit gate decision.

Part IV begins with the Filing Package Candidate as a governed artifact, version-specific professional review and Filing Approval.