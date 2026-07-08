# Appendix D — Core Service Index

**Book:** Book 02 — MarkOrbit Core Specification  
**Appendix ID:** B02-APP-D  
**Appendix Title:** Core Service Index  
**Rewrite Stage:** Second Canonical Draft  
**Status:** Draft  
**Version:** 0.2.0  
**Owner:** MarkOrbit Publications Editorial Board  

**Related Documents:**

- B02-CH-15 — Core Service Architecture
- B02-CH-22 — Domain Specification
- B02-CH-23 — Object Specification
- B02-CH-24 — Service Specification
- B02-CH-25 — Event Specification
- B02-CH-26 — AI Capability and Agent Governance Specification
- B02-CH-27 — Core Consumption Specification
- B02-CH-28 — Core MVP Boundary
- B02-CH-29 — MVP Domain Priority
- B02-CH-30 — MVP Execution Matrix
- B02-APP-A — Glossary
- B02-APP-B — Core Domain Index
- B02-APP-C — Core Object Index

---

# 1. Purpose

This appendix defines the Core Service Index for Book 02.

A Core Service is a governed capability that operates Core meaning.

A Core Service is not a button, helper function, controller method, vendor wrapper, prompt, queue worker or product screen action.

The purpose of this appendix is to stabilize the initial service surface before detailed `core-specs/services/` files are generated.

This index supports:

```text
Appendix E — Event Index
Appendix F — API Index
Appendix G — Agent Index
Appendix H — Codex Task Index
core-specs/services/
core-specs/contracts/
core-specs/api/
Codex Wave 0–7 tasks
```

---

# 2. Canonical Service Rule

The canonical service rule is:

```text
A Core Service operates approved Core Objects, under domain ownership, through explicit contracts, permissions, events, review and audit rules.
```

Every Core Service must declare:

```text
owning domain or cross-cutting system
service category
objects read
objects created or updated
state changes
events emitted
contracts required
permissions required
policy requirements
knowledge dependencies
AI usage
human review requirement
audit requirement
failure behavior
MVP phase
MVP depth
product consumers
```

---

# 3. Service Categories

Book 02 recognizes the following Core Service categories.

```text
Command Service
Query Service
Validation Service
Transformation Service
Recommendation Service
Routing Service
Review Service
Notification Service
Integration Service
AI-Assisted Service
Governance Service
```

## 3.1 Command Service

Creates or changes Core state.

## 3.2 Query Service

Retrieves approved Core information under permission and contract rules.

## 3.3 Validation Service

Checks whether a Core Object, request, document, classification or workflow action satisfies rules.

## 3.4 Transformation Service

Converts one Core state or structure into another.

## 3.5 Recommendation Service

Produces a recommendation that may require human review.

## 3.6 Routing Service

Directs work, matters, tasks or recommendations to actors or providers.

## 3.7 Review Service

Creates, assigns, approves, rejects or records review actions.

## 3.8 Notification Service

Creates controlled notifications based on events or workflow conditions.

## 3.9 Integration Service

Mediates external system interaction through contracts.

## 3.10 AI-Assisted Service

Uses governed AI capability under an Agent Contract.

## 3.11 Governance Service

Manages policy, permission, responsibility, audit or architecture-controlled behavior.

---

# 4. MVP Depth Definitions

Service MVP depth uses the same depth vocabulary as the Core MVP.

```text
Must Implement
Partial Implement
Reserved Boundary
Deferred
```

## Must Implement

Required for the first executable Core kernel.

## Partial Implement

Required in limited form or as a governed baseline.

## Reserved Boundary

Defined enough to avoid future conflicts but not deeply implemented.

## Deferred

Explicitly out of MVP scope.

---

# 5. Foundation Service Index

## 5.1 Identity Services

| Service | Category | Objects Operated | Events | Contracts | MVP Phase | MVP Depth | Consumers |
|---|---|---|---|---|---|---|---|
| Identity Registration Service | Command | Identity | IdentityCreated | Identity Data Contract | Phase 1 | Must Implement | Workplace, MarkReg, Lite, Codex |
| Identity Resolution Service | Query | Identity | None | Identity Query Contract | Phase 1 | Must Implement | Workplace, AI Agents, Internal Services |
| Actor Identity Binding Service | Command | Identity, User, AI Agent, Agent | ActorIdentityBound | Identity Binding Contract | Phase 1 | Must Implement | Workplace, AI Agents, Codex |
| System Actor Registration Service | Command | System Actor, AI Agent | SystemActorRegistered | System Actor Contract | Phase 1 | Partial Implement | AI Agents, Codex |

## 5.2 Organization Services

