# API Index

**Repository:** `book-02-core`  
**Directory:** `indexes/`  
**Index ID:** B02-IDX-API  
**Source Appendix:** B02-APP-F — API Index  
**Related Appendices:** B02-APP-A — Glossary; B02-APP-B — Core Domain Index; B02-APP-C — Core Object Index; B02-APP-D — Core Service Index; B02-APP-E — Event Index  
**Stage:** Second Canonical Draft  
**Status:** Draft  
**Version:** 0.1.0  
**Owner:** MarkOrbit Publications Editorial Board  

---

# 1. Index Purpose

This index operationalizes **B02-APP-F — API Index**.

The appendix is the canonical manuscript reference.

This file is the implementation-ready API index used by:

```text
core-specs/api/
core-specs/services/
core-specs/events/
core-specs/contracts/
core-specs/agents/
codex-tasks/
validation scripts
release checks
```

This index does not define Core meaning.

It defines controlled API consumption surfaces through which products, Workplaces, AI Agents, internal services, integrations and Codex may consume approved Core Services and Core Objects.

---

# 2. Canonical API Rule

Book 02 uses the following canonical rule:

```text
API is a contract-bound consumption surface.
API does not define Core meaning.
```

Therefore:

```text
No Core Service, no implementation-ready API.
No input contract, no API.
No output contract, no API.
No permission rule, no safe API.
No event side-effect declaration, no mutating API.
No consumer boundary, no Core consumption.
```

---

# 3. API vs Core

An API is not automatically:

```text
a Core Domain
a Core Object
a Core Service
a Workflow Contract
an AI Agent
a product feature
a database interface
a third-party integration definition
```

An API exposes governed Core capabilities to consumers.

It must not redefine:

```text
Domain meaning
Object meaning
Service responsibility
Event semantics
AI authority
Business responsibility
MVP scope
```

---

# 4. API Index Fields

Each API entry should include the following fields.

```text
API ID
API Name
API Category
Owning Domain or System
Backing Core Service
HTTP / RPC Shape
Consumer Type
MVP Phase or Wave
MVP Depth
Input Contract
Output Contract
Permission Requirement
Policy Requirement
Review Requirement
Audit Requirement
Events Emitted
AI Usage
Workflow Usage
Rate / Safety Constraints
Error Contract
Product Consumers
Deferred Scope
Validation Notes
```

---

# 5. API Categories

This index uses the following API categories.

```text
Foundation API
Professional API
Business Execution API
Workflow API
Collaboration Network API
Cross-Cutting API
AI Invocation API
Codex API
Validation API
Internal API
Product API
Integration API
Admin API
```

---

# 6. API Exposure Levels

API exposure should be classified conservatively.

```text
Internal API
Product API
Agent API
Integration API
Admin API
No API
```

## 6.1 Internal API

Used by Core or internal services only.

## 6.2 Product API

Used by MarkReg, MarkOrbit Lite, Workplace or later product consumers.

## 6.3 Agent API

Used by governed AI Agents under Agent Contract.

## 6.4 Integration API

Used by external systems or connectors.

## 6.5 Admin API

Used by authorized administrative or governance actors.

## 6.6 No API

The service is not exposed directly.

---

# 7. MVP Depth Vocabulary

```text
Must Implement
Partial Implement
Reserved Boundary
Deferred
```

An API marked `Must Implement` is required for the first executable Core kernel.

An API marked `Partial Implement` requires baseline specification but limited exposure.

An API marked `Reserved Boundary` is recognized but should not be deeply implemented in MVP.

An API marked `Deferred` belongs to future releases.

---

# 8. API Consumer Types

This index uses the following consumer types.

```text
Core Internal Service
MarkReg
MarkOrbit Lite
Workplace
AI Agent
Codex Implementation
MGSN
Partner Center
Client Portal
Service Platform
External Integration
Reporting Consumer
Admin Console
```

Consumers must not use APIs to redefine Core meaning.

---

