# Book 02

# Appendix B — Core Domain Index

**Book Title:** MarkOrbit Core Specification  
**Appendix ID:** B02-APP-B  
**Appendix Title:** Core Domain Index  
**Appendix Type:** Canonical Index  
**Rewrite Stage:** Second Canonical Draft  
**Status:** Draft  
**Version:** 0.2.0  
**Owner:** MarkOrbit Publications Editorial Board  

**Related Documents:**

- B02-APP-A — Glossary
- B02-CH-08 — Ontology and Domain Classification
- B02-CH-13 — Core Domain Architecture
- B02-CH-22 — Domain Specification
- B02-CH-28 — Core MVP Boundary
- B02-CH-29 — MVP Domain Priority
- B02-CH-30 — MVP Execution Matrix
- B02-CH-31 — Codex Implementation Roadmap
- B02-REV-R1-FIXPLAN — Round 1 Fix Plan
- B02-REV-R2-FIXPLAN — Round 2 Repository and Appendix Fix Plan
- B02-REV-R4 — Round 4 Appendix Blueprint and Canonical Index Gate Review

---

# 1. Appendix Purpose

This appendix defines the canonical Core Domain Index for Book 02.

It converts the domain architecture described in Chapter 08 and Chapter 13 into an index that can be used by:

```text
manuscript rewrite
Appendix C — Core Object Index
Appendix D — Core Service Index
Appendix E — Event Index
Appendix F — API Index
Appendix G — Agent Index
Appendix H — Codex Task Index
core-specs/domains/
Codex task generation
MVP execution planning
```

The purpose of this appendix is to prevent domain drift.

A domain index must not become a product module list, database schema list or implementation backlog.

It is a canonical architecture index.

---

# 2. Canonical Domain Rule

The canonical baseline Core Domain Map contains **26 domains**.

```text
Foundation Domains: 6
Professional Domains: 6
Business Execution Domains: 8
Collaboration Network Domains: 6
Total: 26
```

This baseline shall not be changed silently.

Any future change to the baseline domain map requires architecture review, version update and appendix revision.

---

# 3. Cross-Cutting System Rule

Capability and Business Responsibility are cross-cutting Core specification systems.

They are not counted as additional baseline Core Domains.

Canonical clarification:

```text
Capability and Business Responsibility are cross-cutting Core specification systems.
They govern multiple domains and may produce executable specs, objects, services, events and contracts.
They are not counted as additional baseline Core Domains unless a later architecture release explicitly changes the domain map.
```

This appendix therefore contains two sections:

```text
Canonical Core Domains
Cross-Cutting Specification Systems
```

The first section contains the 26 baseline domains.

The second section contains Capability and Business Responsibility.

---

# 4. Domain Category Model

Book 02 uses four domain categories.

```text
Foundation Domains
    define identity, authority, policy and knowledge foundations.

Professional Domains
    define brand and trademark professional meaning.

Business Execution Domains
    define how professional work becomes orders, matters, tasks, events and notifications.

Collaboration Network Domains
    define partner, agent, provider, routing and communication foundations.
```

These categories are architecture categories, not product modules.

---

# 5. Index Field Definitions

Each domain entry includes the following fields.

```text
Domain ID
Domain Name
Domain Category
Core Purpose
Canonical Model Alignment
MVP Phase
MVP Depth
Primary Objects
Primary Services
Primary Events
Primary Contracts
AI Usage
Workflow Usage
Product Consumers
Deferred Scope
Notes
```

## 5.1 MVP Phase

MVP Phase indicates implementation sequence.

```text
Phase 1 — Foundation Core
Phase 2 — Professional Core
Phase 3 — Business Execution Core
Phase 4 — Growth Core Baseline
Phase 5 — Network Reserved
```

## 5.2 MVP Depth

MVP Depth indicates implementation depth.

```text
Must Implement
Partial Implement
Reserved Boundary
Deferred
```

## 5.3 Product Consumers

Consumers are classified as:

```text
MVP Consumers
Partial Consumers
Future Consumers
```

---

# 6. Foundation Domains

Foundation Domains define the identity, authority, policy and knowledge base required for all later Core execution.

---

## 6.1 Identity

| Field | Value |
|------|-------|
| Domain ID | DOM-FOUND-001 |
| Domain Name | Identity |
| Domain Category | Foundation |
| Core Purpose | Defines who or what an actor is. |
| Canonical Model Alignment | Identity Model |
| MVP Phase | Phase 1 — Foundation Core |
| MVP Depth | Must Implement |
| Primary Objects | Identity, Actor Identity, AI Agent Identity, External Actor Identity |
| Primary Services | Identity Registration, Identity Resolution, Identity Verification, Identity Linking |
| Primary Events | IdentityCreated, IdentityUpdated, IdentityLinked, IdentityDeactivated |
| Primary Contracts | Identity Data Contract, Identity API Contract, Identity Audit Contract |
| AI Usage | AI agents require AI Agent Identity before execution. |
| Workflow Usage | Identity anchors actor attribution in tasks, reviews and events. |
| Product Consumers | MarkReg, MarkOrbit Lite, Workplace, AI Agents, Codex Implementation |
| Deferred Scope | Advanced identity federation and external SSO federation. |
| Notes | Identity is the root of permission, audit and responsibility. |

