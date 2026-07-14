# B04-CH-22 — Product Embedding and Cross-Product Context

**Status:** Release Candidate 1  
**Chapter Map:** B04-TOC-V0.1  
**Part:** Part IV — Product Architecture and Product Embedding

## Chapter Purpose

CH20 established the constitutional principles of Product architecture.

CH21 explained how Products remain independently owned, designed, released, deployed, and replaceable while consuming stable shared foundations.

This chapter defines how an independent Product appears within or alongside Workplace:

> Where may a Product be placed, which Workplace surfaces may host or launch it, what authorized context may it receive, and how can context move across Product boundaries without transferring authority, private data, or ownership?

Product embedding is necessary because users should not experience MarkOrbit as disconnected applications.

A user may begin in Lite, open a MarkReg filing journey, compare providers through an MGSN interface, return to Workplace Review, and later inspect the formal outcome.

The experience should remain coherent.

But coherence must not be achieved by:

- turning Workplace into one universal Product;
- giving every embedded Product the full Workplace database;
- allowing a host surface to control Product semantics;
- allowing a Product to inherit the host’s authority;
- copying private client context across Product boundaries;
- treating one browser session as authorization;
- hiding which Product is active;
- merging Product state with formal business state.

The central proposition is:

```text
Embedded Product Experience
=
Independent Product
+ Authorized Host Surface
+ Explicit Product Entry
+ Purpose-Bound Context Package
+ Product Entitlement
+ Permission and Policy Evaluation
+ Minimum Sufficient Data
+ Stable References
+ Context Version and Expiry
+ Transparent Product Identity
+ Governed Result Return
```

Cross-Product Context means:

> a purpose-bound, source-linked, minimized, version-aware, and policy-filtered representation that allows one Product to continue a user journey in another Product without granting unrestricted access or transferring mutation authority.

The constitutional distinctions are:

```text
Embedding ≠ absorption

Host surface ≠ Product owner

Product entry ≠ Product authorization

Active session ≠ valid context

Context package ≠ database access

Context inheritance ≠ authority inheritance

Context continuity ≠ unrestricted memory sharing

Deep link ≠ Permission

Product card ≠ formal object

Embedded Product state ≠ Workplace state

Product result ≠ formal outcome

Return to Workplace ≠ transfer of domain ownership

Same organization ≠ same purpose

Same user ≠ same Product entitlement

Same subject ≠ same data scope

Cross-Product context ≠ transitive context
```

Book 02 remains authoritative for Identity, references, Permission, Policy, shared objects, Events, and Owning Services.

Book 03 remains authoritative for Execution, Workflow, Task, Review, approval, and protected-action coordination.

Parts I–III of Book 04 remain authoritative for Workplace context, data boundaries, AI Context, recommendations, Prepared Action, and Human Review.

This chapter defines Product placement and contextual entry.

It does not define final UI layouts or the complete cross-Product lifecycle model of CH27.

---

## 1. Product Embedding Is an Architectural Relationship

Product embedding means:

> an independent Product is made accessible through a Workplace or another Product surface while retaining its Product identity, user-value loop, state boundary, release ownership, and constitutional obligations.

Embedding may create a visually integrated experience.

It does not erase architectural separation.

The host may provide:

- entry point;
- organization context;
- navigation;
- subject references;
- entitlement check;
- display frame;
- return path.

The embedded Product continues to own:

- Product journey;
- Product-specific interaction state;
- Product logic;
- Product version;
- Product-level failure;
- Product outcome presentation.

---

## 2. Embedding Is Not Absorption

A Product is absorbed when the host begins to own or redefine:

- Product roadmap;
- Product loop;
- Product state;
- Product-specific semantics;
- Product release;
- Product outcome.

An embedded Product should not become an arbitrary collection of Workplace widgets.

The distinction is:

```text
Embedding
→ Product remains identifiable and independently governed

Absorption
→ Product identity and ownership disappear into the host
```

MarkOrbit requires embedding, not absorption.

---

## 3. Workplace Is a Host Environment, Not a Mega-Product

Workplace may host or connect several Products.

