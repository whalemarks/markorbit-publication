# Service Index

**Repository:** `book-02-core`  
**Directory:** `indexes/`  
**Index ID:** B02-IDX-SERVICE  
**Source Appendix:** B02-APP-D — Core Service Index  
**Related Appendices:** B02-APP-A — Glossary; B02-APP-B — Core Domain Index; B02-APP-C — Core Object Index  
**Stage:** Second Canonical Draft  
**Status:** Draft  
**Version:** 0.1.0  
**Owner:** MarkOrbit Publications Editorial Board  

---

# 1. Index Purpose

This index operationalizes **B02-APP-D — Core Service Index**.

The appendix is the canonical manuscript reference.

This file is the implementation-ready service index used by:

```text
core-specs/services/
core-specs/objects/
core-specs/events/
core-specs/contracts/
core-specs/api/
core-specs/agents/
codex-tasks/
validation scripts
```

This index does not define product UI actions.

It defines governed Core Services that operate Core meaning through objects, contracts, events, permissions, policies, review rules and audit requirements.

---

# 2. Canonical Service Rule

Book 02 uses the following canonical rule:

```text
A Core Service is a governed capability that operates Core meaning.
```

Therefore:

```text
No owning domain or system, no Core Service.
No Core Object relationship, no implementation-ready service.
No permission or policy boundary, no safe service.
No event or explicit no-event reason, no execution trace.
No contract, no consumption surface.
```

---

# 3. Service vs UI Action

A Core Service is not automatically:

```text
a UI button
a menu item
a controller method
a helper function
a third-party API wrapper
a database operation
a background job
a prompt
```

A Core Service may later be exposed through those artifacts, but it must first have:

```text
owning domain or cross-cutting system
purpose
input contract
output contract
objects read
objects created or updated
events emitted
permission requirements
policy requirements
review requirements
audit requirements
consumer boundary
failure behavior
```

---

# 4. Service Index Fields

Each service entry should include the following fields.

```text
Service ID
Service Name
Service Category
Owning Domain or System
MVP Phase
MVP Depth
Purpose
Inputs
Outputs
Objects Read
Objects Created
Objects Updated
Objects Linked
Events Emitted
Contracts Required
Permission Requirement
Policy Requirement
Review Requirement
Audit Requirement
AI Usage
Workflow Usage
API Exposure
Product Consumers
Deferred Scope
Validation Notes
```

---

# 5. Service Categories

This index uses the following service categories.

```text
Foundation Service
Professional Service
Business Execution Service
Execution Primitive Service
Collaboration Network Service
Cross-Cutting Service
AI Governance Service
Codex Service
Validation Service
```

---

# 6. MVP Depth Vocabulary

```text
Must Implement
Partial Implement
Reserved Boundary
Deferred
```

A Core Service marked `Must Implement` is required for the first executable Core kernel.

A Core Service marked `Partial Implement` requires baseline specification and limited execution.

A Core Service marked `Reserved Boundary` is recognized but should not be deeply implemented in MVP.

A Core Service marked `Deferred` belongs to future releases.

---

# 7. Service Index Summary

## 7.1 Foundation Service Summary

