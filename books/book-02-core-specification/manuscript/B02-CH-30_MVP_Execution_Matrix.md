# Book 02

# 30 — MVP Execution Matrix

**Book Title:** MarkOrbit Core Specification  
**Chapter ID:** B02-CH-30  
**Chapter Title:** MVP Execution Matrix  
**Part:** Part IV — Core Execution Boundary  
**Chapter Type:** Execution  
**Rewrite Stage:** Second Canonical Draft  
**Status:** Draft  
**Version:** 0.2.0  
**Owner:** MarkOrbit Publications Editorial Board  

**Related Documents:**

- B02-CH-03 — Core Position
- B02-CH-04 — Core Boundary
- B02-CH-05 — Core Principles
- B02-CH-13 — Core Domain Architecture
- B02-CH-22 — Domain Specification
- B02-CH-23 — Object Specification
- B02-CH-24 — Service Specification
- B02-CH-25 — Event Specification
- B02-CH-26 — AI Capability and Agent Governance Specification
- B02-CH-27 — Core Consumption Specification
- B02-CH-28 — Core MVP Boundary
- B02-CH-29 — MVP Domain Priority
- B02-CH-31 — Codex Implementation Roadmap
- B02-REV-R1 — Round 1 Manuscript Architecture Review
- B02-REV-R2 — Round 2 Packaged Manuscript Review
- B02-REV-R3 — Round 3 Pre-Appendix Gate Review
- B02-REV-R4 — Round 4 Appendix Blueprint and Canonical Index Gate Review
- B02-REWRITE-0001 — Book 02 Rewrite Plan and Document List

---

# 1. Chapter Purpose

This chapter defines the MVP Execution Matrix for the MarkOrbit Core.

Chapter 28 defined the Core MVP boundary.

Chapter 29 defined MVP domain priority.

This chapter converts that priority into an execution matrix that can guide appendices, `core-specs/`, indexes and Codex tasks.

The MVP Execution Matrix is not a project management table only.

It is an architecture control device.

It prevents implementation from starting with attractive product features instead of Core dependencies.

It prevents Codex from inventing specs.

It prevents future products from expanding MVP scope.

It ensures that each Core Domain or cross-cutting system is connected to:

```text
MVP depth
required specs
objects
services
events
contracts
AI usage
workflow usage
product consumers
Codex tasks
acceptance criteria
```

The matrix is the bridge between Book 02 manuscript and implementable work.

---

# 2. Core Question

This chapter answers one question:

> How should the MarkOrbit Core MVP be converted into executable specification and implementation work without losing architectural control?

The answer is:

> Each Core Domain and approved cross-cutting system must be mapped to MVP depth, required specifications, objects, services, events, contracts, AI usage, workflow usage, consumers, Codex task packages and acceptance criteria before implementation begins.

---

# 3. Matrix Definition

The MVP Execution Matrix is the canonical planning structure that translates Core architecture into executable work.

It is not a replacement for `core-specs/`.

It is not a replacement for Codex tasks.

It is the control layer that tells `core-specs/` and Codex what must be generated, in what order and within what scope.

The matrix follows this structure:

```text
Core Domain or Cross-Cutting System
        ↓
MVP Depth
        ↓
Required Specs
        ↓
Objects
        ↓
Services
        ↓
Events
        ↓
Contracts
        ↓
AI Usage
        ↓
Workflow Usage
        ↓
Product Consumers
        ↓
Codex Tasks
        ↓
Acceptance Criteria
```

This structure must be preserved in Appendix H and future Codex task files.

---

# 4. Matrix Scope

The matrix covers:

```text
26 baseline Core Domains
2 cross-cutting Core specification systems
```

The 26 baseline Core Domains remain canonical.

The two cross-cutting systems are:

```text
Capability
Business Responsibility
```

They are included in the execution matrix because they produce executable artifacts.

They are not counted as additional baseline Core Domains.

Therefore, the matrix contains:

```text
26 baseline domain rows
+ 2 cross-cutting system rows
= 28 execution rows
```

This distinction must be preserved in Appendix B and Appendix H.

---

# 5. MVP Depth Types

The matrix uses four MVP depth types.

```text
Must Implement
Partial Implement
Reserved Boundary
Deferred
```

## 5.1 Must Implement

The domain or system must have enough executable specification and implementation to support the first Core MVP consumers.

Must Implement rows require:

```text
Domain spec
Object specs
Service specs
Event specs
Contract specs
Tests
Codex tasks
Acceptance criteria
```

