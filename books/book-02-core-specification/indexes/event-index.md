# Event Index

**Repository:** `book-02-core`  
**Directory:** `indexes/`  
**Index ID:** B02-IDX-EVENT  
**Source Appendix:** B02-APP-E — Event Index  
**Related Appendices:** B02-APP-A — Glossary; B02-APP-B — Core Domain Index; B02-APP-C — Core Object Index; B02-APP-D — Core Service Index  
**Stage:** Second Canonical Draft  
**Status:** Draft  
**Version:** 0.1.0  
**Owner:** MarkOrbit Publications Editorial Board  

---

# 1. Index Purpose

This index operationalizes **B02-APP-E — Event Index**.

The appendix is the canonical manuscript reference.

This file is the implementation-ready event index used by:

```text
core-specs/events/
core-specs/services/
core-specs/contracts/
core-specs/api/
core-specs/agents/
codex-tasks/
validation scripts
release checks
```

This index does not define logs, UI actions or analytics tracking.

It defines Core Events as meaningful changes in Core state, professional execution, review requirements, AI output, routing decisions, communication linkage or workflow progress.

---

# 2. Canonical Event Rule

Book 02 uses the following canonical rule:

```text
A Core Event is a meaningful change in Core state, professional execution, review requirement, AI output, routing decision, communication linkage or workflow progress.
```

Therefore:

```text
No meaning, no Core Event.
No source service or external source, no implementation-ready event.
No payload contract, no event contract.
No consumer boundary, no safe event publication.
No audit rule, no governed execution trace.
```

---

# 3. Event Is Not Log

A Core Event is not automatically:

```text
a log
a UI action
an activity feed entry
a queue message
an analytics ping
a database trigger
a notification
a webhook payload
```

A Core Event may later be represented in logs, queues, audit records or notifications, but the Core Event itself must have canonical meaning.

---

# 4. Event Index Fields

Each event entry should include the following fields.

```text
Event ID
Event Name
Event Category
Source Domain or System
Source Service
Trigger
Payload Contract
Related Objects
Consumer Domains
Consumer Services
API Side Effects
AI Usage
Workflow Usage
Audit Requirement
Review Requirement
MVP Phase or Wave
MVP Depth
Retention Requirement
Deferred Scope
Validation Notes
```

---

# 5. Event Categories

This index uses the following event categories.

```text
Foundation Event
Professional Event
Business Execution Event
Workflow Event
Collaboration Network Event
Cross-Cutting Event
AI Governance Event
API / Integration Event
Codex Event
Validation Event
```

---

# 6. MVP Depth Vocabulary

```text
Must Implement
Partial Implement
Reserved Boundary
Deferred
```

A Core Event marked `Must Implement` is required for the first executable Core kernel.

A Core Event marked `Partial Implement` requires baseline contract and limited publication/subscription.

A Core Event marked `Reserved Boundary` is recognized but should not be deeply implemented in MVP.

A Core Event marked `Deferred` belongs to future releases.

---

# 7. Event Naming Rules

Event names must use past-tense meaningful domain language.

Preferred form:

```text
<Noun><PastTenseVerb>
<Noun><StateChanged>
<Noun><ReviewRequired>
<Noun><Approved>
<Noun><Rejected>
```

Examples:

```text
TrademarkStatusChanged
OrderConvertedToMatter
ClassificationReviewRequired
AIOutputGenerated
AgentContractValidated
CodexTaskImplemented
```

Do not use vague event names:

```text
UpdateDone
ClickButton
DataChanged
RunAI
SendMessage
LogCreated
```

---

# 8. Event Index Summary

## 8.1 Foundation Event Summary

