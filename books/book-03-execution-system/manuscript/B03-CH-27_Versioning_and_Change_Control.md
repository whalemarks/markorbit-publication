# B03-CH-27 — Versioning and Change Control

## Chapter Purpose

Execution depends on meaning remaining stable long enough for people and Services to act responsibly.

That stability cannot be assumed.

Objects change. Documents are revised. Communications are edited. Workflow Contracts evolve. Policies are updated. Knowledge sources are superseded. Provider terms change. Jurisdiction requirements change. AI-assisted outputs are regenerated. Approvals expire or become inapplicable. An execution attempt that was valid yesterday may be stale today.

Versioning identifies what changed.

Change control governs whether that change may affect execution.

The governing principle is:

```text
Identify the exact version.
Classify the change.
Protect in-flight execution.
Require renewed authority when meaning changes.
Never apply a new meaning to an old decision silently.
```

This chapter defines how the MarkOrbit Execution System coordinates version-aware execution, controlled change, compatibility, activation, deprecation, supersession and migration while preserving the authority of Book 02 contracts and owning Services.

It does not define source-control branching, database migrations, package publishing, semantic-version algorithms, deployment pipelines or Product release screens.

The core governance path is:

```text
change proposed
→ identify governed subject and current version
→ classify the change and affected execution meaning
→ determine compatibility and protected-action impact
→ review Permission, Policy and Human Review requirements
→ approve, reject, defer or constrain activation
→ protect or reconcile in-flight executions
→ delegate mutation to the owning Service
→ record activation, supersession and audit references
→ prevent stale versions from silently controlling new action
```

Versioning is not merely a technical history mechanism.

In a professional operating system, versioning preserves the relationship between evidence, judgment, authority and action.

---

## 1. Dependency Baseline

This chapter builds directly on Chapters 12, 14–16 and 25–26. Its primary Book 02 dependencies are the approved versioning, audit, Human Review, Permission, Policy, idempotency and error contracts, together with the relevant Task, Communication and Workflow API contracts.

Book 02 owns canonical structures, controlled values and Service behavior. This chapter defines only how Execution consumes them.

## 2. Version, Revision, State and Release Are Different

These terms must not be used interchangeably.

| Term | Governance meaning |
|---|---|
| Version | An identified form of a governed object, contract, content item or rule set |
| Revision | A change that produces a new identified form |
| State | The current lifecycle or execution condition of an object or operation |
| Release | An approved package or set of versions made available for defined consumption |
| Activation | The moment a version becomes effective for a defined scope |
| Effective date | The time from which a version governs specified action |
| Supersession | Replacement of one version by another for future use |
| Deprecation | A controlled signal that a version should no longer be selected for new use |
| Retirement | Removal from active consumption while preserving historical trace |
| Migration | Governed movement of data, references or execution context to a newer version |
| Rollback | A separately governed decision to restore a prior approved version or behavior |
| Compatibility | The degree to which a new version may be consumed without changing governed meaning or required action |
| Snapshot | A fixed reference to the versions and context used at a particular decision or execution point |

A state transition does not always create a new content version.

A content revision does not automatically activate a new execution rule.

A release does not automatically migrate in-flight Workflows.

Deprecation does not erase historical validity.

Rollback does not erase that the newer version existed or may have produced effects.

---

## 3. Why Versioning Is an Execution Concern

Book 02 defines versionable Core contracts and objects.

Execution must answer a different set of questions:

```text
Which exact version was used?
Was that version active for this scope?
Did the version change after review?
Does the current approval still apply?
May an in-flight operation continue?
Must a preview be regenerated?
Does the change alter professional meaning?
Can an old result be replayed safely?
Which version governs a retry?
Which version should a new Task or Communication consume?
```

Without version-aware execution, the system may:

- send a Communication different from the reviewed draft;
- file a package different from the approved package;
- apply a new Policy to an earlier decision without disclosure;
- execute an old Workflow Contract against a changed object;
- use superseded Knowledge as current authority;
- compare providers using terms from different dates;
- reuse an approval after material fields changed;
- replay a result generated under an incompatible contract;
- show a Product user the current state while acting on stale state.

Versioning protects the integrity of the decision chain:

```text
source
→ interpretation
→ preparation
→ review
→ approval
→ protected action
→ Event and audit trace
```

