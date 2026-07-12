# Object Index

**Repository:** `book-02-core`  
**Directory:** `indexes/`  
**Index ID:** B02-IDX-OBJECT  
**Source Appendix:** B02-APP-C — Core Object Index  
**Related Appendices:** B02-APP-A — Glossary; B02-APP-B — Core Domain Index  
**Stage:** Second Canonical Draft  
**Status:** Draft  
**Version:** 0.1.0  
**Owner:** MarkOrbit Publications Editorial Board  

---

# 1. Index Purpose

This index operationalizes **B02-APP-C — Core Object Index**.

The appendix is the canonical manuscript reference.

This file is the implementation-ready object index used by:

```text
core-specs/objects/
core-specs/domains/
core-specs/services/
core-specs/events/
core-specs/contracts/
core-specs/api/
core-specs/agents/
codex-tasks/
validation scripts
```

This index does not create database schemas.

It defines Core Objects as professional meaning units that later specifications may convert into data contracts, service contracts, event payloads, APIs and implementation artifacts.

---

# 2. Canonical Object Rule

Book 02 uses the following canonical rule:

```text
A Core Object is professional meaning before data structure.
Every Core Object must have an owning Core Domain or an explicitly declared cross-cutting specification system.
```

Therefore:

```text
No owner, no Core Object.
No professional meaning, no Core Object.
No lifecycle, no Core Object.
No service or contract relationship, no implementation-ready object.
```

---

# 3. Object vs Data Structure

A Core Object is not automatically:

```text
a database table
a DTO
a UI form
a JSON blob
a spreadsheet row
an API response
a third-party payload
```

A Core Object may later be represented by those artifacts, but it must first have:

```text
Core meaning
owning domain
lifecycle
responsibility boundary
relationship to services
relationship to events
relationship to contracts
relationship to consumers
validation rules
```

---

# 4. Object Index Fields

Each object entry should include the following fields.

```text
Object ID
Object Name
Object Category
Owning Domain or System
MVP Phase
MVP Depth
Core Meaning
Lifecycle
Primary Services
Primary Events
Primary Contracts
Related Objects
AI Usage
Workflow Usage
API Exposure
Product Consumers
Deferred Scope
Validation Notes
```

---

# 5. Object Categories

This index uses the following object categories.

```text
Foundation Object
Professional Object
Business Execution Object
Execution Primitive Object
Collaboration Network Object
Contract Object
Governance Object
AI Governance Object
Cross-Cutting Object
Codex Object
```

## 5.1 Non-Object Specification Categories

Book 02 also recognizes specification categories that are not Core Objects:

- **Controlled State Value Specification** — has no independent identity; is owned by a parent object or contract; defines legal values and semantics; may be versioned; may define transition constraints; cannot mutate independently; cannot become an aggregate root.
- **Workflow Contract Component** — exists inside Workflow Contract; may define structure and validation; does not execute independently; does not own business state; does not directly call external actions; is not defined by Product UI.
- **Contract** — defines exchange, validation or obligation shape for objects, services, events, APIs or workflows.
- **Event** — records meaningful changes or outcomes without owning the changed state.
- **Service** — owns governed actions and mutations; objects and components do not mutate themselves.

A controlled value set is not automatically a Core Object.
A workflow component is not automatically a Core Object.
No independent identity means no independent Core Object.
No separate source of truth means no independent Core Object.

---

# 6. MVP Depth Vocabulary

```text
Must Implement
Partial Implement
Reserved Boundary
Deferred
```

A Core Object marked `Must Implement` is required for the first executable Core kernel.

A Core Object marked `Partial Implement` requires baseline specification and limited execution.

A Core Object marked `Reserved Boundary` is recognized but should not be deeply implemented in MVP.

A Core Object marked `Deferred` belongs to future releases.

---

# 7. Object Index Summary

## 7.1 Foundation Object Summary

