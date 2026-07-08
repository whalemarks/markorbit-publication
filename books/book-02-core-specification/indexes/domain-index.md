# Domain Index

**Repository:** `book-02-core`  
**Directory:** `indexes/`  
**Index ID:** B02-IDX-DOMAIN  
**Source Appendix:** B02-APP-B — Core Domain Index  
**Related Appendix:** B02-APP-A — Glossary  
**Stage:** Second Canonical Draft  
**Status:** Draft  
**Version:** 0.1.0  
**Owner:** MarkOrbit Publications Editorial Board  

---

# 1. Index Purpose

This index operationalizes **B02-APP-B — Core Domain Index**.

The appendix is the canonical manuscript reference.

This file is the implementation-ready domain index used by:

```text
core-specs/domains/
core-specs/objects/
core-specs/services/
core-specs/events/
core-specs/contracts/
core-specs/api/
core-specs/agents/
codex-tasks/
validation scripts
```

This index does not invent new Core architecture.

It converts the canonical 26-domain map into a structured operational index.

---

# 2. Canonical Domain Rule

Book 02 uses the following canonical rule:

```text
The baseline Core Domain Map contains 26 domains.
Capability and Business Responsibility are cross-cutting Core specification systems.
They are not counted as additional baseline Core Domains unless a later architecture release explicitly changes the domain map.
```

Therefore, this index contains:

```text
26 baseline Core Domains
+
2 cross-cutting Core specification systems
=
28 execution rows
```

The 28 execution rows are for MVP planning and Codex sequencing only.

They do not change the 26-domain baseline.

---

# 3. Domain Categories

The 26 baseline Core Domains are grouped into four categories.

```text
Foundation Domains
Professional Domains
Business Execution Domains
Collaboration Network Domains
```

Cross-cutting systems are listed separately.

```text
Cross-Cutting Core Specification Systems
    Capability
    Business Responsibility
```

---

# 4. MVP Depth Vocabulary

This index uses four MVP depth values.

```text
Must Implement
Partial Implement
Reserved Boundary
Deferred
```

## 4.1 Must Implement

Required for the first executable Core kernel.

## 4.2 Partial Implement

Requires baseline specification and limited execution, but not full implementation.

## 4.3 Reserved Boundary

Must be recognized and protected, but should not be deeply implemented in MVP.

## 4.4 Deferred

Belongs to future releases.

---

# 5. Consumer Classification

This index uses the following consumer classification.

## 5.1 MVP Consumers

```text
MarkReg
MarkOrbit Lite
Workplace
AI Agents
Codex Implementation
```

## 5.2 Partial Consumers

```text
MGSN
Opportunity Engine baseline
Brand Asset Vault baseline
```

## 5.3 Future Consumers

```text
Partner Center
Client Portal
Service Platform
External Integrations
Reporting Consumers
```

---

# 6. Domain Index Summary

| Row | Name | Type | Category | MVP Phase | MVP Depth |
|---:|------|------|----------|-----------|-----------|
| 1 | Identity | Baseline Domain | Foundation | Phase 1 | Must Implement |
| 2 | Organization | Baseline Domain | Foundation | Phase 1 | Must Implement |
| 3 | User | Baseline Domain | Foundation | Phase 1 | Must Implement |
| 4 | Permission | Baseline Domain | Foundation | Phase 1 | Must Implement |
| 5 | Policy | Baseline Domain | Foundation | Phase 1 | Partial Implement |
| 6 | Knowledge | Baseline Domain | Foundation | Phase 1 | Must Implement |
| 7 | Brand | Baseline Domain | Professional | Phase 2 | Must Implement |
| 8 | Trademark | Baseline Domain | Professional | Phase 2 | Must Implement |
| 9 | Jurisdiction | Baseline Domain | Professional | Phase 2 | Must Implement |
| 10 | Classification | Baseline Domain | Professional | Phase 2 | Must Implement |
| 11 | Document | Baseline Domain | Professional | Phase 2 | Must Implement |
| 12 | Evidence | Baseline Domain | Professional | Phase 2 | Partial Implement |
| 13 | Customer | Baseline Domain | Business Execution | Phase 3 | Must Implement |
| 14 | Matter | Baseline Domain | Business Execution | Phase 3 | Must Implement |
| 15 | Order | Baseline Domain | Business Execution | Phase 3 | Must Implement |
| 16 | Opportunity | Baseline Domain | Business Execution | Phase 4 | Partial Implement |
| 17 | Workflow Contract | Baseline Domain | Business Execution | Phase 3 | Must Implement |
| 18 | Task | Baseline Domain | Business Execution | Phase 3 | Must Implement |
| 19 | Event | Baseline Domain | Business Execution | Phase 3 | Must Implement |
| 20 | Notification | Baseline Domain | Business Execution | Phase 3 | Partial Implement |
| 21 | Partner | Baseline Domain | Collaboration Network | Phase 5 | Reserved Boundary |
| 22 | Agent | Baseline Domain | Collaboration Network | Phase 4 | Partial Implement |
| 23 | Service Provider | Baseline Domain | Collaboration Network | Phase 4 | Partial Implement |
| 24 | Service Network | Baseline Domain | Collaboration Network | Phase 5 | Reserved Boundary |
| 25 | Routing | Baseline Domain | Collaboration Network | Phase 4 | Partial Implement |
| 26 | Communication | Baseline Domain | Collaboration Network | Phase 4 | Partial Implement |
| 27 | Capability | Cross-Cutting System | Cross-Cutting | Phase 1 | Partial Implement |
| 28 | Business Responsibility | Cross-Cutting System | Cross-Cutting | Phase 3 | Partial Implement |

