# Book 02 — Appendix E

# Event Index

**Book Title:** MarkOrbit Core Specification  
**Appendix ID:** B02-APP-E  
**Appendix Title:** Event Index  
**Appendix Type:** Canonical Index  
**Rewrite Stage:** Second Canonical Draft  
**Status:** Draft  
**Version:** 0.2.0  
**Owner:** MarkOrbit Publications Editorial Board  

**Related Documents:**

- B02-CH-16 — Core Execution Primitives
- B02-CH-17 — Core Contract Architecture
- B02-CH-22 — Domain Specification
- B02-CH-23 — Object Specification
- B02-CH-24 — Service Specification
- B02-CH-25 — Event Specification
- B02-CH-26 — AI Capability and Agent Governance Specification
- B02-CH-27 — Core Consumption Specification
- B02-CH-30 — MVP Execution Matrix
- B02-APP-A — Glossary
- B02-APP-B — Core Domain Index
- B02-APP-C — Core Object Index
- B02-APP-D — Core Service Index

---

# 1. Appendix Purpose

This appendix defines the canonical Event Index for the MarkOrbit Core.

The purpose of the Event Index is to make meaningful Core changes visible, contract-bound, auditable and consumable.

Book 02 defines a Core Event as:

```text
A Core Event is a meaningful change in Core state, professional execution, review requirement, AI output, routing decision, communication linkage or workflow progress.
```

This appendix lists the baseline Events that should guide:

```text
core-specs/events/
core-specs/contracts/event-contracts/
core-specs/services/
core-specs/workflows/
core-specs/agents/
indexes/event-index.md
Codex task generation
```

The Event Index does not define final payload schemas.

Payload schemas belong to detailed Event Specifications under `core-specs/events/`.

---

# 2. Canonical Event Rule

The canonical Event Rule is:

```text
Event before coordination.
Meaningful change before downstream action.
Semantic event before queue message.
```

Events are required when Core state, professional execution, AI review, routing, communication or workflow progress changes in a way that another actor or system may need to know.

---

# 3. What Is Not an Event

A Core Event is not:

```text
a log line
a UI click
an activity feed row
a queue message
an analytics ping
a temporary frontend state
a database trigger by itself
a notification by itself
a report metric by itself
```

Those artifacts may be derived from Events or may transport Events.

They do not define Event meaning.

---

# 4. Event Naming Rules

## 4.1 Event Name

Event names use PascalCase.

Examples:

```text
MatterCreated
TaskAssigned
AIRecommendationReviewRequired
RoutingDecisionMade
```

## 4.2 Event File Name

Event specification files use lowercase kebab-case.

Examples:

```text
matter-created.md
task-assigned.md
ai-recommendation-review-required.md
routing-decision-made.md
```

## 4.3 Event Tense

Event names should use completed semantic tense.

Preferred:

```text
OrderCreated
MatterStatusChanged
DocumentUploaded
ReviewApproved
```

Avoid:

```text
CreateOrder
ChangeMatterStatus
UploadDocument
ApproveReview
```

The Event reports that something meaningful has happened.

It is not the command itself.

---

# 5. Event Index Fields

Each Event Index entry should include:

```text
Event Name
File Name
Source Domain or Source System
Event Category
Trigger
Related Objects
Payload Contract
Downstream Consumers
AI Usage
Workflow Usage
Audit Requirement
MVP Phase
MVP Depth
Deferred Notes
```

Detailed `core-specs/events/` files should later expand these fields into complete specifications.

---

# 6. Event Categories

Book 02 uses the following Event categories.

```text
Lifecycle Event
State Change Event
Assignment Event
Review Event
Document Event
Knowledge Event
AI Event
Workflow Event
Routing Event
Communication Event
Notification Event
Integration Event
Audit Event
Governance Event
```

These categories are used for indexing.

They do not replace source-domain ownership.

---

# 7. Event Ownership Rule

Every Event must have a source domain or source system.

```text
Event source ownership must be explicit.
Event consumers may be many.
Event ownership must be one primary source.
```

Examples:

```text
TrademarkCreated
    source domain: Trademark

TaskAssigned
    source domain: Task

AIRecommendationGenerated
    source system: AI Governance

ReviewRequired
    source system: Business Responsibility / Workflow Contract
```

Where an Event crosses domains, the detailed Event Specification must declare the primary source owner.

---

# 8. Event Consumer Rule

Consumers may subscribe to Events only through an Event Contract.

Consumers include:

```text
Products
Workplace
AI agents
internal services
external integrations
reporting systems
notification services
Codex-generated implementation
```

Consumers must not reinterpret Event meaning.

