# Chapter 07 — External Filing Requires Appointment, Acceptance and Evidence

International trademark filing often leaves the originating Workplace.

A local lawyer, trademark agent, filing provider, government portal or technical connector may become necessary. That external route creates the most dangerous illusion in professional software: the illusion that sending something means the intended legal act has occurred.

An email may be sent without being read. A Provider may receive instructions without accepting them. A connector may return technical success while the office rejects the payload. A lawyer may report filing before an official receipt exists. Payment may be made to the wrong beneficiary. The official record may remain unchanged.

MarkReg should govern external filing through a chain of explicit authority, accepted responsibility and typed evidence.

```text
Prepared and reviewed Package
→ Filing Approval
→ Capability Need
→ eligible route
→ Human selection
→ appointment authority
→ provider instruction
→ Provider Acceptance
→ external submission
→ Provider Return
→ official acknowledgement
→ Owning Service validation
```

## 1. Prepared does not mean executable

A complete Filing Package Candidate may still lack:

- customer Filing Approval;
- expenditure approval;
- Provider selection;
- conflict clearance;
- professional appointment;
- accepted engagement terms;
- POA;
- original documents;
- payment;
- an available submission channel;
- current office requirements.

```text
Package prepared
≠ Package approved
≠ Provider appointed
≠ filing submitted
```

## 2. External route begins with a Capability Need

The Product should express what external capability is required before searching for a provider.

The Capability Need may include:

- jurisdiction;
- service and lifecycle stage;
- local qualification requirements;
- filing deadline;
- mark and applicant context;
- classes and goods;
- document requirements;
- language;
- conflict and independence constraints;
- communication model;
- evidence and Return requirements;
- commercial constraints;
- customer-relationship restrictions.

A country name alone is not a sufficient Provider requirement.

## 3. Candidate, eligible, selected and appointed are distinct

Provider participation should progress through separate states:

```text
Known Provider
→ Candidate
→ Eligible Candidate
→ Recommended Route
→ Human Selection
→ Appointment Authorized
→ Instruction Sent
→ Provider Acceptance
```

### Candidate

A provider appears relevant based on geography, service or prior relationship.

### Eligible candidate

Current evidence supports jurisdiction, capability, conflict, status and route requirements.

### Recommended route

MarkReg or MGSN presents a reasoned route and alternatives.

### Human selection

An accountable actor chooses the route.

### Appointment authorized

The party with authority authorizes the engagement or representation.

### Provider Acceptance

The Provider confirms the exact scope, fees, deadline, documents and responsibility.

```text
Highest-ranked Provider
≠ selected Provider

Selected Provider
≠ appointed Provider

Instruction sent
≠ Provider accepted
```

## 4. Private and existing routes should remain available

The originating Workplace may prefer:

- its existing local agent;
- a customer-mandated lawyer;
- MarkReg's managed route;
- MGSN candidates;
- a direct official connector;
- an internal qualified professional;
- a self-managed external route.

MarkReg should not force network usage merely because the platform earns a margin.

The selected route should show:

- relationship source;
- eligibility basis;
- commercial interest;
- alternatives;
- responsibility and recovery model.

## 5. Conflict checks apply before appointment

Conflict review may consider:

- the applicant or owner;
- known adverse parties;
- related companies;
- prior rights identified by search;
- co-broker or partner relationships;
- confidentiality restrictions;
- existing Provider engagements;
- commercial self-interest.

A conflict signal is not always a proven conflict. Possible outcomes include:

```text
Cleared
Further Information Required
Information Barrier Required
Limited Scope Permitted
Consent or Waiver Required Where Lawful
Alternate Provider Required
Route Declined
```

## 6. The instruction package is a bounded contract

A Provider Instruction should identify:

- originating Workplace;
- contracting and relationship roles;
- customer or applicant represented;
- jurisdiction and service;
- exact Filing Package version;
- Filing Approval reference;
- required documents;
- deadlines and urgency;
- approved fee basis;
- communication rules;
- change-control rules;
- actions the Provider may take;
- actions requiring renewed approval;
- expected Return and evidence;
- confidentiality and data restrictions;
- exception and recovery route.

