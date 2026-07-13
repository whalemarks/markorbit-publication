# B04-CH-05 — Workplace Principles

**Status:** Draft 2 — Pack 01 Editorial Repair  
**Chapter Map:** B04-TOC-V0.1  
**Writing Pack:** B04-PACK-01 — Front Matter and Part I

## Chapter Purpose

This chapter defines the durable architectural principles that every MarkOrbit Workplace must preserve.

A Workplace may serve:

- an independent professional;
- a small specialist team;
- a regional agency;
- a global law firm;
- an enterprise legal department;
- a local or private operating environment;
- an embedded Product experience;
- an organization-specific application.

Its interface, deployment model, Product composition, scale, and technical implementation may change.

Its constitutional principles must not.

These principles prevent Product pressure, implementation convenience, network growth, or AI capability from weakening organizational autonomy and professional responsibility.

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
What is the principle?

Why does it exist?

What does it require?

What would violate it?
```

These principles are not a Product feature list.

They are architectural constraints that future Workplace editions, Products, specifications, and implementations must preserve.

---

## 1. Organizational Autonomy

### Principle

> Each Workplace represents an independent professional organization and must preserve that organization’s control over its clients, data, knowledge, rules, pricing, relationships, brand, commercial decisions, and professional responsibility.

### Why it exists

MarkOrbit is an orbital professional ecosystem.

Its primary operating units are independent organizations, not centrally owned provider accounts.

Professional organizations create value through client trust, accumulated knowledge, service quality, partner relationships, pricing judgment, jurisdiction experience, brand, reputation, and internal standards.

These assets must not be absorbed into a central platform merely because the organization uses shared infrastructure.

Without autonomy, Workplace would become a tenant account inside a marketplace rather than the operating boundary of an independent Orbit.

### What it requires

A conforming Workplace must allow the organization to:

- retain client ownership and engagement authority;
- preserve organization identity and brand;
- control users, roles, and Product access;
- maintain private knowledge and templates;
- define business rules and pricing;
- select or reject providers;
- preserve trusted relationships;
- control which knowledge is shared;
- retain local or private data where appropriate;
- remain accountable for professional decisions.

Shared services may support the organization.

They must not replace it.

### What would violate it

Violations include:

- treating the platform as the owner of the client;
- forcing provider allocation;
- centralizing pricing authority;
- copying private knowledge into a shared pool without authorization;
- converting trusted relationships into platform-owned relationships;
- requiring all organizations to adopt one commercial model;
- preventing the organization from retaining or exporting its own data;
- presenting the organization as replaceable provider inventory.

---

## 2. Authorized Context

### Principle

> Every Workplace action must operate within explicit organizational, user, client, Product, permission, policy, and professional context.

### Why it exists

Professional work is context-dependent.

The same recommendation may be appropriate for one organization and inappropriate for another.

The same user may have authority in one Matter and no authority in another.

The same AI capability may be permitted for one client and prohibited for another.

The same Product may access one class of private knowledge but not another.

Without authorized context, users, Products, Skills, and AI Agents may act on incomplete or excessive information.

### What it requires

A conforming Workplace must identify:

```text
Which organization?

Which user?

Which role?

Which client or business context?

Which Product?

Which purpose?

Which permission?

Which policy?

Which private information?

Which professional responsibility?
```

Context assembly must be:

- scoped;
- purpose-bound;
- permission-aware;
- explainable;
- auditable;
- revocable where appropriate.

A Product should receive only the context necessary for its authorized purpose.

An AI Agent should receive only the context necessary for its governed role.

### What would violate it

Violations include:

- assembling broad organization data by default;
- treating login as sufficient authorization;
- allowing a Product to read all private knowledge because the user has an account;
- allowing an AI Agent to act without identified organization or user context;
- carrying one client’s information into another client’s work;
- using sensitive context for an unrelated purpose;
- hiding which data influenced an output;
- retaining context after its authorized purpose has ended.

---

## 3. Private and Local by Default

### Principle

> Organization-private and client-sensitive information should remain private or local unless explicit authority, purpose, and governance justify broader use.

### Why it exists

Professional organizations hold information that may be confidential, commercially sensitive, legally privileged, client-specific, jurisdiction-sensitive, or competitively valuable.

Examples include:

- client instructions;
- pricing and margins;
- provider evaluations;
- draft legal positions;
- evidence;
- internal templates;
- risk assessments;
- dispute history;
- unpublished strategy;
- AI context.

A centralized-by-default model would create unnecessary exposure and weaken organizational autonomy by treating all information as a platform asset.

### What it requires

A conforming Workplace should distinguish:

```text
shared
organization-private
client-private
local-only
```

It should:

- minimize unnecessary synchronization;
- support local or private storage where justified;
- make sharing explicit;
- preserve purpose limitations;
- define retention and deletion expectations;
- identify which Products and AI capabilities may access which data;
- prevent silent promotion of private records into shared knowledge;
- record synchronization and sharing decisions.

The default is:

```text
private until authorized