| Service ID | Service Name | Owning Domain/System | MVP Phase | MVP Depth |
|-----------|--------------|----------------------|-----------|-----------|
| SVC-ID-001 | Identity Registration Service | Identity | Phase 1 | Must Implement |
| SVC-ID-002 | Identity Resolution Service | Identity | Phase 1 | Must Implement |
| SVC-ID-003 | Identity Verification Baseline Service | Identity | Phase 1 | Partial Implement |
| SVC-ID-004 | Actor Identity Lookup Service | Identity | Phase 1 | Must Implement |
| SVC-ORG-001 | Organization Registration Service | Organization | Phase 1 | Must Implement |
| SVC-ORG-002 | Organization Membership Service | Organization | Phase 1 | Must Implement |
| SVC-ORG-003 | Organization Context Service | Organization | Phase 1 | Must Implement |
| SVC-USER-001 | User Registration Service | User | Phase 1 | Must Implement |
| SVC-USER-002 | User Profile Service | User | Phase 1 | Must Implement |
| SVC-USER-003 | User Role Assignment Service | User / Permission | Phase 1 | Must Implement |
| SVC-USER-004 | User Context Service | User | Phase 1 | Must Implement |
| SVC-PERM-001 | Permission Check Service | Permission | Phase 1 | Must Implement |
| SVC-PERM-002 | Access Scope Resolution Service | Permission | Phase 1 | Must Implement |
| SVC-PERM-003 | Permission Assignment Service | Permission | Phase 1 | Must Implement |
| SVC-POL-001 | Policy Evaluation Baseline Service | Policy | Phase 1 | Partial Implement |
| SVC-POL-002 | Review Policy Lookup Service | Policy / Business Responsibility | Phase 1 / 3 | Partial Implement |
| SVC-POL-003 | AI Risk Policy Check Service | Policy / AI Governance | Phase 4 | Must Implement |
| SVC-KNO-001 | Knowledge Retrieval Service | Knowledge | Phase 1 | Must Implement |
| SVC-KNO-002 | Knowledge Source Registration Service | Knowledge | Phase 1 | Must Implement |
| SVC-KNO-003 | Knowledge Asset Validation Service | Knowledge | Phase 1 | Must Implement |
| SVC-KNO-004 | Knowledge Gap Detection Service | Knowledge | Phase 1 | Partial Implement |

## 7.2 Professional Service Summary

| Service ID | Service Name | Owning Domain/System | MVP Phase | MVP Depth |
|-----------|--------------|----------------------|-----------|-----------|
| SVC-BRD-001 | Brand Registration Service | Brand | Phase 2 | Must Implement |
| SVC-BRD-002 | Brand Context Service | Brand | Phase 2 | Must Implement |
| SVC-BRD-003 | Brand-to-Trademark Link Service | Brand / Trademark | Phase 2 | Must Implement |
| SVC-TM-001 | Trademark Registration Service | Trademark | Phase 2 | Must Implement |
| SVC-TM-002 | Trademark Status Normalization Service | Trademark | Phase 2 | Must Implement |
| SVC-TM-003 | Trademark Lookup Service | Trademark | Phase 2 | Must Implement |
| SVC-TM-004 | Trademark Lifecycle Summary Service | Trademark | Phase 2 | Must Implement |
| SVC-JUR-001 | Jurisdiction Requirement Lookup Service | Jurisdiction | Phase 2 | Must Implement |
| SVC-JUR-002 | Jurisdiction Rule Validation Service | Jurisdiction / Policy | Phase 2 | Must Implement |
| SVC-JUR-003 | Trademark Office Context Service | Jurisdiction | Phase 2 | Must Implement |
| SVC-CLS-001 | Classification Recommendation Service | Classification / AI Governance | Phase 2 / 4 | Must Implement |
| SVC-CLS-002 | Classification Validation Service | Classification | Phase 2 | Must Implement |
| SVC-CLS-003 | GoodsServices Term Lookup Service | Classification | Phase 2 | Must Implement |
| SVC-CLS-004 | Classification Review Service | Classification / Business Responsibility | Phase 2 / 3 | Must Implement |
| SVC-DOC-001 | Document Upload Service | Document | Phase 2 | Must Implement |
| SVC-DOC-002 | Document Requirement Service | Document / Jurisdiction | Phase 2 | Must Implement |
| SVC-DOC-003 | Document Draft Service | Document / AI Governance | Phase 2 / 4 | Partial Implement |
| SVC-DOC-004 | Document Validation Service | Document | Phase 2 | Must Implement |
| SVC-DOC-005 | Document Link Service | Document | Phase 2 | Must Implement |
| SVC-EVD-001 | Evidence Upload Service | Evidence | Phase 2 | Partial Implement |
| SVC-EVD-002 | Evidence Package Service | Evidence | Phase 2 | Partial Implement |
| SVC-EVD-003 | Evidence Review Service | Evidence / AI Governance | Phase 2 / 4 | Partial Implement |
| SVC-EVD-004 | Evidence Metadata Extraction Service | Evidence | Phase 2 | Partial Implement |

## 7.3 Business Execution Service Summary