| Service | Category | Objects Operated | Events | Contracts | MVP Phase | MVP Depth | Consumers |
|---|---|---|---|---|---|---|---|
| Organization Creation Service | Command | Organization | OrganizationCreated | Organization Data Contract | Phase 1 | Must Implement | MarkReg, Lite, Workplace |
| Organization Membership Service | Command | Organization, User | OrganizationMemberAdded | Membership Contract | Phase 1 | Must Implement | Workplace, MarkReg |
| Organization Lookup Service | Query | Organization | None | Organization Query Contract | Phase 1 | Must Implement | MarkReg, Lite, Internal Services |
| Organization Relationship Service | Command | Organization Relationship | OrganizationRelationshipCreated | Organization Relationship Contract | Phase 1 | Partial Implement | Partner Center, MGSN baseline |

## 5.3 User Services

| Service | Category | Objects Operated | Events | Contracts | MVP Phase | MVP Depth | Consumers |
|---|---|---|---|---|---|---|---|
| User Registration Service | Command | User, Identity | UserCreated | User Data Contract | Phase 1 | Must Implement | Workplace, MarkReg, Lite |
| User Role Assignment Service | Command | User, Role, Permission | UserRoleAssigned | Role Assignment Contract | Phase 1 | Must Implement | Workplace, Admin |
| User Profile Query Service | Query | User | None | User Query Contract | Phase 1 | Must Implement | Workplace, Internal Services |
| User Activity Context Service | Query | User, Audit | None | User Context Contract | Phase 1 | Partial Implement | Workplace, AI Agents |

## 5.4 Permission Services

| Service | Category | Objects Operated | Events | Contracts | MVP Phase | MVP Depth | Consumers |
|---|---|---|---|---|---|---|---|
| Permission Evaluation Service | Governance | Permission Rule, Actor, Object | PermissionEvaluated | Permission Contract | Phase 1 | Must Implement | All Consumers |
| Permission Assignment Service | Command | Permission Rule, Role, User | PermissionAssigned | Permission Admin Contract | Phase 1 | Must Implement | Workplace, Admin |
| Object Access Check Service | Validation | Permission Rule, Core Object | AccessChecked | Access Contract | Phase 1 | Must Implement | Services, APIs, AI Agents |
| AI Access Permission Service | Governance | Permission Rule, AI Agent | AIAccessChecked | Agent Permission Contract | Phase 1 | Partial Implement | AI Agents |

## 5.5 Policy Services

| Service | Category | Objects Operated | Events | Contracts | MVP Phase | MVP Depth | Consumers |
|---|---|---|---|---|---|---|---|
| Policy Rule Registration Service | Command | Policy Rule | PolicyRuleCreated | Policy Contract | Phase 1 | Partial Implement | Workplace, AI Agents |
| Policy Evaluation Service | Governance | Policy Rule, Context | PolicyEvaluated | Policy Evaluation Contract | Phase 1 | Partial Implement | Services, AI Agents |
| Review Policy Service | Governance | Policy Rule, Review Rule | ReviewPolicyEvaluated | Review Policy Contract | Phase 3 | Partial Implement | Workplace, AI Agents |
| AI Risk Policy Service | Governance | Policy Rule, AI Output | AIRiskPolicyEvaluated | AI Risk Policy Contract | Phase 4 | Partial Implement | AI Agents |

## 5.6 Knowledge Services

| Service | Category | Objects Operated | Events | Contracts | MVP Phase | MVP Depth | Consumers |
|---|---|---|---|---|---|---|---|
| Knowledge Source Registration Service | Command | Knowledge Source | KnowledgeSourceCreated | Knowledge Source Contract | Phase 1 | Must Implement | AI Agents, Lite, MarkReg |
| Knowledge Asset Indexing Service | Command | Knowledge Asset | KnowledgeAssetIndexed | Knowledge Asset Contract | Phase 1 | Must Implement | AI Agents, Internal Services |
| Knowledge Retrieval Service | Query | Knowledge Asset | KnowledgeRetrieved | Knowledge Retrieval Contract | Phase 1 | Must Implement | AI Agents, Lite, Workplace |
| Knowledge Validation Service | Validation | Knowledge Asset | KnowledgeValidationRequired, KnowledgeValidated | Knowledge Validation Contract | Phase 1 | Partial Implement | AI Agents, Professional Review |
| Knowledge Gap Detection Service | Recommendation | Knowledge Gap | KnowledgeGapDetected | Knowledge Gap Contract | Phase 1 | Partial Implement | AI Agents, Codex |

---

# 6. Professional Service Index

## 6.1 Brand Services

