# B04-CH-15 — Capability Discovery and Skill Selection

**Status:** Release Candidate 1  
**Chapter Map:** B04-TOC-V0.1  
**Part:** Part III — Knowledge, Intelligence and Capability Consumption

## Chapter Purpose

CH13 defined how Workplace discovers information, preserves provenance, and assembles authorized professional context.

CH14 defined how Workplace consumes governed Knowledge through the logical Brain without centralizing private organizational memory or transferring professional judgment to the Knowledge layer.

This chapter defines the next architectural movement:

> How does Workplace identify what function is required, discover an eligible Capability, and select a concrete Skill without confusing ability, implementation, provider, permission, Product feature, Agent identity, Workflow, or execution authority?

Knowledge tells Workplace what is understood.

Capability tells Workplace what can be done.

Skill tells Workplace how a particular Capability may be implemented in a concrete, replaceable, testable form.

This distinction is essential because MarkOrbit may support the same professional function through different implementations.

For example, document comparison may be performed through:

- a deterministic local parser;
- a shared Core Service;
- a third-party tool;
- an AI-assisted Skill;
- a human professional;
- a hybrid Skill requiring Human Review.

Trademark classification may be supported through:

- a rules-based classification Skill;
- a jurisdiction-specific private Skill;
- a shared AI-assisted Skill;
- a Product-embedded guided Skill;
- a human specialist.

If Capability and Skill are collapsed, the architecture cannot safely:

- replace one implementation with another;
- compare quality and cost;
- constrain data access;
- distinguish local from cloud processing;
- test behavior;
- version implementations;
- apply Product or organization preferences;
- require Human Review;
- suspend an unsafe implementation without removing the underlying Capability.

The central proposition is:

```text
Capability Discovery
=
Professional Need
+ Organization Context
+ Subject
+ Required Outcome
+ Scope
+ Knowledge Dependencies
+ Risk
+ Permission
+ Policy
+ Review Boundary
+ Eligible Providers
```

and:

```text
Skill Selection
=
Eligible Capability
+ Concrete Implementation
+ Compatibility
+ Data Boundary
+ Quality Evidence
+ Cost and Performance
+ Organization Preference
+ Product Context
+ Availability
+ Fallback
+ Governance
```

The constitutional distinctions are:

```text
Capability ≠ Skill

Capability ≠ Product feature

Capability ≠ Service offering

Capability ≠ Permission

Capability ≠ professional qualification

Skill ≠ Tool

Skill ≠ Model

Skill ≠ Prompt

Skill ≠ Agent

Skill ≠ Workflow

Skill ≠ protected action authority

Capability discovery ≠ provider appointment

Capability match ≠ Skill selection

Skill selection ≠ invocation

Invocation ≠ formal business-state mutation

Claimed Capability ≠ verified Capability

Enabled Skill ≠ universally allowed Skill

High-performing Skill ≠ professionally accountable actor
```

Book 02 remains authoritative for Capability semantics, provider identity, scope, verification, Permission, Policy, risk, review, contracts, and formal Core objects.

Book 03 remains authoritative for governed Execution, Workflow coordination, Task lifecycle, Human Review, protected actions, and Owning Service handoff.

This chapter defines Workplace consumption and selection.

It does not redefine Core or Execution.

---

## 1. Capability Answers What Can Be Done

Capability means:

> a governed ability that may be provided by a system, service, AI Agent, human professional, organization, external provider, or governed workflow under defined scope, conditions, Permission, Policy, risk, review, contract, and audit rules.

Capability answers questions such as:

```text
Can the system retrieve validated jurisdiction Knowledge?

Can the system classify goods and services?

Can the organization prepare a filing package?

Can an AI Agent summarize an office action?

Can a human professional review evidence?

Can a provider perform a trademark filing in a jurisdiction?

Can a Product prepare a quotation candidate?

Can a governed workflow coordinate an approval sequence?
```

Capability is an architectural and governance concept.

It is not merely a button, endpoint, tool name, employee title, or marketing statement.

A Capability should remain identifiable even when its implementation changes.

For example:

```text
Capability:
Translate professional Communication

Possible Skills:
- local deterministic glossary-assisted translation
- shared AI translation
- external translation provider
- bilingual human review service
```

The Capability remains stable.

The Skills may change.

---

