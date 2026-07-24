# CH14 — Skill, Tool, Service and Implementation Profiles

## Capability remains stable while implementations vary

A Capability Definition describes the governed outcome. The platform still needs to know how that outcome may be produced in a particular scenario.

That production side contains several different concepts:

```text
Skill Definition
Tool
Service
Implementation Profile
Action / Invocation
```

They interoperate. They must not be collapsed.

## Skill Definition

A Skill Definition is a reusable, scenario-specific implementation of part or all of a Capability.

It may include:

- purpose and supported Capability references;
- accepted inputs and preconditions;
- instructions or procedure;
- deterministic rules;
- prompt and model bindings;
- Tool dependencies;
- input and output adapters;
- validation checks;
- review expectations;
- failure, escalation and Unknown behavior;
- Evidence emitted;
- version and compatibility information.

A Skill may be human-readable, machine-executable or hybrid.

```text
Skill Definition
≠ Capability Definition
```

The same Capability may be implemented by several Skills. One Skill may support several Capabilities when its scope and output remain explicit.

A Skill never receives authority merely because it exists or performs well in another context.

## Source Skill and Verified platform Skill

Skills may have different origins and maturity.

A **Source Skill** preserves a procedure, framework or decision method from an attributable source. Its assumptions, provenance and limits should remain visible.

A **Composite Skill** combines compatible steps from several Source Skills or internal methods for a bounded scenario.

An **Experimental Skill** is being evaluated under explicit restrictions.

A **Verified platform Skill** has passed the relevant evaluation, compatibility, security and governance gates for its declared use.

```text
Source Skill
≠ Verified MO Capability
```

A source method may be valuable without being sufficiently complete, current or safe to support a released Capability on its own.

## Skill granularity

A Skill should normally implement a coherent decision or production step that can be reused and evaluated.

Examples include:

- extract applicant identity from a signed instruction form;
- reconcile registered goods with candidate use evidence;
- calculate a sourced filing window;
- draft a customer update from validated Matter events;
- compare two versions of an Instruction Package;
- screen a Provider Return for missing Evidence.

“Do trademark work” is too broad. “Click submit” is an Action rather than a Skill.

## Tool

A Tool performs a bounded operation.

Examples include:

- source retrieval;
- OCR or document extraction;
- similarity calculation;
- translation;
- image rendering;
- database query;
- email transmission;
- official-portal submission;
- payment initiation.

Tool contracts should identify:

- version;
- accepted inputs and outputs;
- side effects;
- Data disclosure;
- authentication context;
- retry and idempotency behavior;
- Evidence emitted;
- known failure modes.

```text
Tool technically available
≠ Tool authorized for this request
```

A Tool does not define professional meaning. The Skill and Capability explain why it is used, what its result means and which review follows.

## Service

The word Service can refer to several architectural roles:

```text
runtime service
Product service
Owning Service
external professional service
```

A runtime service executes software. A Product service is a user-facing or commercial offering. An Owning Service controls formal state for a business object. An external professional service is delivered by a Provider under a defined Engagement and authority contract.

The unqualified word `service` is insufficient for consequential architecture decisions.

## Implementation Profile

An Implementation Profile binds a Capability version to a specific governed realization.

It may identify:

- implementation class;
- Skill versions;
- Tool versions;
- service dependencies;
- supported Human–AI mode;
- maximum risk and control tier;
- Data and memory scope;
- jurisdiction and language;
- required human roles;
- review policy;
- evaluation Evidence;
- production-authorization state;
- rollback and replacement route.

```text
Capability Definition
+ Implementation Profile
= governed implementation candidate
```

The binding does not create Eligibility, Assignment or permission to execute a specific request.

## Human implementation

A human implementation should not be represented merely by a Person’s name or job title.

It should preserve:

- relevant Capability Profile Evidence;
- jurisdiction and language;
- Professional Qualification where needed;
- permitted work class;
- supervision requirement;
- Tool access;
- Data restrictions;
- current Production Authorization;
- availability and conflict state at runtime.

