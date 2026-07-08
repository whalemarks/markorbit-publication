# Book 02

# Appendix F — API Index

**Book Title:** MarkOrbit Core Specification  
**Appendix ID:** B02-APP-F  
**Appendix Title:** API Index  
**Appendix Type:** Canonical Index  
**Rewrite Stage:** Second Canonical Draft  
**Status:** Draft  
**Version:** 0.2.0  
**Owner:** MarkOrbit Publications Editorial Board  

**Related Documents:**

- B02-CH-03 — Core Position
- B02-CH-04 — Core Boundary
- B02-CH-05 — Core Principles
- B02-CH-17 — Core Contract Architecture
- B02-CH-22 — Domain Specification
- B02-CH-24 — Service Specification
- B02-CH-25 — Event Specification
- B02-CH-27 — Core Consumption Specification
- B02-CH-28 — Core MVP Boundary
- B02-CH-30 — MVP Execution Matrix
- B02-APP-A — Glossary
- B02-APP-B — Core Domain Index
- B02-APP-C — Core Object Index
- B02-APP-D — Core Service Index
- B02-APP-E — Event Index

---

# 1. Appendix Purpose

This appendix defines the canonical API Index for the MarkOrbit Core.

Book 02 does not include a standalone API chapter.

That is intentional.

API is not a separate source of Core meaning.

API is a governed consumption surface of Core Objects, Core Services, Core Events and Core Contracts.

This appendix makes API explicit without turning API into architecture ownership.

The purpose of this appendix is to define:

```text
which API surfaces are required for MVP
which API surfaces are partial or future
which Core Domains and Services own each API
which Contracts govern each API
which Consumers may use each API
which Events may be emitted
which permissions, policies, AI rules and audit rules apply
```

This appendix prepares the future scaffold:

```text
core-specs/api/
```

and the future template:

```text
core-specs/api/_template.md
```

---

# 2. API Canonical Rule

The canonical API rule is:

```text
API is a contract-bound consumption surface.
API does not define Core meaning.
```

This means:

```text
Core Object defines meaning.
Core Service defines responsibility.
Core Event defines meaningful change.
Core Contract defines consumption safety.
API exposes governed access.
```

An API may expose Core capability.

An API may not redefine Core capability.

---

# 3. API Position

API sits between Core Services and Core Consumers.

```text
Core Domain
    ↓
Core Object
    ↓
Core Service
    ↓
Core Contract
    ↓
API Surface
    ↓
Core Consumer
```

API must not bypass:

```text
Object Specification
Service Specification
Permission
Policy
Event Contract
Data Contract
AI Agent Contract
Workflow Contract
Audit Rule
```

---

# 4. API Scope

## 4.1 In Scope

This appendix defines:

```text
API categories
API naming rules
API ownership rules
API contract requirements
MVP API surfaces
Partial API surfaces
Future API surfaces
API index fields
API template expectations
API consumer boundaries
API event side effects
API permission and audit requirements
API anti-patterns
core-specs/api/ readiness
```

## 4.2 Out of Scope

This appendix does not define:

```text
final HTTP routes
request body schemas
response body schemas
OpenAPI files
SDK design
rate limit implementation
vendor-specific API mapping
authentication implementation
deployment gateway configuration
production endpoint versioning policy
```

Those belong to future `core-specs/api/`, implementation tasks or infrastructure design.

---

# 5. API Categories

Book 02 recognizes eight API categories.

```text
Core Object API
Core Service API
Query API
Command API
Event API
AI Invocation API
Integration API
Consumption API
```

## 5.1 Core Object API

Exposes approved read access to Core Objects.

It must follow Data Contracts and field exposure rules.

## 5.2 Core Service API

Exposes governed Core Services.

It must follow Service Specifications and permission rules.

## 5.3 Query API

Reads data or retrieves recommendations without mutating Core state.

It must define read boundary and audit rules where required.

## 5.4 Command API

Creates or changes Core state.

It must invoke a governed Core Service.

It must define Events emitted.

## 5.5 Event API

Exposes event publication or subscription surfaces.

It must follow Event Contracts.

## 5.6 AI Invocation API

Invokes governed AI Agents or AI-assisted Services.

It must require Agent Contract, authorized knowledge and review rules.

## 5.7 Integration API

Exposes Core to external systems or accepts data from them.

It must follow Integration Contracts, Data Contracts and audit rules.

## 5.8 Consumption API

Exposes Core to products, Workplace, AI agents or Codex consumers under Consumption Contracts.

---

# 6. API Naming Rules

API names must be semantic and contract-bound.

## 6.1 API Name Format

Use:

```text
<Domain or System> <Capability> API
```

Examples:

```text
Identity API
Knowledge Retrieval API
Trademark API
Jurisdiction Requirement API
Classification Recommendation API
Document API
Order API
Matter API
Task API
Event API
AI Invocation API
Core Consumption API
```

## 6.2 API File Name Format

Use lowercase kebab-case.

Examples:

```text
identity-api.md
knowledge-retrieval-api.md
classification-recommendation-api.md
ai-invocation-api.md
core-consumption-api.md
```

## 6.3 Prohibited Names

Do not use vague names such as:

```text
Common API
Utility API
Helper API
Data API
AI API
Workflow API
System API
General API
```

unless the file clearly defines a specific governed surface.

---

# 7. API Index Fields

Every API Index entry should include:

```text
API ID
API Name
API File Name
API Category
Owning Domain or Cross-Cutting System
Owning Service
Core Objects Read
Core Objects Created or Updated
Input Contract
Output Contract
Permission Requirement
Policy Requirement
Knowledge Dependency
AI Usage
Human Review Requirement
Events Emitted
Events Consumed
Audit Requirement
Primary Consumers
Consumer Priority Classification
MVP Phase
MVP Depth
Deferred Scope
Acceptance Criteria
```

---

# 8. MVP API Surfaces

The following API surfaces are required or expected for the Core MVP.

```text
Identity API
Organization API
User API
Permission API
Knowledge Retrieval API
Brand API
Trademark API
Jurisdiction Requirement API
Classification Recommendation API
Document API
Customer API
Order API
Matter API
Workflow Contract API
Task API
Event API
Notification API baseline
AI Invocation API
Core Consumption API baseline
```

These APIs do not imply full product implementation.

They define the minimum governed API surfaces needed by MVP consumers.

MVP consumers are:

```text
MarkReg
MarkOrbit Lite
Workplace
AI Agents
Codex Implementation
```

---

# 9. Partial API Surfaces

The following API surfaces are partial in MVP.

```text
Policy API
Evidence API
Opportunity API
Communication API
Agent API
Service Provider API
Routing API
Capability API
Business Responsibility API
```

Partial API surfaces may define:

```text
read baseline
minimal creation/update capability
controlled service invocation
limited event subscription
reserved future fields
```

They must not expand into full future platform scope.

---

# 10. Future API Surfaces

The following API surfaces are future or reserved.

```text
Partner API
Service Network API
External Partner API
MGSN Provider API
Brand Asset Vault API
Opportunity Engine API
Reporting API
Public Developer API
Webhook API
Advanced Integration API
Network Trust API
Provider Ranking API
Marketplace API
```

These APIs must not be implemented deeply in Core MVP unless architecture governance explicitly changes the scope.

---

# 11. Foundation API Index

## 11.1 Identity API

```text
API ID: B02-API-001
API Name: Identity API
API File Name: identity-api.md
API Category: Core Object / Core Service API
Owning Domain: Identity
Owning Services:
    Identity Resolution Service
    Actor Identity Validation Service
Core Objects Read:
    Identity
Core Objects Created or Updated:
    Identity
Input Contract:
    Identity Input Contract
Output Contract:
    Identity Data Contract
Permission Requirement:
    Required
Policy Requirement:
    Required where actor type affects access
AI Usage:
    AI Agent Identity validation only
Events Emitted:
    IdentityCreated
    IdentityUpdated
Audit Requirement:
    Required
Primary Consumers:
    Workplace
    MarkReg
    MarkOrbit Lite
    AI Agents
    Codex Implementation
Consumer Priority Classification:
    MVP Consumer
MVP Phase:
    Phase 1 — Foundation Core
MVP Depth:
    Must Implement
```

## 11.2 Organization API

```text
API ID: B02-API-002
API Name: Organization API
API File Name: organization-api.md
API Category: Core Object / Query / Command API
Owning Domain: Organization
Owning Services:
    Organization Registration Service
    Organization Lookup Service
Core Objects Read:
    Organization
Core Objects Created or Updated:
    Organization
Input Contract:
    Organization Input Contract
Output Contract:
    Organization Data Contract
Permission Requirement:
    Required
Events Emitted:
    OrganizationCreated
    OrganizationUpdated
Audit Requirement:
    Required
Primary Consumers:
    MarkReg
    MarkOrbit Lite
    Workplace
MVP Phase:
    Phase 1 — Foundation Core
MVP Depth:
    Must Implement
```

## 11.3 User API

```text
API ID: B02-API-003
API Name: User API
API File Name: user-api.md
API Category: Core Object / Core Service API
Owning Domain: User
Owning Services:
    User Registration Service
    User Profile Service
    User Role Binding Service
Core Objects Read:
    User
    Identity
    Organization
Core Objects Created or Updated:
    User
Input Contract:
    User Input Contract
Output Contract:
    User Data Contract
Permission Requirement:
    Required
Events Emitted:
    UserCreated
    UserUpdated
Audit Requirement:
    Required
Primary Consumers:
    Workplace
    MarkReg
    MarkOrbit Lite
MVP Phase:
    Phase 1 — Foundation Core
MVP Depth:
    Must Implement
```

## 11.4 Permission API

```text
API ID: B02-API-004
API Name: Permission API
API File Name: permission-api.md
API Category: Query / Service API
Owning Domain: Permission
Owning Services:
    Permission Check Service
    Permission Assignment Service
Core Objects Read:
    Permission Rule
    User
    Identity
Core Objects Created or Updated:
    Permission Rule baseline where approved
Input Contract:
    Permission Check Input Contract
Output Contract:
    Permission Decision Contract
Permission Requirement:
    Required
Policy Requirement:
    Required
Events Emitted:
    PermissionGranted
    PermissionChanged
Audit Requirement:
    Required
Primary Consumers:
    All MVP Consumers
MVP Phase:
    Phase 1 — Foundation Core
MVP Depth:
    Must Implement
```