## 2. Skill Answers How a Capability Is Implemented

Skill means:

> a concrete, replaceable, versioned, testable, and governable implementation through which one or more Capabilities may be performed under a defined execution and data boundary.

A Skill may define:

- implemented Capability;
- implementation identity;
- provider;
- version;
- supported input;
- expected output;
- dependencies;
- required Knowledge;
- allowed data scope;
- execution location;
- risk;
- Permission requirements;
- Policy constraints;
- Human Review;
- quality evidence;
- failure behavior;
- fallback;
- audit requirements.

Examples include:

```text
Capability:
Extract trademark application fields

Skill:
Local PDF Trademark Form Extractor v2.1
```

```text
Capability:
Draft response summary

Skill:
AI Office Action Summary Skill v1.4
```

```text
Capability:
Check filing package completeness

Skill:
MarkReg Filing Package Validator v3
```

A Skill is not automatically an executable Workflow.

It may be invoked within a Workflow, Product, Assistant, Guide, or Agent operation.

---

## 3. Capability and Skill Form Two Different Registries

The architecture distinguishes:

```text
Capability Catalog
→ what governed abilities exist

Skill Registry
→ which concrete implementations are available
```

The Capability Catalog may identify:

- Capability name;
- purpose;
- domain;
- scope;
- expected outcome;
- risk;
- review requirement;
- eligible provider types;
- consumption contract.

The Skill Registry may identify:

- Skill identity;
- implemented Capability references;
- implementation provider;
- version;
- status;
- execution mode;
- input and output compatibility;
- data access;
- dependencies;
- quality evidence;
- availability;
- fallback;
- restrictions.

The same Capability may have multiple Skills.

One Skill may implement several closely related Capabilities, provided the boundaries remain explicit.

The registries may be logical responsibilities rather than separate technical services.

---

## 4. Capability Must Remain Stable Across Implementations

A Capability should express durable professional function.

A Skill may change when:

- a model is replaced;
- a provider changes;
- a parser is improved;
- a local implementation becomes available;
- a jurisdiction rule changes;
- a Product adopts a new interface;
- quality testing reveals weakness;
- cost or latency becomes unacceptable.

If the Capability identity changes whenever implementation changes, Products and Workflows become tightly coupled to tools.

The desired relationship is:

```text
Stable Capability
        ↓
Replaceable Skill
        ↓
Governed Invocation
```

This supports:

- experimentation;
- gradual migration;
- local/private alternatives;
- provider substitution;
- Product independence;
- testing;
- resilience.

---

## 5. Product Feature Is Not Capability

A Product feature is a user-facing function or experience.

A Capability is a reusable governed ability.

Examples:

```text
Capability:
Trademark classification recommendation

Product feature:
MarkReg class recommendation page
```

```text
Capability:
Next Best Action generation

Product feature:
Lite Today recommendation card
```

```text
Capability:
Provider capability matching

Product feature:
MGSN provider comparison interface
```

A Product feature may consume several Capabilities.

A Capability may appear in several Products.

Products should not redefine the Capability each time.

The Product owns its experience.

The Capability Catalog owns the governed functional meaning.

---

## 6. Service Offering Is Not Capability

A Service Offering is a commercial or professional proposition.

It may include:

- jurisdiction;
- service scope;
- price;
- provider;
- turnaround;
- terms;
- deliverables;
- exclusions.

Capability describes what can be done.

Service Offering describes what is offered commercially under defined conditions.

Example:

```text
Capability:
File a trademark application in Singapore

Service Offering:
Singapore trademark filing,
one class,
including local associate handling,
at a defined price and service level
```

Several Service Offerings may rely on the same Capability.

A Capability may exist even when no current commercial offering is enabled.

This distinction prevents the Capability Catalog from becoming a price list or marketplace inventory.

---

## 7. Capability Is Not Permission

Capability answers:

```text
Can this actor or system perform this kind of function?
```

Permission answers:

```text
May this actor perform this operation
on this resource
in this context?
```

A user may possess professional filing Capability but lack Permission for a particular client Matter.

An AI Agent may possess summarization Capability but lack Permission to access raw Evidence.

A Product may consume document-generation Capability but lack Permission to send the generated Communication.

The rule is:

```text
Capability establishes ability.

Permission governs allowed action.
```

Capability matching must never be used as a substitute for Permission evaluation.