| Service | Category | Objects Operated | Events | Contracts | MVP Phase | MVP Depth | Consumers |
|---|---|---|---|---|---|---|---|
| Brand Creation Service | Command | Brand | BrandCreated | Brand Data Contract | Phase 2 | Must Implement | Lite, MarkReg |
| Brand Ownership Linking Service | Command | Brand, Customer, Organization | BrandOwnerLinked | Brand Ownership Contract | Phase 2 | Must Implement | Lite, MarkReg |
| Brand Portfolio Query Service | Query | Brand, Trademark | None | Brand Query Contract | Phase 2 | Partial Implement | MarkReg, Brand Asset Vault baseline |
| Brand Asset Baseline Service | Command | Brand Asset | BrandAssetRegistered | Brand Asset Contract | Phase 5 | Reserved Boundary | Brand Asset Vault baseline |

## 6.2 Trademark Services

| Service | Category | Objects Operated | Events | Contracts | MVP Phase | MVP Depth | Consumers |
|---|---|---|---|---|---|---|---|
| Trademark Creation Service | Command | Trademark | TrademarkCreated | Trademark Data Contract | Phase 2 | Must Implement | MarkReg, Lite |
| Trademark Status Normalization Service | Transformation | Trademark, Trademark Status | TrademarkStatusChanged | Trademark Status Contract | Phase 2 | Must Implement | MarkReg, AI Agents |
| Trademark Lookup Service | Query | Trademark | None | Trademark Query Contract | Phase 2 | Must Implement | MarkReg, Lite, Workplace |
| Trademark Lifecycle Service | Command | Trademark | TrademarkLifecycleUpdated | Trademark Lifecycle Contract | Phase 2 | Partial Implement | MarkReg, Workplace |
| Trademark Status Summary Service | AI-Assisted | Trademark, Knowledge Asset | AITrademarkSummaryGenerated | Agent Contract, Trademark Data Contract | Phase 4 | Partial Implement | AI Agents, MarkReg |

## 6.3 Jurisdiction Services

| Service | Category | Objects Operated | Events | Contracts | MVP Phase | MVP Depth | Consumers |
|---|---|---|---|---|---|---|---|
| Jurisdiction Registration Service | Command | Jurisdiction | JurisdictionCreated | Jurisdiction Contract | Phase 2 | Must Implement | MarkReg, Lite |
| Jurisdiction Requirement Retrieval Service | Query | Jurisdiction Requirement, Knowledge Asset | JurisdictionRequirementRetrieved | Requirement Contract | Phase 2 | Must Implement | Lite, AI Agents |
| Jurisdiction Rule Validation Service | Validation | Jurisdiction Rule | JurisdictionRuleValidated | Jurisdiction Rule Contract | Phase 2 | Partial Implement | MarkReg, AI Agents |
| Office Procedure Baseline Service | Query | Office Procedure | None | Office Procedure Contract | Phase 2 | Partial Implement | MarkReg |

## 6.4 Classification Services

| Service | Category | Objects Operated | Events | Contracts | MVP Phase | MVP Depth | Consumers |
|---|---|---|---|---|---|---|---|
| Classification Term Lookup Service | Query | Classification Term | None | Classification Query Contract | Phase 2 | Must Implement | Lite, MarkReg |
| Classification Recommendation Service | Recommendation / AI-Assisted | Classification Recommendation, Knowledge Asset | ClassificationRecommendationGenerated | Agent Contract, Classification Contract | Phase 2 | Must Implement | Lite, AI Agents |
| Classification Validation Service | Validation | Classification, Goods/Services Term | ClassificationValidationCompleted | Classification Validation Contract | Phase 2 | Must Implement | MarkReg, Lite |
| Classification Review Service | Review | Classification Recommendation, Review Record | ClassificationReviewRequired, ClassificationReviewApproved | Review Contract | Phase 3 | Partial Implement | Workplace, AI Agents |

## 6.5 Document Services

| Service | Category | Objects Operated | Events | Contracts | MVP Phase | MVP Depth | Consumers |
|---|---|---|---|---|---|---|---|
| Document Upload Service | Command | Document | DocumentUploaded | Document Data Contract | Phase 2 | Must Implement | MarkReg, Workplace, Lite |
| Document Requirement Service | Query | Document Requirement, Jurisdiction | DocumentRequirementRetrieved | Document Requirement Contract | Phase 2 | Must Implement | Lite, AI Agents |
| Document Generation Service | AI-Assisted / Transformation | Document, Knowledge Asset | DocumentGenerated | Document Generation Contract, Agent Contract | Phase 4 | Partial Implement | MarkReg, AI Agents |
| Document Review Service | Review | Document, Review Record | DocumentReviewRequired, DocumentReviewApproved | Review Contract | Phase 3 | Partial Implement | Workplace, MarkReg |
| Document Linking Service | Command | Document, Matter, Trademark, Order | DocumentLinked | Document Link Contract | Phase 2 | Must Implement | MarkReg, Workplace |

