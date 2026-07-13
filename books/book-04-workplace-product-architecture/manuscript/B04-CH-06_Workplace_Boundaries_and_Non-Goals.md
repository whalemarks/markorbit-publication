# B04-CH-06 — Workplace Boundaries and Non-Goals

**Status:** Draft 2 — Pack 01 Editorial Repair  
**Chapter Map:** B04-TOC-V0.1  
**Writing Pack:** B04-PACK-01 — Front Matter and Part I

## Chapter Purpose

This chapter closes Part I by defining what **Workplace** is responsible for, what it consumes, what it coordinates with, and what it must never absorb.

The earlier chapters established:

- why Workplace exists;
- why each Workplace is an independent organizational Orbit;
- how Workplace is positioned between Core, Execution, Products, MGSN, Owning Services, human professionals, and AI Agents;
- which principles every Workplace must preserve.

This chapter converts those ideas into explicit boundaries.

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

A professional organization needs one coherent operating environment for identity, people, roles, clients, private knowledge, business rules, pricing, preferences, Product access, review visibility, partner relationships, and organizational memory.

But broad scope does not justify unlimited authority.

The central proposition is:

```text
Workplace is responsible for organizational context.

Workplace consumes shared semantics and capabilities.

Workplace exposes governed work.

Workplace hosts or connects Products.

Workplace participates in networks.

Workplace does not replace the authorities around it.
```

---

## 1. Boundaries Prevent Responsibility Drift

A system rarely becomes over-centralized through one explicit decision.

It usually happens through convenience.

A team may say:

- the Workplace already has the user, so let it define permissions;
- the Workplace already displays Tasks, so let it own Task states;
- the Workplace already stores client files, so let it become the universal data layer;
- the Workplace already presents AI recommendations, so let it approve them;
- the Workplace already connects providers, so let it appoint them;
- the Workplace already hosts several Products, so let it become one mega-Product.

Each step appears practical.

Together, they destroy the architectural separation that makes MarkOrbit governable and extensible.

Boundaries prevent:

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

It defines how integration occurs without collapsing responsibility or ownership.

Three tests should remain visible throughout this chapter:

```text
Visibility does not equal ownership.

Invocation does not equal definition.

Context does not equal mutation authority.
```

---

## 2. Workplace and Core

Core provides the stable shared professional model.

Workplace provides the organization-specific context in which that model is used.

The relationship is:

```text
Core
→ shared meaning and formal contracts

Workplace
→ authorized organizational context
```

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

Workplace may contribute:

- organization identity;
- user and role context;
- client context;
- organization-specific rules;
- pricing;
- preferences;
- reviewer assignment;
- private knowledge references;
- Product access;
- partner relationships.

But Workplace must not:

- create competing definitions of Core Objects;
- redefine canonical statuses;
- redefine Service authority;
- create alternate Task or Event semantics;
- change formal mutation authority;
- promote one organization’s preference into a universal Core rule without governed change control;
- silently modify the frozen Book 02 baseline.

The boundary test is straightforward:

```text
If a concept must mean the same thing
across Products and organizations,
it belongs in Core or requires Core-level governance.

If a rule is specific to one organization,
client, Product, or operating preference,
it belongs in organizational or Product context.
```

Workplace is not a second Core.

---

## 3. Workplace and Execution

Workplace supplies authorized context.

Execution governs coordinated work.

The relationship is:

```text
Workplace
→ who is operating, under which context and authority

Execution
→ how work proceeds, pauses, reviews, fails, and completes
```

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

It may also initiate or hand off:

- confirmed user intent;
- prepared requests;
- Product-originated actions;
- review requests;
- Workflow entry;
- collaboration preparation;
- Artifact preparation.

But Execution remains authoritative for:

- Workflow progression;
- Task lifecycle;
- Human Review gates;
- approval sequencing;
- Communication boundaries;
- protected-action controls;
- retry;
- safe failure;
- idempotency;
- execution trace;
- replay;
- escalation.

Workplace must not invent its own Task statuses, bypass Human Review, perform protected action directly, treat interface completion as execution completion, or redefine Event ownership.

The distinction is:

```text
Workplace makes governed work visible and contextual.

Execution makes governed work proceed.
```

Workplace is not a Workflow engine.

---

## 4. Workplace and Products

Workplace is the organizational environment.

Products provide focused user experiences and domain journeys.

The relationship is:

```text
Workplace preserves the organization.

Product serves the journey.
```

Products may consume authorized Workplace context, including:

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

Workplace may host or connect Lite, MarkReg, MGSN interfaces, organization-specific applications, and future Products.

Those Products may differ in:

- navigation;
- interaction model;
- Product loop;
- domain scope;
- release cycle;
- data presentation;
- Artifact types;
- recommendation model;
- embedded or standalone operation.

That independence is desirable.

What must remain stable is organizational continuity.

Workplace must not become:

- one mandatory monolithic interface;
- a universal Product backlog;
- a reason to merge all Product responsibilities;
- a mega-application that must be completed before Product loops are validated.

Products must not become:

- owners of organization identity;
- owners of client relationships;
- owners of shared Task semantics;
- owners of private organizational truth;
- substitutes for Workplace.

The boundary test is:

```text
If the responsibility preserves organizational continuity
across several Products,
it belongs in Workplace.

If it shapes one focused user journey,
it belongs in a Product.
```

Workplace is not the only Product, and no Product is the whole Workplace.

---

## 5. Workplace and MGSN

Workplace is the network participation node.

MGSN enables and governs cross-Workplace discovery, routing, and collaboration interfaces.

The relationship is:

```text
Organization / Workplace / Orbit
→ participates through MGSN
```

Under authorization, Workplace may provide:

- organization identity;
- public or shared Capability profile;
- jurisdiction coverage;
- selected provider evidence;
- availability;
- network preferences;
- partner relationships;
- outcome feedback;
- trust evidence.

MGSN may provide:

- provider candidates;
- Capability discovery;
- trust-supported recommendations;
- jurisdiction coverage;
- routing explanations;
- collaboration options;
- partner-expansion paths.

Workplace retains authority over:

- whether to participate;
- which profile data is shared;
- which relationships remain private;
- whether a candidate is accepted;
- which provider is selected;
- whether public discovery is used;
- which outcome evidence is contributed.

MGSN must not become:

- the owner of the client;
- an open bidding marketplace by default;
- a forced-allocation engine;
- an automatic provider-appointment authority;
- the universal owner of trust;
- the owner of organization pricing;
- the owner of private partner relationships.

The distinction is:

```text
MGSN enables connection.

Participating Workplaces retain relationship and selection authority.
```

Workplace is not the network itself, and MGSN does not own the relationship merely because it supports the connection.

---

## 6. Workplace and Private, Local, and Shared Context

Workplace carries organization-private context while consuming shared knowledge and capabilities.

These responsibilities must remain distinct.

### Private knowledge and organizational memory

Workplace may preserve:

- private templates;
- client instructions;
- internal practice notes;
- provider evaluations;
- pricing knowledge;
- local procedures;
- internal risk interpretations;
- organization-specific lessons;
- unpublished strategy;
- historical outcomes.

Some information may later be shared through explicit governance.

It does not become shared merely because it exists inside MarkOrbit.

The architecture must preserve:

```text
private knowledge
≠
shared knowledge

organization preference
≠
universal rule

knowledge candidate
≠
canonical knowledge
```

### Local Vault

Local Vault provides a logical local or private technical boundary that Workplace may use.

Workplace may define policy for:

- which data remains local;
- which Products may access it;
- which users may unlock it;
- which records may synchronize;
- which AI capabilities may use local context;
- which retention rules apply.

But Workplace architecture does not define the exact storage engine, encryption algorithm, synchronization protocol, file layout, local database schema, or backup mechanism.

Those belong to future Local Vault specifications and implementation decisions.

### Shared knowledge and capabilities

Workplace may consume shared knowledge, intelligence, Capabilities, Skills, Agent Profiles, Workflows, Artifact services, and Delivery capabilities.

It may decide:

- which Capability is enabled;
- which Skill is preferred;
- which users may invoke it;
- which clients permit its use;
- which review level applies;
- which Product may expose it;
- which result remains a candidate.

But Workplace does not redefine shared Capability or Skill semantics.

The overall rule is:

```text
Workplace governs authorized organizational use.

Shared systems define and provide reusable functions.

Local Vault provides the local/private technical boundary.
```

Workplace is neither the universal knowledge authority nor the universal storage engine.

---

## 7. Workplace and AI Agent Runtime

Workplace supplies authorized organization, user, client, Product, and purpose context.

AI Agent Runtime governs how an Agent operates within that context.

