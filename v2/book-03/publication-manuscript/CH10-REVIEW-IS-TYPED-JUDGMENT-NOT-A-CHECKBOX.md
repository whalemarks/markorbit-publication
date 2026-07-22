# CH10 — Review Is Typed Judgment, Not a Checkbox

## 1. Review exists because production and authority are different

Professional systems often treat Review as a checkbox added near the end of a task. That model is too weak for MarkOrbit.

Review is a governed judgment about a defined object, by an eligible reviewer, under a stated review purpose and standard.

```text
Review
= typed judgment on an exact version
```

It is not:

```text
Review
= generic approval
= final authority
= customer decision
= permission to Apply
```

The fundamental boundary is:

```text
Produced
≠ Reviewed
≠ Approved
≠ Applied
```

## 2. Review must answer a specific question

A useful Review identifies what is being judged.

Examples include:

- factual accuracy;
- source sufficiency;
- professional reasoning;
- jurisdiction compliance;
- document validity;
- visual quality;
- trademark continuity;
- commercial fit;
- privacy compliance;
- customer-communication safety;
- fee and deadline accuracy;
- execution readiness;
- evidence completeness.

A reviewer should not receive an object with the instruction:

> Please review.

The Review Request should instead state:

> Review Package v3 for applicant identity, filed-mark continuity, goods scope and jurisdiction-specific document readiness. Do not approve filing or customer communication.

## 3. Review types must remain distinct

A single artifact can require multiple Review types.

For a filing package:

```text
Identity Review
+ Mark Review
+ Goods Review
+ Document Review
+ Fee Review
+ Jurisdiction Review
```

For public content:

```text
Professional-fact Review
+ Editorial Review
+ SEO Review
+ GEO Review
+ Conversion-safety Review
+ Privacy Review
```

For a trademark transaction:

```text
Right Verification
+ Chain-of-title Review
+ Commercial Review
+ Contract Review
+ Recordal Readiness Review
```

These perspectives cannot be merged into an anonymous “reviewed” status.

```text
Reviewed for SEO
≠ Reviewed for Professional Accuracy
```

## 4. Review is bound to an exact object and version

Every Review Record should identify:

- object type;
- object identifier;
- version or checksum;
- source package;
- Review type;
- reviewer;
- represented authority;
- applicable jurisdiction;
- review standard;
- findings;
- limitations;
- disposition;
- time;
- expiry or invalidation conditions.

```text
Package v1 Reviewed
≠ Package v2 Reviewed
```

A material change to applicant, mark, goods, evidence, argument, cost or provider can invalidate an earlier Review.

## 5. Reviewer eligibility is task-specific

The system must evaluate whether the reviewer is eligible for the specific Review.

Possible requirements include:

- Capability Evidence;
- Certification;
- Production Authorization;
- Professional Qualification;
- jurisdiction;
- language;
- conflict clearance;
- data-access scope;
- recent practice;
- independence from the producer;
- capacity before deadline.

```text
Experienced Person
≠ Eligible Reviewer for Every Review
```

A senior editor may review clarity but not issue a legal conclusion. A trademark lawyer may review legal strategy but not necessarily visual design quality. A Provider may confirm local practice but may have a commercial interest that needs disclosure.

## 6. Review depth follows risk, reversibility and authority

MarkOrbit may use a review scale such as:

```text
R0 — deterministic validation
R1 — standardized work with sampling
R2 — complete professional review
R3 — senior or cross-professional review
R4 — qualified final-authority review
```

The tier should consider:

- severity of a wrong result;
- reversibility;
- deadline pressure;
- financial consequence;
- professional reservation;
- data sensitivity;
- uncertainty;
- performer quality history;
- source authority;
- external effect.

```text
Low Effort
≠ Low Risk
```

A short instruction to file, pay or disclose data can be more consequential than a long internal report.

## 7. Review can produce findings, not only pass or fail

Useful Review dispositions include:

```text
Accepted
Accepted with Conditions
Accepted for Limited Purpose
Revision Required
Escalation Required
Additional Evidence Required
Customer Decision Required
Professional Authority Required
Rejected for Defined Reason
Review Inconclusive
```

A Review Record should preserve each finding and its severity.

Example:

```text
Applicant identity: Accepted
Goods scope: Revision Required
POA: Original requirement unresolved
Fee: Estimate only
Filing readiness: Not established
```

This is more informative than `review failed`.

## 8. Review comments must be attributable

Anonymous comments such as “change this” or “not good enough” are not sufficient governance.

Each material finding should identify:

- reviewer;
- review role;
- exact location or field;
- reason;
- source or standard;
- requested disposition;
- whether it blocks the next transition.

This makes review auditable and allows later analysis of reviewer quality.