| Object ID | Object Name | Owning Domain/System | MVP Phase | MVP Depth |
|----------|-------------|----------------------|-----------|-----------|
| OBJ-ID-001 | Identity | Identity | Phase 1 | Must Implement |
| OBJ-ID-002 | Actor | Identity | Phase 1 | Must Implement |
| OBJ-ID-003 | System Identity | Identity | Phase 1 | Partial Implement |
| OBJ-ID-004 | AI Agent Identity | Identity / AI Governance | Phase 1 / 4 | Must Implement |
| OBJ-ORG-001 | Organization | Organization | Phase 1 | Must Implement |
| OBJ-ORG-002 | Organization Unit | Organization | Phase 1 | Partial Implement |
| OBJ-ORG-003 | Organization Membership | Organization | Phase 1 | Must Implement |
| OBJ-USER-001 | User | User | Phase 1 | Must Implement |
| OBJ-USER-002 | User Profile | User | Phase 1 | Must Implement |
| OBJ-USER-003 | User Role Assignment | User / Permission | Phase 1 | Must Implement |
| OBJ-PERM-001 | Permission Rule | Permission | Phase 1 | Must Implement |
| OBJ-PERM-002 | Access Scope | Permission | Phase 1 | Must Implement |
| OBJ-PERM-003 | Role Permission | Permission | Phase 1 | Must Implement |
| OBJ-POL-001 | Policy Rule | Policy | Phase 1 | Partial Implement |
| OBJ-POL-002 | Review Policy | Policy / Business Responsibility | Phase 1 / 3 | Partial Implement |
| OBJ-POL-003 | AI Risk Policy | Policy / AI Governance | Phase 4 | Must Implement |
| OBJ-KNO-001 | Knowledge Source | Knowledge | Phase 1 | Must Implement |
| OBJ-KNO-002 | Knowledge Asset | Knowledge | Phase 1 | Must Implement |
| OBJ-KNO-003 | Knowledge Rule | Knowledge | Phase 1 | Partial Implement |
| OBJ-KNO-004 | Knowledge Gap | Knowledge | Phase 1 | Partial Implement |
| OBJ-KNO-005 | Knowledge Citation | Knowledge | Phase 1 | Must Implement |

## 7.2 Professional Object Summary

| Object ID | Object Name | Owning Domain/System | MVP Phase | MVP Depth |
|----------|-------------|----------------------|-----------|-----------|
| OBJ-BRD-001 | Brand | Brand | Phase 2 | Must Implement |
| OBJ-BRD-002 | Brand Owner | Brand | Phase 2 | Must Implement |
| OBJ-BRD-003 | Brand Asset Reference | Brand | Phase 2 | Partial Implement |
| OBJ-BRD-004 | Brand Market Context | Brand | Phase 2 | Partial Implement |
| OBJ-TM-001 | Trademark | Trademark | Phase 2 | Must Implement |
| OBJ-TM-002 | Trademark Owner | Trademark | Phase 2 | Must Implement |
| OBJ-TM-004 | Trademark GoodsServices | Trademark / Classification | Phase 2 | Must Implement |
| OBJ-TM-005 | Trademark Image Reference | Trademark / Document | Phase 2 | Partial Implement |
| OBJ-TM-006 | Trademark Lifecycle Record | Trademark | Phase 2 | Must Implement |
| OBJ-JUR-001 | Jurisdiction | Jurisdiction | Phase 2 | Must Implement |
| OBJ-JUR-002 | Trademark Office | Jurisdiction | Phase 2 | Must Implement |
| OBJ-JUR-003 | Jurisdiction Requirement | Jurisdiction | Phase 2 | Must Implement |
| OBJ-JUR-004 | Jurisdiction Rule | Jurisdiction / Policy | Phase 2 | Partial Implement |
| OBJ-CLS-001 | Classification | Classification | Phase 2 | Must Implement |
| OBJ-CLS-002 | Class | Classification | Phase 2 | Must Implement |
| OBJ-CLS-003 | GoodsServices Term | Classification | Phase 2 | Must Implement |
| OBJ-CLS-004 | Classification Recommendation | Classification / AI Governance | Phase 2 / 4 | Must Implement |
| OBJ-CLS-005 | Classification Review Record | Classification / Business Responsibility | Phase 2 / 3 | Must Implement |
| OBJ-DOC-001 | Document | Document | Phase 2 | Must Implement |
| OBJ-DOC-002 | Document Requirement | Document / Jurisdiction | Phase 2 | Must Implement |
| OBJ-DOC-003 | Document Draft | Document / AI Governance | Phase 2 / 4 | Partial Implement |
| OBJ-DOC-004 | Document Version | Document | Phase 2 | Partial Implement |
| OBJ-DOC-005 | Document Metadata | Document | Phase 2 | Must Implement |
| OBJ-EVD-001 | Evidence | Evidence | Phase 2 | Partial Implement |
| OBJ-EVD-002 | Evidence Package | Evidence | Phase 2 | Partial Implement |
| OBJ-EVD-003 | Evidence Review Note | Evidence / AI Governance | Phase 2 / 4 | Partial Implement |
| OBJ-EVD-004 | Evidence Source | Evidence | Phase 2 | Partial Implement |

