# CH13 — Capability Definition as a Durable Outcome Contract

## Capability is the unit that should survive implementation change

MarkOrbit needs a stable way to describe what professional outcome can be produced even when the underlying human, AI, software, provider or workflow changes.

That stable unit is the Capability Definition.

```text
Capability Definition
= durable governed outcome contract
```

It is not a marketing label, feature name, prompt, job title, checklist or workflow template.

A Capability Definition answers five questions:

1. What outcome is promised?
2. Under which inputs, assumptions and scope?
3. Which evidence and review make the outcome acceptable?
4. Which implementation classes may produce it?
5. Which authority and compatibility limits apply?

## Minimum contract

A mature Capability Definition should include:

- stable identifier;
- semantic version;
- domain and jurisdiction scope;
- purpose and expected outcome;
- accepted input classes;
- output contract;
- required Evidence;
- Knowledge and data dependencies;
- supported implementation modes;
- review policy;
- risk and authority ceiling;
- restrictions and exclusions;
- failure and Unknown behavior;
- compatibility and deprecation policy.

The contract should be precise enough that different implementations can be evaluated against the same promise.

## Outcome first

Capability should be defined by the governed outcome, not by the activity performed.

Weak definition:

```text
Search trademarks
```

Stronger definition:

```text
Produce a source-backed, jurisdiction-scoped search decision package
that identifies relevant candidates, limitations, Unknowns,
review requirements and recommended next actions.
```

The stronger definition makes clear that retrieval alone is insufficient.

## Inputs are part of the contract

A Capability is not valid for every possible input.

Input conditions may specify:

- required identity fields;
- jurisdiction;
- language;
- document quality;
- source freshness;
- mark representation;
- goods and services scope;
- customer confirmation;
- permitted data class.

```text
input accepted by interface
≠ input sufficient for Capability
```

The Capability Definition should say when clarification, professional review or refusal is required.

## Output is more than a file

An output contract should define:

- object type;
- versioning;
- mandatory fields;
- Evidence links;
- epistemic labels;
- limitations;
- review disposition;
- whether the output is draft, Candidate, accepted Outcome or decision-ready package.

```text
file generated
≠ Capability outcome satisfied
```

A polished PDF without source lineage or review status may fail the Capability contract.

## Capability and formal state

Capability outputs may support formal-state transitions, but they do not perform those transitions by definition.

```text
Capability Outcome
≠ Approval
≠ Apply
≠ Formal-state Mutation
```

A filing-readiness Capability may produce an accepted filing package. The actual filing remains a protected action under Book 03 and formal state remains with the applicable Owning Service.

## Capability versioning

A Capability version may change when there is a material change to:

- outcome meaning;
- required inputs;
- Evidence requirements;
- review tier;
- supported jurisdiction;
- authority ceiling;
- compatibility obligations.

Implementation-only changes do not always require a new Capability version.

```text
model upgraded
≠ Capability changed automatically
```

But if the model upgrade changes the output contract, risk or review requirement, a Capability version change may be necessary.

## Capability Definition and Product promise

A Product may package the same Capability differently.

MarkReg may offer a reviewed search package as part of an application service. Lite may expose a limited informational result. A partner Workplace may purchase the same underlying Capability under a white-label commercial arrangement.

The Product promise can narrow the Capability. It cannot silently broaden its authority.

```text
Product wording
≠ Capability authority expansion
```

## Evidence of capability performance

Capability quality should be assessed against the contract, including:

- outcome completeness;
- source quality;
- defect severity;
- review findings;
- escalation quality;
- correction behavior;
- customer communication;
- formal outcome where relevant.

A fast or fluent result is not sufficient evidence.

## Capability as a shared semantic candidate

Capability Definition is already central to the current Core architecture. The publication manuscript may explain and organize it, but must not introduce incompatible new mandatory fields without a formal change process.

## Constitutional rule

```text
Capability is the stable contract for a governed outcome.
Products package it.
Workflows coordinate it.
Implementations realize it.
Review and authority constrain it.

No implementation detail may silently redefine the Capability.
```
