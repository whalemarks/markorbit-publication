# CH13 — Capability Definition as a Durable Outcome Contract

## Capability is the unit that should survive implementation change

MarkOrbit needs a stable way to describe what professional outcome can be produced even when the underlying human, AI, software, Provider or Workflow changes.

That stable unit is the Capability Definition.

```text
Capability Definition
= durable governed outcome contract
```

It is not a marketing label, feature name, prompt, job title, checklist or Workflow template.

A mature definition answers:

1. What outcome is promised?
2. Under which inputs, assumptions and scope?
3. Which Evidence and review make the outcome acceptable?
4. Which implementation classes may produce it?
5. Which risk, authority and compatibility limits apply?
6. How may experience propose a future version without silently changing the current one?

The sixth question is essential. Capability must remain stable at runtime while remaining capable of controlled evolution.

## The semantic hierarchy

The publication architecture uses the following hierarchy:

```text
Capability Domain
→ Capability Definition
→ Skill Definition
→ Action / Invocation
```

A **Capability Domain** organizes a durable field of professional or business competence.

A **Capability Definition** establishes the governed outcome contract.

A **Skill Definition** describes a reusable scenario-specific implementation of part or all of a Capability.

An **Action or Invocation** is one bounded execution under a particular request, version, context and authority envelope.

These distinctions prevent a prompt, Tool operation or individual task from becoming the shared meaning of the Capability.

## Minimum Capability contract

A mature Capability Definition should normally include:

- stable identifier;
- semantic version;
- Domain and family;
- purpose and expected outcome;
- jurisdiction and procedure scope;
- accepted input classes;
- assumptions and required confirmations;
- output contract;
- required Evidence;
- Data and Knowledge dependencies;
- supported implementation classes and Human–AI modes;
- review policy;
- risk and authority ceiling;
- restrictions and exclusions;
- failure, escalation and Unknown behavior;
- compatibility and deprecation policy;
- provenance and lineage references;
- evolution and change-governance references.

The contract should be precise enough that different implementations can be evaluated against the same promise.

Publication discussion of these fields does not by itself activate new mandatory Core fields. Formal admission remains governed by Book 02 change control.

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

```text
activity completed
≠ Capability outcome accepted
```

## Inputs are part of the contract

A Capability is not valid for every possible input.

Input conditions may specify:

- required identity fields;
- jurisdiction and language;
- document quality;
- source freshness;
- mark representation;
- goods and services scope;
- customer confirmation;
- permitted Data class;
- authority and disclosure prerequisites.

```text
input accepted by interface
≠ input sufficient for Capability
```

The Definition should state when clarification, professional review, revalidation or refusal is required.

## Output is more than a file

An output contract should define:

- object or artifact type;
- exact version;
- mandatory fields;
- Evidence links;
- epistemic labels;
- limitations and Unknowns;
- review disposition;
- whether the output is draft, Candidate, accepted Outcome or decision-ready package.

```text
file generated
≠ Capability outcome satisfied
```

A polished PDF without source lineage or review status may fail the Capability contract.

## Capability and formal state

Capability outputs may support formal-state transitions, but they do not perform those transitions merely because the outcome is complete.

```text
Capability Outcome
≠ Approval
≠ Apply
≠ External Protected Action
≠ Formal-state Mutation
```

A filing-readiness Capability may produce an accepted filing package. The actual filing remains a protected action under Book 03. Formal state remains with the applicable Owning Service.

## Capability is stable and versioned

A Capability version may change when there is a material change to:

- outcome meaning;
- required inputs;
- Evidence requirements;
- review tier;
- supported jurisdiction;
- authority ceiling;
- compatibility obligations;
- failure or Unknown behavior.

Implementation-only changes do not always require a new Capability version.

```text
model upgraded
≠ Capability changed automatically
```

But a model change that materially affects output meaning, risk or review burden may require a new Implementation Profile, re-evaluation or a Capability version proposal.

## Capability classes preserve origin and maturity

The word Capability is used in several governed states. They must not be treated as interchangeable.

### Source Capability

A Source Capability reconstructs the reasoning of an attributable source such as a book, course, interview or practitioner body. It preserves assumptions, methods, cases, boundaries and provenance.

### Composite Capability

A Composite Capability combines selected Source Capabilities, Data, Knowledge and practice Evidence for a defined problem. It records composition rationale and unresolved conflicts.