Every link that matters must be version-identifiable.

---

## 4. Governed Version Surfaces

Not every change has the same execution effect.

The Execution System may encounter versions across several surfaces.

### 4.1 Core Object Version

Examples include versions of:

- Trademark records;
- Matter records;
- Document records;
- Evidence records;
- Communication records;
- provider references;
- classification selections;
- applicant or owner information;
- Task content where Book 02 permits versioned Task definition.

The owning Service determines what constitutes a new object version.

Execution must not invent object-version semantics.

### 4.2 Content Version

Content requiring exact version binding may include:

- Communication draft;
- application package;
- office action response draft;
- Evidence bundle;
- assignment document set;
- renewal instruction;
- provider instruction;
- quote comparison;
- classification proposal;
- review memorandum.

A content version often represents what a Human Reviewed.

### 4.3 Workflow Contract Version

A Workflow Contract version may change:

- required steps;
- transition conditions;
- review gates;
- protected actions;
- Service dependencies;
- validation requirements;
- completion criteria;
- allowed alternate paths.

A new Workflow Contract version must not silently reinterpret an active Workflow.

### 4.4 Policy and Permission Version

Policy or Permission changes may alter:

- access;
- approval requirements;
- retention;
- external sharing;
- provider selection;
- AI assistance;
- Communication send;
- filing authority;
- audit obligations.

Current Policy may block continuation even when an earlier version permitted it.

Historical audit must still identify the Policy version used at the time.

### 4.5 Knowledge Version

Knowledge changes may include:

- jurisdiction requirements;
- fee schedules;
- filing rules;
- classification guidance;
- provider information;
- official forms;
- deadline rules;
- procedural interpretations;
- professional playbooks.

A Knowledge update may require regeneration or renewed review, but it does not automatically change a Core object.

### 4.6 External Version

External versions may include:

- provider terms;
- official forms;
- filing portal behavior;
- fee schedules;
- API schemas;
- external status vocabulary;
- document templates.

Execution must not treat an external change as governed Core truth until the owning domain or Knowledge process accepts and versions it.

### 4.7 AI Output Version

An AI-assisted output is version-sensitive to:

- model or capability;
- prompt or instruction set;
- source set;
- source versions;
- retrieval result;
- tool result;
- structured-output contract;
- generation time;
- human edits.

AI output versioning supports traceability.

It does not grant AI authority or professional correctness.

---

## 5. Exact Version Binding

A protected execution decision must bind to the exact version that was evaluated.

The binding may include:

- subject version;
- target version;
- content version;
- Workflow Contract version;
- Policy version;
- Permission context;
- Knowledge source versions;
- provider terms version;
- review version;
- approval version;
- intended-action version;
- attachment versions;
- external form or schema version where material.

This is a conceptual governance set. Book 03 does not define a new aggregate contract.

### 5.1 Review Binding

Human Review must answer:

```text
What exact version did the reviewer see?
What sources supported it?
What action was being reviewed?
What scope and constraints applied?
```

A review of version `v3` is not review of `v4`.

### 5.2 Approval Binding

Approval must be bound to:

- exact approved version;
- exact intended action;
- exact scope;
- applicable constraints;
- reviewer identity or role;
- decision time;
- expiry or revocation where applicable.

Approval is not transferable merely because a later version looks similar.

### 5.3 Apply Binding

Apply must verify that:

```text
reviewed version
= approved version
= requested apply version
= current version allowed for the action
```

Where equality is not required by the governing contract, compatibility must be explicit and approved.

Execution must not perform “best effort” matching.

---

## 6. Change Classification

Every governed change should be classified by execution effect.

A useful governance model is:

| Change class | Meaning | Default execution effect |
|---|---|---|
| Editorial | Wording or formatting changes without changed meaning | May preserve prior review only if the owning contract explicitly permits |
| Metadata-only | Non-substantive metadata changes | May be compatible, subject to scope |
| Clarifying | Makes existing meaning clearer without intending to change obligation | Requires compatibility review where protected action is involved |
| Additive | Adds optional fields, outputs or paths | Existing executions may continue if unaffected |
| Restrictive | Narrows permission, access, action or acceptable state | Current restrictive rule usually applies before new protected action |
| Expansive | Broadens permission, scope or capability | Must not apply automatically to existing actors or approvals |
| Corrective | Fixes a known defect or inaccurate rule | May require affected-execution review and remediation |
| Material | Changes professional, legal, financial or operational meaning | Requires renewed review and controlled activation |
| Breaking | Existing consumers or decisions cannot safely continue unchanged | Requires explicit migration, version pinning or stop |
| Emergency | Urgent change needed to prevent harm or non-compliance | Requires constrained authority, trace and post-change review |
| Retirement | Ends availability for new use | Historical references remain preserved |