A consumer may react differently to an Event.

It may not redefine what the Event means.

---

# 9. Event Payload Rule

Every Event must have a payload contract.

A payload contract should define:

```text
event identity
source domain
source object
actor or system source
occurred time
related objects
exposed fields
sensitivity level
permission requirement
idempotency key
audit metadata
consumer restrictions
```

The payload should expose enough meaning for downstream coordination.

It should not expose private internal implementation details.

---

# 10. MVP Event Depth

Events use MVP depth classification.

```text
Must Implement
Partial Implement
Reserved Boundary
Deferred
```

## 10.1 Must Implement

Events required by first executable Core consumers.

## 10.2 Partial Implement

Events that need baseline definition and limited implementation.

## 10.3 Reserved Boundary

Events that prepare future architecture but should not be implemented deeply in MVP.

## 10.4 Deferred

Events that belong to future products, marketplace, analytics, advanced AI or advanced integrations.

---

# 11. Foundation Event Index

Foundation Events support identity, organization, user, permission, policy and knowledge foundations.

| Event Name | File Name | Source | Category | MVP Phase | MVP Depth | Primary Consumers |
|---|---|---|---|---|---|---|
| IdentityCreated | identity-created.md | Identity | Lifecycle | Phase 1 | Must Implement | Workplace, Products, Audit |
| IdentityUpdated | identity-updated.md | Identity | State Change | Phase 1 | Must Implement | Permission, Audit, Workplace |
| OrganizationCreated | organization-created.md | Organization | Lifecycle | Phase 1 | Must Implement | Products, Workplace, Customer |
| OrganizationUpdated | organization-updated.md | Organization | State Change | Phase 1 | Must Implement | Products, Workplace, Audit |
| UserCreated | user-created.md | User | Lifecycle | Phase 1 | Must Implement | Workplace, Permission, Audit |
| UserRoleAssigned | user-role-assigned.md | User / Permission | Assignment | Phase 1 | Must Implement | Permission, Audit, Workplace |
| UserDeactivated | user-deactivated.md | User | State Change | Phase 1 | Must Implement | Permission, Workplace, Audit |
| PermissionGranted | permission-granted.md | Permission | Governance | Phase 1 | Must Implement | Audit, Workplace, Products |
| PermissionRevoked | permission-revoked.md | Permission | Governance | Phase 1 | Must Implement | Audit, Workplace, Products |
| PolicyRuleCreated | policy-rule-created.md | Policy | Governance | Phase 1 | Partial Implement | Services, AI Governance, Audit |
| PolicyRuleUpdated | policy-rule-updated.md | Policy | Governance | Phase 1 | Partial Implement | Services, AI Governance, Audit |
| KnowledgeSourceCreated | knowledge-source-created.md | Knowledge | Lifecycle | Phase 1 | Must Implement | AI Agents, Knowledge Services |
| KnowledgeAssetCreated | knowledge-asset-created.md | Knowledge | Lifecycle | Phase 1 | Must Implement | AI Agents, Products, Workplace |
| KnowledgeAssetUpdated | knowledge-asset-updated.md | Knowledge | State Change | Phase 1 | Must Implement | AI Agents, Knowledge Services |
| KnowledgeGapIdentified | knowledge-gap-identified.md | Knowledge | Knowledge Event | Phase 1 | Partial Implement | AI Agents, Review, Workplace |
| KnowledgeValidationRequired | knowledge-validation-required.md | Knowledge | Review Event | Phase 1 | Partial Implement | Reviewers, Workplace, AI Governance |
| KnowledgeValidated | knowledge-validated.md | Knowledge | Review Event | Phase 1 | Partial Implement | AI Agents, Products, Audit |

## 11.1 Foundation Event Notes

Foundation Events are security-sensitive.

They must include audit metadata.

Permission and policy Events must not expose private role internals to unauthorized consumers.

Knowledge Events must indicate validation status because AI consumption depends on authorized and validated knowledge.

---

# 12. Professional Event Index

Professional Events support Brand, Trademark, Jurisdiction, Classification, Document and Evidence.

