# B04-CH-21 — Product Independence and Shared Foundations

**Status:** Release Candidate 1  
**Chapter Map:** B04-TOC-V0.1  
**Part:** Part IV — Product Architecture and Product Embedding

## Chapter Purpose

CH20 established the constitutional principles of Product architecture.

It defined Product as the direct user-value unit and required every Product to preserve:

- a clear primary user;
- a clear primary problem;
- a focused value loop;
- authorized Workplace context;
- shared semantic conformance;
- governed preparation and handoff;
- human accountability;
- independent evolution.

This chapter develops the tension at the center of that model:

> How can Lite, MarkReg, MGSN interfaces, organization-specific applications, and future Products remain independently owned, designed, released, deployed, and replaced while still consuming stable shared semantics, governance, organizational context, Knowledge, Capabilities, Execution, Artifact rules, and network contracts?

Product independence is necessary.

Without it, every Product would wait for one central roadmap, one shared frontend, one release train, and one universal operating model.

Shared foundations are also necessary.

Without them, every Product would redefine Organization, Customer, Matter, Task, Review, Permission, Communication, Opportunity, Routing, AI governance, and formal-state authority.

The architecture must avoid both extremes:

```text
One shared monolith
and
many disconnected Product silos
```

The central proposition is:

```text
Independent Product
=
Independent User Proposition
+ Independent Product Ownership
+ Independent Roadmap
+ Independent Experience
+ Independent Release and Deployment
+ Product-Specific State and Logic
+ Conformance to Shared Foundations
+ Explicit Dependency Contracts
+ Governed Context and Handoffs
+ Replaceability
```

Shared foundations mean:

```text
Stable shared meaning
+ common governance contracts
+ reusable organization context
+ governed Execution boundaries
+ reusable Knowledge and Capabilities
+ common Agent and Artifact rules
+ network participation contracts
+ traceable outcomes
```

Shared foundations do not necessarily mean:

```text
one repository

one database

one frontend

one service

one deployment

one Product team

one release schedule

one cloud environment
```

The constitutional distinctions are:

```text
Product independence ≠ Product sovereignty

Shared foundation ≠ shared monolith

Shared meaning ≠ shared implementation

Shared contract ≠ synchronous dependency in every journey

Independent release ≠ semantic drift

Product extension ≠ Core redefinition

Local copy ≠ local authority

Product cache ≠ Product-owned truth

Shared capability ≠ mandatory use

Foundation availability ≠ Product usability in every mode

Compatibility ≠ identical Product behavior

Reuse ≠ centralization

Temporary duplication ≠ permanent semantic fork

Product replacement ≠ organizational migration
```

Book 02 remains authoritative for Core semantics, shared objects, Capability, Permission, Policy, Agent governance, Events, and Owning Services.

Book 03 remains authoritative for Execution, Workflow, Task, Review, approval, retry, failure, and protected-action coordination.

Workplace remains authoritative for organization-specific context.

This chapter defines the Product–foundation relationship.

It does not define service topology or repository architecture.

---

## 1. Product Independence Exists to Protect User Value

Product independence is not primarily an engineering preference.

It exists so each Product can serve its user and problem well.

Lite may need:

- rapid experimentation;
- lightweight onboarding;
- a Today-centered experience;
- fast recommendation loops;
- personal and small-team context.

MarkReg may need:

- deep trademark-domain behavior;
- long lifecycle continuity;
- country and class logic;
- professional review;
- filing and maintenance integrations.

MGSN interfaces may need:

- cross-Workplace discovery;
- capability evidence;
- provider comparison;
- trust context;
- collaboration preparation.

Forcing these Products into one design and release model would weaken all of them.

Independence protects focus.

---

## 2. Product Independence Requires Explicit Ownership

Every Product should have identifiable ownership for:

- target user;
- Product proposition;
- Product loop;
- roadmap;
- prioritization;
- Product-specific risk;
- user experience;
- release decisions;
- Product metrics;
- deprecation.

Shared architecture does not remove Product accountability.

A Product team should not blame a shared platform for an unclear Product proposition.