local where appropriate

shared only for a defined purpose
```

Local does not mean ungoverned.

Local data still requires identity, permission, audit, versioning, and professional responsibility.

### What would violate it

Violations include:

- synchronizing all local files by default;
- using client records for shared AI training without authorization;
- treating private knowledge as public network evidence;
- exposing pricing or partner history to unrelated Products;
- requiring cloud centralization for every Workplace function;
- hiding where data is stored;
- allowing copied data to outlive its authorized purpose;
- assuming encryption alone resolves governance.

---

## 4. Shared Foundations Without Central Ownership

### Principle

> Workplaces should consume shared Core semantics, governed Execution, capabilities, knowledge, and infrastructure without transferring organizational ownership to the shared platform.

### Why it exists

MarkOrbit requires common foundations.

Without them, organizations would implement inconsistent meanings, Workflows, review rules, Artifacts, and network interactions.

Shared foundations create:

- interoperability;
- safer collaboration;
- reusable capability;
- lower implementation cost;
- stronger governance;
- better learning.

But shared infrastructure can become central ownership if the platform gradually claims control over clients, identity, data, pricing, relationships, provider appointment, or professional decisions.

### What it requires

A conforming Workplace must preserve this distinction:

```text
Core defines shared semantics.

Execution governs coordinated work.

Shared capabilities provide governed functions.

Workplace preserves organizational context.

The organization retains control of its professional environment.
```

Shared services may provide identity infrastructure, knowledge, intelligence, Workflow support, Artifact tooling, network interfaces, audit, synchronization, or common components.

They must not automatically own:

- clients;
- private knowledge;
- pricing;
- partner relationships;
- commercial strategy;
- professional conclusions.

### What would violate it

Violations include:

- treating use of shared infrastructure as transfer of client ownership;
- making platform ranking the final provider decision;
- centralizing all organizational knowledge;
- requiring shared pricing;
- making Product access conditional on surrendering private data;
- using common identity to erase organization identity;
- preventing organization-specific rules merely because they differ from defaults.

---

## 5. Human Professional Accountability

### Principle

> Human professionals remain accountable for professional judgment, review, approval, and protected action.

### Why it exists

MarkOrbit operates in professional services.

Many actions carry legal, financial, evidentiary, reputational, and professional consequences.

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
- what AI support was used;
- what evidence informed the decision.

Human Review must remain distinct from:

- AI output;
- automated validation;
- Product confirmation;
- Workflow completion;
- system confidence.

Protected actions require appropriate human authority.

Examples include filing, submission, payment, provider appointment, external Communication send, legal-position approval, and official recordal.

### What would violate it

Violations include:

- allowing AI confidence to substitute for review;
- treating user inactivity as approval;
- allowing a Product button to bypass professional authorization;
- attributing an AI-generated conclusion to a human who did not review it;
- allowing an AI Agent to file, send, appoint, or pay autonomously;
- obscuring who made the final decision;
- recording “system approved” without an accountable authority.

---

## 6. Candidate Before Canonical

### Principle

> Derived outputs must remain candidates until professional validation and governance promote them into approved or canonical states.

### Why it exists

MarkOrbit may produce:

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
- recommendations.

These outputs may be valuable.

They are not automatically authoritative.

Without a candidate stage, the system may silently convert extraction into knowledge, recommendation into decision, draft into approval, or match into appointment.

### What it requires

A conforming Workplace must preserve distinctions such as:

```text
Structured Information ≠ verified Knowledge

Knowledge Candidate ≠ Canonical Knowledge