# 9. API Index Summary

## 9.1 Foundation API Summary

| API ID | API Name | Owning Domain/System | Backing Service | MVP Phase | MVP Depth | Exposure |
|-------|----------|----------------------|-----------------|-----------|-----------|----------|
| API-ID-001 | Identity Registration API | Identity | Identity Registration Service | Phase 1 | Must Implement | Internal / Product |
| API-ID-002 | Identity Resolution API | Identity | Identity Resolution Service | Phase 1 | Must Implement | Internal |
| API-ID-003 | Actor Identity Lookup API | Identity | Actor Identity Lookup Service | Phase 1 | Must Implement | Internal / Agent |
| API-ORG-001 | Organization Registration API | Organization | Organization Registration Service | Phase 1 | Must Implement | Product |
| API-ORG-002 | Organization Membership API | Organization | Organization Membership Service | Phase 1 | Must Implement | Internal / Product |
| API-ORG-003 | Organization Context API | Organization | Organization Context Service | Phase 1 | Must Implement | Internal / Product |
| API-USER-001 | User Registration API | User | User Registration Service | Phase 1 | Must Implement | Product / Admin |
| API-USER-002 | User Profile API | User | User Profile Service | Phase 1 | Must Implement | Product |
| API-USER-003 | User Role Assignment API | User / Permission | User Role Assignment Service | Phase 1 | Must Implement | Admin |
| API-USER-004 | User Context API | User | User Context Service | Phase 1 | Must Implement | Internal / Agent |
| API-PERM-001 | Permission Check API | Permission | Permission Check Service | Phase 1 | Must Implement | Internal |
| API-PERM-002 | Access Scope Resolution API | Permission | Access Scope Resolution Service | Phase 1 | Must Implement | Internal |
| API-PERM-003 | Permission Assignment API | Permission | Permission Assignment Service | Phase 1 | Must Implement | Admin |
| API-POL-001 | Policy Evaluation API | Policy | Policy Evaluation Baseline Service | Phase 1 | Partial Implement | Internal |
| API-POL-002 | Review Policy Lookup API | Policy / Business Responsibility | Review Policy Lookup Service | Phase 1 / 3 | Partial Implement | Internal |
| API-POL-003 | AI Risk Policy Check API | Policy / AI Governance | AI Risk Policy Check Service | Phase 4 | Must Implement | Internal / Agent |
| API-KNO-001 | Knowledge Retrieval API | Knowledge | Knowledge Retrieval Service | Phase 1 | Must Implement | Internal / Agent / Product |
| API-KNO-002 | Knowledge Source Registration API | Knowledge | Knowledge Source Registration Service | Phase 1 | Must Implement | Admin |
| API-KNO-003 | Knowledge Asset Validation API | Knowledge | Knowledge Asset Validation Service | Phase 1 | Must Implement | Internal / Admin |
| API-KNO-004 | Knowledge Gap Detection API | Knowledge | Knowledge Gap Detection Service | Phase 1 | Partial Implement | Internal / Agent |

## 9.2 Professional API Summary

