# CH34 — Compatibility, Deprecation and Migration Evidence

## Change is safe only when consumers can survive it

A shared contract does not exist in isolation. Products, Workplaces, Data services, Knowledge systems, Execution routes and Owning Services depend on it.

When Core semantics change, the platform must ask more than whether the new design is better.

It must ask:

- which consumers rely on the old meaning;
- which records were created under it;
- whether old and new versions can coexist;
- whether adapters preserve meaning;
- how migration will be verified;
- what happens when migration fails;
- how historical evidence remains reconstructable.

Book 02 therefore treats compatibility, deprecation and migration as semantic governance rather than release-management details.

```text
New Version Published
≠ Consumers Safely Migrated
```

## Compatibility has several dimensions

A contract may be compatible in one dimension and incompatible in another.

Book 02 distinguishes at least:

```text
Syntactic Compatibility
Semantic Compatibility
Lifecycle Compatibility
Authority Compatibility
Evidence Compatibility
Operational Compatibility
Historical Compatibility
```

Syntactic compatibility asks whether a consumer can parse the record.

Semantic compatibility asks whether the consumer interprets the fields and values correctly.

Lifecycle compatibility asks whether states and transitions remain valid.

Authority compatibility asks whether the same actors and services remain permitted to act.

Evidence compatibility asks whether existing evidence still satisfies the contract.

Operational compatibility asks whether workflows and integrations can continue safely.

Historical compatibility asks whether earlier records and decisions remain reconstructable.

```text
JSON Still Parses
≠ Contract Still Compatible
```

## Compatibility must be directional

Compatibility is not one universal yes-or-no property.

A newer producer may emit records that an older consumer can partially read. An older producer may omit fields that a newer consumer requires. A migration adapter may support one direction only.

A compatibility statement should identify:

- producer version;
- consumer version;
- direction;
- supported features;
- unsupported states;
- required adapter;
- known semantic loss;
- evidence and test coverage.

```text
A Compatible with B
≠ B Compatible with A
```

## Backward compatibility must not preserve unsafe authority

Sometimes a stricter contract is introduced because the earlier behavior was unsafe.

For example:

- an explicit Approval becomes mandatory;
- a data-disclosure field becomes purpose-bound;
- a Provider Return can no longer mutate formal state directly;
- a professional qualification must be verified before Assignment.

In such cases, backward compatibility cannot mean continuing the unsafe behavior indefinitely.

```text
Backward Compatible
≠ Preserve Every Historical Permission
```

The migration plan may need to suspend old routes, require revalidation or place records into a restricted legacy mode.

## Deprecation is a governed transition

Deprecation communicates that a contract, field, value, route or behavior remains temporarily supported but should no longer be used for new work.

A deprecation record should specify:

- deprecated item and version;
- reason;
- replacement;
- affected consumers;
- date announced;
- last date for new creation;
- support window;
- migration route;
- security or authority implications;
- removal criteria;
- escalation owner.

```text
Deprecated
≠ Deleted
≠ Invalid Immediately
```

A deprecated contract may remain necessary for historical reading while being prohibited for new creation.

## Supersession, withdrawal and invalidation are distinct

```text
Deprecated
≠ Superseded
≠ Withdrawn
≠ Invalidated
```

`Superseded` identifies a successor.

`Withdrawn` removes publication or adoption authority, often because the candidate or release should no longer be relied upon.

`Invalidated` indicates that use may be unsafe or incorrect and may require immediate consumer action.

The platform should not use one generic `inactive` status for all four conditions.

## Migration begins with an inventory

Before migration, the platform should identify:

- affected contracts and versions;
- affected record counts and owners;
- active Workflows and Assignments;
- Product Installations;
- projections, caches and indexes;
- integrations and external consumers;
- unresolved Candidates and Unknowns;
- historical Decisions and Evidence;
- legal, privacy and contractual constraints.

```text
Schema Known
≠ Migration Scope Known
```

A shared field may be copied into reports, emails, documents, data exports and external provider systems that are not visible from the primary database.

## Migration needs a semantic mapping

A migration mapping should state how every relevant old concept maps to the new contract.

Possible dispositions include:

```text
Unchanged
Renamed
Split
Merged
Reclassified
Deprecated
Removed
Unmappable
Requires Human Review
```

Each mapping should preserve:

- old and new identifiers;
- meaning before and after;
- authority changes;
- lifecycle changes;
- evidence requirements;
- transformation method;
- ambiguity and loss;
- validation rule.

```text
Field Copied
≠ Meaning Migrated
```

## Some migrations require new records, not mutation

When a concept changes materially, rewriting the old record may erase history.

A safer route may be:

```text
Legacy Record Preserved
→ Migration Candidate Created
→ Review
→ New-version Record Created
→ Link to Legacy Record
→ Consumer Cutover
```