## 7.3 Business Execution Object Summary

| Object ID | Object Name | Owning Domain/System | MVP Phase | MVP Depth |
|----------|-------------|----------------------|-----------|-----------|
| OBJ-CUS-001 | Customer | Customer | Phase 3 | Must Implement |
| OBJ-CUS-002 | Customer Contact | Customer | Phase 3 | Must Implement |
| OBJ-CUS-003 | Customer Organization Link | Customer / Organization | Phase 3 | Must Implement |
| OBJ-CUS-004 | Customer Service Context | Customer | Phase 3 | Partial Implement |
| OBJ-ORD-001 | Order | Order | Phase 3 | Must Implement |
| OBJ-ORD-002 | Order Item | Order | Phase 3 | Must Implement |
| OBJ-ORD-003 | Order Requirement | Order | Phase 3 | Must Implement |
| OBJ-ORD-005 | Order-to-Matter Link | Order / Matter | Phase 3 | Must Implement |
| OBJ-MAT-001 | Matter | Matter | Phase 3 | Must Implement |
| OBJ-MAT-003 | Matter Participant | Matter | Phase 3 | Must Implement |
| OBJ-MAT-004 | Matter Context | Matter | Phase 3 | Must Implement |
| OBJ-MAT-005 | Matter Timeline | Matter / Event | Phase 3 | Partial Implement |
| OBJ-WFC-001 | Workflow Contract | Workflow Contract | Phase 3 | Must Implement |
| OBJ-WFC-004 | Workflow Rule | Workflow Contract / Policy | Phase 3 | Partial Implement |
| OBJ-TSK-001 | Task | Task | Phase 3 | Must Implement |
| OBJ-TSK-002 | Task Assignment | Task / Business Responsibility | Phase 3 | Must Implement |
| OBJ-TSK-004 | Task Review Link | Task / Business Responsibility | Phase 3 | Must Implement |
| OBJ-EVT-001 | Event | Event | Phase 3 | Must Implement |
| OBJ-EVT-002 | Event Payload | Event | Phase 3 | Must Implement |
| OBJ-EVT-003 | Event Subscription | Event | Phase 3 | Partial Implement |
| OBJ-EVT-004 | Event Audit Reference | Event / AI Governance | Phase 3 / 4 | Must Implement |
| OBJ-NOT-001 | Notification | Notification | Phase 3 | Partial Implement |
| OBJ-NOT-002 | Notification Rule | Notification / Policy | Phase 3 | Partial Implement |
| OBJ-NOT-003 | Notification Recipient | Notification | Phase 3 | Partial Implement |
| OBJ-NOT-004 | Notification Delivery Record | Notification | Phase 3 | Partial Implement |
| OBJ-OPP-001 | Opportunity | Opportunity | Phase 4 | Partial Implement |
| OBJ-OPP-002 | Opportunity Signal | Opportunity / AI Governance | Phase 4 | Partial Implement |
| OBJ-OPP-003 | Opportunity Recommendation | Opportunity / AI Governance | Phase 4 | Reserved Boundary |
| OBJ-OPP-004 | Opportunity Follow-up | Opportunity / Task | Phase 4 | Partial Implement |

