# Book 02

# B02-PLN-0004 — Core Execution Matrix v1.0

**Document ID:** B02-PLN-0004

**Title:** Core Execution Matrix v1.0

**Version:** 1.0.0

**Status:** Canonical Draft

**Category:** Planning

**Owner:** MarkOrbit Publications Editorial Board

**Applies To:** Book 02 — *MarkOrbit Core Specification*

**Related Documents:**

- Book 01 — *The Operating System for Global Brand Services*
- Book 02 TOC v1.2 — Frozen
- B02-PLN-0001 — Core Positioning
- B02-PLN-0002 — Architecture Blueprint v2.0
- B02-PLN-0003 — Core Domain Map v1.0
- B02-EDT-0001 — Editorial Protocol and Chapter Writing Template
- MAC — MarkOrbit Architecture Canon
- MAG — MarkOrbit Architecture Governance
- MAS — MarkOrbit Architecture Specifications

---

# 1. Purpose

This document defines the Core Execution Matrix for the MarkOrbit Core.

Its purpose is to translate the Core Domain Map into execution assets that can guide `core-specs/`, Codex tasks and future implementation.

This document does not define full database schemas.

It does not define product UI.

It does not define product PRDs.

It does not define implementation code.

It defines the execution mapping that connects:

```text
Core Domain
        ↓
Execution Assets
        ↓
core-specs/
        ↓
Codex Tasks
        ↓
Software Implementation
```

The Core Execution Matrix is therefore the bridge between architecture planning and implementation planning.

---

# 2. Execution Matrix Statement

Every Core Domain shall eventually map to a consistent set of execution assets.

A Core Domain is accepted for implementation only when its execution assets can be identified.

The standard execution asset set is:

- database tables;
- domain models;
- domain services;
- API surface;
- events;
- AI capability usage;
- workflow or execution usage;
- product consumers;
- Codex tasks;
- acceptance criteria.

The matrix does not require all assets to be implemented immediately.

It requires that every domain has a clear implementation path.

---

# 3. Relationship to Book 02 Manuscript

The Book 02 manuscript defines Core meaning, architecture, boundaries and specification frameworks.

This document defines how those concepts become executable.

The relationship is:

```text
Book 02 Manuscript
    defines Core meaning and specification frameworks

B02-PLN-0004
    maps Core Domains to execution assets

core-specs/
    contains detailed executable specifications

Codex
    generates implementation tasks from core-specs and planning
```

The manuscript shall not duplicate the full execution matrix.

The matrix supports Part IV of Book 02:

- 28 Core MVP Boundary
- 29 MVP Domain Priority
- 30 MVP Execution Matrix
- 31 Codex Implementation Roadmap

---

# 4. Relationship to core-specs

The execution matrix identifies the assets that shall later be specified in `core-specs/`.

| Execution Asset | Target Location |
|-----------------|-----------------|
| Domain Specs | `core-specs/domains/` |
| Object Specs | `core-specs/objects/` |
| Service Specs | `core-specs/services/` |
| Contract Specs | `core-specs/contracts/` |
| Event Specs | `core-specs/events/` |
| Agent Specs | `core-specs/agents/` |
| API Specs | `core-specs/api/` |
| Workflow Contracts | `core-specs/workflows/` |
| Codex Tasks | `indexes/codex-task-index.md` or `planning/` |

This document does not replace those files.

It defines what they must eventually contain.

---

# 5. Execution Asset Model

Each Core Domain shall be mapped to the following asset model.

```text
Core Domain
    ├── Database Tables
    ├── Domain Models
    ├── Domain Services
    ├── API Surface
    ├── Events
    ├── AI Capability Usage
    ├── Workflow / Execution Usage
    ├── Product Consumers
    ├── Codex Tasks
    └── Acceptance Criteria
```

Each asset has a different responsibility.

## 5.1 Database Tables

Database tables store persistent domain state.

They do not define domain meaning.

Domain meaning is defined by Book 02 and `core-specs/`.

## 5.2 Domain Models

Domain models represent domain objects in implementation.

They shall preserve Core semantics.

## 5.3 Domain Services

Domain services expose reusable Core capabilities.

They shall not contain product-specific UI behavior.

## 5.4 API Surface

API surface defines how products and services consume the Core.

API details belong in `core-specs/api/`.

## 5.5 Events

Events record significant domain changes.

They support automation, audit, notification, opportunity discovery and cross-product coordination.

## 5.6 AI Capability Usage

AI capability usage defines where AI may support professional work.

AI shall be governed.

AI shall not define professional truth.

## 5.7 Workflow / Execution Usage

This identifies whether a domain participates in execution.

Core defines execution primitives and workflow contracts.

Workplace operates workflow execution.

## 5.8 Product Consumers

Product consumers identify which publications or products consume the domain.

Consumers do not own the domain.