| Event Name | File Name | Source | Category | MVP Phase | MVP Depth | Primary Consumers |
|---|---|---|---|---|---|---|
| BrandCreated | brand-created.md | Brand | Lifecycle | Phase 2 | Must Implement | Lite, MarkReg, Customer |
| BrandUpdated | brand-updated.md | Brand | State Change | Phase 2 | Must Implement | Lite, MarkReg, Workplace |
| TrademarkCreated | trademark-created.md | Trademark | Lifecycle | Phase 2 | Must Implement | MarkReg, Lite, Workplace |
| TrademarkUpdated | trademark-updated.md | Trademark | State Change | Phase 2 | Must Implement | MarkReg, Workplace, Reporting |
| TrademarkStatusChanged | trademark-status-changed.md | Trademark | State Change | Phase 2 | Must Implement | MarkReg, Workplace, Notification |
| TrademarkOwnerChanged | trademark-owner-changed.md | Trademark | State Change | Phase 2 | Partial Implement | MarkReg, Audit, Document |
| TrademarkGoodsServicesUpdated | trademark-goods-services-updated.md | Trademark | State Change | Phase 2 | Partial Implement | Classification, MarkReg, Audit |
| JurisdictionCreated | jurisdiction-created.md | Jurisdiction | Lifecycle | Phase 2 | Must Implement | Knowledge, Lite, MarkReg |
| JurisdictionRequirementUpdated | jurisdiction-requirement-updated.md | Jurisdiction | Knowledge Event | Phase 2 | Must Implement | Lite, MarkReg, AI Agents |
| ClassificationTermAdded | classification-term-added.md | Classification | Lifecycle | Phase 2 | Must Implement | Lite, MarkReg, AI Agents |
| ClassificationRecommendationGenerated | classification-recommendation-generated.md | Classification / AI Governance | AI Event | Phase 2 | Must Implement | Lite, Reviewers, Audit |
| ClassificationReviewRequired | classification-review-required.md | Classification / Business Responsibility | Review Event | Phase 2 | Must Implement | Workplace, Reviewers, Lite |
| ClassificationApproved | classification-approved.md | Classification | Review Event | Phase 2 | Must Implement | Lite, MarkReg, Audit |
| ClassificationRejected | classification-rejected.md | Classification | Review Event | Phase 2 | Must Implement | Lite, MarkReg, Audit |
| DocumentUploaded | document-uploaded.md | Document | Document Event | Phase 2 | Must Implement | MarkReg, Workplace, Audit |
| DocumentGenerated | document-generated.md | Document | Document Event | Phase 2 | Must Implement | MarkReg, Lite, Workplace |
| DocumentRequirementIdentified | document-requirement-identified.md | Document / Jurisdiction | Knowledge Event | Phase 2 | Must Implement | Lite, MarkReg, AI Agents |
| DocumentReviewRequired | document-review-required.md | Document / Business Responsibility | Review Event | Phase 2 | Must Implement | Workplace, Reviewers, Audit |
| DocumentApproved | document-approved.md | Document | Review Event | Phase 2 | Must Implement | MarkReg, Workplace, Customer |
| DocumentRejected | document-rejected.md | Document | Review Event | Phase 2 | Must Implement | Workplace, MarkReg, Audit |
| EvidenceCreated | evidence-created.md | Evidence | Lifecycle | Phase 2 | Partial Implement | MarkReg, Workplace, AI Agents |
| EvidenceReviewRequired | evidence-review-required.md | Evidence / Business Responsibility | Review Event | Phase 2 | Partial Implement | Reviewers, Workplace, Audit |
| EvidenceApproved | evidence-approved.md | Evidence | Review Event | Phase 2 | Partial Implement | MarkReg, Workplace, Audit |
| EvidenceRejected | evidence-rejected.md | Evidence | Review Event | Phase 2 | Partial Implement | MarkReg, Workplace, Audit |

## 12.1 Professional Event Notes

Professional Events may carry legal or client-sensitive information.

Payloads must be limited to contract-approved fields.

AI-generated professional recommendations must be tied to review and audit Events where risk requires human judgment.

---

# 13. Business Execution Event Index

Business Execution Events support Customer, Order, Matter, Opportunity, Workflow Contract, Task, Event and Notification.