## 11.5 Policy API

```text
API ID: B02-API-005
API Name: Policy API
API File Name: policy-api.md
API Category: Query / Validation API
Owning Domain: Policy
Owning Services:
    Policy Evaluation Service
Core Objects Read:
    Policy Rule
Core Objects Created or Updated:
    Policy Rule baseline where approved
Input Contract:
    Policy Evaluation Input Contract
Output Contract:
    Policy Decision Contract
Permission Requirement:
    Required
Events Emitted:
    PolicyRuleCreated
    PolicyRuleChanged
Audit Requirement:
    Required where policy affects access, AI or review
Primary Consumers:
    Workplace
    AI Agents
    Codex Implementation
MVP Phase:
    Phase 1 — Foundation Core
MVP Depth:
    Partial Implement
```

## 11.6 Knowledge Retrieval API

```text
API ID: B02-API-006
API Name: Knowledge Retrieval API
API File Name: knowledge-retrieval-api.md
API Category: Query / AI-supporting API
Owning Domain: Knowledge
Owning Services:
    Knowledge Retrieval Service
    Knowledge Validation Service
    Knowledge Gap Detection Service
Core Objects Read:
    Knowledge Source
    Knowledge Asset
    Knowledge Rule
Core Objects Created or Updated:
    Knowledge Gap
Input Contract:
    Knowledge Query Contract
Output Contract:
    Knowledge Result Contract
Permission Requirement:
    Required
Policy Requirement:
    Required for jurisdiction and AI access
AI Usage:
    Authorized knowledge retrieval
Events Emitted:
    KnowledgeRetrieved
    KnowledgeGapDetected
Audit Requirement:
    Required for AI and professional use
Primary Consumers:
    MarkOrbit Lite
    MarkReg
    AI Agents
    Workplace
MVP Phase:
    Phase 1 — Foundation Core
MVP Depth:
    Must Implement
```

---

# 12. Professional API Index

## 12.1 Brand API

```text
API ID: B02-API-007
API Name: Brand API
API File Name: brand-api.md
API Category: Core Object API
Owning Domain: Brand
Owning Services:
    Brand Registration Service
    Brand Lookup Service
Core Objects Read:
    Brand
Core Objects Created or Updated:
    Brand
Input Contract:
    Brand Input Contract
Output Contract:
    Brand Data Contract
Permission Requirement:
    Required
Events Emitted:
    BrandCreated
    BrandUpdated
Audit Requirement:
    Required
Primary Consumers:
    MarkReg
    MarkOrbit Lite
MVP Phase:
    Phase 2 — Professional Core
MVP Depth:
    Must Implement
```

## 12.2 Trademark API

```text
API ID: B02-API-008
API Name: Trademark API
API File Name: trademark-api.md
API Category: Core Object / Query / Command API
Owning Domain: Trademark
Owning Services:
    Trademark Registration Service
    Trademark Lookup Service
    Trademark Status Normalization Service
Core Objects Read:
    Trademark
    Brand
    Jurisdiction
    Classification
Core Objects Created or Updated:
    Trademark
Input Contract:
    Trademark Input Contract
Output Contract:
    Trademark Data Contract
Permission Requirement:
    Required
Policy Requirement:
    Required for jurisdiction-sensitive data
AI Usage:
    Trademark Status Summary Agent may consume read outputs
Events Emitted:
    TrademarkCreated
    TrademarkUpdated
    TrademarkStatusChanged
Audit Requirement:
    Required
Primary Consumers:
    MarkReg
    MarkOrbit Lite
    Workplace
    AI Agents
MVP Phase:
    Phase 2 — Professional Core
MVP Depth:
    Must Implement
```

## 12.3 Jurisdiction Requirement API

```text
API ID: B02-API-009
API Name: Jurisdiction Requirement API
API File Name: jurisdiction-requirement-api.md
API Category: Query / Validation API
Owning Domain: Jurisdiction
Owning Services:
    Jurisdiction Requirement Retrieval Service
    Jurisdiction Rule Validation Service
Core Objects Read:
    Jurisdiction
    Knowledge Asset
    Document Requirement
Core Objects Created or Updated:
    none in MVP unless governance approves
Input Contract:
    Jurisdiction Query Contract
Output Contract:
    Jurisdiction Requirement Contract
Permission Requirement:
    Required
Knowledge Dependency:
    Required
AI Usage:
    AI consultation and document requirement support
Events Emitted:
    JurisdictionRequirementRetrieved
    KnowledgeGapDetected where applicable
Audit Requirement:
    Required for professional and AI use
Primary Consumers:
    MarkReg
    MarkOrbit Lite
    AI Agents
MVP Phase:
    Phase 2 — Professional Core
MVP Depth:
    Must Implement
```

## 12.4 Classification Recommendation API