## 5.9 Codex Tasks

Codex tasks are generated from approved `core-specs/` assets.

Codex shall not infer product requirements beyond the Core specification.

## 5.10 Acceptance Criteria

Acceptance criteria define minimum completion conditions for a domain implementation.

---

# 6. Execution Phases

The MVP implementation sequence is divided into five phases.

```text
Phase 1 — Foundation Core
        ↓
Phase 2 — Professional Core
        ↓
Phase 3 — Business Execution Core
        ↓
Phase 4 — Growth Core
        ↓
Phase 5 — Network Core
```

The phases are designed to build an executable skeleton before expanding into full ecosystem capability.

---

# 7. Phase 1 — Foundation Core

Phase 1 establishes identity, structure, access and knowledge foundation.

| Domain | Execution Purpose |
|--------|-------------------|
| Identity | Establish persistent identity resolution |
| Organization | Register organizations and relationships |
| User | Register users, memberships and assignments |
| Permission | Control access and authorization |
| Knowledge | Store and retrieve professional knowledge |

Phase 1 must be implemented before professional, execution or network domains become reliable.

---

# 8. Phase 2 — Professional Core

Phase 2 establishes the professional subject matter of international trademark and global brand services.

| Domain | Execution Purpose |
|--------|-------------------|
| Brand | Store brand assets and brand ownership context |
| Trademark | Store trademark records and lifecycle data |
| Jurisdiction | Store country, office and filing rules |
| Classification | Store classes, goods/services and classification logic |
| Document | Store and generate professional documents |

Phase 2 creates the professional data and knowledge base for MarkReg, MarkOrbit Lite and future AI capabilities.

---

# 9. Phase 3 — Business Execution Core

Phase 3 establishes work execution and commercial execution.

| Domain | Execution Purpose |
|--------|-------------------|
| Customer | Store customer context and relationships |
| Matter | Create and manage professional service matters |
| Order | Convert service purchases into executable matters |
| Workflow Contract | Define reusable workflow contracts |
| Task | Assign and track execution units |
| Event | Record domain and lifecycle events |

Phase 3 makes the Core operational without requiring product-specific workflow execution.

---

# 10. Phase 4 — Growth Core

Phase 4 establishes growth, risk, opportunity and advanced professional support.

| Domain | Execution Purpose |
|--------|-------------------|
| Opportunity | Generate and route business opportunities |
| Notification | Deliver reminders and alerts |
| Policy | Evaluate business, routing and workflow rules |
| Evidence | Manage use evidence and supporting materials |
| Agent | Match professional agents and service representatives |
| Routing | Route work, opportunities and service requests |

Phase 4 turns Core data into business growth and intelligent coordination.

---

# 11. Phase 5 — Network Core

Phase 5 establishes global collaboration network capability.

| Domain | Execution Purpose |
|--------|-------------------|
| Partner | Manage partner agencies and collaborators |
| Service Provider | Manage external providers and offerings |
| Service Network | Manage network membership, trust and capability exchange |
| Communication | Manage structured communication records |

Phase 5 prepares the Core for MGSN and global collaboration at scale.

---

# 12. Domain Execution Matrix

This matrix provides the initial execution mapping for all Core Domains.

It is planning-level.

Detailed specifications belong in `core-specs/`.

---

## 12.1 Identity Domain

| Asset | Execution Mapping |
|-------|-------------------|
| Database Tables | `identities`, `identity_relationships`, `identity_verifications` |
| Domain Models | `Identity`, `PersonIdentity`, `OrganizationIdentity`, `WorkplaceIdentity` |
| Services | `IdentityResolutionService`, `IdentityMatchingService`, `IdentityVerificationService` |
| API Surface | `/api/identities`, `/api/identities/{id}/relationships` |
| Events | `IdentityCreated`, `IdentityLinked`, `IdentityVerified` |
| AI Usage | Identity matching assistance, duplicate detection |
| Execution Usage | Permission, organization, user and network identity resolution |
| Product Consumers | MarkReg, MarkOrbit Lite, MGSN |
| Codex Tasks | Create identity schema, models, services, APIs and tests |
| MVP Phase | Phase 1 |

---

## 12.2 Organization Domain

| Asset | Execution Mapping |
|-------|-------------------|
| Database Tables | `organizations`, `organization_profiles`, `organization_relationships` |
| Domain Models | `Organization`, `OrganizationProfile`, `OrganizationRelationship` |
| Services | `OrganizationRegistryService`, `OrganizationSearchService`, `OrganizationRelationshipService` |
| API Surface | `/api/organizations`, `/api/organizations/{id}/relationships` |
| Events | `OrganizationCreated`, `OrganizationUpdated`, `OrganizationRelationshipChanged` |
| AI Usage | Organization classification, duplicate organization detection |
| Execution Usage | Customer, partner, agent and service provider foundation |
| Product Consumers | MarkReg, MarkOrbit Lite, MGSN |
| Codex Tasks | Create organization schema, models, registry service and tests |
| MVP Phase | Phase 1 |