That does not make Workplace one Product containing every feature.

Workplace provides:

- organization identity;
- authorized context;
- Product access;
- operating surfaces;
- cross-Product visibility;
- review and outcome visibility.

Products provide focused user journeys.

The relationship is:

```text
Workplace hosts context and continuity.

Product owns focused value delivery.
```

---

## 4. A Product May Operate Within or Alongside Workplace

Product placement may include:

- embedded within a Workplace surface;
- opened as a full Product view;
- launched through a contextual deep link;
- opened in a separate application;
- invoked through a local/private bridge;
- used in standalone mode with Workplace context;
- exposed through an external participant surface.

Architectural conformance does not depend on one visual placement.

The context and authority rules remain stable.

---

## 5. Embedding Modes Must Be Explicit

A minimum conceptual set of embedding modes includes:

```text
Navigation Entry

Contextual Product Card

Inline Product Surface

Side Panel or Auxiliary Surface

Full Product Workspace

Review or Action Surface

External or Partner Surface

Local or Private Product Bridge

Standalone Product with Workplace Context
```

These are architectural placement modes.

They do not prescribe a frontend framework or component design.

---

## 6. Navigation Entry Provides Discovery, Not Context by Itself

A navigation item may allow the user to open a Product.

It may communicate:

- Product availability;
- Product identity;
- general purpose;
- entitlement.

Navigation entry alone should not imply:

- active client;
- active Matter;
- authorized private data;
- preselected action.

Where the Product requires subject context, it should request or receive an explicit context package.

---

## 7. Contextual Product Card Represents an Entry Opportunity

A Workplace surface may display a Product card such as:

```text
Continue in MarkReg

Open provider comparison

Launch class-selection Guide

Prepare content in Lite
```

The card may be generated from:

- Recommendation;
- Task;
- Matter;
- client;
- Product outcome;
- Value Candidate.

The card is an entry proposition.

It is not the Product journey itself.

It does not create a formal object or action.

---

## 8. Inline Product Surface Must Remain Bounded

A small Product experience may appear directly inside a Workplace surface.

Examples include:

- Lite recommendation explanation;
- MarkReg filing-readiness summary;
- MGSN provider comparison preview;
- Product-specific status view.

The inline surface should identify:

- Product origin;
- subject;
- scope;
- action boundary;
- next handoff.

Inline convenience must not hide which Product logic is being used.

---

## 9. Full Product Workspace Preserves Product Depth

Some journeys require a full Product environment.

MarkReg may require:

- long-form intake;
- document preparation;
- lifecycle state;
- professional review;
- filing and maintenance context.

Embedding should allow transition into a full Product workspace without forcing the journey into a small card or panel.

The host may remain visible or provide a return path.

The Product retains its own journey depth.

---

## 10. Review and Action Surfaces Are Specialized Embeddings

A Product may expose only the part required for:

- review;
- approval;
- confirmation;
- Prepared Action inspection;
- execution result;
- failure resolution.

The reviewer should not need full Product access if the review package is sufficient.

The surface must still preserve:

- Product origin;
- reviewed version;
- subject;
- sources;
- intended consequence;
- formal authority boundary.

---

## 11. External or Partner Surfaces Require Stronger Minimization

An external participant may access a limited Product surface.

Examples include:

- client confirmation;
- foreign associate response;
- provider quotation;
- document upload;
- review request;
- collaboration update.

The participant should receive only the minimum purpose-specific context.

External embedding must not expose the internal Workplace shell or unrelated Product state.

---

## 12. Local and Private Product Bridges Preserve Location Boundaries

A Product may use a local or private component for:

- local data search;
- document extraction;
- browser automation;
- rendering;
- local publication support;
- private Knowledge.

The Workplace or shared Product may connect through a governed bridge.

The bridge should preserve:

- local Product identity;
- requested Capability;
- data scope;
- result type;
- synchronization restriction;
- user confirmation;
- audit reference where required.

Local placement does not remove governance.

---

## 13. Standalone Product May Still Operate in Workplace Context

A Product may have its own application shell.

It may still consume:

- organization identity;
- Product entitlement;
- user role;
- client or Matter references;
- private Knowledge;
- business rules;
- review requirements.

Standalone does not mean disconnected.

The Product should not recreate the organization merely because it has its own interface.

---

## 14. Host and Guest Responsibilities Must Be Explicit

In an embedding relationship:

```text
Host
→ Workplace or Product surface providing placement and entry

Guest
→ independent Product receiving authorized context
```

The host may own:

- surface placement;
- navigation;
- current organization presentation;
- entry request;
- return path.

The guest Product may own:

- Product journey;
- Product validation;
- Product-specific state;
- Product result;
- Product failure.

Neither side should silently assume the other owns formal mutation.

---

## 15. Host Must Not Control Guest Semantics

The host may request:

```text
Open MarkReg for this trademark need.
```

It must not redefine:

- MarkReg intake completion;
- filing readiness;
- review status;
- lifecycle meaning;
- Product error state.

The guest Product owns its Product-specific interpretation within shared semantic boundaries.

---

## 16. Guest Product Must Not Expand Host Context

A Product receiving one subject reference must not automatically retrieve:

- all clients;
- all Matters;
- all private Knowledge;
- all Communications;
- all provider history.

The Product should request additional context only when the journey requires it and the user, Permission, and Policy allow it.

The rule is:

```text
Received context defines a maximum starting scope.

It is not permission to explore the entire Workplace.
```

---

## 17. Product Identity Must Remain Visible

Users should be able to understand which Product is active.

This matters because Products may differ in:

- purpose;
- data access;
- AI behavior;
- review requirements;
- Product state;
- formal handoff.

Product identity may be visible through:

- name;
- Product context label;
- navigation state;
- outcome attribution;
- review package.

The design may remain visually coherent.

The Product origin must remain traceable.

---

## 18. Organization Context Must Be Visible Where Risk Requires It

A user may belong to several Workplaces.

The embedded experience should make the active organization clear where a mistake could cause:

- wrong pricing;
- wrong client data;
- wrong brand;
- wrong provider instruction;
- wrong filing authority;
- cross-organization leakage.

The Product should not treat organization switching as cosmetic.

---

## 19. Product Entry Requires an Explicit Context Request

A Product entry should identify:

- source Product or Workplace surface;
- destination Product;
- organization;
- actor;
- purpose;
- subject;
- requested mode;
- expected outcome.

The destination Product may accept, narrow, reject, or request clarification.

Entry is not one untyped redirect.

---

## 20. Cross-Product Context Must Be Purpose-Bound

A context package should state why the destination Product needs the context.

Example:

```text
Purpose:
Prepare a trademark filing intake
for internal review.
```

This purpose constrains:

- subject;
- data;
- Knowledge;
- Skills;
- AI access;
- retention;
- output;
- return result.

The same trademark reference may support a different context for content creation or provider routing.

---

## 21. Cross-Product Context Must Be Minimal

A minimum context package may include:

```text
organization reference

actor reference

source Product

destination Product

purpose

subject references

selected client or Matter reference

Product entitlement

allowed data scope

Permission and Policy references

review requirements

source and provenance

version and time

return route
```

It should not include full Product state unless required.

---

## 22. Context Package Is Not Direct Database Access

A destination Product should receive:

- stable references;
- selected fields;
- Metadata;
- safe summaries;
- authorized extracts;
- temporary access.

It should not be granted broad database access merely to simplify integration.

The Product may resolve references through authorized services.

The package defines context.

It does not expose the entire source system.

---

## 23. Stable References Preserve Ownership

Cross-Product context should use stable references where formal objects already exist.

Examples include:

- Customer reference;
- Trademark reference;
- Matter reference;
- Task reference;
- Artifact reference;
- Communication reference;
- Opportunity reference;
- Routing reference.

The destination Product can consume the reference.

The owning domain retains lifecycle authority.

---

## 24. Product-Specific State Should Not Be Exported by Default

Product state may include:

- open panel;
- filter;
- current Guide question;
- local draft;
- dismissed card;
- unsaved form.

Most of this state is not required by another Product.

Only state that supports a defined handoff should be exported.