---

## 6.2 Organization

| Field | Value |
|------|-------|
| Domain ID | DOM-FOUND-002 |
| Domain Name | Organization |
| Domain Category | Foundation |
| Core Purpose | Defines organizational context and ownership structures. |
| Canonical Model Alignment | Identity Model / Business Responsibility Model |
| MVP Phase | Phase 1 — Foundation Core |
| MVP Depth | Must Implement |
| Primary Objects | Organization, Team, Organization Membership, Organization Role |
| Primary Services | Organization Registration, Membership Assignment, Team Management |
| Primary Events | OrganizationCreated, OrganizationUpdated, MembershipAssigned |
| Primary Contracts | Organization Data Contract, Membership Contract |
| AI Usage | AI access may be scoped by organization. |
| Workflow Usage | Organization context supports ownership and task routing. |
| Product Consumers | MarkReg, MarkOrbit Lite, Workplace, Codex Implementation |
| Deferred Scope | Complex multi-entity hierarchy and inter-organization collaboration logic. |
| Notes | Organization connects users, customers, agents and providers to accountable structures. |

---

## 6.3 User

| Field | Value |
|------|-------|
| Domain ID | DOM-FOUND-003 |
| Domain Name | User |
| Domain Category | Foundation |
| Core Purpose | Defines human actors operating in MarkOrbit. |
| Canonical Model Alignment | Identity Model |
| MVP Phase | Phase 1 — Foundation Core |
| MVP Depth | Must Implement |
| Primary Objects | User, User Profile, User Role, User Membership |
| Primary Services | User Registration, User Assignment, Role Assignment, User Deactivation |
| Primary Events | UserCreated, UserUpdated, RoleAssigned, UserDeactivated |
| Primary Contracts | User Data Contract, User Permission Contract |
| AI Usage | Human users may invoke, review or approve AI output. |
| Workflow Usage | Users are assignees, reviewers, approvers and operators. |
| Product Consumers | MarkReg, MarkOrbit Lite, Workplace, AI Agents, Codex Implementation |
| Deferred Scope | Advanced HR, performance and compensation features. |
| Notes | User is a human actor; AI Agent is governed separately through AI governance. |

---

## 6.4 Permission

| Field | Value |
|------|-------|
| Domain ID | DOM-FOUND-004 |
| Domain Name | Permission |
| Domain Category | Foundation |
| Core Purpose | Governs what actors may read, create, update, approve, export or invoke. |
| Canonical Model Alignment | Identity Model / Policy Model |
| MVP Phase | Phase 1 — Foundation Core |
| MVP Depth | Must Implement |
| Primary Objects | Permission Rule, Role Permission, Access Scope, Permission Grant |
| Primary Services | Permission Check, Permission Grant, Permission Revocation, Access Scope Evaluation |
| Primary Events | PermissionGranted, PermissionRevoked, PermissionDenied |
| Primary Contracts | Permission Contract, Access Control Contract, API Permission Contract |
| AI Usage | AI requires explicit allowed object, service and knowledge access. |
| Workflow Usage | Permission controls task actions, review actions and state changes. |
| Product Consumers | MarkReg, MarkOrbit Lite, Workplace, AI Agents, External Integrations, Codex Implementation |
| Deferred Scope | Advanced attribute-based access control and external delegated authorization. |
| Notes | Permission must precede AI, API and external integration consumption. |

---

## 6.5 Policy

| Field | Value |
|------|-------|
| Domain ID | DOM-FOUND-005 |
| Domain Name | Policy |
| Domain Category | Foundation |
| Core Purpose | Defines rules that influence decisions, constraints, review and governance. |
| Canonical Model Alignment | Policy Model / Business Responsibility Model |
| MVP Phase | Phase 1 — Foundation Core |
| MVP Depth | Partial Implement |
| Primary Objects | Policy Rule, Review Policy, AI Risk Policy, Data Sharing Policy |
| Primary Services | Policy Evaluation, Review Rule Evaluation, AI Risk Rule Evaluation |
| Primary Events | PolicyRuleCreated, PolicyEvaluated, PolicyViolationDetected |
| Primary Contracts | Policy Contract, Review Policy Contract, AI Policy Contract |
| AI Usage | AI risk and review rules depend on Policy. |
| Workflow Usage | Policy may trigger review, approval or escalation. |
| Product Consumers | Workplace, AI Agents, MarkReg, MarkOrbit Lite |
| Deferred Scope | Full policy engine, advanced jurisdictional policy automation and commercial policy automation. |
| Notes | Policy is partial in MVP but must be reserved early. |

---

## 6.6 Knowledge

| Field | Value |
|------|-------|
| Domain ID | DOM-FOUND-006 |
| Domain Name | Knowledge |
| Domain Category | Foundation |
| Core Purpose | Defines governed professional knowledge sources, assets and retrieval rules. |
| Canonical Model Alignment | Knowledge Model |
| MVP Phase | Phase 1 — Foundation Core |
| MVP Depth | Must Implement |
| Primary Objects | Knowledge Source, Knowledge Asset, Knowledge Rule, Knowledge Gap, Knowledge Citation |
| Primary Services | Knowledge Registration, Knowledge Retrieval, Knowledge Validation, Knowledge Gap Detection |
| Primary Events | KnowledgeSourceCreated, KnowledgeAssetUpdated, KnowledgeGapDetected |
| Primary Contracts | Knowledge Data Contract, Knowledge Retrieval Contract, AI Knowledge Authorization Contract |
| AI Usage | AI may consume only authorized knowledge. |
| Workflow Usage | Knowledge supports consultation, classification, document and review workflows. |
| Product Consumers | MarkReg, MarkOrbit Lite, Workplace, AI Agents, Codex Implementation |
| Deferred Scope | Full global law knowledge automation and advanced knowledge reasoning. |
| Notes | Knowledge is not equivalent to unvalidated generated content. |