The relationship is:

```text
Workplace
→ supplies authorized context

AI Agent Runtime
→ governs Agent identity, permission, tools, limits, and trace
```

Workplace may provide:

- active organization;
- active user;
- role;
- client context;
- private knowledge;
- Product context;
- purpose;
- approved tools;
- policy references;
- review requirements.

Agent governance must determine:

- Agent identity;
- Agent Profile;
- permission;
- Capability;
- tool access;
- context scope;
- output type;
- audit;
- termination;
- handoff;
- prohibited actions.

Workplace must not assume:

- that any AI Agent may use all organizational context;
- that Product access equals Agent permission;
- that model capability equals professional authority;
- that an AI draft is approved;
- that an Agent may mutate formal state;
- that an Agent may send, file, pay, appoint, or instruct autonomously.

The boundary is:

```text
Workplace determines which context may be supplied.

Agent governance determines how the Agent may operate.

Human Review and Owning Services preserve authority.
```

Workplace is not an Agent framework.

---

## 8. Workplace and Artifacts, Delivery, and Formal State

Workplace supplies organization context for Artifact creation, review, access, and delivery.

It does not collapse the Artifact lifecycle or become the universal system of record.

Workplace may provide:

- organization brand;
- client context;
- approved templates;
- reviewer assignment;
- delivery preferences;
- private assets;
- access control;
- version visibility;
- retention policy.

The architecture must preserve:

```text
Content ≠ Artifact

Artifact ≠ Document

Render ≠ Edit

Delivery ≠ Publish

Draft ≠ approved output
```

A Product may generate Content.

A shared service may render an Artifact.

A human professional may review it.

Delivery may send it to a defined recipient.

Publish may make it available to a broader audience.

These are related steps, not interchangeable states.

The same discipline applies to formal business facts.

Workplace may display Matters, Tasks, Orders, Communications, Documents, payments, provider engagements, filing status, official outcomes, and Opportunities.

It may prepare intent, draft changes, review requests, recommendations, candidate records, and context packages.

But the proper Owning Service remains authoritative for formal mutation.

```text
Visible or prepared in Workplace
≠
formally owned by Workplace
```

Workplace is not a generic file manager and not the universal system of record.

---

## 9. What Workplace Is Responsible For

At the architectural level, Workplace is responsible for the organization-level representation and governance of:

- organization identity;
- organization profile;
- users and roles;
- Product access;
- client context;
- relationship context;
- private knowledge;
- business rules;
- pricing and preferences;
- service catalog;
- partner preferences;
- AI context policy;
- work and review visibility;
- network participation preferences;
- organizational memory;
- local and private data policy.

This does not imply one database, one service, or one repository.

Logical responsibility and implementation topology are separate decisions.

Workplace consumes:

- Core semantics;
- governed Execution;
- shared knowledge and intelligence;
- Capability definitions;
- Skills;
- Agent Profiles;
- Workflow definitions;
- Artifact, Render, Edit, Delivery, and Publish capabilities;
- MGSN interfaces;
- Product-specific functions;
- Local Vault functions.

It coordinates with Products, Execution, Owning Services, AI Agent Runtime, shared knowledge systems, MGSN, Local Vault, and external organization systems.

Consumption and coordination do not imply ownership.

---

## 10. Boundary Matrix

| Concept | Workplace responsibility | External authority or responsibility | Boundary rule |
|---|---|---|---|
| Organization identity and context | Primary organizational responsibility | Organization itself remains the real legal and professional actor | Workplace represents; it does not replace legal identity |
| Users and roles | Organization-level representation and assignment | Core permission and policy boundaries remain authoritative | Role context must not redefine shared permission semantics |
| Clients and relationships | Preserves organization-controlled context and continuity | Relevant Owning Services may hold formal records | Platform use does not transfer relationship ownership |
| Private knowledge | Preserves organization and client-private context | Shared knowledge governance controls promotion to shared states | Private does not become shared automatically |
| Core semantics | Consumes and applies | Core is authoritative | Workplace must not redefine shared meaning |
| Workflow and Task progression | Exposes and contextualizes | Execution is authoritative | Visibility does not equal lifecycle ownership |
| Product UX | Hosts or connects | Product is responsible for its journey | Workplace must not become a universal Product |
| Capability definition | Authorizes organizational use | Capability Catalog is authoritative | Enabled does not mean universally permitted |
| Skill implementation | Selects or prefers under policy | Skill Registry governs implementation identity and version | Workplace does not redefine Skill semantics |
| AI Agent operation | Supplies authorized context | Agent governance controls runtime identity, tools, and limits | Context does not equal Agent authority |
| Formal business state | Displays and prepares context | Proper Owning Service is authoritative | Workplace does not mutate protected state by convenience |
| Artifact lifecycle | Supplies organization context, assets, reviewer, and visibility | Artifact architecture and relevant Owning Services govern formal states | Artifact must not collapse into file or Document |
| Delivery and Publish | Supplies policy and recipient context | Delivery/Publish authorities govern execution and state | Delivery and Publish remain distinct |
| Local/private technical control | Defines organization policy | Local Vault provides technical boundary | Workplace policy does not define storage implementation |
| Network participation | Defines organization preferences and selection | MGSN enables and governs connection interfaces | Workplaces retain relationship and selection authority |
| Professional judgment | Supports evidence and review | Human professionals remain accountable | Software capability does not become professional authority |