| API ID | API Name | Owning Domain/System | Backing Service | MVP Phase | MVP Depth | Exposure |
|-------|----------|----------------------|-----------------|-----------|-----------|----------|
| API-BRD-001 | Brand Registration API | Brand | Brand Registration Service | Phase 2 | Must Implement | Product |
| API-BRD-002 | Brand Context API | Brand | Brand Context Service | Phase 2 | Must Implement | Product / Agent |
| API-BRD-003 | Brand-to-Trademark Link API | Brand / Trademark | Brand-to-Trademark Link Service | Phase 2 | Must Implement | Internal / Product |
| API-TM-001 | Trademark Registration API | Trademark | Trademark Registration Service | Phase 2 | Must Implement | Product |
| API-TM-002 | Trademark Status Normalization API | Trademark | Trademark Status Normalization Service | Phase 2 | Must Implement | Internal |
| API-TM-003 | Trademark Lookup API | Trademark | Trademark Lookup Service | Phase 2 | Must Implement | Product / Agent |
| API-TM-004 | Trademark Lifecycle Summary API | Trademark | Trademark Lifecycle Summary Service | Phase 2 | Must Implement | Product / Agent |
| API-JUR-001 | Jurisdiction Requirement Lookup API | Jurisdiction | Jurisdiction Requirement Lookup Service | Phase 2 | Must Implement | Product / Agent |
| API-JUR-002 | Jurisdiction Rule Validation API | Jurisdiction / Policy | Jurisdiction Rule Validation Service | Phase 2 | Must Implement | Internal / Agent |
| API-JUR-003 | Trademark Office Context API | Jurisdiction | Trademark Office Context Service | Phase 2 | Must Implement | Product / Agent |
| API-CLS-001 | Classification Recommendation API | Classification / AI Governance | Classification Recommendation Service | Phase 2 / 4 | Must Implement | Product / Agent |
| API-CLS-002 | Classification Validation API | Classification | Classification Validation Service | Phase 2 | Must Implement | Internal / Product |
| API-CLS-003 | GoodsServices Term Lookup API | Classification | GoodsServices Term Lookup Service | Phase 2 | Must Implement | Product / Agent |
| API-CLS-004 | Classification Review API | Classification / Business Responsibility | Classification Review Service | Phase 2 / 3 | Must Implement | Product / Admin |
| API-DOC-001 | Document Upload API | Document | Document Upload Service | Phase 2 | Must Implement | Product |
| API-DOC-002 | Document Requirement API | Document / Jurisdiction | Document Requirement Service | Phase 2 | Must Implement | Product / Agent |
| API-DOC-003 | Document Draft API | Document / AI Governance | Document Draft Service | Phase 2 / 4 | Partial Implement | Product / Agent |
| API-DOC-004 | Document Validation API | Document | Document Validation Service | Phase 2 | Must Implement | Internal / Product |
| API-DOC-005 | Document Link API | Document | Document Link Service | Phase 2 | Must Implement | Internal / Product |
| API-EVD-001 | Evidence Upload API | Evidence | Evidence Upload Service | Phase 2 | Partial Implement | Product |
| API-EVD-002 | Evidence Package API | Evidence | Evidence Package Service | Phase 2 | Partial Implement | Product |
| API-EVD-003 | Evidence Review API | Evidence / AI Governance | Evidence Review Service | Phase 2 / 4 | Partial Implement | Internal / Agent |
| API-EVD-004 | Evidence Metadata Extraction API | Evidence | Evidence Metadata Extraction Service | Phase 2 | Partial Implement | Internal |

## 9.3 Business Execution API Summary