---

## 8. Capability Is Not Professional Qualification

A Capability record may represent:

- claimed experience;
- observed performance;
- tested system behavior;
- verified professional qualification;
- organization authorization;
- provider service coverage.

These are different.

A person cannot become legally qualified merely because an administrator enables a Capability label.

A provider cannot become officially authorized in a jurisdiction merely because the system infers experience.

Professional qualification may require:

- license;
- registration;
- employment relationship;
- local status;
- contractual appointment;
- verified evidence;
- effective date;
- jurisdiction scope.

Capability records may reference qualification.

They do not create it.

---

## 9. Human Capability and System Capability Must Remain Distinct

Human professionals and systems can both provide Capabilities.

But they differ in:

- responsibility;
- judgment;
- explainability;
- availability;
- authority;
- legal qualification;
- review role;
- error handling.

A human Capability may include:

- legal review;
- evidence judgment;
- client counseling;
- provider selection;
- approval;
- professional signature.

A system Capability may include:

- extraction;
- classification support;
- comparison;
- validation;
- summarization;
- drafting;
- monitoring;
- recommendation.

A system may support a human Capability.

It does not acquire human accountability.

The system should not describe AI-assisted performance as if the AI were the responsible professional.

---

## 10. Capability Providers Must Be Explicit

Every Capability requires a provider context.

Provider types may include:

- Core;
- Core Service;
- organization;
- Product;
- human professional;
- AI Agent;
- system actor;
- external organization;
- service provider;
- partner;
- governed Workflow;
- local tool environment.

The provider relationship should identify:

- provider identity;
- organization;
- Capability scope;
- verification;
- availability;
- responsibility boundary;
- contract;
- status.

A Capability without a provider is an abstract possibility.

It is not an available operational resource.

---

## 11. Capability Consumers Must Also Be Explicit

Capability consumers may include:

- Workplace;
- Product;
- human user;
- Assistant;
- Guide;
- AI Agent;
- Workflow;
- Core Service;
- external integration.

The same Capability may expose different consumption modes.

For example:

```text
Human user:
interactive use

Product:
contract-based embedded use

AI Agent:
tool or Skill invocation

Workflow:
governed step invocation

External integration:
restricted API use
```

Consumer identity affects:

- input;
- output;
- Permission;
- Policy;
- data access;
- audit;
- review;
- allowed downstream use.

---

## 12. Capability Discovery Begins with a Need, Not a Tool

A common design error is to begin with available tools.

Workplace should begin with the professional need.

A Capability Requirement may include:

```text
purpose

subject

required outcome

organization

client or Matter

jurisdiction

service type

input type

output type

time requirement

risk

knowledge dependency

data boundary

human responsibility

review requirement

cost or performance constraint
```

Only after the requirement is clear should Workplace search for eligible Capabilities.

The correct order is:

```text
Need
→ Capability Requirement
→ Capability Discovery
→ Skill Candidates
```

not:

```text
Available tool
→ find somewhere to use it
```

---

## 13. Capability Requirement Must Describe Outcome and Boundary

A Capability Requirement should state what must be achieved.

It should not prematurely choose the implementation.

Example:

```text
Required:
Extract applicant identity and filing details
from an uploaded official form,
without sending the raw file outside Local Vault,
with field-level source references.
```

This requirement allows several Skill candidates.

It already constrains:

- data location;
- output;
- provenance;
- source;
- purpose.

A weak requirement such as “use AI to parse this PDF” incorrectly selects implementation before defining need.

---

## 14. Capability Discovery Is Contextual

Capability discovery may consider:

- organization;
- user and role;
- client;
- Matter;
- Product;
- jurisdiction;
- service;
- object type;
- purpose;
- Knowledge;
- data boundary;
- risk;
- Permission;
- Policy;
- review;
- time;
- language;
- provider availability.

A Capability may be relevant in general but ineligible in context.

Examples:

- a cloud AI Capability may be disallowed for client-restricted data;
- a provider may cover the jurisdiction but lack current availability;
- a Skill may support English but not the required language;
- a human reviewer may be qualified but conflicted;
- a Product may not be entitled to consume the Capability.

Discovery must therefore return contextual candidates rather than a universal list.

---

## 15. Discovery, Matching, Eligibility, Selection, and Invocation Are Different