This matrix is an authority map.

It is not a service or repository map.

---

## 11. Explicit Non-Goals

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

a shared knowledge authority

a Workflow engine

an implementation repository

a deployment model

a production-readiness declaration
```

Workplace must not:

- redefine Core Objects, Services, statuses, or ownership;
- redefine Task, Workflow, Review, or Event semantics;
- bypass Human Review;
- authorize autonomous AI professional action;
- perform external Communication send by default;
- authorize filing, submission, payment, provider instruction, or official recordal;
- treat candidates as approved;
- convert recommendations directly into formal Tasks or Opportunities;
- treat Artifact as identical to Document;
- treat MGSN as open bidding or forced allocation;
- treat the organization as a platform-owned account;
- require one universal Product experience;
- require cloud centralization;
- require destructive migration;
- treat visibility as ownership;
- treat invocation as definition;
- treat context as mutation authority.

These are constitutional non-goals.

They do not prohibit future implementation.

They constrain how future implementation must preserve authority and organizational autonomy.

---

## 12. Minimum Boundary Lock

Every conforming Workplace must preserve the following lock:

```text
Workplace is responsible for authorized organizational context.

Core is authoritative for shared semantics.

Execution is authoritative for governed coordination.

Products are responsible for user journeys and domain composition.

MGSN enables and governs cross-Workplace discovery,
routing, and collaboration interfaces;
participating Workplaces retain relationship and selection authority.

Owning Services are authoritative for formal business-state mutation.

Human professionals remain accountable for professional judgment.

AI Agents assist under identity, permission, context, and governance.

Local Vault provides the local/private technical boundary
under authorized Workplace policy.

Artifact architecture defines the cross-Product outcome model.
```

This lock may be implemented in different technical forms.

Its authority model must not change.

---

## 13. Book 04 and Chapter Boundary

Book 04 defines:

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
- Book 03 Execution changes;
- final Lite requirements;
- final MarkReg requirements;
- MGSN implementation;
- APIs;
- schemas;
- code architecture;
- deployment;
- infrastructure;
- repository topology;
- production readiness.

This chapter does not authorize external Communication send, filing, payment, provider appointment, provider instruction, official recordal, autonomous AI action, or unrestricted implementation.

Book 04 is architecture.

It is not a Product PRD or implementation manual.

---

## 14. Chapter Conclusion

Workplace is intentionally broad.

It must hold the organizational context that makes professional operation coherent across Products, Execution, capabilities, knowledge, Artifacts, and networks.

But Workplace must not become total.

It must not absorb:

- the shared meaning defined by Core;
- the coordination governed by Execution;
- the journeys owned by Products;
- the connection role of MGSN;
- the runtime governance of AI Agents;
- the technical implementation of Local Vault;
- the formal mutation authority of Owning Services.

The final distinction is:

```text
Workplace is where the organization operates.

It is not where every system responsibility is owned.
```

A conforming Workplace preserves organizational autonomy, authorized context, privacy, human accountability, governed handoff, Product independence, network independence, and explicit formal-state authority.

This is how MarkOrbit avoids two opposite failures:

```text
a fragmented collection of disconnected Products
and
a centralized platform that owns everything
```

Workplace sits between those extremes.

It creates one coherent organizational Orbit while preserving the authority, independence, and responsibility of every surrounding layer.