```text
experienced person
≠ eligible implementation for every request
```

## AI implementation

An AI Implementation Profile should preserve:

- model and version;
- policy version;
- instruction or prompt reference;
- retrieval and source policy;
- Tool access;
- memory policy;
- allowed outputs;
- prohibited actions;
- review requirement;
- evaluation Evidence;
- stop and escalation conditions.

```text
model capability
≠ invocation authority
```

A stronger model does not automatically inherit a prior model’s Production Authorization.

## Deterministic implementation

Deterministic systems provide repeatability only when the rule and input remain valid.

```text
rule executed correctly
≠ source rule current
≠ professional conclusion correct
```

Their profiles should include rule source, effective period, test fixtures, invalid-input behavior and version history.

## Hybrid implementation

Many professional outcomes require a chain such as:

```text
deterministic extraction
→ AI classification
→ contributor preparation
→ professional review
→ customer approval
→ Provider execution
```

A hybrid profile must preserve each component’s Contribution, authority and Evidence rather than describing the whole route as “AI” or “human.”

## Action and Invocation

An Action or Invocation is one bounded use of a Skill, Tool or human procedure under an exact runtime context.

It should normally resolve:

- Capability Request and version;
- selected Skill and Implementation Profile;
- input references and versions;
- represented Workplace and purpose;
- Data and memory scope;
- authority and review envelope;
- time, cost and Tool budget;
- Evidence and Session Receipt requirements;
- idempotency or retry controls where relevant.

```text
Skill available
≠ Skill invoked

Skill invoked
≠ Outcome accepted
```

An Invocation is an event in the execution lifecycle. It is not a new Skill or Capability version.

## Composition Profile

A complex request may use several Capabilities or Skills. The composition should be explicit rather than hidden in a large prompt.

A Composition Profile may identify:

```text
one Primary Capability
zero to three Supporting Capabilities
zero or one Critic Capability
Capability Budget
conflicts and resolution rules
```

The Primary Capability owns the main decision structure. Supporting Capabilities answer bounded nodes. A Critic Capability examines a specified risk, assumption or failure mode.

The Capability Budget limits:

- context size;
- number of active methods;
- Tool calls;
- time and cost;
- review burden;
- escalation depth.

```text
more Skills loaded
≠ better composition
```

Composition should preserve disagreement when assumptions conflict. It should not average incompatible methods into a false consensus.

## Tool access and protected action

Tools that create external consequences require stricter treatment.

An email sender, official connector or payment gateway should not be treated like an internal formatter.

The profile must distinguish:

```text
read
prepare
preview
submit
send
pay
mutate
```

Entitlement to a Tool does not authorize every operation. Capability Composition does not create protected-action authority.

## Replacement and compatibility

An implementation may be replaced only after checking:

- output compatibility;
- Evidence compatibility;
- changed risk;
- changed review burden;
- Data disclosure;
- side effects;
- active work impact;
- migration or revalidation needs.

```text
same output schema
≠ same governance behavior
```

A model, Skill or Tool update may require renewed simulation, shadow evaluation or supervised use without changing the Capability Definition itself.

## Core boundary

Core may standardize the references and distinctions needed to describe Capabilities, Skills, implementations and Invocations. It should not absorb every prompt, connector configuration, procedural checklist or vendor-specific API.

Source Skills, Product-local Skills and implementation records may remain versioned in their owning contexts. Their existence does not activate a new Core contract.

Formal admission of any new shared semantic still requires the Book 02 governance route.

## Constitutional rule

```text
Capabilities define governed outcomes.
Skills describe reusable implementations.
Tools perform bounded operations.
Services host, own or deliver defined responsibilities.
Implementation Profiles bind them for evaluation.
Actions and Invocations use them in exact runtime context.

None alone proves Eligibility, Assignment, Approval or Authority.
```