The owning Service or contract authority determines the canonical classification.

Execution uses the classification to decide how existing and new work may proceed.

### 6.1 Materiality Is About Meaning

A change can be technically small but professionally material.

Examples:

- changing one recipient address;
- changing one goods/services item;
- changing one filing basis;
- changing a fee;
- changing a deadline date;
- changing provider identity;
- changing an attachment;
- changing “may” to “must”;
- changing whether Human Review is required;
- changing whether AI may prepare a field.

Line count is not a materiality measure.

### 6.2 “No Material Change” Requires Authority

AI, Product UI or Workflow must not independently declare that a change is non-material.

Where materiality affects protected action, the determination belongs to the governing contract, owning Service or accountable Human Reviewer.

---

## 7. Change Control Lifecycle

Version creation and version activation are separate decisions.

A controlled change lifecycle may be understood as:

```text
proposal
→ impact identification
→ draft version
→ validation
→ compatibility assessment
→ review
→ approval
→ activation planning
→ activation
→ observation
→ supersession, deprecation or rollback where required
```

This is a governance lifecycle, not a Workflow Engine definition.

### 7.1 Proposal

A change proposal should identify:

- governed subject;
- current version;
- proposed version;
- reason;
- intended scope;
- affected domains and consumers;
- expected execution impact;
- urgency;
- known risks;
- proposed activation conditions.

A proposal does not create authority to activate.

### 7.2 Impact Identification

Impact analysis should consider:

- new executions;
- active Workflows;
- active Tasks;
- pending Human Reviews;
- approved but unapplied actions;
- Communications awaiting send;
- provider instructions;
- payments;
- filings;
- deadlines;
- Event and audit interpretation;
- Product consumers;
- AI-assisted outputs;
- integration and external dependencies.

### 7.3 Validation

Validation should confirm that the proposed version:

- satisfies Book 02 structure;
- uses valid references;
- preserves required invariants;
- identifies compatibility;
- does not create prohibited authority;
- includes required non-goals and boundaries;
- has an explicit activation scope.

Validation does not replace professional review.

### 7.4 Review and Approval

Review should be proportionate to consequence.

A material or breaking change may require:

- domain owner review;
- Policy review;
- security or privacy review;
- professional review;
- execution impact review;
- migration review;
- release approval.

The existence of a merged file or deployed package is not governance approval.

### 7.5 Activation

Activation should define:

- effective version;
- effective time;
- applicable organizations, domains or jurisdictions;
- whether only new operations use the version;
- whether active operations remain pinned;
- migration requirements;
- fallback or rollback conditions;
- notification and audit requirements.

Activation must not be inferred from file modification time.

---

## 8. Activation Models

Different changes require different activation models.

### 8.1 New-Execution-Only Activation

The new version governs operations created after activation.

Existing operations remain pinned to their prior versions unless separately migrated.

This is often safest for:

- Workflow Contract changes;
- review model changes;
- Task structure changes;
- Communication preparation changes;
- non-urgent process improvements.

### 8.2 Next-Protected-Action Activation

An active operation may retain earlier preparation context, but must use the new version before its next protected action.

This may be appropriate when:

- a new Policy restricts send;
- filing requirements change;
- provider terms change;
- a required official form changes;
- security rules tighten.

Execution must regenerate, revalidate or re-review affected content where necessary.

### 8.3 Immediate Restrictive Activation

Some restrictive changes may need immediate effect.

Examples:

- revoked Permission;
- prohibited provider;
- compromised channel;
- security exposure;
- invalidated form;
- legal prohibition.

Immediate activation may block in-flight operations before the next protected effect.

It must still preserve trace and explain the stop.

### 8.4 Scheduled Activation

A version may become effective at a future time.

Scheduled activation must account for:

- timezone;
- jurisdiction;
- deadline;
- active operations;
- review queues;
- external system availability;
- rollback plan.

Execution must not apply the scheduled version early.

### 8.5 Scoped Activation

A version may apply only to:

- a jurisdiction;
- an organization;
- a provider;
- a service class;
- a product;
- a controlled pilot;
- a defined Matter category.

Scope must be explicit.

Product segmentation must not silently redefine Core scope.

---

## 9. In-Flight Execution Governance

A version change is most dangerous when work is already underway.

An in-flight execution may have:

- completed preparation;
- pending review;
- completed approval;
- pending apply;
- partial Service effects;
- pending external confirmation;
- active Tasks;
- deadline-sensitive work;
- uncertain outcomes.

The system must not assume that every active operation should immediately adopt the newest version.

### 9.1 Pin, Revalidate, Migrate, Stop or Complete

For each in-flight execution, the governed decision may be:

| Decision | Meaning |
|---|---|
| Pin | Continue under the existing version within its approved scope |
| Revalidate | Confirm that current versions and conditions still permit the next action |
| Migrate | Move to the new version under an explicit migration decision |
| Stop | Block continuation because compatibility or authority is insufficient |
| Complete under old version | Finish a narrowly defined operation where allowed |
| Restart under new version | End the old request and create a new governed operation |

These decisions are not interchangeable.

### 9.2 Pending Review

If content changes before review completes, the reviewer should receive the new version or an explicit change comparison.

The system must not attach the review decision to a version the reviewer did not see.

### 9.3 Approved but Unapplied

An approved action that has not yet been applied requires special attention.

Execution must determine whether:

- the approved version is still current;
- the applicable Policy changed;
- the provider or destination changed;
- the action remains legally and operationally valid;
- the approval remains within time and scope.

Where meaning changed, new approval is required.

### 9.4 Partially Completed

A partially completed operation cannot be migrated by pretending no earlier effects occurred.

Migration or continuation must preserve:

- completed effects;
- Event references;
- external references;
- prior versions;
- remaining steps;
- compatibility constraints;
- prohibited repetition.

### 9.5 Deadline-Sensitive Work

A version change near a deadline must expose:

- deadline source and version;
- current execution status;
- effect of adopting the new version;
- effect of remaining pinned;
- required Human Review;
- escalation path.

Execution must not choose legal strategy automatically.

---

## 10. Compatibility Governance

Compatibility is not merely whether code continues to run.

It is whether governed meaning remains safe.

### 10.1 Structural Compatibility

A consumer can still read and validate the structure.

Structural compatibility does not prove professional compatibility.

### 10.2 Behavioral Compatibility

The same request produces equivalent governed behavior.

A changed validation rule, review gate or allowed transition may break behavioral compatibility even when the data shape is unchanged.

### 10.3 Professional Compatibility

The change does not alter legal, financial, evidentiary, communicative or professional meaning for the operation.

This may require human judgment.

### 10.4 Authority Compatibility

Existing Permission, Policy and Human Review remain valid for the new version.

A version may be structurally compatible but authority-incompatible.

### 10.5 Audit Compatibility

Historical Events and decisions remain interpretable under the version references recorded at the time.

New terminology must not rewrite old history.

### 10.6 Compatibility Result

A compatibility assessment may conclude:

```text
compatible
compatible with constraints
requires revalidation
requires renewed Human Review
requires migration
breaking
unknown
```

The controlled values belong to Book 02 if formalized.

Execution must fail safely when compatibility is unknown and protected action is involved.

---

## 11. Human Review and Change Approval

Human Review governs both content and change where professional meaning is affected.

### 11.1 Review of the Change

A reviewer may need to assess:

- what changed;
- why it changed;
- affected operations;
- compatibility;
- required migration;
- risk of continuing the old version;
- risk of adopting the new version;
- activation scope;
- rollback conditions.

### 11.2 Review of Affected Work

Approval of a new Workflow Contract or Policy does not automatically approve every affected Matter, Communication or filing.

Affected work may require its own renewed review.

### 11.3 Change Comparison

A review should receive a meaningful comparison, not only two complete documents.

Useful comparison dimensions include:

- added, removed and changed fields;
- changed sources;
- changed professional conclusions;
- changed recipients;
- changed attachments;
- changed providers;
- changed fees;
- changed deadlines;
- changed protected actions;
- changed Policy or Permission requirements;
- changed AI involvement.