| Event ID | Event Name | Source Domain/System | Source Service | MVP Phase | MVP Depth |
|---------|------------|----------------------|----------------|-----------|-----------|
| EVT-ID-001 | IdentityCreated | Identity | Identity Registration Service | Phase 1 | Must Implement |
| EVT-ID-002 | IdentityUpdated | Identity | Identity Resolution Service | Phase 1 | Partial Implement |
| EVT-ID-003 | IdentityLinked | Identity | Identity Resolution Service | Phase 1 | Partial Implement |
| EVT-ID-004 | IdentityDeactivated | Identity | Identity Registration Service | Phase 1 | Partial Implement |
| EVT-ORG-001 | OrganizationCreated | Organization | Organization Registration Service | Phase 1 | Must Implement |
| EVT-ORG-002 | OrganizationUpdated | Organization | Organization Context Service | Phase 1 | Partial Implement |
| EVT-ORG-003 | OrganizationMembershipChanged | Organization | Organization Membership Service | Phase 1 | Must Implement |
| EVT-USER-001 | UserCreated | User | User Registration Service | Phase 1 | Must Implement |
| EVT-USER-002 | UserUpdated | User | User Profile Service | Phase 1 | Partial Implement |
| EVT-USER-003 | UserRoleAssigned | User / Permission | User Role Assignment Service | Phase 1 | Must Implement |
| EVT-USER-004 | UserDeactivated | User | User Registration Service | Phase 1 | Partial Implement |
| EVT-PERM-001 | PermissionGranted | Permission | Permission Assignment Service | Phase 1 | Must Implement |
| EVT-PERM-002 | PermissionRevoked | Permission | Permission Assignment Service | Phase 1 | Must Implement |
| EVT-PERM-003 | PermissionCheckFailed | Permission | Permission Check Service | Phase 1 | Must Implement |
| EVT-POL-001 | PolicyRuleCreated | Policy | Policy Evaluation Baseline Service | Phase 1 | Partial Implement |
| EVT-POL-002 | PolicyRuleUpdated | Policy | Policy Evaluation Baseline Service | Phase 1 | Partial Implement |
| EVT-POL-003 | PolicyViolationDetected | Policy | Policy Evaluation Baseline Service | Phase 1 | Must Implement |
| EVT-KNO-001 | KnowledgeSourceAdded | Knowledge | Knowledge Source Registration Service | Phase 1 | Must Implement |
| EVT-KNO-002 | KnowledgeAssetValidated | Knowledge | Knowledge Asset Validation Service | Phase 1 | Must Implement |
| EVT-KNO-003 | KnowledgeGapDetected | Knowledge | Knowledge Gap Detection Service | Phase 1 | Partial Implement |
| EVT-KNO-004 | KnowledgeAssetUpdated | Knowledge | Knowledge Asset Validation Service | Phase 1 | Partial Implement |

## 8.2 Professional Event Summary

| Event ID | Event Name | Source Domain/System | Source Service | MVP Phase | MVP Depth |
|---------|------------|----------------------|----------------|-----------|-----------|
| EVT-BRD-001 | BrandCreated | Brand | Brand Registration Service | Phase 2 | Must Implement |
| EVT-BRD-002 | BrandUpdated | Brand | Brand Context Service | Phase 2 | Partial Implement |
| EVT-BRD-003 | BrandLinkedToTrademark | Brand / Trademark | Brand-to-Trademark Link Service | Phase 2 | Must Implement |
| EVT-TM-001 | TrademarkCreated | Trademark | Trademark Registration Service | Phase 2 | Must Implement |
| EVT-TM-002 | TrademarkUpdated | Trademark | Trademark Registration Service | Phase 2 | Partial Implement |
| EVT-TM-003 | TrademarkStatusChanged | Trademark | Trademark Status Normalization Service | Phase 2 | Must Implement |
| EVT-TM-004 | TrademarkLinkedToMatter | Trademark / Matter | Matter Link Service | Phase 3 | Must Implement |
| EVT-TM-005 | TrademarkStatusSummaryGenerated | Trademark / AI Governance | Trademark Lifecycle Summary Service | Phase 2 / 4 | Partial Implement |
| EVT-JUR-001 | JurisdictionAdded | Jurisdiction | Trademark Office Context Service | Phase 2 | Must Implement |
| EVT-JUR-002 | JurisdictionRequirementUpdated | Jurisdiction | Jurisdiction Requirement Lookup Service | Phase 2 | Partial Implement |
| EVT-JUR-003 | JurisdictionRuleChanged | Jurisdiction / Policy | Jurisdiction Rule Validation Service | Phase 2 | Partial Implement |
| EVT-CLS-001 | ClassificationRecommendationGenerated | Classification / AI Governance | Classification Recommendation Service | Phase 2 / 4 | Must Implement |
| EVT-CLS-002 | ClassificationReviewRequired | Classification / Business Responsibility | Classification Recommendation Service | Phase 2 / 3 | Must Implement |
| EVT-CLS-003 | ClassificationRecommendationApproved | Classification / Business Responsibility | Classification Review Service | Phase 2 / 3 | Must Implement |
| EVT-CLS-004 | ClassificationRecommendationRejected | Classification / Business Responsibility | Classification Review Service | Phase 2 / 3 | Must Implement |
| EVT-DOC-001 | DocumentUploaded | Document | Document Upload Service | Phase 2 | Must Implement |
| EVT-DOC-002 | DocumentGenerated | Document / AI Governance | Document Draft Service | Phase 2 / 4 | Partial Implement |
| EVT-DOC-003 | DocumentReviewRequired | Document / Business Responsibility | Document Draft Service | Phase 2 / 3 | Partial Implement |
| EVT-DOC-004 | DocumentApproved | Document / Business Responsibility | Document Validation Service | Phase 2 / 3 | Partial Implement |
| EVT-DOC-005 | DocumentRejected | Document / Business Responsibility | Document Validation Service | Phase 2 / 3 | Partial Implement |
| EVT-EVD-001 | EvidenceUploaded | Evidence | Evidence Upload Service | Phase 2 | Partial Implement |
| EVT-EVD-002 | EvidencePackageCreated | Evidence | Evidence Package Service | Phase 2 | Partial Implement |
| EVT-EVD-003 | EvidenceReviewRequired | Evidence / Business Responsibility | Evidence Review Service | Phase 2 / 3 | Partial Implement |
| EVT-EVD-004 | EvidencePackageFlagged | Evidence / AI Governance | Evidence Review Service | Phase 2 / 4 | Partial Implement |

