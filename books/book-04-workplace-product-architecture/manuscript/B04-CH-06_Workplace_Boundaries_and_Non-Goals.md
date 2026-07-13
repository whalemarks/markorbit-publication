# B04-CH-06 — Workplace Boundaries and Non-Goals

**Status:** Draft 1  
**Chapter Map:** B04-TOC-V0.1  
**Writing Pack:** B04-PACK-01 — Front Matter and Part I

## Chapter Purpose

This chapter closes Part I by defining what **Workplace** owns, what it consumes, what it coordinates with, and what it must never absorb.

The previous chapters established:

- why Workplace exists;
- why each Workplace is an independent organizational Orbit;
- where Workplace sits between Core, Execution, Products, and Network;
- which principles every Workplace must preserve.

This chapter turns those ideas into explicit boundaries.

The core rule is:

```text
Workplace provides authorized organizational context.

It does not become the owner of every shared concept,
every Workflow,
every Product,
every network relationship,
or every formal business fact.
```

Workplace is broad because organizations are broad.

But broad scope does not justify unlimited authority.

A professional organization needs one coherent operating environment for:

- identity;
- people;
- roles;
- clients;
- relationships;
- private knowledge;
- business rules;
- pricing;
- preferences;
- Product access;
- work visibility;
- review visibility;
- partner relationships;
- organizational memory.

That does not mean Workplace should redefine:

- Core semantics;
- Task lifecycle;
- Workflow governance;
- Event ownership;
- Product behavior;
- MGSN routing authority;
- AI Agent runtime;
- Local Vault implementation;
- formal mutation ownership.

The central proposition of this chapter is:

```text
Workplace owns organizational context.

Workplace consumes shared semantics and capabilities.

Workplace exposes governed work.

Workplace hosts or connects Products.

Workplace participates in networks.

Workplace does not replace the authorities around it.
```

---

## 1. Why Boundaries Matter

A system rarely becomes over-centralized through one explicit decision.

It usually happens through convenience.

A team says:

- “The Workplace already has the user, so let it define permissions.”
- “The Workplace already shows Tasks, so let it own Task states.”
- “The Workplace already stores client files, so let it become the universal data layer.”
- “The Workplace already presents AI recommendations, so let it approve them.”
- “The Workplace already connects providers, so let it appoint them.”
- “The Workplace already contains multiple Products, so let it become one mega-Product.”

Each step appears practical.

Together, they destroy the architectural separation that makes MarkOrbit scalable and governable.

Boundaries exist to prevent:

- authority drift;
- semantic duplication;
- Product coupling;
- hidden centralization;
- AI overreach;
- private-data leakage;
- Workflow fragmentation;
- formal-state ambiguity;
- network marketplace drift.

A boundary is not a refusal to integrate.

It is a rule about **how integration occurs without ownership collapse**.

---

## 2. Workplace and Core

### Relationship

Workplace consumes Core semantics.

Core provides the stable shared professional model.

Workplace provides the organization-specific context in which that model is used.

The relationship is:

```text
Core
→ shared meaning and formal contracts

Workplace
→ authorized organizational context
```

### Workplace may consume

Workplace may consume:

- Core Objects;
- Core Services;
- canonical status values;
- permission and policy definitions;
- Human Review boundaries;
- Event and audit rules;
- Workflow Contract structures;
- common validation rules;
- shared identity concepts.

### Workplace may contribute context

Workplace may supply:

- organization identity;
- user identity;
- role context;
- client context;
- organization rules;
- pricing;
- preferences;
- reviewer assignment;
- private knowledge references;
- Product access;
- partner relationships.

### Workplace must not own

Workplace must not:

- create competing definitions of Core Objects;
- redefine canonical statuses;
- redefine Service ownership;
- create alternate Task semantics;
- create alternate Event semantics;
- change formal mutation authority;
- promote organization rules into universal Core rules without change control;
- silently modify Book 02 semantics.

### Boundary test

Ask:

```text
Is this concept intended to mean the same thing
across Products and organizations?
```

If yes, it may belong in Core or require a Core-level change process.

Ask:

```text
Is this rule specific to one organization,
one client,
one Product,
or one operating preference?
```