## 6.6 Evidence Services

| Service | Category | Objects Operated | Events | Contracts | MVP Phase | MVP Depth | Consumers |
|---|---|---|---|---|---|---|---|
| Evidence Upload Service | Command | Evidence | EvidenceUploaded | Evidence Data Contract | Phase 2 | Partial Implement | MarkReg, Workplace |
| Evidence Package Service | Transformation | Evidence Package | EvidencePackageCreated | Evidence Package Contract | Phase 3 | Partial Implement | MarkReg |
| Evidence Review Service | Review / AI-Assisted | Evidence, Review Record | EvidenceReviewRequired, EvidenceReviewCompleted | Agent Contract, Review Contract | Phase 4 | Partial Implement | AI Agents, Workplace |
| Evidence Sufficiency Check Service | Validation | Evidence Package | EvidenceSufficiencyChecked | Evidence Validation Contract | Phase 4 | Deferred | MarkReg, AI Agents |

---

# 7. Business Execution Service Index

## 7.1 Customer Services

| Service | Category | Objects Operated | Events | Contracts | MVP Phase | MVP Depth | Consumers |
|---|---|---|---|---|---|---|---|
| Customer Creation Service | Command | Customer | CustomerCreated | Customer Data Contract | Phase 3 | Must Implement | Lite, MarkReg |
| Customer Contact Linking Service | Command | Customer, Contact | CustomerContactLinked | Customer Contact Contract | Phase 3 | Must Implement | MarkReg, Workplace |
| Customer Context Query Service | Query | Customer, Brand, Trademark, Order | None | Customer Query Contract | Phase 3 | Must Implement | Lite, MarkReg, AI Agents |
| Customer Duplicate Detection Service | Validation | Customer | CustomerDuplicateDetected | Customer Validation Contract | Phase 3 | Partial Implement | MarkReg, Lite |

## 7.2 Order Services

| Service | Category | Objects Operated | Events | Contracts | MVP Phase | MVP Depth | Consumers |
|---|---|---|---|---|---|---|---|
| Order Creation Service | Command | Order | OrderCreated | Order Data Contract | Phase 3 | Must Implement | Lite, MarkReg |
| Order Requirement Validation Service | Validation | Order, Document Requirement, Classification | OrderValidationCompleted | Order Validation Contract | Phase 3 | Must Implement | Lite, AI Agents |
| Order Confirmation Service | Command | Order | OrderConfirmed | Order Confirmation Contract | Phase 3 | Must Implement | MarkReg, Workplace |
| Order-to-Matter Conversion Service | Transformation | Order, Matter | OrderConvertedToMatter, MatterCreated | Workflow Contract, Order/Matter Contract | Phase 3 | Must Implement | MarkReg, Workplace |

## 7.3 Matter Services

| Service | Category | Objects Operated | Events | Contracts | MVP Phase | MVP Depth | Consumers |
|---|---|---|---|---|---|---|---|
| Matter Creation Service | Command | Matter | MatterCreated | Matter Data Contract | Phase 3 | Must Implement | MarkReg, Workplace |
| Matter Status Service | Command | Matter | MatterStatusChanged | Matter Status Contract | Phase 3 | Must Implement | Workplace, MarkReg |
| Matter Context Query Service | Query | Matter, Customer, Trademark, Document, Task | None | Matter Query Contract | Phase 3 | Must Implement | Workplace, MarkReg, AI Agents |
| Matter Assignment Service | Command | Matter, Responsibility Assignment | MatterAssigned | Responsibility Contract | Phase 3 | Partial Implement | Workplace |
| Matter Closure Service | Command | Matter | MatterClosed | Matter Closure Contract | Phase 3 | Partial Implement | Workplace, MarkReg |

## 7.4 Opportunity Services

| Service | Category | Objects Operated | Events | Contracts | MVP Phase | MVP Depth | Consumers |
|---|---|---|---|---|---|---|---|
| Opportunity Creation Service | Command | Opportunity | OpportunityCreated | Opportunity Contract | Phase 4 | Partial Implement | Opportunity Engine baseline |
| Opportunity Discovery Service | AI-Assisted / Recommendation | Opportunity Signal | OpportunitySignalDetected | Agent Contract, Opportunity Contract | Phase 4 | Partial Implement | AI Agents |
| Opportunity Follow-up Service | Command | Opportunity, Task | OpportunityFollowUpCreated | Opportunity Workflow Contract | Phase 4 | Partial Implement | Workplace |
| Opportunity Scoring Service | Recommendation | Opportunity | OpportunityScored | Opportunity Scoring Contract | Future | Deferred | Opportunity Engine |