## 8.3 Business Execution Event Summary

| Event ID | Event Name | Source Domain/System | Source Service | MVP Phase | MVP Depth |
|---------|------------|----------------------|----------------|-----------|-----------|
| EVT-CUS-001 | CustomerCreated | Customer | Customer Registration Service | Phase 3 | Must Implement |
| EVT-CUS-002 | CustomerUpdated | Customer | Customer Context Service | Phase 3 | Partial Implement |
| EVT-CUS-003 | CustomerLinkedToOrder | Customer / Order | Customer Link Service | Phase 3 | Must Implement |
| EVT-CUS-004 | CustomerLinkedToMatter | Customer / Matter | Customer Link Service | Phase 3 | Must Implement |
| EVT-ORD-001 | OrderCreated | Order | Order Creation Service | Phase 3 | Must Implement |
| EVT-ORD-002 | OrderUpdated | Order | Order Validation Service | Phase 3 | Partial Implement |
| EVT-ORD-003 | OrderConfirmed | Order | Order Confirmation Service | Phase 3 | Must Implement |
| EVT-ORD-004 | OrderConvertedToMatter | Order / Matter | Order-to-Matter Conversion Service | Phase 3 | Must Implement |
| EVT-MAT-001 | MatterCreated | Matter | Matter Creation Service | Phase 3 | Must Implement |
| EVT-MAT-002 | MatterUpdated | Matter | Matter Context Service | Phase 3 | Partial Implement |
| EVT-MAT-003 | MatterStatusChanged | Matter | Matter Status Service | Phase 3 | Must Implement |
| EVT-MAT-004 | MatterClosed | Matter | Matter Status Service | Phase 3 | Partial Implement |
| EVT-WFC-001 | WorkflowContractCreated | Workflow Contract | Workflow Contract Registration Service | Phase 3 | Must Implement |
| EVT-WFC-002 | WorkflowTransitionRequested | Workflow Contract | Workflow Transition Validation Service | Phase 3 | Must Implement |
| EVT-WFC-003 | WorkflowTransitionApproved | Workflow Contract | Workflow Transition Validation Service | Phase 3 | Must Implement |
| EVT-WFC-004 | WorkflowTransitionRejected | Workflow Contract | Workflow Transition Validation Service | Phase 3 | Must Implement |
| EVT-TSK-001 | TaskCreated | Task | Task Creation Service | Phase 3 | Must Implement |
| EVT-TSK-002 | TaskAssigned | Task / Business Responsibility | Task Assignment Service | Phase 3 | Must Implement |
| EVT-TSK-003 | TaskCompleted | Task | Task Completion Service | Phase 3 | Must Implement |
| EVT-TSK-004 | TaskReviewRequired | Task / Business Responsibility | Task Review Service | Phase 3 | Must Implement |
| EVT-EVT-001 | EventPublished | Event | Event Publication Service | Phase 3 | Must Implement |
| EVT-EVT-002 | EventConsumed | Event | Event Subscription Service | Phase 3 | Partial Implement |
| EVT-EVT-003 | EventSubscriptionCreated | Event | Event Subscription Service | Phase 3 | Partial Implement |
| EVT-EVT-004 | EventValidationFailed | Event | Event Validation Service | Phase 3 | Must Implement |
| EVT-NOT-001 | NotificationCreated | Notification | Notification Dispatch Service | Phase 3 | Partial Implement |
| EVT-NOT-002 | NotificationSent | Notification | Notification Dispatch Service | Phase 3 | Partial Implement |
| EVT-NOT-003 | NotificationFailed | Notification | Notification Dispatch Service | Phase 3 | Partial Implement |
| EVT-OPP-001 | OpportunitySignalDetected | Opportunity / AI Governance | Opportunity Detection Baseline Service | Phase 4 | Partial Implement |
| EVT-OPP-002 | OpportunityCreated | Opportunity | Opportunity Creation Service | Phase 4 | Partial Implement |
| EVT-OPP-003 | OpportunityReviewRequired | Opportunity / Business Responsibility | Opportunity Review Service | Phase 4 | Partial Implement |