---

# 7. Professional Domains

Professional Domains define the brand and trademark professional objects that MarkOrbit operates.

---

## 7.1 Brand

| Field | Value |
|------|-------|
| Domain ID | DOM-PRO-001 |
| Domain Name | Brand |
| Domain Category | Professional |
| Core Purpose | Defines the business or market-facing identity that trademark work protects. |
| Canonical Model Alignment | Professional Model |
| MVP Phase | Phase 2 — Professional Core |
| MVP Depth | Must Implement |
| Primary Objects | Brand, Brand Name, Brand Owner Link, Brand Asset Reference |
| Primary Services | Brand Registration, Brand Linking, Brand Context Update |
| Primary Events | BrandCreated, BrandLinkedToCustomer, BrandUpdated |
| Primary Contracts | Brand Data Contract, Brand Consumption Contract |
| AI Usage | AI may summarize brand context or suggest trademark strategy under review. |
| Workflow Usage | Brand provides context for intake and trademark filing work. |
| Product Consumers | MarkReg, MarkOrbit Lite, Workplace, AI Agents |
| Deferred Scope | Full Brand Asset Vault, brand valuation and advanced portfolio analytics. |
| Notes | Brand connects business intention to trademark execution. |

---

## 7.2 Trademark

| Field | Value |
|------|-------|
| Domain ID | DOM-PRO-002 |
| Domain Name | Trademark |
| Domain Category | Professional |
| Core Purpose | Defines mark-related professional meaning and lifecycle. |
| Canonical Model Alignment | Professional Model |
| MVP Phase | Phase 2 — Professional Core |
| MVP Depth | Must Implement |
| Primary Objects | Trademark, Mark, Trademark Status, Trademark Record, Goods/Services Link |
| Primary Services | Trademark Creation, Trademark Status Normalization, Trademark Lifecycle Update |
| Primary Events | TrademarkCreated, TrademarkUpdated, TrademarkStatusChanged |
| Primary Contracts | Trademark Data Contract, Trademark API Contract, Trademark Event Contract |
| AI Usage | AI may summarize status, detect lifecycle issues or assist intake under review. |
| Workflow Usage | Trademark anchors order, matter, document, evidence and status workflows. |
| Product Consumers | MarkReg, MarkOrbit Lite, Workplace, AI Agents, Reporting Consumers |
| Deferred Scope | Full global official-data automation, advanced watch and conflict analysis. |
| Notes | Trademark is a central professional domain and must not be reduced to a filing record. |

---

## 7.3 Jurisdiction

| Field | Value |
|------|-------|
| Domain ID | DOM-PRO-003 |
| Domain Name | Jurisdiction |
| Domain Category | Professional |
| Core Purpose | Defines country, region or office-specific professional context. |
| Canonical Model Alignment | Professional Model / Knowledge Model |
| MVP Phase | Phase 2 — Professional Core |
| MVP Depth | Must Implement |
| Primary Objects | Jurisdiction, Trademark Office, Jurisdiction Requirement, Local Rule |
| Primary Services | Jurisdiction Lookup, Requirement Retrieval, Jurisdiction Rule Validation |
| Primary Events | JurisdictionCreated, RequirementUpdated, JurisdictionRuleChanged |
| Primary Contracts | Jurisdiction Data Contract, Requirement Retrieval Contract |
| AI Usage | AI may recommend jurisdictions or summarize requirements with citations and review. |
| Workflow Usage | Jurisdiction drives document, classification, filing and agent routing context. |
| Product Consumers | MarkReg, MarkOrbit Lite, AI Agents, Workplace |
| Deferred Scope | Full worldwide office-data automation and automatic rule change monitoring. |
| Notes | Jurisdiction prevents global trademark work from becoming one-size-fits-all. |

---

## 7.4 Classification

| Field | Value |
|------|-------|
| Domain ID | DOM-PRO-004 |
| Domain Name | Classification |
| Domain Category | Professional |
| Core Purpose | Defines goods/services classification meaning and constraints. |
| Canonical Model Alignment | Professional Model / Knowledge Model |
| MVP Phase | Phase 2 — Professional Core |
| MVP Depth | Must Implement |
| Primary Objects | Classification Term, Nice Class, Goods/Services Item, Classification Recommendation |
| Primary Services | Classification Recommendation, Term Validation, Class Mapping, Goods/Services Normalization |
| Primary Events | ClassificationSuggested, ClassificationValidated, ClassificationReviewRequired |
| Primary Contracts | Classification API Contract, Classification Recommendation Contract, Review Contract |
| AI Usage | AI may suggest classes and goods/services, but review is required where risk applies. |
| Workflow Usage | Classification supports intake, filing, review and document workflows. |
| Product Consumers | MarkReg, MarkOrbit Lite, AI Agents, Workplace |
| Deferred Scope | Full local subclass automation, similarity risk scoring and global class strategy automation. |
| Notes | Classification is high-impact and must remain professionally governed. |

