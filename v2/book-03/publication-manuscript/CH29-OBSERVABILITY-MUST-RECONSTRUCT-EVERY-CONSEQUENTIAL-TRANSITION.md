# CH29 — Observability Must Reconstruct Every Consequential Transition

## 1. A professional execution system must be able to explain what happened

Execution becomes trustworthy only when it can reconstruct consequential transitions after the fact.

The required chain is:

```text
Request
→ Context
→ Scope
→ Eligibility
→ Implementation Binding
→ Assignment or Invocation
→ Contribution
→ Review
→ Approval
→ Preview
→ Apply
→ Return
→ Reconciliation
→ Formal-state Validation
```

If any material transition cannot be reconstructed, the system cannot reliably answer:

- what was requested;
- who acted;
- under which authority;
- which object version was used;
- which model or tool participated;
- what was sent externally;
- whether the external effect occurred;
- how the final state was established.

```text
Activity Log
≠ Execution Observability
```

A list of clicks is not enough. Observability must preserve the meaning, authority, version and consequence of each event.

## 2. Observability serves multiple forms of accountability

The same execution record may need to support:

- customer explanation;
- internal quality review;
- professional accountability;
- provider dispute resolution;
- financial reconciliation;
- privacy investigation;
- security response;
- regulatory or contractual audit;
- system debugging;
- Capability learning;
- incident recovery.

These audiences do not require identical access, but they require a coherent underlying event history.

```text
Auditable
≠ Universally Visible
```

## 3. Every consequential event needs a semantic envelope

A meaningful execution event should preserve at least:

- event type;
- timestamp;
- actor or service identity;
- represented Workplace and role;
- Product Installation;
- Capability and version;
- affected object and version;
- authority source;
- data scope;
- M-mode;
- R-tier;
- input references;
- output references;
- decision or transition;
- external target;
- evidence;
- correlation and causation identifiers;
- resulting state or Unknown.

This semantic envelope allows later reconstruction without embedding all sensitive data in the event itself.

## 4. Event history must preserve causation, not only chronology

Chronological order does not explain why an action occurred.

The system should link:

```text
Customer Instruction
→ Capability Request
→ Work Package
→ Assignment
→ Contribution
→ Review Finding
→ Approval
→ Apply Attempt
```

Useful relationships include:

```text
Caused By
Responds To
Supersedes
Corrects
Derived From
Approved By
Applied Through
Reconciled By
Formalized As
```

```text
Occurred After
≠ Caused By
```

## 5. Correlation must survive cross-system execution

Execution may cross:

- Workplace systems;
- MarkReg or Lite;
- Core services;
- AI providers;
- provider portals;
- payment gateways;
- email systems;
- official offices;
- manual operator actions.

The audit chain should preserve stable references such as:

- Capability Request ID;
- Workflow Instance ID;
- Work Package ID;
- Assignment ID;
- Contribution ID;
- Approval ID;
- Apply Attempt ID;
- idempotency key;
- external reference;
- formal-state mutation ID.

No single external system will provide the full history. MarkOrbit must correlate the evidence without falsely claiming external authority.

## 6. Exact versions must remain observable

For every material event, the system should be able to identify:

- package version;
- file hash;
- source version;
- fee schedule version;
- policy version;
- model version;
- prompt or instruction reference;
- provider quote version;
- Review version;
- Approval version.

```text
Same File Name
≠ Same Artifact
```

A later replacement must not erase the version that was actually reviewed or submitted.

## 7. Human and machine actions require equal traceability

```text
Manual
≠ Untracked

Automated
≠ Fully Explained by Technical Logs
```

A human who logs into an official portal and submits manually should record:

- identity;
- represented role;
- package hash;
- portal and account context;
- time;
- external reference;
- receipt;
- uncertainty.

An automated Connector should record the same semantic information in addition to request and response details.

## 8. AI observability requires provenance beyond output text

An AI-assisted event should expose:

- model and version;
- policy version;
- prompt or instruction reference;
- source set;
- retrieved passages;
- tool calls;
- memory context;
- generation parameters where relevant;
- output artifact;
- human edits;
- review and disposition;
- Apply authority.

```text
Model Output Stored
≠ AI Execution Reconstructable
```

The system must also distinguish AI suggestion, AI draft, AI decision candidate and AI Apply attempt.

## 9. Review and Approval must remain independently observable

A later auditor should be able to determine:

- what Review type occurred;
- which exact version was reviewed;
- reviewer eligibility;
- findings;
- limitations;
- whether revision followed;
- who approved the next action;
- the authority source;
- conditions and expiry.

```text
Reviewer and Approver Are Same Person
≠ Review and Approval Are Same Event
```