## 7.4 Collaboration Network Object Summary

| Object ID | Object Name | Owning Domain/System | MVP Phase | MVP Depth |
|----------|-------------|----------------------|-----------|-----------|
| OBJ-PRT-001 | Partner | Partner | Phase 5 | Reserved Boundary |
| OBJ-PRT-002 | Partner Relationship | Partner | Phase 5 | Reserved Boundary |
| OBJ-PRT-003 | Partner Capability Link | Partner / Capability | Phase 5 | Reserved Boundary |
| OBJ-AGT-001 | Agent | Agent | Phase 4 | Partial Implement |
| OBJ-AGT-002 | Agent Organization | Agent / Organization | Phase 4 | Partial Implement |
| OBJ-AGT-003 | Agent Jurisdiction Coverage | Agent / Jurisdiction | Phase 4 | Partial Implement |
| OBJ-AGT-004 | Agent Capability | Agent / Capability | Phase 4 | Partial Implement |
| OBJ-AGT-005 | Agent Contact | Agent / Communication | Phase 4 | Partial Implement |
| OBJ-SP-001 | Service Provider | Service Provider | Phase 4 | Partial Implement |
| OBJ-SP-002 | Service Provider Capability | Service Provider / Capability | Phase 4 | Partial Implement |
| OBJ-SP-003 | Service Provider Coverage | Service Provider / Jurisdiction | Phase 4 | Partial Implement |
| OBJ-SN-001 | Service Network | Service Network | Phase 5 | Reserved Boundary |
| OBJ-SN-002 | Network Membership | Service Network | Phase 5 | Reserved Boundary |
| OBJ-SN-003 | Network Rule | Service Network / Policy | Phase 5 | Reserved Boundary |
| OBJ-RT-001 | Routing Decision | Routing | Phase 4 | Partial Implement |
| OBJ-RT-002 | Routing Candidate | Routing / Service Provider | Phase 4 | Partial Implement |
| OBJ-RT-003 | Routing Rule | Routing / Policy | Phase 4 | Partial Implement |
| OBJ-RT-004 | Routing Review Record | Routing / Business Responsibility | Phase 4 | Partial Implement |
| OBJ-COMM-001 | Communication | Communication | Phase 4 | Partial Implement |
| OBJ-COMM-002 | Communication Thread | Communication | Phase 4 | Partial Implement |
| OBJ-COMM-003 | Communication Summary | Communication / AI Governance | Phase 4 | Partial Implement |
| OBJ-COMM-004 | Communication Action Item | Communication / Task | Phase 4 | Partial Implement |

## 7.5 Cross-Cutting and Governance Object Summary

| Object ID | Object Name | Owning Domain/System | MVP Phase | MVP Depth |
|----------|-------------|----------------------|-----------|-----------|
| OBJ-CAP-001 | Capability | Capability | Phase 1 | Partial Implement |
| OBJ-CAP-002 | Capability Provider | Capability | Phase 1 | Partial Implement |
| OBJ-CAP-003 | Capability Scope | Capability | Phase 1 | Partial Implement |
| OBJ-CAP-004 | Capability Requirement | Capability | Phase 1 | Partial Implement |
| OBJ-BR-001 | Responsibility Assignment | Business Responsibility | Phase 3 | Must Implement |
| OBJ-BR-002 | Review Record | Business Responsibility | Phase 3 | Must Implement |
| OBJ-BR-003 | Approval Record | Business Responsibility | Phase 3 | Must Implement |
| OBJ-BR-004 | Escalation Rule | Business Responsibility / Policy | Phase 3 | Partial Implement |
| OBJ-AI-001 | AI Agent | AI Governance | Phase 4 | Must Implement |
| OBJ-AI-002 | Agent Contract | AI Governance | Phase 4 | Must Implement |
| OBJ-AI-003 | AI Output | AI Governance | Phase 4 | Must Implement |
| OBJ-AI-004 | AI Recommendation | AI Governance | Phase 4 | Must Implement |
| OBJ-AI-005 | AI Audit Record | AI Governance | Phase 4 | Must Implement |
| OBJ-AI-006 | AI Draft | AI Governance / Document | Phase 4 | Partial Implement |
| OBJ-CX-001 | Codex Task | Codex Task System | Wave 0 | Must Implement |
| OBJ-CX-002 | Spec File | Specification Governance | Wave 0 | Must Implement |
| OBJ-CX-003 | Test Fixture | Specification Governance | Wave 0 | Must Implement |
| OBJ-CX-004 | Implementation Artifact | Codex Task System | Wave 0–7 | Partial Implement |