## 8.4 Collaboration Network Event Summary

| Event ID | Event Name | Source Domain/System | Source Service | MVP Phase | MVP Depth |
|---------|------------|----------------------|----------------|-----------|-----------|
| EVT-PRT-001 | PartnerRegistered | Partner | Partner Registration Baseline Service | Phase 5 | Reserved Boundary |
| EVT-PRT-002 | PartnerRelationshipCreated | Partner | Partner Relationship Service | Phase 5 | Reserved Boundary |
| EVT-AGT-001 | AgentRegistered | Agent | Agent Registration Service | Phase 4 | Partial Implement |
| EVT-AGT-002 | AgentUpdated | Agent | Agent Registration Service | Phase 4 | Partial Implement |
| EVT-AGT-003 | AgentCapabilityUpdated | Agent / Capability | Agent Capability Service | Phase 4 | Partial Implement |
| EVT-SP-001 | ServiceProviderRegistered | Service Provider | Service Provider Registration Service | Phase 4 | Partial Implement |
| EVT-SP-002 | ServiceProviderCapabilityUpdated | Service Provider / Capability | Service Provider Lookup Service | Phase 4 | Partial Implement |
| EVT-SN-001 | ServiceNetworkReserved | Service Network | Service Network Boundary Service | Phase 5 | Reserved Boundary |
| EVT-SN-002 | NetworkMembershipCreated | Service Network | Network Membership Baseline Service | Phase 5 | Reserved Boundary |
| EVT-RT-001 | RoutingRecommendationGenerated | Routing / AI Governance | Routing Recommendation Service | Phase 4 | Partial Implement |
| EVT-RT-002 | RoutingReviewRequired | Routing / Business Responsibility | Routing Review Service | Phase 4 | Partial Implement |
| EVT-RT-003 | RoutingDecisionMade | Routing | Routing Decision Service | Phase 4 | Partial Implement |
| EVT-COMM-001 | CommunicationLinked | Communication | Communication Link Service | Phase 4 | Partial Implement |
| EVT-COMM-002 | CommunicationSummaryGenerated | Communication / AI Governance | Communication Summary Service | Phase 4 | Partial Implement |
| EVT-COMM-003 | CommunicationActionItemDetected | Communication / Task | Communication Action Item Service | Phase 4 | Partial Implement |
| EVT-COMM-004 | CommunicationLinkedToMatter | Communication / Matter | Communication Link Service | Phase 4 | Partial Implement |

## 8.5 Cross-Cutting and AI Governance Event Summary

