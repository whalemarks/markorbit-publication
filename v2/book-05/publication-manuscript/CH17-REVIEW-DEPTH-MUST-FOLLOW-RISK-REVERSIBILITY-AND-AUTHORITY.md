# Chapter 17 — Review Depth Must Follow Risk, Reversibility and Authority

A review step is easy to add to a workflow.

A trustworthy review system is much harder to design.

Many professional-service platforms use a single checkbox:

```text
Reviewed = yes
```

That checkbox conceals the questions that actually matter:

- what was reviewed;
- against which source and standard;
- by whom;
- at which version;
- for which risk;
- with what authority;
- what was outside scope;
- whether the reviewer could act independently;
- what happens when the underlying facts change.

MarkReg should treat review as a governed decision architecture rather than a final proofreading step.

```text
Prepared work
→ risk and authority classification
→ required review mode
→ reviewer eligibility
→ exact-version review
→ finding, limitation or escalation
→ approval where applicable
→ protected action or customer delivery
```

## 1. Quality is designed before review

A senior reviewer cannot reliably repair a production system that begins with:

- stale official data;
- an ambiguous Work Package;
- incomplete customer facts;
- mismatched versions;
- unqualified Assignment;
- missing evidence;
- hidden assumptions;
- unclear responsibility;
- an impossible deadline.

Review is one control among several.

```text
Source quality
+ clear Work Package
+ suitable performer
+ deterministic validation
+ version control
+ proportional review
+ accountable approval
= governed quality path
```

The Product should therefore distinguish prevention from detection.

### Prevention controls

- controlled input schemas;
- required sources;
- Capability and eligibility gates;
- version locks;
- permitted AI modes;
- document validation;
- deadline verification;
- data-access limits;
- explicit acceptance criteria.

### Detection controls

- deterministic checks;
- sampling;
- professional review;
- cross-checking;
- discrepancy detection;
- customer confirmation;
- official-result reconciliation.

A final reviewer should not become the default substitute for missing upstream controls.

## 2. Review depth follows consequence, not convenience

Review depth should consider multiple dimensions.

### Legal or professional consequence

Could the output affect the existence, scope, priority, ownership, use, maintenance or enforceability of a trademark right?

### Reversibility

Can an error be corrected before external effect, or would it create a missed deadline, official record, public statement or irreversible customer decision?

### Source quality

Is the work based on a current official source, a Provider statement, customer recollection, AI inference or an unresolved conflict?

### Uncertainty

How many material facts remain Unknown, disputed or inferred?

### Value and financial exposure

Could the decision cause significant official fees, professional fees, transaction value, refunds or customer loss?

### Customer impact

Would an error mislead the customer, expose confidential information, damage trust or cause an unsuitable filing strategy?

### Novelty and complexity

Is the task routine under an approved Requirement Set, or does it involve an unusual jurisdiction, disputed evidence, cross-border ownership chain or new rule?

### Deadline and recovery risk

Is there time for correction? Is a grace period verified? Would a failed action be restorable?

### Performer and reviewer history

Is the person newly authorized, recently inactive, repeatedly corrected or demonstrably reliable in this exact scope?

### External authority

Does the action require a qualified attorney, agent, office representative or other Professional Authority?

No single score should hide these dimensions.

```text
Low aggregate score
≠ no material legal issue

High performer history
≠ authority for every jurisdiction
```

## 3. A practical review spectrum

MarkReg may use a review spectrum such as:

```text
R0 — deterministic validation only
R1 — standardized work with sampling
R2 — complete professional review
R3 — senior or cross-disciplinary review
R4 — qualified final authority
```

The labels are implementation candidates, not universal legal categories.

### R0 — deterministic validation only

Suitable for bounded, reversible checks such as:

- required-field presence;
- identifier format;
- document page count;
- exact-version comparison;
- arithmetic reconciliation;
- duplicate detection;
- known-schema validation.

R0 is not appropriate merely because software can produce a result.

### R1 — standardized work with sampling

Suitable where:

- the rules are stable and explicit;
- consequences are limited;
- errors are detectable and reversible;
- contributor history is strong;
- quality sampling remains meaningful.

Examples may include routine data normalization or low-risk content-format checks.