If yes, it likely belongs in Workplace context or Product behavior, not Core.

### Non-goal

Workplace is not a second Core.

---

## 3. Workplace and Execution

### Relationship

Workplace supplies context.

Execution governs coordinated work.

The relationship is:

```text
Workplace
→ who is operating, under which context and authority

Execution
→ how work proceeds, pauses, reviews, fails, and completes
```

### Workplace may expose

Workplace may expose:

- Tasks;
- Workflow status;
- review requests;
- warnings;
- recommendations;
- prepared actions;
- approval requests;
- execution history;
- failure notices;
- audit summaries.

### Workplace may initiate

Workplace may initiate or hand off:

- user-confirmed intent;
- prepared requests;
- Product-originated actions;
- review requests;
- Workflow entry;
- provider-routing preparation;
- Artifact preparation.

### Execution must continue to own

Execution must continue to own:

- Workflow progression;
- Task lifecycle;
- Human Review gates;
- approval sequencing;
- communication boundaries;
- protected-action controls;
- retry;
- safe failure;
- idempotency;
- execution trace;
- replay;
- escalation.

### Workplace must not

Workplace must not:

- invent its own Task statuses;
- bypass Human Review;
- directly perform protected action;
- treat UI completion as execution completion;
- treat user confirmation as formal mutation;
- allow a Product surface to replace Execution governance;
- redefine communication send rules;
- redefine Event ownership.

### Boundary test

Ask:

```text
Is this about organizational visibility and context?
```

That belongs in Workplace.

Ask:

```text
Is this about governed progression and operational state?
```

That belongs in Execution.

### Non-goal

Workplace is not a Workflow engine.

---

## 4. Workplace and Products

### Relationship

Workplace is the organizational environment.

Products provide focused user experiences and domain journeys.

The relationship is:

```text
Workplace preserves the organization.

Product serves the journey.
```

### Products may use Workplace context

Products may consume:

- organization identity;
- users and roles;
- client context;
- private knowledge;
- pricing;
- preferences;
- service catalog;
- partner history;
- review rules;
- Product entitlements.

### Workplace may host or connect

Workplace may host or connect:

- Lite;
- MarkReg;
- MGSN interfaces;
- organization-specific applications;
- future Products.

### Products remain independent

Products may differ in:

- navigation;
- interaction model;
- Product loop;
- domain scope;
- release cycle;
- data presentation;
- Artifact types;
- recommendation model;
- embedded or standalone operation.

### Workplace must not become

Workplace must not become:

- a universal feature catalog;
- one mandatory monolithic interface;
- a substitute for Product design;
- a Product backlog for every domain;
- a reason to merge all Product repositories;
- a mega-application that must ship before Product loops are validated.

### Products must not become

Products must not become:

- owners of organization identity;
- owners of client relationships;
- owners of shared Task semantics;
- owners of private organizational truth;
- owners of cross-Product authority;
- substitutes for Workplace.

### Boundary test

Ask:

```text
Does this responsibility preserve organizational continuity
across multiple Products?
```

That belongs in Workplace.

Ask:

```text
Does this responsibility shape a specific user journey?
```

That belongs in a Product.

### Non-goal

Workplace is not the only Product.

---

## 5. Workplace and MGSN

### Relationship

Workplace is the network node.

MGSN connects nodes.

The relationship is:

```text
Organization / Workplace / Orbit
→ participates in MGSN
```

### Workplace may provide to MGSN

Under authorization, Workplace may provide:

- organization identity;
- public or shared capability profile;
- jurisdiction coverage;
- selected provider evidence;
- availability;
- network preferences;
- partner relationships;
- outcome feedback;
- trust evidence.

### MGSN may provide to Workplace

MGSN may provide:

- provider candidates;
- capability discovery;
- trust-supported recommendations;
- jurisdiction coverage;
- routing explanations;
- collaboration options;
- network evidence;
- partner expansion paths.

### Workplace retains authority over

Workplace retains authority over:

- whether to participate;
- which profile data is shared;
- which providers are visible;
- whether a candidate is accepted;
- which partner is selected;
- which relationship remains private;
- which outcome evidence is contributed;
- whether public discovery is used.

### MGSN must not become