| API ID | API Name | Owning Domain/System | Backing Service | MVP Phase | MVP Depth | Exposure |
|-------|----------|----------------------|-----------------|-----------|-----------|----------|
| API-CUS-001 | Customer Registration API | Customer | Customer Registration Service | Phase 3 | Must Implement | Product |
| API-CUS-002 | Customer Context API | Customer | Customer Context Service | Phase 3 | Must Implement | Product / Agent |
| API-CUS-003 | Customer Link API | Customer | Customer Link Service | Phase 3 | Must Implement | Internal |
| API-ORD-001 | Order Creation API | Order | Order Creation Service | Phase 3 | Must Implement | Product |
| API-ORD-002 | Order Validation API | Order | Order Validation Service | Phase 3 | Must Implement | Internal / Product |
| API-ORD-003 | Order Confirmation API | Order | Order Confirmation Service | Phase 3 | Must Implement | Product |
| API-ORD-004 | Order-to-Matter Conversion API | Order / Matter | Order-to-Matter Conversion Service | Phase 3 | Must Implement | Internal / Product |
| API-MAT-001 | Matter Creation API | Matter | Matter Creation Service | Phase 3 | Must Implement | Internal / Product |
| API-MAT-002 | Matter Status API | Matter | Matter Status Service | Phase 3 | Must Implement | Product |
| API-MAT-003 | Matter Context API | Matter | Matter Context Service | Phase 3 | Must Implement | Product / Agent |
| API-MAT-004 | Matter Link API | Matter | Matter Link Service | Phase 3 | Must Implement | Internal |
| API-WFC-001 | Workflow Contract Registration API | Workflow Contract | Workflow Contract Registration Service | Phase 3 | Must Implement | Admin / Internal |
| API-WFC-002 | Workflow Transition Validation API | Workflow Contract | Workflow Transition Validation Service | Phase 3 | Must Implement | Internal / Product |
| API-WFC-003 | Workflow State Resolution API | Workflow Contract | Workflow State Resolution Service | Phase 3 | Must Implement | Internal / Agent |
| API-TSK-001 | Task Creation API | Task | Task Creation Service | Phase 3 | Must Implement | Product / Internal |
| API-TSK-002 | Task Assignment API | Task / Business Responsibility | Task Assignment Service | Phase 3 | Must Implement | Product / Internal |
| API-TSK-003 | Task Completion API | Task | Task Completion Service | Phase 3 | Must Implement | Product |
| API-TSK-004 | Task Review API | Task / Business Responsibility | Task Review Service | Phase 3 | Must Implement | Product / Admin |
| API-EVT-001 | Event Publication API | Event | Event Publication Service | Phase 3 | Must Implement | Internal |
| API-EVT-002 | Event Subscription API | Event | Event Subscription Service | Phase 3 | Partial Implement | Internal |
| API-EVT-003 | Event Validation API | Event | Event Validation Service | Phase 3 | Must Implement | Internal |
| API-EVT-004 | Event Replay Baseline API | Event | Event Replay Baseline Service | Phase 3 | Partial Implement | Internal / Admin |
| API-NOT-001 | Notification Dispatch API | Notification | Notification Dispatch Service | Phase 3 | Partial Implement | Internal |
| API-NOT-002 | Notification Rule API | Notification / Policy | Notification Rule Service | Phase 3 | Partial Implement | Admin |
| API-NOT-003 | Notification Preference Baseline API | Notification | Notification Preference Baseline Service | Phase 3 | Reserved Boundary | Product |
| API-OPP-001 | Opportunity Detection Baseline API | Opportunity / AI Governance | Opportunity Detection Baseline Service | Phase 4 | Partial Implement | Internal / Agent |
| API-OPP-002 | Opportunity Creation API | Opportunity | Opportunity Creation Service | Phase 4 | Partial Implement | Product |
| API-OPP-003 | Opportunity Review API | Opportunity / Business Responsibility | Opportunity Review Service | Phase 4 | Partial Implement | Product / Admin |

## 9.4 Collaboration Network API Summary