| Service ID | Service Name | Owning Domain/System | MVP Phase | MVP Depth |
|-----------|--------------|----------------------|-----------|-----------|
| SVC-CUS-001 | Customer Registration Service | Customer | Phase 3 | Must Implement |
| SVC-CUS-002 | Customer Context Service | Customer | Phase 3 | Must Implement |
| SVC-CUS-003 | Customer Link Service | Customer | Phase 3 | Must Implement |
| SVC-ORD-001 | Order Creation Service | Order | Phase 3 | Must Implement |
| SVC-ORD-002 | Order Validation Service | Order | Phase 3 | Must Implement |
| SVC-ORD-003 | Order Confirmation Service | Order | Phase 3 | Must Implement |
| SVC-ORD-004 | Order-to-Matter Conversion Service | Order / Matter | Phase 3 | Must Implement |
| SVC-MAT-001 | Matter Creation Service | Matter | Phase 3 | Must Implement |
| SVC-MAT-002 | Matter Status Service | Matter | Phase 3 | Must Implement |
| SVC-MAT-003 | Matter Context Service | Matter | Phase 3 | Must Implement |
| SVC-MAT-004 | Matter Link Service | Matter | Phase 3 | Must Implement |
| SVC-WFC-001 | Workflow Contract Registration Service | Workflow Contract | Phase 3 | Must Implement |
| SVC-WFC-002 | Workflow Transition Validation Service | Workflow Contract | Phase 3 | Must Implement |
| SVC-WFC-003 | Workflow State Resolution Service | Workflow Contract | Phase 3 | Must Implement |
| SVC-TSK-001 | Task Creation Service | Task | Phase 3 | Must Implement |
| SVC-TSK-002 | Task Assignment Service | Task / Business Responsibility | Phase 3 | Must Implement |
| SVC-TSK-003 | Task Completion Service | Task | Phase 3 | Must Implement |
| SVC-TSK-004 | Task Review Service | Task / Business Responsibility | Phase 3 | Must Implement |
| SVC-EVT-001 | Event Publication Service | Event | Phase 3 | Must Implement |
| SVC-EVT-002 | Event Subscription Service | Event | Phase 3 | Partial Implement |
| SVC-EVT-003 | Event Validation Service | Event | Phase 3 | Must Implement |
| SVC-EVT-004 | Event Replay Baseline Service | Event | Phase 3 | Partial Implement |
| SVC-NOT-001 | Notification Dispatch Service | Notification | Phase 3 | Partial Implement |
| SVC-NOT-002 | Notification Rule Service | Notification / Policy | Phase 3 | Partial Implement |
| SVC-NOT-003 | Notification Preference Baseline Service | Notification | Phase 3 | Reserved Boundary |
| SVC-OPP-001 | Opportunity Detection Baseline Service | Opportunity / AI Governance | Phase 4 | Partial Implement |
| SVC-OPP-002 | Opportunity Creation Service | Opportunity | Phase 4 | Partial Implement |
| SVC-OPP-003 | Opportunity Review Service | Opportunity / Business Responsibility | Phase 4 | Partial Implement |

## 7.4 Collaboration Network Service Summary

| Service ID | Service Name | Owning Domain/System | MVP Phase | MVP Depth |
|-----------|--------------|----------------------|-----------|-----------|
| SVC-PRT-001 | Partner Registration Baseline Service | Partner | Phase 5 | Reserved Boundary |
| SVC-PRT-002 | Partner Relationship Service | Partner | Phase 5 | Reserved Boundary |
| SVC-AGT-001 | Agent Registration Service | Agent | Phase 4 | Partial Implement |
| SVC-AGT-002 | Agent Lookup Service | Agent | Phase 4 | Partial Implement |
| SVC-AGT-003 | Agent Capability Service | Agent / Capability | Phase 4 | Partial Implement |
| SVC-AGT-004 | Agent Contact Service | Agent / Communication | Phase 4 | Partial Implement |
| SVC-SP-001 | Service Provider Registration Service | Service Provider | Phase 4 | Partial Implement |
| SVC-SP-002 | Service Provider Lookup Service | Service Provider | Phase 4 | Partial Implement |
| SVC-SP-003 | Capability Matching Baseline Service | Service Provider / Capability | Phase 4 | Partial Implement |
| SVC-SN-001 | Service Network Boundary Service | Service Network | Phase 5 | Reserved Boundary |
| SVC-SN-002 | Network Membership Baseline Service | Service Network | Phase 5 | Reserved Boundary |
| SVC-RT-001 | Routing Recommendation Service | Routing / AI Governance | Phase 4 | Partial Implement |
| SVC-RT-002 | Routing Review Service | Routing / Business Responsibility | Phase 4 | Partial Implement |
| SVC-RT-003 | Routing Decision Service | Routing | Phase 4 | Partial Implement |
| SVC-COMM-001 | Communication Link Service | Communication | Phase 4 | Partial Implement |
| SVC-COMM-002 | Communication Summary Service | Communication / AI Governance | Phase 4 | Partial Implement |
| SVC-COMM-003 | Communication Action Item Service | Communication / Task | Phase 4 | Partial Implement |