| Event ID | Event Name | Source Domain/System | Source Service | MVP Phase/Wave | MVP Depth |
|---------|------------|----------------------|----------------|----------------|-----------|
| EVT-CAP-001 | CapabilityRegistered | Capability | Capability Registration Service | Phase 1 | Partial Implement |
| EVT-CAP-002 | CapabilityUpdated | Capability | Capability Validation Service | Phase 1 | Partial Implement |
| EVT-CAP-003 | CapabilityMatched | Capability | Capability Matching Service | Phase 4 | Partial Implement |
| EVT-BR-001 | ResponsibilityAssigned | Business Responsibility | Responsibility Assignment Service | Phase 3 | Must Implement |
| EVT-BR-002 | ReviewRequired | Business Responsibility | Review Assignment Service | Phase 3 | Must Implement |
| EVT-BR-003 | ReviewApproved | Business Responsibility | Approval Service | Phase 3 | Must Implement |
| EVT-BR-004 | ReviewRejected | Business Responsibility | Approval Service | Phase 3 | Must Implement |
| EVT-BR-005 | EscalationRequired | Business Responsibility | Escalation Baseline Service | Phase 3 | Partial Implement |
| EVT-AI-001 | AgentContractValidated | AI Governance | Agent Contract Validation Service | Phase 4 | Must Implement |
| EVT-AI-002 | AgentContractValidationFailed | AI Governance | Agent Contract Validation Service | Phase 4 | Must Implement |
| EVT-AI-003 | AIOutputGenerated | AI Governance | AI Output Registration Service | Phase 4 | Must Implement |
| EVT-AI-004 | AIRecommendationGenerated | AI Governance | AI Recommendation Registration Service | Phase 4 | Must Implement |
| EVT-AI-005 | AIReviewRequired | AI Governance / Business Responsibility | AI Review Routing Service | Phase 4 | Must Implement |
| EVT-AI-006 | AIUsagePolicyViolationDetected | AI Governance / Policy | AI Risk Policy Check Service | Phase 4 | Must Implement |
| EVT-AI-007 | AIAuditRecordCreated | AI Governance | AI Audit Recording Service | Phase 4 | Must Implement |

## 8.6 Codex and Validation Event Summary

| Event ID | Event Name | Source Domain/System | Source Service | Wave | MVP Depth |
|---------|------------|----------------------|----------------|------|-----------|
| EVT-CX-001 | CodexTaskStarted | Codex Task System | Codex Task Execution Service | Wave 0–7 | Partial Implement |
| EVT-CX-002 | CodexTaskImplemented | Codex Task System | Codex Task Execution Service | Wave 0–7 | Partial Implement |
| EVT-CX-003 | CodexTaskTested | Codex Task System | Codex Task Validation Service | Wave 0–7 | Partial Implement |
| EVT-CX-004 | CodexTaskBlocked | Codex Task System | Codex Task Validation Service | Wave 0–7 | Partial Implement |
| EVT-CX-005 | CodexTaskAccepted | Codex Task System | Codex Task Validation Service | Wave 0–7 | Partial Implement |
| EVT-CX-006 | SpecConsistencyIssueDetected | Specification Governance | Spec Consistency Check Service | Wave 0 / 7 | Partial Implement |
| EVT-CX-007 | SpecReviewRequired | Specification Governance | Spec Consistency Check Service | Wave 0 / 7 | Partial Implement |
| EVT-CX-008 | ProhibitedOverreachDetected | Specification Governance | Prohibited Overreach Check Service | Wave 0 / 7 | Must Implement |
| EVT-CX-009 | ReleaseCandidateReportGenerated | Release Governance | Release Validation Service | Wave 7 | Partial Implement |

---

# 9. High-Priority MVP Events

The following events form the minimum executable event baseline.

```text
IdentityCreated
OrganizationCreated
OrganizationMembershipChanged
UserCreated
UserRoleAssigned
PermissionGranted
PermissionRevoked
PermissionCheckFailed
PolicyViolationDetected
KnowledgeSourceAdded
KnowledgeAssetValidated
BrandCreated
BrandLinkedToTrademark
TrademarkCreated
TrademarkStatusChanged
TrademarkLinkedToMatter
JurisdictionAdded
ClassificationRecommendationGenerated
ClassificationReviewRequired
ClassificationRecommendationApproved
ClassificationRecommendationRejected
DocumentUploaded
CustomerCreated
CustomerLinkedToOrder
CustomerLinkedToMatter
OrderCreated
OrderConfirmed
OrderConvertedToMatter
MatterCreated
MatterStatusChanged
WorkflowContractCreated
WorkflowTransitionRequested
WorkflowTransitionApproved
WorkflowTransitionRejected
TaskCreated
TaskAssigned
TaskCompleted
TaskReviewRequired
EventPublished
EventValidationFailed
ResponsibilityAssigned
ReviewRequired
ReviewApproved
ReviewRejected
AgentContractValidated
AgentContractValidationFailed
AIOutputGenerated
AIRecommendationGenerated
AIReviewRequired
AIUsagePolicyViolationDetected
AIAuditRecordCreated
ProhibitedOverreachDetected
```