This reduces coupling and privacy risk.

---

## 25. Context May Include a Prepared Action

A Product may hand off:

- recommendation;
- selected option;
- completed intake draft;
- Prepared Action;
- review request;
- Artifact reference.

The destination should know the exact type.

A Prepared Action remains subject to CH18 and CH19 governance.

It does not become executable because it crossed a Product boundary.

---

## 26. Context May Include Product Outcome References

A source Product may provide:

- completed Guide result;
- validation result;
- provider comparison;
- recommendation;
- delivered Artifact;
- formal result reference.

The destination should preserve:

- Product origin;
- version;
- output classification;
- source;
- review status;
- authority.

A Product result is not automatically a formal business fact.

---

## 27. Context Authority Is Not Transitive

Suppose:

```text
Lite receives client context from Workplace.

Lite launches MarkReg.

MarkReg launches an MGSN provider comparison.
```

The MGSN interface must not assume it inherits all context and authority granted to Lite or MarkReg.

Each boundary requires:

- purpose;
- minimization;
- entitlement;
- Permission;
- Policy;
- data classification.

The rule is:

```text
Product A may receive context from Workplace.

Product A cannot independently delegate all of it to Product B.
```

---

## 28. Same Organization Does Not Mean Same Purpose

Two Products may serve the same organization and user.

They may still require different data scopes.

Example:

- MarkReg may need applicant documents;
- Lite content creation may need only public trademark fields;
- MGSN provider discovery may need capability requirements but not Evidence.

Organization membership is necessary context.

It is not a universal data grant.

---

## 29. Same Subject Does Not Mean Same Representation

The same trademark may appear as:

- public identity;
- client portfolio asset;
- active Matter subject;
- content topic;
- provider-routing requirement;
- Evidence subject.

Each Product may receive a different authorized representation.

Shared reference preserves identity.

Purpose controls representation.

---

## 30. Same User Does Not Mean Same Product Entitlement

A user may be authorized for one Product and not another.

They may also have different roles in each Product context.

Product entry should verify:

- Product access;
- edition;
- organization enablement;
- role;
- feature scope;
- data scope.

A deep link must not bypass entitlement.

---

## 31. Deep Link Is a Navigation Reference, Not Authority

A deep link may include:

- Product;
- route;
- subject reference;
- display mode;
- return route.

It should not carry unrestricted sensitive payloads.

Opening a link does not prove:

- user identity;
- Permission;
- Product entitlement;
- target validity;
- action authority.

The destination revalidates context.

---

## 32. Browser Session Is Not Cross-Product Authorization

Two Products may run in the same browser or device.

That does not mean one Product may read the other’s:

- local storage;
- unsaved data;
- session data;
- cookies;
- private context;
- credentials.

Technical proximity does not create architectural access.

---

## 33. Context Must Be Version-Aware

The source context may change after Product entry.

Examples:

- client instruction changed;
- Matter state changed;
- fee changed;
- reviewer changed;
- provider selected;
- Task completed;
- Policy changed.

The destination Product should know:

- context assembly time;
- source version;
- freshness;
- refresh requirement;
- expiry.

---

## 34. Context Refresh Must Be Controlled

A Product may refresh context:

- on entry;
- before protected preparation;
- before review;
- before handoff;
- after Event;
- on user request.

Refresh should not silently expand scope.

It may update the permitted representation.

Material change may require:

- warning;
- draft invalidation;
- reassembly;
- new recommendation;
- new review.

---

## 35. Context Expiry Must Be Enforced

A context package may expire due to:

- elapsed time;
- Product exit;
- user role change;
- organization switch;
- subject change;
- Permission change;
- Policy change;
- completion of purpose.

Expired context may remain in historical trace.

It must not remain active for current use.

---

## 36. Organization Switching Must Invalidate Embedded Context Where Required

A user may switch from one Workplace to another.

Embedded Products should not continue using the prior organization’s:

- client;
- pricing;
- private Knowledge;
- provider history;
- prepared action;
- review state.

The Product may:

- close the embedded session;
- ask the user to return;
- reassemble context;
- preserve an unsaved local draft under the original organization;
- block high-consequence continuation.

---

## 37. Subject Switching Must Be Deliberate

Changing from one client, trademark, or Matter to another may invalidate:

- source;
- recommendation;
- draft;
- Artifact;
- provider comparison;
- review;
- Prepared Action.

The Product should not silently reuse one subject’s context for another.

---

## 38. Embedded AI Must Follow Destination Product Context

An Assistant or AI Agent shown inside an embedded Product must operate under:

- destination Product;
- active organization;
- current subject;
- Product purpose;
- permitted data;
- Agent Contract;
- review boundary.

It must not continue using broad context inherited from the host Assistant unless explicitly authorized.

Persona continuity does not create context continuity automatically.

---

## 39. Host Assistant Must Not Impersonate Product Authority

A Workplace Assistant may explain:

```text
MarkReg reports that filing review is pending.
```

It should not independently state:

```text
Your application is approved for filing.
```

unless that status comes from the proper Product and authority record.

The host Assistant may summarize Product results.

It must preserve Product origin and formal authority.

---

## 40. Embedded Product Must Preserve Its Own Failure State

A Product may fail because of:

- missing context;
- entitlement;
- unsupported subject;
- stale reference;
- Capability failure;
- Product validation;
- Execution handoff.

The host should not replace this with an inaccurate generic success or failure.

The Product should return a typed result.

The host may present it coherently.

---

## 41. Return Path Must Be Defined

After the Product journey, the user may return to:

- originating Workplace surface;
- originating Product;
- Review queue;
- Matter view;
- Today Feed;
- outcome surface.

The return path should preserve:

- source;
- subject;
- result type;
- user intent;
- pending action;
- failure;
- correlation.

A back button alone is not an architectural handoff.

---

## 42. Result Return Must Be Minimal and Typed

A destination Product may return:

```text
GuideResult

Recommendation

ValidationResult

PreparedAction

ReviewRequest

ArtifactReference

FormalResultReference

Failure

CancelledByUser
```

The host should not infer more than the typed result states.

Returning a result does not transfer ownership of the underlying Product state.

---

## 43. Workplace May Aggregate Result Visibility

Workplace may show cross-Product results in:

- Today;
- Matter view;
- client view;
- Review queue;
- management surface;
- activity surface.

Aggregation should use references and authorized summaries.

Workplace does not need full internal Product state to provide organizational visibility.

---

## 44. Product Embedding Must Preserve Review Context

When an embedded Product submits work for review, the Review surface should preserve:

- Product origin;
- Product version;
- subject;
- prepared output;
- source and provenance;
- intended consequence;
- required reviewer;
- return route.

Review should not occur against an anonymous snapshot with no Product context.

---

## 45. Product Embedding Must Preserve Execution Boundary

An embedded Product may prepare or request action.

It must not gain direct mutation authority because it is displayed inside Workplace.

The chain remains:

```text
Embedded Product
→ Prepared Action
→ Human Review and Approval
→ Execution
→ Owning Service
```

Placement never changes authority.

---

## 46. Product Embedding Must Preserve External Representation

When Product output becomes external, the system should preserve:

- acting organization;
- appropriate brand or legal identity;
- responsible human;
- Product origin where relevant;
- Artifact or Document version;
- approval;
- Delivery or send authority.

An embedded Product must not accidentally use the host’s display identity as the legal external identity.

---

## 47. Embedding Compatibility Must Be Governed

Host and Product versions may evolve independently.

Embedding should consider compatibility of:

- context package version;
- Product route;
- reference types;
- result types;
- entitlement;
- review package;
- return path.

The architecture does not define a protocol.

It requires explicit compatibility and safe failure.

---

## 48. Unsupported Embedding Must Fail Safely

A Product may not support:

- the requested mode;
- current context version;
- subject type;
- local deployment;
- required data boundary;
- review integration.

The Product should:

- reject safely;
- suggest standalone entry;
- request a narrower context;
- offer read-only view;
- preserve the user’s preparation.

It must not silently ignore required context.

---

## 49. Product Embedding Does Not Require Visual Uniformity