| Event Name | File Name | Source | Category | MVP Phase | MVP Depth | Primary Consumers |
|---|---|---|---|---|---|---|
| CustomerCreated | customer-created.md | Customer | Lifecycle | Phase 3 | Must Implement | MarkReg, Lite, Workplace |
| CustomerUpdated | customer-updated.md | Customer | State Change | Phase 3 | Must Implement | Products, Workplace, Audit |
| OrderCreated | order-created.md | Order | Lifecycle | Phase 3 | Must Implement | Lite, MarkReg, Workplace |
| OrderConfirmed | order-confirmed.md | Order | State Change | Phase 3 | Must Implement | Matter, Workflow, Workplace |
| OrderCancelled | order-cancelled.md | Order | State Change | Phase 3 | Must Implement | Products, Workplace, Audit |
| OrderConvertedToMatter | order-converted-to-matter.md | Order / Matter / Workflow Contract | Workflow Event | Phase 3 | Must Implement | Matter, Workplace, MarkReg |
| MatterCreated | matter-created.md | Matter | Lifecycle | Phase 3 | Must Implement | Workplace, MarkReg, Task |
| MatterUpdated | matter-updated.md | Matter | State Change | Phase 3 | Must Implement | Workplace, MarkReg, Audit |
| MatterStatusChanged | matter-status-changed.md | Matter | State Change | Phase 3 | Must Implement | Workplace, Notification, Reporting |
| MatterClosed | matter-closed.md | Matter | State Change | Phase 3 | Must Implement | Workplace, MarkReg, Audit |
| WorkflowContractCreated | workflow-contract-created.md | Workflow Contract | Lifecycle | Phase 3 | Must Implement | Workplace, Codex, Services |
| WorkflowStateChanged | workflow-state-changed.md | Workflow Contract | Workflow Event | Phase 3 | Must Implement | Workplace, Task, Notification |
| WorkflowTransitionBlocked | workflow-transition-blocked.md | Workflow Contract / Policy | Governance | Phase 3 | Partial Implement | Workplace, Audit, Services |
| TaskCreated | task-created.md | Task | Lifecycle | Phase 3 | Must Implement | Workplace, Notification, Audit |
| TaskAssigned | task-assigned.md | Task | Assignment Event | Phase 3 | Must Implement | Workplace, Notification, User |
| TaskReassigned | task-reassigned.md | Task | Assignment Event | Phase 3 | Must Implement | Workplace, Notification, Audit |
| TaskDueDateChanged | task-due-date-changed.md | Task | State Change | Phase 3 | Partial Implement | Workplace, Notification, Audit |
| TaskCompleted | task-completed.md | Task | State Change | Phase 3 | Must Implement | Workflow, Matter, Workplace |
| TaskBlocked | task-blocked.md | Task | State Change | Phase 3 | Partial Implement | Workplace, Notification, Review |
| ReviewRequired | review-required.md | Business Responsibility / Workflow Contract | Review Event | Phase 3 | Must Implement | Workplace, Reviewers, AI Agents |
| ReviewAssigned | review-assigned.md | Business Responsibility | Assignment Event | Phase 3 | Must Implement | Workplace, Reviewers, Notification |
| ReviewApproved | review-approved.md | Business Responsibility | Review Event | Phase 3 | Must Implement | Workflow, Audit, Products |
| ReviewRejected | review-rejected.md | Business Responsibility | Review Event | Phase 3 | Must Implement | Workflow, Audit, Products |
| ResponsibilityAssigned | responsibility-assigned.md | Business Responsibility | Assignment Event | Phase 3 | Partial Implement | Workplace, Audit, Task |
| NotificationCreated | notification-created.md | Notification | Notification Event | Phase 3 | Partial Implement | Workplace, Products, Users |
| NotificationSent | notification-sent.md | Notification | Notification Event | Phase 3 | Partial Implement | Users, Audit, Workplace |
| OpportunityCreated | opportunity-created.md | Opportunity | Lifecycle | Phase 4 | Partial Implement | MarkReg, Lite, Sales Workflow |
| OpportunityUpdated | opportunity-updated.md | Opportunity | State Change | Phase 4 | Partial Implement | Workplace, Products, Reporting |
| OpportunityReviewRequired | opportunity-review-required.md | Opportunity / Business Responsibility | Review Event | Phase 4 | Partial Implement | Workplace, Reviewers, AI Agents |

## 13.1 Business Execution Event Notes

Business Execution Events coordinate work.

They must be reliable, auditable and idempotent where they trigger downstream tasks, workflow transitions or notifications.

Review Events are especially important because they preserve professional responsibility.

---

# 14. Collaboration Network Event Index

Collaboration Network Events support Partner, Agent, Service Provider, Service Network, Routing and Communication.