## 5.2 Partial Implement

The domain or system must be specified and partially implemented, but not fully built.

Partial Implement rows require:

```text
Scope definition
minimum object/service/event baseline
clear deferred scope
consumer limits
acceptance criteria
```

## 5.3 Reserved Boundary

The domain or system must be named and reserved, but not deeply implemented.

Reserved Boundary rows require:

```text
boundary statement
future ownership
prohibited MVP overbuild
placeholder spec or appendix reference
```

## 5.4 Deferred

The domain feature or product capability must not be implemented in MVP.

Deferred items require:

```text
deferral reason
future trigger
prohibited implementation note
```

---

# 6. MVP Consumer Baseline

The MVP Execution Matrix is driven by consumer readiness.

## 6.1 MVP Consumers

```text
MarkReg
MarkOrbit Lite
Workplace
AI Agents
Codex Implementation
```

These consumers define what the first executable Core must support.

## 6.2 Partial Consumers

```text
MGSN
Opportunity Engine baseline
Brand Asset Vault baseline
```

These consumers require limited support or reserved boundaries.

## 6.3 Future Consumers

```text
Partner Center
Client Portal
Service Platform
External Integrations
Reporting Consumers
```

These consumers do not define MVP implementation scope.

---

# 7. Matrix Row Template

Each matrix row should follow this template.

```text
1. Row ID
2. Domain or System Name
3. Type
       Baseline Domain
       Cross-Cutting System
4. Domain Category
5. MVP Phase
6. MVP Depth
7. Primary Purpose
8. Required Specs
9. MVP Objects
10. MVP Services
11. MVP Events
12. Required Contracts
13. AI Usage
14. Workflow Usage
15. Product Consumers
16. Codex Package
17. Dependencies
18. Deferred Scope
19. Acceptance Criteria
20. Notes
```

This template should later be mirrored in:

```text
Appendix H — Codex Task Index
indexes/mvp-execution-matrix.md
codex-tasks/*
```

---

# 8. MVP Execution Matrix Summary

The following summary table is the canonical second-draft MVP execution baseline.

| Row | Domain / System | Type | Category | MVP Phase | MVP Depth | Main Consumers |
|---:|-----------------|------|----------|-----------|-----------|----------------|
| 01 | Identity | Domain | Foundation | Phase 1 | Must Implement | Workplace, MarkReg, Lite, AI, Codex |
| 02 | Organization | Domain | Foundation | Phase 1 | Must Implement | Workplace, MarkReg, Lite |
| 03 | User | Domain | Foundation | Phase 1 | Must Implement | Workplace, MarkReg, Lite |
| 04 | Permission | Domain | Foundation | Phase 1 | Must Implement | All MVP consumers |
| 05 | Policy | Domain | Foundation | Phase 1 | Partial Implement | AI, Workflow, Workplace |
| 06 | Knowledge | Domain | Foundation | Phase 1 | Must Implement | Lite, AI, MarkReg, Workplace |
| 07 | Capability | Cross-Cutting System | Cross-Cutting | Phase 1 | Partial Implement | AI, Routing, Service Provider, Workplace |
| 08 | Brand | Domain | Professional | Phase 2 | Must Implement | Lite, MarkReg |
| 09 | Trademark | Domain | Professional | Phase 2 | Must Implement | Lite, MarkReg, Workplace, AI |
| 10 | Jurisdiction | Domain | Professional | Phase 2 | Must Implement | Lite, MarkReg, AI |
| 11 | Classification | Domain | Professional | Phase 2 | Must Implement | Lite, MarkReg, AI |
| 12 | Document | Domain | Professional | Phase 2 | Must Implement | MarkReg, Lite, Workplace, AI |
| 13 | Evidence | Domain | Professional | Phase 2 | Partial Implement | MarkReg, AI, Workplace |
| 14 | Customer | Domain | Business Execution | Phase 3 | Must Implement | MarkReg, Lite, Workplace |
| 15 | Order | Domain | Business Execution | Phase 3 | Must Implement | Lite, MarkReg, Workplace |
| 16 | Matter | Domain | Business Execution | Phase 3 | Must Implement | MarkReg, Workplace |
| 17 | Workflow Contract | Domain | Business Execution | Phase 3 | Must Implement | Workplace, MarkReg, AI, Codex |
| 18 | Task | Domain | Business Execution | Phase 3 | Must Implement | Workplace, MarkReg |
| 19 | Event | Domain | Business Execution | Phase 3 | Must Implement | All MVP consumers |
| 20 | Business Responsibility | Cross-Cutting System | Cross-Cutting | Phase 3 | Partial Implement | Workplace, MarkReg, AI |
| 21 | Notification | Domain | Business Execution | Phase 3 | Partial Implement | Workplace, MarkReg, Lite |
| 22 | Communication | Domain | Collaboration Network | Phase 4 | Partial Implement | MarkReg, Workplace, AI |
| 23 | Agent | Domain | Collaboration Network | Phase 4 | Partial Implement | MarkReg, MGSN baseline |
| 24 | Service Provider | Domain | Collaboration Network | Phase 4 | Partial Implement | MarkReg, MGSN baseline |
| 25 | Routing | Domain | Collaboration Network | Phase 4 | Partial Implement | MarkReg, AI, MGSN baseline |
| 26 | Opportunity | Domain | Business Execution | Phase 4 | Partial Implement | Lite, MarkReg, Opportunity baseline |
| 27 | Partner | Domain | Collaboration Network | Phase 5 | Reserved Boundary | MGSN future |
| 28 | Service Network | Domain | Collaboration Network | Phase 5 | Reserved Boundary | MGSN future |

