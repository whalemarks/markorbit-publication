# CH06 — Implementation Binding Across Human, AI and Deterministic Systems

## 1. Capability describes the Outcome, not the performer

A Capability defines what governed Outcome the platform can request. It does not permanently define who or what must perform the work.

The same Capability may be fulfilled through:

- deterministic software;
- AI assistance;
- an internal team member;
- a certified Contributor;
- an expert Reviewer;
- a partner Workplace;
- a Provider Organization;
- a hybrid route.

The decision that connects a Capability Request to one of these routes is the **Implementation Binding**.

```text
Capability
≠ Implementation

Capability Request
≠ Performer Selection
```

## 2. Products request Outcomes; they do not silently choose authority

Lite, MarkReg, Sites or another Product may present a user action such as:

- verify a trademark status;
- generate a content pack;
- review a document;
- prepare an OA response;
- obtain a local filing route;
- validate evidence.

The Product may recommend an experience, but it should not silently decide that:

- AI may make the final judgment;
- a specific Contributor is authorized;
- an external Provider is appointed;
- a connector may submit;
- customer data may be disclosed.

```text
Product Experience
≠ Execution Authority
```

Execution validates or selects the binding under policy.

## 3. Binding must be explicit and versioned

An Implementation Binding should identify:

- the Capability Request;
- the selected implementation class;
- the exact implementation or candidate set;
- version;
- applicable collaboration mode;
- data scope;
- allowed actions;
- Review policy;
- authority conditions;
- cost basis;
- expected Evidence Return;
- fallback route;
- expiry and revocation.

If any of these materially changes, the binding should be revised rather than silently reused.

## 4. Deterministic systems are narrow, testable implementations

Deterministic implementations are appropriate when:

- the input contract is clear;
- the transformation is stable;
- the expected output is testable;
- ambiguity is low;
- the operation is reversible or safely contained;
- failures can be detected;
- the version is controlled.

Examples may include:

- schema validation;
- date normalization;
- duplicate detection;
- document checksum generation;
- template rendering;
- deterministic fee arithmetic;
- field mapping;
- package completeness checks.

But deterministic does not mean authoritative.

```text
Rule Executed Correctly
≠ Source Rule Correct
≠ Legal Conclusion Correct
```

A fee calculator may perfectly apply an outdated fee table. A deadline engine may correctly calculate from the wrong trigger date.

## 5. AI implementations operate under collaboration modes

AI can support:

- extraction;
- classification;
- summarization;
- translation candidates;
- drafting;
- comparison;
- anomaly detection;
- recommendation;
- structured question generation.

The binding must specify the collaboration mode, such as:

```text
M0 — Human-only
M1 — AI Reference
M2 — AI Assist
M3 — AI Draft, Human Approve
M4 — AI Execute under Governance
M5 — Hybrid Professional Network
```

The mode is not merely a user-interface preference. It determines:

- what AI may see;
- what AI may produce;
- whether a human must review;
- whether Apply is permitted;
- what disclosure is required;
- what evidence and provenance must be retained.

## 6. AI ability is not AI permission

A model may be technically able to draft a filing instruction, infer a deadline or recommend a legal response. That does not mean the current binding allows it.

```text
Model Capability
≠ Product Entitlement
≠ Invocation Scope
≠ Professional Authority
≠ Apply Authority
```

The binding should restrict:

- purpose;
- input objects;
- source set;
- allowed output type;
- maximum autonomy;
- memory use;
- tool access;
- external communication;
- formal-state mutation.

## 7. Human implementations also require policy

A human performer is not automatically safe because they are human.

Execution must still establish:

- identity;
- represented role;
- Capability Evidence;
- Production Authorization;
- Professional Qualification where required;
- conflict status;
- capacity;
- data scope;
- Review requirement;
- compensation terms;
- communication boundaries.

```text
Human Judgment
≠ Unreviewable Judgment
```

## 8. Contributor and Provider bindings are different

A Contributor typically performs a bounded Work Package and returns a Contribution.

A Provider Organization may accept a professional service engagement, perform external work and return Provider Evidence.

```text
Contributor Assignment
≠ Provider Appointment

Contribution
≠ Provider Return
```

The two routes differ in:

- authority;
- professional responsibility;
- customer visibility;
- commercial structure;
- evidence obligations;
- external execution rights;
- failure and replacement logic.

## 9. Hybrid binding is often the normal route

A complex Outcome may use several implementations:

```text
Deterministic extraction
→ AI issue classification
→ Contributor preparation
→ Professional Review
→ Customer Approval
→ Provider execution
→ Official evidence validation
```