---

## 7.5 Document

| Field | Value |
|------|-------|
| Domain ID | DOM-PRO-005 |
| Domain Name | Document |
| Domain Category | Professional |
| Core Purpose | Defines professional files, generated materials and official documents. |
| Canonical Model Alignment | Professional Model / Execution Model |
| MVP Phase | Phase 2 — Professional Core |
| MVP Depth | Must Implement |
| Primary Objects | Document, Document Requirement, Document Template, Generated Document, Official Document |
| Primary Services | Document Upload, Document Generation, Document Validation, Document Linking |
| Primary Events | DocumentUploaded, DocumentGenerated, DocumentValidated, DocumentLinked |
| Primary Contracts | Document Data Contract, Document Generation Contract, Document Access Contract |
| AI Usage | AI may draft or summarize documents under Agent Contract and review. |
| Workflow Usage | Document supports intake, filing, evidence, office action and communication workflows. |
| Product Consumers | MarkReg, MarkOrbit Lite, Workplace, AI Agents |
| Deferred Scope | Full document automation, e-sign integration and advanced template orchestration. |
| Notes | Document is a professional artifact, not only a file. |

---

## 7.6 Evidence

| Field | Value |
|------|-------|
| Domain ID | DOM-PRO-006 |
| Domain Name | Evidence |
| Domain Category | Professional |
| Core Purpose | Defines proof materials and evidence packages. |
| Canonical Model Alignment | Professional Model / Knowledge Model |
| MVP Phase | Phase 2 — Professional Core |
| MVP Depth | Partial Implement |
| Primary Objects | Evidence Item, Evidence Package, Evidence Source, Evidence Review Record |
| Primary Services | Evidence Upload, Evidence Packaging, Evidence Review, Evidence Gap Detection |
| Primary Events | EvidenceUploaded, EvidencePackageCreated, EvidenceReviewRequired |
| Primary Contracts | Evidence Data Contract, Evidence Review Contract, AI Evidence Contract |
| AI Usage | AI may assist evidence review or gap detection, but high-risk review is required. |
| Workflow Usage | Evidence supports office action, opposition, cancellation, use declaration and dispute workflows. |
| Product Consumers | MarkReg, Workplace, AI Agents |
| Deferred Scope | Advanced evidence scoring, automatic marketplace evidence collection and legal sufficiency automation. |
| Notes | Evidence is partial in MVP because professional risk is high. |

---

# 8. Business Execution Domains

Business Execution Domains turn professional objects into managed work.

---

## 8.1 Customer

| Field | Value |
|------|-------|
| Domain ID | DOM-BIZ-001 |
| Domain Name | Customer |
| Domain Category | Business Execution |
| Core Purpose | Defines the person or organization receiving service. |
| Canonical Model Alignment | Business Execution Model / Identity Model |
| MVP Phase | Phase 3 — Business Execution Core |
| MVP Depth | Must Implement |
| Primary Objects | Customer, Customer Contact, Customer Organization Link, Customer Portfolio Link |
| Primary Services | Customer Creation, Customer Update, Customer Linking, Customer Lookup |
| Primary Events | CustomerCreated, CustomerUpdated, CustomerLinkedToBrand |
| Primary Contracts | Customer Data Contract, Customer API Contract, Customer Consumption Contract |
| AI Usage | AI may summarize customer context under permission and audit rules. |
| Workflow Usage | Customer anchors order, matter and communication workflows. |
| Product Consumers | MarkReg, MarkOrbit Lite, Workplace, AI Agents |
| Deferred Scope | Full CRM automation, scoring and marketing automation. |
| Notes | Customer is not merely a CRM lead; it is a Core business execution actor. |

---

## 8.2 Matter

| Field | Value |
|------|-------|
| Domain ID | DOM-BIZ-002 |
| Domain Name | Matter |
| Domain Category | Business Execution |
| Core Purpose | Defines a managed professional service case. |
| Canonical Model Alignment | Business Execution Model / Workplace Model |
| MVP Phase | Phase 3 — Business Execution Core |
| MVP Depth | Must Implement |
| Primary Objects | Matter, Matter Status, Matter Participant, Matter Timeline, Matter Context |
| Primary Services | Matter Creation, Matter Update, Matter Status Change, Matter Assignment |
| Primary Events | MatterCreated, MatterStatusChanged, MatterAssigned, MatterClosed |
| Primary Contracts | Matter Data Contract, Matter Workflow Contract, Matter Event Contract |
| AI Usage | AI may summarize matter status or suggest next action under review. |
| Workflow Usage | Matter anchors task, document, event, review and communication workflows. |
| Product Consumers | MarkReg, Workplace, AI Agents, Reporting Consumers |
| Deferred Scope | Advanced matter analytics, automatic risk prediction and complex litigation-style matter management. |
| Notes | Matter is central to Workplace and MarkReg execution. |

---

## 8.3 Order