---

# 9. Phase 1 — Foundation Core Matrix

Phase 1 establishes identity, authority and knowledge.

No professional workflow should be implemented before Phase 1 is stable.

## 9.1 Identity

```text
MVP Depth: Must Implement
Required Specs: Domain, Object, Service, Event, Contract
Objects: Identity, Actor Identity, System Actor Identity, AI Agent Identity baseline
Services: Identity Create, Identity Resolve, Identity Link
Events: IdentityCreated, IdentityLinked
Contracts: Identity Data Contract, Identity API Contract
AI Usage: AI Agent identity binding
Workflow Usage: actor resolution
Consumers: Workplace, MarkReg, Lite, AI, Codex
Codex Package: Foundation Core
Acceptance: every actor can be identified and audited
```

## 9.2 Organization

```text
MVP Depth: Must Implement
Objects: Organization, Organization Membership
Services: Organization Create, Organization Link, Organization Resolve
Events: OrganizationCreated, OrganizationLinked
Contracts: Organization Data Contract
AI Usage: organization context only
Workflow Usage: ownership context
Consumers: Workplace, MarkReg, Lite
Codex Package: Foundation Core
Acceptance: users, customers and agents can be linked to organizations
```

## 9.3 User

```text
MVP Depth: Must Implement
Objects: User, User Profile, User Role Assignment
Services: User Create, User Activate, User Role Assign
Events: UserCreated, UserActivated, UserRoleAssigned
Contracts: User Data Contract, User Permission Contract
AI Usage: user review responsibility context
Workflow Usage: assignment and review
Consumers: Workplace, MarkReg, Lite
Codex Package: Foundation Core
Acceptance: human actors can perform governed actions
```

## 9.4 Permission

```text
MVP Depth: Must Implement
Objects: Permission Rule, Permission Grant
Services: Permission Check, Permission Grant, Permission Revoke
Events: PermissionGranted, PermissionRevoked
Contracts: Permission Contract
AI Usage: AI access must pass permission check
Workflow Usage: action authorization
Consumers: all MVP consumers
Codex Package: Foundation Core
Acceptance: read/write/invoke/export boundaries can be enforced
```

## 9.5 Policy

```text
MVP Depth: Partial Implement
Objects: Policy Rule, Policy Decision baseline
Services: Policy Evaluate baseline
Events: PolicyRuleCreated, PolicyDecisionRecorded baseline
Contracts: Policy Contract baseline
AI Usage: risk and review rules
Workflow Usage: review requirement logic
Consumers: Workplace, AI, MarkReg
Codex Package: Foundation Core
Acceptance: policy is available for MVP risk/review decisions without full policy engine
```

## 9.6 Knowledge

```text
MVP Depth: Must Implement
Objects: Knowledge Source, Knowledge Asset, Knowledge Rule, Knowledge Gap
Services: Knowledge Retrieve, Knowledge Validate, Knowledge Link
Events: KnowledgeSourceAdded, KnowledgeAssetValidated, KnowledgeGapRecorded
Contracts: Knowledge Data Contract, AI Knowledge Authorization Contract
AI Usage: authorized knowledge retrieval
Workflow Usage: professional context support
Consumers: Lite, AI, MarkReg, Workplace
Codex Package: Foundation Core
Acceptance: AI and users can consume governed knowledge sources
```