| Event Name | File Name | Source | Category | MVP Phase | MVP Depth | Primary Consumers |
|---|---|---|---|---|---|---|
| PartnerCreated | partner-created.md | Partner | Lifecycle | Phase 5 | Reserved Boundary | MGSN, Admin, Audit |
| PartnerUpdated | partner-updated.md | Partner | State Change | Phase 5 | Reserved Boundary | MGSN, Audit |
| AgentCreated | agent-created.md | Agent | Lifecycle | Phase 4 | Partial Implement | MarkReg, MGSN, Routing |
| AgentUpdated | agent-updated.md | Agent | State Change | Phase 4 | Partial Implement | MarkReg, Routing, Audit |
| AgentCapabilityUpdated | agent-capability-updated.md | Agent / Capability | State Change | Phase 4 | Partial Implement | Routing, MGSN, MarkReg |
| ServiceProviderCreated | service-provider-created.md | Service Provider | Lifecycle | Phase 4 | Partial Implement | MGSN, Routing, Products |
| ServiceProviderUpdated | service-provider-updated.md | Service Provider | State Change | Phase 4 | Partial Implement | MGSN, Routing, Audit |
| ServiceNetworkCreated | service-network-created.md | Service Network | Lifecycle | Phase 5 | Reserved Boundary | MGSN, Governance |
| ServiceNetworkPolicyUpdated | service-network-policy-updated.md | Service Network / Policy | Governance | Phase 5 | Reserved Boundary | MGSN, Audit |
| RoutingRequested | routing-requested.md | Routing | Routing Event | Phase 4 | Partial Implement | MarkReg, Workplace, AI Agents |
| RoutingRecommendationGenerated | routing-recommendation-generated.md | Routing / AI Governance | AI Event | Phase 4 | Partial Implement | Workplace, Reviewers, MarkReg |
| RoutingReviewRequired | routing-review-required.md | Routing / Business Responsibility | Review Event | Phase 4 | Partial Implement | Workplace, Reviewers, Audit |
| RoutingDecisionMade | routing-decision-made.md | Routing | Routing Event | Phase 4 | Partial Implement | MarkReg, Agent, Communication |
| RoutingDecisionRejected | routing-decision-rejected.md | Routing | Review Event | Phase 4 | Partial Implement | Workplace, Routing, Audit |
| CommunicationCreated | communication-created.md | Communication | Communication Event | Phase 4 | Partial Implement | MarkReg, Workplace, Agent |
| CommunicationLinked | communication-linked.md | Communication | Communication Event | Phase 4 | Partial Implement | Matter, Task, Agent, Audit |
| CommunicationSummaryGenerated | communication-summary-generated.md | Communication / AI Governance | AI Event | Phase 4 | Partial Implement | Workplace, MarkReg, Reviewers |
| CommunicationReviewRequired | communication-review-required.md | Communication / Business Responsibility | Review Event | Phase 4 | Partial Implement | Reviewers, Workplace, Audit |

## 14.1 Collaboration Network Event Notes

Collaboration Network Events should not force full MGSN marketplace implementation into the Core MVP.

Most network Events are partial or reserved.

Routing and Communication are the most useful early collaboration Events because they support MarkReg and Workplace execution.

---

# 15. AI Governance Event Index

AI Events are source-system events tied to governed AI execution.

They do not replace domain Events.

They describe AI activity, output, review and audit.

| Event Name | File Name | Source | Category | MVP Phase | MVP Depth | Primary Consumers |
|---|---|---|---|---|---|---|
| AIAgentCreated | ai-agent-created.md | AI Governance | Lifecycle | Phase 1 | Must Implement | AI Governance, Audit, Codex |
| AIAgentContractCreated | ai-agent-contract-created.md | AI Governance | Governance | Phase 1 | Must Implement | AI Agents, Products, Audit |
| AIAgentContractUpdated | ai-agent-contract-updated.md | AI Governance | Governance | Phase 1 | Must Implement | AI Agents, Products, Audit |
| AIInvocationRequested | ai-invocation-requested.md | AI Governance | AI Event | Phase 1 | Partial Implement | AI Services, Audit |
| AIInvocationCompleted | ai-invocation-completed.md | AI Governance | AI Event | Phase 1 | Partial Implement | AI Services, Audit |
| AIInvocationFailed | ai-invocation-failed.md | AI Governance | AI Event | Phase 1 | Partial Implement | AI Services, Audit, Workplace |
| AIOutputGenerated | ai-output-generated.md | AI Governance | AI Event | Phase 1 | Must Implement | Products, Workplace, Audit |
| AIRecommendationGenerated | ai-recommendation-generated.md | AI Governance | AI Event | Phase 1 | Must Implement | Products, Workplace, Reviewers |
| AIRecommendationReviewRequired | ai-recommendation-review-required.md | AI Governance / Business Responsibility | Review Event | Phase 1 | Must Implement | Workplace, Reviewers, Audit |
| AIRecommendationApproved | ai-recommendation-approved.md | AI Governance / Business Responsibility | Review Event | Phase 1 | Must Implement | Products, Audit, Workflow |
| AIRecommendationRejected | ai-recommendation-rejected.md | AI Governance / Business Responsibility | Review Event | Phase 1 | Must Implement | Products, Audit, Workflow |
| AIOutputExpired | ai-output-expired.md | AI Governance | State Change | Phase 1 | Partial Implement | Products, Workplace, Audit |
| AIOutputSuperseded | ai-output-superseded.md | AI Governance | State Change | Phase 1 | Partial Implement | Products, Workplace, Audit |
| AIAuditRecordCreated | ai-audit-record-created.md | AI Governance | Audit Event | Phase 1 | Must Implement | Audit, Governance, Review |
| AIKnowledgeAccessDenied | ai-knowledge-access-denied.md | AI Governance / Knowledge | Governance | Phase 1 | Partial Implement | Audit, AI Governance |
| AIObjectAccessDenied | ai-object-access-denied.md | AI Governance / Permission | Governance | Phase 1 | Partial Implement | Audit, Permission, AI Governance |