| API ID | API Name | Owning Domain/System | Backing Service | MVP Phase | MVP Depth | Exposure |
|-------|----------|----------------------|-----------------|-----------|-----------|----------|
| API-PRT-001 | Partner Registration Baseline API | Partner | Partner Registration Baseline Service | Phase 5 | Reserved Boundary | Admin |
| API-PRT-002 | Partner Relationship API | Partner | Partner Relationship Service | Phase 5 | Reserved Boundary | Admin |
| API-AGT-001 | Agent Registration API | Agent | Agent Registration Service | Phase 4 | Partial Implement | Admin |
| API-AGT-002 | Agent Lookup API | Agent | Agent Lookup Service | Phase 4 | Partial Implement | Product / Internal |
| API-AGT-003 | Agent Capability API | Agent / Capability | Agent Capability Service | Phase 4 | Partial Implement | Product / Internal |
| API-AGT-004 | Agent Contact API | Agent / Communication | Agent Contact Service | Phase 4 | Partial Implement | Product / Internal |
| API-SP-001 | Service Provider Registration API | Service Provider | Service Provider Registration Service | Phase 4 | Partial Implement | Admin |
| API-SP-002 | Service Provider Lookup API | Service Provider | Service Provider Lookup Service | Phase 4 | Partial Implement | Product / Internal |
| API-SP-003 | Capability Matching Baseline API | Service Provider / Capability | Capability Matching Baseline Service | Phase 4 | Partial Implement | Internal / Agent |
| API-SN-001 | Service Network Boundary API | Service Network | Service Network Boundary Service | Phase 5 | Reserved Boundary | Admin |
| API-SN-002 | Network Membership Baseline API | Service Network | Network Membership Baseline Service | Phase 5 | Reserved Boundary | Admin |
| API-RT-001 | Routing Recommendation API | Routing / AI Governance | Routing Recommendation Service | Phase 4 | Partial Implement | Product / Agent |
| API-RT-002 | Routing Review API | Routing / Business Responsibility | Routing Review Service | Phase 4 | Partial Implement | Product / Admin |
| API-RT-003 | Routing Decision API | Routing | Routing Decision Service | Phase 4 | Partial Implement | Product / Internal |
| API-COMM-001 | Communication Link API | Communication | Communication Link Service | Phase 4 | Partial Implement | Product / Internal |
| API-COMM-002 | Communication Summary API | Communication / AI Governance | Communication Summary Service | Phase 4 | Partial Implement | Product / Agent |
| API-COMM-003 | Communication Action Item API | Communication / Task | Communication Action Item Service | Phase 4 | Partial Implement | Product / Internal |

## 9.5 Cross-Cutting, AI Governance and Codex API Summary

| API ID | API Name | Owning Domain/System | Backing Service | Phase/Wave | MVP Depth | Exposure |
|-------|----------|----------------------|-----------------|------------|-----------|----------|
| API-CAP-001 | Capability Registration API | Capability | Capability Registration Service | Phase 1 | Partial Implement | Admin |
| API-CAP-002 | Capability Matching API | Capability | Capability Matching Service | Phase 1 / 4 | Partial Implement | Internal / Agent |
| API-CAP-003 | Capability Validation API | Capability | Capability Validation Service | Phase 1 | Partial Implement | Internal |
| API-BR-001 | Responsibility Assignment API | Business Responsibility | Responsibility Assignment Service | Phase 3 | Must Implement | Product / Internal |
| API-BR-002 | Review Assignment API | Business Responsibility | Review Assignment Service | Phase 3 | Must Implement | Product / Internal |
| API-BR-003 | Approval API | Business Responsibility | Approval Service | Phase 3 | Must Implement | Product / Admin |
| API-BR-004 | Escalation Baseline API | Business Responsibility / Policy | Escalation Baseline Service | Phase 3 | Partial Implement | Internal |
| API-AI-001 | Agent Contract Validation API | AI Governance | Agent Contract Validation Service | Phase 4 | Must Implement | Internal / Admin |
| API-AI-002 | AI Output Registration API | AI Governance | AI Output Registration Service | Phase 4 | Must Implement | Internal / Agent |
| API-AI-003 | AI Recommendation Registration API | AI Governance | AI Recommendation Registration Service | Phase 4 | Must Implement | Internal / Agent |
| API-AI-004 | AI Audit Recording API | AI Governance | AI Audit Recording Service | Phase 4 | Must Implement | Internal |
| API-AI-005 | AI Review Routing API | AI Governance / Business Responsibility | AI Review Routing Service | Phase 4 | Must Implement | Internal / Product |
| API-CX-001 | Codex Task Registration API | Codex Task System | Codex Task Registration Service | Wave 0 | Must Implement | Internal |
| API-CX-002 | Codex Task Validation API | Codex Task System | Codex Task Validation Service | Wave 0 | Must Implement | Internal |
| API-CX-003 | Codex Task Execution API | Codex Task System | Codex Task Execution Service | Wave 0–7 | Partial Implement | Internal |
| API-CX-004 | Spec Consistency Check API | Specification Governance | Spec Consistency Check Service | Wave 0 / 7 | Partial Implement | Internal |
| API-CX-005 | Prohibited Overreach Check API | Specification Governance | Prohibited Overreach Check Service | Wave 0 / 7 | Must Implement | Internal |