### R2 — complete professional review

Required where the result contains professional interpretation or affects customer decisions, such as:

- search-risk explanation;
- goods-scope recommendation;
- use-evidence screening;
- deadline interpretation;
- owner mismatch assessment;
- response-package preparation;
- public legal-content factual review.

### R3 — senior or cross-disciplinary review

Appropriate where several domains intersect:

- trademark law and corporate ownership;
- transaction terms and official recordal;
- evidence sufficiency and licensing;
- public marketing claims and professional rules;
- data privacy and cross-border fulfillment;
- disputed or contradictory official sources.

### R4 — qualified final authority

Required where law, professional regulation or Engagement terms reserve the decision or external action to a qualified person or Organization.

```text
R4 review completed
≠ customer approved
≠ Provider appointed
≠ action submitted
```

Review and execution remain separate.

## 4. The object of review must be exact

A reviewer should not approve “the application” in the abstract.

The review record should reference:

- Matter;
- Work Package;
- Contribution or Package version;
- mark representation version;
- applicant and address version;
- classes and goods version;
- source and Requirement Set versions;
- documents and evidence versions;
- fee and Provider route where relevant;
- deadline basis;
- stated assumptions and Unknowns.

```text
Version 1 reviewed
≠ materially changed Version 2 reviewed
```

A material change may invalidate all or part of the review.

Material changes may include:

- applicant identity;
- mark image;
- goods deletion or addition;
- filing basis;
- priority claim;
- evidence item;
- response argument;
- owner or transaction party;
- fee basis;
- external route;
- public content claim;
- conversion recommendation.

The system should show the diff and request the appropriate new review rather than silently retaining an old green status.

## 5. Review findings need more than pass or fail

A useful review outcome may be:

```text
Accepted
Accepted with stated limitation
Accepted for preparation only
Customer confirmation required
Professional escalation required
Revision required
Source refresh required
Blocked by authority
Rejected with reason
Unable to conclude because evidence is insufficient
```

The finding should identify:

- what was tested;
- what passed;
- what failed;
- what remains outside scope;
- what evidence is missing;
- what correction is required;
- whether the prior approval remains valid;
- who owns the next action.

An honest inability to conclude is a valid professional outcome.

## 6. Review is different from approval

The following distinctions remain mandatory:

```text
Review
≠ Approval
≠ Customer Decision
≠ Professional Authority
≠ External Execution
```

A reviewer may conclude that a Package is technically coherent while the customer still needs to approve cost or scope.

A customer may approve a business choice while a qualified professional rejects the legal route.

A Delivery Owner may accept an internal Contribution while the Owning Service still requires official evidence before updating formal state.

## 7. Reviewers need eligibility and current authority

Review authority should be governed like production authority.

A reviewer should have:

- scoped Capability;
- relevant jurisdiction and language fit;
- current evidence;
- appropriate professional qualification where required;
- independence from unresolved conflicts;
- access to the necessary sources and versions;
- time and Capacity;
- calibration history;
- escalation routes.

```text
Senior title
≠ eligible reviewer for every task
```

A reviewer who lacks the source, context or time should not be treated as having completed meaningful review.

## 8. Independence and conflict must be visible

Complete separation between producer and reviewer is not always necessary, especially in small Workplaces. The Product should nevertheless identify:

- self-review;
- peer review;
- supervisor review;
- independent professional review;
- external expert review;
- customer confirmation;
- official validation.

Higher-risk work may require separation between:

- preparer and approver;
- seller-side and buyer-side review;
- content author and legal factual reviewer;
- Provider and originating validator;
- fee recommender and commercial approver.

A reviewer should disclose material conflicts and related commercial interests.

## 9. Sampling is a governance choice, not a shortcut

Sampling can be appropriate where:

- task definition is stable;
- performer history is sufficient;
- deterministic validation covers material defects;
- the unreviewed error consequence is limited;
- sampling rates respond to quality signals;
- failed samples trigger broader review.

Sampling should increase when:

- a rule changes;
- a new contributor starts;
- error rates rise;
- source quality declines;
- a new jurisdiction is introduced;
- customer complaints emerge;
- content correction rates increase.

Sampling should not be used for reserved advice or irreversible protected actions merely to reduce cost.