## 9.7 Capability

```text
Type: Cross-Cutting System
MVP Depth: Partial Implement
Objects: Capability, Capability Provider, Capability Scope
Services: Capability Register, Capability Match baseline
Events: CapabilityRegistered, CapabilityMatched baseline
Contracts: Capability Contract
AI Usage: agent/tool capability boundary
Workflow Usage: routing and assignment support
Consumers: AI, Routing, Service Provider, Workplace
Codex Package: Foundation Core / Growth Baseline
Acceptance: capability can be referenced without becoming a baseline domain
```

---

# 10. Phase 2 — Professional Core Matrix

Phase 2 establishes the professional objects needed for international trademark services.

## 10.1 Brand

```text
MVP Depth: Must Implement
Objects: Brand, Brand Owner Link, Brand Asset baseline
Services: Brand Create, Brand Link Trademark
Events: BrandCreated, BrandLinkedToTrademark
Contracts: Brand Data Contract
AI Usage: brand context support
Workflow Usage: intake and matter context
Consumers: Lite, MarkReg
Codex Package: Professional Core
Acceptance: trademark work can be linked to brand context
```

## 10.2 Trademark

```text
MVP Depth: Must Implement
Objects: Trademark, Trademark Status, Trademark Owner Link
Services: Trademark Create, Trademark Update, Trademark Status Normalize
Events: TrademarkCreated, TrademarkStatusChanged, TrademarkOwnerLinked
Contracts: Trademark Data Contract, Trademark API Contract
AI Usage: status summary and professional context
Workflow Usage: matter and task context
Consumers: Lite, MarkReg, Workplace, AI
Codex Package: Professional Core
Acceptance: trademark records can support intake, matter and status workflows
```

## 10.3 Jurisdiction

```text
MVP Depth: Must Implement
Objects: Jurisdiction, Trademark Office, Jurisdiction Requirement
Services: Jurisdiction Resolve, Requirement Retrieve
Events: JurisdictionCreated, JurisdictionRequirementUpdated
Contracts: Jurisdiction Requirement Contract
AI Usage: jurisdiction-aware recommendations
Workflow Usage: country/office-specific work routing
Consumers: Lite, MarkReg, AI
Codex Package: Professional Core
Acceptance: trademark work can be tied to country/office-specific requirements
```

## 10.4 Classification

```text
MVP Depth: Must Implement
Objects: Nice Class, Goods/Services Term, Classification Recommendation
Services: Classification Recommend, Classification Validate
Events: ClassificationRecommended, ClassificationValidated, ClassificationReviewRequired
Contracts: Classification Recommendation API Contract
AI Usage: AI-assisted classification under review
Workflow Usage: intake and filing scope preparation
Consumers: Lite, MarkReg, AI
Codex Package: Professional Core
Acceptance: AI-assisted classification can produce reviewable recommendations
```

## 10.5 Document

```text
MVP Depth: Must Implement
Objects: Document, Document Requirement, Document Template, Generated Document
Services: Document Upload, Document Generate, Document Validate, Document Link
Events: DocumentUploaded, DocumentGenerated, DocumentValidated, DocumentLinked
Contracts: Document Data Contract, Document Generation Contract
AI Usage: document draft assistance under review
Workflow Usage: document preparation and review
Consumers: MarkReg, Lite, Workplace, AI
Codex Package: Professional Core
Acceptance: documents can be uploaded, generated, linked and reviewed
```

## 10.6 Evidence

```text
MVP Depth: Partial Implement
Objects: Evidence Item, Evidence Package baseline
Services: Evidence Add, Evidence Link, Evidence Review baseline
Events: EvidenceAdded, EvidenceReviewRequired baseline
Contracts: Evidence Data Contract baseline
AI Usage: evidence review assistance under human review
Workflow Usage: high-risk matter support
Consumers: MarkReg, Workplace, AI
Codex Package: Professional Core
Acceptance: evidence can be recorded and linked without full evidence automation
```

---

# 11. Phase 3 — Business Execution Core Matrix

Phase 3 makes professional work executable.

## 11.1 Customer

```text
MVP Depth: Must Implement
Objects: Customer, Customer Contact, Customer Organization Link
Services: Customer Create, Customer Link Brand, Customer Link Order
Events: CustomerCreated, CustomerLinkedToOrder
Contracts: Customer Data Contract
AI Usage: customer context only
Workflow Usage: order and matter ownership
Consumers: MarkReg, Lite, Workplace
Codex Package: Business Execution Core
Acceptance: service requests can be tied to a customer
```

