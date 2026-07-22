# CH33 — Version Every Public Contract and Shared Record

## Shared meaning changes even when object names do not

A platform often assumes that versioning matters only for APIs, files and software releases.

That is too narrow for MarkOrbit.

A shared concept can change when:

- a field is added or reinterpreted;
- an identifier rule changes;
- a lifecycle state is split or merged;
- an authority requirement becomes stricter;
- an Evidence contract changes;
- a Projection exposes different fields;
- a Handoff or Return requires new acceptance behavior;
- a Product begins relying on a previously optional value.

The object may still be called `Matter`, `Capability`, `Projection` or `Handoff`, while its practical contract has changed.

Book 02 therefore requires explicit versioning for every public contract and every shared semantic record whose meaning or use may affect independent consumers.

```text
Same Object Name
≠ Same Contract
```

## What must be versioned

Versioning applies to more than schemas.

A complete public contract may include:

- semantic definition;
- identifier rules;
- required and optional fields;
- lifecycle states and transitions;
- authority requirements;
- validation rules;
- Evidence expectations;
- error and Unknown behavior;
- compatibility guarantees;
- deprecation policy;
- privacy and rights constraints;
- consumer obligations.

A change to any of these may be contract-significant.

```text
Schema Compatible
≠ Semantically Compatible
```

Adding an optional field can still be breaking if consumers begin treating its absence as failure. Renaming a status can be breaking even when the stored value remains technically readable. Relaxing a validation rule can be breaking if downstream systems relied on the previous guarantee.

## Contract version and record version are different

Book 02 separates:

```text
Contract Version
≠ Record Version
≠ Source Version
≠ Product Version
≠ Implementation Version
```

A Contract Version identifies the shared rules under which a record is interpreted.

A Record Version identifies a particular historical state of one object.

A Source Version identifies the external or upstream material from which a claim or record was derived.

A Product Version identifies the user-facing release that consumes the contract.

An Implementation Version identifies the code, model, workflow or tool route that produced or processed the record.

A trustworthy record may need to reference several of these simultaneously.

## Public contracts require stable identity

Each public contract should have:

- a stable contract identifier;
- an explicit version;
- publication status;
- effective date;
- compatibility declaration;
- owner or semantic authority;
- change history;
- superseded and successor references;
- migration guidance where applicable.

The stable identifier answers what contract family is involved. The version answers which exact meaning applies.

```text
Stable Identifier
+ Explicit Version
= Interpretable Contract Reference
```

## Shared records must preserve the contract they used

A record should not be interpreted only against the latest available schema.

It should preserve or make resolvable:

- contract identifier and version;
- record version;
- creation and effective time;
- Owning Service;
- authority context;
- source and Evidence versions;
- correction or supersession history.

This matters when an older record remains valid under an earlier contract.

```text
Latest Contract Published
≠ Historical Record Invalid
```

A previous filing Matter, Capability Certification or Handoff must remain reconstructable under the rules active when it was created or accepted.

## Semantic versioning requires semantic judgment

Numeric labels such as `1.2.0` are useful only when the platform defines what changes they represent.

A possible policy is:

```text
Major
= incompatible semantic, lifecycle, authority or consumer change

Minor
= backward-compatible shared capability or optional contract extension

Patch
= clarification, defect correction or non-semantic editorial repair
```

But the label cannot be determined mechanically from field diffs alone.

Examples of major changes may include:

- changing which service owns formal state;
- redefining Customer or Matter identity;
- adding a mandatory approval boundary;
- changing a lifecycle transition's legal or commercial meaning;
- making a previously local object universally shared;
- changing authority or data-disclosure rules.

Examples of minor changes may include:

- adding an optional Citation reference;
- adding a new compatible Projection profile;
- supporting a new explicit Unknown reason while preserving existing behavior.

Examples of patch changes may include:

- correcting a typo;
- clarifying an example without changing the contract;
- fixing a non-normative diagram.

```text
Small Diff
≠ Patch Change by Default
```

## Normative and explanatory content must be marked

Publication prose can explain a contract without changing it.

To prevent accidental activation, Book 02 should distinguish:

- normative contract language;
- explanatory guidance;
- examples;
- implementation notes;
- candidate semantics;
- deprecated material.

```text
Example Added
≠ Contract Expanded
```

A new example may reveal an ambiguity. It should not silently create a mandatory field or lifecycle state.

## Controlled values need independent versioning