## 7.5 Cross-Cutting, AI Governance and Codex Service Summary

| Service ID | Service Name | Owning Domain/System | MVP Phase/Wave | MVP Depth |
|-----------|--------------|----------------------|----------------|-----------|
| SVC-CAP-001 | Capability Registration Service | Capability | Phase 1 | Partial Implement |
| SVC-CAP-002 | Capability Matching Service | Capability | Phase 1 / 4 | Partial Implement |
| SVC-CAP-003 | Capability Validation Service | Capability | Phase 1 | Partial Implement |
| SVC-BR-001 | Responsibility Assignment Service | Business Responsibility | Phase 3 | Must Implement |
| SVC-BR-002 | Review Assignment Service | Business Responsibility | Phase 3 | Must Implement |
| SVC-BR-003 | Approval Service | Business Responsibility | Phase 3 | Must Implement |
| SVC-BR-004 | Escalation Baseline Service | Business Responsibility / Policy | Phase 3 | Partial Implement |
| SVC-AI-001 | Agent Contract Validation Service | AI Governance | Phase 4 | Must Implement |
| SVC-AI-002 | AI Output Registration Service | AI Governance | Phase 4 | Must Implement |
| SVC-AI-003 | AI Recommendation Registration Service | AI Governance | Phase 4 | Must Implement |
| SVC-AI-004 | AI Audit Recording Service | AI Governance | Phase 4 | Must Implement |
| SVC-AI-005 | AI Review Routing Service | AI Governance / Business Responsibility | Phase 4 | Must Implement |
| SVC-CX-001 | Codex Task Registration Service | Codex Task System | Wave 0 | Must Implement |
| SVC-CX-002 | Codex Task Validation Service | Codex Task System | Wave 0 | Must Implement |
| SVC-CX-003 | Codex Task Execution Service | Codex Task System | Wave 0–7 | Partial Implement |
| SVC-CX-004 | Spec Consistency Check Service | Specification Governance | Wave 0 / 7 | Partial Implement |
| SVC-CX-005 | Prohibited Overreach Check Service | Specification Governance | Wave 0 / 7 | Must Implement |

---

# 8. High-Priority MVP Services

The following services form the minimum executable service baseline.

```text
Identity Registration Service
Identity Resolution Service
Actor Identity Lookup Service
Organization Registration Service
Organization Membership Service
Organization Context Service
User Registration Service
User Profile Service
User Role Assignment Service
User Context Service
Permission Check Service
Access Scope Resolution Service
Permission Assignment Service
Knowledge Retrieval Service
Knowledge Source Registration Service
Knowledge Asset Validation Service
Brand Registration Service
Brand Context Service
Brand-to-Trademark Link Service
Trademark Registration Service
Trademark Status Normalization Service
Trademark Lookup Service
Trademark Lifecycle Summary Service
Jurisdiction Requirement Lookup Service
Jurisdiction Rule Validation Service
Trademark Office Context Service
Classification Recommendation Service
Classification Validation Service
GoodsServices Term Lookup Service
Classification Review Service
Document Upload Service
Document Requirement Service
Document Validation Service
Document Link Service
Customer Registration Service
Customer Context Service
Customer Link Service
Order Creation Service
Order Validation Service
Order Confirmation Service
Order-to-Matter Conversion Service
Matter Creation Service
Matter Status Service
Matter Context Service
Matter Link Service
Workflow Contract Registration Service
Workflow Transition Validation Service
Workflow State Resolution Service
Task Creation Service
Task Assignment Service
Task Completion Service
Task Review Service
Event Publication Service
Event Validation Service
Responsibility Assignment Service
Review Assignment Service
Approval Service
Agent Contract Validation Service
AI Output Registration Service
AI Audit Recording Service
AI Review Routing Service
Codex Task Registration Service
Codex Task Validation Service
Prohibited Overreach Check Service
```