---

## 12.3 User Domain

| Asset | Execution Mapping |
|-------|-------------------|
| Database Tables | `users`, `user_profiles`, `memberships`, `assignments` |
| Domain Models | `User`, `UserProfile`, `Membership`, `Assignment` |
| Services | `UserRegistrationService`, `UserContextService`, `MembershipService` |
| API Surface | `/api/users`, `/api/users/{id}/memberships` |
| Events | `UserCreated`, `MembershipAssigned`, `UserContextChanged` |
| AI Usage | Workload and assignment assistance |
| Execution Usage | Task assignment, permission evaluation, workplace participation |
| Product Consumers | MarkReg, MarkOrbit Lite |
| Codex Tasks | Create user schema, membership model, user service and tests |
| MVP Phase | Phase 1 |

---

## 12.4 Permission Domain

| Asset | Execution Mapping |
|-------|-------------------|
| Database Tables | `roles`, `permissions`, `access_policies`, `authorization_logs` |
| Domain Models | `Role`, `Permission`, `AccessPolicy`, `AuthorizationContext` |
| Services | `PermissionEvaluationService`, `RoleAssignmentService`, `AuthorizationAuditService` |
| API Surface | `/api/permissions`, `/api/roles`, `/api/access/check` |
| Events | `RoleAssigned`, `PermissionChanged`, `AccessDenied` |
| AI Usage | Permission-aware agent execution |
| Execution Usage | All Core domains |
| Product Consumers | All products |
| Codex Tasks | Create RBAC/ABAC foundation, permission checks and audit tests |
| MVP Phase | Phase 1 |

---

## 12.5 Knowledge Domain

| Asset | Execution Mapping |
|-------|-------------------|
| Database Tables | `knowledge_assets`, `knowledge_sources`, `knowledge_nodes`, `knowledge_relationships` |
| Domain Models | `KnowledgeAsset`, `KnowledgeSource`, `KnowledgeNode`, `KnowledgeRelationship` |
| Services | `KnowledgeRetrievalService`, `KnowledgeClassificationService`, `KnowledgeValidationService` |
| API Surface | `/api/knowledge`, `/api/knowledge/search`, `/api/knowledge/{id}/relationships` |
| Events | `KnowledgeAssetCreated`, `KnowledgeUpdated`, `KnowledgeValidated` |
| AI Usage | Retrieval, rule explanation, professional drafting support |
| Execution Usage | AI capability, professional services, validation and recommendations |
| Product Consumers | MarkReg, MarkOrbit Lite, MGSN |
| Codex Tasks | Create knowledge schema, retrieval service, indexing hooks and tests |
| MVP Phase | Phase 1 |

---

## 12.6 Brand Domain

| Asset | Execution Mapping |
|-------|-------------------|
| Database Tables | `brands`, `brand_assets`, `brand_portfolios`, `brand_owners` |
| Domain Models | `Brand`, `BrandAsset`, `BrandPortfolio`, `BrandOwner` |
| Services | `BrandAssetService`, `BrandPortfolioService`, `BrandOpportunityService` |
| API Surface | `/api/brands`, `/api/brands/{id}/assets`, `/api/brands/{id}/portfolio` |
| Events | `BrandCreated`, `BrandAssetAdded`, `BrandPortfolioUpdated` |
| AI Usage | Brand strategy support, opportunity discovery |
| Execution Usage | Trademark, opportunity and brand asset vault |
| Product Consumers | MarkOrbit Lite, MarkReg, Brand Asset Vault |
| Codex Tasks | Create brand schema, brand asset service and basic portfolio tests |
| MVP Phase | Phase 2 |

---

## 12.7 Trademark Domain

| Asset | Execution Mapping |
|-------|-------------------|
| Database Tables | `trademarks`, `trademark_applications`, `trademark_registrations`, `trademark_status_events` |
| Domain Models | `Trademark`, `TrademarkApplication`, `TrademarkRegistration`, `TrademarkStatusEvent` |
| Services | `TrademarkSearchService`, `TrademarkLifecycleService`, `TrademarkStatusNormalizationService` |
| API Surface | `/api/trademarks`, `/api/trademarks/{id}`, `/api/trademarks/{id}/events` |
| Events | `TrademarkCreated`, `TrademarkStatusChanged`, `TrademarkRegistered`, `TrademarkExpired` |
| AI Usage | Trademark analysis, lifecycle risk detection, status interpretation |
| Execution Usage | Matter, opportunity, brand asset management |
| Product Consumers | MarkReg, MarkOrbit Lite, Brand Asset Vault |
| Codex Tasks | Create trademark schema, lifecycle model, status service and tests |
| MVP Phase | Phase 2 |

