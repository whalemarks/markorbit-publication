# B04-EDIT-0001 — CH00–CH12 Editorial Weave Patch Set

## Status

Controlled editorial input for `B04-vNEXT-CANDIDATE-01`. RC1 remains immutable.

## Use rule

Each module below identifies the natural point in the chapter argument where accepted vNext meaning must replace, merge with or extend RC1 prose. The supplied wording is candidate prose: it may receive copyediting, but its authority distinctions must not be weakened.

---

## CH00 — Preface

**Operation:** MERGE / INSERT

**Placement:** After the first explanation that each organization needs a stable operating boundary.

**Retain:** The independent-Orbit thesis and the statement that shared foundations do not require centralized ownership.

**Weave text:**

> Workplace is the Organization-scoped boundary through which business sovereignty, accountability, permission, Product operation and governed collaboration remain coherent. It is not the Organization itself, and it does not become the authority over every fact visible within it. Core continues to define shared meaning; each Owning Service continues to control its formal lifecycle records; legal and official sources remain authoritative for the facts they govern. Workplace makes those authorities usable within an independent professional operating context without absorbing them.

**Remove or normalize:** Any implication that Workplace simply “owns” all organization data. Replace broad ownership language with the applicable combination of business authority, source authority, formal-state authority and physical custody.

**Continuity:** Prepares CH02 and CH04 without front-loading implementation detail.

---

## CH01 — Why Workplace and Product Architecture Matters

**Operation:** INSERT / NORMALIZE

**Placement:** Where the chapter distinguishes shared platform capability from organization independence.

**Weave text:**

> Independence is not architectural isolation. An Organization may operate one or more Workplaces, and each Workplace may install multiple Products. The independence that matters is bounded authority: the Originating Workplace retains its customer and commercial relationship context; Products remain focused experiences; Core retains semantic authority; Owning Services retain formal-state authority; and cross-boundary access remains explicit, purpose-limited, revocable and auditable.

**Replace:** “Single organizational container” language with “Organization-scoped operating boundary” wherever the former would imply that one Organization can have only one Workplace.

**Continuity:** Establishes the problem statement that CH02 resolves.

---

## CH02 — Defining Workplace

**Operation:** REPLACE / MERGE

**Placement:** Replace the primary definition block.

**Weave text:**

> A Workplace is an Organization-scoped business sovereignty and operating boundary. It carries the authorized identity, people, permissions, customer and commercial context, private Knowledge, Product Installations, policies, approvals, collaboration context and institutional memory needed for professional work. It does not replace the Organization, Core, an Owning Service, a Product, a legal source or a professional decision-maker.

> One Organization may operate multiple Workplaces when different business units, jurisdictions, brands, regulated practices or operating models require independently governed boundaries. The relationship is therefore one-to-many unless a Product profile deliberately constrains it.

**Canonical equation:**

```text
Organization
→ may govern one or more Workplaces
→ each Workplace may host one or more Product Installations
```

**Remove:** Any equation that treats Organization and Workplace as interchangeable identities.

---

## CH03 — Workplace as an Independent Orbit

**Operation:** MERGE / INSERT

**Placement:** Immediately after the autonomy principle.

**Weave text:**

> Autonomy is bounded rather than absolute. A Workplace may control its business rules, relationships, permissions, private Knowledge and operating choices, but it cannot redefine Core semantics, mutate records owned by another service, override an official source, enlarge a user's authority or treat another Workplace's context as portable by default. Each Orbit remains independent because its boundaries are governed, not because it is disconnected from shared authority.

**Normalize:** “Own path” must mean local business choice within shared constitutional constraints, not unilateral control over every connected record.

---

## CH04 — Responsibility Across the Architecture

**Operation:** REPLACE

**Placement:** Replace the chapter's central responsibility model with the five-authority model.

**Weave text:**