---

# 7. Foundation Domains

## 7.1 Identity

| Field | Value |
|------|-------|
| Type | Baseline Domain |
| Category | Foundation |
| MVP Phase | Phase 1 |
| MVP Depth | Must Implement |
| Primary Consumers | MarkReg, MarkOrbit Lite, Workplace, AI Agents, Codex Implementation |
| Core Purpose | Defines who or what an actor is. |

### Primary Objects

```text
Identity
Actor
System Identity
AI Agent Identity
External Actor Identity
```

### Primary Services

```text
Identity Registration Service
Identity Resolution Service
Identity Verification Baseline Service
Actor Identity Lookup Service
```

### Primary Events

```text
IdentityCreated
IdentityUpdated
IdentityLinked
IdentityDeactivated
```

### Contracts

```text
Identity Data Contract
Identity API Contract
Identity Event Contract
```

### AI Usage

```text
AI Agents require AI Agent Identity before Core consumption.
```

### Deferred Scope

```text
full enterprise IAM
advanced identity federation
external identity marketplace
```

---

## 7.2 Organization

| Field | Value |
|------|-------|
| Type | Baseline Domain |
| Category | Foundation |
| MVP Phase | Phase 1 |
| MVP Depth | Must Implement |
| Primary Consumers | MarkReg, MarkOrbit Lite, Workplace, Codex Implementation |
| Core Purpose | Defines business entities and structural ownership. |

### Primary Objects

```text
Organization
Organization Unit
Organization Membership
```

### Primary Services

```text
Organization Registration Service
Organization Membership Service
Organization Context Service
```

### Primary Events

```text
OrganizationCreated
OrganizationUpdated
OrganizationMembershipChanged
```

### Contracts

```text
Organization Data Contract
Organization API Contract
Organization Event Contract
```

### Deferred Scope

```text
complex enterprise hierarchy
multi-tenant enterprise governance
advanced partner hierarchy
```

---

## 7.3 User

| Field | Value |
|------|-------|
| Type | Baseline Domain |
| Category | Foundation |
| MVP Phase | Phase 1 |
| MVP Depth | Must Implement |
| Primary Consumers | MarkReg, MarkOrbit Lite, Workplace, AI Agents, Codex Implementation |
| Core Purpose | Defines human actors operating in MarkOrbit. |

### Primary Objects

```text
User
User Profile
User Role Assignment
```

### Primary Services

```text
User Registration Service
User Profile Service
User Role Assignment Service
User Context Service
```

### Primary Events

```text
UserCreated
UserUpdated
UserRoleAssigned
UserDeactivated
```

### Contracts

```text
User Data Contract
User API Contract
User Event Contract
```

### Deferred Scope

```text
advanced HR integration
full role marketplace
complex HR permission sync
```

---

## 7.4 Permission

| Field | Value |
|------|-------|
| Type | Baseline Domain |
| Category | Foundation |
| MVP Phase | Phase 1 |
| MVP Depth | Must Implement |
| Primary Consumers | All MVP Consumers |
| Core Purpose | Governs what actors may read, create, update, approve, export or invoke. |

### Primary Objects

```text
Permission Rule
Access Scope
Role Permission
```

### Primary Services

```text
Permission Check Service
Access Scope Resolution Service
Permission Assignment Service
```

### Primary Events

```text
PermissionGranted
PermissionRevoked
PermissionCheckFailed
```

### Contracts

```text
Permission Data Contract
Permission API Contract
Permission Event Contract
```

### AI Usage

```text
AI access must be permission-bound.
```