AI may prepare the comparison.

The Human Reviewer owns the decision.

### 11.4 Approval Scope

Change approval should state whether it authorizes:

- creation of the version;
- activation;
- scoped pilot;
- migration;
- emergency use;
- deprecation of the prior version;
- rollback if defined conditions occur.

These are separate authorities.

---

## 12. Permission and Policy Change

Permission and Policy versions require careful temporal treatment.

### 12.1 Current Authority Governs New Protected Action

A user who was authorized when preparation began may no longer be authorized when apply is requested.

Execution must evaluate current Permission before the protected action.

### 12.2 Restrictive Changes

Restrictive changes generally take effect before new protected action according to their activation scope.

Examples:

- provider access revoked;
- Communication channel prohibited;
- external sharing restricted;
- AI assistance narrowed;
- approval level increased.

An old approval does not bypass a current restriction.

### 12.3 Expansive Changes

A broader Permission or Policy must not retroactively authorize earlier conduct.

It also must not automatically expand existing approval scope.

### 12.4 Historical Interpretation

Audit must preserve the version that governed the original action.

A later Policy version must not make an earlier Event appear compliant or non-compliant without an explicit retrospective analysis.

### 12.5 Policy Exception

An exception is a separate governed decision.

It must identify:

- Policy version;
- scope;
- actor;
- reason;
- time boundary;
- affected action;
- required review;
- audit reference.

Execution must not manufacture exceptions.

---

## 13. Knowledge Change Control

Knowledge changes frequently and may affect preparation before Core contracts change.

### 13.1 Source Version and Effective Time

Knowledge should preserve:

- source;
- publication or retrieval date;
- effective date where known;
- jurisdiction;
- authority level;
- supersession relationship;
- confidence or verification status;
- reviewer where applicable.

Execution should disclose when an output relies on Knowledge that is:

- outdated;
- superseded;
- disputed;
- incomplete;
- unofficial;
- not yet professionally reviewed.

### 13.2 Knowledge Update Impact

A Knowledge update may require:

- regenerated preview;
- refreshed fee calculation;
- revised classification proposal;
- revised deadline analysis;
- changed document checklist;
- renewed provider comparison;
- new Human Review.

It does not automatically authorize mutation.

### 13.3 Historical Knowledge

Historical execution must retain the Knowledge version used at the time.

The system should not silently regenerate an old result using current Knowledge and present it as the original result.

### 13.4 Conflicting Sources

Where sources conflict, Execution may:

- preserve each source and version;
- identify the conflict;
- request professional review;
- block protected action;
- prepare a comparison.

AI must not select professional truth independently.

---

## 14. Communication and Document Version Control

Communication and Documents are high-risk version surfaces because small edits can change meaning.

### 14.1 Communication Draft

A Communication review must bind to:

- body version;
- subject version;
- recipient set;
- attachments;
- channel;
- sender identity;
- intended purpose.

A change to any material element may require renewed review.

### 14.2 Attachment Change

An unchanged message with a changed attachment is a changed Communication package.

The system must not preserve send approval automatically.

### 14.3 Document Replacement

Replacing a Document file must not erase the prior version if it supported:

- review;
- Evidence;
- filing;
- provider instruction;
- Event;
- audit.

The new Document may supersede the old one for future use while historical references remain stable.

### 14.4 Signed Documents

A signed version is not interchangeable with a later edited version.

Execution must not:

- edit the signed content silently;
- attach a signature to a new version;
- treat a corrected draft as the signed instrument;
- overwrite the signed Document reference.

Correction requires a separately governed process.

---

## 15. Workflow Contract Change Control

Workflow Contracts define coordination meaning.

Changes may affect:

- required steps;
- sequence;
- review gates;
- protected actions;
- Task generation;
- Service calls;
- completion;
- alternate paths;
- error handling;
- retry and idempotency expectations.

### 15.1 No Silent Rebinding

An active Workflow must not silently rebind from one Workflow Contract version to another.

The execution record should identify the version under which it began and any later migration decision.

### 15.2 Safe Additive Changes

A new optional reporting field may be compatible.

A new required review gate is not merely additive for active work.

### 15.3 Breaking Workflow Change

