# B05-CH-21 — Validation, Readiness and Missing Information

**Status:** Part III Draft  
**Chapter Map:** B05-TOC-V0.1  
**Part:** Part III — Commercial Journey and Formal Intake

## Chapter Purpose

Part III has now produced a proposal, price model, Quote, acceptance, Commercial Instruction, Formal Intake, and document and signature states.

The next question is not simply whether the form is complete.

It is:

> Ready for which next action, under which scope, authority, version, deadline, and unresolved conditions?

```text
Readiness
=
Purpose-Specific Validation
across
Commercial
Information
Identity
Authority
Professional
Document
Payment
Provider
Deadline
Execution
Filing
dimensions
```

```text
Complete
≠ Correct
≠ Reviewed
≠ Approved
≠ Paid
≠ Filing Ready
≠ Submitted
```

---

## 1. Readiness Is Purpose-Specific

A journey may be ready for commercial review, client decision, professional review, document signature, payment request, Order creation, Matter creation, filing approval, provider appointment, Execution scheduling, or submission.

It may be ready for one and not another.

---

## 2. Structural Validation Is the Lowest Layer

Structural checks may confirm required field present, date format, identifier format, file readability, class number, numeric amount, or signature block.

Structural validity does not establish professional correctness.

---

## 3. Semantic Validation Checks Meaning

Examples include:

- applicant name matches entity record;
- mark description matches representation;
- class relates to specification;
- priority applicant matches;
- route eligibility aligns with applicant and base right;
- POA scope covers action.

Semantic checks may require rules and human interpretation.

---

## 4. Commercial Readiness

Commercial readiness may require valid Quote, accepted scope, Commercial Instruction, pricing approval, discount approval, payment terms, credit or procurement approval, and cancellation terms.

Commercial readiness does not establish filing readiness.

---

## 5. Information Readiness

Information readiness may require filing unit, applicant, address, entity data, signatory, route, priority, classes, goods/services, use data, and contact information.

The required set is jurisdiction- and service-specific.

---

## 6. Identity and Authority Readiness

This dimension checks applicant identity, current owner, signatory identity, signatory capacity, instructor authority, payer identity, representative authority, and provider appointment.

An account login is not sufficient.

---

## 7. Professional Readiness

Professional readiness may require review of jurisdiction strategy, filing route, filing unit, applicant, classes, specification, search and risk, priority, mark description, disclaimers, and local requirements.

The Product may prepare. An eligible human decides professional sufficiency.

---

## 8. Document Readiness

Document readiness should identify required, received, correct type, correct version, signed, certified, translated, original available, reviewed, and accepted for defined use.

An uploaded document is not automatically ready.

---

## 9. Payment Readiness

Payment readiness may mean no payment required yet, payment request issued, deposit received, official-fee advance received, credit approved, payment reconciled, provider funds available, or variance within tolerance.

Paid does not mean approved for filing.

---

## 10. Provider Readiness

Provider readiness may require provider need defined, private partner checked, capability evidence, conflict cleared, price confirmed, availability confirmed, Human Selection, appointment prepared, instruction approved, and provider accepted.

A recommended provider is not ready merely because it appears first.

---

## 11. Deadline Readiness

Deadline readiness should preserve source, event, calculated date, official date, time zone, extension, uncertainty, verification, responsible person, and safety margin.

A calculated deadline may require official confirmation.

---

## 12. Filing Readiness Is a Composite Gate

```text
Filing Readiness
=
Approved Scope
+ Approved Filing Unit
+ Approved Applicant
+ Approved Specification
+ Required Documents
+ Required Authority
+ Commercial Condition
+ Payment Condition
+ Provider or Connector Condition
+ Verified Deadline Context
+ Execution Entry Condition
```

The exact formula is jurisdiction- and service-specific.

---

## 13. Blocker, Warning and Condition Must Differ

```text
Blocker
→ progression prohibited

Warning
→ progression allowed with visible risk or acknowledgement

Condition
→ progression depends on a later or external event

Recommendation
→ improvement suggested but not mandatory

Information
→ context only
```

Color alone should not carry the meaning.

---

## 14. Overrides Need Authority

An override should identify rule, reason, decision-maker, authority, affected scope, risk, expiry, evidence, and version.

Some blockers should not be overridable inside MarkReg.

---

## 15. Readiness Should Be Versioned and May Expire

A readiness result depends on exact versions of scope, filing unit, applicant, specification, documents, Quote, acceptance, payment, provider, and rule pack.

It may expire because fees, documents, search, provider availability, deadline, applicant, official rules, signature package, or payment conditions changed.

The Product should show checked time and invalidation reason.

---

## 16. Missing Information Needs an Owner and Resolution Path

Each missing item should identify:

- description;
- why needed;
- owner;
- due date;
- source;
- acceptable evidence;
- blocker level;
- fallback;
- escalation;
- affected action.

A generic missing-information list is not enough.

---

## 17. Contradictions Need Resolution, Not Suppression

Examples include:

- accepted Quote says three classes while Intake says four;
- POA applicant differs from Intake;
- official record differs from client statement;
- payer references the wrong Matter;
- provider quote excludes a required stage.

The Product should create a resolution task or Review request.

---

## 18. Readiness Summary Should Be Explainable

A useful summary may show:

```text
Ready for commercial confirmation: YES
Ready for professional review: YES
Ready for filing approval: NO
Ready for provider appointment: CONDITIONAL
Ready for payment request: YES
Ready for submission: NO
```

Each result should open to underlying checks.

---

## 19. A Score May Supplement but Not Replace Gates

A percentage may support prioritization.

It should not hide one critical blocker, unresolved authority, expired document, unpaid official fee, or unreviewed specification.

Gate meaning remains primary.

---

## 20. AI May Assist Validation

AI may detect missing items, compare versions, identify contradictions, explain blockers, recommend resolution, generate readiness summaries, and route questions.

AI should not waive blockers, establish authority, approve filing, decide professional sufficiency, mark payment reconciled, or declare official acceptance.

---

## 21. Failure Modes to Reject

```text
One completion percentage used for every action
Uploaded file treated as document-ready
Paid treated as filing-ready
Recommended provider treated as appointed
Calculated deadline treated as verified
Warning and blocker mixed
Override without authority
Material change does not invalidate readiness
AI approves filing
Unknown status shown as ready
```

---

## 22. Minimum Readiness Lock

```text
Readiness is defined for a purpose.

It is evaluated across several dimensions.

Complete, correct, reviewed,
approved, paid, appointed,
filing-ready, submitted,
and officially acknowledged remain distinct.

Blockers, warnings, conditions,
recommendations, and information
retain different effects.

AI may validate and explain.

Authorized humans and formal services
review, approve, override, reconcile,
and execute.
```

---

## 23. Handoff to Formal Object Formation

The output is a versioned Readiness Assessment with explicit blockers, warnings, conditions, owners, and next actions.

The final chapter of Part III defines how the accepted commercial journey and sufficient Intake hand into formal Order, Matter, payment, responsibility, and Execution contexts without duplicating authority.