Hybrid work should not be represented as if one actor performed everything.

Each contribution must retain:

- performer;
- tool or model;
- version;
- scope;
- Review status;
- authority level;
- evidence.

## 10. Binding selection follows mandatory gates

A route cannot be selected solely because it is fast, cheap or highly ranked.

Mandatory gates may include:

- Capability support;
- risk class;
- jurisdiction;
- professional qualification;
- data residency;
- conflict;
- customer or Workplace restrictions;
- Review availability;
- deadline feasibility;
- connector safety;
- commercial approval.

Only candidates passing mandatory gates should enter route comparison.

```text
High Quality Score
≠ Mandatory Gate Passed
```

## 11. Route recommendation must disclose platform interests

Execution may consider:

- quality history;
- availability;
- speed;
- cost;
- evidence-return reliability;
- customer preference;
- Workplace preference;
- existing relationship;
- platform commercial interest.

If the recommended route benefits MarkReg, MGSN or another platform-operated service, the relevant commercial interest should be visible at the appropriate decision point.

```text
Platform-preferred Route
≠ Objectively Mandatory Route
```

## 12. Binding and Assignment remain distinct

An Implementation Binding may identify that a Work Package requires a human Reviewer or an MGSN Provider. It does not by itself create an accepted Assignment or Provider Appointment.

```text
Implementation Class Selected
→ Candidate Eligibility
→ Candidate Selection
→ Offer / Appointment
→ Acceptance
→ Active Assignment or Engagement
```

## 13. Binding and Apply remain distinct

A binding may authorize preparation or review while prohibiting external action.

Examples:

- AI may draft but not send;
- Contributor may normalize goods but not approve them;
- Reviewer may recommend but not bind the customer;
- Provider may prepare but not file until customer approval;
- connector may validate payload but not submit.

```text
Bound to Work
≠ Authorized to Apply
```

## 14. Fallback routes must be predefined

Implementations fail. Models become unavailable. Contributors decline. Providers go silent. Connectors time out.

A safe binding may define:

- retry conditions;
- human fallback;
- alternate Provider;
- escalation to expert review;
- pause conditions;
- customer notification;
- data-access revocation;
- reconciliation before switching.

Fallback must not create duplicate external action.

```text
Primary Route Failed
≠ Alternate Route May Act Immediately
```

## 15. Binding changes may invalidate prior Review

If an Outcome prepared by one implementation is transferred to another, the system must determine whether prior Review remains valid.

Material changes may include:

- different model version;
- different source set;
- new Provider;
- changed jurisdiction interpretation;
- expanded Work Package;
- altered document package;
- changed fee or deadline.

```text
Output Looks Similar
≠ Prior Review Still Applies
```

## 16. Model and tool provenance must remain available

For AI and deterministic tools, Execution should preserve:

- tool or model identity;
- version;
- invocation policy;
- source references;
- input object versions;
- output version;
- confidence or uncertainty where relevant;
- human disposition;
- later correction.

This does not require exposing sensitive internal prompts publicly, but the system must retain enough evidence to reconstruct consequential work.

## 17. Memory and learning are separate permissions

An AI binding may permit inference over current inputs without permitting long-term memory or shared learning.

```text
Inference Allowed
≠ Memory Allowed
≠ Shared Learning Allowed
≠ Model Training Allowed
```

These permissions should be explicit in the binding.

## 18. Binding quality should be evaluated by Outcomes

The best implementation is not necessarily the one with the highest automation rate.

Evaluation should consider:

- Outcome accuracy;
- Review burden;
- deadline reliability;
- correction rate;
- evidence completeness;
- customer impact;
- privacy and relationship protection;
- recovery cost;
- total expected cost.

```text
More Automated
≠ Better Governed
```

## 19. The binding record supports accountability

When a result is questioned, MarkOrbit should be able to answer:

- why this implementation was allowed;
- why it was selected;
- what it was permitted to do;
- which version acted;
- what sources were used;
- who reviewed it;
- what authority applied;
- what changed afterward.

Without a binding record, hybrid work becomes an opaque chain of prompts, messages and undocumented human intervention.

## 20. Chapter locks

```text
Capability
≠ Implementation

Product Recommendation
≠ Implementation Authority

AI Ability
≠ AI Permission

Human Performer
≠ Unbounded Authority

Contributor Assignment
≠ Provider Appointment

Implementation Binding
≠ Assignment Acceptance

Implementation Binding
≠ Apply Authority

Automation Rate
≠ Execution Quality

Inference Permission
≠ Memory or Training Permission
```
