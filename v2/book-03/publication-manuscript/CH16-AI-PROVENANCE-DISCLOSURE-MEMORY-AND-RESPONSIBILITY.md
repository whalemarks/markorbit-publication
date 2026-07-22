# CH16 — AI Provenance, Disclosure, Memory and Responsibility

## 1. AI output must remain attributable

A professional execution system cannot treat AI output as if it appeared from nowhere.

Every material AI-assisted Contribution should preserve sufficient provenance to explain:

- which model and version were used;
- which Capability Request and Work Package applied;
- which instructions or prompt references governed the invocation;
- what sources and retrieval time were used;
- what tools were called;
- what data was disclosed;
- what collaboration mode applied;
- what uncertainty or limitations were reported;
- what human disposition followed.

```text
AI Output
≠ Source-free Professional Fact
```

## 2. Provenance is more than a model name

Knowing that a draft came from a particular model is useful but insufficient.

A complete provenance record may include:

```text
Model Identity
Model Version
System and Policy Version
Capability Version
Instruction Reference
Input Object Versions
Source Set
Tool Calls
Generation Time
Memory Context
Human Edits
Review and Approval
```

This allows later reconstruction when sources, models or policies change.

## 3. Source grounding must remain visible

AI may combine official sources, Provider practice, internal Knowledge and inference. Those categories must not be blended into one voice.

Useful source classifications include:

```text
Official Source
Authoritative Professional Source
Provider-reported Practice
Customer-provided Fact
Internal Verified Knowledge
Inference
Unknown
```

```text
Confident Language
≠ Authoritative Source
```

Where a conclusion depends on a Provider report or inference, the output should say so.

## 4. Retrieval date and freshness matter

Trademark fees, procedures, forms, software interfaces and Provider practices change.

An AI answer should retain:

- source date;
- retrieval date;
- jurisdiction;
- effective period;
- freshness status;
- recheck trigger.

```text
Previously Correct
≠ Currently Correct
```

An accepted AI-assisted Outcome may expire when its sources change.

## 5. AI disclosure should explain role, not create noise

Disclosure should answer the practical question:

> What did AI do, and who remained responsible?

Examples include:

- AI assisted with extraction; human verified all fields;
- AI drafted the communication; Relationship Owner reviewed and sent it;
- AI compared evidence; qualified professional determined sufficiency;
- AI executed a bounded internal action under approved M4 policy.

A generic “AI may have been used” notice is too weak.

## 6. Disclosure audiences differ

Different audiences may need different disclosure:

- performer;
- reviewer;
- approver;
- customer;
- Provider;
- regulator;
- assessor;
- auditor.

The customer may need a clear explanation of material AI involvement. The reviewer may need detailed provenance. The auditor may need immutable tool logs.

```text
One Disclosure Text
≠ Adequate for Every Audience
```

## 7. AI responsibility remains allocated to accountable actors

AI does not hold customer relationships, professional licences, contractual responsibility or formal-state authority.

```text
AI Generated
≠ AI Accountable Party
```

Responsibility remains distributed among:

- requester;
- performer;
- Delivery Owner;
- reviewer;
- approver;
- Professional Authority;
- Product-owning Workplace;
- model or tool provider under applicable contract;
- Owning Service for formal-state validation.

The system should not use AI as a reason to make responsibility untraceable.

## 8. Human approval must be meaningful

A human cannot responsibly approve AI work when they lack:

- access to sources;
- competence to assess the output;
- visibility into uncertainty;
- time to review;
- power to reject;
- understanding of downstream action.

```text
Human in the Loop
≠ Meaningful Human Control
```

The Review policy should reflect the real capacity of the human reviewer.

## 9. Memory must be purpose-bound

AI memory can improve continuity, but it also creates privacy, accuracy and authority risks.

Memory categories should remain distinct:

```text
Session Context
Task Context
Matter Context
Customer-authorized Memory
Workplace Memory
Reusable Knowledge Candidate
Model-training Data
```

```text
Conversation Context
≠ Permanent Memory
≠ Shared Knowledge
≠ Training Permission
```

## 10. Customer-specific memory needs explicit governance

Customer memory may contain:

- preferred communication style;
- confirmed applicant identity;
- commercial priorities;
- recurring service choices;
- authorized contact information;
- past decisions.

It should record:

- source;
- confirmer;
- purpose;
- scope;
- expiry;
- correction method;
- deletion or retention rule;
- permitted Products and Workplaces.

An AI inference should not become permanent customer memory without validation.

## 11. Memory may become stale or wrong

Examples include:

- former employee still treated as signatory;
- old address reused after ownership change;
- previous filing preference applied to a new jurisdiction;
- historical Provider requirement treated as current rule.

Memory should support:

```text
Current
Recheck Due
Conflicted
Superseded
Withdrawn
Unknown
```

## 12. Cross-customer memory requires strong separation

Patterns learned from one customer must not expose that customer to another.

```text
Pattern Reuse
≠ Customer-data Reuse
```

Knowledge distillation should require rights review, de-identification, professional validation and governance before broader use.

## 13. AI training is a separate permission domain

Operational access does not create training consent.

```text
Data Used for Delivery
≠ Data Authorized for Model Training
```

Likewise:

```text
Contribution Accepted
≠ AI-training Consent

De-identified
≠ Automatically Authorized for Training
```

Training use should define dataset rights, purpose, retention, model scope, withdrawal handling and security.

## 14. Prompt and instruction records need proportional retention

High-impact AI work may require retaining the relevant instruction chain. Lower-risk work may retain a policy reference and structured metadata instead of every transient token.

Retention should consider:

- audit need;
- confidential information;
- intellectual property;
- security;
- reproducibility;
- regulatory requirements;
- storage cost.

```text
More Retention
≠ Better Governance by Default
```

## 15. Tool use creates additional provenance

When AI invokes search, code, connectors or external systems, the record should include:

- tool identity and version;
- input parameters where safe;
- returned evidence;
- side-effect classification;
- authorization;
- idempotency key;
- failure or timeout;
- data disclosed.

```text
Model Response
≠ Complete Tool Audit
```

## 16. AI uncertainty must influence execution

Uncertainty can arise from:

- incomplete sources;
- source conflict;
- ambiguous customer facts;
- low-confidence extraction;
- unfamiliar jurisdiction;
- model limitation;
- missing evidence;
- changing rules.

Uncertainty should trigger actions such as:

```text
Request Clarification
Require Source Verification
Increase Review Tier
Reduce Autonomy
Block Apply
Escalate to Professional Authority
```

It should not be hidden merely to make the interface feel decisive.

## 17. Hallucination is one failure mode, not the only one

AI risks also include:

- correct fact applied to the wrong Matter;
- stale source;
- incomplete exception;
- excessive disclosure;
- wrong tool target;
- unsupported legal certainty;
- biased routing;
- fabricated citation;
- failure to preserve version differences.

Governance must focus on Outcome risk rather than only factual fabrication.

## 18. AI incident handling

AI incidents may require:

- stop or suspend the model binding;
- contain affected Outputs;
- identify downstream use;
- preserve logs;
- notify Delivery Owners;
- re-review accepted Outcomes;
- correct customer communication;
- retract public content;
- update capability evaluation;
- change policy or prompts;
- switch to human-only mode.

```text
Prompt Fixed
≠ Incident Resolved
```

## 19. Model changes can invalidate prior evaluation

A new model version may behave differently even under the same prompt.

```text
Model v1 Evaluated
≠ Model v2 Evaluated
```

Implementation Binding should specify the model version or governed release channel and define re-evaluation triggers.

## 20. Evaluation must reflect actual Capability use

Generic benchmark performance does not prove suitability for a MarkOrbit Capability.

Evaluation should include:

- representative jurisdiction cases;
- source grounding;
- version control;
- privacy behavior;
- refusal and escalation;
- tool safety;
- deadline and fee accuracy;
- multilingual performance;
- adversarial and incomplete inputs;
- human-review burden.

```text
High General Benchmark Score
≠ Production Authorization
```

## 21. AI output may create a learning candidate, not Canon

Execution outcomes can produce candidates for:

- prompt improvement;
- Capability evaluation;
- Knowledge correction;
- workflow redesign;
- training scenario;
- product guidance.

But:

```text
Successful AI Output
≠ Canonical Knowledge
```

Rights, quality and authority review remain required.

## 22. Product boundaries remain intact

Guide may use AI to explain and prepare decisions. Products may invoke AI-enabled Capabilities. Execution governs the invocation. Brain and Knowledge govern verified reusable knowledge. Owning Services govern formal records.

```text
AI Answer in Guide
≠ Workflow
≠ Approval
≠ Apply
≠ Formal-state Truth
```

## 23. The governing model

```text
Governed Request
→ Mode and Model Binding
→ Source- and Tool-aware AI Contribution
→ Provenance and Uncertainty
→ Human or Qualified Review
→ Specific Approval
→ Bounded Apply
→ Evidence
→ Learning Candidate under Separate Governance
```

AI becomes trustworthy in MarkOrbit not by pretending it is infallible, but by making its role, evidence, limits and human responsibility visible.