```text
1. Workplace business sovereignty
   customer, commercial, permission, accountability and operating context

2. Core semantic authority
   canonical meanings, identities, contracts and shared invariants

3. Owning Service formal-state authority
   creation, transition and recordal of governed lifecycle facts

4. Physical custody
   where data is stored, replicated, cached or processed

5. Legal / source authority
   the external or authoritative source governing a fact
```

> These dimensions may coincide in one implementation, but the architecture must not assume that they do. A Workplace may be accountable for using a fact without owning its formal lifecycle. A Product may display or edit a proposed value without controlling the authoritative record. A database may hold a copy without becoming the source of truth.

**Remove:** Any two-layer “platform versus organization ownership” model that collapses these distinctions.

---

## CH05 — Workplace Principles

**Operation:** INSERT / NORMALIZE

**Placement:** Add to the durable principle set.

**Weave text:**

- **Sovereignty with constraint:** Workplace controls its bounded business context while respecting Core, Owning Service and legal authority.
- **Custody neutrality:** local, cloud or hybrid storage does not itself determine ownership or authority.
- **Source respect:** imported, synchronized and projected facts retain provenance and source authority.
- **Least authority:** visibility, editability, administrative role and AI capability never imply broader mutation rights.
- **Purpose limitation:** cross-Workplace and support access is granted for a declared purpose, minimum scope and bounded duration.

**Editorial rule:** Integrate these principles into the existing list rather than adding a second competing list.

---

## CH06 — Workplace Boundaries and Non-Goals

**Operation:** REPLACE / INSERT

**Placement:** In the “what Workplace is not” section.

**Weave text:**

> Workplace is not a universal system of record. It may hold authoritative Workplace-owned facts, projections of records owned elsewhere, synchronized copies, derived context and locally governed private material. Each item must preserve its authority class.

```text
visible ≠ owned
editable ≠ formally mutable
stored ≠ source authoritative
administered ≠ generally accessible
approved ≠ externally completed
```

> Platform support and administration must use explicit support-access grants, scoped purpose, trace and revocation. Administrative capability is not a standing right to inspect participant data.

**Remove:** Broad “single pane of ownership” wording.

---

## CH07 — Organization Identity and Workplace Context

**Operation:** REPLACE / MERGE

**Placement:** Replace language that uses Organization and Workplace as synonyms.

**Weave text:**

> Organization is the durable legal, commercial or institutional actor. Workplace is a governed operating boundary through which that actor conducts a defined body of work. Organization identity may be referenced by several Workplaces; each Workplace adds its own people, permissions, Product Installations, policies, relationships and operating history.

```text
Organization identity
+ Workplace boundary and policy
= authorized operating context
```

> A Workplace identifier must therefore not be used as a substitute for the Organization's legal identity, and an Organization identifier must not bypass Workplace-specific authorization.

---

## CH08 — People, Roles, Permissions and Accountability

**Operation:** REPLACE / INSERT

**Placement:** In the permission model and administrative-access sections.

**Weave text:**

> Permission is evaluated as a scoped tuple rather than a role label alone:

```text
principal
+ Workplace
+ Product Installation
+ resource or capability
+ action
+ purpose
+ conditions
+ time boundary
```

> A role may contribute defaults, but it does not erase resource ownership, purpose limitation, review requirements or legal constraints. Support access is a separate governed path requiring an explicit case, minimum scope, traceable use and revocation. Impersonation, hidden standing access and role-based expansion across Workplaces are non-conforming.

**AI insertion:**

> An AI Assistant or Agent inherits the effective authority of the initiating user within the active Workplace, Product Installation and declared purpose. It cannot compose several partial permissions into a broader authority that no human principal possesses.

---

## CH09 — Customers, Clients and Commercial Relationships

**Operation:** MERGE / INSERT

**Placement:** Where customer context and external provider collaboration are introduced.

**Weave text:**