## 9. Review is not Approval

Review answers questions such as:

- Is the evidence sufficient?
- Does the package meet the professional standard?
- Are risks disclosed?
- Is the object ready to be presented for a decision?

Approval answers a different question:

- Does the authorized actor permit the specified next action?

```text
Professional Review Accepted
≠ Customer Approved Cost
≠ Relationship Owner Approved Communication
≠ Professional Authority Approved Filing
```

One person may hold both roles in a small Workplace, but the records should remain distinct.

## 10. Review is not customer instruction

A reviewer may conclude that filing is professionally supportable. The customer may still choose not to file because of cost, timing or strategy.

Conversely, a customer may request filing despite identified risk. That does not erase required professional Review or jurisdictional authority.

```text
Professional Recommendation
≠ Customer Decision

Customer Risk Acceptance
≠ Professional Review Waived
```

## 11. Review of AI output requires provenance

AI-assisted work should expose:

- model and version;
- instruction or prompt reference;
- source set;
- retrieval time;
- tool use;
- uncertainty;
- memory policy;
- human edits;
- unresolved hallucination risk.

The reviewer must know whether the artifact is:

- fully human-produced;
- AI-assisted;
- AI-drafted;
- AI-executed under policy;
- hybrid multi-contributor work.

```text
Fluent Output
≠ Grounded Output
≠ Reviewed Output
```

Review should focus on the substantive risk, not merely the fact that AI was used.

## 12. AI may assist Review but cannot silently become the reviewer of record

AI can:

- check completeness;
- compare versions;
- identify contradictions;
- verify citations;
- apply deterministic rubrics;
- detect missing fields;
- propose findings.

But where a human or professionally qualified Review is required, AI output remains a Review Candidate.

```text
AI Review Candidate
≠ Qualified Review Record
```

The human disposition should state whether the AI finding was accepted, modified or rejected.

## 13. Reviewer independence matters

Some Reviews require separation between producer and reviewer.

Risk signals include:

- self-review of high-impact work;
- reviewer compensation tied to approval volume;
- Provider reviewing its own compliance;
- commercial team reviewing legal accuracy;
- Relationship Owner suppressing inconvenient risk.

MarkOrbit should record conflicts and, where necessary, require a different reviewer or an additional independent Review.

## 14. Review availability is part of readiness

A package is not execution-ready merely because production is complete.

```text
Production Complete
+ Required Reviewer Unavailable
= Not Review Ready
```

Workflows should expose:

- reviewer assigned;
- reviewer accepted;
- deadline feasible;
- fallback reviewer;
- escalation route;
- expiry of prior Review.

## 15. Sampling must be governed

R1 sampling can be appropriate for standardized, low-risk production, but sampling policy should define:

- population;
- sample rate;
- selection method;
- reviewer;
- defect thresholds;
- escalation rules;
- retrospective review;
- suspension triggers.

```text
Sampled Review
≠ No Accountability for Unsampled Work
```

Systemic failures discovered through sampling may require review of previously accepted work.

## 16. Review debt must not be hidden

When deadlines force work to proceed with incomplete Review, the exception must be explicit.

Possible states include:

```text
Emergency Review Exception Requested
Exception Approved
Post-action Review Required
Residual Risk Accepted
Exception Expired
```

This cannot be used to bypass Professional Authority or legal requirements.

```text
Urgency
≠ Authority
```

## 17. Review affects capability evidence, but carefully

A reviewed Contribution may produce Capability Evidence about the performer and reviewer.

Useful signals include:

- defect type;
- severity;
- independence level;
- correction quality;
- recurrence;
- context;
- reviewer agreement;
- downstream outcome.

But one negative result should not create a universal judgment.

```text
One Review Finding
≠ Universal Capability Conclusion
```

## 18. Review history must remain immutable

When an artifact is corrected, the earlier Review remains part of the audit trail.

```text
Review v1
→ Revision v2
→ Review v2
```

The system should not overwrite `Review v1` with the later accepted result. That history explains what changed and why.

## 19. Review completion is not formal-state completion

Even after all Reviews are accepted, the next stages may still require:

- customer decision;
- specific Approval;
- Provider acceptance;
- funds checkpoint;
- Apply;
- external acknowledgement;
- Owning Service validation.

```text
Review Complete
≠ Apply Authorized
≠ External Action Complete
≠ Formal State Updated
```

## 20. The governing principle

Review is where MarkOrbit turns production into accountable professional judgment.

It must remain:

- typed;
- attributable;
- version-bound;
- risk-calibrated;
- authority-aware;
- separate from Approval and Apply.

A checkbox can record that somebody clicked. A Review Record must explain what was judged, by whom, under what authority and with what remaining risk.