### Deferred Scope

```text
full policy engine
advanced attribute-based access control
external delegated authorization
```

---

## 7.5 Policy

| Field | Value |
|------|-------|
| Type | Baseline Domain |
| Category | Foundation |
| MVP Phase | Phase 1 |
| MVP Depth | Partial Implement |
| Primary Consumers | Workplace, AI Agents, Codex Implementation |
| Core Purpose | Defines rules that influence decisions and constraints. |

### Primary Objects

```text
Policy Rule
Review Policy
AI Risk Policy
Data Exposure Policy
```

### Primary Services

```text
Policy Evaluation Baseline Service
Review Policy Lookup Service
AI Risk Policy Check Service
```

### Primary Events

```text
PolicyRuleCreated
PolicyRuleUpdated
PolicyViolationDetected
```

### Contracts

```text
Policy Data Contract
Policy Event Contract
AI Policy Contract
```

### Deferred Scope

```text
full rule engine
jurisdiction-wide automated policy enforcement
complex business policy automation
```

---

## 7.6 Knowledge

| Field | Value |
|------|-------|
| Type | Baseline Domain |
| Category | Foundation |
| MVP Phase | Phase 1 |
| MVP Depth | Must Implement |
| Primary Consumers | MarkOrbit Lite, MarkReg, AI Agents, Workplace |
| Core Purpose | Defines governed professional knowledge. |

### Primary Objects

```text
Knowledge Source
Knowledge Asset
Knowledge Rule
Knowledge Gap
Knowledge Citation
```

### Primary Services

```text
Knowledge Retrieval Service
Knowledge Source Registration Service
Knowledge Asset Validation Service
Knowledge Gap Detection Service
```

### Primary Events

```text
KnowledgeSourceAdded
KnowledgeAssetValidated
KnowledgeGapDetected
KnowledgeAssetUpdated
```

### Contracts

```text
Knowledge Data Contract
Knowledge Retrieval API Contract
AI Knowledge Authorization Contract
```

### AI Usage

```text
AI may only use authorized Knowledge Sources and Knowledge Assets.
```

### Deferred Scope

```text
full automated knowledge graph
complete global legal knowledge automation
unreviewed AI-generated knowledge validation
```

---

# 8. Professional Domains

## 8.1 Brand

| Field | Value |
|------|-------|
| Type | Baseline Domain |
| Category | Professional |
| MVP Phase | Phase 2 |
| MVP Depth | Must Implement |
| Primary Consumers | MarkOrbit Lite, MarkReg |
| Core Purpose | Defines the business or market identity that trademark work protects. |

### Primary Objects

```text
Brand
Brand Owner
Brand Asset Reference
Brand Market Context
```

### Primary Services

```text
Brand Registration Service
Brand Context Service
Brand-to-Trademark Link Service
```

### Primary Events

```text
BrandCreated
BrandUpdated
BrandLinkedToTrademark
```

### Contracts

```text
Brand Data Contract
Brand API Contract
Brand Event Contract
```

### Deferred Scope

```text
full Brand Asset Vault
brand valuation
brand portfolio intelligence
```

---

## 8.2 Trademark

| Field | Value |
|------|-------|
| Type | Baseline Domain |
| Category | Professional |
| MVP Phase | Phase 2 |
| MVP Depth | Must Implement |
| Primary Consumers | MarkReg, MarkOrbit Lite, Workplace, AI Agents |
| Core Purpose | Defines mark-related professional meaning. |

### Primary Objects

```text
Trademark
Trademark Owner
Trademark Status
Trademark GoodsServices
Trademark Image Reference
Trademark Lifecycle Record
```

### Primary Services

```text
Trademark Registration Service
Trademark Status Normalization Service
Trademark Lookup Service
Trademark Lifecycle Summary Service
```

### Primary Events

```text
TrademarkCreated
TrademarkUpdated
TrademarkStatusChanged
TrademarkLinkedToMatter
```

### Contracts

```text
Trademark Data Contract
Trademark API Contract
Trademark Event Contract
```

### AI Usage

```text
Trademark Status Summary Agent may summarize trademark status under review rules.
```

### Deferred Scope

```text
full official office sync
advanced portfolio analytics
automatic legal strategy
```

---

## 8.3 Jurisdiction

| Field | Value |
|------|-------|
| Type | Baseline Domain |
| Category | Professional |
| MVP Phase | Phase 2 |
| MVP Depth | Must Implement |
| Primary Consumers | MarkReg, MarkOrbit Lite, AI Agents |
| Core Purpose | Defines country, region or office-specific professional context. |