## 7.5 Workflow Contract Services

| Service | Category | Objects Operated | Events | Contracts | MVP Phase | MVP Depth | Consumers |
|---|---|---|---|---|---|---|---|
| Workflow Contract Registration Service | Command | Workflow Contract | WorkflowContractCreated | Workflow Contract | Phase 3 | Must Implement | Workplace, Codex |
| Workflow Transition Validation Service | Validation | Workflow State, Workflow Transition | WorkflowTransitionValidated | Workflow Contract | Phase 3 | Must Implement | Workplace, Services |
| Workflow State Change Service | Command | Workflow State | WorkflowStateChanged | Workflow Event Contract | Phase 3 | Must Implement | Workplace |
| Workflow Review Gate Service | Review | Workflow Contract, Review Record | ReviewRequired | Review Contract | Phase 3 | Partial Implement | Workplace, AI Agents |

## 7.6 Task Services

| Service | Category | Objects Operated | Events | Contracts | MVP Phase | MVP Depth | Consumers |
|---|---|---|---|---|---|---|---|
| Task Creation Service | Command | Task | TaskCreated | Task Data Contract | Phase 3 | Must Implement | Workplace, MarkReg |
| Task Assignment Service | Command | Task, User, Responsibility Assignment | TaskAssigned | Task Assignment Contract | Phase 3 | Must Implement | Workplace |
| Task Completion Service | Command | Task | TaskCompleted | Task Completion Contract | Phase 3 | Must Implement | Workplace |
| Task Due Date Service | Command | Task | TaskDueDateChanged | Task Schedule Contract | Phase 3 | Partial Implement | Workplace |
| Task Context Query Service | Query | Task, Matter, Event | None | Task Query Contract | Phase 3 | Must Implement | Workplace, AI Agents |

## 7.7 Event Services

| Service | Category | Objects Operated | Events | Contracts | MVP Phase | MVP Depth | Consumers |
|---|---|---|---|---|---|---|---|
| Event Publishing Service | Command | Event | EventPublished | Event Contract | Phase 3 | Must Implement | All Services |
| Event Subscription Service | Query / Subscription | Event | None | Event Subscription Contract | Phase 3 | Must Implement | Workplace, Products, Reporting |
| Event Replay Service | Query | Event | EventReplayed | Event Replay Contract | Phase 3 | Partial Implement | Testing, Reporting |
| Event Audit Service | Governance | Event, Audit Record | EventAuditRecorded | Audit Contract | Phase 3 | Partial Implement | Compliance, AI Agents |

## 7.8 Notification Services

| Service | Category | Objects Operated | Events | Contracts | MVP Phase | MVP Depth | Consumers |
|---|---|---|---|---|---|---|---|
| Notification Creation Service | Notification | Notification | NotificationCreated | Notification Contract | Phase 3 | Partial Implement | Workplace |
| Notification Dispatch Service | Notification | Notification | NotificationDispatched | Notification Dispatch Contract | Phase 3 | Partial Implement | Workplace, Products |
| Deadline Reminder Service | Notification | Task, Matter | DeadlineReminderCreated | Reminder Contract | Phase 3 | Partial Implement | Workplace |
| Notification Preference Service | Command | Notification Preference | NotificationPreferenceUpdated | Preference Contract | Future | Deferred | Client Portal, Workplace |

---

# 8. Collaboration Network Service Index

## 8.1 Partner Services

| Service | Category | Objects Operated | Events | Contracts | MVP Phase | MVP Depth | Consumers |
|---|---|---|---|---|---|---|---|
| Partner Registration Service | Command | Partner | PartnerRegistered | Partner Contract | Phase 5 | Reserved Boundary | Partner Center |
| Partner Relationship Service | Command | Partner, Organization | PartnerRelationshipCreated | Partner Relationship Contract | Phase 5 | Reserved Boundary | MGSN |
| Partner Capability Query Service | Query | Partner, Capability | None | Partner Capability Contract | Phase 5 | Deferred | MGSN |

## 8.2 Agent Services

| Service | Category | Objects Operated | Events | Contracts | MVP Phase | MVP Depth | Consumers |
|---|---|---|---|---|---|---|---|
| Agent Registration Service | Command | Agent | AgentRegistered | Agent Data Contract | Phase 4 | Partial Implement | MarkReg, MGSN baseline |
| Agent Capability Linking Service | Command | Agent, Capability | AgentCapabilityLinked | Capability Contract | Phase 4 | Partial Implement | Routing, MarkReg |
| Agent Lookup Service | Query | Agent, Jurisdiction | None | Agent Query Contract | Phase 4 | Partial Implement | MarkReg, Routing |
| Agent Quality Context Service | Query | Agent, Matter, Communication | None | Agent Quality Contract | Future | Deferred | MGSN |