---

## 12.8 Jurisdiction Domain

| Asset | Execution Mapping |
|-------|-------------------|
| Database Tables | `jurisdictions`, `trademark_offices`, `filing_requirements`, `deadline_rules` |
| Domain Models | `Jurisdiction`, `TrademarkOffice`, `FilingRequirement`, `DeadlineRule` |
| Services | `JurisdictionLookupService`, `FilingRequirementService`, `DeadlineCalculationService` |
| API Surface | `/api/jurisdictions`, `/api/jurisdictions/{code}/requirements` |
| Events | `JurisdictionRuleUpdated`, `FilingRequirementChanged` |
| AI Usage | Jurisdiction recommendation and filing route support |
| Execution Usage | Trademark, classification, matter, order and routing |
| Product Consumers | MarkReg, MarkOrbit Lite, MGSN |
| Codex Tasks | Create jurisdiction schema, requirement service and deadline tests |
| MVP Phase | Phase 2 |

---

## 12.9 Classification Domain

| Asset | Execution Mapping |
|-------|-------------------|
| Database Tables | `classes`, `goods_service_items`, `classification_rules`, `similar_groups` |
| Domain Models | `Class`, `GoodsServiceItem`, `ClassificationRule`, `SimilarGroup` |
| Services | `ClassificationSearchService`, `GoodsRecommendationService`, `ClassificationValidationService` |
| API Surface | `/api/classes`, `/api/goods-services/search`, `/api/classification/validate` |
| Events | `ClassificationRuleUpdated`, `GoodsItemAdded`, `ClassificationValidated` |
| AI Usage | Class recommendation and goods/services drafting |
| Execution Usage | Trademark filing, order quotation, AI filing advisor |
| Product Consumers | MarkReg, MarkOrbit Lite |
| Codex Tasks | Create classification schema, search service and validation tests |
| MVP Phase | Phase 2 |

---

## 12.10 Document Domain

| Asset | Execution Mapping |
|-------|-------------------|
| Database Tables | `documents`, `document_templates`, `document_versions`, `document_packages` |
| Domain Models | `Document`, `DocumentTemplate`, `DocumentVersion`, `DocumentPackage` |
| Services | `DocumentGenerationService`, `DocumentParsingService`, `DocumentStorageService` |
| API Surface | `/api/documents`, `/api/documents/{id}`, `/api/document-packages` |
| Events | `DocumentCreated`, `DocumentParsed`, `DocumentPackageGenerated` |
| AI Usage | Drafting support, OA review support, document summarization |
| Execution Usage | Matter, evidence, communication and order delivery |
| Product Consumers | MarkReg, MarkOrbit Lite, MGSN |
| Codex Tasks | Create document metadata schema, storage contract, parsing hooks and tests |
| MVP Phase | Phase 2 |

---

## 12.11 Customer Domain

| Asset | Execution Mapping |
|-------|-------------------|
| Database Tables | `customers`, `customer_accounts`, `customer_contacts`, `customer_relationships` |
| Domain Models | `Customer`, `CustomerAccount`, `CustomerContact`, `CustomerRelationship` |
| Services | `CustomerRegistryService`, `CustomerContextService`, `CustomerRelationshipService` |
| API Surface | `/api/customers`, `/api/customers/{id}/contacts`, `/api/customers/{id}/context` |
| Events | `CustomerCreated`, `CustomerContactAdded`, `CustomerContextUpdated` |
| AI Usage | Customer context summary, opportunity context generation |
| Execution Usage | Order, matter, opportunity, communication |
| Product Consumers | MarkReg, MarkOrbit Lite |
| Codex Tasks | Create customer schema, registry service and customer context tests |
| MVP Phase | Phase 3 |

---

## 12.12 Matter Domain

| Asset | Execution Mapping |
|-------|-------------------|
| Database Tables | `matters`, `matter_types`, `matter_statuses`, `matter_assignments`, `matter_timelines` |
| Domain Models | `Matter`, `MatterType`, `MatterStatus`, `MatterAssignment`, `MatterTimeline` |
| Services | `MatterCreationService`, `MatterTrackingService`, `MatterAssignmentService` |
| API Surface | `/api/matters`, `/api/matters/{id}`, `/api/matters/{id}/timeline` |
| Events | `MatterCreated`, `MatterStatusChanged`, `MatterAssigned`, `MatterClosed` |
| AI Usage | Matter assistant, deadline and process support |
| Execution Usage | Workflow contract, task, document, agent collaboration |
| Product Consumers | MarkReg, MarkOrbit Lite |
| Codex Tasks | Create matter schema, matter service, status transitions and tests |
| MVP Phase | Phase 3 |

---

## 12.13 Order Domain