### Primary Objects

```text
Jurisdiction
Trademark Office
Jurisdiction Requirement
Jurisdiction Rule
```

### Primary Services

```text
Jurisdiction Requirement Lookup Service
Jurisdiction Rule Validation Service
Trademark Office Context Service
```

### Primary Events

```text
JurisdictionAdded
JurisdictionRequirementUpdated
JurisdictionRuleChanged
```

### Contracts

```text
Jurisdiction Data Contract
Jurisdiction Requirement API Contract
Jurisdiction Event Contract
```

### Deferred Scope

```text
complete global office automation
all-country rule engine
automatic office procedure interpretation
```

---

## 8.4 Classification

| Field | Value |
|------|-------|
| Type | Baseline Domain |
| Category | Professional |
| MVP Phase | Phase 2 |
| MVP Depth | Must Implement |
| Primary Consumers | MarkOrbit Lite, MarkReg, AI Agents |
| Core Purpose | Defines goods and services classification meaning. |

### Primary Objects

```text
Classification
Class
GoodsServices Term
Classification Recommendation
Classification Review Record
```

### Primary Services

```text
Classification Recommendation Service
Classification Validation Service
GoodsServices Term Lookup Service
Classification Review Service
```

### Primary Events

```text
ClassificationRecommendationGenerated
ClassificationReviewRequired
ClassificationRecommendationApproved
ClassificationRecommendationRejected
```

### Contracts

```text
Classification Data Contract
Classification Recommendation API Contract
Classification Event Contract
```

### AI Usage

```text
Classification Assistant Agent may suggest classifications, but cannot finalize filing scope without review.
```

### Deferred Scope

```text
full automatic classification finalization
unreviewed filing term generation
complete global local-class automation
```

---

## 8.5 Document

| Field | Value |
|------|-------|
| Type | Baseline Domain |
| Category | Professional |
| MVP Phase | Phase 2 |
| MVP Depth | Must Implement |
| Primary Consumers | MarkReg, MarkOrbit Lite, Workplace, AI Agents |
| Core Purpose | Defines files and generated materials used in professional service execution. |

### Primary Objects

```text
Document
Document Requirement
Document Draft
Document Version
Document Metadata
```

### Primary Services

```text
Document Upload Service
Document Requirement Service
Document Draft Service
Document Validation Service
Document Link Service
```

### Primary Events

```text
DocumentUploaded
DocumentGenerated
DocumentReviewRequired
DocumentApproved
DocumentRejected
```

### Contracts

```text
Document Data Contract
Document API Contract
Document Event Contract
```

### AI Usage

```text
Document Draft Assistant Agent may create non-final drafts under review rules.
```

### Deferred Scope

```text
full document signing workflow
complete document automation
official submission automation
```

---

## 8.6 Evidence

| Field | Value |
|------|-------|
| Type | Baseline Domain |
| Category | Professional |
| MVP Phase | Phase 2 |
| MVP Depth | Partial Implement |
| Primary Consumers | MarkReg, Workplace, AI Agents |
| Core Purpose | Defines proof materials and evidence packages. |

### Primary Objects

```text
Evidence
Evidence Package
Evidence Review Note
Evidence Source
```

### Primary Services

```text
Evidence Upload Service
Evidence Package Service
Evidence Review Service
Evidence Metadata Extraction Service
```

### Primary Events

```text
EvidenceUploaded
EvidencePackageCreated
EvidenceReviewRequired
EvidencePackageFlagged
```

### Contracts

```text
Evidence Data Contract
Evidence Event Contract
Evidence Review Contract
```

### AI Usage

```text
Evidence Review Assistant Agent may assist preliminary evidence review, but cannot make final sufficiency decisions.
```

### Deferred Scope

```text
full evidence scoring engine
automatic evidentiary sufficiency decision
high-risk official evidence submission automation
```

---

# 9. Business Execution Domains

## 9.1 Customer

| Field | Value |
|------|-------|
| Type | Baseline Domain |
| Category | Business Execution |
| MVP Phase | Phase 3 |
| MVP Depth | Must Implement |
| Primary Consumers | MarkReg, MarkOrbit Lite, Workplace |
| Core Purpose | Defines the person or organization receiving service. |

### Primary Objects

```text
Customer
Customer Contact
Customer Organization Link
Customer Service Context
```

### Primary Services

```text
Customer Registration Service
Customer Context Service
Customer Link Service
```

### Primary Events

```text
CustomerCreated
CustomerUpdated
CustomerLinkedToOrder
CustomerLinkedToMatter
```

### Contracts

```text
Customer Data Contract
Customer API Contract
Customer Event Contract
```