## 8.3 Service Provider Services

| Service | Category | Objects Operated | Events | Contracts | MVP Phase | MVP Depth | Consumers |
|---|---|---|---|---|---|---|---|
| Service Provider Registration Service | Command | Service Provider | ServiceProviderRegistered | Service Provider Contract | Phase 4 | Partial Implement | MGSN baseline |
| Provider Capability Linking Service | Command | Service Provider, Capability | ProviderCapabilityLinked | Capability Contract | Phase 4 | Partial Implement | Routing |
| Provider Lookup Service | Query | Service Provider | None | Provider Query Contract | Phase 4 | Partial Implement | MarkReg, MGSN baseline |
| Provider Ranking Service | Recommendation | Service Provider | ProviderRanked | Provider Ranking Contract | Future | Deferred | MGSN |

## 8.4 Service Network Services

| Service | Category | Objects Operated | Events | Contracts | MVP Phase | MVP Depth | Consumers |
|---|---|---|---|---|---|---|---|
| Service Network Baseline Service | Command | Service Network | ServiceNetworkCreated | Service Network Contract | Phase 5 | Reserved Boundary | MGSN |
| Network Membership Service | Command | Service Network, Partner, Agent | NetworkMemberAdded | Network Membership Contract | Phase 5 | Reserved Boundary | MGSN |
| Network Trust Service | Governance | Trust Record | TrustRecordUpdated | Trust Contract | Future | Deferred | MGSN |
| Service Exchange Service | Command | Service Network, Matter | ServiceExchangeCreated | Service Exchange Contract | Future | Deferred | MGSN |

## 8.5 Routing Services

| Service | Category | Objects Operated | Events | Contracts | MVP Phase | MVP Depth | Consumers |
|---|---|---|---|---|---|---|---|
| Routing Candidate Service | Recommendation | Routing Candidate, Agent, Service Provider | RoutingCandidatesGenerated | Routing Contract | Phase 4 | Partial Implement | MarkReg, AI Agents |
| Routing Decision Service | Routing | Routing Decision | RoutingDecisionMade | Routing Decision Contract | Phase 4 | Partial Implement | MarkReg, Workplace |
| Routing Review Service | Review | Routing Decision, Review Record | RoutingReviewRequired, RoutingApproved | Review Contract | Phase 4 | Partial Implement | Workplace |
| Advanced Routing Optimization Service | Recommendation | Routing Decision | RoutingOptimized | Routing Optimization Contract | Future | Deferred | MGSN |

## 8.6 Communication Services

| Service | Category | Objects Operated | Events | Contracts | MVP Phase | MVP Depth | Consumers |
|---|---|---|---|---|---|---|---|
| Communication Linking Service | Command | Communication, Matter, Customer, Agent | CommunicationLinked | Communication Contract | Phase 4 | Partial Implement | MarkReg, Workplace |
| Communication Summary Service | AI-Assisted | Communication, AI Output | AICommunicationSummaryGenerated | Agent Contract, Communication Contract | Phase 4 | Partial Implement | AI Agents, Workplace |
| Communication Thread Query Service | Query | Communication | None | Communication Query Contract | Phase 4 | Partial Implement | Workplace, MarkReg |
| External Communication Sync Service | Integration | Communication | CommunicationSynced | Integration Contract | Future | Deferred | External Integrations |

---

# 9. Cross-Cutting Service Index

Capability and Business Responsibility are cross-cutting Core specification systems.

They are not counted as additional baseline Core Domains.

## 9.1 Capability Services

| Service | Category | Objects Operated | Events | Contracts | MVP Phase | MVP Depth | Consumers |
|---|---|---|---|---|---|---|---|
| Capability Registration Service | Command | Capability | CapabilityCreated | Capability Contract | Phase 1 | Partial Implement | AI Agents, Routing, MGSN baseline |
| Capability Provider Linking Service | Command | Capability, Capability Provider | CapabilityProviderLinked | Capability Provider Contract | Phase 1 | Partial Implement | Routing, Agent, Provider |
| Capability Matching Service | Recommendation | Capability, Agent, Service Provider | CapabilityMatched | Capability Matching Contract | Phase 4 | Partial Implement | Routing, MGSN baseline |
| Capability Scope Validation Service | Validation | Capability Scope | CapabilityScopeValidated | Capability Scope Contract | Phase 1 | Partial Implement | AI Agents, Workplace |