This is especially important when changing:

- identity resolution;
- Customer or relationship ownership;
- professional authority;
- Matter formal state;
- Evidence sufficiency;
- payment or settlement meaning.

```text
Migration
≠ Historical Rewrite
```

## Active work requires special handling

A contract migration may affect work already in progress.

The plan should decide whether active items are:

- grandfathered under the old version;
- migrated immediately;
- paused for revalidation;
- split into old and new phases;
- cancelled and recreated;
- allowed to complete with additional controls.

```text
Template Updated
≠ Active Instance Updated
```

A Work Package, Assignment, Review or Approval bound to an earlier version cannot be silently reinterpreted under the new contract.

## Migration evidence must prove more than execution

A successful script run is not sufficient proof.

Migration Evidence may include:

- inventory report;
- mapping specification;
- transformed-record counts;
- rejected and quarantined records;
- before-and-after samples;
- authority and lifecycle checks;
- conformance test results;
- reconciliation report;
- consumer acceptance;
- rollback rehearsal;
- approval and sign-off;
- post-migration monitoring.

```text
Migration Job Completed
≠ Migration Semantically Accepted
```

## Conformance fixtures protect shared meaning

A conformance fixture is a controlled example that demonstrates expected behavior under a contract version.

Fixtures should cover:

- valid records;
- invalid records;
- Unknown values;
- authority failures;
- lifecycle edge cases;
- version transitions;
- deprecated values;
- conflicting Evidence;
- correction and rollback.

A consumer should prove that it interprets the fixture correctly, not merely that it can deserialize it.

```text
Parser Test Passed
≠ Semantic Conformance Passed
```

## Adapters must disclose semantic loss

Compatibility adapters can translate between versions, but they may lose information or authority context.

An adapter contract should state:

- source and target versions;
- supported fields and states;
- generated defaults;
- lost information;
- unresolved mappings;
- review requirements;
- permitted use;
- expiration.

```text
Adapter Exists
≠ Full Fidelity
```

A default inserted by an adapter must remain distinguishable from a source-confirmed value.

## Rollback must restore governed state

Rollback is not simply restoring an old database snapshot.

The platform must consider:

- external actions already performed;
- provider instructions already accepted;
- customer communications already sent;
- payments already initiated;
- records created under the new contract;
- source and Knowledge updates;
- audit and Evidence continuity.

```text
Code Rolled Back
≠ Business Effects Rolled Back
```

A rollback plan may require compensation actions, correction records, consumer notices or reconciliation rather than deletion.

## Dual-running requires clear authority

During migration, old and new versions may run in parallel.

The platform must identify:

- which version accepts new writes;
- which version is authoritative for each object;
- how updates synchronize;
- how conflicts are reconciled;
- when cutover occurs;
- which version downstream consumers should trust.

```text
Two Versions Active
≠ Two Formal Authorities
```

Dual-running without an authority rule creates divergent truth stores.

## External consumers require notification and evidence

Partners, providers and customer systems may depend on shared contracts.

A migration plan should define:

- notification audience;
- change summary;
- affected behavior;
- required action;
- compatibility window;
- test environment or fixtures;
- support route;
- acceptance evidence.

Silence from a consumer is not proof of compatibility.

```text
Notice Sent
≠ Consumer Ready
```

## Product-local migrations remain product-owned

A Product may migrate local records without a Core change where shared meaning is unchanged.

Examples include:

- a new Listing UI;
- a different content brief schema;
- an internal provider-ranking feature;
- a local reporting table.

Product-local migration should still preserve source, version and formal-state boundaries, but it does not automatically require a Core release.

```text
Local Schema Migration
≠ Core Migration
```

## Migration cannot activate candidate semantics by accident

A Product may already store a local concept that resembles a proposed Core Candidate.

Moving the field into a shared package before the formal Change Proposal is approved would silently activate the candidate.

```text
Existing Local Data
≠ Approved Shared Contract
```

The migration must wait for the admission decision, contract version, conformance fixtures and Owner approval.

## Completion criteria

A migration should be considered complete only when:

- the approved contract version is published;
- required records are migrated or explicitly grandfathered;
- rejected and unresolved records are governed;
- consumers demonstrate compatibility;
- active work has a declared version;
- formal-state ownership remains clear;
- rollback and correction paths are available;
- migration evidence is preserved;
- deprecated creation routes are closed;
- post-migration monitoring is accepted.

```text
Data Moved
≠ Migration Complete
```

## Constitutional rule

```text
Compatibility must preserve meaning and authority.
Deprecation must provide an accountable transition.
Migration must produce evidence that records,
consumers and active work remain correctly governed.

No shared semantic change is complete
merely because new code has been deployed.
```