### Deferred Scope

```text
full CRM
advanced customer scoring
marketing automation
```

---

## 9.2 Matter

| Field | Value |
|------|-------|
| Type | Baseline Domain |
| Category | Business Execution |
| MVP Phase | Phase 3 |
| MVP Depth | Must Implement |
| Primary Consumers | MarkReg, Workplace, AI Agents |
| Core Purpose | Defines a managed professional service case. |

### Primary Objects

```text
Matter
Matter Status
Matter Participant
Matter Context
Matter Timeline
```

### Primary Services

```text
Matter Creation Service
Matter Status Service
Matter Context Service
Matter Link Service
```

### Primary Events

```text
MatterCreated
MatterUpdated
MatterStatusChanged
MatterClosed
```

### Contracts

```text
Matter Data Contract
Matter API Contract
Matter Event Contract
Matter Workflow Contract
```

### AI Usage

```text
AI may summarize Matter context or suggest next actions under review rules.
```

### Deferred Scope

```text
full case management suite
advanced legal matter strategy automation
```

---

## 9.3 Order

| Field | Value |
|------|-------|
| Type | Baseline Domain |
| Category | Business Execution |
| MVP Phase | Phase 3 |
| MVP Depth | Must Implement |
| Primary Consumers | MarkReg, MarkOrbit Lite, Workplace |
| Core Purpose | Defines a confirmed or pending service request. |

### Primary Objects

```text
Order
Order Item
Order Requirement
Order Status
Order-to-Matter Link
```

### Primary Services

```text
Order Creation Service
Order Validation Service
Order Confirmation Service
Order-to-Matter Conversion Service
```

### Primary Events

```text
OrderCreated
OrderUpdated
OrderConfirmed
OrderConvertedToMatter
```

### Contracts

```text
Order Data Contract
Order API Contract
Order Event Contract
Order-to-Matter Workflow Contract
```

### Deferred Scope

```text
full billing system
full sales commission system
advanced payment orchestration
```

---

## 9.4 Opportunity

| Field | Value |
|------|-------|
| Type | Baseline Domain |
| Category | Business Execution |
| MVP Phase | Phase 4 |
| MVP Depth | Partial Implement |
| Primary Consumers | Opportunity Engine baseline, MarkReg, AI Agents |
| Core Purpose | Defines potential business value or follow-up opportunity. |

### Primary Objects

```text
Opportunity
Opportunity Signal
Opportunity Recommendation
Opportunity Follow-up
```

### Primary Services

```text
Opportunity Detection Baseline Service
Opportunity Creation Service
Opportunity Review Service
```

### Primary Events

```text
OpportunitySignalDetected
OpportunityCreated
OpportunityReviewRequired
```

### Contracts

```text
Opportunity Data Contract
Opportunity Event Contract
Opportunity Review Contract
```

### AI Usage

```text
Opportunity Discovery Agent may detect signals, but sales action requires human review.
```

### Deferred Scope

```text
full opportunity scoring engine
automatic client outreach
full marketing automation
```

---

## 9.5 Workflow Contract

| Field | Value |
|------|-------|
| Type | Baseline Domain |
| Category | Business Execution |
| MVP Phase | Phase 3 |
| MVP Depth | Must Implement |
| Primary Consumers | Workplace, MarkReg, Codex Implementation |
| Core Purpose | Defines allowed execution states and transitions. |

### Primary Objects

```text
Workflow Contract
Workflow State
Workflow Transition
Workflow Rule
```

### Primary Services

```text
Workflow Contract Registration Service
Workflow Transition Validation Service
Workflow State Resolution Service
```

### Primary Events

```text
WorkflowContractCreated
WorkflowTransitionRequested
WorkflowTransitionApproved
WorkflowTransitionRejected
```

### Contracts

```text
Workflow Contract
Workflow Event Contract
Workflow API Contract
```

### Deferred Scope

```text
full workflow designer
product-specific workflow UI
unreviewed workflow automation
```

---

## 9.6 Task

| Field | Value |
|------|-------|
| Type | Baseline Domain |
| Category | Business Execution |
| MVP Phase | Phase 3 |
| MVP Depth | Must Implement |
| Primary Consumers | Workplace, MarkReg, AI Agents |
| Core Purpose | Defines work to be performed. |

### Primary Objects

```text
Task
Task Assignment
Task Status
Task Review Link
```

### Primary Services

```text
Task Creation Service
Task Assignment Service
Task Completion Service
Task Review Service
```

### Primary Events

```text
TaskCreated
TaskAssigned
TaskCompleted
TaskReviewRequired
```