| Field | Value |
|------|-------|
| Domain ID | DOM-BIZ-003 |
| Domain Name | Order |
| Domain Category | Business Execution |
| Core Purpose | Defines a service request or confirmed service commitment. |
| Canonical Model Alignment | Business Execution Model |
| MVP Phase | Phase 3 — Business Execution Core |
| MVP Depth | Must Implement |
| Primary Objects | Order, Order Item, Order Requirement, Order Status, Order-to-Matter Link |
| Primary Services | Order Creation, Order Confirmation, Order Validation, Order-to-Matter Conversion |
| Primary Events | OrderCreated, OrderConfirmed, OrderConvertedToMatter, OrderCancelled |
| Primary Contracts | Order Data Contract, Order API Contract, Order Conversion Contract |
| AI Usage | AI may assist intake, requirement summary or order validation under review. |
| Workflow Usage | Order starts business execution and converts to Matter when ready. |
| Product Consumers | MarkReg, MarkOrbit Lite, Workplace, AI Agents |
| Deferred Scope | Full payment, invoicing, pricing engine and commercial package automation. |
| Notes | Order connects intake and business commitment to execution. |

---

## 8.4 Opportunity

| Field | Value |
|------|-------|
| Domain ID | DOM-BIZ-004 |
| Domain Name | Opportunity |
| Domain Category | Business Execution |
| Core Purpose | Defines potential business value or follow-up opportunity. |
| Canonical Model Alignment | Business Execution Model / Knowledge Model |
| MVP Phase | Phase 4 — Growth Core Baseline |
| MVP Depth | Partial Implement |
| Primary Objects | Opportunity, Opportunity Signal, Opportunity Source, Opportunity Recommendation |
| Primary Services | Opportunity Detection, Opportunity Creation, Opportunity Review, Opportunity Assignment |
| Primary Events | OpportunityCreated, OpportunityReviewRequired, OpportunityAssigned |
| Primary Contracts | Opportunity Data Contract, AI Opportunity Contract, Review Contract |
| AI Usage | AI may detect opportunity signals but should not auto-convert without review. |
| Workflow Usage | Opportunity supports sales follow-up and service expansion workflows. |
| Product Consumers | Opportunity Engine baseline, MarkReg, AI Agents, Workplace |
| Deferred Scope | Full opportunity scoring, campaign automation and revenue attribution. |
| Notes | Opportunity is partial in MVP to prevent overbuilding. |

---

## 8.5 Workflow Contract

| Field | Value |
|------|-------|
| Domain ID | DOM-BIZ-005 |
| Domain Name | Workflow Contract |
| Domain Category | Business Execution |
| Core Purpose | Defines allowed execution states, transitions, roles and review requirements. |
| Canonical Model Alignment | Execution Model / Contract Model |
| MVP Phase | Phase 3 — Business Execution Core |
| MVP Depth | Must Implement |
| Primary Objects | Workflow Contract, Workflow State, Workflow Transition, Workflow Role |
| Primary Services | Workflow Validation, State Transition, Workflow Contract Registration |
| Primary Events | WorkflowContractCreated, WorkflowStateChanged, WorkflowTransitionRejected |
| Primary Contracts | Workflow Contract, State Transition Contract, Review Contract |
| AI Usage | AI may suggest next actions but cannot create unapproved states. |
| Workflow Usage | This domain governs workflow usage itself. |
| Product Consumers | Workplace, MarkReg, MarkOrbit Lite, AI Agents, Codex Implementation |
| Deferred Scope | Full workflow engine and advanced process designer. |
| Notes | Workflow Contract is Core governance, not UI flow. |

---

## 8.6 Task

| Field | Value |
|------|-------|
| Domain ID | DOM-BIZ-006 |
| Domain Name | Task |
| Domain Category | Business Execution |
| Core Purpose | Defines work to be performed. |
| Canonical Model Alignment | Execution Model / Workplace Model |
| MVP Phase | Phase 3 — Business Execution Core |
| MVP Depth | Must Implement |
| Primary Objects | Task, Task Assignment, Task Status, Task Review, Task Due Date |
| Primary Services | Task Creation, Task Assignment, Task Completion, Task Review Request |
| Primary Events | TaskCreated, TaskAssigned, TaskCompleted, TaskReviewRequired |
| Primary Contracts | Task Data Contract, Task Service Contract, Task Event Contract |
| AI Usage | AI may suggest tasks or summarize task context under governance. |
| Workflow Usage | Task is the primary unit of execution in Workplace. |
| Product Consumers | Workplace, MarkReg, AI Agents |
| Deferred Scope | Advanced workforce optimization and automatic task planning. |
| Notes | Task must remain Core-owned and not be hidden inside UI logic. |

---

## 8.7 Event

| Field | Value |
|------|-------|
| Domain ID | DOM-BIZ-007 |
| Domain Name | Event |
| Domain Category | Business Execution |
| Core Purpose | Defines meaningful change in Core state or professional execution. |
| Canonical Model Alignment | Execution Model / Event Model |
| MVP Phase | Phase 3 — Business Execution Core |
| MVP Depth | Must Implement |
| Primary Objects | Event, Event Payload, Event Source, Event Subscription, Event Audit Record |
| Primary Services | Event Publishing, Event Subscription, Event Validation, Event Replay where approved |
| Primary Events | EventPublished, EventSubscriptionCreated, EventDeliveryFailed |
| Primary Contracts | Event Contract, Event Payload Contract, Event Subscription Contract |
| AI Usage | AI-related events must be governed and auditable. |
| Workflow Usage | Events coordinate downstream workflow, notification, review and reporting. |
| Product Consumers | Workplace, MarkReg, MarkOrbit Lite, AI Agents, Reporting Consumers, Codex Implementation |
| Deferred Scope | Full event streaming, advanced replay and external webhook platform. |
| Notes | Event is not log, UI action, activity feed, queue message or analytics ping. |