---

# 9. Service Ownership Rules

## 9.1 Single Primary Owner

Each Core Service must have one primary owning domain or cross-cutting system.

## 9.2 Cross-Domain Services Must Declare Primary Ownership

Some services operate across domains.

Example:

```text
Order-to-Matter Conversion Service
    Primary Owner: Order
    Related Domain: Matter
```

## 9.3 Cross-Cutting Ownership Must Be Explicit

Services owned by Capability, Business Responsibility, AI Governance or Codex Task System must be explicitly marked.

## 9.4 Product Services Are Not Core Services

A product-specific feature is not a Core Service unless it operates Core meaning under Core contracts.

Not Core Services:

```text
Lite Wizard Step Service
MarkReg Dashboard Widget Service
Client Portal Button Handler
Partner Center Menu Loader
```

---

# 10. Service-to-Object Mapping Rules

Every Core Service must specify object access.

Allowed object access types:

```text
read
create
update
link
unlink
validate
approve
reject
archive
emit-reference
```

A service that mutates objects must emit an event unless it has an explicit no-event reason.

Examples:

| Service | Objects Read | Objects Created/Updated |
|--------|--------------|--------------------------|
| Identity Registration Service | Identity input | Identity, Actor |
| Permission Check Service | Permission Rule, Access Scope | none |
| Knowledge Asset Validation Service | Knowledge Asset, Knowledge Source | Knowledge Asset validation status |
| Trademark Registration Service | Brand, Jurisdiction, Classification | Trademark |
| Classification Recommendation Service | Trademark, Jurisdiction, Knowledge Asset | Classification Recommendation |
| Document Upload Service | Matter, Document Requirement | Document, Document Metadata |
| Order-to-Matter Conversion Service | Order, Customer, Trademark | Matter, Order-to-Matter Link |
| Task Assignment Service | Task, User, Responsibility Assignment | Task Assignment |
| Event Publication Service | Event Payload | Event |
| Agent Contract Validation Service | AI Agent, Agent Contract, Policy Rule | Agent Contract validation status |
| AI Audit Recording Service | AI Output, Agent Contract | AI Audit Record |
| Codex Task Validation Service | Codex Task, Spec File | Validation Report |

---

# 11. Service-to-Event Mapping Rules

Core Services produce meaningful events.

Examples:

| Service | Events Emitted |
|--------|----------------|
| Identity Registration Service | IdentityCreated |
| Organization Registration Service | OrganizationCreated |
| User Registration Service | UserCreated |
| Permission Assignment Service | PermissionGranted, PermissionRevoked |
| Knowledge Source Registration Service | KnowledgeSourceAdded |
| Knowledge Asset Validation Service | KnowledgeAssetValidated |
| Brand Registration Service | BrandCreated |
| Trademark Status Normalization Service | TrademarkStatusChanged |
| Classification Recommendation Service | ClassificationRecommendationGenerated, ClassificationReviewRequired |
| Classification Review Service | ClassificationRecommendationApproved, ClassificationRecommendationRejected |
| Document Upload Service | DocumentUploaded |
| Document Draft Service | DocumentGenerated, DocumentReviewRequired |
| Evidence Review Service | EvidenceReviewRequired, EvidencePackageFlagged |
| Customer Registration Service | CustomerCreated |
| Order Confirmation Service | OrderConfirmed |
| Order-to-Matter Conversion Service | OrderConvertedToMatter, MatterCreated |
| Matter Status Service | MatterStatusChanged |
| Workflow Transition Validation Service | WorkflowTransitionApproved, WorkflowTransitionRejected |
| Task Completion Service | TaskCompleted |
| Task Review Service | TaskReviewRequired |
| Event Publication Service | EventPublished |
| Notification Dispatch Service | NotificationSent, NotificationFailed |
| Opportunity Detection Baseline Service | OpportunitySignalDetected |
| Routing Recommendation Service | RoutingRecommendationGenerated, RoutingReviewRequired |
| Communication Summary Service | CommunicationSummaryGenerated |
| Responsibility Assignment Service | ResponsibilityAssigned |
| Approval Service | ReviewApproved, ReviewRejected |
| Agent Contract Validation Service | AgentContractValidated, AgentContractValidationFailed |
| AI Audit Recording Service | AIAuditRecordCreated |
| Codex Task Execution Service | CodexTaskStarted, CodexTaskImplemented |
| Prohibited Overreach Check Service | ProhibitedOverreachDetected |

