# CH11 — Approval Must Be Specific, Versioned and Revocable

## 1. Approval is a governed authorization, not a mood

Professional systems often infer Approval from informal conduct:

- the customer paid;
- a reviewer said the draft looked good;
- a manager had approved a similar matter before;
- nobody objected;
- the user clicked through a general consent screen;
- the provider began work.

None of these is sufficient by itself.

Approval is a recorded authorization by an actor who has the relevant authority, for a defined next action, against an exact object version, within stated conditions.

```text
Approval
= authorized permission for a specific transition
```

It is not:

```text
Approval
= general satisfaction
= silence
= prior precedent
= payment
= Review acceptance
= permanent authority
```

## 2. Review and Approval answer different questions

Review asks whether an object meets a standard.

Approval asks whether the authorized actor permits the next action.

```text
Review
→ Is this professionally, technically or commercially acceptable?

Approval
→ May this exact next action proceed?
```

Examples:

- a professional reviewer accepts an OA response as legally supportable;
- the customer approves the commercial strategy and amendment;
- the Relationship Owner approves the customer-facing communication;
- the finance authority approves an additional fee;
- the Professional Authority approves formal filing;
- the data owner approves a defined disclosure.

These may be separate approvals held by different actors.

## 3. Approval must identify its authority source

An Approval Record should state:

- approver identity;
- represented role;
- represented Workplace or organization;
- authority source;
- object and version;
- action authorized;
- scope;
- conditions;
- exclusions;
- effective time;
- expiry;
- delegation rule;
- revocation rule;
- evidence of the approval event.

Possible authority sources include:

- customer instruction;
- Engagement terms;
- Workplace role assignment;
- professional appointment;
- jurisdiction-specific qualification;
- internal policy;
- data-processing authorization;
- finance policy;
- emergency authority.

```text
Authenticated User
≠ Authorized Approver for Every Action
```

## 4. Approval applies to an exact version

The approved object may be:

- a filing package;
- a response package;
- a communication draft;
- a provider appointment;
- a payment amount;
- a disclosure set;
- a transaction agreement;
- a public content page;
- a recovery action.

The Approval Record must bind the exact version or checksum.

```text
Package v1 Approved
≠ Package v2 Approved
```

Material changes may include:

- applicant identity;
- trademark image;
- goods or classes;
- legal argument;
- evidence;
- price;
- provider;
- disclosure recipient;
- deadline;
- contract term;
- customer-facing risk statement.

A material change requires re-approval unless the original Approval explicitly permits a bounded class of changes.

## 5. Approval scope must name the next transition

A vague approval such as `approved` is not enough.

More precise forms include:

```text
Approved for Customer Discussion
Approved for Provider Quotation
Approved for Professional Review
Approved for Signature Collection
Approved for External Submission
Approved for Publication
Approved for Payment up to USD X
Approved for Disclosure to Named Provider
```

```text
Approved for Discussion
≠ Approved for Filing
```

## 6. Different approval domains must remain separate

A single Matter can require multiple approval domains:

```text
Customer Decision Approval
Professional Approval
Relationship-owner Communication Approval
Data-disclosure Approval
Commercial Approval
Funds Approval
Provider Appointment Approval
External Protected Action Approval
```

One Approval should not silently imply all others.

```text
Customer Approves Strategy
≠ Finance Approves Additional Cost
≠ Lawyer Approves Legal Filing
```

## 7. Customer instruction must be explicit enough to act on

Customer messages often contain ambiguous language:

- “Looks fine.”
- “Please proceed.”
- “Send me the details.”
- “Do whatever is needed.”

Execution should interpret them in context, but high-impact action requires confirmation of:

- which matter;
- which option;
- which version;
- which cost;
- which deadline;
- which action;
- which known risks.

```text
Positive Reply
≠ Sufficient Customer Instruction
```

Where ambiguity remains, the correct state is `Clarification Required`, not inferred Approval.

## 8. Silence is not Approval

```text
No Response
≠ Approval
≠ Abandonment Decision
≠ Waiver of Review
```

Some Engagements may authorize limited protective action when the customer cannot be reached. That authority must be established in advance, bounded and recorded.

It cannot be invented after the deadline is missed.

## 9. Payment is not Approval

Payment may indicate acceptance of commercial terms, but it does not automatically approve:

- the exact applicant;
- goods scope;
- filing package;
- evidence;
- provider;
- amendment;
- legal argument;
- external action.

```text
Payment Received
≠ Filing Approved
≠ Provider Appointed
≠ Execution Ready
```

Commercial and professional approvals remain separate.

## 10. General consent cannot replace specific Approval

Terms of service may authorize routine processing, storage or defined platform operations. They should not be used as blanket consent for every future Protected Action.

```text
General Platform Consent
≠ Specific Matter Approval
```