### Experimental Capability

An Experimental Capability is a bounded candidate under evaluation. It has explicit users, contexts, risk controls, review burden and evaluation criteria.

### Verified MO Capability

A Verified MO Capability is a released platform version supported by sufficient evidence, governance, compatibility review and controlled adoption.

```text
Source Capability
≠ Composite Capability
≠ Experimental Capability
≠ Verified MO Capability
```

These names are publication-level semantic candidates unless and until the formal Book 02 admission process resolves their exact Core representation.

## Capability Definition and Skill Definition

A Capability Definition describes the stable outcome. A Skill Definition describes one reusable implementation route.

```text
Capability Definition
= what governed result is required

Skill Definition
= how part or all of that result may be produced
```

One Capability may have several Skills. A Skill may support more than one Capability when its scope and output remain explicit.

The Skill must not silently broaden the Capability’s outcome or authority.

## Capability Composition is a separate record

Complex requests may require several Capabilities. The resulting composition should not be hidden inside an opaque prompt.

A Capability Composition may identify:

- one Primary Capability;
- zero to three Supporting Capabilities;
- zero or one Critic Capability;
- exact versions;
- bounded decision nodes;
- Capability Budget;
- conflict statements;
- resolution rationale;
- expected composed Outcome.

```text
Capability Composition
≠ new Capability Definition
≠ Approval
≠ authority to execute
```

A successful one-time composition may later support a Composite or Experimental Capability Candidate. It does not create one automatically.

## Runtime, production and evolution are different lifecycles

The semantic model must distinguish:

```text
Capability production
Source → Distillation → Source Capability

Capability runtime
Request → Eligibility → Composition → Execution → Outcome

Capability evolution
Outcome and Evidence
→ Reflection Candidate
→ Case Candidate
→ Principle Candidate
→ Capability Change Proposal
→ Version Review
→ Release
```

A runtime invocation should resolve an already known Capability version. Learning records may reference that invocation, but they must not mutate the definition in place.

## Capability Change Proposal

A Capability Change Proposal should identify:

- affected Capability and current version;
- proposed semantic change;
- supporting and contradicting Evidence;
- relevant Reflections, Cases and Principles;
- rights and privacy disposition;
- affected Skills, assessments and Products;
- compatibility and migration impact;
- reviewer and approval route;
- pilot, rollback and evaluation plan.

```text
Change Proposal opened
≠ change approved
≠ new version released
≠ production migration authorized
```

## Capability Ledger

A Capability Ledger preserves governed lineage across:

- source versions;
- distillation records;
- composition decisions;
- Experimental releases;
- evaluation results;
- accepted and rejected Change Proposals;
- reviewer Decisions;
- supersession and rollback;
- affected Products and assessments.

The Ledger does not need to be one universal public object. Its exact representation may remain distributed across typed records and references.

Its constitutional purpose is clear:

```text
latest Capability version
≠ permission to erase how it was produced
```

## Capability Definition and Product promise

A Product may package the same Capability differently.

MarkReg may offer a reviewed search package as part of an application service. Lite may expose a limited informational result. A partner Workplace may purchase the same underlying Capability under a white-label arrangement.

The Product promise can narrow the Capability. It cannot silently broaden its authority.

```text
Product wording
≠ Capability authority expansion
```

## Evidence of Capability performance

Capability quality may be assessed against:

- Outcome completeness;
- source quality;
- defect severity;
- review findings;
- escalation quality;
- correction and recovery;
- customer communication;
- formal Outcome where relevant;
- context, complexity and implementation version.

A fast or fluent result is not sufficient evidence.

Evidence about one performer, Provider, model or Workflow must not be collapsed into universal proof of the Capability Definition.

## Core and publication boundary

Capability Definition is central to the current architecture. This chapter may clarify its role and identify candidate supporting semantics. It does not activate incompatible fields, new root objects, public exports or production behavior.

Formal Core change still requires:

```text
semantic gap
→ cross-Product need
→ authority analysis
→ compatibility review
→ Change Proposal
→ conformance evidence
→ approval and migration decision
```

## Constitutional rule

```text
Capability is the stable contract for a governed outcome.
Skills and Implementation Profiles realize it.
Products package it.
Execution invokes it.
Evidence may propose its evolution.
Only governed version release changes it.

No implementation, Outcome or model inference may silently redefine the Capability.
```