## 15.1 AI Event Notes

AI Events must include:

```text
agent identity
agent contract version
authorized knowledge reference
input context reference
output reference
risk level
review requirement
audit reference
consumer binding
```

AI Events must not expose sensitive prompt or context details unless allowed by contract.

AI output does not become professional truth merely because an AI Event exists.

---

# 16. API and Integration Event Index

API and Integration Events should be limited in MVP.

They are useful for contract enforcement, audit and synchronization.

| Event Name | File Name | Source | Category | MVP Phase | MVP Depth | Primary Consumers |
|---|---|---|---|---|---|---|
| APIContractCreated | api-contract-created.md | API / Contract | Governance | Phase 3 | Partial Implement | Codex, Products, Audit |
| APIContractUpdated | api-contract-updated.md | API / Contract | Governance | Phase 3 | Partial Implement | Codex, Products, Audit |
| APIAccessGranted | api-access-granted.md | API / Permission | Governance | Phase 3 | Partial Implement | Integrations, Audit |
| APIAccessRevoked | api-access-revoked.md | API / Permission | Governance | Phase 3 | Partial Implement | Integrations, Audit |
| ExternalIntegrationConnected | external-integration-connected.md | External Integration | Integration Event | Future | Deferred | Integration Consumers |
| ExternalIntegrationDisconnected | external-integration-disconnected.md | External Integration | Integration Event | Future | Deferred | Integration Consumers |
| ExternalDataImported | external-data-imported.md | External Integration | Integration Event | Future | Deferred | Data Services, Audit |
| ExternalDataSyncFailed | external-data-sync-failed.md | External Integration | Integration Event | Future | Deferred | Integration Services, Audit |
| DataExportRequested | data-export-requested.md | Data / Reporting | Integration Event | Future | Deferred | Reporting, Audit |
| DataExportCompleted | data-export-completed.md | Data / Reporting | Integration Event | Future | Deferred | Reporting, Audit |

## 16.1 API and Integration Event Notes

API Events are primarily governance Events.

External Integration Events are mostly deferred because full integration platform scope is not part of the Core MVP.

Appendix F must define API surfaces before integration Events expand.

---

# 17. Audit and Governance Event Index

Audit and Governance Events support traceability and architecture control.

| Event Name | File Name | Source | Category | MVP Phase | MVP Depth | Primary Consumers |
|---|---|---|---|---|---|---|
| AuditRecordCreated | audit-record-created.md | Audit | Audit Event | Phase 1 | Must Implement | Governance, Review, Compliance |
| CoreSpecCreated | core-spec-created.md | Specification Governance | Governance | After Appendices | Partial Implement | Codex, Editorial, Architecture |
| CoreSpecUpdated | core-spec-updated.md | Specification Governance | Governance | After Appendices | Partial Implement | Codex, Editorial, Architecture |
| CoreSpecApproved | core-spec-approved.md | Specification Governance | Governance | After Appendices | Partial Implement | Codex, Architecture |
| CoreSpecDeprecated | core-spec-deprecated.md | Specification Governance | Governance | Future | Deferred | Architecture, Codex |
| ArchitectureIssueCreated | architecture-issue-created.md | Architecture Governance | Governance | Phase 0 | Partial Implement | Editorial, Architecture |
| ArchitectureDecisionApproved | architecture-decision-approved.md | Architecture Governance | Governance | Phase 0 | Partial Implement | Editorial, Codex, Specs |
| DeferredScopeActivated | deferred-scope-activated.md | Architecture Governance | Governance | Future | Deferred | Architecture, Products, Codex |
| CodexTaskCreated | codex-task-created.md | Codex Task Governance | Governance | After Appendix H | Partial Implement | Codex, Editorial |
| CodexTaskAccepted | codex-task-accepted.md | Codex Task Governance | Governance | After Appendix H | Partial Implement | Codex, Release |
| CodexTaskRejected | codex-task-rejected.md | Codex Task Governance | Governance | After Appendix H | Partial Implement | Codex, Editorial |

## 17.1 Governance Event Notes