The shared foundations support the Product.

They do not define its user value automatically.

---

## 3. Product Independence Includes Roadmap Independence

Products may mature at different speeds.

Examples:

- Lite may validate personal assistance before enterprise administration;
- MarkReg may deepen filing before transaction services;
- MGSN may begin with private provider relationships before broader discovery;
- an organization-specific application may solve one internal workflow.

Each Product needs its own sequencing.

A shared roadmap may coordinate dependencies.

It should not force every Product to release the same concepts at the same time.

---

## 4. Product Independence Includes Experience Independence

Products may use different:

- navigation;
- interaction patterns;
- information density;
- terminology presentation;
- onboarding;
- Guide structure;
- recommendation surfaces;
- mobile or desktop emphasis.

Experience variation is desirable when the users and problems differ.

The shared requirement is not visual uniformity.

It is semantic and authority consistency.

---

## 5. Product Independence Includes Implementation Independence

A Product may choose different:

- frameworks;
- local or cloud components;
- databases for Product-owned state;
- rendering approaches;
- AI models;
- Skills;
- deployment patterns.

Implementation freedom is allowed where shared contracts remain intact.

The architecture should not confuse:

```text
common meaning
with
common code
```

---

## 6. Product Independence Includes Release Independence

A Product should be able to:

- release improvements;
- roll back;
- run experiments;
- support staged rollout;
- deprecate features;
- migrate implementation;

without requiring every other Product to release simultaneously.

Shared foundation changes must therefore support compatibility and controlled adoption.

A release train shared by every Product should be an implementation choice, not an architectural requirement.

---

## 7. Product Independence Includes Deployment Independence

A Product may be deployed:

- as a shared cloud service;
- in a private environment;
- locally;
- as an embedded module;
- through a hybrid model.

Deployment form should not change semantic or authority rules.

A locally deployed MarkReg edition must still respect Core meaning and Execution authority.

A shared Lite deployment must still respect private Workplace boundaries.

---

## 8. Product Independence Includes Replaceability

A Product may eventually be:

- rewritten;
- split;
- merged at the experience level;
- replaced;
- retired.

The organization should not lose:

- identity;
- clients;
- Matters;
- Tasks;
- private Knowledge;
- Artifacts;
- outcomes;
- network relationships.

Replaceability is evidence that the Product has not absorbed the entire organization.

---

## 9. Product Independence Does Not Mean Product Sovereignty

A Product is not a sovereign system inside MarkOrbit.

It cannot decide independently what shared concepts mean.

It cannot override:

- Core ownership;
- Permission;
- Policy;
- Review authority;
- Execution gates;
- Owning Service contracts;
- network-governance rules.

Product independence governs Product responsibility.

It does not create constitutional independence from MarkOrbit.

---

## 10. Shared Foundations Are Logical Responsibilities

A shared foundation is a stable responsibility or contract consumed by more than one Product or Workplace context.

It may later be implemented through:

- one service;
- several services;
- a library;
- a local component;
- a federated source;
- Product-specific adapters.

The logical foundation should be defined before technical form.

This allows the implementation to change without changing architectural meaning.

---

## 11. Shared Semantic Foundations Define Common Meaning

Shared semantic foundations include concepts that must mean the same thing across Products and organizations.

Examples include:

- Organization;
- User;
- Customer;
- Trademark;
- Matter;
- Task;
- Communication;
- Review;
- Opportunity;
- Routing;
- Document;
- Evidence;
- Capability;
- Event.

A Product may present a simplified view.

It must not create a competing canonical definition.

The test is:

```text
Must this concept remain interoperable
and historically understandable across Products?

If yes, its meaning requires shared governance.
```

---

## 12. Shared Identity Foundations Preserve the Acting Context

Products should consume common identity references for:

- organization;
- user;
- Agent;
- external collaborator;
- provider;
- client participant.

This does not require one login interface.

It requires stable identity meaning and trace.

A Product must not create an unlinked local identity whenever it can use an authorized shared reference.

---

## 13. Shared Permission and Policy Foundations Preserve Governance

