# CH15 — M0–M5 Human–AI Collaboration Modes

## 1. Human–AI collaboration needs explicit operating modes

“AI-assisted” is too vague to govern professional work. It can mean anything from showing a reference answer to allowing an agent to invoke external tools.

MarkOrbit therefore uses M0–M5 as collaboration modes. The mode governs how work is produced, reviewed, disclosed and authorized.

```text
M0 — Human-only
M1 — AI Reference
M2 — AI Assist
M3 — AI Draft, Human Approve
M4 — AI Execute under Governance
M5 — Hybrid Professional Network
```

The mode is not merely a user-interface preference. It is an execution policy.

## 2. The mode applies to a specific Capability invocation

A Workplace, person or Product does not have one permanent AI mode for everything.

```text
M3 for Content Drafting
≠ M3 for Official Filing
```

The selected mode should be bound to:

- Capability and version;
- Work Package;
- user and represented role;
- jurisdiction;
- risk tier;
- data scope;
- tool permissions;
- Review policy;
- Approval policy;
- retention and memory policy;
- external-action boundary.

## 3. M0 — Human-only

In M0, substantive production is performed by humans without AI-generated content or AI-assisted judgment.

Deterministic software may still support basic operations such as file validation, checksum generation or date formatting if policy permits.

M0 may be required where:

- customer or Workplace policy prohibits AI;
- data sensitivity is exceptionally high;
- professional regulation restricts AI use;
- source or model reliability is insufficient;
- assessment is intended to measure unaided performance;
- a conflict or incident requires isolated human review.

```text
M0
≠ No Software
```

It means no AI contribution to the governed substantive Outcome.

## 4. M1 — AI Reference

In M1, AI provides reference material without editing or producing the official work object.

Examples include:

- explaining a concept;
- showing examples;
- retrieving public knowledge candidates;
- suggesting questions to consider;
- summarizing a non-authoritative source.

The human remains responsible for creating the Contribution.

```text
AI Reference
≠ Source Authority
≠ Work Product
```

The reference may inform judgment but should not be silently inserted into formal work.

## 5. M2 — AI Assist

In M2, AI assists a human performer during production.

Possible assistance includes:

- classification;
- extraction;
- translation candidate;
- version comparison;
- checklist generation;
- issue spotting;
- formatting;
- source organization;
- draft fragments.

The human remains the primary producer and must dispose of the AI suggestions.

The record should preserve:

- assistance type;
- model and version;
- source set;
- accepted, modified and rejected suggestions;
- human Contribution.

```text
AI Suggestion Accepted
≠ AI Becomes the Performer of Record
```

## 6. M3 — AI Draft, Human Approve

In M3, AI produces a substantial draft, and a human reviews, revises and accepts the final Contribution or Outcome candidate.

Examples include:

- communication draft;
- structured search report;
- service recommendation draft;
- content page draft;
- Work Package decomposition;
- evidence summary;
- filing-package candidate where permitted.

The human must have adequate time, information and competence to review the draft.

```text
Human Clicked Approve
≠ Meaningful Human Review
```

M3 fails when the human becomes a ceremonial approver of work they cannot evaluate.

## 7. M4 — AI Execute under Governance

In M4, AI may perform bounded execution, potentially including tool use or internal state transitions.

M4 requires explicit controls:

- bounded Capability;
- allowed tools and actions;
- prohibited actions;
- exact data scope;
- risk tier;
- specific Approval rule;
- Preview requirement;
- idempotency;
- maximum cost;
- stop conditions;
- human escalation;
- observability;
- Evidence Contract;
- recovery route.

```text
M4
≠ Autonomous General Agent
```

An M4 capability might automatically validate a known schema, reconcile a low-risk record or send a previously approved standardized reminder. It does not imply authority to file applications, appoint providers, move funds or communicate legal positions without the required governance.

## 8. M5 — Hybrid Professional Network

M5 coordinates humans, AI, deterministic systems, Contributors, reviewers and Providers in one governed delivery route.

Example:

```text
Deterministic Extraction
→ AI Issue Classification
→ Contributor Preparation
→ Senior Professional Review
→ Customer Approval
→ Provider Submission
→ Official Evidence Validation
```

M5 is not “AI plus many people.” It is a typed network in which every participant has a defined role, authority and Evidence Return.