Shared vocabularies may evolve independently from their containing objects.

Examples include:

- status values;
- Evidence types;
- Review types;
- authority roles;
- M0–M5 collaboration modes;
- R0–R4 risk or review tiers;
- source classifications;
- Brain Result types.

A controlled value set should preserve:

- set identifier and version;
- value identity;
- meaning;
- effective and deprecated status;
- aliases;
- compatibility mapping;
- permitted transitions or combinations.

```text
New Label
≠ New Meaning

Same Label
≠ Same Meaning
```

A label change may be only an alias. A retained label may conceal a changed meaning. Both require explicit treatment.

## Capability versioning must preserve outcome meaning

A Capability Definition should receive a new version when its outcome contract changes materially.

Relevant changes include:

- required inputs;
- accepted output;
- Evidence contract;
- jurisdictional scope;
- permitted implementations;
- review policy;
- authority ceiling;
- Unknown behavior;
- compatibility guarantees.

A model or Skill upgrade does not automatically require a new Capability version if the outcome contract remains unchanged.

```text
Implementation Changed
≠ Capability Changed by Default
```

Conversely, a Capability may change even when the implementation remains the same.

## Projection, Handoff and Return versions must bind exact payloads

A Projection must identify which source version and Projection contract produced the visible view.

A Handoff must identify the exact object, package and instruction versions passed to the destination.

A Return must identify the Handoff or Assignment version it answers.

```text
Return for Package v1
≠ Return for Package v2
```

If the package changes materially, prior acceptance, Review and Approval may no longer apply.

## Evidence and Decision versions must remain linked

A Decision should preserve the exact Evidence and Claim versions considered.

When Evidence changes later, the platform can identify which Decisions may require impact review.

```text
Evidence Corrected
≠ Decision Automatically Rewritten
```

The prior Decision remains historical fact. A new Decision may supersede it after review.

## Versioning across Data, Knowledge and Brain

These layers change independently:

```text
Data Product Version
Knowledge Version
Brain Policy Version
Model Version
Prompt or Instruction Version
Tool Version
```

A Brain Result should preserve the relevant combination. A Knowledge Claim should preserve its source and Knowledge Version. A Data Product consumer should preserve the release used.

This enables later reconstruction when an output changes after a model, source or policy update.

## Product-local versions must not redefine shared meaning

A Product may version its own records and interfaces independently.

For example, Lite may release a new Listing format or MarkReg may change a filing-package screen. Those Product versions should not redefine the shared meaning of Trademark, Projection, Handoff or Matter.

```text
Product Release
≠ Core Contract Release
```

If a Product needs new shared meaning, it must enter the F0–F4 admission process.

## Version status must remain explicit

Useful contract or record statuses include:

```text
Draft
Candidate
Active
Deprecated
Superseded
Withdrawn
Archived
Invalidated
```

These statuses have different implications.

`Deprecated` may still be supported temporarily. `Superseded` points to a successor. `Withdrawn` may indicate that publication authority was removed. `Invalidated` may require consumers to stop relying on the record.

```text
Not Active
≠ Safe to Delete
```

Historical reconstruction may require retaining the version even when new use is prohibited.

## Consumer-declared compatibility

A consumer should be able to declare:

- minimum supported version;
- maximum tested version;
- required features or fields;
- unsupported states;
- fallback behavior;
- migration readiness.

```text
Can Parse
≠ Can Safely Interpret
```

A consumer might technically parse a newer record while misunderstanding its authority or lifecycle meaning. Compatibility must therefore include semantic conformance, not only syntax.

## Unknown version is a governed failure state

If a consumer cannot determine the applicable contract version, it should not silently use the latest interpretation.

```text
Unknown Contract Version
≠ Use Latest by Default
```

The correct response may be:

- block the transition;
- request migration;
- require manual review;
- use a documented compatibility adapter;
- preserve the record as unresolved.

## Corrections and editorial changes

A correction should state whether it changes meaning.

If a published contract contained an error that affected interpretation, the correction may require a new semantic version and impact analysis, even if described as editorial.

```text
Called Editorial
≠ Non-semantic
```

The change record should explain:

- what was wrong;
- which versions and consumers were affected;
- whether historical records require reinterpretation;
- whether migration or re-review is required.

## Constitutional rule

```text
Every public contract and shared semantic record
must be interpretable against an explicit version.

Versioning must preserve meaning, authority,
lifecycle, evidence and compatibility—not merely syntax.
```