---

# 12. Service-to-Contract Mapping Rules

Every Core Service must require one or more contracts.

Contract types include:

```text
Input Contract
Output Contract
Data Contract
API Contract
Event Contract
Workflow Contract
Permission Contract
Policy Contract
Review Contract
Agent Contract
Codex Task Contract
```

Examples:

| Service | Required Contracts |
|--------|--------------------|
| Identity Registration Service | Identity Input Contract, Identity Data Contract |
| Permission Check Service | Permission Contract |
| Knowledge Retrieval Service | Knowledge Retrieval API Contract, AI Knowledge Authorization Contract |
| Classification Recommendation Service | Classification Recommendation Contract, Agent Contract if AI-assisted |
| Document Draft Service | Document Draft Contract, Review Contract, Agent Contract if AI-assisted |
| Order-to-Matter Conversion Service | Order-to-Matter Workflow Contract |
| Workflow Transition Validation Service | Workflow Contract |
| Task Assignment Service | Responsibility Contract |
| Event Publication Service | Event Contract, Event Payload Contract |
| Agent Contract Validation Service | Agent Contract |
| AI Output Registration Service | AI Output Contract |
| Codex Task Validation Service | Codex Task Contract |

---

# 13. Permission, Policy and Review Rules

## 13.1 Permission Rule

A Core Service that reads, creates, updates, exports or invokes Core Objects must check permission.

## 13.2 Policy Rule

A Core Service affected by jurisdiction, review, AI risk, data exposure or business responsibility must check policy.

## 13.3 Review Rule

A Core Service that produces high-risk professional output must require review.

Review-required service examples:

```text
Classification Recommendation Service
Document Draft Service
Evidence Review Service
Routing Recommendation Service
AI Output Registration Service
Office Action Analysis Service
```

## 13.4 Approval Rule

Approval must be represented through Business Responsibility services.

```text
Review Assignment Service
Approval Service
Escalation Baseline Service
```

---

# 14. AI-Assisted Service Rules

AI-assisted services must follow AI governance.

AI-assisted services require:

```text
AI Agent
Agent Contract
Authorized Knowledge
Permission Check
Policy Check
AI Output
AI Audit Record
Review Rule
Event Emission
```

AI-assisted services include:

```text
Classification Recommendation Service
Document Draft Service
Evidence Review Service
Trademark Lifecycle Summary Service
Communication Summary Service
Opportunity Detection Baseline Service
Routing Recommendation Service
Workflow Assistance Service
Spec Consistency Check Service
```

AI-assisted services must not:

```text
make final professional decisions without review
submit official filings
alter evidence
invent legal authority
change Core state directly outside services
bypass audit
```

---

# 15. API Exposure Rules

A Core Service may be exposed through API only when it has:

```text
input contract
output contract
permission rule
policy rule
event side-effect definition
consumer classification
error contract
audit rule if required
```

API exposure levels:

```text
Internal API
Product API
Agent API
Integration API
Admin API
No API
```

MVP API exposure should be conservative.

High-risk services should use internal or product-mediated APIs first.

---

# 16. Workflow Usage Rules

Services used in workflow execution must specify:

```text
workflow contract
allowed state transition
task creation or update
review requirement
events emitted
failure behavior
```

Workflow-critical services include:

```text
Order-to-Matter Conversion Service
Workflow Transition Validation Service
Task Creation Service
Task Assignment Service
Task Completion Service
Task Review Service
Matter Status Service
Approval Service
Event Publication Service
Notification Dispatch Service
```

---

# 17. Deferred Service Scope

The following service groups are deferred or reserved.

```text
full enterprise IAM services
full policy engine services
full global legal knowledge automation
full evidence scoring engine
official filing automation services
full billing and payment orchestration services
full CRM automation services
full notification preference center
full opportunity scoring engine
full provider ranking service
full MGSN marketplace services
full network trust economy services
autonomous AI legal strategy services
automatic external reply services
```

Deferred services must not be implemented through MVP task shortcuts.