| Asset | Execution Mapping |
|-------|-------------------|
| Database Tables | `orders`, `order_items`, `service_products`, `price_quotes`, `payment_records` |
| Domain Models | `Order`, `OrderItem`, `ServiceProduct`, `PriceQuote`, `PaymentRecord` |
| Services | `OrderCreationService`, `QuoteGenerationService`, `OrderToMatterService` |
| API Surface | `/api/orders`, `/api/orders/{id}`, `/api/orders/{id}/convert-to-matter` |
| Events | `OrderCreated`, `QuoteGenerated`, `OrderConvertedToMatter`, `PaymentLinked` |
| AI Usage | Quote support and order assistant |
| Execution Usage | Customer, matter, opportunity and product purchase flow |
| Product Consumers | MarkReg, MarkOrbit Lite |
| Codex Tasks | Create order schema, quote service, order-to-matter conversion and tests |
| MVP Phase | Phase 3 |

---

## 12.14 Workflow Contract Domain

| Asset | Execution Mapping |
|-------|-------------------|
| Database Tables | `workflow_contracts`, `workflow_steps`, `workflow_states`, `workflow_transitions` |
| Domain Models | `WorkflowContract`, `WorkflowStep`, `WorkflowState`, `WorkflowTransition` |
| Services | `WorkflowContractService`, `WorkflowValidationService`, `WorkflowStateRuleService` |
| API Surface | `/api/workflow-contracts`, `/api/workflow-contracts/{id}/validate` |
| Events | `WorkflowContractCreated`, `WorkflowContractValidated`, `WorkflowStateRuleChanged` |
| AI Usage | Workflow review and optimization suggestions |
| Execution Usage | Matter, task, event and Workplace operation |
| Product Consumers | Book 03 Workplace, MarkReg, MarkOrbit Lite |
| Codex Tasks | Create workflow contract schema, validation service and contract tests |
| MVP Phase | Phase 3 |

**Boundary Rule:** Core defines workflow contracts. Workplace operates workflows.

---

## 12.15 Task Domain

| Asset | Execution Mapping |
|-------|-------------------|
| Database Tables | `tasks`, `task_assignments`, `task_statuses`, `task_dependencies`, `task_results` |
| Domain Models | `Task`, `TaskAssignment`, `TaskStatus`, `TaskDependency`, `TaskResult` |
| Services | `TaskCreationService`, `TaskAssignmentService`, `TaskTrackingService` |
| API Surface | `/api/tasks`, `/api/tasks/{id}`, `/api/tasks/{id}/assign` |
| Events | `TaskCreated`, `TaskAssigned`, `TaskCompleted`, `TaskEscalated` |
| AI Usage | Task assistant, workload suggestion |
| Execution Usage | Workflow contract, matter, event and notification |
| Product Consumers | MarkReg, MarkOrbit Lite, Workplace |
| Codex Tasks | Create task schema, assignment service, task lifecycle tests |
| MVP Phase | Phase 3 |

---

## 12.16 Event Domain

| Asset | Execution Mapping |
|-------|-------------------|
| Database Tables | `events`, `event_types`, `event_streams`, `event_subscriptions`, `event_logs` |
| Domain Models | `Event`, `EventType`, `EventStream`, `EventSubscription` |
| Services | `EventPublishingService`, `EventSubscriptionService`, `EventReplayService` |
| API Surface | `/api/events`, `/api/event-streams`, `/api/event-subscriptions` |
| Events | `EventPublished`, `EventSubscribed`, `EventReplayRequested` |
| AI Usage | Monitoring, alerting and opportunity trigger support |
| Execution Usage | All execution and growth domains |
| Product Consumers | All products |
| Codex Tasks | Create event schema, event bus abstraction, subscription tests |
| MVP Phase | Phase 3 |

---

## 12.17 Opportunity Domain

| Asset | Execution Mapping |
|-------|-------------------|
| Database Tables | `opportunities`, `opportunity_sources`, `opportunity_scores`, `opportunity_assignments` |
| Domain Models | `Opportunity`, `OpportunitySource`, `OpportunityScore`, `OpportunityAssignment` |
| Services | `OpportunityDiscoveryService`, `OpportunityScoringService`, `OpportunityRoutingService` |
| API Surface | `/api/opportunities`, `/api/opportunities/{id}`, `/api/opportunities/{id}/route` |
| Events | `OpportunityCreated`, `OpportunityScored`, `OpportunityAssigned`, `OpportunityConverted` |
| AI Usage | Opportunity discovery, scoring and recommendation |
| Execution Usage | Customer, trademark, brand, routing and notification |
| Product Consumers | MarkOrbit Lite, MarkReg, Opportunity Engine |
| Codex Tasks | Create opportunity schema, scoring service, routing hook and tests |
| MVP Phase | Phase 4 |

---

## 12.18 Notification Domain