---

# 10. Event Payload Contract Rules

Every implementation-ready Core Event must have a payload contract.

A payload contract should include:

```text
event_id
event_name
event_version
occurred_at
source_service
source_domain_or_system
actor_identity
correlation_id
related_object_ids
payload
audit_reference
review_reference
permission_context
policy_context
consumer_scope
```

High-risk events must include:

```text
risk_level
review_required
review_status
human_reviewer
ai_agent_id if AI-assisted
agent_contract_id if AI-assisted
knowledge_source_reference if AI-assisted
```

---

# 11. Event Source Rules

Every Core Event must have one of the following source types.

```text
Core Service
External Source
System Agent
AI Agent through governed service
Codex Task Service
Validation Service
```

An AI Agent must not emit Core Events directly without a governed service.

A product UI must not emit Core Events directly without a governed service.

A database trigger must not be treated as a Core Event source unless wrapped by a governed service.

---

# 12. Event Consumer Rules

Event consumers must be classified.

Consumer categories include:

```text
Core Service Consumer
Workflow Consumer
Product Consumer
AI Agent Consumer
Notification Consumer
Audit Consumer
Integration Consumer
Codex Consumer
Reporting Consumer
```

Consumer access must respect:

```text
permission
policy
data exposure rules
review status
consumer classification
MVP depth
```

---

# 13. AI Governance Event Rules

AI-related events must preserve governance.

AI events require:

```text
AI Agent Identity
Agent Contract
AI Output
AI Audit Record
Review Rule
Policy Rule
Permission Check
Authorized Knowledge Reference
```

AI governance events include:

```text
AgentContractValidated
AgentContractValidationFailed
AIOutputGenerated
AIRecommendationGenerated
AIReviewRequired
AIUsagePolicyViolationDetected
AIAuditRecordCreated
```

AI output must not be treated as final professional truth unless review has been completed where required.

---

# 14. Workflow Event Rules

Workflow-related events must preserve execution integrity.

Workflow events include:

```text
WorkflowContractCreated
WorkflowTransitionRequested
WorkflowTransitionApproved
WorkflowTransitionRejected
TaskCreated
TaskAssigned
TaskCompleted
TaskReviewRequired
MatterStatusChanged
OrderConvertedToMatter
ReviewRequired
ReviewApproved
ReviewRejected
```

Workflow event rules:

```text
state transitions must reference Workflow Contract
task changes must reference Task
review events must reference Review Record
approval events must reference Approval Record
matter events must reference Matter
order conversion events must reference Order and Matter
```

---

# 15. Audit Requirements

Audit is required for events involving:

```text
permission failure
policy violation
AI output
AI recommendation
classification recommendation
document draft
evidence review
routing recommendation
review requirement
approval or rejection
responsibility assignment
workflow transition
order-to-matter conversion
Codex task implementation
prohibited overreach
```

Audit may be optional for low-risk reference updates, unless policy requires otherwise.

---

# 16. API Side-Effect Rules

API endpoints that mutate Core state must map to Core Events.

Examples:

```text
create identity
    → IdentityCreated

confirm order
    → OrderConfirmed

convert order to matter
    → OrderConvertedToMatter
    → MatterCreated

generate classification recommendation
    → ClassificationRecommendationGenerated
    → ClassificationReviewRequired

validate agent contract
    → AgentContractValidated
    or AgentContractValidationFailed
```

APIs must not hide state changes.

---

# 17. Deferred Event Scope

The following event groups are deferred or reserved.