## 11.2 Order

```text
MVP Depth: Must Implement
Objects: Order, Order Item, Service Request
Services: Order Create, Order Confirm, Order Convert To Matter
Events: OrderCreated, OrderConfirmed, OrderConvertedToMatter
Contracts: Order Data Contract, Order-to-Matter Contract
AI Usage: intake assistance and requirement suggestion
Workflow Usage: intake-to-execution handoff
Consumers: Lite, MarkReg, Workplace
Codex Package: Business Execution Core
Acceptance: confirmed orders can become executable matters
```

## 11.3 Matter

```text
MVP Depth: Must Implement
Objects: Matter, Matter Status, Matter Context
Services: Matter Create, Matter Update, Matter Close baseline
Events: MatterCreated, MatterStatusChanged, MatterClosed baseline
Contracts: Matter Data Contract, Matter Workflow Contract
AI Usage: status summary and task assistance
Workflow Usage: central execution object
Consumers: MarkReg, Workplace
Codex Package: Business Execution Core
Acceptance: professional work can be managed as matters
```

## 11.4 Workflow Contract

```text
MVP Depth: Must Implement
Objects: Workflow Contract, Workflow State, Workflow Transition
Services: Workflow Validate Transition, Workflow Apply Transition
Events: WorkflowTransitionApplied, ReviewRequired
Contracts: Workflow Contract
AI Usage: workflow assistance under contract
Workflow Usage: governs states and transitions
Consumers: Workplace, MarkReg, AI, Codex
Codex Package: Business Execution Core
Acceptance: workflow states are governed outside UI
```

## 11.5 Task

```text
MVP Depth: Must Implement
Objects: Task, Task Assignment, Task Status
Services: Task Create, Task Assign, Task Complete
Events: TaskCreated, TaskAssigned, TaskCompleted
Contracts: Task Data Contract, Task Service Contract
AI Usage: task suggestion only where governed
Workflow Usage: work execution unit
Consumers: Workplace, MarkReg
Codex Package: Business Execution Core
Acceptance: work can be assigned, tracked and completed
```

## 11.6 Event

```text
MVP Depth: Must Implement
Objects: Event Record, Event Payload, Event Subscription
Services: Event Publish, Event Subscribe, Event Replay baseline
Events: EventPublished, EventSubscriptionCreated
Contracts: Event Contract
AI Usage: AI events must be recorded
Workflow Usage: coordination and downstream reaction
Consumers: all MVP consumers
Codex Package: Business Execution Core
Acceptance: meaningful changes are captured as governed events
```

## 11.7 Business Responsibility

```text
Type: Cross-Cutting System
MVP Depth: Partial Implement
Objects: Responsibility Assignment, Review Record, Approval Record
Services: Responsibility Assign, Review Request, Review Approve, Review Reject
Events: ResponsibilityAssigned, ReviewRequired, ReviewApproved, ReviewRejected
Contracts: Responsibility Contract, Review Contract
AI Usage: AI output approval and review
Workflow Usage: ownership, review and escalation
Consumers: Workplace, MarkReg, AI
Codex Package: Business Execution Core
Acceptance: work and AI output can be tied to accountable actors
```

## 11.8 Notification

```text
MVP Depth: Partial Implement
Objects: Notification, Notification Preference baseline
Services: Notification Create, Notification Dispatch baseline
Events: NotificationCreated, NotificationSent baseline
Contracts: Notification Contract baseline
AI Usage: notify review-required outputs
Workflow Usage: task and review alerting
Consumers: Workplace, MarkReg, Lite
Codex Package: Business Execution Core
Acceptance: essential task/review notifications can be produced
```

---

# 12. Phase 4 — Growth Core Baseline Matrix

Phase 4 introduces limited collaboration, routing, communication and opportunity support.

These rows must remain carefully scoped.

## 12.1 Communication

```text
MVP Depth: Partial Implement
Objects: Communication Record, Communication Link, Communication Summary baseline
Services: Communication Link, Communication Summarize baseline
Events: CommunicationLinked, CommunicationSummaryGenerated baseline
Contracts: Communication Data Contract
AI Usage: communication summary under review where needed
Workflow Usage: matter and agent communication context
Consumers: MarkReg, Workplace, AI
Codex Package: Growth Core Baseline
Acceptance: communications can be linked to matters without full messaging platform
```