> The Originating Workplace retains the originating customer relationship, commercial terms, instruction context and approval responsibility unless a separate governed agreement explicitly establishes a different relationship. Sending work to another Workplace does not transfer the customer, and participating in a network does not convert participant relationships into platform-owned inventory.

> An Execution Provider Workplace receives only the context needed to evaluate or perform the accepted scope. Provider-side professional records, evidence and delivery responsibility remain distinct from the originating commercial relationship.

**Normalize:** Replace generic “shared client” language with the actual relationship and authority path.

---

## CH10 — Private Knowledge, AI Context, Preferences and Organizational Memory

**Operation:** REPLACE / INSERT

**Placement:** At the start of the private Knowledge model and again in the AI context section.

**Weave text:**

> Private Knowledge is not one undifferentiated memory pool. The Workplace must preserve source class, provenance, confidentiality, permitted purpose, retention boundary and whether the material is authoritative, advisory, derived or user preference. Synchronization or embedding does not erase those distinctions.

> AI context is assembled for a bounded task from sources the initiating principal is permitted to use. Retrieval, inference and generated content remain attributable to that scope. AI may propose a synthesis, but it does not convert private notes into official facts, another Workplace's material into portable Knowledge or a model output into an approved professional decision.

**Isolation rule:**

```text
no cross-Workplace retrieval by default
no training or reuse beyond declared policy
no authority expansion through derived context
```

---

## CH11 — Workplace Surfaces and Operating Views

**Operation:** MERGE / INSERT

**Placement:** Where dashboards, portals and Product surfaces are described.

**Weave text:**

> A surface is a governed view of authorized context. It may combine Workplace-owned facts, Product state, projections, recommendations and records owned by other services. Presentation does not flatten those authority differences.

```text
surface visibility
≠ record ownership
editable presentation
≠ formal-state mutation
Product action
≠ completed external action
```

> Every action exposed by a surface must resolve to the authority that can validly perform it: local Workplace update, Product configuration, Owning Service command, Human Review, governed Execution or external confirmation.

---

## CH12 — Local, Private, Shared and Synchronized Data

**Operation:** REPLACE / MERGE

**Placement:** Replace any storage-location-based ownership model.

**Weave text:**

> Data classification must separate physical custody from logical and source authority. A fact may be stored locally, synchronized to cloud infrastructure, projected into another Product or cached for performance while remaining formally owned by an Owning Service or authoritative external source.

```text
custody: where bytes are held or processed
business authority: who is accountable for use and decisions
formal-state authority: which service may mutate the governed record
source authority: which source establishes the fact
access authority: who may use it, for what purpose and under which conditions
```

> Synchronization must preserve provenance, version, permitted purpose and conflict behavior. A synchronized copy cannot silently become authoritative. Cross-Workplace synchronization requires explicit authorization, minimum necessary scope, revocation and audit. Platform support access follows the same purpose-limited rule.

**Continuity:** Provides the data-boundary foundation for later Product Projection, Handoff, Return and portability chapters.

---

## Batch-level reconciliation

After applying these modules, the candidate must read as one progressive argument:

```text
why an independent operating boundary is needed
→ what Workplace is
→ how its autonomy is constrained
→ which authorities coexist
→ which principles and non-goals follow
→ how identity, permission, relationships, Knowledge, surfaces and data obey those boundaries
```

## Provenance

Primary controls:

- `B04-VNEXT-WPB-0001_Workplace_Authority_and_Data_Boundaries.md`;
- `B04-CORR-0001_WP-B_Chapter_Correction_Ledger.md`;
- `B04-PROV-0001_CH00-CH39_Integrated_Candidate_Provenance_Ledger.md`;
- Architecture Canon vNext.1;
- ARC-029–ARC-038;
- `MO-ADR-WSP-001`.

## Result gate

```text
Assigned chapters: 13
Weave modules: 13
Unattributed modules: 0
RC1 source modifications: 0
Immediate Book 02 Change Proposal: NO
```