Permission and Policy decisions must not vary silently by Product.

A Product may request or present them differently.

It cannot invent a weaker authority model because its interface is simpler.

Shared governance foundations should preserve:

- actor;
- organization;
- operation;
- target;
- data scope;
- purpose;
- decision;
- trace.

Product-specific rules may add restrictions.

They must not bypass shared restrictions.

---

## 14. Shared Workplace Context Preserves Organizational Continuity

Products may consume organization-specific context such as:

- active organization;
- role;
- clients;
- business rules;
- pricing preferences;
- private Knowledge;
- partner relationships;
- data boundaries;
- Product access.

This context belongs to Workplace.

A Product receives a purpose-bound representation.

It should not create its own permanent competing organization model.

---

## 15. Shared Execution Foundations Preserve Governed Work

Products may initiate or display:

- Workflow;
- Task;
- Review;
- approval;
- failure;
- retry;
- protected action.

The shared Execution foundation preserves common meaning for how governed work proceeds.

A Product may have Product-specific journey state.

It must not duplicate the authoritative execution lifecycle.

---

## 16. Shared Knowledge Foundations Preserve Governed Understanding

Products may consume:

- shared Knowledge;
- organization-private Knowledge;
- source references;
- validated rules;
- controlled templates;
- terminology;
- historical versions.

Knowledge remains governed by source, scope, version, validation, and access.

A Product should not copy Knowledge into a private Product database and treat it as permanently current.

---

## 17. Shared Intelligence Foundations Preserve Candidate Meaning

Products may consume common intelligence responsibilities such as:

- scoring;
- matching;
- ranking;
- recommendation;
- explanation.

The Products may compose those responsibilities differently.

Shared intelligence does not imply one universal ranking formula.

It preserves distinctions such as:

```text
candidate ≠ formal object

recommendation ≠ decision

score ≠ formal Priority
```

---

## 18. Shared Capability Foundations Preserve Reusable Function

Products may consume common Capabilities.

Examples include:

- Knowledge retrieval;
- classification recommendation;
- document comparison;
- Artifact rendering;
- provider matching;
- deadline extraction;
- Communication drafting.

The Capability meaning should remain stable.

Products may select different Skills or implementations.

---

## 19. Shared Agent Governance Preserves Runtime Accountability

Products may expose different Assistant personas and Guide experiences.

The underlying AI Agents must still follow shared rules for:

- registration;
- identity;
- Agent Contract;
- Capability;
- Skill;
- data access;
- Permission;
- Policy;
- output classification;
- Human Review;
- audit.

A Product must not create hidden unregistered Agents for convenience.

---

## 20. Shared Artifact Foundations Preserve Outcome Continuity

Products may create:

- Content;
- drafts;
- reports;
- filing packages;
- videos;
- images;
- client proposals;
- professional outputs.

Artifact architecture should preserve common distinctions among:

- Content;
- Artifact;
- Document;
- Render;
- Edit;
- Delivery;
- Publish;
- formalization.

Part V develops these foundations.

CH21 establishes that Products should not invent incompatible Artifact meaning.

---

## 21. Shared Network Foundations Preserve Cross-Orbit Boundaries

Products that participate in MGSN may consume shared contracts for:

- organization network identity;
- Capability need;
- provider evidence;
- Routing context;
- collaboration preparation;
- outcome feedback;
- trust evidence.

A Product must not turn network discovery into automatic provider appointment.

Shared network contracts preserve the independence of participating Workplaces.

---

## 22. Shared Observability Foundations Preserve Trace

Products may generate or display:

- Events;
- audit references;
- correlation;
- failures;
- external outcomes;
- Product analytics.

Operational telemetry and professional audit are not identical.

The shared foundation should preserve formal trace where responsibility and protected action require it.

A Product analytics event must not masquerade as a Core Event.

---

## 23. Shared Foundations Do Not Require One Runtime

Different Products may consume a foundation through different technical routes.

For example, Knowledge may be:

- retrieved through a shared service;
- resolved locally from an authorized cache;
- accessed through Local Vault;
- supplied through a Product-specific adapter.

The runtime form may vary.

The semantic and governance meaning must remain consistent.

---

## 24. Shared Foundations Do Not Require One Database

A shared concept may appear in several stores as:

- authoritative record;
- cache;
- projection;
- local replica;
- search index;
- historical snapshot.

The Owning Service remains authoritative.

Database centralization is not required for semantic sharing.

Database duplication does not create authority duplication.

---

## 25. Shared Foundations Do Not Require One Frontend

Lite, MarkReg, MGSN, and Workplace may use different frontends.

They may also share components where useful.

A shared design system can improve coherence.

It is not the source of semantic authority.

The constitutional boundary must survive even when the interfaces look very different.

---

## 26. Shared Foundations Do Not Require One Repository

Repository topology is an implementation decision.

Possible forms include:

- one monorepo;
- several Product repositories;
- shared package repositories;
- separate specification and implementation repositories;
- local/private components.

The architecture does not require one form.

Repository boundaries must not be mistaken for domain or authority boundaries.

---

## 27. Shared Foundations Do Not Require One Team

A shared foundation may have:

- a dedicated owner;
- federated maintainers;
- specification governance;
- several implementation teams.

A Product team may contribute to a shared foundation.

It should not unilaterally redefine it for all consumers.

Ownership and change governance must remain explicit.

---

## 28. Dependency Direction Must Be Controlled

The intended dependency direction is:

```text
Products
→ consume Workplace context and shared foundations

Workplace
→ coordinates Product access and organization context

Shared foundations
→ do not depend on one Product’s private UX assumptions
```

A shared foundation should not require Lite-specific or MarkReg-specific screen logic.

If it does, Product concerns may have leaked downward.

---

## 29. Product-Specific Extensions Must Be Namespaced

A Product may need fields or behavior not shared by other Products.

These extensions should remain identifiable as Product-specific.

Examples include:

- Lite Today display preferences;
- MarkReg intake-progress metadata;
- MGSN comparison-view state.

An extension must not silently redefine the shared object.

Where repeated need proves broader meaning, the concept may later be promoted through governance.

---

## 30. Product Extensions Must Not Become Hidden Canon

A Product-specific field may become widely used.

Usage alone does not make it canonical.

Promotion should require:

- repeated cross-Product need;
- stable meaning;
- ownership clarity;
- compatibility;
- migration plan;
- governance approval.

This is Candidate Before Canonical applied to architecture.

---

## 31. Temporary Duplication May Be Acceptable

Early Product loops may implement similar logic separately.

This can be acceptable when:

- the user problem is not yet stable;
- meanings may diverge;
- extraction would slow learning;
- there is no proven shared consumer.

Temporary duplication should still preserve shared semantics and authority boundaries.

The risk is not all duplication.

The risk is ungoverned permanent divergence.

---

## 32. Semantic Forks Are Not Acceptable

A semantic fork occurs when Products define incompatible meanings for the same shared concept.

Examples:

- Lite treats a recommendation as a Task;
- MarkReg treats review as approval;
- MGSN treats provider ranking as Routing selection;
- one Product treats Communication draft as sent.

These are not harmless implementation differences.

They break interoperability and accountability.

Semantic forks require repair, not accommodation.

---

## 33. Local Copies Must Preserve Authority Metadata

A Product may keep local copies for:

- performance;
- offline work;
- search;
- Product presentation.

The copy should preserve:

- source;
- version;
- authority;
- synchronization time;
- staleness;
- mutation route.

A local copy must not become authoritative formal business state unless the local component is itself the authorized Owning Service.

---

## 34. Product Caches Must Fail Safely

A cache may be stale or unavailable.

The Product should distinguish:

- current authoritative value;
- cached value;
- historical snapshot;
- unknown freshness;
- unavailable source.

A Product must not perform protected action using stale cached authority without revalidation.

---

## 35. Shared Dependency Failure Must Not Produce False Success

A shared foundation may be unavailable.

Examples include:

- Knowledge service unavailable;
- Permission evaluation unavailable;
- Execution intake unavailable;
- Agent Registry unavailable;
- Owning Service timeout.

The Product may:

- degrade to read-only;
- use safe cached context;
- allow local drafting;
- queue a preparation request;
- show unavailable state.

It must not:

- assume Permission;
- invent Knowledge;
- claim execution;
- bypass review;
- record formal success.

---

## 36. Product Degradation Modes Must Be Explicit

A Product may support modes such as:

```text
Full Connected Mode

Connected Read-Only Mode

Local Preparation Mode

Cached Historical View

Unavailable for Protected Action
```

The mode should be visible where it affects professional use.

Graceful degradation is valuable.

Silent governance degradation is not.

---

## 37. Shared Foundation Changes Require Compatibility Discipline

A shared foundation may change:

- semantic version;
- field;
- status;
- contract;
- Policy behavior;
- validation;
- Event.

Changes should consider:

- current Products;
- historical records;
- local deployments;
- adapters;
- migration;
- deprecation;
- rollback.

The architecture does not define a versioning protocol.

It requires disciplined compatibility.

---

## 38. Independent Products May Adopt Changes at Different Times

Products may not upgrade simultaneously.

Shared changes may need:

- compatibility window;
- adapters;
- version negotiation;
- dual-read;
- migration support;
- deprecation notice.

Independent adoption should not permit indefinite semantic divergence.

There must be a governed path toward convergence.

---

## 39. Backward Compatibility Is Not Unlimited

Preserving every historical behavior forever may block improvement.

A breaking change may be justified when:

- prior meaning was unsafe;
- authority drift must be repaired;
- security requires change;
- old behavior prevents conformance.

The change should still preserve:

- migration;
- historical interpretation;
- clear deprecation;
- Product impact review.

---

## 40. Product Adapters May Protect Independence

A Product adapter may translate between:

- Product-specific interaction;
- shared references;
- shared contracts;
- local implementations;
- external systems.

Adapters can reduce coupling.

They must not conceal semantic mismatch.

An adapter may transform representation.

It may not redefine authority.

---

## 41. Anti-Corruption Boundaries Protect Shared Meaning

When a Product integrates with an external system or legacy application, it may need an anti-corruption boundary.

This boundary prevents external concepts from silently redefining MarkOrbit concepts.

Example:

```text
External "case"
→ may map to Matter, Task, Order,
or several references depending on meaning
```

A direct field-name match is not enough.

Meaning must be evaluated.

---

## 42. Product Configuration Must Not Change Constitutional Rules

Products may allow configuration for:

- labels;
- defaults;
- views;
- preferred Skills;
- review routing;
- local processing;
- notifications.

Configuration must not permit:

- redefining shared statuses;
- disabling mandatory Human Review;
- granting Permission;
- bypassing Owning Services;
- treating candidates as canonical.

Configuration changes experience and eligible behavior.

It does not rewrite architecture.

---

## 43. Shared Capability Use May Be Optional

A shared Capability may exist without being mandatory for every Product.

A Product may:

- use another eligible Skill;
- use a local implementation;
- defer the feature;
- use a human process;
- remain read-only.

Optional consumption supports Product independence.

Where a constitutional function is required, the Product must still preserve its meaning even if implemented differently.

---

## 44. Shared Foundation Ownership Must Be Explicit

Each shared foundation needs an identifiable governance owner for:

- meaning;
- version;
- change review;
- conformance;
- deprecation;
- dispute resolution.

This owner may be:

- Core governance;
- Execution governance;
- Workplace architecture;
- Capability governance;
- Artifact governance;
- network governance.

Technical maintainers may differ from architectural owners.

---

## 45. Product Teams Must Participate in Foundation Feedback

Shared foundations improve through real Product use.

Product teams should contribute:

- unmet needs;
- friction;
- edge cases;
- failure evidence;
- extension candidates;
- migration impact;
- outcome feedback.

They should not bypass governance by implementing private semantic changes.

The correct path is:

```text
Product evidence
→ foundation change candidate
→ governance
→ accepted, experimental, or rejected change
```