```text
API ID: B02-API-010
API Name: Classification Recommendation API
API File Name: classification-recommendation-api.md
API Category: Query / Recommendation / AI Invocation API
Owning Domain: Classification
Owning Services:
    Classification Recommendation Service
    Goods and Services Validation Service
Core Objects Read:
    Classification Term
    Trademark
    Brand
    Knowledge Asset
Core Objects Created or Updated:
    Classification Recommendation
Input Contract:
    Classification Request Contract
Output Contract:
    Classification Recommendation Contract
Permission Requirement:
    Required
Policy Requirement:
    Required for jurisdiction-specific constraints
AI Usage:
    Classification Assistant Agent
Human Review Requirement:
    Required where professional risk is above threshold
Events Emitted:
    ClassificationRecommendationGenerated
    AIRecommendationReviewRequired
Audit Requirement:
    Required
Primary Consumers:
    MarkOrbit Lite
    MarkReg
    AI Agents
MVP Phase:
    Phase 2 — Professional Core
MVP Depth:
    Must Implement
```

## 12.5 Document API

```text
API ID: B02-API-011
API Name: Document API
API File Name: document-api.md
API Category: Core Object / Command / Query API
Owning Domain: Document
Owning Services:
    Document Upload Service
    Document Generation Service
    Document Validation Service
Core Objects Read:
    Document
    Document Requirement
    Matter
    Trademark
Core Objects Created or Updated:
    Document
Input Contract:
    Document Input Contract
Output Contract:
    Document Data Contract
Permission Requirement:
    Required
Policy Requirement:
    Required for access and export
AI Usage:
    Document Draft Assistant Agent may produce drafts under review
Human Review Requirement:
    Required for professional documents where risk applies
Events Emitted:
    DocumentUploaded
    DocumentGenerated
    DocumentReviewRequired
    DocumentApproved
Audit Requirement:
    Required
Primary Consumers:
    MarkReg
    MarkOrbit Lite
    Workplace
    AI Agents
MVP Phase:
    Phase 2 — Professional Core
MVP Depth:
    Must Implement
```

## 12.6 Evidence API

```text
API ID: B02-API-012
API Name: Evidence API
API File Name: evidence-api.md
API Category: Query / Command / Review API
Owning Domain: Evidence
Owning Services:
    Evidence Collection Service
    Evidence Review Service
    Evidence Package Service
Core Objects Read:
    Evidence Item
    Evidence Package
    Document
Core Objects Created or Updated:
    Evidence Item
    Evidence Package
Input Contract:
    Evidence Input Contract
Output Contract:
    Evidence Data Contract
Permission Requirement:
    Required
Policy Requirement:
    Required for high-risk evidence use
AI Usage:
    Evidence Review Assistant Agent under review rules
Human Review Requirement:
    Required
Events Emitted:
    EvidenceUploaded
    EvidenceReviewRequired
    EvidenceApproved
Audit Requirement:
    Required
Primary Consumers:
    MarkReg
    Workplace
    AI Agents
MVP Phase:
    Phase 2 — Professional Core
MVP Depth:
    Partial Implement
```

---

# 13. Business Execution API Index

## 13.1 Customer API

```text
API ID: B02-API-013
API Name: Customer API
API File Name: customer-api.md
API Category: Core Object / Command / Query API
Owning Domain: Customer
Owning Services:
    Customer Registration Service
    Customer Lookup Service
Core Objects Read:
    Customer
    Organization
    Identity
Core Objects Created or Updated:
    Customer
Input Contract:
    Customer Input Contract
Output Contract:
    Customer Data Contract
Permission Requirement:
    Required
Events Emitted:
    CustomerCreated
    CustomerUpdated
Audit Requirement:
    Required
Primary Consumers:
    MarkReg
    MarkOrbit Lite
    Workplace
MVP Phase:
    Phase 3 — Business Execution Core
MVP Depth:
    Must Implement
```

## 13.2 Order API

```text
API ID: B02-API-014
API Name: Order API
API File Name: order-api.md
API Category: Command / Query API
Owning Domain: Order
Owning Services:
    Order Creation Service
    Order Confirmation Service
    Order Validation Service
Core Objects Read:
    Customer
    Brand
    Trademark
    Jurisdiction
    Classification
Core Objects Created or Updated:
    Order
Input Contract:
    Order Input Contract
Output Contract:
    Order Data Contract
Permission Requirement:
    Required
Policy Requirement:
    Required for business rules
Events Emitted:
    OrderCreated
    OrderConfirmed
    OrderValidationFailed
Audit Requirement:
    Required
Primary Consumers:
    MarkReg
    MarkOrbit Lite
    Workplace
MVP Phase:
    Phase 3 — Business Execution Core
MVP Depth:
    Must Implement
```

## 13.3 Matter API

```text
API ID: B02-API-015
API Name: Matter API
API File Name: matter-api.md
API Category: Command / Query API
Owning Domain: Matter
Owning Services:
    Matter Creation Service
    Matter Status Service
    Order-to-Matter Conversion Service
Core Objects Read:
    Order
    Customer
    Trademark
    Jurisdiction
    Workflow Contract
Core Objects Created or Updated:
    Matter
Input Contract:
    Matter Input Contract
Output Contract:
    Matter Data Contract
Permission Requirement:
    Required
Policy Requirement:
    Required
Events Emitted:
    MatterCreated
    MatterStatusChanged
    OrderConvertedToMatter
Audit Requirement:
    Required
Primary Consumers:
    MarkReg
    Workplace
    Codex Implementation
MVP Phase:
    Phase 3 — Business Execution Core
MVP Depth:
    Must Implement
```