---

# 18. Validation Rules

The service index must pass the following validation checks.

```text
[ ] Every service has a Service ID.
[ ] Every service has a name.
[ ] Every service has an owning domain or cross-cutting system.
[ ] Every service has MVP phase or wave.
[ ] Every service has MVP depth.
[ ] Every service has a category.
[ ] Every service defines related objects.
[ ] Every mutating service defines emitted events or explicit no-event reason.
[ ] Every service defines required contracts.
[ ] Every service defines permission requirement.
[ ] Every service defines policy requirement where applicable.
[ ] Every AI-assisted service defines Agent Contract requirement.
[ ] Every AI-assisted service defines audit requirement.
[ ] Every high-risk service defines review requirement.
[ ] No service is only a UI action.
[ ] No service is only a database operation.
[ ] No service silently expands deferred scope.
```

---

# 19. Prohibited Service Changes

This index must not be changed to:

```text
add UI buttons as Core Services
add product-specific workflow steps as Core Services without Core meaning
add database CRUD operations as Core Services without governance
create services without owning domain or system
create AI services without Agent Contract
create AI services without audit
create mutating services without events
create services that bypass permission or policy
create official filing automation in MVP
create full marketplace services in MVP
create full opportunity scoring in MVP
rename canonical services without architecture review
```

---

# 20. Handoff to core-specs/services/

This index will generate future files under:

```text
core-specs/services/
```

Expected scaffold:

```text
core-specs/services/README.md
core-specs/services/_template.md
core-specs/services/foundation/
core-specs/services/professional/
core-specs/services/business-execution/
core-specs/services/collaboration-network/
core-specs/services/cross-cutting/
core-specs/services/ai-governance/
core-specs/services/codex/
```

Initial detailed service specs should prioritize:

```text
identity-registration-service.md
permission-check-service.md
knowledge-retrieval-service.md
knowledge-asset-validation-service.md
trademark-registration-service.md
trademark-status-normalization-service.md
classification-recommendation-service.md
classification-validation-service.md
document-upload-service.md
document-requirement-service.md
order-creation-service.md
order-to-matter-conversion-service.md
matter-creation-service.md
workflow-transition-validation-service.md
task-creation-service.md
task-assignment-service.md
event-publication-service.md
responsibility-assignment-service.md
review-assignment-service.md
approval-service.md
agent-contract-validation-service.md
ai-output-registration-service.md
ai-audit-recording-service.md
codex-task-validation-service.md
prohibited-overreach-check-service.md
```

---

# 21. Handoff to event-index.md

The next index should be checked against this service index.

```text
indexes/event-index.md
```

Each Core Event must specify:

```text
source service
source domain or system
trigger
payload contract
consumer domains
audit requirement
MVP depth
```

An event without a source service is not implementation-ready unless it is explicitly external or imported.

---

# 22. Acceptance Criteria

This index is accepted only if it satisfies the following criteria.

```text
[ ] It defines Core Service as a governed capability that operates Core meaning.
[ ] It distinguishes Core Service from UI action, helper, database operation and API wrapper.
[ ] It defines service index fields.
[ ] It lists Foundation Services.
[ ] It lists Professional Services.
[ ] It lists Business Execution Services.
[ ] It lists Collaboration Network Services.
[ ] It lists Cross-Cutting Services.
[ ] It lists AI Governance Services.
[ ] It lists Codex Services.
[ ] It identifies high-priority MVP Services.
[ ] It defines service ownership rules.
[ ] It maps services to objects.
[ ] It maps services to events.
[ ] It maps services to contracts.
[ ] It defines permission, policy and review rules.
[ ] It defines AI-assisted service rules.
[ ] It defines API exposure rules.
[ ] It defines workflow usage rules.
[ ] It defines deferred service scope.
[ ] It defines validation rules.
[ ] It defines prohibited service changes.
[ ] It prepares core-specs/services/.
[ ] It hands off to event-index.md.
```

---

# 23. Revision Notes

| Version | Status | Notes |
|---------|--------|-------|
| 0.1.0 | Draft | Initial operational Service Index derived from B02-APP-D. Defines service ownership, MVP depth, service categories, AI-assisted service rules, object/event/contract mapping, validation rules and handoff to event-index.md. |

---

**End of Index**