### Contracts

```text
Task Data Contract
Task API Contract
Task Event Contract
```

### AI Usage

```text
Workflow Assistant Agent may suggest next tasks, but cannot bypass task services or review requirements.
```

### Deferred Scope

```text
full project management suite
automatic task completion without review
```

---

## 9.7 Event

| Field | Value |
|------|-------|
| Type | Baseline Domain |
| Category | Business Execution |
| MVP Phase | Phase 3 |
| MVP Depth | Must Implement |
| Primary Consumers | All MVP Consumers |
| Core Purpose | Defines meaningful change in Core state or professional execution. |

### Primary Objects

```text
Event
Event Payload
Event Subscription
Event Audit Reference
```

### Primary Services

```text
Event Publication Service
Event Subscription Service
Event Validation Service
Event Replay Baseline Service
```

### Primary Events

```text
EventPublished
EventConsumed
EventSubscriptionCreated
EventValidationFailed
```

### Contracts

```text
Event Contract
Event Payload Contract
Event Subscription Contract
```

### Deferred Scope

```text
full event streaming platform
advanced replay architecture
analytics-first event model
```

---

## 9.8 Notification

| Field | Value |
|------|-------|
| Type | Baseline Domain |
| Category | Business Execution |
| MVP Phase | Phase 3 |
| MVP Depth | Partial Implement |
| Primary Consumers | Workplace, MarkReg, MarkOrbit Lite |
| Core Purpose | Defines baseline user or system alerting. |

### Primary Objects

```text
Notification
Notification Rule
Notification Recipient
Notification Delivery Record
```

### Primary Services

```text
Notification Dispatch Service
Notification Rule Service
Notification Preference Baseline Service
```

### Primary Events

```text
NotificationCreated
NotificationSent
NotificationFailed
```

### Contracts

```text
Notification Data Contract
Notification Event Contract
```

### Deferred Scope

```text
full notification preference center
multi-channel notification automation
advanced marketing notification
```

---

# 10. Collaboration Network Domains

## 10.1 Partner

| Field | Value |
|------|-------|
| Type | Baseline Domain |
| Category | Collaboration Network |
| MVP Phase | Phase 5 |
| MVP Depth | Reserved Boundary |
| Primary Consumers | MGSN, Partner Center |
| Core Purpose | Defines business partners participating in service or channel relationships. |

### Primary Objects

```text
Partner
Partner Relationship
Partner Capability Link
```

### Primary Services

```text
Partner Registration Baseline Service
Partner Relationship Service
```

### Primary Events

```text
PartnerRegistered
PartnerRelationshipCreated
```

### Contracts

```text
Partner Data Contract
Partner Event Contract
```

### Deferred Scope

```text
full partner center
partner marketplace
commission and rebate automation
```

---

## 10.2 Agent

| Field | Value |
|------|-------|
| Type | Baseline Domain |
| Category | Collaboration Network |
| MVP Phase | Phase 4 |
| MVP Depth | Partial Implement |
| Primary Consumers | MarkReg, MGSN, Workplace |
| Core Purpose | Defines professional agents or law firms that can perform trademark-related work. |

### Primary Objects

```text
Agent
Agent Organization
Agent Jurisdiction Coverage
Agent Capability
Agent Contact
```

### Primary Services

```text
Agent Registration Service
Agent Lookup Service
Agent Capability Service
Agent Contact Service
```

### Primary Events

```text
AgentRegistered
AgentUpdated
AgentCapabilityUpdated
```

### Contracts

```text
Agent Data Contract
Agent API Contract
Agent Event Contract
```

### Deferred Scope

```text
full agent marketplace
provider ranking
network trust scoring
```

---

## 10.3 Service Provider

| Field | Value |
|------|-------|
| Type | Baseline Domain |
| Category | Collaboration Network |
| MVP Phase | Phase 4 |
| MVP Depth | Partial Implement |
| Primary Consumers | MGSN, MarkReg |
| Core Purpose | Defines entities providing services inside or outside the network. |

### Primary Objects

```text
Service Provider
Service Provider Capability
Service Provider Coverage
```

### Primary Services

```text
Service Provider Registration Service
Service Provider Lookup Service
Capability Matching Baseline Service
```

### Primary Events

```text
ServiceProviderRegistered
ServiceProviderCapabilityUpdated
```

### Contracts

```text
Service Provider Data Contract
Service Provider API Contract
Service Provider Event Contract
```

### Deferred Scope

```text
full provider marketplace
automatic provider selection
advanced provider scoring
```

---

## 10.4 Service Network