## 13.4 Workflow Contract API

```text
API ID: B02-API-016
API Name: Workflow Contract API
API File Name: workflow-contract-api.md
API Category: Query / Validation / Command API
Owning Domain: Workflow Contract
Owning Services:
    Workflow Contract Retrieval Service
    Workflow Transition Validation Service
    Workflow State Transition Service
Core Objects Read:
    Workflow Contract
    Matter
    Task
Core Objects Created or Updated:
    Workflow State where approved
Input Contract:
    Workflow Transition Input Contract
Output Contract:
    Workflow Transition Decision Contract
Permission Requirement:
    Required
Policy Requirement:
    Required
Events Emitted:
    WorkflowStateChanged
    ReviewRequired
Audit Requirement:
    Required
Primary Consumers:
    Workplace
    MarkReg
    AI Agents
MVP Phase:
    Phase 3 — Business Execution Core
MVP Depth:
    Must Implement
```

## 13.5 Task API

```text
API ID: B02-API-017
API Name: Task API
API File Name: task-api.md
API Category: Command / Query API
Owning Domain: Task
Owning Services:
    Task Creation Service
    Task Assignment Service
    Task Completion Service
Core Objects Read:
    Task
    Matter
    User
    Responsibility Assignment
Core Objects Created or Updated:
    Task
Input Contract:
    Task Input Contract
Output Contract:
    Task Data Contract
Permission Requirement:
    Required
Policy Requirement:
    Required
Events Emitted:
    TaskCreated
    TaskAssigned
    TaskCompleted
Audit Requirement:
    Required
Primary Consumers:
    Workplace
    MarkReg
    AI Agents
MVP Phase:
    Phase 3 — Business Execution Core
MVP Depth:
    Must Implement
```

## 13.6 Event API

```text
API ID: B02-API-018
API Name: Event API
API File Name: event-api.md
API Category: Event API
Owning Domain: Event
Owning Services:
    Event Publication Service
    Event Subscription Service
    Event Replay Service baseline
Core Objects Read:
    Core Event
Core Objects Created or Updated:
    Core Event
Input Contract:
    Event Publication Contract
Output Contract:
    Event Subscription Contract
Permission Requirement:
    Required
Policy Requirement:
    Required for event exposure
Events Emitted:
    EventPublished
Audit Requirement:
    Required
Primary Consumers:
    Workplace
    MarkReg
    MarkOrbit Lite
    AI Agents
    Codex Implementation
MVP Phase:
    Phase 3 — Business Execution Core
MVP Depth:
    Must Implement
```

## 13.7 Notification API

```text
API ID: B02-API-019
API Name: Notification API
API File Name: notification-api.md
API Category: Notification / Event Consumer API
Owning Domain: Notification
Owning Services:
    Notification Dispatch Service
    Notification Preference Service baseline
Core Objects Read:
    Notification
    Event
    Task
Core Objects Created or Updated:
    Notification
Input Contract:
    Notification Input Contract
Output Contract:
    Notification Data Contract
Permission Requirement:
    Required
Events Emitted:
    NotificationCreated
    NotificationSent
Audit Requirement:
    Required where notification affects responsibility or deadline
Primary Consumers:
    Workplace
    MarkReg
MVP Phase:
    Phase 3 — Business Execution Core
MVP Depth:
    Partial Implement
```

## 13.8 Opportunity API

```text
API ID: B02-API-020
API Name: Opportunity API
API File Name: opportunity-api.md
API Category: Query / Recommendation API
Owning Domain: Opportunity
Owning Services:
    Opportunity Creation Service baseline
    Opportunity Discovery Service baseline
Core Objects Read:
    Customer
    Trademark
    Jurisdiction
    Order
Core Objects Created or Updated:
    Opportunity
Input Contract:
    Opportunity Signal Contract
Output Contract:
    Opportunity Data Contract
Permission Requirement:
    Required
AI Usage:
    Opportunity Discovery Agent baseline
Human Review Requirement:
    Required before business action
Events Emitted:
    OpportunityCreated
    OpportunityReviewRequired
Audit Requirement:
    Required
Primary Consumers:
    MarkReg
    Opportunity Engine baseline
    AI Agents
MVP Phase:
    Phase 4 — Growth Core Baseline
MVP Depth:
    Partial Implement
Deferred Scope:
    Full scoring engine
    full revenue attribution
    advanced recommendation ranking
```

---

# 14. Collaboration Network API Index

## 14.1 Communication API

```text
API ID: B02-API-021
API Name: Communication API
API File Name: communication-api.md
API Category: Query / Command / Integration API
Owning Domain: Communication
Owning Services:
    Communication Linking Service
    Communication Summary Service baseline
Core Objects Read:
    Communication
    Matter
    Customer
    Agent
Core Objects Created or Updated:
    Communication
Input Contract:
    Communication Input Contract
Output Contract:
    Communication Data Contract
Permission Requirement:
    Required
AI Usage:
    Communication Summary Agent baseline
Events Emitted:
    CommunicationLinked
    CommunicationSummaryGenerated
Audit Requirement:
    Required
Primary Consumers:
    MarkReg
    Workplace
    AI Agents
MVP Phase:
    Phase 4 — Growth Core Baseline
MVP Depth:
    Partial Implement
```

