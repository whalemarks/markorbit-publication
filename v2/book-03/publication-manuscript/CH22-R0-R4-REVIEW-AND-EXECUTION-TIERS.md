# CH22 — R0–R4 Review and Execution Tiers

## 1. Risk classification needs an operational response

A risk model is useful only when it changes how work is performed, reviewed, approved and applied.

Book 03 therefore uses five execution-control tiers:

```text
R0 — deterministic and low-consequence control
R1 — standardized production with governed sampling
R2 — complete professional review before consequential use
R3 — senior or cross-professional review
R4 — qualified final-authority control
```

These tiers are not labels for people, Products or organizations. They attach to a specific transition under a specific context.

```text
R-tier
≠ Job Title
≠ Permanent Performer Rank
≠ Product Marketing Label
```

## 2. M-mode and R-tier answer different questions

The Human–AI mode answers:

> How is the work produced?

The risk tier answers:

> What level of control is required before the result may be relied upon or applied?

```text
M-mode
≠ R-tier
```

Examples:

```text
M0 / R4 — human-only final legal approval
M2 / R1 — AI-assisted standardized data work with sampling
M3 / R2 — AI draft with complete professional review
M4 / R0 — bounded deterministic-like automation for low-risk internal action
M5 / R4 — hybrid network with final qualified authority
```

A highly automated route can have a high Review tier. A human-only route can still be low risk.

## 3. R0 — deterministic and low-consequence control

R0 is appropriate when:

- inputs are structured and validated;
- rules are explicit and current;
- action is reversible or has minimal consequence;
- no professional reservation applies;
- no external Protected Action occurs;
- failure is detectable;
- evidence is automatically captured.

Examples may include:

- format validation;
- duplicate-field detection;
- schema transformation;
- checksum verification;
- internal reminder generation from a verified deadline;
- simulation-only Apply;
- low-risk internal routing.

R0 does not mean uncontrolled.

It still requires:

- Capability version;
- source version where relevant;
- deterministic rule;
- input validation;
- logging;
- failure state;
- rollback or correction;
- test coverage.

```text
Automated
≠ R0 Automatically
```

A deterministic filing connector may still be R4 because its external consequence is severe.

## 4. R1 — standardized production with governed sampling

R1 is suitable for repeatable work where:

- scope is bounded;
- errors are usually detectable and correctable;
- performers or models have current quality evidence;
- standardized rubrics exist;
- sampling can detect systemic drift;
- unsampled work remains auditable.

Examples may include:

- routine source extraction;
- metadata normalization;
- standard document completeness checks;
- low-risk content formatting;
- recurring status triage.

Sampling policy must define:

- population;
- sample method;
- sample rate;
- Reviewer;
- defect threshold;
- escalation threshold;
- retrospective review trigger;
- temporary suspension rule.

```text
R1 Sampling
≠ No Accountability for Unsampled Work
```

A material defect found in a sample may require review of the entire affected population.

## 5. R2 — complete professional review

R2 requires every relevant output to receive complete Review before it is used for the specified consequential purpose.

Appropriate examples include:

- filing-package preparation;
- OA response drafts;
- evidence sufficiency analysis;
- public jurisdiction guidance;
- customer-facing professional recommendations;
- provider instruction packages;
- recordal preparation.

R2 should define:

- Review types;
- eligible Reviewer;
- exact version;
- standard;
- required findings;
- material-change rules;
- revision loop;
- Approval boundary.

```text
R2 Review Complete
≠ Apply Authorized
```

Customer decision, professional Approval, Provider appointment or funds Approval may still be required.

## 6. R3 — senior or cross-professional review

R3 is used where one competent Review is not sufficient because the matter is unusually complex, contested, high-value or cross-disciplinary.

Triggers may include:

- conflicting professional opinions;
- unusual jurisdiction practice;
- multi-country strategy;
- high-value transaction;
- significant evidence ambiguity;
- material customer relationship risk;
- public statement with broad reach;
- novel Human–AI execution path;
- repeated production defects;
- recovery from a serious incident.

R3 may require:

```text
Primary Professional Review
+ Senior Review
+ Independent or Cross-professional Review
+ Delivery-owner Synthesis
```

```text
More Reviewers
≠ Automatic Consensus
```

Typed disagreement and authority must remain visible.

## 7. R4 — qualified final-authority control

R4 applies where the final decision or action requires a specifically qualified, appointed or legally authorized actor.

Examples may include:

- final legal filing approval;
- signing a declaration;
- submitting under local professional authority;
- binding legal response;
- official withdrawal or surrender;
- final transaction legal approval;
- regulated professional communication;
- non-delegable formal action.

R4 requires verification of:

- identity;
- professional qualification;
- jurisdiction;
- appointment;
- conflict clearance;
- exact approved object;
- current authority;
- signature or Apply method;
- durable evidence.