| Field | Value |
|------|-------|
| Type | Baseline Domain |
| Category | Collaboration Network |
| MVP Phase | Phase 5 |
| MVP Depth | Reserved Boundary |
| Primary Consumers | MGSN |
| Core Purpose | Defines network-level collaboration structure. |

### Primary Objects

```text
Service Network
Network Membership
Network Rule
```

### Primary Services

```text
Service Network Boundary Service
Network Membership Baseline Service
```

### Primary Events

```text
ServiceNetworkReserved
NetworkMembershipCreated
```

### Contracts

```text
Service Network Contract
Network Membership Contract
```

### Deferred Scope

```text
full MGSN marketplace
network trust economy
global service exchange engine
```

---

## 10.5 Routing

| Field | Value |
|------|-------|
| Type | Baseline Domain |
| Category | Collaboration Network |
| MVP Phase | Phase 4 |
| MVP Depth | Partial Implement |
| Primary Consumers | MarkReg, MGSN, AI Agents |
| Core Purpose | Defines how work, matters or recommendations are directed to agents or providers. |

### Primary Objects

```text
Routing Decision
Routing Candidate
Routing Rule
Routing Review Record
```

### Primary Services

```text
Routing Recommendation Service
Routing Review Service
Routing Decision Service
```

### Primary Events

```text
RoutingRecommendationGenerated
RoutingReviewRequired
RoutingDecisionMade
```

### Contracts

```text
Routing Data Contract
Routing API Contract
Routing Event Contract
```

### AI Usage

```text
Routing Assistant Agent may recommend routing, but provider selection requires review.
```

### Deferred Scope

```text
full provider ranking
automatic provider selection
full network routing marketplace
```

---

## 10.6 Communication

| Field | Value |
|------|-------|
| Type | Baseline Domain |
| Category | Collaboration Network |
| MVP Phase | Phase 4 |
| MVP Depth | Partial Implement |
| Primary Consumers | MarkReg, Workplace, AI Agents |
| Core Purpose | Defines linked professional communication. |

### Primary Objects

```text
Communication
Communication Thread
Communication Summary
Communication Action Item
```

### Primary Services

```text
Communication Link Service
Communication Summary Service
Communication Action Item Service
```

### Primary Events

```text
CommunicationLinked
CommunicationSummaryGenerated
CommunicationActionItemDetected
```

### Contracts

```text
Communication Data Contract
Communication API Contract
Communication Event Contract
```

### AI Usage

```text
Communication Summary Agent may summarize communications under permission and review rules.
```

### Deferred Scope

```text
full email client
full communication automation
automatic external reply without approval
```

---

# 11. Cross-Cutting Core Specification Systems

## 11.1 Capability

| Field | Value |
|------|-------|
| Type | Cross-Cutting Core Specification System |
| Category | Cross-Cutting |
| MVP Phase | Phase 1 |
| MVP Depth | Partial Implement |
| Primary Consumers | MarkReg, MarkOrbit Lite, Workplace, AI Agents, MGSN |
| Core Purpose | Defines what can be performed, by whom or by what actor. |

### Primary Objects

```text
Capability
Capability Provider
Capability Scope
Capability Requirement
```

### Primary Services

```text
Capability Registration Service
Capability Matching Service
Capability Validation Service
```

### Primary Events

```text
CapabilityRegistered
CapabilityUpdated
CapabilityMatched
```

### Contracts

```text
Capability Data Contract
Capability Matching API Contract
Capability Event Contract
```

### Important Rule

```text
Capability is not counted as an additional baseline Core Domain.
```

### Deferred Scope

```text
full capability marketplace
automatic provider ranking
commercial capability packaging
```

---

## 11.2 Business Responsibility

| Field | Value |
|------|-------|
| Type | Cross-Cutting Core Specification System |
| Category | Cross-Cutting |
| MVP Phase | Phase 3 |
| MVP Depth | Partial Implement |
| Primary Consumers | Workplace, MarkReg, AI Agents, Codex Implementation |
| Core Purpose | Defines accountability for work. |

### Primary Objects

```text
Responsibility Assignment
Review Record
Approval Record
Escalation Rule
```

### Primary Services

```text
Responsibility Assignment Service
Review Assignment Service
Approval Service
Escalation Baseline Service
```

### Primary Events

```text
ResponsibilityAssigned
ReviewRequired
ReviewApproved
ReviewRejected
EscalationRequired
```

### Contracts

```text
Responsibility Contract
Review Contract
Approval Contract
```

### Important Rule

```text
Business Responsibility is not counted as an additional baseline Core Domain.
```

### Deferred Scope