| Asset | Execution Mapping |
|-------|-------------------|
| Database Tables | `notifications`, `reminders`, `alerts`, `channels`, `delivery_logs` |
| Domain Models | `Notification`, `Reminder`, `Alert`, `Channel`, `DeliveryLog` |
| Services | `NotificationDispatchService`, `ReminderSchedulingService`, `AlertGenerationService` |
| API Surface | `/api/notifications`, `/api/reminders`, `/api/alerts` |
| Events | `NotificationCreated`, `ReminderDue`, `AlertTriggered`, `NotificationDelivered` |
| AI Usage | Reminder drafting and follow-up suggestions |
| Execution Usage | Event, task, opportunity and communication |
| Product Consumers | MarkReg, MarkOrbit Lite |
| Codex Tasks | Create notification schema, dispatch contract and scheduling tests |
| MVP Phase | Phase 4 |

---

## 12.19 Policy Domain

| Asset | Execution Mapping |
|-------|-------------------|
| Database Tables | `policies`, `policy_rules`, `policy_scopes`, `policy_decisions`, `policy_versions` |
| Domain Models | `Policy`, `PolicyRule`, `PolicyScope`, `PolicyDecision`, `PolicyVersion` |
| Services | `PolicyEvaluationService`, `PolicyValidationService`, `PolicyVersioningService` |
| API Surface | `/api/policies`, `/api/policies/evaluate`, `/api/policy-decisions` |
| Events | `PolicyCreated`, `PolicyUpdated`, `PolicyDecisionMade` |
| AI Usage | Policy-aware recommendations and AI execution constraints |
| Execution Usage | Routing, workflow contract, order, matter and AI governance |
| Product Consumers | All products |
| Codex Tasks | Create policy schema, evaluation service and policy tests |
| MVP Phase | Phase 4 |

---

## 12.20 Evidence Domain

| Asset | Execution Mapping |
|-------|-------------------|
| Database Tables | `evidence`, `evidence_sources`, `evidence_packages`, `evidence_reviews` |
| Domain Models | `Evidence`, `EvidenceSource`, `EvidencePackage`, `EvidenceReview` |
| Services | `EvidenceIntakeService`, `EvidenceClassificationService`, `EvidencePackagingService` |
| API Surface | `/api/evidence`, `/api/evidence-packages`, `/api/evidence/{id}/review` |
| Events | `EvidenceUploaded`, `EvidenceClassified`, `EvidencePackageGenerated` |
| AI Usage | Evidence review and declaration support |
| Execution Usage | Trademark, matter, document and brand asset vault |
| Product Consumers | MarkReg, MarkOrbit Lite, Brand Asset Vault |
| Codex Tasks | Create evidence schema, packaging service and evidence review tests |
| MVP Phase | Phase 4 |

---

## 12.21 Agent Domain

| Asset | Execution Mapping |
|-------|-------------------|
| Database Tables | `agents`, `agent_contacts`, `agent_capabilities`, `agent_jurisdictions`, `agent_ratings` |
| Domain Models | `Agent`, `AgentContact`, `AgentCapability`, `AgentJurisdiction`, `AgentRating` |
| Services | `AgentRegistryService`, `AgentSearchService`, `AgentCapabilityMatchingService` |
| API Surface | `/api/agents`, `/api/agents/{id}/capabilities`, `/api/agents/search` |
| Events | `AgentCreated`, `AgentCapabilityUpdated`, `AgentRatingChanged` |
| AI Usage | Agent selection and reliability evaluation |
| Execution Usage | Matter, routing, service network and MGSN |
| Product Consumers | MarkReg, MGSN |
| Codex Tasks | Create agent schema, matching service and rating tests |
| MVP Phase | Phase 4 |

---

## 12.22 Routing Domain

| Asset | Execution Mapping |
|-------|-------------------|
| Database Tables | `routes`, `routing_rules`, `routing_decisions`, `routing_candidates`, `routing_history` |
| Domain Models | `Route`, `RoutingRule`, `RoutingDecision`, `RoutingCandidate`, `RoutingHistory` |
| Services | `WorkRoutingService`, `OpportunityRoutingService`, `ProviderRoutingService` |
| API Surface | `/api/routing/decide`, `/api/routing/history`, `/api/routes` |
| Events | `RoutingDecisionMade`, `RouteAssigned`, `RoutingFailed` |
| AI Usage | Routing recommendation and assignment explanation |
| Execution Usage | Matter, opportunity, agent, service provider and service network |
| Product Consumers | MarkReg, MarkOrbit Lite, MGSN |
| Codex Tasks | Create routing schema, decision service and routing tests |
| MVP Phase | Phase 4 |

---

## 12.23 Partner Domain