Capability Candidate ≠ approved Capability

Skill Candidate ≠ enabled Skill

Workflow Fragment ≠ executable Workflow

Task Suggestion ≠ formal Task

Opportunity Candidate ≠ formal Opportunity

AI Draft ≠ approved professional output
```

Candidate records should retain source, provenance, generating method, confidence, version, reviewer, and validation status.

Promotion must be explicit.

### What would violate it

Violations include:

- inserting AI output directly into approved knowledge;
- creating formal Tasks from suggestions without acceptance;
- treating extracted rules as canonical;
- converting provider evidence into a final rating automatically;
- publishing Artifact drafts without review;
- hiding candidate status in the interface;
- losing the source or version of a candidate.

---

## 7. Governed Execution Before Protected Action

### Principle

> Any protected action must pass through governed Execution, required review, and the proper Owning Service.

### Why it exists

Professional systems often confuse preparation with action.

A filing package may be complete.

A recommendation may be persuasive.

A provider may appear suitable.

A payment may be calculated.

None of those facts means the protected action may proceed.

Protected actions require identity, permission, policy, completeness, Human Review, approval, trace, and formal mutation authority.

### What it requires

A conforming Workplace must hand protected work into governed Execution.

The expected interaction pattern is:

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

Execution governs Tasks, reviews, approvals, Communication boundaries, protected-action gates, retries, safe failure, Events, and audit.

The proper Owning Service records the formal fact.

### What would violate it

Violations include:

- allowing a recommendation to trigger filing automatically;
- treating document completion as approval;
- allowing a Product interface to mutate protected state directly;
- allowing an AI Agent to send Communications;
- recording provider appointment before authorization;
- treating fee calculation as payment approval;
- bypassing review because the Workflow is familiar;
- hiding failed protected actions;
- retrying without idempotency or audit.

---

## 8. Evidence, Provenance, and Audit

### Principle

> Professional outputs, recommendations, decisions, and state changes must remain traceable to their evidence, source, version, actor, and authority.

### Why it exists

Professional work must be explainable.

A user should be able to ask:

```text
Why was this recommended?

Which data and rule were used?

Which version was active?

Who prepared and reviewed it?

What did AI contribute?

Which Product initiated the work?

Which Owning Service changed the state?

What happened after approval?
```

Without evidence and provenance, the system may produce plausible results that cannot be trusted, corrected, defended, or learned from.

### What it requires

A conforming Workplace should preserve, where relevant:

- source identifiers and versions;
- timestamps;
- organization and actor identity;
- Product origin;
- AI Agent or model role;
- Skill and policy versions;
- reviewer and approval;
- state transition;
- Owning Service;
- Artifact version;
- delivery or failure result.

The system should distinguish:

```text
AI suggested

Human reviewed

Execution coordinated

Owning Service recorded
```

### What would violate it

Violations include:

- storing only the final output;
- losing the source behind a recommendation;
- overwriting prior versions;
- recording approval without the approver;
- allowing unaudited AI mutation;
- hiding failed attempts;
- merging human and AI contributions into one anonymous result;
- deleting evidence needed to explain a professional decision.

---

## 9. Product Loop First, Shared Platform Extraction Second

### Principle

> Product value loops should be validated before responsibilities are extracted into shared platform services.

### Why it exists

Architecture can become speculative.

Teams may design universal services, generic registries, shared APIs, or platform abstractions before real Product behavior has been validated.

This creates premature complexity.

MarkOrbit should first prove value through concrete Product loops.

Examples include:

```text
Lite:
Today → Recommendation → Prepared Action → Confirmation → Handoff

MarkReg:
Need → Recommendation → Intake → Filing Preparation