---

# 10. High-Priority MVP API Baseline

The following APIs form the minimum controlled API baseline.

```text
Identity Registration API
Identity Resolution API
Actor Identity Lookup API
Organization Registration API
Organization Membership API
Organization Context API
User Registration API
User Profile API
User Role Assignment API
User Context API
Permission Check API
Access Scope Resolution API
Permission Assignment API
Knowledge Retrieval API
Knowledge Source Registration API
Knowledge Asset Validation API
Brand Registration API
Brand Context API
Brand-to-Trademark Link API
Trademark Registration API
Trademark Status Normalization API
Trademark Lookup API
Trademark Lifecycle Summary API
Jurisdiction Requirement Lookup API
Jurisdiction Rule Validation API
Trademark Office Context API
Classification Recommendation API
Classification Validation API
GoodsServices Term Lookup API
Classification Review API
Document Upload API
Document Requirement API
Document Validation API
Document Link API
Customer Registration API
Customer Context API
Customer Link API
Order Creation API
Order Validation API
Order Confirmation API
Order-to-Matter Conversion API
Matter Creation API
Matter Status API
Matter Context API
Matter Link API
Workflow Contract Registration API
Workflow Transition Validation API
Workflow State Resolution API
Task Creation API
Task Assignment API
Task Completion API
Task Review API
Event Publication API
Event Validation API
Responsibility Assignment API
Review Assignment API
Approval API
Agent Contract Validation API
AI Output Registration API
AI Recommendation Registration API
AI Audit Recording API
AI Review Routing API
Codex Task Registration API
Codex Task Validation API
Prohibited Overreach Check API
```

---

# 11. API Contract Rules

Every API must define:

```text
input contract
output contract
error contract
permission contract
policy contract when applicable
event side-effect contract when mutating
review contract when high-risk
Agent Contract when AI-assisted
```

A mutating API without event mapping is not implementation-ready.

An AI-assisted API without Agent Contract is prohibited.

---

# 12. API Permission Rules

Every API must declare permission requirements.

Permission requirements should include:

```text
actor identity
organization context
user role
access scope
object-level permission
service-level permission
consumer type
```

APIs must not rely on product UI permission alone.

---

# 13. API Policy Rules

APIs affected by the following must declare policy requirements:

```text
AI risk
professional review
jurisdiction constraint
data exposure
external integration
workflow transition
business responsibility
client-facing output
provider routing
Codex task execution
```

Policy-bound APIs must return controlled failure responses when policy checks fail.

---

# 14. API Event Side-Effect Rules

APIs that mutate Core state must emit or trigger Core Events through backing services.

Examples:

| API | Events |
|-----|--------|
| Identity Registration API | IdentityCreated |
| Organization Membership API | OrganizationMembershipChanged |
| User Role Assignment API | UserRoleAssigned |
| Permission Assignment API | PermissionGranted, PermissionRevoked |
| Knowledge Asset Validation API | KnowledgeAssetValidated |
| Brand Registration API | BrandCreated |
| Trademark Status Normalization API | TrademarkStatusChanged |
| Classification Recommendation API | ClassificationRecommendationGenerated, ClassificationReviewRequired |
| Classification Review API | ClassificationRecommendationApproved, ClassificationRecommendationRejected |
| Document Upload API | DocumentUploaded |
| Order Confirmation API | OrderConfirmed |
| Order-to-Matter Conversion API | OrderConvertedToMatter, MatterCreated |
| Matter Status API | MatterStatusChanged |
| Workflow Transition Validation API | WorkflowTransitionApproved, WorkflowTransitionRejected |
| Task Completion API | TaskCompleted |
| Task Review API | TaskReviewRequired |
| Responsibility Assignment API | ResponsibilityAssigned |
| Approval API | ReviewApproved, ReviewRejected |
| Agent Contract Validation API | AgentContractValidated, AgentContractValidationFailed |
| AI Output Registration API | AIOutputGenerated |
| AI Audit Recording API | AIAuditRecordCreated |
| Prohibited Overreach Check API | ProhibitedOverreachDetected |