---

## 46. Conformance Must Be Testable at Product Boundaries

A Product should be testable for:

- shared reference use;
- status meaning;
- candidate handling;
- Permission and Policy enforcement;
- AI disclosure;
- Prepared Action handoff;
- formal success reporting;
- failure behavior;
- cross-Product context;
- historical trace.

Conformance is not proven by architecture diagrams alone.

It must appear in Product behavior.

---

## 47. The Minimum Independence and Foundation Model

```text
Independent Product
  │
  ├── Product owner
  ├── primary user and problem
  ├── Product loop
  ├── Product UX
  ├── Product-specific state
  ├── roadmap
  ├── release
  ├── deployment
  └── implementation
        │
        ▼
Product Boundary Contracts
  │
  ├── shared references
  ├── authorized Workplace context
  ├── semantic versions
  ├── Permission and Policy
  ├── Knowledge and Capability access
  ├── Agent governance
  ├── Execution handoff
  ├── Artifact rules
  ├── Event and audit trace
  └── network contracts
        │
        ▼
Shared Foundations
  │
  ├── Core semantics
  ├── organization context
  ├── governed Execution
  ├── Knowledge and Intelligence
  ├── Capability and Skill governance
  ├── Agent governance
  ├── Artifact architecture
  └── MGSN participation rules
        │
        ▼
Owning Service and Formal Results
        │
        ▼
Product Outcome and Workplace Visibility
```

The Product is independent in ownership and experience.

It is conformant in meaning and authority.

---

## 48. Required Distinctions

```text
Product independence ≠ Product sovereignty
```

Products remain subject to shared constitutional rules.

```text
Shared foundation ≠ shared monolith
```

Logical reuse does not require one implementation.

```text
Shared meaning ≠ shared code
```

Products may implement contracts differently.

```text
Independent release ≠ semantic drift
```

Release timing may differ; meaning may not.

```text
Product extension ≠ Core redefinition
```

Extensions remain namespaced until governed promotion.

```text
Temporary duplication ≠ permanent fork
```

Early repetition may support learning.

```text
Local copy ≠ local authority
```

Authority follows the Owning Service.

```text
Cache availability ≠ current truth
```

Staleness remains explicit.

```text
Shared Capability ≠ mandatory shared Skill
```

Products may choose eligible implementations.

```text
Adapter ≠ semantic bypass
```

Representation translation must preserve authority.

```text
Configuration ≠ constitutional change
```

Product settings cannot weaken governance.

```text
Repository boundary ≠ architecture boundary
```

Technical layout does not define ownership automatically.

```text
Product replacement ≠ organization replacement
```

The Orbit remains continuous.

---

## 49. Failure Modes This Chapter Prevents

### Shared monolith

Every Product depends on one codebase, release, frontend, database, and central team.

### Product sovereignty

A Product treats shared contracts as optional suggestions.

### Semantic fork

Products create incompatible Task, Review, Communication, or Routing meanings.

### Organization duplication

Each Product maintains its own client, identity, role, and preference model.

### Shared-service absolutism

Every repeated function is prematurely centralized.

### Hidden Product extension

Product-specific fields become de facto canonical without governance.

### Permanent copy drift

A Product copies Knowledge or formal objects and stops tracking source versions.

### Cache authority

Stale Product state becomes the basis for protected action.

### Silent degradation

Permission, Policy, Knowledge, or Execution failures are hidden behind fallback behavior.

### Release coupling

One Product cannot improve without releasing every Product.

### Compatibility neglect

Shared changes break embedded, local, or slower-moving Products without migration.

### Adapter laundering

An adapter hides a real semantic mismatch.

### Configuration bypass

A Product setting disables mandatory governance.

### Optional-foundation confusion

A Product avoids one implementation and accidentally avoids the constitutional responsibility itself.

### Repository-driven architecture

Code location is treated as proof of domain ownership.

These designs may produce either speed or reuse.

They do not preserve both Product value and architectural coherence.

---

## 50. Minimum Conformance Rule

