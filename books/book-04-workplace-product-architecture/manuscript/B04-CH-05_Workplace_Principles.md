# B04-CH-05 — Workplace Principles

**Status:** Draft 1  
**Chapter Map:** B04-TOC-V0.1  
**Writing Pack:** B04-PACK-01 — Front Matter and Part I

## Chapter Purpose

This chapter defines the durable architectural principles that every MarkOrbit Workplace must preserve.

A Workplace may take different forms.

It may serve:

- an independent professional;
- a small specialist team;
- a regional agency;
- a global law firm;
- an enterprise legal department;
- a local or private operating environment;
- an embedded product experience;
- an organization-specific application.

Its user interface may change.

Its deployment model may change.

Its Product composition may change.

Its scale may change.

Its technical architecture may change.

But the Workplace principles must remain stable.

These principles exist to prevent implementation convenience, Product pressure, network growth, or AI capability from weakening organizational autonomy and professional responsibility.

The ten minimum principles are:

1. Organizational Autonomy;
2. Authorized Context;
3. Private and Local by Default;
4. Shared Foundations Without Central Ownership;
5. Human Professional Accountability;
6. Candidate Before Canonical;
7. Governed Execution Before Protected Action;
8. Evidence, Provenance, and Audit;
9. Product Loop First, Shared Platform Extraction Second;
10. Evolution Without Forced Replacement.

Each principle is presented through four questions:

```text
Principle
Why it exists
What it requires
What would violate it
```

The purpose is not to create a Product feature list.

The purpose is to establish architectural constraints that future Workplace editions, Products, specifications, and implementations must preserve.

---

## 1. Principle One — Organizational Autonomy

### Principle

> Each Workplace represents an independent professional organization and must preserve that organization’s control over its clients, data, knowledge, rules, pricing, relationships, brand, commercial decisions, and professional responsibility.

### Why it exists

MarkOrbit is designed as an orbital professional ecosystem.

Its primary operating units are independent organizations, not centrally owned provider accounts.

Professional organizations create value through:

- client trust;
- accumulated knowledge;
- service quality;
- partner relationships;
- pricing judgment;
- jurisdiction experience;
- brand;
- professional reputation;
- internal standards;
- commercial strategy.

These assets must not be absorbed into a central platform merely because the organization uses shared infrastructure.

Without organizational autonomy, Workplace would become a tenant account inside a marketplace rather than the operating boundary of an independent Orbit.

### What it requires

A conforming Workplace must preserve the organization’s authority over:

- client ownership and engagement;
- organization identity and brand;
- user and role structure;
- private knowledge;
- internal templates;
- business rules;
- pricing;
- service catalog;
- preferred partners;
- local data;
- AI context;
- professional review;
- final commercial decisions.

The organization must be able to:

- choose which Products it uses;
- control which context a Product may access;
- select its own providers;
- preserve trusted relationships;
- reject system recommendations;
- retain work internally;
- decide which knowledge is shared;
- maintain organization-specific policies.

Shared services may support the organization.

They must not replace it.

### What would violate it

Violations include:

- treating the platform as the owner of the client;
- converting private partner relationships into platform-owned relationships;
- forcing provider allocation;
- centralizing pricing authority;
- copying private knowledge into a shared pool without authorization;
- making the organization’s operating rules subordinate to platform defaults;
- preventing the organization from retaining or exporting its own data;
- requiring all organizations to adopt one commercial model;
- presenting the organization as replaceable provider inventory.

---

## 2. Principle Two — Authorized Context

### Principle

> Every Workplace action must operate within explicit organizational, user, client, Product, permission, policy, and professional context.

### Why it exists

Professional work is context-dependent.

The same recommendation may be appropriate for one organization and inappropriate for another.

The same user may have authority in one Matter and no authority in another.

The same AI capability may be permitted for one client and prohibited for another.

The same Product may access one category of private knowledge but not another.

Without authorized context, Workplaces become unsafe because users, Products, Skills, and AI Agents act on incomplete or excessive information.

Context must answer:

```text
Which organization?
Which user?
Which role?
Which client?
Which Product?
Which purpose?
Which permission?
Which policy?
Which private information?
Which professional responsibility?
```

### What it requires

A conforming Workplace must:

- identify the active organization;
- identify the acting user;
- establish the user’s role;
- establish the client or business context;
- identify the Product or interface;
- define the purpose of access;
- evaluate permission and policy;
- limit private information to what is authorized;
- preserve review and accountability requirements;
- record which context supported a recommendation or action.

Context assembly must be:

- scoped;
- explainable;
- permission-aware;
- purpose-bound;
- auditable;
- revocable where appropriate.

A Product should receive only the context required for its authorized purpose.

An AI Agent should receive only the context required for its governed role.

### What would violate it

Violations include:

- assembling broad organizational data by default;
- allowing a Product to read all private knowledge because the user has an account;
- allowing an AI Agent to act without an identified user or organization;
- carrying client context into another client’s work;
- using private information for unrelated recommendations;
- treating login as sufficient authorization;
- hiding which data influenced an output;
- reusing sensitive context after its purpose has ended;
- bypassing policy because the action appears low risk.

---

## 3. Principle Three — Private and Local by Default

### Principle

> Organization-private and client-sensitive information should remain private or local unless explicit authority, purpose, and governance justify broader use.

### Why it exists

Professional organizations hold information that may be:

- confidential;
- commercially sensitive;
- legally privileged;
- client-specific;
- jurisdiction-sensitive;
- competitively valuable;
- operationally private.

Examples include:

- client instructions;
- pricing;
- partner evaluations;
- draft legal positions;
- evidence;
- internal templates;
- risk assessments;
- service margins;
- dispute history;
- local operating records;
- AI context;
- unpublished strategy.

A centralized-by-default model would create unnecessary exposure.

It would also weaken organizational autonomy by treating all information as a platform asset.

### What it requires

A conforming Workplace should:

- distinguish shared, organization-private, client-private, and local-only information;
- minimize unnecessary synchronization;
- support local or private storage where justified;
- make sharing explicit;
- define retention and deletion expectations;
- preserve purpose limitations;
- identify which Products may access which data;
- identify which AI capabilities may use which context;
- prevent silent promotion of private records into shared knowledge;
- record synchronization and sharing decisions.

The default should be:

```text
private until authorized
local where appropriate
shared only for a defined purpose
```

“Local” does not automatically mean ungoverned.

Local data still requires:

- identity;
- permission;
- audit;
- versioning;
- backup policy;
- professional responsibility.

### What would violate it

Violations include:

- synchronizing all local files by default;
- using client records for shared AI training without authorization;
- treating private knowledge as public network evidence;
- exposing pricing or partner history to unrelated Products;
- requiring cloud centralization for all Workplace functions;
- hiding where data is stored;
- making local-only status technically impossible;
- allowing copied data to outlive the authorized purpose;
- assuming that encryption alone resolves governance.

---

## 4. Principle Four — Shared Foundations Without Central Ownership

### Principle

> Workplaces should consume shared Core semantics, governed Execution, capabilities, knowledge, and infrastructure without transferring organizational ownership to the shared platform.

### Why it exists

MarkOrbit requires common foundations.

Without them, organizations would implement inconsistent meanings, workflows, reviews, Artifacts, and network interactions.

Shared foundations create:

- interoperability;
- consistency;
- safer collaboration;
- reusable capability;
- lower implementation cost;
- stronger governance;
- better learning.

But shared infrastructure can easily become central ownership.

A platform may begin by providing common services and gradually claim control over:

- clients;
- data;
- relationships;
- identity;
- pricing;
- provider appointment;
- professional decisions.

The architecture must prevent that drift.

### What it requires

A conforming Workplace must preserve the distinction:

```text
Core defines shared semantics.
Execution governs coordinated work.
Shared capabilities provide governed functions.
Workplace preserves organizational context.
The organization retains ownership of its professional environment.
```

Shared services may provide:

- identity infrastructure;
- capability definitions;
- knowledge services;
- intelligence;
- Workflow support;
- Artifact tooling;
- network interfaces;
- audit;
- synchronization;
- common UX components.

But they must not automatically own:

- clients;
- private knowledge;
- pricing;
- partner relationships;
- professional conclusions;
- commercial strategy.

### What would violate it

Violations include:

- treating use of shared infrastructure as transfer of client ownership;
- making platform ranking the final provider decision;
- centralizing all organizational knowledge;
- requiring shared pricing;
- making Product access conditional on surrendering private data;
- using common identity to erase organization identity;
- treating shared capability as platform authority;
- preventing organization-specific rules because they differ from defaults.

---

## 5. Principle Five — Human Professional Accountability

### Principle

> Human professionals remain accountable for professional judgment, approval, and protected action.

### Why it exists

MarkOrbit operates in professional services.

Many actions carry:

- legal consequences;
- financial consequences;
- client commitments;
- deadline risk;
- evidentiary consequences;
- reputational risk;
- professional liability.

AI may improve speed and quality.

Products may simplify the journey.

Execution may enforce gates.

But accountability cannot disappear into the system.

A professional conclusion must remain attributable to an accountable person or organization.

### What it requires

A conforming Workplace must make visible:

- who prepared;
- who reviewed;
- who approved;
- who instructed;
- who executed;
- who remains responsible;
- which AI support was used;
- which evidence informed the decision.

Human Review must remain distinct from:

- AI output;
- automated validation;
- Product confirmation;
- Workflow completion;
- system confidence.

Protected actions must require appropriate human authority.

Examples include:

- filing;
- submission;
- payment;
- provider appointment;
- external Communication send;
- legal-position approval;
- official recordal;
- binding client instruction.

### What would violate it

Violations include:

- allowing AI confidence to substitute for review;
- treating user inactivity as approval;
- allowing a Product button to bypass professional authorization;
- attributing an AI-generated conclusion to a human who did not review it;
- allowing an Agent to file or send autonomously;
- obscuring who made the final decision;
- making Human Review optional for convenience;
- recording “system approved” without an accountable authority.

---

## 6. Principle Six — Candidate Before Canonical

### Principle

> Derived outputs must remain candidates until professional validation and governance promote them into approved or canonical states.

### Why it exists

MarkOrbit produces many useful outputs:

- Structured Information;
- Knowledge Candidates;
- Capability Candidates;
- Skill Candidates;
- Workflow Fragments;
- Task Suggestions;
- Opportunity Candidates;
- provider matches;
- AI drafts;
- Artifact drafts;
- capability evidence;
- recommendations.

These outputs may be valuable.

They are not automatically authoritative.

Without a candidate stage, the system may silently convert:

- extraction into knowledge;
- recommendation into decision;
- draft into approval;
- evidence into rating;
- suggestion into Task;
- match into appointment.

The candidate stage protects professional judgment and governance.

### What it requires

A conforming Workplace must preserve distinctions such as:

```text
Structured Information ≠ verified Knowledge

Knowledge Candidate ≠ Canonical Knowledge

Capability Candidate ≠ approved Capability

Skill Candidate ≠ enabled Skill

Workflow Fragment ≠ executable Workflow

TaskSuggestion ≠ formal Task

Opportunity Candidate ≠ formal Opportunity

Capability Evidence ≠ final capability rating

AI Draft ≠ approved professional output
```

Candidate records should preserve:

- source;
- provenance;
- generating method;
- confidence;
- version;
- reviewer;
- validation status;
- approval status;
- rejection reason where applicable.

Promotion must be explicit.

### What would violate it

Violations include:

- inserting AI output directly into approved knowledge;
- creating formal Tasks from recommendations without acceptance;
- treating extracted rules as canonical;
- converting provider evidence into a final rating automatically;
- publishing Artifact drafts without review;
- hiding candidate status in the UI;
- allowing Product labels to imply approval;
- losing the source or version of a candidate.

---

## 7. Principle Seven — Governed Execution Before Protected Action

### Principle

> Any protected action must pass through governed Execution, required review, and the proper Owning Service.

### Why it exists

Professional systems often confuse preparation with action.

A draft may be complete.

A recommendation may be persuasive.

A filing package may be ready.

A provider may be suitable.

A payment may be calculated.

None of these facts means the protected action may proceed.

Protected actions require:

- identity;
- permission;
- policy;
- completeness;
- Human Review;
- approval;
- trace;
- formal mutation authority.

### What it requires

A conforming Workplace must hand protected work into governed Execution.

The correct line is:

```text
Observe
→ Explain
→ Recommend
→ Prepare
→ Confirm
→ Execute
→ Learn
```