MGSN must not become:

- the owner of the client;
- an open bidding marketplace by default;
- a forced-allocation engine;
- an automatic provider-appointment authority;
- the universal owner of trust;
- the owner of organizational pricing;
- the owner of private partner relationships.

### Boundary test

Ask:

```text
Is this about the organization’s own relationship,
selection, or network policy?
```

That belongs in Workplace.

Ask:

```text
Is this about cross-organization discovery,
routing, and collaboration support?
```

That belongs in MGSN.

### Non-goal

Workplace is not the network itself.

---

## 6. Workplace and Local Vault

### Relationship

Local Vault is a logical local/private data boundary.

Workplace is the organizational environment that may use it.

The relationship is:

```text
Workplace
→ defines authorized organizational use

Local Vault
→ provides local/private storage and control boundary
```

### Workplace may decide

Workplace may govern:

- which data should remain local;
- which Product may access local data;
- which user may unlock private context;
- which records may synchronize;
- which AI capability may use local context;
- which retention rule applies;
- which audit record is required.

### Local Vault may provide

Local Vault may provide:

- local storage;
- private indexing;
- controlled retrieval;
- local encryption;
- local model context;
- selective synchronization;
- offline continuity;
- local audit support.

### Workplace must not define implementation

Workplace must not define:

- exact storage engine;
- encryption algorithm;
- synchronization protocol;
- file-system layout;
- local database schema;
- backup implementation;
- device-management implementation;
- network transport.

Those belong to a future Local Vault architecture specification and implementation decisions.

### Boundary test

Ask:

```text
Is this about why the organization needs local/private control?
```

That belongs in Workplace architecture.

Ask:

```text
Is this about how local/private storage technically works?
```

That belongs in Local Vault specifications.

### Non-goal

Workplace is not a storage engine.

---

## 7. Workplace and AI Agent Runtime

### Relationship

Workplace supplies authorized context.

AI Agent Runtime governs Agent identity, permissions, role, tools, and execution limits.

The relationship is:

```text
Workplace
→ provides organization, user, client, Product, and purpose context

AI Agent Runtime
→ governs how an Agent operates within that context
```

### Workplace may provide

Workplace may provide:

- active organization;
- active user;
- user role;
- client context;
- private knowledge;
- Product context;
- purpose;
- approved tools;
- policy references;
- review requirements.

### AI Agent Runtime must govern

AI Agent Runtime must govern:

- Agent identity;
- Agent Profile;
- permission;
- capability;
- tool access;
- context scope;
- execution time;
- output type;
- audit;
- termination;
- handoff;
- prohibited actions.

### Workplace must not assume

Workplace must not assume:

- that any AI Agent may use all organizational context;
- that Product access equals Agent permission;
- that model capability equals professional authority;
- that an AI draft is approved;
- that an Agent may mutate formal state;
- that an Agent may send, file, pay, appoint, or instruct.

### Boundary test

Ask:

```text
Which organization context may the Agent use?
```

That belongs in Workplace.

Ask:

```text
How is the Agent governed as a runtime role?
```

That belongs in Agent governance and runtime specifications.

### Non-goal

Workplace is not an Agent framework.

---

## 8. Workplace and Shared Knowledge

### Relationship

Workplace holds private knowledge and organizational memory.

The shared Brain provides governed shared knowledge and context.

The relationship is:

```text
Private organization knowledge
+
shared validated knowledge
→ authorized context assembly
```

### Workplace may own

Workplace may own:

- private templates;
- client instructions;
- internal practice notes;
- provider evaluations;
- pricing knowledge;
- local procedures;
- internal risk interpretations;
- organization-specific lessons;
- unpublished strategies.

### Shared knowledge may provide

Shared knowledge may provide:

- validated jurisdiction information;
- approved professional rules;
- shared terminology;
- common guidance;
- cross-organization knowledge;
- reference materials;
- reusable patterns.

### Workplace must preserve the distinction

Workplace must preserve:

```text
private knowledge
≠
shared knowledge

knowledge candidate
≠
canonical knowledge

organization preference
≠
universal rule
```

### Workplace must not

Workplace must not:

- promote private knowledge into shared knowledge automatically;
- treat Distillery output as approved;
- lose source and provenance;
- merge client-specific instructions into general guidance;
- allow one Product to own organization memory;
- hide which knowledge was used.

### Boundary test

Ask:

```text
Is this knowledge specific to the organization or client?
```

That belongs in Workplace-private context.

Ask:

```text
Is this knowledge intended to be shared and governed broadly?
```

That belongs in the Brain or shared knowledge governance.

### Non-goal

Workplace is not the universal knowledge authority.

---

## 9. Workplace and Shared Capabilities

### Relationship

Workplace consumes capabilities.

It does not define every capability.

The relationship is:

```text
Capability Catalog
→ defines what can be done

Skill Registry
→ defines governed implementations

Workplace
→ selects and authorizes use in organization context
```

### Workplace may decide

Workplace may decide:

- which capability is enabled;
- which Skill is preferred;
- which users may invoke it;
- which clients permit its use;
- which review level applies;
- which context may be supplied;
- which result remains a candidate;
- which Product may expose it.

### Workplace must not

Workplace must not:

- redefine Capability globally;
- create ungoverned Skill semantics;
- treat enabled Skill as permission for every user;
- treat capability availability as authority;
- convert capability evidence into a final rating automatically;
- create Product-specific duplicates of shared Capability definitions without justification.

### Boundary test

Ask:

```text
What can the system do?
```

That belongs in Capability.

Ask:

```text
Which implementation performs it?
```

That belongs in Skill.

Ask:

```text
May this organization use it here and now?
```

That belongs in Workplace authorization.

### Non-goal

Workplace is not the Capability Catalog.

---

## 10. Workplace and Artifact

### Relationship

Workplace supplies organization context for Artifact creation, review, storage, and delivery.

Artifact is a cross-Product business outcome concept.

The relationship is:

```text
Content
→ Artifact
→ Human Review
→ Render
→ Optional Edit
→ Delivery or Publish
→ Outcome feedback
```

### Workplace may provide

Workplace may provide:

- organization brand;
- client context;
- approved templates;
- reviewer;
- delivery preference;
- private assets;
- access control;
- version visibility;
- retention rules.

### Artifact lifecycle must remain distinct

Workplace must preserve:

```text
Content ≠ Artifact
Artifact ≠ Document
Render ≠ Edit
Delivery ≠ Publish
Draft ≠ approved output
```

### Workplace must not

Workplace must not:

- treat every file as an approved Artifact;
- treat rendering as approval;
- treat delivery as publication;
- treat Product-generated content as final;
- hide Artifact provenance;
- overwrite prior versions;
- allow AI-generated Artifact output to bypass Human Review.

### Boundary test

Ask:

```text
Which organization context, asset, reviewer, and delivery rule apply?
```

That belongs in Workplace.

Ask:

```text
What is the Artifact lifecycle and cross-Product model?
```

That belongs in Artifact architecture.

### Non-goal

Workplace is not a generic file manager.

---

## 11. Workplace and Formal Business State

### Relationship

Workplace may display formal state.

It does not automatically own formal state.

Formal business facts remain under the proper Owning Service.

### Workplace may display

Workplace may display:

- Matters;
- Tasks;
- Orders;
- Communications;
- Documents;
- payments;
- provider engagements;
- filing status;
- official outcomes;
- Opportunities.

### Workplace may prepare

Workplace may prepare:

- user intent;
- draft changes;
- review requests;
- recommendations;
- candidate records;
- context packages;
- Product handoffs.

### Owning Services must mutate

Owning Services must mutate:

- formal status;
- official record;
- approved Communication send;
- payment state;
- provider instruction;
- formal Opportunity;
- official filing record;
- governed Task or Matter state.

### Boundary test

Ask:

```text
Is this merely visible or prepared in Workplace?
```

That does not imply ownership.

Ask:

```text
Which service is authoritative for the formal fact?
```

That identifies the Owning Service.

### Non-goal

Workplace is not the universal system of record.

---

## 12. Workplace and Organizational Memory

### Relationship

Workplace preserves the continuity of the organization.

Organizational memory spans:

- people;
- clients;
- matters;
- Products;
- outcomes;
- knowledge;
- reviews;
- partners;
- Artifacts;
- decisions.