The stages must remain separate.

### Discovery

Identifies potentially relevant Capabilities.

### Matching

Compares the requirement with Capability scope and provider evidence.

### Eligibility

Applies Permission, Policy, data, status, compatibility, qualification, and review constraints.

### Selection

Chooses a Skill candidate for the defined purpose.

### Invocation preparation

Builds the governed request with input, references, limits, and review requirements.

### Invocation

The selected Skill performs an allowed operation through its contract.

The path is:

```text
Discover
→ Match
→ Determine Eligibility
→ Select
→ Prepare Invocation
→ Authorize
→ Invoke
→ Validate Result
```

No earlier stage proves that the Skill executed.

---

## 16. Capability Match Is Not Provider Appointment

Capability matching may identify:

- qualified providers;
- relevant organizations;
- eligible professionals;
- possible service partners.

It does not appoint them.

Provider appointment may require:

- human selection;
- commercial agreement;
- conflict review;
- client approval;
- responsibility assignment;
- formal Order or Matter relationship;
- provider acceptance;
- Execution.

This boundary applies especially to MGSN.

MGSN may support discovery and routing.

It must not automatically appoint a provider from a match score.

---

## 17. Skill Selection Is Not Invocation

A Skill may be selected as the preferred implementation.

It has not yet run.

Selection may establish:

- chosen Skill;
- version;
- provider;
- expected input;
- expected output;
- fallback;
- review boundary.

Invocation still requires:

- current availability;
- Permission;
- Policy;
- valid data access;
- contract validation;
- idempotency where relevant;
- current context;
- audit.

This distinction allows a Product to show:

```text
Selected Skill:
Local Evidence Extractor v2

Status:
Ready for governed invocation
```

without implying execution.

---

## 18. Invocation Is Not Formal Business Mutation

A Skill invocation may produce:

- extraction result;
- classification result;
- draft;
- comparison;
- recommendation;
- validation result;
- prepared package;
- error.

The result does not automatically mutate:

- Matter;
- Task;
- Communication;
- Document;
- Evidence;
- Order;
- provider appointment;
- payment;
- official status.

Formal mutation remains with the Owning Service.

The normal path is:

```text
Skill Result
→ result validation
→ candidate or prepared action
→ Human Review where required
→ Execution handoff
→ Owning Service
```

---

## 19. Skill Is Not Tool

A Tool is a technical mechanism that can perform an operation.

Examples:

- browser;
- API;
- parser;
- database client;
- rendering engine;
- email connector;
- command-line program.

A Skill is a governed implementation of a Capability.

A Skill may use one or more Tools.

The Tool does not define:

- professional purpose;
- input boundary;
- allowed consumer;
- output meaning;
- Human Review;
- quality evidence;
- fallback;
- professional risk.

The relationship is:

```text
Capability
→ Skill
→ Tool or Tools
```

A Tool may support many Skills.

A Skill may replace one Tool with another while preserving its governed meaning.

---

## 20. Skill Is Not Model

An AI model is a technical dependency.

A Skill defines governed behavior around that dependency.

For example:

```text
Model:
general language model

Skill:
Trademark Office Action Summary Skill
```

The Skill may add:

- prompt or instruction;
- Knowledge retrieval;
- input filtering;
- output schema;
- source references;
- confidence;
- Human Review;
- tests;
- error handling;
- fallback.

Changing the model does not necessarily create a new Capability.

It may require a new Skill version if behavior or risk changes materially.

---

## 21. Skill Is Not Prompt

A prompt is an instruction representation used by an AI system.

A Skill may include prompts.

It may also include:

- deterministic rules;
- retrieval;
- Tools;
- output validation;
- policy;
- version;
- tests;
- fallback.

A prompt alone is insufficient to define a governed Skill.

The prompt does not grant:

- data access;
- Permission;
- professional authority;
- execution rights.

Hidden prompt changes may materially change Skill behavior.

Skill versioning should account for those changes where they affect output.

---

## 22. Skill Is Not Agent

An AI Agent is a governed runtime role operating under identity, Agent Contract, Permission, context, and policy.

A Skill is an implementation the Agent may use.

The relationship is:

```text
Agent
→ operates for a purpose

Skill
→ provides a concrete function

Tool
→ performs technical operations
```

One Agent may use multiple Skills.

One Skill may be available to several authorized Agents.