## 7.6 Reclassified Legacy Status and Workflow Entries

The following legacy IDs are retained as historical references only. They are not active independent identity-bearing Core Objects and must not be reassigned.

| Legacy ID | Existing Name | Canonical Classification | Parent / Owner | Status | Canonical specification |
|-----------|---------------|--------------------------|----------------|--------|-------------------------|
| OBJ-TM-003 | Trademark Status | Controlled State Value Specification | Trademark | Reclassified | [controlled-state-values/trademark-status-values.md](../core-specs/controlled-state-values/trademark-status-values.md) |
| OBJ-ORD-004 | Order Status | Controlled State Value Specification | Order | Reclassified | [controlled-state-values/order-status-values.md](../core-specs/controlled-state-values/order-status-values.md) |
| OBJ-MAT-002 | Matter Status | Controlled State Value Specification | Matter | Reclassified | [controlled-state-values/matter-status-values.md](../core-specs/controlled-state-values/matter-status-values.md) |
| OBJ-WFC-002 | Workflow State | Workflow Contract Component | Workflow Contract | Reclassified | [workflows/components/workflow-state-definition.md](../core-specs/workflows/components/workflow-state-definition.md) |
| OBJ-WFC-003 | Workflow Transition | Workflow Contract Component | Workflow Contract | Reclassified | [workflows/components/workflow-transition-definition.md](../core-specs/workflows/components/workflow-transition-definition.md) |
| OBJ-TSK-003 | Task Status | Controlled State Value Specification | Task | Reclassified | [controlled-state-values/task-status-values.md](../core-specs/controlled-state-values/task-status-values.md) |

Active Must Implement object inventory excludes these six legacy entries. The first executable Core kernel must implement their parent fields or Workflow Contract structures, not standalone aggregate roots.

---

# 8. High-Priority MVP Objects

The following objects form the minimum object baseline for the first executable Core kernel.

```text
Identity
Actor
AI Agent Identity
Organization
Organization Membership
User
User Profile
User Role Assignment
Permission Rule
Access Scope
Knowledge Source
Knowledge Asset
Knowledge Citation
Brand
Brand Owner
Trademark
Trademark Owner
Trademark GoodsServices
Trademark Lifecycle Record
Jurisdiction
Trademark Office
Jurisdiction Requirement
Classification
Class
GoodsServices Term
Classification Recommendation
Classification Review Record
Document
Document Requirement
Document Metadata
Customer
Customer Contact
Order
Order Item
Order Requirement
Order-to-Matter Link
Matter
Matter Participant
Matter Context
Workflow Contract
Task
Task Assignment
Task Review Link
Event
Event Payload
Event Audit Reference
Responsibility Assignment
Review Record
Approval Record
AI Agent
Agent Contract
AI Output
AI Recommendation
AI Audit Record
Codex Task
Spec File
Test Fixture
```

---

# 9. Object Ownership Rules

## 9.1 Single Primary Owner

Each Core Object must have one primary owning domain or cross-cutting system.

## 9.2 Secondary Relationships Allowed

An object may be related to other domains, but secondary relationships do not change ownership.

Example:

```text
Classification Recommendation
    Primary Owner: Classification
    Related System: AI Governance
```

## 9.3 Cross-Cutting Ownership Must Be Explicit

Objects owned by Capability, Business Responsibility, AI Governance or Codex Task System must be explicitly marked.

## 9.4 Product Ownership Is Not Core Ownership

Objects owned only by products are not Core Objects.

Examples that should not be added here without Core justification:

```text
Lite Form Screen
MarkReg Dashboard Card
Partner Center Menu
Client Portal Widget
```

---

# 10. Object-to-Service Handoff

Objects become executable through Core Services.

Examples:

| Object | Required Service |
|--------|------------------|
| Identity | Identity Registration Service |
| Permission Rule | Permission Check Service |
| Knowledge Asset | Knowledge Asset Validation Service |
| Trademark | Trademark Registration Service |
| Classification Recommendation | Classification Recommendation Service |
| Document | Document Upload Service |
| Order | Order Creation Service |
| Matter | Matter Creation Service |
| Workflow Contract | Workflow Contract Registration Service |
| Task | Task Creation Service |
| Event | Event Publication Service |
| Responsibility Assignment | Responsibility Assignment Service |
| AI Output | AI Output Registration Service |
| Agent Contract | Agent Contract Validation Service |
| Codex Task | Codex Task Registration Service |

A Core Object must not mutate itself.

State changes must occur through governed Core Services.

---

# 11. Object-to-Event Handoff

Objects produce meaningful state changes captured by Core Events.

Examples:

| Object | Event |
|--------|-------|
| Identity | IdentityCreated |
| Organization | OrganizationCreated |
| User | UserCreated |
| Permission Rule | PermissionGranted |
| Knowledge Asset | KnowledgeAssetValidated |
| Brand | BrandCreated |
| Trademark | TrademarkStatusChanged |
| Classification Recommendation | ClassificationRecommendationGenerated |
| Document | DocumentUploaded |
| Evidence Package | EvidenceReviewRequired |
| Customer | CustomerCreated |
| Order | OrderConfirmed |
| Matter | MatterStatusChanged |
| Workflow Contract transition definitions | WorkflowTransitionRequested |
| Task | TaskCompleted |
| Notification | NotificationSent |
| Opportunity Signal | OpportunitySignalDetected |
| Routing Decision | RoutingDecisionMade |
| Communication Summary | CommunicationSummaryGenerated |
| Responsibility Assignment | ResponsibilityAssigned |
| AI Output | AIOutputGenerated |
| AI Audit Record | AIAuditRecordCreated |
| Codex Task | CodexTaskImplemented |

---

# 12. Object-to-Contract Handoff

Each implementation-ready object should have at least one related contract.

Contract types include:

```text
Data Contract
API Contract
Event Contract
Workflow Contract
Agent Contract
Review Contract
Permission Contract
Policy Contract
Codex Task Contract
```

Examples:

| Object | Contract |
|--------|----------|
| Identity | Identity Data Contract |
| User | User API Contract |
| Permission Rule | Permission Contract |
| Knowledge Asset | AI Knowledge Authorization Contract |
| Trademark | Trademark Data Contract |
| Classification Recommendation | Classification Recommendation API Contract |
| Document | Document Data Contract |
| Order | Order API Contract |
| Matter | Matter Workflow Contract |
| Task | Task Event Contract |
| AI Agent | Agent Contract |
| AI Output | AI Output Contract |
| Review Record | Review Contract |
| Codex Task | Codex Task Contract |

---

# 13. AI Governance Object Rules

AI-related objects must not be optional if AI is used.

AI governance requires:

```text
AI Agent
Agent Contract
AI Output
AI Recommendation
AI Audit Record
Review Record
Authorized Knowledge Source
Permission Rule
Policy Rule
```

AI output must not be treated as final professional truth unless it has the required review status.

Allowed AI output statuses:

```text
Draft
Recommendation
ReviewRequired
ReviewApproved
ReviewRejected
Expired
Superseded
```

---

