# B05-CH-27 — Direct Connector, Provider Filing and Owning Service Boundaries

**Status:** Part IV Draft  
**Chapter Map:** B05-TOC-V0.1 — Owner Accepted  
**Part:** Part IV — Filing Preparation and Governed Execution

## Chapter Purpose

CH26 produces an accepted provider instruction or an approved direct route.

CH27 answers:

> Which system or professional may perform the protected filing action, what does MarkReg coordinate, and where do credentials, formal records, funds and official authority remain?

```text
Approved package
+ permitted execution route
+ credentials and authority
+ Book 03 governed Execution
→ protected action attempt
→ returned evidence
```

MarkReg prepares and projects the Product journey. It does not become every filing-capable service.

---

## 1. User Question and Primary Action

**User question:** Through which approved route will this package be filed, and who controls the actual external action?

**Primary action:** Start or authorize the permitted execution step only when all route-specific conditions are satisfied.

The Product should identify the actor and effect before exposing a filing action.

---

## 2. Execution Route Types

Possible routes include:

| Route | Protected-action actor |
| --- | --- |
| direct office connector | authorized connector or filing service using controlled credentials |
| external provider filing | appointed provider or eligible professional |
| internal professional filing | eligible professional under organization credentials |
| Owning Service filing | formal filing-capable service that owns the transaction record |
| assisted manual filing | eligible Human using an official portal under governed Task and evidence return |
| unavailable | no approved route currently satisfies the requirements |

A route label must not conceal who actually performs the action.

---

## 3. MarkReg Responsibility

MarkReg may:

- prepare and display the approved package;
- identify route requirements;
- request governed Execution;
- carry stable references and approvals;
- show route state and returned evidence;
- reconcile Product projections;
- explain next actions.

MarkReg does not automatically own credentials, official accounts, filing transactions, formal Documents, funds, provider engagement or office records.

---

## 4. Book 03 Execution Responsibility

Book 03 governs:

- Task and Workflow execution;
- approvals and protected-action gates;
- credential use;
- connector invocation;
- retries and compensation;
- Communications;
- Events and audit;
- return evidence.

Book 05 defines the MarkReg Product contract consumed by that governed execution. It does not create a second Workflow engine.

---

## 5. Direct Connector Boundary

A direct connector may:

- authenticate to an office or authorized intermediary;
- validate a payload against connector rules;
- transmit data and files;
- initiate official-fee payment where authorized;
- receive technical and official responses.

A connector does not:

- decide applicant ownership;
- provide professional advice;
- grant Filing Approval;
- create official acceptance before the office does;
- convert a technical success into legal success.

---

## 6. Connector Credentials

Credentials must remain controlled by their owner and purpose.

The execution record should identify:

- credential owner;
- permitted user or service;
- office and environment;
- scope;
- authentication time;
- secret-management boundary;
- expiry;
- action performed;
- result.

Credentials must not be copied into the Filing Package or exposed to clients and providers.

---

## 7. Provider Filing Boundary

An appointed provider may:

- review local filing feasibility;
- prepare office-specific forms;
- submit under its credentials and professional authority;
- pay official fees under agreed terms;
- receive office correspondence;
- return filing and acknowledgement evidence.

The provider remains accountable for the actions it accepts. MarkReg and the instructing organization retain their own responsibilities.

---

## 8. Owning Service Boundary

A filing-capable Owning Service may own:

- formal filing transaction;
- connector request and result;
- fee payment record;
- official identifier and acknowledgement evidence;
- formal Document or Communication records;
- retry and reconciliation state.

MarkReg consumes references and Events. It should not create competing formal truth by copying those records without provenance.

---

## 9. Official Office Boundary

The official office controls:

- official receipt;
- filing date where granted;
- application number;
- fee acceptance;
- formal requirements;
- examination and status;
- rejection, correction and later outcomes.

Neither connector success nor provider statement overrides official evidence.

---

## 10. Route Selection Inputs

The permitted route depends on:

- jurisdiction-pack execution entry;
- applicant and representation rules;
- selected provider or internal professional;
- Filing Approval scope;
- document and original status;
- payment condition;
- credential availability;
- office availability;
- deadline;
- package schema and file limits;
- organization policy.

A route may become unavailable after approval and require renewed routing.

---

## 11. Payload Transformation

The approved package may need transformation into:

- connector JSON or XML;
- official portal fields;
- local-language form;
- provider worksheet;
- file bundle;
- payment instruction.

Transformation must preserve source lineage and create a reviewable diff where meaning may change.

Technical mapping must not silently alter legal scope.

---

## 12. Pre-Execution Validation

Immediately before protected action, Execution should verify:

1. approved package version;
2. approval validity;
3. route and actor authority;
4. credential availability;
5. provider acceptance where applicable;
6. official-fee and payment condition;
7. required Documents and originals;
8. jurisdiction-pack and connector version;
9. deadline and office availability;
10. idempotency key and prior attempts.

A stale earlier readiness result is insufficient by itself.

---

## 13. Manual Filing Is Still Governed

A Human using an official web portal is not outside the architecture.

The Task should preserve:

- approved package;
- responsible professional;
- portal and credential boundary;
- entered values or screenshots where permitted;
- fees paid;
- submission action time;
- returned receipt or error;
- unresolved reconciliation.

Manual does not mean unaudited.

---

## 14. Route Change During Execution

If a connector fails and a provider route is proposed, MarkReg must determine:

- whether Filing Approval covered the alternative;
- whether provider selection and appointment are complete;
- whether fees changed;
- whether package transformation changed meaning;
- whether deadline and duplicate risk permit the switch;
- which new approvals are required.

A failed route does not authorize any available route automatically.

---

## 15. `EMBERLOOP` Reference Journey

The `EMBERLOOP` US word-mark package uses the accepted private provider route.

The EU filing uses an approved Owning Service with a supported connector. The UK filing uses an internal eligible professional through the official portal.

MarkReg displays the three routes in one Product journey while retaining separate:

- Filing Approvals;
- credentials and actors;
- fee-payment records;
- execution attempts;
- returned evidence;
- official identifiers.

---

## 16. Conformance Scenario — Connector Technical Success Without Receipt

**Given** a connector reports HTTP success after transmitting an approved EU package.  
**When** no official receipt or application number is returned.  
**Then** the execution state is `sent — acknowledgement unknown`, duplicate submission is blocked, and reconciliation begins before retry.  
**Authority boundary:** technical transport success is not official acceptance.  
**Evidence retained:** payload hash, connector response, timestamps, idempotency key, payment state and reconciliation actions.

---

## 17. AI Assistance

AI may:

- map package fields to route schemas;
- compare transformed payloads;
- identify missing route prerequisites;
- explain technical errors;
- propose safe escalation;
- summarize returned evidence.

AI may not access uncontrolled credentials, choose an unauthorized route, approve a meaning-changing transformation, commit funds, instruct a provider, or perform protected external action without governed authority.

---

## 18. Minimum Chapter Lock

```text
MarkReg owns the focused Product journey.
Book 03 governs Execution.
Connectors transmit under controlled credentials.
Providers file under accepted engagement.
Owning Services record formal transaction facts.
Official offices control official outcomes.

A technical success is not official receipt.
A route failure does not authorize another route.
Manual filing remains governed and auditable.
```

---

## 19. Handoff to CH28

CH27 establishes who may perform the filing action and through which route.

CH28 defines the submission-state model, technical and provider responses, official acknowledgement, application identifiers, corrections, rejection and official evidence.