An Agent must not gain access to every Skill merely because it is registered.

CH16 develops Assistant, Guide, and AI Agent roles in detail.

---

## 23. Skill Is Not Workflow

A Skill performs a bounded function.

A Workflow coordinates multiple steps, states, actors, reviews, and services.

Example:

```text
Skill:
Validate filing form completeness

Workflow:
Prepare, review, approve, and submit filing package
```

A Workflow may invoke several Skills.

A Skill should not create a hidden workflow through internal side effects.

If the function requires durable multi-step coordination, state, retries, approvals, and handoffs, the architecture may require a Workflow rather than one Skill.

---

## 24. Skill Input and Output Must Be Contractual

A Skill should define expected input and output.

Input may include:

- typed references;
- Content or Document reference;
- selected text;
- Knowledge references;
- organization context;
- client or Matter context;
- language;
- output mode;
- data scope.

Output may include:

- structured result;
- candidate;
- draft;
- validation;
- explanation;
- error;
- trace.

The contract should distinguish:

```text
accepted input

required input

optional context

prohibited input

output type

output limitations

review requirement
```

Free-form input without boundaries increases privacy and reliability risk.

---

## 25. Skill Must Declare Knowledge Dependencies

Professional Skills may depend on governed Knowledge.

Examples:

- jurisdiction filing validator;
- classification recommendation;
- evidence checklist generator;
- deadline calculator;
- office-action summarizer.

A Skill should identify:

- required Knowledge domain;
- minimum validation status;
- applicable jurisdiction;
- effective version;
- behavior when Knowledge is missing;
- conflict handling.

A Skill must not fabricate missing Knowledge.

It may:

- return a gap;
- request retrieval;
- downgrade the output;
- require review;
- refuse safely.

---

## 26. Skill Must Declare Data Boundaries

A Skill may process:

- public information;
- organization-private data;
- client-restricted data;
- Matter-restricted data;
- raw Documents;
- Evidence;
- financial information;
- personal information;
- credentials.

The Skill must declare:

- allowed classification;
- local or cloud processing;
- raw-content access;
- retention;
- logging;
- external provider;
- field omission;
- output boundary.

This allows Workplace to select a local Skill when a cloud Skill is ineligible.

Execution location is part of selection.

It is not merely an infrastructure detail.

---

## 27. Skill Risk Must Be Explicit

Skill risk may depend on:

- output consequence;
- data sensitivity;
- autonomy;
- external effect;
- reversibility;
- uncertainty;
- professional meaning;
- provider trust.

Conceptual levels may include:

```text
Low
Medium
High
Critical
```

Examples:

- formatting a private draft may be low or medium;
- extracting a deadline may be high;
- preparing filing instructions may be high;
- autonomous transmission would be critical and generally prohibited without governed Execution.

Risk influences:

- Permission;
- Policy;
- testing;
- Human Review;
- logging;
- fallback;
- allowed consumers.

---

## 28. Skill Status Must Be Governed

A Skill may have statuses such as:

```text
Candidate

Draft

Experimental

Enabled

Restricted

Deprecated

Suspended

Revoked

Archived
```

Candidate or Draft Skills should not appear as ordinary production choices.

Experimental Skills may be available only for:

- selected organizations;
- low-risk use;
- test data;
- explicit consent;
- mandatory review.

Suspended or Revoked Skills must not be invoked.

Deprecation should provide migration or fallback where practical.

---

## 29. Skill Version Is Part of Selection

A Skill version may change because of:

- model;
- prompt;
- code;
- Tool;
- Knowledge dependency;
- output schema;
- policy;
- provider;
- test baseline;
- error behavior.

The selected version should remain identifiable.

Review and historical trace may depend on it.

The architecture must distinguish:

```text
latest Skill version

enabled Skill version

organization-approved version

version used historically
```

Automatic upgrades may be unsafe for high-risk Skills.

---

## 30. Compatibility Must Be Evaluated

A Skill may be incompatible with:

- input format;
- Product version;
- language;
- jurisdiction;
- data boundary;
- output contract;
- workflow version;
- Knowledge version;
- local environment;
- Agent profile.

Compatibility should be evaluated before invocation.

A high-quality Skill that cannot satisfy the current input and context is not eligible.

Compatibility is distinct from general Capability relevance.