---

## 8.8 Notification

| Field | Value |
|------|-------|
| Domain ID | DOM-BIZ-008 |
| Domain Name | Notification |
| Domain Category | Business Execution |
| Core Purpose | Defines baseline user or system alerting. |
| Canonical Model Alignment | Execution Model / Workplace Model |
| MVP Phase | Phase 3 — Business Execution Core |
| MVP Depth | Partial Implement |
| Primary Objects | Notification, Notification Rule, Notification Recipient, Notification Status |
| Primary Services | Notification Creation, Notification Dispatch, Notification Read Tracking |
| Primary Events | NotificationCreated, NotificationSent, NotificationRead |
| Primary Contracts | Notification Contract, Event-to-Notification Contract |
| AI Usage | AI may trigger review notifications only through approved events and policies. |
| Workflow Usage | Notification supports task assignment, review, deadlines and status changes. |
| Product Consumers | Workplace, MarkReg, MarkOrbit Lite, AI Agents |
| Deferred Scope | Full omnichannel notification center and advanced preference management. |
| Notes | Notification is partial in MVP but necessary for execution support. |

---

# 9. Collaboration Network Domains

Collaboration Network Domains prepare MarkOrbit for external agents, service providers and global service collaboration.

---

## 9.1 Partner

| Field | Value |
|------|-------|
| Domain ID | DOM-NET-001 |
| Domain Name | Partner |
| Domain Category | Collaboration Network |
| Core Purpose | Defines business partners participating in channel, service or network relationships. |
| Canonical Model Alignment | Network Model / Business Responsibility Model |
| MVP Phase | Phase 5 — Network Reserved |
| MVP Depth | Reserved Boundary |
| Primary Objects | Partner, Partner Organization, Partner Relationship, Partner Account |
| Primary Services | Partner Registration, Partner Relationship Management, Partner Access Setup |
| Primary Events | PartnerCreated, PartnerActivated, PartnerSuspended |
| Primary Contracts | Partner Contract, Partner Consumption Contract |
| AI Usage | AI may summarize partner context in future, subject to permissions. |
| Workflow Usage | Partner may later support partner-facing order and collaboration workflows. |
| Product Consumers | Future Partner Center, MGSN, Service Platform |
| Deferred Scope | Full partner portal, partner commission, partner marketplace and partner analytics. |
| Notes | Partner is reserved in MVP to prevent channel/product overbuild. |

---

## 9.2 Agent

| Field | Value |
|------|-------|
| Domain ID | DOM-NET-002 |
| Domain Name | Agent |
| Domain Category | Collaboration Network |
| Core Purpose | Defines professional agents or law firms that perform trademark-related work. |
| Canonical Model Alignment | Network Model / Capability Model |
| MVP Phase | Phase 4 — Growth Core Baseline |
| MVP Depth | Partial Implement |
| Primary Objects | Agent, Agent Contact, Agent Jurisdiction Coverage, Agent Capability |
| Primary Services | Agent Registration, Agent Lookup, Agent Capability Matching, Agent Linking |
| Primary Events | AgentCreated, AgentCapabilityUpdated, AgentLinkedToMatter |
| Primary Contracts | Agent Data Contract, Agent Communication Contract, Agent Consumption Contract |
| AI Usage | AI may assist agent recommendation or communication summary under review. |
| Workflow Usage | Agent supports routing, communication and matter execution. |
| Product Consumers | MarkReg, MGSN, Workplace, AI Agents |
| Deferred Scope | Full agent scoring, ranking, marketplace matching and performance automation. |
| Notes | Agent is partial in MVP because MarkReg needs basic agent context. |

---

## 9.3 Service Provider

| Field | Value |
|------|-------|
| Domain ID | DOM-NET-003 |
| Domain Name | Service Provider |
| Domain Category | Collaboration Network |
| Core Purpose | Defines entities providing services inside or outside the network. |
| Canonical Model Alignment | Network Model / Capability Model |
| MVP Phase | Phase 4 — Growth Core Baseline |
| MVP Depth | Partial Implement |
| Primary Objects | Service Provider, Provider Service, Provider Capability, Provider Contact |
| Primary Services | Provider Registration, Provider Lookup, Provider Capability Matching |
| Primary Events | ServiceProviderCreated, ProviderCapabilityUpdated |
| Primary Contracts | Service Provider Contract, Provider Consumption Contract |
| AI Usage | AI may help match provider capabilities under governance. |
| Workflow Usage | Service Provider may support routing and execution outsourcing. |
| Product Consumers | MGSN, MarkReg, Workplace, AI Agents |
| Deferred Scope | Full provider marketplace, trust scoring and provider billing. |
| Notes | Service Provider is broader than trademark Agent. |

---

## 9.4 Service Network