Governance Events are useful for architecture traceability.

They should not replace formal review documents.

They may be implemented later as repository automation or publication workflow support.

---

# 18. MVP Event Baseline

The following Events should be considered MVP baseline candidates.

## 18.1 Phase 1 — Foundation Core

```text
IdentityCreated
IdentityUpdated
OrganizationCreated
OrganizationUpdated
UserCreated
UserRoleAssigned
UserDeactivated
PermissionGranted
PermissionRevoked
KnowledgeSourceCreated
KnowledgeAssetCreated
KnowledgeAssetUpdated
AIAgentCreated
AIAgentContractCreated
AIAgentContractUpdated
AIOutputGenerated
AIRecommendationGenerated
AIRecommendationReviewRequired
AIAuditRecordCreated
AuditRecordCreated
```

## 18.2 Phase 2 — Professional Core

```text
BrandCreated
BrandUpdated
TrademarkCreated
TrademarkUpdated
TrademarkStatusChanged
JurisdictionCreated
JurisdictionRequirementUpdated
ClassificationTermAdded
ClassificationRecommendationGenerated
ClassificationReviewRequired
ClassificationApproved
ClassificationRejected
DocumentUploaded
DocumentGenerated
DocumentRequirementIdentified
DocumentReviewRequired
DocumentApproved
DocumentRejected
```

## 18.3 Phase 3 — Business Execution Core

```text
CustomerCreated
CustomerUpdated
OrderCreated
OrderConfirmed
OrderCancelled
OrderConvertedToMatter
MatterCreated
MatterUpdated
MatterStatusChanged
MatterClosed
WorkflowContractCreated
WorkflowStateChanged
TaskCreated
TaskAssigned
TaskReassigned
TaskCompleted
ReviewRequired
ReviewAssigned
ReviewApproved
ReviewRejected
```

## 18.4 Phase 4 — Growth Core Baseline

```text
AgentCreated
AgentUpdated
AgentCapabilityUpdated
ServiceProviderCreated
ServiceProviderUpdated
RoutingRequested
RoutingRecommendationGenerated
RoutingReviewRequired
RoutingDecisionMade
CommunicationCreated
CommunicationLinked
CommunicationSummaryGenerated
OpportunityCreated
OpportunityUpdated
```

## 18.5 Phase 5 — Network Reserved

```text
PartnerCreated
PartnerUpdated
ServiceNetworkCreated
ServiceNetworkPolicyUpdated
```

These Phase 5 Events are reserved boundary Events.

They should not trigger full MGSN implementation unless approved.

---

# 19. Deferred Event Scope

The following Event types are deferred unless explicitly approved:

```text
full external integration lifecycle events
advanced marketplace transaction events
advanced provider ranking events
full opportunity scoring events
full brand asset vault analytics events
advanced reporting pipeline events
public developer webhook events
fully autonomous AI decision events
```

Deferred Events must not be introduced by Codex without source specification approval.

---

# 20. Event-to-Service Rule

A Core Service that changes meaningful state must declare Event side effects.

Every Service Specification should answer:

```text
Does this service emit an Event?
Which Event?
What is the source domain?
What object changed?
Who is the actor?
What payload contract applies?
Who may consume it?
Is audit required?
```

If a service creates, updates, approves, rejects, routes, reviews, assigns or closes Core meaning, it likely emits an Event.

---

# 21. Event-to-Workflow Rule

Workflow depends on Events.

Workflow transitions must declare whether they:

```text
consume an Event
emit an Event
require review before Event publication
trigger tasks
trigger notifications
trigger AI review
trigger audit
```

Workflow state must not be hidden inside UI.

---

# 22. Event-to-AI Rule

AI usage must emit or create audit-linked Events when it:

```text
generates a recommendation
generates a draft
generates a summary
requires review
is approved
is rejected
fails
accesses denied knowledge
accesses denied object context
```

AI Events must not bypass review rules.

AI Events must not expose unauthorized context.

---

# 23. Event-to-Notification Rule

Notifications may be triggered by Events.

But a Notification is not automatically the Event.

Example:

```text
TaskAssigned
    may trigger NotificationCreated and NotificationSent.

ReviewRequired
    may trigger NotificationCreated and NotificationSent.
```

Notification Events should reference source Events.

They should not replace source Events.

---

# 24. Event-to-Reporting Rule

Reporting consumes Events.

Reporting does not redefine Events.

If reporting requires a new metric, it should first determine whether the metric can be derived from existing Events.

If a meaningful Event is missing, reporting should request architecture review.

---

# 25. Event Contract Template

Each detailed Event Specification should follow this template.