## 12.2 Agent

```text
MVP Depth: Partial Implement
Objects: Agent, Agent Jurisdiction Coverage, Agent Contact baseline
Services: Agent Register, Agent Search baseline, Agent Link Matter baseline
Events: AgentRegistered, AgentLinkedToMatter baseline
Contracts: Agent Data Contract
AI Usage: routing and communication context only
Workflow Usage: external work assignment context
Consumers: MarkReg, MGSN baseline
Codex Package: Growth Core Baseline
Acceptance: agent records can support basic matter routing/contact context
```

## 12.3 Service Provider

```text
MVP Depth: Partial Implement
Objects: Service Provider, Provider Capability baseline
Services: Provider Register, Provider Capability Link baseline
Events: ServiceProviderRegistered, ProviderCapabilityLinked baseline
Contracts: Service Provider Contract baseline
AI Usage: provider matching future/reserved
Workflow Usage: service sourcing context
Consumers: MarkReg, MGSN baseline
Codex Package: Growth Core Baseline
Acceptance: service provider identity/capability baseline exists without marketplace overbuild
```

## 12.4 Routing

```text
MVP Depth: Partial Implement
Objects: Routing Decision, Routing Candidate, Routing Reason
Services: Routing Recommend baseline, Routing Review baseline
Events: RoutingDecisionMade, RoutingReviewRequired baseline
Contracts: Routing Contract
AI Usage: routing recommendation under review
Workflow Usage: agent/provider selection context
Consumers: MarkReg, AI, MGSN baseline
Codex Package: Growth Core Baseline
Acceptance: routing recommendations can be recorded and reviewed without full scoring engine
```

## 12.5 Opportunity

```text
MVP Depth: Partial Implement
Objects: Opportunity, Opportunity Signal, Opportunity Follow-up baseline
Services: Opportunity Create, Opportunity Link Customer, Opportunity Suggest baseline
Events: OpportunityCreated, OpportunityFollowupRequired baseline
Contracts: Opportunity Data Contract baseline
AI Usage: opportunity discovery under review
Workflow Usage: follow-up task creation
Consumers: Lite, MarkReg, Opportunity baseline
Codex Package: Growth Core Baseline
Acceptance: opportunity signals can be recorded without full opportunity engine
```

---

# 13. Phase 5 — Reserved Network Boundary Matrix

Phase 5 reserves future network structure.

It should not be deeply implemented in Core MVP.

## 13.1 Partner

```text
MVP Depth: Reserved Boundary
Objects: Partner placeholder / future
Services: none in MVP except possible reference baseline
Events: none required for MVP
Contracts: Partner Boundary Note
AI Usage: none in MVP
Workflow Usage: none in MVP
Consumers: MGSN future
Codex Package: Reserved / no implementation task unless explicitly approved
Acceptance: partner concept is reserved without marketplace implementation
```

## 13.2 Service Network

```text
MVP Depth: Reserved Boundary
Objects: Service Network placeholder / future
Services: none in MVP
Events: none in MVP
Contracts: Service Network Boundary Note
AI Usage: none in MVP
Workflow Usage: none in MVP
Consumers: MGSN future
Codex Package: Reserved / no implementation task unless explicitly approved
Acceptance: network architecture is reserved without full MGSN operation
```

---

# 14. Required Specification Outputs

The MVP Execution Matrix requires the following specification outputs.

## 14.1 Appendix Outputs

```text
Appendix A — Glossary
Appendix B — Core Domain Index
Appendix C — Core Object Index
Appendix D — Core Service Index
Appendix E — Event Index
Appendix F — API Index
Appendix G — Agent Index
Appendix H — Codex Task Index
```

Appendices must be generated before detailed `core-specs/` files.

## 14.2 Index Outputs

```text
indexes/domain-index.md
indexes/object-index.md
indexes/service-index.md
indexes/event-index.md
indexes/api-index.md
indexes/agent-index.md
indexes/consumer-index.md
indexes/mvp-execution-matrix.md
indexes/codex-task-index.md
```

Indexes should be generated from appendices.

## 14.3 core-specs Outputs

```text
core-specs/domains/
core-specs/objects/
core-specs/services/
core-specs/events/
core-specs/contracts/
core-specs/api/
core-specs/agents/
core-specs/workflows/
```

Detailed `core-specs/` must not be generated before appendices and indexes are ready.

## 14.4 Codex Outputs