### Workplace should preserve

Workplace should preserve:

- historical context;
- prior decisions;
- client preferences;
- trusted providers;
- quality lessons;
- review patterns;
- outcome history;
- Product continuity;
- AI-assisted work trace;
- changes in policy.

### Workplace must not confuse

Organizational memory must not be confused with:

- raw logs;
- one Product database;
- one person’s notes;
- unvalidated AI summaries;
- shared public knowledge;
- permanent retention of all data.

Memory requires:

- scope;
- provenance;
- authority;
- retention;
- privacy;
- versioning;
- review.

### Non-goal

Workplace is not an unlimited archive.

---

## 13. Workplace and a Centralized SaaS Tenant

### Relationship

A SaaS tenant may be an implementation mechanism.

Workplace is an architectural concept.

The relationship is:

```text
Tenant
→ possible technical partition

Workplace
→ organizational operating and authority boundary
```

### A tenant may provide

A tenant may provide:

- data partitioning;
- user isolation;
- configuration;
- billing boundary;
- access boundary.

### Workplace additionally requires

Workplace additionally requires:

- professional identity;
- client ownership;
- relationship continuity;
- private knowledge;
- rules;
- pricing;
- Product composition;
- partner trust;
- professional accountability;
- organizational memory;
- network participation.

### Workplace must not be reduced to tenancy

Reducing Workplace to tenancy would ignore:

- autonomy;
- professional responsibility;
- organizational capital;
- Product continuity;
- private knowledge;
- trust relationships.

### Non-goal

Workplace is not “multi-tenancy plus more settings.”

---

## 14. Workplace and the Organization Itself

Workplace represents the organization’s operating environment.

It is not the legal organization itself.

The organization may exist through:

- legal entities;
- departments;
- teams;
- brands;
- professional practices;
- business units;
- external collaborators.

Workplace is the digital and operational boundary through which these realities are represented and governed.

It must not claim that software representation replaces:

- legal identity;
- professional qualification;
- contractual authority;
- regulatory responsibility;
- employment authority;
- client engagement terms.

The organization remains the real professional and commercial actor.

Workplace is its operating environment.

---

## 15. What Workplace Owns

Workplace may own or govern the organization-level representation of:

- organization identity;
- organization profile;
- users;
- roles;
- Product access;
- client context;
- relationship context;
- private knowledge;
- business rules;
- pricing preferences;
- service catalog;
- partner preferences;
- AI context policy;
- work visibility;
- review visibility;
- network participation preferences;
- organizational memory;
- local/private data policy.

Ownership here means architectural responsibility for organization context.

It does not automatically mean one database, one service, or one repository.

---

## 16. What Workplace Consumes

Workplace consumes:

- Core semantics;
- Core contracts;
- governed Execution;
- shared knowledge;
- intelligence;
- Capability definitions;
- Skills;
- Agent Profiles;
- Workflow definitions;
- Artifact services;
- Render and Edit capabilities;
- Delivery and Publish capabilities;
- MGSN interfaces;
- Product-specific functions;
- Local Vault functions.

Consumption does not imply ownership.

---

## 17. What Workplace Coordinates With

Workplace coordinates with:

- Products;
- Execution;
- Owning Services;
- AI Agent Runtime;
- shared knowledge systems;
- capability systems;
- Artifact and Delivery systems;
- MGSN;
- Local Vault;
- external organizational systems;
- local operating tools.

Coordination should occur through explicit contracts, context, permission, and handoff.

---

## 18. What Workplace Must Never Absorb

Workplace must never absorb:

- all Core semantics;
- all Workflow logic;
- all Product behavior;
- all network authority;
- all shared knowledge;
- all Agent governance;
- all formal state;
- all data storage;
- all implementation architecture;
- all protected-action authority.

The architectural shell must remain a shell.

Its job is coherence, not total ownership.

---

## 19. Boundary Matrix

