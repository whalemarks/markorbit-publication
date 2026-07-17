# B07-CH-23 — Fulfillment Milestones and Evidence

## 1. Managed work must be observable without pretending that observation is official truth

International professional work often passes through stages that are invisible to the customer: conflict review, document preparation, filing, authority receipt, examination, publication, registration, certification and follow-up.

MGSN needs a governed way to observe these stages.

```text
Provider work
→ Fulfillment Milestone
→ Fulfillment Evidence
→ Fulfillment Observation
→ Return
→ Owning Service validation
```

The network may observe and coordinate progress, but only the authoritative source and Owning Service can establish formal business truth.

## 2. Fulfillment Milestone

A Fulfillment Milestone is a defined checkpoint in the accepted Service Package or Managed Network Engagement.

A milestone should identify:

- milestone type;
- expected actor;
- expected timing;
- prerequisite inputs;
- required evidence;
- completion tolerance;
- escalation rule;
- whether it affects funds-release eligibility;
- whether it creates a Return obligation.

Examples include:

- provider conflict check completed;
- documents accepted for preparation;
- application prepared for approval;
- filing instruction accepted;
- filing submitted;
- official receipt obtained;
- examination response delivered;
- publication confirmed;
- certificate obtained;
- closing report returned.

## 3. Milestones must reflect the service, not a universal template

Different jurisdictions and services have different procedural structures. A filing service, opposition, renewal, assignment or office-action response should not be forced into the same milestone sequence.

MGSN should use:

```text
common milestone grammar
+ service-specific sequence
+ jurisdiction-specific conditions
+ provider-specific accepted obligations
```

This allows comparability without erasing legal differences.

## 4. Fulfillment Evidence

Fulfillment Evidence supports a milestone observation. It may include:

- provider confirmation;
- filing receipt;
- official acknowledgment;
- stamped document;
- authority screenshot or export;
- courier record;
- invoice or payment receipt;
- work product;
- signed declaration;
- structured status payload.

Evidence should carry:

- source;
- date and time;
- engagement reference;
- provider identity;
- document or payload type;
- jurisdiction and service;
- integrity or provenance information;
- confidentiality classification;
- expiry or recheck requirement where applicable.

## 5. Evidence quality

Not all evidence has equal authority.

A practical evidence hierarchy may distinguish:

```text
Official source evidence
Provider-generated professional evidence
Third-party operational evidence
Customer-supplied evidence
Operator observation
Unverified assertion
```

The hierarchy does not mean lower-ranked evidence is useless. It means the system must not represent all sources as equally authoritative.

## 6. Fulfillment Observation

A Fulfillment Observation records what MGSN has reasonably inferred from available evidence.

Examples:

- milestone evidence received;
- evidence incomplete;
- expected deadline approaching;
- provider-reported filing completed;
- official confirmation pending;
- evidence inconsistent;
- milestone overdue;
- correction requested.

```text
Fulfillment Observation
≠ official legal status
≠ Matter formal state
≠ automatic acceptance by Originating Workplace
```

It is a network-control record used to coordinate action and Return.

## 7. Deadline monitoring

Deadlines should be linked to source and confidence.

A deadline record should distinguish:

- official deadline;
- provider-calculated deadline;
- contractual target;
- internal operating target;
- estimated timing;
- unknown or disputed date.

The platform must not present an estimate as an official deadline. When the source is uncertain, the record should show uncertainty and trigger human review.

## 8. Missing or weak evidence

A provider statement such as “done” is not always sufficient.

Missing, unreadable, inconsistent or stale evidence should trigger a controlled branch:

```text
request clarification
or
request replacement evidence
or
mark observation uncertain
or
escalate
or
open incident
or
hold related release eligibility
```

The platform should not manufacture certainty to keep the workflow moving.

## 9. Acceptance of work

Evidence received does not automatically mean the work is accepted.

Acceptance may require:

- scope conformity;
- correct applicant or owner data;
- correct goods or services;
- correct filing basis;
- complete official receipt;
- absence of material discrepancy;
- Originating Workplace review;
- customer approval where required.

A milestone can therefore be “evidence received” while still remaining “not accepted” or “correction required”.

## 10. Product rule

MGSN must make professional fulfillment observable through typed milestones, source-qualified evidence and explicit observations, while preserving the distinction between network visibility and authoritative legal or business truth.