```text
Strong Capability Evidence
≠ R4 Authority
```

R4 authority cannot be created by Certification, platform ranking, AI performance or customer preference.

## 8. R-tier applies to transitions, not whole workflows

A single Workflow may contain several tiers.

Example:

```text
R0 — schema validation
R1 — standardized data extraction
R2 — complete package review
R3 — strategy conflict resolution
R4 — final professional filing approval
```

This allows low-risk stages to remain efficient while consequential transitions receive stronger governance.

## 9. Tier selection should be explainable

The selected tier should state its basis:

- consequence;
- reversibility;
- source authority;
- uncertainty;
- external effect;
- deadline;
- professional reservation;
- data sensitivity;
- financial exposure;
- performer evidence;
- model evidence;
- recovery feasibility.

```text
R3 Selected
→ Reasons Visible
```

The system should not merely display a risk color without explaining the control requirement.

## 10. Material changes can raise the tier

Examples include:

- a standard filing becomes contested;
- applicant identity becomes disputed;
- deadline enters emergency range;
- provider practice conflicts with official source;
- evidence authenticity is questioned;
- customer requests broader scope;
- payment amount increases materially;
- AI model or source changes.

```text
R1 at Start
≠ R1 Forever
```

Tier should be re-evaluated before critical Review, Approval and Apply transitions.

## 11. A tier may be lowered only with evidence

Risk reduction may occur when:

- official status is verified;
- missing document is obtained;
- deterministic validation is proven;
- source conflict is resolved;
- scope is narrowed;
- customer selects a reversible route;
- stronger evidence becomes available.

Commercial pressure or user impatience does not justify lowering the tier.

```text
Faster Desired
≠ Lower Tier Justified
```

## 12. Emergency exceptions do not erase R4 requirements

Emergency procedures may alter timing or sequencing, but cannot fabricate professional authority.

Possible emergency controls include:

- expedited Reviewer selection;
- parallel Review;
- protective limited action;
- pre-authorized cost ceiling;
- immediate customer notification;
- post-action audit where legally permissible.

```text
Emergency
≠ Professional Authority Waived
```

## 13. Reviewer and approver roles can differ by tier

At R0, the control may be deterministic validation owned by the Capability team.

At R1, a qualified sampler or quality reviewer may suffice.

At R2, a complete professional reviewer is required.

At R3, senior and cross-professional contributors may be needed.

At R4, the final qualified authority must approve or execute.

```text
Reviewer at R2
≠ Final Authority at R4
```

## 14. AI participation must respect tier constraints

AI may participate across all tiers, but its role changes.

Examples:

```text
R0 — bounded deterministic-like operation under policy
R1 — standardized assistance with sampling
R2 — draft or analysis subject to full review
R3 — synthesis support with explicit disagreement preservation
R4 — preparation support; qualified authority remains final actor
```

```text
AI Produces R4 Package
≠ AI Holds R4 Authority
```

## 15. Tier evidence should support audit and improvement

The execution record should preserve:

- original risk classification;
- selected tier;
- reasons;
- Review performed;
- Reviewer eligibility;
- findings;
- Approval;
- Apply result;
- defects;
- recovery;
- later tier adjustments.

This enables MarkOrbit to test whether controls are too weak, too costly or incorrectly targeted.

## 16. Under-classification is an incident

If an R4 action was incorrectly treated as R1, the problem is not merely a workflow configuration defect.

The system should:

- contain further action;
- identify affected Matters;
- preserve evidence;
- reassess prior outputs;
- notify responsible owners;
- correct tier policy;
- consider customer or professional notification;
- review capability authorization.

## 17. Over-classification also has cost

Applying R4 controls to every low-risk step can create:

- delay;
- reviewer bottlenecks;
- unnecessary cost;
- ceremonial approval;
- reduced attention to genuinely high-risk work.

The goal is proportional control.

```text
Maximum Review Everywhere
≠ Maximum Safety
```

## 18. The governing matrix

A simplified control matrix is:

| Tier | Typical consequence | Review pattern | Apply authority |
|---|---|---|---|
| R0 | low, reversible | deterministic validation | bounded policy |
| R1 | standardized, detectable | governed sampling | limited internal action |
| R2 | material professional reliance | full review | separate Approval required |
| R3 | complex or cross-professional | senior/multiple typed Reviews | explicit accountable synthesis |
| R4 | protected or reserved action | qualified final-authority Review | qualified/appointed actor |

## 19. The governing principle

R0–R4 provides a common language for connecting risk to execution controls.

```text
Risk
→ Tier
→ Review
→ Approval
→ Apply Authority
```

It allows MarkOrbit to automate safely where evidence supports automation and to preserve real professional authority where the consequence demands it.