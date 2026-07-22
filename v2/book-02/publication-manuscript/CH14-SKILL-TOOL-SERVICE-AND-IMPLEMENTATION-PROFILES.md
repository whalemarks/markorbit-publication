# CH14 — Skill, Tool, Service and Implementation Profiles

## Capability remains stable while implementations vary

A Capability Definition describes the governed outcome. The platform still needs to know how that outcome may be produced.

That production side contains several different concepts:

```text
Skill
Tool
Service
Implementation Profile
```

They should interoperate, but they should not be collapsed.

## Skill

A Skill is a reusable procedure or agent package that implements part or all of a Capability.

It may include:

- instructions;
- deterministic rules;
- prompt and model bindings;
- Tool dependencies;
- input and output adapters;
- validation checks;
- review expectations;
- failure and escalation behavior.

A Skill can be human-readable, machine-executable or hybrid.

```text
Skill
≠ Capability
```

The same Capability may be implemented by several Skills, and one Skill may support several Capabilities.

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
- accepted inputs;
- outputs;
- side effects;
- data disclosure;
- authentication context;
- retry and idempotency behavior;
- evidence emitted;
- known failure modes.

```text
Tool technically available
≠ Tool authorized for this request
```

## Service

Service must be qualified because it can refer to different architectural roles.

```text
runtime service
Product service
Owning Service
external professional service
```

A runtime service executes code. A Product service is a commercial offering. An Owning Service controls formal state for a business object. An external professional service is delivered by a Provider under a specific authority contract.

The word `service` alone is insufficient for consequential architecture decisions.

## Implementation Profile

An Implementation Profile binds a Capability version to a specific governed realization.

It may identify:

- implementation class;
- Skill versions;
- Tool versions;
- service dependencies;
- supported M-mode;
- maximum R-tier;
- data scope;
- jurisdiction and language;
- required human roles;
- review policy;
- performance evidence;
- production authorization state;
- rollback and replacement route.

```text
Capability Definition
+ Implementation Profile
= governed implementation candidate
```

The binding still does not create Assignment or permission to execute a specific request.

## Human implementation

A human implementation should not be represented merely by a person's name.

It should preserve:

- relevant Capability evidence;
- jurisdiction and language;
- professional qualification where needed;
- permitted work class;
- supervision requirement;
- tool access;
- data restrictions;
- current production authorization.

```text
experienced person
≠ eligible implementation for every task
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
- evaluation evidence;
- stop and escalation conditions.

```text
model capability
≠ invocation authority
```

A stronger model does not automatically inherit the prior model's production approval.

## Deterministic implementation

Deterministic systems can provide strong repeatability, but only if the rule and input remain valid.

```text
rule executed correctly
≠ source rule correct
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
→ provider execution
```

A hybrid profile must preserve each component's contribution, authority and evidence rather than describing the whole route as “AI” or “human.”

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

Entitlement to a Tool does not authorize every operation.

## Replacement and compatibility

An implementation may be replaced only after checking:

- output compatibility;
- evidence compatibility;
- changed risk;
- changed review burden;
- data disclosure;
- side effects;
- active work impact.

```text
same output schema
≠ same governance behavior
```

## Core boundary

Core may standardize the references and distinctions needed to describe implementations. It should not absorb every prompt, connector configuration, procedural checklist or vendor-specific API.

Those remain versioned implementation records owned by the relevant service or Product context.

## Constitutional rule

```text
Skills describe reusable procedures.
Tools perform bounded operations.
Services host, own or deliver defined responsibilities.
Implementation Profiles bind them to a Capability.

None alone proves eligibility, assignment, approval or authority.
```