---

## 31. Quality Evidence Must Support Selection

Skill selection may consider evidence such as:

- test results;
- fixture performance;
- review acceptance;
- error rate;
- source-trace quality;
- latency;
- cost;
- failure recovery;
- historical outcomes;
- organization experience;
- provider verification.

Quality evidence must remain scoped.

A Skill may perform well:

- for one language;
- one jurisdiction;
- one document type;
- one organization;
- low-risk contexts.

It should not receive one universal quality label.

---

## 32. Claimed, Inferred, Tested, Reviewed, and Verified Must Remain Distinct

Capability and Skill evidence may be:

- claimed by provider;
- imported;
- inferred from activity;
- tested;
- reviewed;
- verified;
- trusted through repeated outcomes.

These states are not equal.

A provider claim may support discovery.

A test may support technical eligibility.

Professional review may support scoped use.

Verification may support stronger consumption.

The system should expose evidence state rather than one opaque score.

---

## 33. Skill Selection May Consider Cost and Performance

Selection may consider:

- latency;
- cost;
- local compute;
- external fees;
- availability;
- throughput;
- quality;
- data movement;
- review burden;
- failure cost.

The cheapest or fastest Skill is not always appropriate.

The best selection is contextual.

For example:

```text
Low-risk internal summary
→ fast shared AI Skill

Client-restricted evidence extraction
→ local Skill

Critical legal conclusion
→ human professional Capability with AI support
```

Commercial optimization must remain subordinate to professional and data boundaries.

---

## 34. Organization Preferences May Influence Selection

A Workplace may prefer:

- local processing;
- approved providers;
- specific language models;
- lower cost;
- higher review;
- organization templates;
- private Skills;
- certain fallback routes.

Preferences may guide selection.

They cannot override:

- Permission;
- Policy;
- qualification;
- risk;
- contract;
- data boundary;
- professional responsibility.

The rule is:

```text
Preference ranks eligible options.

It does not make an ineligible Skill eligible.
```

---

## 35. Product Context May Influence but Not Own Selection

Products may request a Capability and express constraints.

For example, MarkReg may require:

- trademark-specific inputs;
- jurisdiction Knowledge;
- filing-package output.

Lite may require:

- concise explanation;
- Today-compatible candidate;
- safe prepared action.

The Product may influence selection through its contract.

It should not hard-code ownership of the Skill.

Shared selection supports replacement and cross-Product reuse.

Products may still choose a Product-specific Skill when justified.

---

## 36. Local and Private Skills Must Be Supported

An organization may maintain private Skills such as:

- private pricing calculator;
- local case retrieval;
- organization drafting Skill;
- client-specific validation;
- local database analysis;
- private provider comparison.

These Skills may remain in Local Vault or an organization-controlled environment.

They may be visible through the logical Skill Registry using:

- metadata;
- capability references;
- version;
- availability;
- local invocation route;
- privacy restrictions.

Shared architecture must not require uploading private Skill internals.

---

## 37. Shared Skill Does Not Mean Universal Enablement

A Skill may be available in the shared registry.

Each Workplace may still decide whether to enable it, subject to governance.

Enablement may consider:

- organization edition;
- subscription or entitlement;
- policy;
- data boundary;
- legal terms;
- test status;
- risk appetite;
- user roles;
- Product.

A shared Skill can be:

- visible but disabled;
- enabled only for test;
- enabled for limited data;
- enabled with mandatory review;
- fully enabled for authorized use.

---

## 38. Fallback Must Be Deliberate

Skills can fail because of:

- outage;
- incompatible input;
- missing Knowledge;
- model error;
- provider suspension;
- local resource failure;
- rate limit;
- policy restriction.

Fallback may include:

- another Skill;
- local implementation;
- human handling;
- safe partial result;
- deferred work;
- refusal.

Fallback must not weaken governance.

A cloud Skill blocked by data policy cannot fall back to another cloud provider without reevaluation.

A Skill requiring review cannot fall back to an unreviewed autonomous route.

---

## 39. Selection Should Be Explainable

A user or reviewer should be able to understand:

- which Capability was required;
- which Skill was selected;
- which version;
- why it was eligible;
- what alternatives existed;
- which data route applies;
- what Knowledge it depends on;
- which risks and review requirements apply;
- what fallback exists.

Explainability need not reveal:

- proprietary ranking details;
- secret prompts;
- credentials;
- restricted Skill internals.

A safe explanation may say:

```text
Local Extraction Skill v2 was selected because:
- the source is client-restricted;
- cloud processing is prohibited;
- the Skill supports this document type;
- its current version passed the required fixture set;
- human verification of extracted deadlines is mandatory.
```

---

## 40. The Minimum Capability and Skill Selection Model

```text
Professional Need
  │
  ├── organization
  ├── actor
  ├── Product
  ├── client or Matter
  ├── purpose
  ├── required outcome
  ├── scope
  ├── risk
  ├── data boundary
  └── review requirement
        │
        ▼
Capability Requirement
        │
        ▼
Capability Discovery
        │
        ├── Core Capability
        ├── system Capability
        ├── human Capability
        ├── organization Capability
        └── external provider Capability
        │
        ▼
Matching and Eligibility
        │
        ├── scope
        ├── provider status
        ├── Permission
        ├── Policy
        ├── qualification
        ├── Knowledge
        └── availability
        │
        ▼
Skill Candidates
        │
        ├── implementation
        ├── version
        ├── input/output
        ├── data route
        ├── quality evidence
        ├── cost/performance
        ├── risk/review
        └── fallback
        │
        ▼
Skill Selection
        │
        ▼
Governed Invocation Preparation
        │
        ▼
Permission and Policy Revalidation
        │
        ▼
Invocation or Safe Rejection
        │
        ▼
Result Validation
        │
        ▼
Candidate, Draft, Prepared Action,
Human Review, or Execution Handoff
```

This is an architectural model.

It is not a registry schema, ranking algorithm, API, plugin protocol, model router, or runtime engine.

---

## 41. Required Distinctions

```text
Capability ≠ Skill
```

Capability is governed ability; Skill is concrete implementation.

```text
Capability ≠ Product feature
```

Products consume Capabilities through experiences.

```text
Capability ≠ Service Offering
```

Commercial offerings add provider, price, terms, and deliverables.

```text
Capability ≠ Permission
```

Ability does not grant action authority.

```text
Capability ≠ professional qualification
```

Configuration cannot create legal or professional status.

```text
Skill ≠ Tool
```

A Skill governs how Tools implement a Capability.

```text
Skill ≠ Model
```

A model is a dependency, not the governed function.

```text
Skill ≠ Prompt
```

Prompt text does not define the full Skill contract.

```text
Skill ≠ Agent
```

Agent is runtime identity and role; Skill is a function it may use.

```text
Skill ≠ Workflow
```

A bounded function is not a durable coordinated lifecycle.

```text
Discovery ≠ matching
```

Potential relevance does not prove fit.

```text
Matching ≠ eligibility
```

Policy and authority may disqualify a match.

```text
Eligibility ≠ selection
```

Several options may remain.

```text
Selection ≠ invocation
```

The Skill has not yet run.

```text
Invocation ≠ formal mutation
```

Owning Services control formal business facts.

```text
Claimed Capability ≠ verified Capability
```

Evidence state must remain visible.

```text
Enabled Skill ≠ universally allowed Skill
```

Current context still governs use.

---

## 42. Failure Modes This Chapter Prevents

### Tool-first architecture

Available tools define product needs instead of professional requirements.

### Capability-skill collapse

One implementation becomes permanently coupled to the Capability identity.

### Product capability duplication

Each Product creates incompatible meanings for the same ability.

### Permission by ability

A user or Agent is allowed to act merely because it has the Capability.

### Qualification fabrication

Administrative configuration creates apparent legal qualification.

### Model-as-skill

A generic model is treated as a governed professional function.

### Prompt-as-governance

Prompt instructions substitute for Permission, Policy, testing, and review.

### Agent-skill collapse

An Agent receives every registered Skill and unrestricted data.

### Hidden workflow

One Skill performs durable multi-step side effects without Workflow governance.

### Match-as-appointment

A provider ranking automatically appoints an external provider.

### Selection-as-execution

A selected Skill is shown as though it already ran.

### Skill-result mutation

A result silently changes Matter, Task, Communication, Evidence, or Order state.

### Universal quality score

Performance in one scope becomes a general quality claim.

### Preference override

Organization preference bypasses data, risk, or qualification constraints.

### Unsafe fallback