---

# 15. AI Invocation API Rules

AI Invocation APIs must be governed.

They require:

```text
AI Agent Identity
Agent Contract
Authorized Knowledge
Permission Check
Policy Check
Input Context Contract
Output Contract
Risk Level
Review Rule
AI Audit Record
Events Emitted
```

AI Invocation APIs include:

```text
Classification Recommendation API
Document Draft API
Evidence Review API
Trademark Lifecycle Summary API
Communication Summary API
Opportunity Detection Baseline API
Routing Recommendation API
AI Output Registration API
AI Recommendation Registration API
Spec Consistency Check API
```

AI Invocation APIs must not:

```text
make final legal decisions without review
submit official filings
send external communications without approval
alter evidence
create unreviewed professional truth
bypass audit
```

---

# 16. Workflow API Rules

Workflow APIs must reference Workflow Contract.

Workflow-critical APIs include:

```text
Order-to-Matter Conversion API
Matter Status API
Workflow Contract Registration API
Workflow Transition Validation API
Workflow State Resolution API
Task Creation API
Task Assignment API
Task Completion API
Task Review API
Review Assignment API
Approval API
Notification Dispatch API
```

Workflow APIs must define:

```text
allowed state transition
required task context
review requirement
events emitted
failure behavior
rollback or compensation rule if applicable
```

---

# 17. Integration API Boundary

External Integration APIs are deferred unless required for MVP data import or controlled source sync.

Reserved or deferred integration API groups include:

```text
official trademark office sync APIs
foreign associate production connector APIs
payment provider APIs
email sending automation APIs
external CRM APIs
full marketplace APIs
partner portal APIs
service provider marketplace APIs
client portal public APIs
advanced reporting APIs
```

MVP should prefer internal and product APIs before external integration APIs.

---

# 18. Error Contract Rules

Every API must define controlled errors.

Common error categories:

```text
PermissionDenied
PolicyViolation
ValidationFailed
ObjectNotFound
Conflict
ReviewRequired
AgentContractMissing
AuthorizedKnowledgeMissing
EventPublicationFailed
WorkflowTransitionRejected
DeferredScopeBlocked
ProhibitedOverreachDetected
```

Error responses must not leak unauthorized data.

---

# 19. Rate and Safety Constraints

APIs with AI, import, event publication, routing, communication or Codex execution should define safety constraints.

Examples:

```text
rate limit
batch limit
idempotency key
correlation ID
retry policy
audit requirement
manual review threshold
safe failure behavior
```

High-risk APIs should be idempotent where possible.

---

# 20. Deferred API Scope

The following API groups are deferred or reserved.

```text
full official filing APIs
full payment and billing APIs
full CRM automation APIs
full partner center APIs
full client portal public APIs
full service platform APIs
full MGSN marketplace APIs
provider ranking APIs
opportunity scoring APIs
network trust APIs
autonomous AI legal strategy APIs
automatic external communication APIs
advanced analytics APIs
```

Deferred APIs must not be implemented through MVP task shortcuts.

---

# 21. Validation Rules

The API index must pass the following validation checks.

```text
[ ] Every API has an API ID.
[ ] Every API has a name.
[ ] Every API has an owning domain or system.
[ ] Every API has a backing Core Service.
[ ] Every API has MVP phase or wave.
[ ] Every API has MVP depth.
[ ] Every API has exposure classification.
[ ] Every API has consumer classification.
[ ] Every API has input and output contract requirements.
[ ] Every API has error contract requirements.
[ ] Every API has permission requirements.
[ ] Every policy-bound API has policy requirements.
[ ] Every mutating API has event side-effect mapping.
[ ] Every AI-assisted API has Agent Contract requirement.
[ ] Every AI-assisted API has audit requirement.
[ ] Every high-risk API has review requirement.
[ ] No API defines Core meaning.
[ ] No API bypasses Core Services.
[ ] No API silently expands deferred scope.
```