```text
sales commission
pricing policy
revenue attribution
full business performance management
```

---

# 12. Domain Dependency Chain

The operational dependency chain is:

```text
Identity
↓
Organization / User
↓
Permission / Policy
↓
Knowledge
↓
Brand / Trademark / Jurisdiction / Classification / Document / Evidence
↓
Customer / Order / Matter
↓
Workflow Contract / Task / Event / Notification
↓
Communication / Agent / Service Provider / Routing / Opportunity
↓
Partner / Service Network
```

Cross-cutting systems apply across the chain.

```text
Capability
Business Responsibility
```

---

# 13. Handoff to core-specs/domains/

This index will generate future files under:

```text
core-specs/domains/
```

Expected initial scaffold:

```text
core-specs/domains/README.md
core-specs/domains/_template.md
core-specs/domains/identity.md
core-specs/domains/organization.md
core-specs/domains/user.md
core-specs/domains/permission.md
core-specs/domains/policy.md
core-specs/domains/knowledge.md
core-specs/domains/brand.md
core-specs/domains/trademark.md
core-specs/domains/jurisdiction.md
core-specs/domains/classification.md
core-specs/domains/document.md
core-specs/domains/evidence.md
core-specs/domains/customer.md
core-specs/domains/matter.md
core-specs/domains/order.md
core-specs/domains/opportunity.md
core-specs/domains/workflow-contract.md
core-specs/domains/task.md
core-specs/domains/event.md
core-specs/domains/notification.md
core-specs/domains/partner.md
core-specs/domains/agent.md
core-specs/domains/service-provider.md
core-specs/domains/service-network.md
core-specs/domains/routing.md
core-specs/domains/communication.md
```

Cross-cutting systems may be represented through either:

```text
core-specs/cross-cutting/capability.md
core-specs/cross-cutting/business-responsibility.md
```

or through object/service/contract specs with explicit cross-cutting ownership.

The MVP recommendation is:

```text
Do not treat Capability and Business Responsibility as ordinary domain files unless the cross-cutting status is explicitly marked.
```

---

# 14. Validation Rules

The domain index must pass the following validation checks.

```text
[ ] Baseline domain count equals 26.
[ ] Cross-cutting system count equals 2.
[ ] Total execution rows equal 28.
[ ] All 26 baseline domains belong to one of four categories.
[ ] Capability is marked as cross-cutting.
[ ] Business Responsibility is marked as cross-cutting.
[ ] No product name is listed as a Core Domain.
[ ] No AI Agent is listed as a Core Domain.
[ ] No database table is listed as a Core Domain.
[ ] MVP depth is defined for every row.
[ ] MVP phase is defined for every row.
[ ] Primary consumers are defined for every row.
[ ] Deferred scope is defined for every row.
```

---

# 15. Prohibited Changes

This index must not be changed to:

```text
increase baseline domain count without architecture release
rename baseline domains without architecture release
merge baseline domains without architecture release
split baseline domains without architecture release
promote Capability into ordinary domain silently
promote Business Responsibility into ordinary domain silently
add Product, Workplace, MarkReg, Lite or MGSN as Core Domains
add AI Agent as Core Domain
add database table as Core Domain
```

---

# 16. Handoff to Next Index

The next index should be:

```text
indexes/object-index.md
```

It must be derived from:

```text
B02-APP-C_Core_Object_Index.md
```

It must map every Core Object to:

```text
owning domain
or cross-cutting Core specification system
```

---

# 17. Acceptance Criteria

This index is accepted only if it satisfies the following criteria.

```text
[ ] It preserves the 26 baseline Core Domain Map.
[ ] It includes all four domain categories.
[ ] It lists all Foundation Domains.
[ ] It lists all Professional Domains.
[ ] It lists all Business Execution Domains.
[ ] It lists all Collaboration Network Domains.
[ ] It separately lists Capability and Business Responsibility as cross-cutting systems.
[ ] It explains why there are 28 execution rows.
[ ] It defines MVP phase and MVP depth for every row.
[ ] It defines primary objects, services, events and contracts for every domain/system.
[ ] It defines AI usage where relevant.
[ ] It defines deferred scope for every domain/system.
[ ] It prepares core-specs/domains/.
[ ] It defines validation rules.
[ ] It defines prohibited changes.
[ ] It hands off to object-index.md.
```

---

# 18. Revision Notes

| Version | Status | Notes |
|---------|--------|-------|
| 0.1.0 | Draft | Initial operational Domain Index derived from B02-APP-B. Preserves 26 baseline domains and 2 cross-cutting systems for 28 execution rows. |

---

**End of Index**