A breaking change may require:

- stop before next protected action;
- new preview;
- new Task plan;
- renewed review;
- migration mapping;
- new execution request;
- preservation of prior completed effects.

### 15.4 Workflow Does Not Own Migration Truth

Workflow coordinates a migration decision.

Owning Services remain responsible for object mutation, Task mutation, Communication mutation and Events.

---

## 16. Service and API Contract Change

Service and API contracts may evolve while Products and Execution continue to consume them.

Book 03 does not define implementation versioning, but it requires execution-safe behavior.

### 16.1 Consumer Expectations

A changed Service or API contract must not cause Execution to:

- reinterpret a success as failure;
- drop Human Review context;
- lose idempotency scope;
- discard version references;
- collapse uncertainty;
- bypass Permission or Policy;
- assume a new default;
- accept unknown fields as authority.

### 16.2 Default Changes

Changing a default can be breaking even when the interface shape remains stable.

Examples:

- default review requirement;
- default provider;
- default Communication channel;
- default deadline handling;
- default retry behavior;
- default AI assistance setting.

Protected behavior should prefer explicit values over silently changed defaults.

### 16.3 Unknown Version

When Execution cannot identify the contract version of a protected Service response, it should fail safely or degrade to a non-protected path.

It must not guess compatibility.

---

## 17. Migration Governance

Migration changes which version governs an existing object, reference or execution.

It is not a clerical copy.

### 17.1 Migration Preconditions

Before migration, Execution should establish:

- source version;
- target version;
- compatibility assessment;
- affected objects and operations;
- completed effects;
- pending reviews;
- required field mapping;
- changed semantics;
- Permission;
- Policy;
- Human Review;
- idempotency;
- rollback or stop conditions.

### 17.2 Migration Result

A migration result should make clear:

- what migrated;
- what remained pinned;
- what could not migrate;
- which reviews became stale;
- which Tasks require change;
- which Communications require regeneration;
- which external effects remain under the prior version;
- whether new protected action is blocked.

### 17.3 No Historical Rewrite

Migration must not rewrite:

- original review;
- original approval;
- original Event;
- original external submission;
- original Communication;
- original Policy version;
- original Knowledge basis.

It may create a new version and a traceable relationship.

### 17.4 Bulk Migration

Bulk migration increases consequence.

It requires:

- explicit scope;
- impact sample or preview;
- validation;
- staged activation where appropriate;
- failure handling;
- reconciliation;
- audit;
- stop conditions.

This chapter does not define batch jobs or migration scripts.

---

## 18. Deprecation, Supersession and Retirement

A version may remain historically valid while becoming inappropriate for new work.

### 18.1 Deprecation

Deprecation signals:

```text
Do not select this version for new use unless an explicit exception applies.
```

It does not necessarily stop active operations.

### 18.2 Supersession

Supersession identifies a preferred or governing replacement.

The relationship should be explicit.

### 18.3 Retirement

Retirement prevents active consumption under the defined scope.

Historical read and audit references should remain available according to Permission, Policy and retention rules.

### 18.4 Old Version Availability

An old version may need to remain available for:

- audit;
- dispute;
- Evidence;
- reproduction of an earlier result;
- explanation of a prior decision;
- reconciliation;
- legal retention.

Availability does not imply active authorization.

---

## 19. Rollback and Reversal

Rollback is not deletion of history.

It is a new governed decision to restore or reactivate a prior approved version or behavior.

### 19.1 Rollback Preconditions

Rollback should consider:

- why the current version is unsafe;
- whether the prior version remains valid;
- effects already produced by the current version;
- data created under the current version;
- compatibility with current Policy and Permission;
- external changes that make the prior version obsolete;
- Human Review;
- migration requirements;
- deadline consequences.

### 19.2 Rollback Does Not Undo External Effects

A rollback cannot automatically undo:

- sent Communications;
- payments;
- filings;
- provider instructions;
- signed Documents;
- disclosed Evidence;
- emitted Events.

Those effects require separate governed actions where reversal is possible.

### 19.3 Forward Fix

Sometimes a forward corrective version is safer than rollback.

Execution should not choose automatically.

The accountable authority must decide based on impact and compatibility.

---

## 20. Emergency Change Control

Urgent risk may require accelerated change.

Examples:

- compromised provider;
- invalid official form;
- critical security issue;
- unlawful data transfer;
- incorrect deadline rule;
- harmful autonomous behavior;
- broken review gate;
- duplicate-payment risk.

Emergency does not remove governance.

It changes the path and time available.

### 20.1 Minimum Emergency Controls

An emergency change should still preserve:

- identified authority;
- reason;
- scope;
- current and target versions;
- affected operations;
- activation time;
- stop conditions;
- restricted access;
- audit reference;
- post-change review;
- rollback or remediation consideration.

### 20.2 Emergency Restriction

A restrictive stop may be activated before a complete replacement exists.

For example:

```text
Disable protected send through the affected provider.
Allow preparation and read-only inspection.
Require manual review for alternate routing.
```

### 20.3 No Emergency Expansion by Default

An emergency must not be used to broaden AI authority, bypass Human Review, skip Policy or create hidden administrator powers.

---

## 21. Change Freeze and Deadline Windows

Some periods require increased stability.

A change freeze may apply around:

- major release;
- jurisdiction filing deadline;
- renewal deadline;
- scheduled migration;
- provider cutover;
- audit;
- incident recovery;
- high-volume submission period.

A freeze may prohibit:

- non-essential Workflow Contract changes;
- provider changes;
- review model changes;
- schema changes;
- Knowledge-source replacement without verification;
- Product defaults that affect protected action.

A freeze does not prohibit urgent corrective action.

Exceptions require explicit authority and trace.

---

## 22. Event Trace and Audit

Version and change control must support reconstruction of:

- prior version;
- proposed version;
- change reason;
- classification;
- impact assessment;
- reviewer;
- approval;
- activation scope and time;
- affected executions;
- migration decisions;
- deprecation or supersession;
- rollback or corrective action;
- Permission and Policy versions;
- Human Review bindings;
- external effects under each version.

### 22.1 Version References Are Part of Audit Meaning

An Event without relevant version context may be insufficient to explain what happened.

The owning Service remains responsible for governed Events associated with mutation.

Workflow may correlate version references and Event references.

It must not manufacture Events or rewrite old Events after a version change.

### 22.2 Current View vs Historical View

The current Product view may show the latest version.

Audit replay must show the version that governed the historical action.

The system must not render a historical Event using current content without clear disclosure.

### 22.3 Change Log Is Not Enough

A file changelog may describe what changed.

It does not replace governed execution audit because it may omit:

- affected objects;
- active Workflows;
- Human Review;
- activation scope;
- external effects;
- migration results;
- Permission and Policy context.

---

## 23. AI and Agent Boundary

AI may assist versioning and change control by:

- comparing versions;
- summarizing changes;
- identifying affected fields;
- mapping references;
- locating potentially affected operations;
- preparing compatibility questions;
- detecting stale approvals;
- preparing migration previews;
- drafting change notes;
- highlighting conflicting Knowledge sources.

AI output remains advisory.

AI and agents may not independently:

- classify a material change as non-material;
- approve a change;
- activate a version;
- migrate protected work;
- reuse approval for a changed version;
- alter signed Documents;
- rewrite historical Events;
- choose rollback;
- broaden Permission;
- bypass Policy;
- resolve professional-source conflict;
- mutate protected state;
- send, file, pay or instruct a provider;
- define professional truth.

### 23.1 Model Change

A changed AI model or prompt can change output even when source data is unchanged.

Where AI output affects professional preparation, the system should preserve enough context to identify that the output came from a different assistance version.

A model upgrade does not automatically validate earlier or later output.

### 23.2 Regeneration Is a New Version

Regenerating an AI-assisted draft creates a new content version when the output changes.

The new output requires the applicable review.

It must not inherit approval from the earlier output automatically.

### 23.3 Agent Migration

An agent may prepare a migration plan.

It may not execute protected migration unless an explicitly approved future contract permits a constrained action.

This chapter grants no such authority.

---

## 24. Governance Examples

### 24.1 Communication Changed After Approval

A Communication draft is approved. Before send, an attachment is replaced.

Unsafe response:

```text
The message body did not change, so send approval remains valid.
```

Governed response:

1. create or identify the new Communication package version;
2. invalidate or suspend the old send authorization for the changed package;
3. show the attachment change;
4. require renewed Human Review;
5. preserve the prior approved version for audit;
6. prevent send until exact-version approval exists.