A conforming Product and foundation architecture must preserve the following lock:

```text
Products remain independently owned,
roadmapped, designed, released,
deployed, and replaceable.

Independent Products remain accountable
for focused user value.

Products consume shared foundations
through explicit contracts.

Shared foundations preserve stable semantics,
governance, organization context,
Execution boundaries, Knowledge,
Capabilities, Agent rules,
Artifact rules, and network participation.

Shared foundations are logical responsibilities,
not mandatory implementation topology.

One shared foundation does not require
one repository, database, frontend,
runtime, team, or release schedule.

Products may extend shared concepts
without redefining them.

Extensions remain namespaced
until governed promotion.

Temporary implementation duplication
may support Product learning.

Semantic forks are prohibited.

Local copies, caches, projections,
and adapters preserve source,
version, authority, and staleness.

Shared dependency failure
must not produce false authority or success.

Products may degrade safely,
but not silently weaken governance.

Shared changes support compatibility,
migration, and historical interpretation.

Products may adopt compatible changes
at different times under governed convergence.

Product configuration does not change
constitutional authority.

Shared Capability use does not require
one mandatory Skill.

Foundation ownership and change governance
remain explicit.

Product behavior must demonstrate conformance.

The Product may change.

The Organization Orbit remains.
```

A technically independent Product that violates shared meaning does not conform.

A highly reused platform that prevents Product independence also does not conform.

---

## 51. Chapter Boundary

This chapter defines:

- Product independence;
- Product ownership;
- roadmap independence;
- experience independence;
- implementation independence;
- release independence;
- deployment independence;
- replaceability;
- logical shared foundations;
- semantic foundations;
- identity;
- Permission and Policy;
- Workplace context;
- Execution;
- Knowledge;
- Intelligence;
- Capability;
- Agent governance;
- Artifact foundations;
- network foundations;
- observability;
- dependency direction;
- Product extensions;
- temporary duplication;
- semantic forks;
- local copies;
- caches;
- degradation;
- compatibility;
- adoption timing;
- adapters;
- anti-corruption boundaries;
- Product configuration;
- optional Capability consumption;
- foundation ownership;
- Product feedback;
- Product conformance.

It does not define:

- Product embedding placement;
- cross-Product context assembly;
- Lite architecture profile;
- MarkReg architecture profile;
- MGSN Gateway profile;
- Workplace editions;
- cross-Product lifecycle continuity;
- final service topology;
- repository topology;
- API schemas;
- version-negotiation protocol;
- Product deployment architecture;
- production implementation.

Those subjects belong to CH22–CH27, dedicated Product publications, technical specifications, ADRs, and implementation repositories.

This chapter does not modify Book 02 Core semantics.

It does not modify Book 03 Execution authority.

It does not require one shared implementation or authorize Product-level mutation of protected business state.

---

## 52. Chapter Conclusion

Product independence and shared foundations are not competing goals.

They solve different problems.

Product independence protects:

- user focus;
- Product learning;
- release speed;
- implementation choice;
- replaceability;
- Product accountability.

Shared foundations protect:

- common meaning;
- organization continuity;
- governance;
- cross-Product interoperability;
- professional accountability;
- formal-state authority;
- ecosystem learning.

The correct architecture is neither:

```text
one Product that owns everything
```

nor:

```text
many Products that agree on nothing
```

It is:

```text
Independent Products
        ↓
explicit boundary contracts
        ↓
stable shared foundations
        ↓
governed handoffs and formal authority
        ↓
coherent organizational outcomes
```

The constitutional outcome is:

```text
Products own their journeys.

Workplace preserves and provides authorized organizational context.

Core defines shared meaning.

Execution governs coordinated work.

Owning Services change and record formal business facts.

Humans remain professionally accountable for professional judgment.

Shared foundations connect the system
without turning it into a monolith.
```

CH22 now moves from independence to placement:

> When an independent Product appears inside or alongside Workplace, which context may it receive, which surfaces may host it, and how can embedded experiences preserve Product identity, data minimization, authority boundaries, and cross-Product continuity?