## 14.2 Agent API

```text
API ID: B02-API-022
API Name: Agent API
API File Name: agent-api.md
API Category: Query / Command API
Owning Domain: Agent
Owning Services:
    Agent Lookup Service
    Agent Capability Profile Service baseline
Core Objects Read:
    Agent
    Capability
    Jurisdiction
Core Objects Created or Updated:
    Agent baseline profile
Input Contract:
    Agent Input Contract
Output Contract:
    Agent Data Contract
Permission Requirement:
    Required
Events Emitted:
    AgentCreated
    AgentUpdated
Audit Requirement:
    Required
Primary Consumers:
    MarkReg
    MGSN baseline
    Routing
MVP Phase:
    Phase 4 — Growth Core Baseline
MVP Depth:
    Partial Implement
```

## 14.3 Service Provider API

```text
API ID: B02-API-023
API Name: Service Provider API
API File Name: service-provider-api.md
API Category: Query / Command API
Owning Domain: Service Provider
Owning Services:
    Service Provider Lookup Service
    Provider Capability Baseline Service
Core Objects Read:
    Service Provider
    Capability
Core Objects Created or Updated:
    Service Provider baseline profile
Input Contract:
    Service Provider Input Contract
Output Contract:
    Service Provider Data Contract
Permission Requirement:
    Required
Events Emitted:
    ServiceProviderCreated
    ServiceProviderUpdated
Audit Requirement:
    Required
Primary Consumers:
    MGSN baseline
    MarkReg
MVP Phase:
    Phase 4 — Growth Core Baseline
MVP Depth:
    Partial Implement
```

## 14.4 Routing API

```text
API ID: B02-API-024
API Name: Routing API
API File Name: routing-api.md
API Category: Recommendation / Review API
Owning Domain: Routing
Owning Services:
    Routing Recommendation Service
    Routing Decision Review Service
Core Objects Read:
    Agent
    Service Provider
    Jurisdiction
    Capability
    Matter
Core Objects Created or Updated:
    Routing Decision
Input Contract:
    Routing Request Contract
Output Contract:
    Routing Decision Contract
Permission Requirement:
    Required
Policy Requirement:
    Required for routing constraints
AI Usage:
    Routing Assistant Agent baseline
Human Review Requirement:
    Required where routing affects responsibility or external assignment
Events Emitted:
    RoutingRecommendationGenerated
    RoutingDecisionMade
    RoutingReviewRequired
Audit Requirement:
    Required
Primary Consumers:
    MarkReg
    MGSN baseline
    Workplace
    AI Agents
MVP Phase:
    Phase 4 — Growth Core Baseline
MVP Depth:
    Partial Implement
```

## 14.5 Partner API

```text
API ID: B02-API-025
API Name: Partner API
API File Name: partner-api.md
API Category: Future API
Owning Domain: Partner
Owning Services:
    Partner Registration Service future
Core Objects Read:
    Partner
Core Objects Created or Updated:
    Partner future
Permission Requirement:
    Required
Audit Requirement:
    Required
Primary Consumers:
    Partner Center
    MGSN
MVP Phase:
    Phase 5 — Network Reserved
MVP Depth:
    Reserved Boundary
Deferred Scope:
    full partner center
    channel management
    commercial partner policies
```

## 14.6 Service Network API

```text
API ID: B02-API-026
API Name: Service Network API
API File Name: service-network-api.md
API Category: Future API
Owning Domain: Service Network
Owning Services:
    Network Membership Service future
    Service Exchange Service future
Core Objects Read:
    Service Network
    Partner
    Agent
    Service Provider
Core Objects Created or Updated:
    Service Network future
Permission Requirement:
    Required
Audit Requirement:
    Required
Primary Consumers:
    MGSN
MVP Phase:
    Phase 5 — Network Reserved
MVP Depth:
    Reserved Boundary
Deferred Scope:
    full MGSN marketplace
    network trust scoring
    provider ranking
    advanced service exchange
```

---

# 15. Cross-Cutting API Index

## 15.1 Capability API

```text
API ID: B02-API-027
API Name: Capability API
API File Name: capability-api.md
API Category: Cross-Cutting Query / Validation API
Owning System: Capability
Classification: Cross-Cutting Core Specification System
Owning Services:
    Capability Lookup Service
    Capability Matching Service baseline
Core Objects Read:
    Capability
    Capability Provider
    Agent
    Service Provider
    User
    AI Agent
Core Objects Created or Updated:
    Capability baseline where approved
Input Contract:
    Capability Query Contract
Output Contract:
    Capability Result Contract
Permission Requirement:
    Required
AI Usage:
    AI capability binding and routing support
Events Emitted:
    CapabilityMatched
Audit Requirement:
    Required where capability affects assignment or routing
Primary Consumers:
    Workplace
    MarkReg
    MGSN baseline
    AI Agents
MVP Phase:
    Phase 1 / Phase 4
MVP Depth:
    Partial Implement
Canonical Note:
    Capability is not counted as an additional baseline Core Domain.
```