### 24.2 Workflow Contract Updated During Active Matter Preparation

A new Workflow Contract adds a mandatory Evidence review before application readiness.

Governed response:

1. identify active executions using the prior version;
2. classify the change as material for affected Workflows;
3. decide whether active work remains pinned or must revalidate before next protected action;
4. preserve completed preparation;
5. create no duplicate Tasks without Task Service governance;
6. require Evidence review where activation scope demands it;
7. record the version and migration decision.

### 24.3 Provider Fee Changed After Selection

A provider was selected based on a quote. Before instruction, the provider updates the fee and service scope.

Governed response:

```text
Provider terms version changed.
The prior comparison and approval no longer match the intended engagement.
Recomparison and renewed approval are required.
```

Execution must not treat the provider identity as sufficient continuity.

### 24.4 Policy Restricts AI Assistance

A new Policy prohibits AI processing of a category of confidential Documents.

Governed response:

1. activate the restrictive Policy under its approved scope;
2. stop new AI processing for affected Documents;
3. preserve prior audit references without exposing restricted content;
4. identify in-flight AI-assisted outputs;
5. require Human Review before continued use;
6. do not allow Product or agent fallback to another model without Policy approval.

### 24.5 Knowledge Rule Superseded Near Deadline

A deadline calculation used a Knowledge source that is later superseded.

Governed response:

1. preserve the original source and calculated result;
2. identify the newer source and effective date;
3. compare the deadline effect;
4. escalate to qualified Human Review;
5. block automated certification;
6. preserve attempted actions and deadline evidence;
7. do not silently overwrite the historical result.

### 24.6 Emergency Provider Disablement

A provider is suspected of exposing confidential attachments.

Governed response:

1. immediately block new protected sends through the provider under emergency authority;
2. leave preparation and read-only review available where safe;
3. identify uncertain or in-progress sends;
4. reconcile external effects;
5. require governed selection of any alternate provider;
6. preserve audit and conduct post-change review;
7. do not automatically resend through another provider.

---

## 25. Governance Rules

Versioning and Change Control are correct when:

1. every protected decision identifies the exact version it evaluated;
2. review, approval and apply remain bound to version, scope and intended action;
3. version, state, release, activation and migration remain distinct;
4. materiality is based on governed meaning, not file size or edit count;
5. version creation does not automatically activate the version;
6. activation scope and effective time are explicit;
7. in-flight executions are pinned, revalidated, migrated, stopped or restarted through a governed decision;
8. current Permission and Policy govern new protected action;
9. historical audit preserves the versions used at the time;
10. compatibility includes behavioral, professional, authority and audit meaning;
11. migration does not rewrite history;
12. rollback is a new governed action and does not undo external effects automatically;
13. emergency change preserves minimum authority, scope and audit controls;
14. deprecated versions remain available for authorized historical interpretation;
15. Workflow coordinates change but does not own object mutation or Event truth;
16. AI assists comparison and impact analysis but does not approve, activate or migrate;
17. Product presentation does not silently substitute current content for historical content;
18. missing version or unknown compatibility causes protected execution to fail safely.

---

## 26. Product Boundary

Book 04 may present history, comparisons, activation, deprecation, migration and stale approval. It must distinguish current content from the version that governed a historical decision.

## 27. Implementation Boundary

This chapter defines no semantic-version syntax, source-control process, deployment pipeline, database migration, feature flag, API routing, Workflow Engine migration or autonomous change execution.

## 28. Chapter Result

Versioning preserves the exact meaning that governed preparation, review, approval and action.

Change control ensures that new meaning enters execution deliberately.

The operating rule is:

```text
Identify the exact governed version.
Separate revision from activation.
Classify materiality and compatibility.
Bind Human Review to the version actually reviewed.
Protect in-flight work.
Revalidate before the next protected action.
Migrate without rewriting history.
Preserve current and historical Policy meaning.
Keep mutation and Event authority with owning Services.
Keep AI advisory.
Never apply a new meaning to an old decision silently.
```

A reliable Execution System does not merely keep the latest version.

It preserves which version mattered, when it mattered, why it changed and who authorized the change.

The next chapter develops the accountable human control that governs protected action across execution: **Chapter 28 — Human Review Governance**.