## 9.2 Business Responsibility Services

| Service | Category | Objects Operated | Events | Contracts | MVP Phase | MVP Depth | Consumers |
|---|---|---|---|---|---|---|---|
| Responsibility Assignment Service | Command | Responsibility Assignment | ResponsibilityAssigned | Responsibility Contract | Phase 3 | Partial Implement | Workplace, MarkReg |
| Review Requirement Service | Governance | Review Rule, AI Output, Document, Classification | ReviewRequired | Review Contract | Phase 3 | Partial Implement | Workplace, AI Agents |
| Review Decision Service | Review | Review Record | ReviewApproved, ReviewRejected | Review Decision Contract | Phase 3 | Partial Implement | Workplace |
| Accountability Audit Service | Governance | Responsibility Assignment, Audit Record | AccountabilityAuditRecorded | Audit Contract | Phase 3 | Partial Implement | Workplace, Compliance |

---

# 10. AI-Assisted Service Baseline

AI-assisted services must operate under Agent Contracts.

| Service | Owning Domain/System | AI Agent | Output | Review Rule | MVP Depth |
|---|---|---|---|---|---|
| Classification Recommendation Service | Classification | Classification Assistant Agent | Classification Recommendation | Review required for high-risk filing decisions | Must Implement |
| Document Generation Service | Document | Document Draft Assistant Agent | AI Draft / Generated Document | Review required before external use | Partial Implement |
| Evidence Review Service | Evidence | Evidence Review Assistant Agent | Evidence Review Note | Review required | Partial Implement |
| Trademark Status Summary Service | Trademark | Trademark Status Summary Agent | AI Summary | Review depending on external use | Partial Implement |
| Communication Summary Service | Communication | Communication Summary Agent | AI Summary | Review depending on use | Partial Implement |
| Opportunity Discovery Service | Opportunity | Opportunity Discovery Agent | Opportunity Signal | Human confirmation required | Partial Implement |
| Routing Candidate Service | Routing | Routing Assistant Agent | Routing Candidate | Review required before assignment | Partial Implement |
| Codex Spec Consistency Review Service | Codex / Governance | Spec Consistency Review Agent | Review Note | Human architecture review required | Partial Implement |

AI-assisted services shall not:

```text
mutate Core state directly
bypass permissions
skip event rules
skip audit
be treated as final professional judgment without review where required
```

---

# 11. API Exposure Baseline

Not every Core Service is exposed as an API.

API exposure requires Appendix F and API Contract review.

## MVP API Candidate Services

```text
Identity Registration Service
Identity Resolution Service
Organization Lookup Service
User Profile Query Service
Permission Evaluation Service
Knowledge Retrieval Service
Trademark Lookup Service
Trademark Status Normalization Service
Jurisdiction Requirement Retrieval Service
Classification Term Lookup Service
Classification Recommendation Service
Classification Validation Service
Document Upload Service
Document Requirement Service
Customer Creation Service
Customer Context Query Service
Order Creation Service
Order Requirement Validation Service
Order-to-Matter Conversion Service
Matter Creation Service
Matter Context Query Service
Task Creation Service
Task Assignment Service
Task Completion Service
Event Subscription Service
AI-assisted service invocation baseline
```

API exposure must specify:

```text
input contract
output contract
permission requirement
policy requirement
event side effects
audit requirement
consumer
MVP status
```

---

# 12. Workflow Usage Baseline

Services that affect workflow must connect to Workflow Contracts.

Workflow-sensitive services include:

```text
Order-to-Matter Conversion Service
Matter Status Service
Task Creation Service
Task Assignment Service
Task Completion Service
Workflow Transition Validation Service
Workflow State Change Service
Workflow Review Gate Service
Document Review Service
Classification Review Service
Evidence Review Service
Routing Review Service
Review Decision Service
```

Workflow-sensitive services must declare:

```text
allowed state transition
actor
responsibility
review rule
event emitted
notification effect
audit requirement
```

---

# 13. Event Emission Rules

A Core Service must declare whether it emits events.

Event emission is required when the service creates meaningful change.

Examples:

```text
Customer Creation Service emits CustomerCreated.
Order Creation Service emits OrderCreated.
Order-to-Matter Conversion Service emits OrderConvertedToMatter and MatterCreated.
Task Assignment Service emits TaskAssigned.
Routing Decision Service emits RoutingDecisionMade.
Classification Recommendation Service emits ClassificationRecommendationGenerated.
Review Requirement Service emits ReviewRequired.
Review Decision Service emits ReviewApproved or ReviewRejected.
```

A service must not hide meaningful state change.

---

# 14. Service Governance Rules

