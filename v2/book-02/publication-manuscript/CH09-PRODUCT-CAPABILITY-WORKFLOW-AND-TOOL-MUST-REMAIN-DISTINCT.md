# CH09 — Product, Capability, Workflow and Tool Must Remain Distinct

## The same work appears through several architectural lenses

A professional platform often describes one activity with several nouns.

A user sees a Product. A Product promises a Capability. A Workflow coordinates the work. A Tool performs one operation. A Service may own a runtime or formal object. An AI model may generate a draft. A human may review it.

These nouns are related, but they are not interchangeable.

```text
Product
≠ Capability
≠ Workflow
≠ Tool
≠ Service
≠ Implementation
```

When these distinctions are lost, the platform becomes difficult to govern. A feature flag starts to look like professional authority. A Workflow becomes the owner of the business object it coordinates. A Tool's output becomes the Capability itself. A Product interface becomes the definition of the underlying semantics.

Core exists to preserve the distinctions without absorbing every implementation detail.

## Capability is the durable outcome contract

Capability answers:

> What governed outcome can be produced, under what inputs, restrictions, evidence and review conditions?

A Capability Definition may include:

- identity and version;
- domain and purpose;
- expected outcome;
- accepted inputs;
- output contract;
- data and Knowledge dependencies;
- eligible implementation classes;
- review policy;
- risk and authority constraints;
- evidence requirements;
- compatibility and deprecation rules.

The Capability remains meaningful even when the implementation changes from a human specialist to a deterministic service, an AI-assisted route or a hybrid network.

```text
Capability
= stable outcome contract

Implementation
= one governed way to realize it
```

A Capability therefore should not be reduced to a button, prompt, script or employee skill label.

## Product is the user and commercial arrangement

Product answers:

> How does a defined audience discover, access, understand and pay for a governed set of capabilities?

A Product may combine:

- capabilities;
- interfaces;
- guidance;
- entitlement;
- workflow entry points;
- pricing and service promises;
- data projections;
- support and recovery paths.

Lite, MarkReg and Sites may use some of the same underlying Capabilities while presenting different experiences and commercial promises.

```text
same Capability
≠ same Product
```

For example, trademark-status verification may appear in Lite as an opportunity signal, in MarkReg as part of lifecycle delivery and in a public Site as a limited informational projection. The Capability contract may be related, but the Product purpose, entitlement, authority and accepted outcome differ.

## Workflow is orchestration

Workflow answers:

> How are dependencies, states, actors and transitions coordinated toward a goal?

Workflow may organize:

- clarification;
- validation;
- Work Packages;
- Assignments;
- Contributions;
- Review;
- Approval;
- Apply;
- Return and reconciliation.

Workflow does not become the professional Matter, customer Order or official state merely because it coordinates them.

```text
Workflow completed
≠ Matter completed
≠ official outcome established
```

Book 03 owns the detailed execution behavior. Book 02 must preserve the semantic boundary that permits multiple Workflow engines or implementations to operate over the same shared references.

## Tool is an execution instrument

Tool answers:

> What specific operation can this system or actor perform?

Examples include:

- document parser;
- classification engine;
- image renderer;
- official-portal connector;
- search service;
- translation model;
- email sender;
- payment gateway.

A Tool may be technically capable of performing an action without being authorized for the present request.

```text
Tool available
≠ Tool allowed
≠ Action approved
```

Tools need version, input, output, side-effect and permission contracts. They do not define the professional meaning of the Capability they support.

## Service is not automatically the Owning Service

The word Service is often overloaded.

A runtime service may host a Tool. A Product service may provide a user-facing offering. An Owning Service has formal-state authority over a defined business object. An external professional service may be delivered by a Provider.

These meanings should not be collapsed.

```text
runtime service
≠ Product service
≠ Owning Service
≠ external professional service
```

The architecture must explicitly identify which meaning applies.

## Skill is an implementation profile, not the Capability itself

A Skill may describe a procedure, agent package, human method or reusable implementation module. It can implement one or more Capabilities and can depend on Tools and Knowledge.

```text
Skill
≠ Capability
```

The same Skill may produce different outcomes under different configurations, while the same Capability may be implemented by different Skills.

This is especially important for AI. A prompt or agent configuration is not a stable professional contract. It is a versioned implementation that must be evaluated against the Capability Definition.

## Product feature must not become semantic authority

A Product may introduce a local feature such as:

- buyer matching;
- maintenance lead ranking;
- filing-package preparation;
- content generation;
- provider route recommendation.

The existence of the feature does not automatically create a new Core object or redefine a shared term.

```text
Product feature
≠ Core semantic activation
```

The feature may first use existing references and local profiles. Only repeated cross-product interoperability need should trigger the F0–F4 admission process.

## Example: AI-assisted trademark search

Consider an AI-assisted search experience.

The Product may be MarkReg. The Capability may be `Trademark Search Decision Support`. The Workflow may collect the mark, goods and jurisdiction, retrieve sources, generate candidates, obtain review and present options. The Tools may include search APIs, similarity models and report generators. A professional reviewer may hold the authority to issue the final opinion.

```text
Product: MarkReg
Capability: Search Decision Support
Workflow: governed search route
Tools: retrieval, similarity and rendering
Professional Authority: qualified reviewer
Outcome: reviewed search decision product
```

None of these components should be named simply `search` in the shared contract.

## Example: content production in Lite

Lite may offer a content-production Product experience. The Capability may be `Source-backed Trademark Content Drafting`. A Workflow may assemble a Content Brief, Claim Ledger, visual assets, review and publication approval. Tools may include retrieval, AI generation and deterministic rendering.

The Product owns the experience. Knowledge preserves sources and claims. Execution governs production. Sites may publish the result. Core supplies shared references and authority vocabulary.

```text
Product composition
≠ layer collapse
```

## Compatibility implications

The distinctions allow independent evolution.

- a Product can redesign its interface without changing Capability meaning;
- a Workflow can be replaced without changing formal Matter identity;
- a Tool can be upgraded without redefining the outcome contract;
- an implementation can move from M2 to M3 without creating a new Product;
- a Service can be split while preserving public references.

Every public contract should therefore reference the correct layer explicitly.

## Constitutional rule

```text
Core standardizes the boundaries among Product,
Capability, Workflow, Tool, Service and Implementation.
It does not merge them into one universal object
or prescribe one runtime architecture.
```