| Field | Value |
|------|-------|
| Domain ID | DOM-NET-004 |
| Domain Name | Service Network |
| Domain Category | Collaboration Network |
| Core Purpose | Defines network-level collaboration structure. |
| Canonical Model Alignment | Network Model |
| MVP Phase | Phase 5 — Network Reserved |
| MVP Depth | Reserved Boundary |
| Primary Objects | Service Network, Network Membership, Network Rule, Network Relationship |
| Primary Services | Network Registration, Membership Management, Network Rule Management |
| Primary Events | ServiceNetworkCreated, NetworkMembershipCreated, NetworkRuleUpdated |
| Primary Contracts | Service Network Contract, Network Membership Contract |
| AI Usage | AI usage deferred except future network analysis and routing assistance. |
| Workflow Usage | Future network operation workflows. |
| Product Consumers | MGSN, Service Platform, Future Partner Center |
| Deferred Scope | Full MGSN operation, service exchange marketplace, trust scoring and global cooperation rules. |
| Notes | Service Network belongs more fully to Book 06 and remains reserved in MVP. |

---

## 9.5 Routing

| Field | Value |
|------|-------|
| Domain ID | DOM-NET-005 |
| Domain Name | Routing |
| Domain Category | Collaboration Network |
| Core Purpose | Defines how work, matters or recommendations are directed to agents or providers. |
| Canonical Model Alignment | Network Model / Capability Model / Business Responsibility Model |
| MVP Phase | Phase 4 — Growth Core Baseline |
| MVP Depth | Partial Implement |
| Primary Objects | Routing Decision, Routing Candidate, Routing Rule, Routing Review Record |
| Primary Services | Routing Recommendation, Routing Decision Creation, Routing Review, Routing Assignment |
| Primary Events | RoutingRecommendationGenerated, RoutingDecisionMade, RoutingReviewRequired |
| Primary Contracts | Routing Contract, AI Routing Contract, Review Contract |
| AI Usage | AI may recommend routing but review is required where business or professional risk exists. |
| Workflow Usage | Routing supports agent selection, service provider selection and assignment. |
| Product Consumers | MarkReg, MGSN, Workplace, AI Agents |
| Deferred Scope | Full automatic routing, provider ranking and marketplace matching. |
| Notes | Routing affects responsibility and must be governed. |

---

## 9.6 Communication

| Field | Value |
|------|-------|
| Domain ID | DOM-NET-006 |
| Domain Name | Communication |
| Domain Category | Collaboration Network |
| Core Purpose | Defines linked professional communication. |
| Canonical Model Alignment | Network Model / Execution Model |
| MVP Phase | Phase 4 — Growth Core Baseline |
| MVP Depth | Partial Implement |
| Primary Objects | Communication, Communication Thread, Communication Participant, Communication Summary |
| Primary Services | Communication Linking, Communication Summary, Communication Search, Communication Assignment |
| Primary Events | CommunicationLinked, CommunicationReceived, CommunicationSummaryGenerated |
| Primary Contracts | Communication Data Contract, Communication Access Contract, AI Communication Contract |
| AI Usage | AI may summarize or classify communication under Agent Contract and audit. |
| Workflow Usage | Communication links agent/client messages to matters, tasks and reviews. |
| Product Consumers | MarkReg, Workplace, AI Agents, MGSN |
| Deferred Scope | Full email client, chat platform, omnichannel communication automation and external message sync. |
| Notes | Communication is partial in MVP and must respect privacy and permission boundaries. |

---

# 10. Cross-Cutting Specification Systems

This section lists systems that cut across multiple domains.

They are not counted in the 26 baseline Core Domains.

---

## 10.1 Capability

| Field | Value |
|------|-------|
| System ID | XSYS-001 |
| System Name | Capability |
| Classification | Cross-Cutting Core Specification System |
| Core Purpose | Defines what can be performed, by whom or by what actor. |
| MVP Phase | Phase 1 — Foundation Core |
| MVP Depth | Partial Implement |
| Primary Objects | Capability, Capability Provider, Capability Scope, Capability Requirement |
| Primary Services | Capability Registration, Capability Matching, Capability Validation |
| Primary Events | CapabilityCreated, CapabilityUpdated, CapabilityMatched |
| Primary Contracts | Capability Contract, Capability Matching Contract |
| AI Usage | AI Agent capabilities must be declared and governed. |
| Workflow Usage | Capability may support task assignment, routing and review. |
| Product Consumers | MarkReg, MarkOrbit Lite, Workplace, AI Agents, MGSN |
| Deferred Scope | Full capability marketplace, provider ranking and advanced capability scoring. |
| Notes | Capability may produce executable specs but does not change the 26-domain baseline. |

---

## 10.2 Business Responsibility

| Field | Value |
|------|-------|
| System ID | XSYS-002 |
| System Name | Business Responsibility |
| Classification | Cross-Cutting Core Specification System |
| Core Purpose | Defines accountability for work, review, approval and delegation. |
| MVP Phase | Phase 3 — Business Execution Core |
| MVP Depth | Partial Implement |
| Primary Objects | Responsibility Assignment, Review Record, Approval Record, Escalation Rule |
| Primary Services | Responsibility Assignment, Review Request, Approval Recording, Escalation Handling |
| Primary Events | ResponsibilityAssigned, ReviewRequired, ReviewApproved, ReviewRejected |
| Primary Contracts | Responsibility Contract, Review Contract, Approval Contract |
| AI Usage | AI output approval and review must bind to responsibility. |
| Workflow Usage | Responsibility governs task assignment, matter ownership and review. |
| Product Consumers | Workplace, MarkReg, MarkOrbit Lite, AI Agents, MGSN |
| Deferred Scope | Full compensation, commission, pricing and revenue attribution logic. |
| Notes | Business Responsibility governs accountability, not commercial pricing. |