A shared shell or design system may improve usability.

But architectural conformance does not require every Product to look identical.

The important consistency is:

- organization visibility;
- Product identity;
- status meaning;
- authority boundary;
- AI disclosure;
- review and action semantics;
- failure language.

Visual sameness cannot substitute for semantic consistency.

---

## 50. The Minimum Embedding and Context Model

```text
Host Surface
  │
  ├── organization
  ├── actor
  ├── source Product or Workplace
  ├── purpose
  ├── subject
  └── requested Product entry
        │
        ▼
Entry Validation
  │
  ├── destination Product
  ├── entitlement
  ├── Permission
  ├── Policy
  ├── supported mode
  └── context compatibility
        │
        ▼
Authorized Context Package
  │
  ├── stable references
  ├── selected fields
  ├── data scope
  ├── source and provenance
  ├── version and time
  ├── review requirements
  ├── expiry
  └── return route
        │
        ▼
Independent Product Journey
  │
  ├── Product-specific state
  ├── Capability and Skill use
  ├── Assistant / Guide / Agent
  ├── validation
  └── preparation
        │
        ▼
Typed Product Result
  │
  ├── recommendation
  ├── prepared action
  ├── review request
  ├── Artifact reference
  ├── formal result reference
  ├── failure
  └── cancellation
        │
        ▼
Host Return and Workplace Visibility
        │
        ▼
Governed Execution or Continued Product Journey
where required
```

The host preserves organizational continuity.

The Product preserves Product ownership.

The context package connects them without transferring authority.

---

## 51. Required Distinctions

```text
Embedding ≠ absorption
```

The Product remains independently owned.

```text
Host surface ≠ Product owner
```

Placement does not transfer Product responsibility.

```text
Product entry ≠ authorization
```

The destination validates entitlement, Permission, and Policy.

```text
Context package ≠ database access
```

The package carries a minimized representation.

```text
Stable reference ≠ lifecycle ownership
```

The owning domain remains authoritative.

```text
Deep link ≠ Permission
```

Navigation does not create authority.

```text
Same browser ≠ shared data access
```

Technical proximity is not authorization.

```text
Same organization ≠ same purpose
```

Purpose constrains data use.

```text
Same subject ≠ same representation
```

Products receive purpose-specific views.

```text
Same user ≠ same Product entitlement
```

Product access remains contextual.

```text
Context continuity ≠ unrestricted memory sharing
```

Only necessary context crosses the boundary.

```text
Context inheritance ≠ authority inheritance
```

Permission and Policy are re-evaluated.

```text
Cross-Product context ≠ transitive context
```

Each boundary requires explicit authorization.

```text
Product result ≠ formal outcome
```

Authority depends on the result type and Owning Service.

```text
Return to Workplace ≠ transfer of Product ownership
```

Workplace may aggregate visibility through references.

---

## 52. Failure Modes This Chapter Prevents

### Workplace mega-Product

Every Product is reduced to arbitrary Workplace screens.

### Embedded Product absorption

Product identity, roadmap, and state disappear inside the host.

### Full-context injection

Every embedded Product receives all organization and client data.

### Context laundering

Product A passes data to Product B without a new purpose and authorization check.

### Deep-link authority

A URL bypasses entitlement, Permission, or Policy.

### Same-session leakage

Products read each other’s local session, cookies, or unsaved data.

### Stale embedded context

A Product continues using old organization, client, fee, or Matter state.

### Silent organization switch

Prepared work from one Workplace is executed in another.

### Product-origin loss

A result appears in Workplace with no indication of which Product produced it.

### Host authority drift

The host Assistant invents or upgrades Product status.

### Product mutation drift

An embedded Product bypasses Execution because it runs inside Workplace.

### Result overinterpretation

The host treats a Guide result as formal completion.

### Context overexport

Product-specific filters, drafts, and local state are copied to unrelated Products.

### Unsupported-mode degradation

A Product silently ignores required data or review because embedding is incompatible.

### Visual-consistency substitution

Products look unified while semantics and authority differ.

These designs may feel integrated.

They do not conform to MarkOrbit architecture.