The following governance rules apply to all Core Services.

## Rule 1 — Service ownership must be explicit

Every service must have an owning domain or cross-cutting system.

## Rule 2 — Services operate objects

Every service must declare objects read and objects created or updated.

## Rule 3 — Services declare side effects

Every service must declare state changes and events emitted.

## Rule 4 — Services require contracts

Service consumption must be governed by Data, API, Event, Agent, Workflow or Consumption Contracts where applicable.

## Rule 5 — AI usage requires Agent Contract

No AI-assisted service may operate without an Agent Contract.

## Rule 6 — Review rules must be explicit

High-risk professional outputs require human review.

## Rule 7 — Failure behavior must be specified

Services must define validation failure, permission denial, missing dependency and retry behavior.

## Rule 8 — MVP depth must be declared

Services must be tagged as Must Implement, Partial Implement, Reserved Boundary or Deferred.

---

# 15. Service Anti-Patterns

The following patterns are prohibited.

## 15.1 UI Button as Service

A button action is treated as a Core Service without domain ownership or contracts.

## 15.2 Helper Function as Service

A utility function becomes a service without Core meaning.

## 15.3 Service Without Object Ownership

A service mutates data without declaring Core Objects.

## 15.4 Eventless State Change

A service changes Core state without emitting required events.

## 15.5 Prompt as Service

An AI prompt is treated as a service without Agent Contract.

## 15.6 Vendor Wrapper as Service

A provider-specific API wrapper is treated as Core Service.

## 15.7 Product Logic as Core Service

Product-specific UI flow logic is placed inside Core Service.

## 15.8 Deferred Service Leakage

Future marketplace or analytics services enter MVP without approval.

---

# 16. Relationship to Appendix E — Event Index

Appendix E must use this service index to confirm event sources.

Every event should reference either:

```text
source domain
source service
source cross-cutting system
```

Appendix E should verify that major services have event side effects where meaningful changes occur.

---

# 17. Relationship to Appendix F — API Index

Appendix F must use this service index to identify API candidate services.

An API surface is a governed exposure of a Core Service or service-backed query.

Appendix F should not expose every service automatically.

API exposure requires:

```text
consumer need
permission rule
input contract
output contract
event side effects
audit rule
MVP status
```

---

# 18. Relationship to Appendix G — Agent Index

Appendix G must use this service index to identify AI-assisted service boundaries.

Every AI agent should be mapped to:

```text
allowed services
prohibited services
objects read
outputs created
review rules
events emitted
audit requirements
```

---

# 19. Relationship to Appendix H — Codex Task Index

Appendix H must use this service index to generate Codex task dependencies.

Codex tasks should not implement services randomly.

Each service implementation task must reference:

```text
owning domain/system
objects required
events required
contracts required
AI restrictions
workflow usage
MVP depth
acceptance criteria
```

---

# 20. Relationship to core-specs/services/

Future `core-specs/services/` files must follow the Chapter 24 template and this appendix.

Each service spec should include:

```text
Service Name
Service ID
Owning Domain or Cross-Cutting System
Service Category
Purpose
In Scope
Out of Scope
Inputs
Outputs
Objects Read
Objects Created or Updated
State Changes
Events Emitted
Events Consumed
Contracts Required
Permission Requirements
Policy Requirements
Knowledge Dependencies
AI Usage
Human Review Requirement
Audit Requirement
Failure Behavior
Idempotency Rule
API Exposure
Workflow Usage
Product Consumers
MVP Phase
MVP Depth
Acceptance Criteria
Revision Notes
```

---

# 21. Acceptance Criteria

This appendix is accepted when:

```text
[ ] It defines Core Service as governed capability.
[ ] It lists service categories.
[ ] It maps services to owning domains or cross-cutting systems.
[ ] It includes Foundation services.
[ ] It includes Professional services.
[ ] It includes Business Execution services.
[ ] It includes Collaboration Network services.
[ ] It includes Capability services.
[ ] It includes Business Responsibility services.
[ ] It includes AI-assisted service baseline.
[ ] It identifies API candidate services.
[ ] It identifies workflow-sensitive services.
[ ] It defines service governance rules.
[ ] It defines service anti-patterns.
[ ] It prepares Appendix E, F, G and H.
[ ] It prepares future core-specs/services/.
[ ] It preserves MVP depth boundaries.
```

---

# 22. Revision Notes

| Version | Status | Notes |
|---------|--------|-------|
| 0.2.0 | Draft | Initial second canonical draft Core Service Index. Defines MVP and future Core Services by domain, cross-cutting system, AI usage, API exposure, workflow usage and Codex readiness. |

---

**End of Appendix**