The system must distinguish:

```text
prepared action
from
authorized action
```

and:

```text
user intent
from
formal mutation
```

Execution should govern:

- Tasks;
- reviews;
- approvals;
- communication boundaries;
- protected-action gates;
- retries;
- safe failure;
- Events;
- audit.

The Owning Service must record the formal fact.

### What would violate it

Violations include:

- allowing a recommendation to trigger filing automatically;
- treating document completion as approval;
- allowing Product UI to mutate protected state directly;
- allowing an Agent to send Communications;
- recording provider appointment before authorization;
- treating payment calculation as payment approval;
- bypassing review because the workflow is familiar;
- hiding failed protected actions;
- allowing retry without idempotency or audit.

---

## 8. Principle Eight — Evidence, Provenance, and Audit

### Principle

> Professional outputs, recommendations, decisions, and state changes must remain traceable to their evidence, source, version, actor, and authority.

### Why it exists

Professional work must be explainable.

A user should be able to ask:

```text
Why was this recommended?
Which data was used?
Which rule was applied?
Which version was active?
Who prepared this?
Who reviewed it?
What did AI contribute?
Which Product initiated the work?
Which Owning Service changed the state?
What happened after approval?
```

Without evidence and provenance, the system may produce plausible results that cannot be trusted, reviewed, corrected, or defended.

Audit is also essential for:

- quality control;
- dispute handling;
- professional review;
- compliance;
- error correction;
- model evaluation;
- capability validation;
- trust feedback;
- organizational learning.

### What it requires

A conforming Workplace must preserve, where relevant:

- source identifiers;
- source versions;
- timestamps;
- actor identity;
- organization identity;
- Product origin;
- AI model or Agent role;
- Skill version;
- policy version;
- reviewer;
- approval;
- state transition;
- Owning Service;
- Artifact version;
- delivery result;
- failure result.

The system should separate:

```text
AI suggested
Human reviewed
System executed
Owning Service recorded
```

### What would violate it

Violations include:

- storing only the final output;
- losing the source behind a recommendation;
- overwriting prior versions;
- recording approval without the approver;
- allowing unaudited AI mutations;
- hiding failed attempts;
- merging human and AI contributions into one anonymous result;
- treating logs as optional;
- deleting evidence required to explain a professional decision.

---

## 9. Principle Nine — Product Loop First, Shared Platform Extraction Second

### Principle

> Product value loops should be validated before responsibilities are extracted into shared platform services.

### Why it exists

Architecture can become speculative.

Teams may attempt to design:

- universal services;
- generic registries;
- shared APIs;
- platform-wide abstractions;
- reusable infrastructure;

before real Product behavior has been validated.

This creates premature complexity.

MarkOrbit should first prove user value through concrete Product loops.

Examples include:

- Lite’s Today → Recommendation → Prepared Action → Confirmation → Handoff;
- MarkReg’s need recognition → recommendation → intake → filing preparation;
- MGSN’s need → candidate discovery → human selection → collaboration.

Repeated and stable needs may then justify shared extraction.

### What it requires

A conforming Workplace and Product architecture should:

- identify the user problem;
- define the Product loop;
- validate the loop;
- observe repeated responsibilities;
- extract only stable shared capabilities;
- preserve Product ownership where behavior remains specific;
- avoid forcing all Products into one abstraction prematurely.

The sequence is:

```text
Product problem
→ Product loop
→ user validation
→ repeated architectural need
→ shared capability extraction
```

not:

```text
shared platform theory
→ generic service
→ search for a Product use
```

### What would violate it

Violations include:

- creating a shared service because two files look similar;
- building a universal Workflow engine before Product loops are proven;
- forcing Lite and MarkReg into one Product model;
- creating repositories for every logical concept;
- extracting capability before ownership is understood;
- using platform elegance as a substitute for user value;
- redesigning Products around speculative abstractions.

---

## 10. Principle Ten — Evolution Without Forced Replacement

### Principle

> MarkOrbit should allow Organizations, Workplaces, Products, Skills, and relationships to evolve without requiring destructive replacement.

### Why it exists

Professional systems accumulate value over time.

Organizations build:

- client history;
- templates;
- review practices;
- trusted providers;
- private knowledge;
- pricing logic;
- operational habits;
- evidence;
- Artifacts;
- audit history.

A new Product, Skill, Agent, or network feature should not require that accumulated value to be discarded.

Evolution should strengthen the organization rather than reset it.

### What it requires

A conforming Workplace should support:

- versioned change;
- migration;
- coexistence;
- gradual adoption;
- rollback where appropriate;
- preservation of history;
- replacement of one Skill without replacing the Capability;
- replacement of one Product without replacing the Workplace;
- addition of a new provider without deleting existing trust history;
- Product embedding without centralization;
- local and cloud evolution under explicit policy.

The principle may be summarized as:

```text
Replace implementation when necessary.
Preserve organizational continuity.
```

### What would violate it

Violations include:

- requiring data reset for Product upgrades;
- tying organization identity to one Product;
- deleting history when a provider changes;
- requiring one deployment model for all Workplaces;
- treating legacy relationships as invalid;
- forcing all organizations onto the same operating model;
- replacing Capability identity when only a Skill changes;
- making migration impossible without surrendering private data;
- using innovation as justification for centralization.

---

## 11. Principle Interaction

The ten principles are not independent checkboxes.

They reinforce one another.

### Autonomy requires authorized context

An organization cannot retain control if the system cannot determine whose context is active.

### Authorized context requires privacy

Context assembly becomes dangerous if private information is shared by default.

### Privacy requires provenance

The system must know where information came from and why it was used.

### Candidate-before-canonical requires Human accountability

Promotion from candidate to approved state requires accountable review.

### Human accountability requires governed Execution

Approval and protected action must occur through controlled gates.

### Governed Execution requires clear ownership

The proper Owning Service must remain responsible for formal mutation.

### Shared foundations require autonomy

Common services are valuable only when they do not absorb the organization.

### Product-loop discipline supports evolution

Validated Product loops create better foundations for gradual extraction.

### Evolution requires versioning and audit

Change without history becomes replacement rather than evolution.

The architecture should therefore evaluate the principles as a system.

---

## 12. Principle-to-Violation Matrix

| Principle | What it protects | Typical violation |
|---|---|---|
| Organizational Autonomy | Clients, data, knowledge, rules, relationships, commercial control | Platform becomes owner of client or provider relationship |
| Authorized Context | Correct identity, permission, purpose, and scope | Product or AI uses broad context without purpose |
| Private and Local by Default | Confidentiality and organizational control | All local or private data is synchronized automatically |
| Shared Foundations Without Central Ownership | Interoperability without absorption | Shared infrastructure claims organizational assets |
| Human Professional Accountability | Professional judgment and responsibility | AI or system confidence substitutes for review |
| Candidate Before Canonical | Validation and governance | Draft, extraction, or recommendation becomes approved fact |
| Governed Execution Before Protected Action | Safe operational control | Product or Agent performs protected action directly |
| Evidence, Provenance, and Audit | Explainability and traceability | Final result is stored without source or reviewer |
| Product Loop First, Shared Platform Extraction Second | User value and disciplined architecture | Generic platform services are built before Product validation |
| Evolution Without Forced Replacement | Organizational continuity | Upgrade requires destructive migration or loss of history |

This table is suitable for future conformance review.

It is not a substitute for detailed Product or implementation acceptance criteria.

---

## 13. Workplace Conformance Questions

A proposed Workplace design should be reviewed through questions such as:

### Organizational autonomy

- Does the organization retain control of clients, knowledge, rules, pricing, and relationships?
- Does the design make the platform appear to own the professional environment?

### Authorized context

- Is organization, user, role, client, Product, and purpose context explicit?
- Is access limited to the minimum necessary context?

### Privacy and locality

- Which data remains local?
- Which data is shared?
- Who authorized the sharing?
- Can the organization understand and reverse synchronization?

### Human accountability

- Which actions require professional review?
- Is the reviewer visible?
- Can AI output be mistaken for approval?

### Candidate states

- Which outputs are candidates?
- How are candidates promoted, rejected, or versioned?

### Execution

- Which protected actions enter governed Execution?
- Which Owning Service records the final state?

### Evidence

- Can the system explain the recommendation, decision, and state change?
- Are human and AI contributions distinguishable?

### Product discipline