The Provider should not receive the entire Workplace or customer portfolio when the filing requires only a bounded context.

## 7. Provider Acceptance is substantive

A valid acceptance should confirm:

- Provider identity;
- acting professional where required;
- conflict status;
- accepted service scope;
- accepted Package version;
- fees and official-fee assumptions;
- deadline feasibility;
- document sufficiency;
- POA and original requirements;
- expected filing time;
- evidence to be returned;
- material exceptions.

A generic “received, thank you” may acknowledge delivery without accepting professional responsibility.

## 8. Provider changes cannot silently alter the approved Package

A Provider may identify that:

- goods wording is unacceptable;
- a document must be original;
- notarization is required;
- fees increased;
- a different filing basis applies;
- mark description should change;
- filing cannot occur by the expected deadline;
- another representative is needed.

Material changes should return to the relevant review and approval gates.

```text
Provider recommendation
≠ amended customer instruction

Additional fee identified
≠ additional fee approved
```

## 9. Direct connectors remain protected boundaries

A connector may transmit data to:

- an official office;
- a Provider portal;
- an approved filing service;
- a payment service;
- a document-signature service.

Technical success can establish:

- request transmitted;
- endpoint responded;
- file delivered;
- identifier returned.

It cannot establish by itself:

- professional validity;
- office acceptance;
- correct legal effect;
- provider appointment;
- registration or filing completion.

```text
HTTP success
≠ legal success
```

## 10. Submission states need precision

A governed sequence may include:

```text
Ready for execution
Queued
Transmission attempted
Sent
Delivered
Provider received
Provider accepted
Provider reports submitted
Technical receipt returned
Official acknowledgement received
Official record verified
Correction or rejection required
Unknown — reconciliation required
```

The Product should not compress these states into “filed” unless the supporting evidence and state definition are clear.

## 11. Evidence contracts should be defined before action

Before sending instructions, MarkReg should define expected evidence such as:

- Provider Acceptance;
- filing form or submitted payload;
- official submission receipt;
- application number;
- filing date;
- official-fee receipt;
- Provider invoice;
- filed goods and mark representation;
- POA submission record;
- screenshot or portal record where appropriate;
- official acknowledgement;
- exception report.

```text
Provider says “filed”
≠ evidence contract satisfied
```

## 12. Provider Return is typed

A Return should identify:

- originating Handoff and idempotency key;
- Provider;
- action performed;
- Package version used;
- changes made;
- submission state;
- evidence attached;
- official reference if available;
- fees actually incurred;
- warnings;
- unresolved issues;
- next action;
- communication required.

MarkReg should reconcile the Return against the approved instruction rather than merely attach the email to a Matter.

## 13. Official acknowledgement is a separate authority layer

The official office remains authoritative for official procedural events and records.

MarkReg should distinguish:

```text
Connector delivery
Provider report
Provider evidence
Official acknowledgement
Official record
Professional interpretation
Product projection
```

These may describe the same journey from different authority positions.

## 14. Unknown external state is first-class

Unknown state may arise when:

- a connector times out after submission;
- the Provider reports filing without evidence;
- payment is debited but no order confirmation appears;
- an application number is inconsistent;
- the official system is unavailable;
- duplicate submissions may exist;
- courier status and Provider receipt conflict.

The system should record:

- what was attempted;
- what evidence exists;
- what remains unknown;
- duplicate and deadline risk;
- reconciliation owner;
- escalation time;
- safe next action.

Blind retry is prohibited where a duplicate external effect is possible.

## 15. Idempotency and duplicate safety

External submissions should use an idempotency or correlation reference where the route supports it.

Before retrying, MarkReg should compare:

- prior instruction;
- transmission logs;
- Provider communication;
- payment records;
- official search;
- returned identifiers;
- time and deadline.