| Concept | Owned by Workplace? | Consumed by Workplace? | Authority owner | Book 04 treatment |
|---|---:|---:|---|---|
| Organization identity and context | Yes | Yes | Workplace / organization | Defined as core Workplace responsibility |
| Users and roles | Organization-level representation | Yes | Workplace with Core permission boundaries | Architectural treatment only |
| Clients and relationships | Organization context | Yes | Workplace / relevant Owning Services | Relationship boundary defined |
| Private knowledge | Yes, under organization control | Yes | Workplace / organization | Private-context boundary defined |
| Shared Core semantics | No | Yes | Core | Must not be redefined |
| Workflow progression | No | Visible and invoked | Execution | Must not be reimplemented in Workplace |
| Task lifecycle | No | Visible and contextualized | Execution / Owning Service | Must not drift by Product |
| Product UX | No | Hosted or connected | Product | Product-specific |
| Product identity | No | Yes | Product | Workplace must not absorb Product scope |
| Capability definition | No | Yes | Capability Catalog | Workplace authorizes use |
| Skill implementation | No | Yes | Skill Registry | Workplace may select or prefer |
| AI Agent runtime | No | Yes | Agent governance/runtime | Workplace supplies context only |
| Formal business state | No, unless Workplace is the designated Owning Service for a specific domain | Yes | Proper Owning Service | Mutation authority must remain explicit |
| Artifact model | No | Yes | Artifact architecture / relevant Owning Service | Cross-Product concept |
| Render/Edit | No | Yes | Shared capability or Product implementation | Not Workplace-owned by default |
| Delivery/Publish | No | Yes | Delivery/Publish authority | Must remain distinct |
| Local Vault implementation | No | Yes | Local Vault specification/implementation | Workplace defines policy, not mechanism |
| Network routing | No | Yes | MGSN | Workplace retains selection authority |
| Provider appointment | No | Prepared and confirmed | Human authority + Owning Service | No automatic appointment |
| Trust evidence | Partly organization-specific | Yes | Workplace and MGSN governance | Contextual, not universal |
| Professional judgment | No software ownership | Supported | Human Professional | Human accountability preserved |

---

## 20. Book 04 Boundaries

Book 04 itself also has boundaries.

It defines:

- Workplace as an independent Orbit;
- organization context;
- authorized consumption;
- Product Architecture principles;
- Product embedding;
- Artifact and Delivery relationships;
- network participation;
- conformance principles.

It does not define:

- Book 02 semantic changes;
- Book 03 execution semantics;
- Lite Product requirements;
- MarkReg Product requirements;
- MGSN implementation;
- APIs;
- schemas;
- code architecture;
- deployment;
- infrastructure;
- repository topology;
- production readiness.

Book 04 is architecture.

It is not a Product PRD.

It is not an implementation manual.

---

## 21. Explicit Non-Goals

Workplace is not:

```text
a replacement for Core
a replacement for Execution
a universal Product
a case-management system
a tenant account
a central marketplace
an AI Agent framework
a universal database
a file manager
a knowledge authority
a Workflow engine
an implementation repository
a deployment model
a production-readiness declaration
```

Workplace must not:

- redefine Core Objects or Services;
- redefine Task or Workflow semantics;
- redefine Event ownership;
- bypass Human Review;
- authorize autonomous AI professional action;
- authorize external Communication send;
- authorize filing;
- authorize submission;
- authorize payment;
- authorize provider instruction;
- authorize official recordal;
- treat candidates as approved;
- treat recommendations as formal Tasks or Opportunities;
- treat Artifact as identical to Document;
- treat MGSN as open bidding;
- treat the organization as a platform-owned account;
- require one universal Product experience;
- require cloud centralization;
- require destructive migration;
- treat visibility as ownership;
- treat invocation as definition;
- treat context as mutation authority.

---

## 22. Boundary Anti-Patterns

### 22.1 The Everything Workplace

Every new responsibility is added to Workplace because it is the most visible layer.

Result:

- centralization;
- coupling;
- authority drift.

### 22.2 The Product-Owned Organization

One Product becomes the owner of users, clients, preferences, and private knowledge.

Result:

- Product lock-in;
- fragmented identity;
- weak cross-Product continuity.

### 22.3 The Hidden Workflow UI

A Workplace screen implements state transitions without governed Execution.

Result:

- inconsistent Tasks;
- bypassed review;
- poor audit.