The higher the external consequence, irreversibility, cost or disclosure, the more specific the Approval must be.

## 11. Delegation must be explicit

An approver may be allowed to delegate certain decisions. The Approval or authority policy should state:

- whether delegation is allowed;
- which decisions may be delegated;
- to whom;
- for what period;
- with what limit;
- whether sub-delegation is allowed;
- whether Professional Authority remains non-delegable.

```text
Can Approve
≠ Can Delegate Approval
```

Jurisdiction-specific professional actions may require the qualified professional personally to approve or sign.

## 12. Conditional Approval is a first-class state

Approval can be conditional.

Examples:

```text
Approved if Original POA Is Received
Approved up to a Maximum Cost
Approved only for Named Classes
Approved after Final Translation Confirmation
Approved if Provider Confirms Filing Before Deadline
Approved subject to Professional Authority Review
```

Execution must verify conditions before moving to Apply.

```text
Conditional Approval Recorded
≠ Conditions Satisfied
```

## 13. Approval can expire

Expiry triggers may include:

- time limit;
- deadline change;
- material package change;
- source change;
- provider change;
- fee increase;
- customer objective change;
- risk reclassification;
- authority termination.

```text
Approved Once
≠ Approved Forever
```

Before Apply, the system should verify that the Approval remains current.

## 14. Revocation ends future authority

Approval may be revoked before the authorized action occurs.

A revocation record should identify:

- who revoked;
- authority to revoke;
- affected Approval;
- effective time;
- reason;
- whether execution had begun;
- whether external action had already occurred;
- required recovery steps.

```text
Approval Revoked
≠ Historical Approval Erased
```

The earlier Approval remains evidence that the action was authorized during a period.

## 15. Revocation cannot reverse external reality

If a provider was already appointed, a message sent, a payment initiated or a filing submitted, revocation cannot pretend the action never happened.

```text
Authority Revoked
≠ External Action Reversed
```

Execution must move into:

- cancellation request;
- provider recall;
- payment stop or refund process;
- correction;
- official withdrawal;
- customer notification;
- reconciliation.

## 16. Approval may be invalidated by discovered facts

Even without active revocation, Approval may become invalid when:

- applicant identity was wrong;
- a conflict appears;
- evidence is fraudulent or insufficient;
- fee changed materially;
- provider lost eligibility;
- legal deadline changed;
- the approved package differs from the actual package.

The system should record:

```text
Approval Valid
Approval Suspended
Approval Expired
Approval Revoked
Approval Invalidated
Re-approval Required
```

## 17. Approval chains must avoid anonymous collective responsibility

A workflow may require sequential or parallel approvals.

Example:

```text
Professional Review
→ Customer Strategy Approval
→ Finance Approval
→ Professional Final Approval
→ Apply Authorization
```

A group vote should not hide who held which authority.

```text
Multiple Approvals
≠ Collective Unspecified Authority
```

## 18. Emergency Approval must remain bounded

Emergency procedures may be necessary where a deadline is imminent. They should specify:

- trigger;
- emergency authority holder;
- allowed actions;
- maximum cost;
- excluded actions;
- evidence required;
- customer notification;
- post-action review;
- expiry.

```text
Urgent
≠ Automatically Authorized
```

Emergency authority cannot bypass non-delegable professional or legal requirements.

## 19. AI cannot approve by implication

AI can:

- summarize the approved version;
- identify missing approvals;
- compare conditions;
- detect package changes;
- draft an approval request;
- warn that Approval expired.

AI cannot silently infer Approval from sentiment, inactivity or historical patterns.

```text
AI Predicts Consent
≠ Consent Recorded
```

If AI assists the approver, the human Approval Record must remain attributable.

## 20. Approval evidence must be durable

Approval may be captured through:

- signed document;
- authenticated platform action;
- verified email instruction;
- recorded professional decision;
- contract clause applied to a defined event;
- approved API event under a controlled service identity.

The evidence should preserve:

- original communication;
- identity assurance;
- time;
- object version;
- conditions;
- subsequent revocation or expiry.

An AI summary cannot replace the original Approval evidence.

## 21. Approval does not itself execute

After valid Approval, Execution still needs to confirm:

- Implementation Binding;
- current eligibility;
- conditions satisfied;
- idempotency boundary;
- data disclosure;
- funds checkpoint;
- exact Apply target;
- recovery plan;
- required evidence return.

```text
Approved
≠ Applied
≠ Externally Effective
```

## 22. The governing chain

The correct chain is:

```text
Reviewed Object
→ Decision-ready Preview
→ Specific Approval
→ Approval Validity Check
→ Apply
→ External Evidence
→ Formal-state Validation
```

Approval is the point where authority becomes explicit. Its purpose is not to add bureaucracy. Its purpose is to ensure that consequential action is attributable, bounded, explainable and reversible where possible.