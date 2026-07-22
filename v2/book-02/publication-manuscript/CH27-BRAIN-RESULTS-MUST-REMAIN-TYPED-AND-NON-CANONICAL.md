# CH27 — Brain Results Must Remain Typed and Non-canonical

## Intelligence becomes dangerous when every answer looks the same

A Brain layer may retrieve documents, compare records, infer relationships, recommend routes, generate candidates and explain complex material.

Those outputs can appear in the same chat, report or interface. They do not have the same semantic status.

Book 02 therefore requires Brain results to remain typed as at least:

```text
Retrieval
Inference
Recommendation
Candidate
Explanation
```

The permanent boundary is:

```text
Brain Result
≠ Canonical Fact
≠ Decision
≠ Approval
≠ Formal State
```

Brain may cite accepted facts and Knowledge Claims. It may not silently convert its processing result into business or legal truth.

## Brain is a reasoning layer, not a hidden authority

Brain can combine:

- Data Product records;
- Knowledge Sources, Documents and Claims;
- Matter or Task context;
- Workplace policy;
- Capability Definitions;
- prior accepted Outcomes;
- model and tool results.

Its purpose is to make that material useful for a declared question or next decision.

Its purpose is not to become a universal owner of:

- customer memory;
- official data;
- professional decisions;
- Product policy;
- formal-state transitions.

```text
Brain can reason across layers
≠ Brain owns those layers
```

## Retrieval Result reports what was found

Retrieval answers:

> Which relevant Sources, Documents, Claims or Data Records were found for this request?

A Retrieval Result should preserve:

- query or purpose;
- requesting context;
- source set;
- retrieval time;
- filters and jurisdiction;
- ranking or selection method;
- returned object versions;
- missing or inaccessible sources;
- freshness and rights constraints.

```text
retrieved
≠ verified
≠ applicable
≠ accepted
```

A search system may retrieve an old form, a superseded fee notice or a provider-specific practice. Retrieval success says only that the material was found.

## Inference Result states a derived proposition

Inference answers:

> What proposition may follow from the available inputs, model, rules or comparison?

Examples include:

- two owner names may refer to the same Organization;
- a status event may create a deadline candidate;
- a trademark may present a similarity risk;
- a customer may need a maintenance service;
- a provider route may be suitable.

An Inference Result should preserve:

- input records and versions;
- derivation method;
- model, rule or actor;
- assumptions;
- confidence or uncertainty;
- alternative interpretations;
- conflicts;
- intended purpose;
- review requirement.

```text
high-confidence inference
≠ verified fact
```

Confidence measures model or rule behavior. It does not establish external authority.

## Recommendation Result proposes a route

Recommendation answers:

> Given the stated Need, constraints and evidence, which option appears preferable and why?

A Recommendation Result may include:

- considered options;
- comparison criteria;
- expected benefit;
- cost and risk;
- prerequisites;
- Unknowns;
- professional or customer decision required;
- expiry or recheck trigger.

```text
Recommendation
≠ Customer Instruction
≠ Professional Approval
≠ Permission to Execute
```

A country, class, goods, provider or filing recommendation becomes actionable only through the applicable decision and execution route.

## Candidate Result proposes a record or transition

Candidate answers:

> What structured object, correction, relationship or state transition should be considered for acceptance?

Examples include:

- Entity Resolution Candidate;
- Deadline Candidate;
- applicant-address correction candidate;
- Knowledge Claim Candidate;
- Opportunity Candidate;
- provider route candidate;
- proposed Work Package decomposition.

A Candidate Result should identify:

- target object or concept;
- proposed value or relationship;
- supporting and conflicting Evidence;
- source and model versions;
- intended purpose;
- acceptance authority;
- expiry;
- correction and rejection path.

```text
Candidate generated
≠ Candidate accepted
≠ Formal State mutated
```

The accepting service or reviewer must decide whether the candidate is sufficient for the declared purpose.

## Explanation Result makes reasoning understandable

Explanation answers:

> How should the user understand a fact, rule, option, result or limitation?

Explanation may summarize:

- source material;
- a professional concept;
- a calculation;
- a Product route;
- a Decision;
- a formal-state change;
- the role AI played.

An Explanation should preserve citations, source status and the distinction between reported fact and interpretation.

```text
clear explanation
≠ authoritative source
```

An explanation can be accurate and useful without being the legal instrument, official notice or professional opinion it describes.

## One response may contain several result types

A customer-facing answer may contain:

```text
Retrieval:
these three official sources were found

Inference:
the deadline may fall on 10 September

Recommendation:
verify the triggering event before filing

Candidate:
create a deadline review Work Package

Explanation:
the date depends on whether the notice was officially served
```

The system should not flatten these into one paragraph with one confidence score.

Typed segments make it possible to apply different review, display, retention and authority rules.

## Brain Result envelope

A shared Brain Result profile may preserve:

- result identity and type;
- purpose or question;
- requester and Workplace context;
- Product Installation and Capability reference;
- source, Claim and Data Product versions;
- model, policy, prompt and tool versions;
- generation time;
- jurisdiction and language;
- data and memory scope;
- assumptions and Unknowns;
- confidence where meaningful;
- limitations;
- expiration or recheck trigger;
- required reviewer or accepting authority;
- downstream Candidate target;
- human edits and disposition.

The envelope enables interoperability without promoting every Brain output into Core business state.

## Confidence is not one universal scale

A retrieval rank, extraction probability, model confidence, source authority and professional certainty are different signals.

```text
Retrieval Score
≠ Source Authority
≠ Factual Confidence
≠ Legal Certainty
≠ Action Safety
```

The platform should label the type of score and the decision it may support.

A model may be confident that it extracted the date printed in a document while the document itself is obsolete. A strong official source may still be ambiguous for the present facts.

## Brain must preserve source categories

Brain may combine official records, provider practice, customer statements, internal Knowledge and inference. The result must preserve the category of each supporting statement.

```text
Confident Language
≠ Authoritative Source
```

Where a conclusion depends on provider practice or inference, the result should say so rather than present it as a universal rule.

## Brain must preserve Unknown

Unknown is not a formatting defect to be removed by language generation.

Brain should be able to return:

- source missing;
- sources conflict;
- applicability unclear;
- customer fact unconfirmed;
- professional review required;
- no safe recommendation;
- external result unresolved.

```text
Unknown
≠ prompt failure
≠ permission to complete the answer by guessing
```

Unknown may cause Book 03 Execution to request clarification, increase review, reduce autonomy or block Apply.

## Brain does not own memory by implication

Brain may use several kinds of context:

```text
Session Context
Task Context
Matter Context
Customer-authorized Memory
Workplace Memory
Reusable Knowledge Candidate
Model-training Data
```

These are separate permission domains.

```text
Conversation Context
≠ Permanent Memory
≠ Shared Knowledge
≠ Training Permission
```

A model inference about a customer's preference or identity should not become permanent memory without validation and purpose authorization.

## Brain cannot self-promote its result

A Brain system must not:

- generate a Claim and mark it verified by itself;
- recommend a route and treat the recommendation as Approval;
- create a Candidate and mutate the target record;
- generate a Contribution and act as its only qualified reviewer;
- infer customer intent and issue a protected instruction;
- upgrade its own Production Authorization.

```text
AI generated
+ AI reviewed
≠ independent qualified acceptance
```

Deterministic checks and secondary models may assist review, but they do not create the missing human, professional or organizational authority.

## Brain versions must remain visible

Brain behavior changes when any of the following changes:

- model;
- prompt or instruction;
- retrieval index;
- source set;
- tool;
- policy;
- memory;
- output schema;
- autonomy level.

```text
Brain Result under version A
≠ reproducible under version B by default
```

Material changes may require reevaluation, Simulation or supervised production before a route is trusted again.

## Brain output may expire

A Recommendation or Explanation may become stale when:

- a fee changes;
- an official rule changes;
- a customer fact changes;
- a provider loses eligibility;
- a deadline passes;
- a Product policy changes;
- a source is corrected;
- the underlying Matter state changes.

A result should carry an effective context and recheck trigger rather than remain permanently valid because it was once accepted.

## Product presentation must not hide type

Guide, Lite, MarkReg and Sites may present Brain results in different experiences. The interface can simplify language, but it must not erase whether the content is:

- retrieved source material;
- inferred possibility;
- recommendation;
- unaccepted candidate;
- explanation of an accepted fact.

```text
one conversational interface
≠ one epistemic status
```

High-impact outputs should make the source, limitations and responsible actor visible to the appropriate audience.

## Execution boundary

Book 03 determines how a Brain Result becomes part of real work.

A possible route is:

```text
Brain Result
→ Contribution or Candidate
→ typed Review
→ Decision or Approval
→ governed Apply
→ Evidence Return
→ Owning Service validation
```

Brain does not skip the route because the model can call a Tool.

```text
Model can invoke Tool
≠ protected action authorized
```

## Knowledge boundary

Knowledge preserves reusable sourced Claims and Versions. Brain performs context-specific retrieval, inference, recommendation and explanation over them.

```text
Knowledge Claim
≠ Brain Inference

Brain Explanation
≠ Knowledge Source
```

A reviewed Brain result may become a Knowledge Candidate through a separate promotion process. It does not automatically enter shared Knowledge.

## Candidate status

The reconciliation classifies Brain Result as an F2/F3 typed intelligence-result profile.

This chapter explains the minimum type distinctions and envelope. It does not activate a universal Brain Result object, prescribe one model provider or grant Brain formal-state or professional authority.

## Constitutional rule

```text
Retrieval reports what was found.
Inference reports what may follow.
Recommendation proposes a route.
Candidate proposes a record or transition.
Explanation makes meaning understandable.

Every Brain Result remains typed,
attributable, versioned and non-canonical
until the applicable authority accepts it
for a declared purpose.
```