```text
codex-tasks/wave-0/
codex-tasks/wave-1/
codex-tasks/wave-2/
codex-tasks/wave-3/
codex-tasks/wave-4/
codex-tasks/wave-5/
codex-tasks/wave-6/
codex-tasks/wave-7/
```

Codex tasks must map to matrix rows.

---

# 15. Codex Task Package Mapping

The matrix maps to Codex task packages.

```text
Package A — Repository Scaffold
Package B — Foundation Core
Package C — Professional Core
Package D — Business Execution Core
Package E — AI Governance and Review
Package F — Product Consumption Baseline
Package G — Growth Core Baseline
Package H — Fixtures and Tests
```

## 15.1 Package A — Repository Scaffold

Covers:

```text
repository folders
README updates
publication.yaml updates
appendices scaffolds
indexes scaffolds
core-specs templates
codex task templates
```

## 15.2 Package B — Foundation Core

Covers:

```text
Identity
Organization
User
Permission
Policy baseline
Knowledge
Capability baseline
```

## 15.3 Package C — Professional Core

Covers:

```text
Brand
Trademark
Jurisdiction
Classification
Document
Evidence baseline
```

## 15.4 Package D — Business Execution Core

Covers:

```text
Customer
Order
Matter
Workflow Contract
Task
Event
Business Responsibility baseline
Notification baseline
```

## 15.5 Package E — AI Governance and Review

Covers:

```text
AI Agent Identity
Agent Contract
AI Output
AI Recommendation
AI Audit Record
ReviewRequired events
human review rules
AI failure behavior
```

## 15.6 Package F — Product Consumption Baseline

Covers:

```text
MarkReg Core Consumption Contract
MarkOrbit Lite Core Consumption Contract
Workplace Core Consumption Contract
AI Agent Consumption Contract
API baseline
```

## 15.7 Package G — Growth Core Baseline

Covers:

```text
Communication
Agent
Service Provider
Routing
Opportunity
Partner reserved boundary
Service Network reserved boundary
```

## 15.8 Package H — Fixtures and Tests

Covers:

```text
fixture objects
fixture events
contract tests
service tests
AI governance tests
permission tests
workflow tests
acceptance tests
```

---

# 16. Matrix-to-Codex Rules

Codex tasks must follow these rules.

## Rule 1 — Source Specs Required

Every Codex task must cite source chapters, appendices, indexes or `core-specs/`.

## Rule 2 — Matrix Row Required

Every Codex task must reference one or more matrix rows.

## Rule 3 — MVP Depth Required

Every task must declare:

```text
Must Implement
Partial Implement
Reserved Boundary
Deferred
```

## Rule 4 — Prohibited Overreach Required

Every task must include explicit out-of-scope items.

## Rule 5 — Tests Required

Every implementation task must define tests.

## Rule 6 — Acceptance Criteria Required

Every task must define acceptance criteria.

## Rule 7 — No AI Without Agent Contract

AI implementation tasks must reference Agent Contracts and audit rules.

## Rule 8 — No Event Without Event Spec

Event implementation tasks must reference Event Specifications.

## Rule 9 — No API Without API Contract

API tasks must reference Appendix F or `core-specs/api/`.

## Rule 10 — No Product Consumption Without Consumption Contract

Product-facing tasks must reference Core Consumption Contracts.

---

# 17. Matrix Acceptance Gates

The MVP Execution Matrix has six gates.

## Gate 1 — Appendix Gate

```text
Appendices A–H exist.
```

## Gate 2 — Index Gate

```text
indexes/ baseline exists and aligns with appendices.
```

## Gate 3 — Template Gate

```text
core-specs/ templates exist for domains, objects, services, events, contracts, API, agents and workflows.
```

## Gate 4 — Matrix Gate

```text
Each row has MVP depth, required specs, dependencies and acceptance criteria.
```

## Gate 5 — Codex Gate

```text
Codex tasks reference matrix rows and source specs.
```

## Gate 6 — Implementation Gate

```text
Implementation passes tests and does not violate MVP boundary.
```

---

# 18. Matrix Anti-Patterns

The following are prohibited.

## 18.1 Feature-First Implementation

Starting from product features instead of matrix rows.

Correction:

```text
Start from Core Domain / System row and MVP depth.
```

## 18.2 Codex Without Source Specs

Codex generates implementation from general conversation or assumptions.

Correction:

```text
Codex task must reference approved source specs.
```