```text
# Event Specification

1. Event Name
2. File Name
3. Source Domain or Source System
4. Event Category
5. Event Meaning
6. Trigger
7. Actor or Source
8. Related Objects
9. Payload Contract
10. Required Fields
11. Optional Fields
12. Sensitive Fields
13. Permission Rules
14. Policy Rules
15. Downstream Consumers
16. Workflow Effects
17. Notification Effects
18. AI Usage
19. Audit Requirement
20. Retention and Replay
21. Idempotency
22. Failure Behavior
23. MVP Phase
24. MVP Depth
25. Deferred Scope
26. Anti-Patterns
27. Acceptance Criteria
28. Revision Notes
```

---

# 26. Event Anti-Patterns

## 26.1 Log-as-Event

A log line is treated as a Core Event.

Correction:

```text
Define semantic change first.
```

## 26.2 UI-action-as-Event

A button click becomes an Event without Core state meaning.

Correction:

```text
Only meaningful Core changes should become Events.
```

## 26.3 Queue-message-as-Event

A transport message is treated as Event meaning.

Correction:

```text
Event meaning must be independent of transport infrastructure.
```

## 26.4 Analytics-ping-as-Event

Analytics tracking becomes Core Event.

Correction:

```text
Analytics consumes Events; it does not define them.
```

## 26.5 Event-without-source-domain

An Event has no owner.

Correction:

```text
Every Event must declare source domain or source system.
```

## 26.6 Event-without-contract

An Event is published without payload contract.

Correction:

```text
Event Contract is required before consumption.
```

## 26.7 Event-redefinition-by-consumer

A consumer interprets an Event differently from source specification.

Correction:

```text
Consumers may react differently, but may not redefine Event meaning.
```

## 26.8 AI-event-without-review

AI recommendation Events bypass review where risk requires human judgment.

Correction:

```text
AI recommendation Events must connect to review and audit.
```

---

# 27. Relationship to Appendix F — API Index

APIs may expose Events through:

```text
query endpoints
webhooks
event subscription APIs
notification APIs
integration APIs
reporting APIs
```

Appendix F must ensure API surfaces are contract-bound.

Public or external webhook Events are deferred unless explicitly approved.

---

# 28. Relationship to Appendix G — Agent Index

Appendix G must ensure every AI Agent declares Event behavior.

Agent entries should include:

```text
Events emitted
Events consumed
Review Events required
Audit Events required
Failure Events
Product consumers
```

AI Agents must not operate invisibly.

---

# 29. Relationship to Appendix H — Codex Task Index

Appendix H must ensure Codex tasks include Event requirements.

Codex tasks that implement services must specify:

```text
which Events are emitted
which Events are consumed
which tests verify Event publication
which payload contract applies
which downstream consumers are expected
which Events are out of scope
```

Codex must not invent Events outside Appendix E or approved Event Specifications.

---

# 30. Relationship to core-specs/events/

This appendix prepares the `core-specs/events/` scaffold.

Future event specs should be generated under:

```text
core-specs/events/foundation/
core-specs/events/professional/
core-specs/events/business-execution/
core-specs/events/collaboration-network/
core-specs/events/ai-governance/
core-specs/events/governance/
```

Each Event spec should use the Event Contract Template in this appendix.

---

# 31. Acceptance Criteria

This appendix is accepted only if it satisfies the following criteria.

```text
[ ] It defines Event as meaningful change.
[ ] It distinguishes Event from log, UI action, activity feed, queue message and analytics ping.
[ ] It defines Event naming rules.
[ ] It defines Event file naming rules.
[ ] It defines Event Index fields.
[ ] It defines Event categories.
[ ] It lists Foundation Events.
[ ] It lists Professional Events.
[ ] It lists Business Execution Events.
[ ] It lists Collaboration Network Events.
[ ] It lists AI Governance Events.
[ ] It lists API / Integration Events.
[ ] It lists Audit / Governance Events.
[ ] It identifies MVP baseline Events.
[ ] It identifies deferred Event scope.
[ ] It defines Event-to-Service, Event-to-Workflow, Event-to-AI, Event-to-Notification and Event-to-Reporting rules.
[ ] It provides an Event Contract Template.
[ ] It defines Event anti-patterns.
[ ] It prepares Appendix F, Appendix G and Appendix H.
[ ] It prepares core-specs/events/.
```

---

# 32. Revision Notes

| Version | Status | Notes |
|---------|--------|-------|
| 0.2.0 | Draft | Initial second canonical draft Event Index. Defines canonical Event rules, baseline Events, MVP depth, AI Events, API/Integration Events, governance Events and core-specs/events readiness. |

---

**End of Appendix**