```text
full external office sync events
advanced evidence scoring events
automatic legal strategy events
full marketplace transaction events
full partner commission events
full network trust score events
advanced analytics events
marketing automation events
autonomous AI filing events
automatic client outreach events
```

Deferred events must not be implemented through MVP task shortcuts.

---

# 18. Validation Rules

The event index must pass the following validation checks.

```text
[ ] Every event has an Event ID.
[ ] Every event has a name.
[ ] Every event name uses meaningful past-tense form.
[ ] Every event has a source domain or system.
[ ] Every event has a source service or explicit external source.
[ ] Every event has a payload contract requirement.
[ ] Every event has related objects.
[ ] Every event has consumer classification.
[ ] Every event has MVP phase or wave.
[ ] Every event has MVP depth.
[ ] Every AI event has Agent Contract requirement.
[ ] Every AI event has audit requirement.
[ ] Every high-risk event has review or audit rule.
[ ] No event is only a log.
[ ] No event is only a UI action.
[ ] No event is only an analytics ping.
[ ] No event silently expands deferred scope.
```

---

# 19. Prohibited Event Changes

This index must not be changed to:

```text
treat logs as Core Events
treat UI clicks as Core Events
treat analytics pings as Core Events
create events without source services
create events without payload contracts
create AI events without Agent Contract
create AI events without audit
create mutating API behavior without events
hide high-risk state changes
rename canonical events without architecture review
implement deferred event groups in MVP
```

---

# 20. Handoff to core-specs/events/

This index will generate future files under:

```text
core-specs/events/
```

Expected scaffold:

```text
core-specs/events/README.md
core-specs/events/_template.md
core-specs/events/foundation/
core-specs/events/professional/
core-specs/events/business-execution/
core-specs/events/collaboration-network/
core-specs/events/cross-cutting/
core-specs/events/ai-governance/
core-specs/events/codex/
```

Initial detailed event specs should prioritize:

```text
identity-created.md
permission-check-failed.md
knowledge-asset-validated.md
trademark-status-changed.md
classification-recommendation-generated.md
classification-review-required.md
document-uploaded.md
order-created.md
order-confirmed.md
order-converted-to-matter.md
matter-created.md
matter-status-changed.md
workflow-transition-requested.md
workflow-transition-approved.md
task-created.md
task-assigned.md
task-completed.md
task-review-required.md
event-published.md
responsibility-assigned.md
review-required.md
review-approved.md
review-rejected.md
agent-contract-validated.md
ai-output-generated.md
ai-review-required.md
ai-audit-record-created.md
prohibited-overreach-detected.md
```

---

# 21. Handoff to api-index.md

The next index should be checked against this event index.

```text
indexes/api-index.md
```

Each API that mutates Core state must specify:

```text
events emitted
payload contract
permission requirement
policy requirement
audit requirement
consumer classification
```

An API that mutates Core state without an event mapping is not implementation-ready.

---

# 22. Acceptance Criteria

This index is accepted only if it satisfies the following criteria.

```text
[ ] It defines Core Event as meaningful change.
[ ] It distinguishes Core Event from log, UI action, activity feed, queue message and analytics ping.
[ ] It defines event index fields.
[ ] It defines event naming rules.
[ ] It lists Foundation Events.
[ ] It lists Professional Events.
[ ] It lists Business Execution Events.
[ ] It lists Collaboration Network Events.
[ ] It lists Cross-Cutting Events.
[ ] It lists AI Governance Events.
[ ] It lists Codex and Validation Events.
[ ] It identifies high-priority MVP Events.
[ ] It defines payload contract rules.
[ ] It defines event source rules.
[ ] It defines event consumer rules.
[ ] It defines AI governance event rules.
[ ] It defines workflow event rules.
[ ] It defines audit requirements.
[ ] It defines API side-effect rules.
[ ] It defines deferred event scope.
[ ] It defines validation rules.
[ ] It defines prohibited event changes.
[ ] It prepares core-specs/events/.
[ ] It hands off to api-index.md.
```

---

# 23. Revision Notes

| Version | Status | Notes |
|---------|--------|-------|
| 0.1.0 | Draft | Initial operational Event Index derived from B02-APP-E. Defines event semantics, naming rules, source services, payload contract rules, AI governance events, workflow events, API side-effect rules, validation rules and handoff to api-index.md. |

---

**End of Index**