| Asset | Execution Mapping |
|-------|-------------------|
| Database Tables | `partners`, `partner_contacts`, `partner_accounts`, `partner_relationships`, `partner_tiers` |
| Domain Models | `Partner`, `PartnerContact`, `PartnerAccount`, `PartnerRelationship`, `PartnerTier` |
| Services | `PartnerRegistryService`, `PartnerMatchingService`, `PartnerPerformanceService` |
| API Surface | `/api/partners`, `/api/partners/{id}/contacts`, `/api/partners/{id}/performance` |
| Events | `PartnerCreated`, `PartnerTierChanged`, `PartnerRelationshipChanged` |
| AI Usage | Partner development and matching support |
| Execution Usage | Opportunity, order, communication and service network |
| Product Consumers | MarkReg, MGSN |
| Codex Tasks | Create partner schema, registry service and partner tests |
| MVP Phase | Phase 5 |

---

## 12.24 Service Provider Domain

| Asset | Execution Mapping |
|-------|-------------------|
| Database Tables | `service_providers`, `service_offerings`, `provider_prices`, `provider_coverage`, `provider_capacity` |
| Domain Models | `ServiceProvider`, `ServiceOffering`, `ProviderPrice`, `ProviderCoverage`, `ProviderCapacity` |
| Services | `ProviderRegistryService`, `ProviderMatchingService`, `ProviderQuoteService` |
| API Surface | `/api/service-providers`, `/api/service-providers/{id}/offerings`, `/api/provider-quotes` |
| Events | `ProviderCreated`, `ProviderOfferingUpdated`, `ProviderQuoteReceived` |
| AI Usage | Provider matching and quote comparison support |
| Execution Usage | Service network, routing, agent and MGSN |
| Product Consumers | MGSN, MarkReg |
| Codex Tasks | Create provider schema, offering model, quote service and tests |
| MVP Phase | Phase 5 |

---

## 12.25 Service Network Domain

| Asset | Execution Mapping |
|-------|-------------------|
| Database Tables | `service_networks`, `network_nodes`, `network_memberships`, `trust_records`, `capability_exchanges` |
| Domain Models | `ServiceNetwork`, `NetworkNode`, `Membership`, `TrustRecord`, `CapabilityExchange` |
| Services | `NetworkDiscoveryService`, `MembershipService`, `TrustEvaluationService` |
| API Surface | `/api/service-networks`, `/api/network-nodes`, `/api/network-memberships` |
| Events | `NetworkNodeJoined`, `MembershipChanged`, `TrustRecordUpdated` |
| AI Usage | Network routing and trust evaluation support |
| Execution Usage | MGSN, routing, partner, agent and service provider |
| Product Consumers | MGSN |
| Codex Tasks | Create network schema, membership service and trust tests |
| MVP Phase | Phase 5 |

---

## 12.26 Communication Domain

| Asset | Execution Mapping |
|-------|-------------------|
| Database Tables | `conversations`, `messages`, `threads`, `communication_participants`, `communication_logs` |
| Domain Models | `Conversation`, `Message`, `Thread`, `CommunicationParticipant`, `CommunicationLog` |
| Services | `MessageCaptureService`, `ConversationLinkingService`, `CommunicationSearchService` |
| API Surface | `/api/conversations`, `/api/messages`, `/api/communication/search` |
| Events | `MessageCaptured`, `ConversationLinked`, `CommunicationSummarized` |
| AI Usage | Email drafting, thread summarization and client reply support |
| Execution Usage | Matter, customer, partner, agent, service provider and MGSN |
| Product Consumers | MarkReg, MarkOrbit Lite, MGSN |
| Codex Tasks | Create communication schema, message capture service and summary tests |
| MVP Phase | Phase 5 |

---

# 13. Cross-Domain Execution Dependencies

The following dependencies shall guide implementation order.

```text
Identity
    ↓
Organization
    ↓
User / Customer / Partner / Agent / Service Provider
    ↓
Permission / Policy

Knowledge
    ↓
Brand / Trademark / Jurisdiction / Classification
    ↓
Document / Evidence
    ↓
Matter / Order / Opportunity

Matter
    ↓
Workflow Contract
    ↓
Task
    ↓
Event
    ↓
Notification

Partner / Agent / Service Provider
    ↓
Service Network
    ↓
Routing
    ↓
Communication
```

Dependencies define execution sequence and ownership.

Dependencies do not authorize one domain to redefine another.

---

# 14. Database Execution Matrix

Database execution shall follow these rules.

## Rule 1

Database tables shall be derived from approved domain and object specifications.

## Rule 2

A database table shall not define Core meaning independently.

## Rule 3

Shared Core Objects shall not be duplicated into product-specific tables without explicit mapping.

## Rule 4

Lifecycle and audit-sensitive objects shall have events or history records.

## Rule 5

AI-generated outputs shall be stored with provenance, source and audit context where used in professional work.

---

# 15. Service Execution Matrix

Service execution shall follow these rules.

## Rule 1

A Core Service shall expose a reusable capability.

## Rule 2