## 9. Mode and risk tier are independent

M0–M5 describes collaboration structure. R0–R4 describes Review and execution risk.

```text
M-mode
≠ R-tier
```

Examples:

- M0/R4: human-only final legal review;
- M2/R1: AI-assisted low-risk normalization with sampling;
- M3/R2: AI draft with full professional review;
- M4/R0: deterministic-like AI action under strict policy;
- M5/R4: hybrid network ending in qualified final authority.

## 10. Mode selection must be explainable

The mode may depend on:

- customer preference;
- Workplace policy;
- jurisdiction;
- data sensitivity;
- Capability maturity;
- model evaluation;
- performer proficiency;
- deadline;
- cost;
- reversibility;
- available reviewers;
- legal or contractual restrictions.

```text
Cheaper Mode
≠ Permitted Mode
```

## 11. Proficiency can change assistance, not authority

Less experienced performers may receive stronger guidance, more examples and mandatory Review. More experienced performers may receive less intrusive assistance.

But proficiency does not create legal authority.

```text
Higher Proficiency
≠ Professional Qualification
≠ Protected-action Authority
```

## 12. Mode transitions must be recorded

A task may move between modes.

Examples:

```text
M2 → M3
```

when AI assistance expands into full drafting, or:

```text
M4 → M0
```

when an incident requires human-only recovery.

The transition record should explain:

- previous mode;
- new mode;
- reason;
- affected versions;
- new Review requirements;
- whether prior Approval remains valid.

## 13. AI mode must be disclosed where material

Disclosure may be required to:

- customer;
- reviewer;
- professional authority;
- Provider;
- auditor;
- assessor.

Disclosure should be proportional and useful. It should explain the role AI played, not merely display a generic “AI used” label.

```text
AI Used
≠ Adequate Disclosure
```

## 14. The human role must be real

Meaningful human oversight requires:

- access to source material;
- ability to reject AI output;
- sufficient competence;
- adequate time;
- clear responsibility;
- no incentive to approve blindly;
- visibility into uncertainty and tool use.

A system should not describe M3 or M4 as human-supervised when the human cannot actually intervene.

## 15. Mode-specific evidence

Execution should retain evidence appropriate to the mode.

### M0

- human performer;
- sources;
- work history;
- Review.

### M1

- AI reference;
- model and version;
- human-authored Contribution.

### M2

- AI suggestions;
- human disposition;
- final Contribution.

### M3

- AI draft;
- human edits;
- Review and acceptance.

### M4

- policy;
- Preview and Approval;
- tool calls;
- idempotency;
- stop and escalation events;
- Return.

### M5

- all typed Contributions, Reviews, provider returns and synthesis records.

## 16. Memory and learning are mode-bound

AI use does not automatically authorize retention, cross-task memory or training.

```text
AI Invocation
≠ Memory Consent
≠ Training Consent
```

Each mode should define:

- session retention;
- reusable memory;
- customer-specific memory;
- de-identification;
- learning-candidate generation;
- prohibited reuse.

## 17. Mode failure must trigger fallback

Failure signals include:

- unsupported source;
- hallucination;
- tool misuse;
- uncertainty above threshold;
- repeated correction;
- unauthorized disclosure;
- model outage;
- reviewer rejection;
- ambiguous external effect.

Fallback may include:

```text
Pause
Reduce Autonomy
Require Full Review
Switch Model
Switch to Human Production
Escalate to Professional Authority
Enter Recovery
```

## 18. Products cannot invent their own mode semantics

Lite, MarkReg, Sites and other Products may present different interfaces, but M0–M5 must retain shared meaning.

```text
Product-specific Label
≠ Product-specific Authority Model
```

Execution remains responsible for applying the selected mode to Capability invocation and evidence.

## 19. Commercial pressure must not determine mode silently

A provider or Product may prefer a mode because it is faster or more profitable. That preference cannot override customer choice, policy, professional requirements or risk.

```text
Higher Margin
≠ Safer Collaboration Mode
```

## 20. The governing model

```text
Capability Request
→ Risk and Policy Context
→ M-mode Selection
→ Implementation Binding
→ Production and Review
→ Approval and Apply Boundary
→ Evidence and Outcome
```

M0–M5 gives MarkOrbit a language for increasing intelligence and automation without making responsibility disappear.