### 22.4 The Platform-Owned Client

Shared infrastructure becomes the apparent owner of the relationship.

Result:

- weakened autonomy;
- marketplace drift.

### 22.5 The Universal Knowledge Pool

Private and shared knowledge are merged.

Result:

- confidentiality risk;
- loss of organizational capital.

### 22.6 The Agent-as-Authority Pattern

AI Agent output mutates state or performs protected action.

Result:

- accountability failure;
- governance failure.

### 22.7 The Universal Database Assumption

Every Workplace concept is placed in one central database.

Result:

- weak locality;
- weak privacy;
- implementation lock-in.

### 22.8 The MGSN-Centered Architecture

The network becomes the center and Workplaces become listings.

Result:

- Orbit model collapse;
- provider commoditization.

---

## 23. Boundary Review Questions

A future architecture or Product proposal should answer:

### Core boundary

- Does this proposal create a new shared semantic?
- Does it silently modify a frozen Core concept?

### Execution boundary

- Does it define progression, review, approval, or protected action?
- Does it bypass governed Execution?

### Product boundary

- Is this responsibility Product-specific?
- Is Workplace absorbing a Product journey?

### Network boundary

- Does this proposal preserve human selection?
- Does MGSN remain a connector rather than owner?

### AI boundary

- Does AI remain under identity, permission, and context?
- Can AI output be mistaken for approval?

### Formal-state boundary

- Which Owning Service records the formal fact?
- Is UI or AI mutating state directly?

### Data boundary

- Which data is private, local, shared, or synchronized?
- Is sharing explicit and reversible?

### Knowledge boundary

- Is the output a candidate or approved knowledge?
- Is provenance preserved?

### Artifact boundary

- Is the result Content, Artifact, Document, Render, Delivery, or Publish?
- Are those concepts being collapsed?

### Implementation boundary

- Is this architecture decision being mistaken for a service, repository, schema, or deployment requirement?

A proposal that cannot answer these questions is not ready for implementation.

---

## 24. Minimum Boundary Lock

Every conforming Workplace must preserve this lock:

```text
Workplace owns organizational context.

Core owns shared meaning.

Execution owns governed coordination.

Products own user journeys.

MGSN owns cross-Workplace connection.

Owning Services own formal mutation.

Humans own professional accountability.

AI Agents assist under governance.

Local Vault owns local/private technical control.

Artifact architecture owns cross-Product outcome structure.
```

This lock may be implemented in different technical forms.

Its meaning must not change.

---

## 25. Non-Goals of This Chapter

This chapter does not define:

- implementation services;
- database schemas;
- APIs;
- message formats;
- identity federation;
- local synchronization protocols;
- Agent runtime code;
- Product screen designs;
- MGSN ranking algorithms;
- trust scoring;
- Artifact schemas;
- deployment architecture;
- repository structure;
- infrastructure;
- production operations.

It does not authorize:

- external Communication send;
- filing;
- payment;
- provider appointment;
- provider instruction;
- official recordal;
- autonomous AI action;
- unrestricted implementation.

Its purpose is to close Part I with a clear constitutional boundary around Workplace.

---

## 26. Chapter Conclusion

Workplace is intentionally broad.

It must hold the organizational context that makes professional operation coherent across Products, Execution, capabilities, knowledge, Artifacts, and networks.

But Workplace must not become total.

It must not absorb the meaning defined by Core.

It must not absorb the coordination governed by Execution.

It must not absorb Product journeys.

It must not absorb MGSN.

It must not absorb Agent governance.

It must not absorb Local Vault implementation.

It must not absorb formal mutation authority.

The final distinction is:

```text
Workplace is where the organization operates.

It is not where every system responsibility is owned.
```

A conforming Workplace preserves:

- organizational autonomy;
- authorized context;
- privacy;
- Human accountability;
- governed handoff;
- Product independence;
- network independence;
- formal mutation authority;
- clear technical and publication boundaries.

This is how MarkOrbit avoids two opposite failures:

```text
a fragmented collection of disconnected Products
and
a centralized platform that owns everything
```

Workplace sits between those extremes.

It creates one coherent organizational Orbit while preserving the authority, independence, and responsibility of every surrounding layer.