## 10. Apply observability must preserve payload identity

For each Apply attempt, preserve:

- Preview reference;
- Approval reference;
- payload hash;
- target;
- implementation;
- actor;
- idempotency key;
- attempt number;
- start and end time;
- response;
- external reference;
- timeout or partial state;
- retry policy;
- reconciliation requirement.

```text
Request Logged
≠ External Effect Known
```

## 11. Unknown must remain visible

Unknown should not disappear because the interface needs a clean status.

Examples include:

- provider claims filing without receipt;
- payment debited but not settled;
- message accepted by mail server but delivery uncertain;
- connector timeout after possible submission;
- courier delivered but recipient has not confirmed the original document.

The system should preserve:

```text
Known Facts
Conflicting Evidence
Current Interpretation
Next Reconciliation Step
Owner
Deadline Exposure
```

```text
Unknown Hidden
= False Confidence
```

## 12. Formal-state mutations need their own evidence chain

When an Owning Service changes a formal state, the event should identify:

- previous state;
- proposed state;
- validating evidence;
- validation rule;
- validator;
- effective time;
- source authority;
- limitations;
- rollback or correction rule.

```text
Execution Completed
≠ Formal State Changed Automatically
```

## 13. Financial observability must separate different events

The audit chain should distinguish:

```text
Customer Payment Requested
Customer Payment Approved
Customer Payment Received
Provider Payment Approved
Provider Payment Sent
Provider Payment Received
Official Fee Applied
Contributor Compensation Released
Refund Issued
Credit Recorded
Reconciliation Completed
```

One generic event called `paid` destroys accountability.

## 14. Communication observability must preserve represented identity

For every consequential communication, preserve:

- visible sender;
- represented organization;
- professional identity where required;
- recipients;
- subject;
- attachments and hashes;
- claims and requests;
- deadline language;
- approval;
- send result;
- delivery result;
- response and interpretation.

```text
Message Sent
≠ Message Delivered
≠ Message Understood
≠ Customer Instruction Received
```

## 15. Data access and disclosure need separate records

The system should distinguish:

- data viewed;
- downloaded;
- exported;
- shared;
- disclosed externally;
- retained;
- deleted;
- reused for another purpose.

```text
View Access
≠ Disclosure
≠ Reuse Permission
```

Observability must not itself create excessive surveillance. It should record necessary events proportionately and restrict access to the record.

## 16. Tamper evidence matters

High-impact histories should support detection of unauthorized alteration through mechanisms such as:

- append-oriented event storage;
- immutable version identifiers;
- checksums;
- signed receipts;
- restricted mutation rights;
- correction events rather than destructive overwrites;
- retention policy;
- access logging.

```text
Corrected Record
≠ Earlier Record Erased
```

## 17. Correction and redaction require explicit governance

Some records may contain inaccurate or excessive personal data. The system may need to correct or redact them while preserving accountability.

A correction should record:

- original value reference;
- corrected value;
- reason;
- authority;
- time;
- downstream objects affected.

A privacy redaction should preserve enough metadata to prove that an event occurred without exposing restricted content.

## 18. Observability should support replay without re-execution

A reviewer should be able to reconstruct the decision path without triggering the original side effects.

```text
Replay for Understanding
≠ Re-run Apply
```

Simulation, audit and incident review must use isolated evidence views rather than live credentials or production actions.

## 19. Metrics must be derived from semantic events carefully

Operational metrics may include:

- acknowledgement time;
- review cycle time;
- defect rate;
- Unknown duration;
- provider return completeness;
- deadline margin;
- recovery time;
- duplicate prevention;
- correction rate.

But metric interpretation must preserve context.

```text
Fast Completion
≠ High-quality Outcome

Low Escalation Rate
≠ Low Risk
```

A performer who escalates correctly may be more reliable than one who hides uncertainty.

## 20. Observability access must follow role and purpose

Different roles may see different projections:

- customer-facing timeline;
- Delivery Owner view;
- professional Review view;
- finance view;
- privacy view;
- security view;
- regulator or auditor export.

The underlying event identity remains consistent, but sensitive content is filtered according to authority and purpose.

## 21. Retention must reflect obligation and risk

Retention policy should consider:

- legal and professional record duties;
- customer contract;
- privacy rules;
- financial reconciliation;
- dispute periods;
- security requirements;
- training and Knowledge exclusions.

```text
Retain for Audit
≠ Retain for AI Training
```

## 22. The governing principle

Observability is the memory of governed execution.

It must make it possible to answer:

```text
Who knew what,
who decided what,
who authorized what,
what exact version was acted upon,
what external effect occurred,
and how the final truth was validated.
```

Without that reconstruction, workflow automation can be fast but not accountable.