## 10. Review queues should reflect deadline and harm

A simple first-in-first-out queue can be unsafe.

Priority may consider:

- official deadline;
- internal safety date;
- customer launch date;
- action reversibility;
- current blocker;
- financial exposure;
- pending Provider acceptance;
- certificate or receipt correction window;
- public-content exposure;
- number of affected customers or pages.

The reason for priority should be visible. Commercial value alone should not override legal or customer-risk urgency.

## 11. Customer-facing review should be understandable

Customers do not need the entire internal quality log. They may need to know:

- what was professionally checked;
- which facts they confirmed;
- what remains uncertain;
- which route was approved;
- what risk remains;
- what external evidence is still pending;
- whether a later change invalidated the prior decision.

```text
Reviewed by MarkReg
```

is too vague unless the service scope and responsible role are clear.

## 12. Review of public content and conversion routes

The Growth & Conversion Layer introduces review before a customer becomes a Matter.

Review may apply to:

- jurisdiction service pages;
- official-fee claims;
- filing and maintenance deadlines;
- POA and document requirements;
- case summaries;
- SEO landing pages;
- GEO answer structures;
- AI-generated recommendations;
- automated route and fee comparisons;
- conversion questions and disclaimers.

Content review should separate:

```text
Professional-fact Review
SEO Review
GEO Structure Review
Conversion Review
Brand and Editorial Review
```

A page may perform well in search while failing professional review. A legally accurate page may still create a misleading conversion route if its CTA implies an instruction or guarantee.

## 13. AI can support review without becoming the reviewer of record

AI may:

- compare versions;
- run deterministic checks;
- locate missing sources;
- flag contradictions;
- summarize evidence;
- compare a Contribution with a rubric;
- identify possible deadline or fee changes;
- draft review comments;
- prioritize queues.

AI must not:

- invent a source;
- conceal uncertainty;
- grant professional authority;
- approve its own material change without an accountable human where required;
- treat statistical confidence as legal sufficiency;
- mutate official or formal state from an unvalidated finding.

## 14. Review quality also requires review

MarkReg should evaluate reviewer performance contextually through:

- agreement and disagreement patterns;
- material issues caught or missed;
- correction quality;
- escalation judgment;
- timeliness;
- source discipline;
- consistency with current rules;
- later official and customer Outcomes.

The objective is calibration, not a universal reviewer leaderboard.

Disagreement may reveal:

- ambiguous criteria;
- outdated Knowledge;
- insufficient source access;
- genuine professional uncertainty;
- reviewer preference being mistaken for requirement.

## 15. Failure and recovery

Review failure modes include:

- wrong version reviewed;
- reviewer unavailable after Assignment;
- conflict discovered late;
- source changed during review;
- high-risk issue missed;
- reviewer exceeds authority;
- silent correction without attribution;
- approval status retained after material change;
- review bottleneck threatens a deadline.

Recovery may require:

```text
Contain affected action
→ preserve versions and evidence
→ classify impact
→ appoint eligible reviewer
→ re-review affected scope
→ notify customer or Provider where necessary
→ correct formal or public projection
→ update Capability and process evidence
```

## 16. Product implications

MarkReg requires:

- explicit review objects;
- risk and reversibility dimensions;
- review-mode policies;
- reviewer eligibility;
- exact-version binding;
- findings and limitations;
- approval separation;
- queue and deadline governance;
- conflict and independence records;
- sampling policies;
- reviewer calibration;
- change-impact invalidation;
- public-content review integration.

## 17. Commercial implications

Risk-based review supports:

- reliable standard services;
- premium expert review;
- white-label quality assurance;
- review-only Work Packages;
- safer contributor scaling;
- better customer retention;
- defensible professional fees.

The Product should not charge for “review” when the action is merely an automated formatting check, nor hide required professional review until after a low-price sale.

## 18. Operating principle

```text
Design quality before review
Classify consequence and reversibility
Bind review to an exact version
Match the reviewer to the scope
Separate finding, approval and action
Escalate uncertainty honestly
Invalidate review when material facts change
```

> Review is not a ceremonial signature at the end of production. It is the controlled point where evidence, consequence, authority and accountability meet.