## 18.3 Cross-Cutting Systems Counted as Domains

Capability and Business Responsibility are counted as new baseline domains.

Correction:

```text
Treat them as cross-cutting systems in the matrix.
```

## 18.4 Future Scope Enters MVP

MGSN marketplace, full opportunity scoring or full brand asset vault is implemented early.

Correction:

```text
Use Partial, Reserved Boundary or Deferred classification.
```

## 18.5 AI Without Review and Audit

AI output is implemented without Agent Contract, review or audit.

Correction:

```text
Use Agent Contract, Review Record, AI Audit Record and AI Events.
```

## 18.6 Eventless Workflow

Workflow state changes happen without semantic events.

Correction:

```text
Define Event Specifications before implementation.
```

## 18.7 API Without Contract

API routes are created without input/output contracts and permissions.

Correction:

```text
Use Appendix F and API Contract.
```

---

# 19. Relationship to Appendix H

Appendix H — Codex Task Index must be generated from this matrix.

Appendix H should include:

```text
task ID
wave
package
matrix row
source specs
dependencies
expected outputs
tests required
acceptance criteria
prohibited overreach
status
```

Appendix H must not introduce implementation tasks that are not traceable to the matrix.

---

# 20. Relationship to Chapter 31

Chapter 31 — Codex Implementation Roadmap defines the wave sequence.

This chapter defines what those waves execute.

The relationship is:

```text
Chapter 30 defines the matrix.
Chapter 31 defines the roadmap.
Appendix H defines task index.
Codex task files define implementation instructions.
```

---

# 21. Specification Output

This chapter produces the following specification outputs:

```text
MVP Execution Matrix Definition
28 execution rows
26-domain baseline preservation
2 cross-cutting system clarification
MVP depth model
consumer baseline
phase-based execution sequencing
required specification outputs
Codex package mapping
matrix-to-Codex rules
matrix acceptance gates
matrix anti-patterns
Appendix H requirements
Chapter 31 handoff
```

---

# 22. Execution Mapping

| Matrix Element | Execution Output |
|----------------|------------------|
| Domain/System row | Appendix B/H and `indexes/mvp-execution-matrix.md` |
| MVP depth | Codex task scope and implementation limits |
| Required specs | `core-specs/` file generation plan |
| Objects | Appendix C and `core-specs/objects/` |
| Services | Appendix D and `core-specs/services/` |
| Events | Appendix E and `core-specs/events/` |
| Contracts | `core-specs/contracts/` |
| AI usage | Appendix G and `core-specs/agents/` |
| Workflow usage | `core-specs/workflows/` |
| Consumers | consumption contracts and product boundaries |
| Codex package | `codex-tasks/wave-*` |
| Acceptance criteria | tests and release gates |

---

# 23. Exclusions

This chapter does not define:

```text
complete object field schemas
complete service input/output payloads
complete event payloads
final API endpoint routes
product UI
commercial pricing
full MGSN marketplace
full opportunity scoring
full external integration platform
production deployment
```

Those belong to later appendices, `core-specs/`, product books or implementation documents.

---

# 24. Acceptance Criteria

This rewritten chapter is accepted only if it satisfies the following criteria.

```text
[ ] It defines the MVP Execution Matrix clearly.
[ ] It preserves the 26 baseline Core Domains.
[ ] It explains the 28 execution rows correctly.
[ ] It classifies Capability and Business Responsibility as cross-cutting systems.
[ ] It defines MVP depth types.
[ ] It maps Phase 1–5 execution rows.
[ ] It identifies objects, services, events and contracts at MVP planning level.
[ ] It identifies AI and workflow usage at MVP planning level.
[ ] It maps consumers to MVP / Partial / Future classification.
[ ] It defines Codex package mapping.
[ ] It defines matrix-to-Codex rules.
[ ] It defines acceptance gates.
[ ] It prevents future-scope leakage.
[ ] It prepares Appendix H.
[ ] It hands off cleanly to Chapter 31.
[ ] It supports the second canonical draft rewrite plan.
```

---

# 25. Revision Notes

| Version | Status | Notes |
|---------|--------|-------|
| 0.1.0 | Draft | Initial first-draft version of Chapter 30, defining the MVP Execution Matrix. |
| 0.2.0 | Draft | Second canonical draft rewrite. Clarified the 28 execution rows, preserved 26 baseline domains, added cross-cutting system treatment, Codex package mapping, acceptance gates and Appendix H readiness. |

---

**End of Chapter**