---

## 53. Minimum Conformance Rule

A conforming Product embedding must preserve the following lock:

```text
Embedded Products remain independent Products.

Workplace hosts organization context
and Product continuity,
not Product ownership.

Embedding mode remains explicit.

Host and guest responsibilities remain distinct.

Product identity remains visible and traceable.

Organization context is visible
where professional risk requires it.

Product entry is an explicit,
typed, and validated request.

The destination verifies Product entitlement,
Permission, Policy, subject,
purpose, and context compatibility.

Cross-Product context remains minimized,
purpose-bound, source-linked,
version-aware, and time-bound.

Context packages use stable references
and selected representations,
not unrestricted database access.

Product-specific state does not cross boundaries
unless required by a defined handoff.

Context authority is not transitive.

Same organization, user, browser,
or subject does not create universal access.

Organization and subject switching
invalidate context where required.

Embedded AI operates under
the destination Product context.

Products return typed and minimal results.

Workplace may aggregate visibility
without absorbing Product state or domain ownership.

Review, approval, Prepared Action,
Execution, and Owning Service boundaries remain intact.

Embedding compatibility is governed.

Unsupported embedding fails safely.

Visual integration never substitutes
for semantic and authority conformance.
```

An embedded experience that is seamless but cannot explain which Product, context, authority, and result were active does not conform.

---

## 54. Chapter Boundary

This chapter defines:

- Product embedding;
- embedding and absorption;
- Workplace hosting;
- within and alongside placement;
- embedding modes;
- navigation entry;
- Product cards;
- inline surfaces;
- full Product workspaces;
- review and action surfaces;
- external surfaces;
- local bridges;
- standalone Product context;
- host and guest responsibilities;
- Product identity;
- organization visibility;
- Product entry requests;
- purpose-bound context;
- minimized context packages;
- stable references;
- Product-specific state;
- Prepared Action and outcome references;
- non-transitive context;
- Product entitlement;
- deep links;
- browser and session boundaries;
- context version;
- refresh;
- expiry;
- organization and subject switching;
- embedded AI;
- return routes;
- typed results;
- Workplace aggregation;
- Review and Execution preservation;
- embedding compatibility;
- safe failure;
- visual consistency boundary.

It does not define:

- final Lite Product requirements;
- final MarkReg Product requirements;
- final MGSN interface requirements;
- Workplace editions;
- complete cross-Product lifecycle continuity;
- Product screen layout;
- iframe or component technology;
- authentication protocol;
- token format;
- frontend routing;
- database access;
- event-bus implementation;
- local-bridge protocol;
- deployment topology.

Those subjects belong to CH23–CH27, dedicated Product publications, technical specifications, ADRs, and implementation repositories.

This chapter does not modify Book 02 Core semantics.

It does not modify Book 03 Execution authority.

It does not authorize external Communication, filing, payment, provider appointment, publication, official recordal, or unrestricted cross-Product data sharing.

---

## 55. Chapter Conclusion

Product embedding should make MarkOrbit feel coherent without making it centralized.

The user should be able to move naturally from:

```text
Workplace
→ Lite
→ MarkReg
→ MGSN interface
→ Review
→ Execution result
```

But the architecture must still know:

```text
Which Product is active?

Which organization is acting?

Which user and Agent are involved?

What purpose justified the context?

Which subject is in scope?

Which data was authorized?

Which Product owns the journey?

Which service owns the formal result?

What should return to Workplace?
```

The correct embedding model is:

```text
Independent Product
+ explicit host placement
+ minimum authorized context
+ stable references
+ destination revalidation
+ typed Product result
+ governed return
```

The constitutional outcome is:

```text
Workplace provides authorized organization context.

Host surface provides placement.

Product provides the journey.

Context connects Products.

Permission and Policy constrain use.

Execution governs protected action.

Owning Services preserve formal authority.

Humans remain professionally accountable.
```

CH23 now applies these principles to the first Product profile:

> How should Lite operate as a lightweight Workplace for independent professionals and small teams without becoming a reduced but constitutionally weaker version of the full Workplace architecture?