A Core Service shall not contain product UI behavior.

## Rule 3

A Core Service shall declare input, output, context, permission and failure handling.

## Rule 4

High-risk professional services shall define human review requirements.

## Rule 5

AI-assisted services shall declare knowledge dependency and audit requirements.

---

# 16. API Execution Matrix

API execution shall follow these rules.

## Rule 1

APIs shall expose Core capabilities through explicit contracts.

## Rule 2

API names shall follow domain ownership.

## Rule 3

APIs shall not allow products to bypass permission or policy rules.

## Rule 4

APIs shall preserve Core Object semantics.

## Rule 5

Detailed API specifications belong in:

```text
core-specs/api/
```

---

# 17. Event Execution Matrix

Event execution shall follow these rules.

## Rule 1

Events shall represent meaningful domain changes.

## Rule 2

Events shall have source, trigger, payload, timestamp and audit context.

## Rule 3

Events shall support subscription where cross-domain coordination is required.

## Rule 4

Events shall not be used as unstructured logs.

## Rule 5

Detailed event specifications belong in:

```text
core-specs/events/
```

---

# 18. AI Execution Matrix

AI execution shall follow these rules.

## Rule 1

AI shall execute governed capabilities.

## Rule 2

AI shall not define professional truth.

## Rule 3

AI shall use authorized knowledge sources.

## Rule 4

AI output used in professional work shall be auditable.

## Rule 5

High-risk AI actions shall require human review.

## Rule 6

Detailed AI agent specifications belong in:

```text
core-specs/agents/
```

---

# 19. Workflow Execution Matrix

Workflow execution shall follow the Core / Workplace boundary.

## Rule 1

Core defines workflow contracts.

## Rule 2

Workplace operates workflow execution.

## Rule 3

Products deliver workflow experience.

## Rule 4

Workflow contract details belong in:

```text
core-specs/workflows/
```

## Rule 5

Product-specific workflow screens shall not be included in Book 02.

---

# 20. Codex Task Generation Rules

Codex tasks shall be generated only from approved specifications.

## Rule 1

A Codex task shall identify the source domain.

## Rule 2

A Codex task shall identify the target asset.

## Rule 3

A Codex task shall reference related objects, services, events and APIs.

## Rule 4

A Codex task shall include acceptance criteria.

## Rule 5

A Codex task shall not introduce product features that are not defined by Book 02 or `core-specs/`.

## Rule 6

A Codex task shall not create AI autonomy beyond approved governance rules.

---

# 21. Codex Task Template

```markdown
# Codex Task — [Task Name]

**Task ID:** B02-CODEX-[ID]

**Source Domain:** [Domain Name]

**Source Spec:** [core-specs path]

**Target Asset:**

- Database
- Model
- Service
- API
- Event
- Agent
- Workflow Contract
- Test

---

# 1. Purpose

# 2. Scope

# 3. Inputs

# 4. Outputs

# 5. Implementation Requirements

# 6. Boundary Rules

# 7. Tests

# 8. Acceptance Criteria

# 9. Exclusions
```

---

# 22. MVP Acceptance Criteria

The Core MVP is accepted only if:

- Foundation Core domains are implemented sufficiently to support identity, organization, user, permission and knowledge.
- Professional Core domains are implemented sufficiently to support brand, trademark, jurisdiction, classification and document.
- Business Execution Core domains are implemented sufficiently to support customer, matter, order, workflow contract, task and event.
- Core Objects have stable semantic definitions.
- Core Services have explicit contracts.
- Events are recorded for meaningful lifecycle changes.
- Permission rules are enforced.
- AI capability usage is governed.
- Products can consume Core through explicit contracts.
- Codex tasks can be generated from `core-specs/`.
- Implementation does not redefine Core meaning locally.

---

# 23. Execution Exclusions

The following shall not be included in the Core Execution Matrix.

- Product UI screens
- Marketing pages
- Product pricing
- Sales scripts
- Prompt libraries
- Deployment scripts
- Vendor-specific infrastructure
- Full product PRDs
- Non-reusable operational SOPs
- Product-specific workflow experience
- Ungoverned AI automation

These may belong to product or implementation documentation.

They shall not define Core execution.

---

# 24. Revision Policy

Changes to this execution matrix require review when they affect:

- MVP phase order;
- domain execution assets;
- database ownership;
- service ownership;
- API ownership;
- event ownership;
- AI governance rules;
- workflow boundary;
- Codex task generation.

Material changes shall be reviewed before they affect `core-specs/` or implementation.

---

# Revision History

| Version | Status | Description |
|---------|--------|-------------|
| 1.0.0 | Canonical Draft | Rewritten Core Execution Matrix aligned with Book 02 TOC v1.2, Core Positioning, Architecture Blueprint v2.0 and Core Domain Map v1.0. |

---

**End of Document**