---

# 11. MVP Domain Priority Summary

The MVP priority sequence uses 28 execution rows:

```text
26 baseline Core Domains
+ 2 cross-cutting specification systems
= 28 MVP execution rows
```

This does not change the baseline domain count.

## 11.1 Phase 1 — Foundation Core

```text
Must Implement:
    Identity
    Organization
    User
    Permission
    Knowledge

Partial Implement:
    Policy
    Capability
```

## 11.2 Phase 2 — Professional Core

```text
Must Implement:
    Brand
    Trademark
    Jurisdiction
    Classification
    Document

Partial Implement:
    Evidence
```

## 11.3 Phase 3 — Business Execution Core

```text
Must Implement:
    Customer
    Order
    Matter
    Workflow Contract
    Task
    Event

Partial Implement:
    Business Responsibility
    Notification
```

## 11.4 Phase 4 — Growth Core Baseline

```text
Partial Implement:
    Communication
    Agent
    Service Provider
    Routing
    Opportunity
```

## 11.5 Phase 5 — Network Reserved

```text
Reserved Boundary:
    Partner
    Service Network
```

---

# 12. Domain-to-Appendix H Handoff

Appendix H — Codex Task Index must use this domain index as a source.

Codex tasks must reference:

```text
Domain ID
Domain Name
MVP Phase
MVP Depth
Required Specs
Primary Objects
Primary Services
Primary Events
Primary Contracts
Acceptance Criteria
```

Codex must not infer new domains from product names, database names or implementation folders.

---

# 13. Domain Governance Rules

A domain change requires review when it:

```text
adds a baseline domain
renames a baseline domain
changes a domain category
moves an object between domains
changes source event ownership
changes service ownership
expands MVP depth
promotes reserved or deferred scope
adds AI authority
changes product consumption boundaries
```

The governance output should update:

```text
Appendix A — Glossary
Appendix B — Core Domain Index
Appendix C — Core Object Index
Appendix D — Core Service Index
Appendix E — Event Index
Appendix F — API Index
Appendix G — Agent Index
Appendix H — Codex Task Index
core-specs/domains/
indexes/
Codex task dependencies
```

---

# 14. Domain Anti-Patterns

The following anti-patterns are prohibited.

## 14.1 Product Module as Domain

A product module is treated as a Core Domain.

Correction:

```text
Products consume domains. They do not define baseline Core Domains by default.
```

## 14.2 Database Table as Domain

A table name becomes a domain name.

Correction:

```text
Domains define professional meaning, not storage layout.
```

## 14.3 AI Agent as Domain

An AI agent is treated as a domain owner.

Correction:

```text
AI agents consume domain context under Agent Contracts.
```

## 14.4 Cross-Cutting System as Hidden Domain

Capability or Business Responsibility silently expands the domain count.

Correction:

```text
Classify them as cross-cutting systems unless architecture release changes the baseline.
```

## 14.5 Future Marketplace as MVP Domain

Full MGSN marketplace features enter Core MVP.

Correction:

```text
Use Reserved Boundary or Deferred classification.
```

---

# 15. Relationship to core-specs/domains/

This appendix prepares future `core-specs/domains/` generation.

Each future domain spec should include:

```text
Domain ID
Domain Name
Domain Category
Core Purpose
Canonical Model Alignment
MVP Phase
MVP Depth
Primary Objects
Primary Services
Primary Events
Primary Contracts
AI Usage
Workflow Usage
Product Consumers
Deferred Scope
Acceptance Criteria
Revision Notes
```

`core-specs/domains/` must follow this appendix and must not redefine the baseline domain map.

---

# 16. Acceptance Criteria

This appendix is accepted only if it satisfies the following criteria.

```text
[ ] It states that the baseline Core Domain Map contains 26 domains.
[ ] It lists all 26 baseline domains.
[ ] It groups domains into four canonical categories.
[ ] It separates Capability and Business Responsibility as cross-cutting systems.
[ ] It does not silently expand the domain count.
[ ] It assigns MVP phase and depth to each domain.
[ ] It identifies primary objects, services, events and contracts for each domain.
[ ] It identifies AI usage and workflow usage for each domain.
[ ] It identifies product consumers and deferred scope for each domain.
[ ] It explains the 28 execution rows as 26 domains plus 2 cross-cutting systems.
[ ] It provides Appendix H handoff requirements.
[ ] It prepares future core-specs/domains/ generation.
[ ] It supports the second canonical draft rewrite plan.
```

---

# 17. Revision Notes

| Version | Status | Notes |
|---------|--------|-------|
| 0.2.0 | Draft | Initial second canonical draft of Appendix B. Preserves 26 baseline Core Domains, separates cross-cutting systems, defines MVP phase/depth and prepares `core-specs/domains/` and Appendix H handoff. |

---

**End of Appendix**