- Is this responsibility proven by a Product loop?
- Is shared extraction justified by repeated use?

### Evolution

- Can the organization adopt the change without losing history or control?
- Can a Product or Skill be replaced without replacing the Workplace?

These questions should be answered before implementation is considered conformant.

---

## 14. What the Principles Do Not Define

The principles do not define:

- Product screen layouts;
- database schemas;
- API payloads;
- service topology;
- microservices;
- deployment architecture;
- cloud-provider choices;
- synchronization protocols;
- encryption algorithms;
- identity federation implementation;
- scoring formulas;
- ranking algorithms;
- AI model selection;
- exact Workflow definitions;
- exact permission matrices;
- Product pricing;
- provider contracting;
- production-readiness approval.

These belong to later architecture specifications, Product charters, implementation ADRs, and repositories.

The principles constrain those decisions.

They do not replace them.

---

## 15. Anti-Patterns

Several recurring anti-patterns should be rejected.

### 15.1 The Universal Workplace

One Product attempts to represent every organization, every domain, every Workflow, and every role.

This creates a mega-Product rather than an architectural shell.

### 15.2 The Smart Tenant

A technical tenant model is given more features and renamed Workplace.

The organizational and authority model remains undefined.

### 15.3 The AI-Owned Organization

An AI Agent becomes the default actor for recommendations, decisions, and mutations.

Human responsibility becomes ceremonial.

### 15.4 The Central Knowledge Pool

Private organizational knowledge is extracted into one shared Brain without explicit governance.

### 15.5 The Invisible Execution Layer

Products directly implement Task, review, send, filing, and payment behavior.

Execution governance fragments.

### 15.6 The Marketplace Workplace

The Workplace is designed primarily to feed demand, ranking, and provider allocation into a central marketplace.

Organizational autonomy weakens.

### 15.7 The Premature Platform

Shared services are extracted before Product loops prove stable needs.

The architecture becomes abstract and expensive.

### 15.8 The Destructive Upgrade

New Products or services require organizations to abandon existing data, relationships, or operating models.

Evolution becomes forced replacement.

---

## 16. Minimum Principle Lock

Every MarkOrbit Workplace must preserve the following lock:

```text
The organization remains independent.

Context is explicitly authorized.

Private information remains private or local by default.

Shared foundations do not become central ownership.

Humans remain professionally accountable.

Candidates do not become canonical without validation.

Protected action enters governed Execution.

Evidence, provenance, and audit remain visible.

Product loops are validated before shared extraction.

Evolution preserves organizational continuity.
```

A system may be technically impressive and still fail this lock.

A system that fails the lock is not a conforming MarkOrbit Workplace.

---

## 17. Non-Goals of This Chapter

This chapter does not:

- define a Workplace Product roadmap;
- define Lite features;
- define MarkReg features;
- define MGSN implementation;
- define Core semantic changes;
- redefine Execution;
- authorize autonomous AI action;
- authorize external Communication send;
- authorize filing, submission, payment, provider instruction, or official recordal;
- define APIs, schemas, repositories, or deployment;
- declare production readiness.

Its purpose is narrower and more durable.

It defines what every future Workplace design must preserve.

---

## 18. Chapter Conclusion

Workplace principles protect the architectural identity of MarkOrbit.

They ensure that Workplace remains:

- an organizational operating environment rather than a platform account;
- connected without becoming centralized;
- intelligent without making AI the authority;
- private without becoming isolated;
- shared without surrendering ownership;
- governed without becoming inflexible;
- Product-driven without becoming fragmented;
- evolvable without destroying continuity.

The ten principles are:

```text
Organizational Autonomy
Authorized Context
Private and Local by Default
Shared Foundations Without Central Ownership
Human Professional Accountability
Candidate Before Canonical
Governed Execution Before Protected Action
Evidence, Provenance, and Audit
Product Loop First, Shared Platform Extraction Second
Evolution Without Forced Replacement
```

Together, they define the minimum architectural discipline for every Workplace edition, Product embedding, network interface, and implementation decision.

The principles do not dictate one technical form.

They preserve one constitutional outcome:

> Every professional organization remains an independent Orbit, operates within authorized context, uses shared capabilities under governance, and remains accountable for the professional work performed in its name.