A safe retry decision should be recorded. The system should not reward fast retries that create duplicate applications or payments.

## 16. Payment is part of readiness, not proof of filing

Payment records may include:

- customer payment;
- Provider advance;
- official fee;
- professional fee;
- tax;
- currency conversion;
- credit or deposit;
- refund;
- variance.

```text
Customer paid
≠ Provider paid

Provider paid
≠ office fee paid

Office fee paid
≠ filing acknowledged
```

This chapter records payment checkpoints but does not authorize MarkOrbit to hold funds, operate escrow or automatically net amounts.

## 17. Communication responsibilities remain explicit

The service mode determines who communicates:

- Direct MarkReg Workplace;
- originating partner Workplace;
- co-delivery coordinator;
- appointed Provider;
- customer contact.

White-label delivery cannot conceal a professional identity that must be disclosed. A Provider should not acquire the customer relationship merely because direct communication becomes necessary.

## 18. Customer-facing status language

Prefer:

- “The application package has been approved and sent to the local agent.”
- “The local agent has accepted the instruction and is preparing submission.”
- “The agent reports submission; the official receipt is pending.”
- “The official filing receipt has been validated.”
- “The filing outcome remains uncertain while we reconcile the portal and Provider records.”

Avoid “completed” when the intended consequence is still pending.

## 19. AI's role

AI may:

- prepare Capability Needs;
- compare Provider evidence;
- detect conflicting fees or requirements;
- summarize instructions;
- draft Provider communications;
- reconcile returned fields;
- flag missing evidence;
- identify duplicate risk.

AI may not:

- select or appoint a Provider autonomously;
- clear conflicts;
- approve additional fees;
- change the Package;
- infer Provider Acceptance from silence;
- declare official filing;
- retry a protected action without authorization.

## 20. Example: original POA required after filing

A customer needs urgent filing in a jurisdiction where the Provider states that a scan can support initial submission but the original must follow within a defined period.

The governed route should record:

1. the Provider's current confirmation and source date;
2. the exact filing deadline;
3. the original-POA deadline;
4. customer confirmation that the original will be couriered;
5. scan validation;
6. Filing Approval;
7. Provider Acceptance;
8. official filing evidence;
9. courier dispatch and receipt;
10. Provider confirmation that the original was lodged;
11. exception escalation if the original is delayed.

The prior experience that an original was never sent should affect risk and communication without becoming a false universal rule.

## 21. Failure modes

External filing fails when:

- a directory listing becomes automatic appointment;
- selection is confused with Provider Acceptance;
- conflict review is skipped;
- a Provider receives excessive customer data;
- material Provider changes bypass reapproval;
- technical transmission becomes official status;
- “filed” has no evidence definition;
- payment becomes proof of legal effect;
- Provider reports are accepted without reconciliation;
- unknown states trigger blind retry;
- customer relationships are transferred through direct contact;
- platform margin secretly determines the route.

## 22. Product and technical implications

MarkReg requires:

- typed Capability Needs;
- Provider eligibility and conflict records;
- route recommendations and alternatives;
- appointment authority;
- versioned instructions;
- Provider Acceptance;
- execution requests;
- connector evidence;
- typed Returns;
- official-source validation;
- unknown-state and reconciliation workflows;
- idempotency and duplicate controls;
- payment checkpoints;
- communication and relationship policies.

## 23. Commercial implications

MarkReg may earn managed-fulfillment margin or coordination fees when disclosed and contractually supported.

The commercial model should separate:

- client price;
- Provider cost;
- official fee;
- tax;
- currency effects;
- platform or coordination fee;
- recovery cost.

The platform should not route work to a weaker Provider solely because the margin is higher.

## 24. Operating principle

```text
Express the Capability Need
Verify eligibility
Select with accountable authority
Appoint explicitly
Require Provider Acceptance
Transmit the exact version
Define evidence before action
Reconcile before declaring success
```

> External filing becomes governable when every transition from preparation to official acknowledgement has its own actor, authority, evidence and failure path.