# 14. Codex Object Rules

Codex-related objects exist to keep implementation controlled.

Required Codex objects:

```text
Codex Task
Spec File
Test Fixture
Implementation Artifact
Acceptance Criteria
Validation Report
```

Codex objects must reference approved source specifications.

Codex must not create new Core Objects without an approved update to this index.

---

# 15. Validation Rules

The object index must pass the following validation checks.

```text
[ ] Every object has an Object ID.
[ ] Every object has a name.
[ ] Every object has an owning domain or cross-cutting system.
[ ] Every object has MVP phase or wave.
[ ] Every object has MVP depth.
[ ] Every object has a category.
[ ] Every Must Implement object has at least one related service.
[ ] Every Must Implement object has at least one related event or explicit no-event reason.
[ ] Every AI object has an audit or review requirement.
[ ] Every Codex object has a source specification requirement.
[ ] No object is owned by a product only.
[ ] No object is only a database table.
[ ] No object is only a UI component.
[ ] No object silently changes the 26-domain baseline.
```

---

# 16. Prohibited Object Changes

This index must not be changed to:

```text
turn database tables into Core Objects without meaning definition
add product screens as Core Objects
add DTOs as Core Objects without canonical object ownership
create unowned objects
create AI outputs without audit
create AI agents without Agent Contract
treat Capability as an ordinary baseline domain
treat Business Responsibility as an ordinary baseline domain
merge objects across domains without architecture review
rename canonical objects without architecture review
implement deferred objects as MVP without approval
```

---

# 17. Handoff to core-specs/objects/

This index will generate future files under:

```text
core-specs/objects/
```

Expected scaffold:

```text
core-specs/objects/README.md
core-specs/objects/_template.md
core-specs/objects/foundation/
core-specs/objects/professional/
core-specs/objects/business-execution/
core-specs/objects/collaboration-network/
core-specs/objects/cross-cutting/
core-specs/objects/ai-governance/
core-specs/objects/codex/
```

Initial detailed object specs should prioritize:

```text
identity.md
user.md
organization.md
permission-rule.md
knowledge-source.md
knowledge-asset.md
trademark.md
jurisdiction.md
classification-recommendation.md
document.md
customer.md
order.md
matter.md
workflow-contract.md
task.md
event.md
responsibility-assignment.md
review-record.md
ai-agent.md
agent-contract.md
ai-output.md
ai-audit-record.md
codex-task.md
```

---

# 18. Handoff to service-index.md

The next index should be checked against this object index.

```text
indexes/service-index.md
```

Each Core Service must specify:

```text
objects read
objects created
objects updated
objects linked
objects validated
objects emitted through events
```

A service without related objects is not implementation-ready.

---

# 19. Acceptance Criteria

This index is accepted only if it satisfies the following criteria.

```text
[ ] It defines Core Object as professional meaning before data structure.
[ ] It distinguishes Core Object from table, DTO, API response and UI record.
[ ] It defines object index fields.
[ ] It lists Foundation Objects.
[ ] It lists Professional Objects.
[ ] It lists Business Execution Objects.
[ ] It lists Collaboration Network Objects.
[ ] It lists Cross-Cutting Objects.
[ ] It lists AI Governance Objects.
[ ] It lists Codex Objects.
[ ] It identifies high-priority MVP Objects.
[ ] It defines object ownership rules.
[ ] It maps objects to services.
[ ] It maps objects to events.
[ ] It maps objects to contracts.
[ ] It preserves AI governance requirements.
[ ] It preserves Codex source-spec requirements.
[ ] It defines validation rules.
[ ] It defines prohibited object changes.
[ ] It prepares core-specs/objects/.
[ ] It hands off to service-index.md.
```

---

# 20. Revision Notes

| Version | Status | Notes |
|---------|--------|-------|
| 0.1.0 | Draft | Initial operational Object Index derived from B02-APP-C. Defines object ownership, MVP depth, object categories, AI governance objects, Codex objects, service/event/contract handoff and validation rules. |

---

**End of Index**