## 15.2 Business Responsibility API

```text
API ID: B02-API-028
API Name: Business Responsibility API
API File Name: business-responsibility-api.md
API Category: Cross-Cutting Review / Assignment API
Owning System: Business Responsibility
Classification: Cross-Cutting Core Specification System
Owning Services:
    Responsibility Assignment Service
    Review Assignment Service
    Approval Recording Service
Core Objects Read:
    Responsibility Assignment
    Review Record
    User
    Task
    Matter
    AI Output
Core Objects Created or Updated:
    Responsibility Assignment
    Review Record
Input Contract:
    Responsibility Assignment Contract
Output Contract:
    Responsibility Decision Contract
Permission Requirement:
    Required
Policy Requirement:
    Required
AI Usage:
    AI Output review and approval linkage
Human Review Requirement:
    Required
Events Emitted:
    ResponsibilityAssigned
    ReviewRequired
    ReviewApproved
    ReviewRejected
Audit Requirement:
    Required
Primary Consumers:
    Workplace
    MarkReg
    AI Agents
    Codex Implementation
MVP Phase:
    Phase 3
MVP Depth:
    Partial Implement
Canonical Note:
    Business Responsibility is not counted as an additional baseline Core Domain.
```

## 15.3 AI Invocation API

```text
API ID: B02-API-029
API Name: AI Invocation API
API File Name: ai-invocation-api.md
API Category: AI Invocation API
Owning System: AI Governance
Owning Services:
    AI Agent Invocation Service
    AI Output Recording Service
    AI Review Routing Service
Core Objects Read:
    AI Agent
    Agent Contract
    Knowledge Asset
    Core Objects authorized by Agent Contract
Core Objects Created or Updated:
    AI Output
    AI Recommendation
    AI Audit Record
Input Contract:
    AI Invocation Contract
Output Contract:
    AI Output Contract
Permission Requirement:
    Required
Policy Requirement:
    Required
Knowledge Dependency:
    Required and authorized
Human Review Requirement:
    Based on risk level
Events Emitted:
    AIAgentInvoked
    AIOutputGenerated
    AIRecommendationGenerated
    AIRecommendationReviewRequired
Audit Requirement:
    Required
Primary Consumers:
    MarkReg
    MarkOrbit Lite
    Workplace
    AI Agents
MVP Phase:
    Phase 4 — AI Governance and Review
MVP Depth:
    Must Implement baseline governance
```

## 15.4 Core Consumption API

```text
API ID: B02-API-030
API Name: Core Consumption API
API File Name: core-consumption-api.md
API Category: Consumption API
Owning System: Core Consumption
Owning Services:
    Consumer Registration Service baseline
    Consumption Boundary Validation Service
Core Objects Read:
    Consumption Contract
    Data Contract
    API Contract
    Event Contract
    Agent Contract
Core Objects Created or Updated:
    Consumption Contract baseline where approved
Input Contract:
    Consumption Request Contract
Output Contract:
    Consumption Decision Contract
Permission Requirement:
    Required
Policy Requirement:
    Required
Events Emitted:
    CoreConsumptionRegistered
    CoreConsumptionViolationDetected
Audit Requirement:
    Required
Primary Consumers:
    Products
    Workplace
    AI Agents
    Codex Implementation
MVP Phase:
    Cross-phase baseline
MVP Depth:
    Must Implement baseline rules
```

---

# 16. API Consumer Classification

## 16.1 MVP Consumer APIs

APIs required for MVP consumers include:

```text
Identity API
Organization API
User API
Permission API
Knowledge Retrieval API
Brand API
Trademark API
Jurisdiction Requirement API
Classification Recommendation API
Document API
Customer API
Order API
Matter API
Workflow Contract API
Task API
Event API
AI Invocation API
Core Consumption API
```

## 16.2 Partial Consumer APIs

APIs partially required for MVP include:

```text
Policy API
Evidence API
Notification API
Opportunity API
Communication API
Agent API
Service Provider API
Routing API
Capability API
Business Responsibility API
```

## 16.3 Future Consumer APIs

Future APIs include:

```text
Partner API
Service Network API
External Partner API
MGSN Provider API
Brand Asset Vault API
Opportunity Engine API
Reporting API
Public Developer API
Webhook API
Advanced Integration API
```

---

# 17. API Permission Rules

Every API must define permission requirements.

Permission rules must answer:

```text
Who may call this API?
What object scope may they access?
What organization scope applies?
What role or capability is required?
Can AI call this API?
Can external integrations call this API?
Can Codex use this API in fixtures or tests?
Is audit required?
```

No API may be considered public by default.

---

# 18. API Event Side Effect Rules

Every command or mutation API must define event side effects.

A command API must state:

```text
Events emitted
Event source domain
Payload contract
Downstream consumers
Audit requirement
Idempotency rule
```

A query API may emit access or audit events where required.

AI invocation APIs must emit AI audit events.

---

# 19. API and AI Rules

AI-related APIs must follow AI Governance.

No AI API may operate without:

```text
AI Agent Identity
Agent Contract
Authorized Knowledge
Allowed Object Access
Risk Level
Human Review Rule
AI Output Contract
AI Audit Record
Failure Behavior
```