MGSN:
Need → Candidate Discovery → Human Selection → Collaboration
```

Repeated and stable needs may then justify shared extraction.

### What it requires

A conforming architecture should:

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

### What would violate it

Violations include:

- building a universal Workflow engine before Product loops are proven;
- forcing Lite and MarkReg into one Product model;
- creating repositories for every logical concept;
- extracting a capability before ownership is understood;
- using platform elegance as a substitute for user value;
- redesigning Products around speculative abstractions.

---

## 10. Evolution Without Forced Replacement

### Principle

> MarkOrbit should allow organizations, Workplaces, Products, Skills, and relationships to evolve without requiring destructive replacement.

### Why it exists

Professional systems accumulate value through:

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

A new Product, Skill, AI Agent, or network capability should strengthen that accumulated value rather than reset it.

### What it requires

A conforming Workplace should support:

- versioned change;
- migration;
- coexistence;
- gradual adoption;
- rollback where appropriate;
- preservation of history;
- replacement of a Skill without replacing the Capability;
- replacement of a Product without replacing the Workplace;
- addition of a provider without deleting trust history;
- Product embedding without organizational centralization;
- local and cloud evolution under explicit policy.

The principle is:

```text
Replace implementation when necessary.

Preserve organizational continuity.
```

### What would violate it

Violations include:

- requiring data reset for Product upgrades;
- tying organization identity to one Product;
- deleting history when a provider changes;
- requiring one deployment model for every Workplace;
- forcing all organizations onto the same operating model;
- replacing Capability identity when only a Skill changes;
- making migration conditional on surrendering private data;
- using innovation as justification for centralization.

---

## 11. How the Principles Work Together

The principles reinforce one another.

Organizational autonomy requires authorized context.

Authorized context requires privacy and purpose limitation.

Candidate-before-canonical requires Human Review.

Human accountability requires governed Execution.

Governed Execution requires explicit mutation authority.

Evidence and provenance allow review, correction, and learning.

Product-loop discipline prevents premature platform centralization.

Versioning and continuity allow the ecosystem to evolve without forcing organizations to discard accumulated capability.

The principles should therefore be reviewed as one constitutional system, not as optional checkboxes.

---

## 12. Principle-to-Violation Matrix

| Principle | What it protects | Typical violation |
|---|---|---|
| Organizational Autonomy | Clients, data, knowledge, rules, relationships, and commercial control | Platform becomes owner of the client or provider relationship |
| Authorized Context | Correct identity, permission, purpose, and scope | Product or AI uses broad context without purpose |
| Private and Local by Default | Confidentiality and organizational control | Local or private data is synchronized automatically |
| Shared Foundations Without Central Ownership | Interoperability without organizational absorption | Shared infrastructure claims organization assets |
| Human Professional Accountability | Professional judgment and responsibility | AI or system confidence substitutes for review |
| Candidate Before Canonical | Validation and governance | Draft, extraction, or recommendation becomes approved fact |
| Governed Execution Before Protected Action | Safe operational control | Product or AI Agent performs protected action directly |
| Evidence, Provenance, and Audit | Explainability and traceability | Final result is stored without source, version, or reviewer |
| Product Loop First, Shared Platform Extraction Second | User value and disciplined architecture | Generic services are built before Product validation |
| Evolution Without Forced Replacement | Organizational continuity | Upgrade requires destructive migration or loss of history |

This matrix is suitable for future conformance review.

It is not a substitute for detailed Product or implementation acceptance criteria.

---

## 13. Minimum Principle Lock

Every MarkOrbit Workplace must preserve the following lock:

```text
The organization remains independent.

Context is explicitly authorized.

Private information remains private or local by default.

Shared foundations do not become central ownership.

Human professionals remain accountable.

Candidates do not become canonical without validation.

Protected action enters governed Execution.

Evidence, provenance, and audit remain visible.

Product loops are validated before shared extraction.

Evolution preserves organizational continuity.
```

A system may be technically impressive and still fail this lock.

A system that fails the lock is not a conforming MarkOrbit Workplace.

---

## 14. Chapter Boundary

These principles do not define:

- Product screen layouts;
- database schemas;
- API payloads;
- service topology;
- deployment architecture;
- synchronization protocols;
- scoring or ranking formulas;
- AI model selection;
- exact Workflow definitions;
- exact permission matrices;
- Product pricing;
- provider contracting;
- production readiness.

Those decisions belong to later architecture specifications, Product charters, implementation ADRs, and repositories.

This chapter also does not modify Core semantics, redefine Execution, or authorize autonomous protected action.

Its purpose is to define what every future Workplace design must preserve.

---

## 15. Chapter Conclusion

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

They do not dictate one technical form.

They preserve one constitutional outcome:

> Every professional organization remains an independent Orbit, operates within authorized context, consumes shared capabilities under governance, and remains accountable for the professional work performed in its name.