Failure routes to a less-governed Skill.

### Shared-skill overexposure

Registry visibility becomes universal enablement.

### Private-skill extraction

Organization-specific Skill internals are centralized without need.

These systems may appear flexible.

They do not conform to the Workplace architecture.

---

## 43. Minimum Conformance Rule

A conforming Workplace must preserve the following lock:

```text
Capability represents governed ability.

Skill represents a concrete,
replaceable, versioned, and testable implementation.

Capability Catalog and Skill Registry
remain logically distinct.

Professional need defines the Capability Requirement.

Tools do not define the need.

Discovery, matching, eligibility,
selection, preparation, and invocation remain distinct.

Capability does not grant Permission.

Capability configuration does not create qualification.

Product features consume Capabilities
without redefining them.

Service Offerings remain commercially distinct.

Skills declare provider, version,
input, output, Knowledge dependency,
data boundary, risk, review, and fallback.

AI models and prompts remain Skill dependencies,
not complete Skills.

Agents use Skills under Agent Contract.

Workflows coordinate multi-step execution.

Claimed, inferred, tested, reviewed,
and verified evidence remain distinguishable.

Organization preferences rank only eligible Skills.

Private and local Skills may remain distributed.

Shared Skills require Workplace enablement.

Fallback never bypasses governance.

Skill results remain candidates, drafts,
validation results, or prepared actions
until the appropriate authority acts.

Owning Services retain formal mutation authority.

Humans retain professional accountability.
```

A technically advanced plugin or agent system that violates this lock does not conform.

---

## 44. Chapter Boundary

This chapter defines:

- Capability consumption in Workplace;
- Capability and Skill distinction;
- Capability Catalog and Skill Registry;
- Capability Requirements;
- discovery;
- matching;
- eligibility;
- selection;
- invocation preparation;
- provider and consumer context;
- Product feature and Service Offering boundaries;
- Tool, model, prompt, Agent, and Workflow boundaries;
- Skill contracts;
- Knowledge dependencies;
- data boundaries;
- risk;
- status;
- version;
- compatibility;
- quality evidence;
- organization preferences;
- Product context;
- local and private Skills;
- shared Skill enablement;
- fallback;
- explainability.

It does not define:

- Assistant, Guide, or AI Agent role architecture;
- Agent runtime orchestration;
- recommendation scoring;
- Next Best Action;
- prepared-action contracts;
- Human Review lifecycle;
- provider appointment;
- MGSN routing algorithm;
- Skill Registry database schema;
- plugin protocol;
- MCP or tool protocol;
- model router;
- prompt implementation;
- exact quality metrics;
- deployment topology;
- production code.

Those subjects belong to CH16–CH19, Part VI, future specifications, Product publications, ADRs, and implementation repositories.

This chapter does not modify Book 02 Capability semantics.

It does not modify Book 03 Execution authority.

It does not authorize external Communication, filing, payment, provider appointment, official recordal, autonomous professional action, or direct business-state mutation.

---

## 45. Chapter Conclusion

Knowledge tells Workplace what is understood.

Capability tells Workplace what may be done.

Skill tells Workplace which concrete implementation may perform the function.

The architecture therefore follows:

```text
Professional Need
→ Capability Requirement
→ Capability Discovery
→ Contextual Matching
→ Eligibility
→ Skill Candidates
→ Skill Selection
→ Governed Invocation
→ Result Validation
→ Human Review or Execution Handoff
```

This architecture allows MarkOrbit to evolve.

A local parser may replace a cloud parser.

A new AI model may replace an older model.

A private organization Skill may coexist with a shared Skill.

A human professional may remain the required provider for high-risk judgment.

A Product can improve its experience without owning the Capability.

A Skill can be suspended without deleting the professional function from the system.

The constitutional outcome is:

```text
Capability defines ability.

Skill implements ability.

Tool performs technical work.

Agent uses Skills under identity and contract.

Product presents the experience.

Workflow coordinates governed steps.

Human Review protects professional judgment.

Execution governs protected action.

Owning Services change and record formal business facts.
```

CH16 now addresses the runtime and user-facing roles that consume these Capabilities and Skills:

> How do Assistant, Guide, and AI Agent differ, and how do they operate inside Workplace without hiding identity, expanding context, bypassing Permission, or replacing human professional responsibility?