AI Invocation API is not a generic model-call API.

It is a governed Core AI consumption surface.

---

# 20. API and Workflow Rules

APIs that affect workflow must follow Workflow Contracts.

Workflow-affecting APIs include:

```text
Order API
Matter API
Workflow Contract API
Task API
Document API
Evidence API
Business Responsibility API
AI Invocation API
Routing API
```

These APIs must define:

```text
allowed states
allowed transitions
responsible actor
review requirement
events emitted
notifications triggered
audit record
```

---

# 21. API and External Integration Rules

External integrations must not consume internal APIs casually.

External integration APIs require:

```text
Integration Contract
Data Contract
API Contract
Permission Rule
Policy Rule
Audit Rule
Vendor Mapping Rule
Failure Handling Rule
```

External systems must not define Core status, event meaning or object lifecycle.

---

# 22. Future core-specs/api Template

Future file:

```text
core-specs/api/_template.md
```

Recommended template:

```text
# API Specification

1. API Identity
2. API Category
3. Owning Domain or System
4. Owning Service
5. API Purpose
6. Consumers
7. Consumer Priority Classification
8. Input Contract
9. Output Contract
10. Core Objects Read
11. Core Objects Created or Updated
12. Permission Requirement
13. Policy Requirement
14. Knowledge Dependency
15. AI Usage
16. Human Review Requirement
17. Workflow Impact
18. Events Emitted
19. Events Consumed
20. Audit Requirement
21. Error and Failure Behavior
22. Idempotency Rule
23. Data Exposure Rule
24. MVP Phase
25. MVP Depth
26. Deferred Scope
27. Prohibited Usage
28. Acceptance Criteria
29. Revision Notes
```

---

# 23. API Anti-Patterns

## 23.1 Route Defines Meaning

A route name or endpoint shape defines Core meaning.

Correction:

```text
Core Object and Service Specifications define meaning.
```

## 23.2 API Bypasses Service

An API writes data without invoking a governed service.

Correction:

```text
Command API must invoke a Core Service.
```

## 23.3 API Has No Event Side Effect

A mutation API changes state without events.

Correction:

```text
Meaningful changes must emit Core Events.
```

## 23.4 API Exposes Internal Fields

An API exposes internal implementation fields without Data Contract.

Correction:

```text
Use Data Contract and field exposure rules.
```

## 23.5 AI API Calls Model Directly

AI API is treated as a generic prompt or model endpoint.

Correction:

```text
AI Invocation API must use Agent Contract and audit.
```

## 23.6 Integration API Creates Vendor Semantics

Vendor-specific status or data shape becomes Core meaning.

Correction:

```text
Vendor mappings stay in adapters; Core meaning remains canonical.
```

## 23.7 Public API Before Governance

External API is exposed before permissions, contracts and audit exist.

Correction:

```text
API Contract precedes public or external exposure.
```

---

# 24. API Governance

API changes require review when they:

```text
create a new API surface
change object exposure
change write authority
change event side effects
change AI invocation behavior
change permission requirements
expose data externally
support future product consumers
expand MVP scope
```

API governance outputs include:

```text
architecture issue
API review decision
updated Appendix F
updated service spec
updated contract spec
updated event spec
updated core-specs/api file
updated Codex task
```

---

# 25. Relationship to Appendix H

Appendix H — Codex Task Index must use Appendix F to generate API-related tasks.

Codex tasks that implement APIs must reference:

```text
Appendix F API entry
owning service spec
input contract
output contract
permission rule
event side effects
test requirements
prohibited overreach
```

Codex must not invent API surfaces not listed or approved through governance.

---

# 26. Relationship to core-specs/

This appendix prepares:

```text
core-specs/api/
core-specs/api/_template.md
core-specs/contracts/api-contracts/
core-specs/services/
core-specs/events/
```

Detailed API specs remain on hold until:

```text
Appendices A–H are complete
indexes/ exists
core-specs templates are approved
Codex Wave 0 scaffold is ready
```

---

# 27. API Index Acceptance Criteria

This appendix is accepted only if:

```text
[ ] It defines API as a contract-bound consumption surface.
[ ] It does not treat API as Core meaning owner.
[ ] It defines API categories.
[ ] It defines API naming rules.
[ ] It defines API index fields.
[ ] It lists MVP API surfaces.
[ ] It lists partial API surfaces.
[ ] It lists future API surfaces.
[ ] It maps APIs to owning domains or cross-cutting systems.
[ ] It includes Capability and Business Responsibility as cross-cutting API surfaces.
[ ] It includes AI Invocation API.
[ ] It includes Core Consumption API.
[ ] It defines permission, event, AI, workflow and integration rules.
[ ] It defines future core-specs/api template expectations.
[ ] It defines API anti-patterns.
[ ] It supports Appendix H Codex task generation.
```

---

# 28. Revision Notes

| Version | Status | Notes |
|---------|--------|-------|
| 0.2.0 | Draft | Initial Appendix F generated for the second canonical draft. Defines API as contract-bound consumption surface, lists MVP/partial/future API surfaces, maps API entries to domains and cross-cutting systems, and prepares `core-specs/api/`. |

---

**End of Appendix**