---

# 22. Prohibited API Changes

This index must not be changed to:

```text
create APIs without backing Core Services
create APIs without input or output contracts
create APIs that mutate Core state without events
create APIs that bypass permission checks
create APIs that bypass policy checks
create AI APIs without Agent Contract
create AI APIs without audit
create external filing APIs in MVP
create full marketplace APIs in MVP
create full opportunity scoring APIs in MVP
use APIs to redefine Core Objects
use APIs to redefine Core Services
use APIs to redefine Core Events
rename canonical APIs without architecture review
```

---

# 23. Handoff to core-specs/api/

This index will generate future files under:

```text
core-specs/api/
```

Expected scaffold:

```text
core-specs/api/README.md
core-specs/api/_template.md
core-specs/api/foundation/
core-specs/api/professional/
core-specs/api/business-execution/
core-specs/api/collaboration-network/
core-specs/api/cross-cutting/
core-specs/api/ai-governance/
core-specs/api/codex/
```

Initial detailed API specs should prioritize:

```text
identity-registration-api.md
permission-check-api.md
knowledge-retrieval-api.md
trademark-registration-api.md
trademark-status-normalization-api.md
classification-recommendation-api.md
classification-validation-api.md
document-upload-api.md
order-creation-api.md
order-confirmation-api.md
order-to-matter-conversion-api.md
matter-creation-api.md
workflow-transition-validation-api.md
task-creation-api.md
task-assignment-api.md
event-publication-api.md
responsibility-assignment-api.md
review-assignment-api.md
approval-api.md
agent-contract-validation-api.md
ai-output-registration-api.md
ai-audit-recording-api.md
codex-task-validation-api.md
prohibited-overreach-check-api.md
```

---

# 24. Handoff to agent-index.md

The next index should be checked against this API index.

```text
indexes/agent-index.md
```

Each AI Agent must specify:

```text
allowed APIs
prohibited APIs
object access
service access
event access
Agent Contract
Authorized Knowledge
review rule
audit rule
```

An AI Agent without allowed API boundary is not implementation-ready.

---

# 25. Acceptance Criteria

This index is accepted only if it satisfies the following criteria.

```text
[ ] It defines API as a contract-bound consumption surface.
[ ] It states that API does not define Core meaning.
[ ] It defines API index fields.
[ ] It defines API categories.
[ ] It defines exposure levels.
[ ] It lists Foundation APIs.
[ ] It lists Professional APIs.
[ ] It lists Business Execution APIs.
[ ] It lists Collaboration Network APIs.
[ ] It lists Cross-Cutting APIs.
[ ] It lists AI Governance APIs.
[ ] It lists Codex APIs.
[ ] It identifies high-priority MVP APIs.
[ ] It defines API contract rules.
[ ] It defines permission rules.
[ ] It defines policy rules.
[ ] It maps API side effects to events.
[ ] It defines AI Invocation API rules.
[ ] It defines Workflow API rules.
[ ] It defines Integration API boundary.
[ ] It defines error contract rules.
[ ] It defines rate and safety constraints.
[ ] It defines deferred API scope.
[ ] It defines validation rules.
[ ] It defines prohibited API changes.
[ ] It prepares core-specs/api/.
[ ] It hands off to agent-index.md.
```

---

# 26. Revision Notes

| Version | Status | Notes |
|---------|--------|-------|
| 0.1.0 | Draft | Initial operational API Index derived from B02-APP-F. Defines API consumption rules, exposure levels, backing services, event side effects, AI invocation rules, workflow API rules, deferred integration boundaries, validation rules and handoff to agent-index.md. |

---

**End of Index**
