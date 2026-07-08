# Book 02

# Appendix C — Core Object Index

**Book Title:** MarkOrbit Core Specification  
**Appendix ID:** B02-APP-C  
**Appendix Title:** Core Object Index  
**Appendix Type:** Canonical Index  
**Rewrite Stage:** Second Canonical Draft  
**Status:** Draft  
**Version:** 0.2.0  
**Owner:** MarkOrbit Publications Editorial Board  

**Related Documents:**

- B02-CH-08 — Ontology and Domain Classification
- B02-CH-13 — Core Domain Architecture
- B02-CH-14 — Core Object Architecture
- B02-CH-23 — Object Specification
- B02-CH-26 — AI Capability and Agent Governance Specification
- B02-CH-27 — Core Consumption Specification
- B02-CH-28 — Core MVP Boundary
- B02-CH-29 — MVP Domain Priority
- B02-CH-30 — MVP Execution Matrix
- B02-APP-A — Glossary
- B02-APP-B — Core Domain Index

---

# 1. Appendix Purpose

This appendix defines the canonical Core Object Index for Book 02.

Appendix B stabilized the Core Domain baseline.

Appendix C stabilizes the Core Object baseline.

A Core Object is not a database table.

A Core Object is not a DTO.

A Core Object is not a product screen record.

A Core Object is professional meaning before data structure.

The purpose of this appendix is to identify the Core Objects that future `core-specs/objects/`, services, events, contracts, APIs, AI agents, Workplaces, products and Codex tasks must reference.

This appendix does not define complete field schemas.

It defines the canonical object list, ownership, MVP depth, consumer usage and governance rules.

---

# 2. Canonical Object Rule

Book 02 uses the following object rule:

```text
Every Core Object must have an owning Core Domain or an explicitly declared cross-cutting specification system.
```

A Core Object must declare:

```text
object name
object purpose
owning domain or cross-cutting system
object category
MVP phase
MVP depth
primary services
primary events
primary contracts
AI usage
workflow usage
product consumers
deferred scope
```

No floating object is allowed.

No product-local duplicate should redefine a Core Object.

No database table should become authoritative before the Core Object is specified.

---

# 3. Object Category Model

Core Objects are grouped into seven categories.

```text
Foundation Objects
Professional Objects
Business Execution Objects
Execution Primitive Objects
Collaboration Network Objects
Contract and Governance Objects
AI Governance Objects
```

These categories help Appendix C prepare:

```text
core-specs/objects/
core-specs/services/
core-specs/events/
core-specs/contracts/
core-specs/api/
core-specs/agents/
Appendix D — Core Service Index
Appendix E — Event Index
Appendix F — API Index
Appendix G — Agent Index
Appendix H — Codex Task Index
```

---

# 4. MVP Depth Types

Each object is tagged with an MVP depth.

```text
Must Implement
Partial Implement
Reserved Boundary
Deferred
```

## 4.1 Must Implement

The object is required for the first executable Core kernel.

## 4.2 Partial Implement

The object must be specified and partially implemented, but not fully automated or fully expanded.

## 4.3 Reserved Boundary

The object must be named and protected, but deep implementation is reserved for later.

## 4.4 Deferred

The object belongs to future releases and must not enter MVP implementation without architecture approval.

---

# 5. Cross-Cutting Object Rule

Capability and Business Responsibility are not baseline Core Domains.

They are cross-cutting Core specification systems.

They may own objects.

Canonical rule:

```text
Capability and Business Responsibility may own cross-cutting Core Objects.
They do not change the 26-domain baseline.
```

Examples:

```text
Capability Object
Capability Provider
Capability Scope
Responsibility Assignment
Review Record
Approval Record
```

---

# 6. Foundation Objects

Foundation Objects support identity, organization, user, permission, policy and knowledge.

---

## 6.1 Identity Object

| Field | Value |
|------|-------|
| Object Name | Identity |
| Owning Domain | Identity |
| Category | Foundation Object |
| Purpose | Defines who or what an actor is in the Core. |
| MVP Phase | Phase 1 — Foundation Core |
| MVP Depth | Must Implement |
| Primary Services | Identity Resolution Service, Identity Verification Service |
| Primary Events | IdentityCreated, IdentityUpdated |
| Primary Contracts | Identity Data Contract, Permission Contract |
| AI Usage | AI Agent Identity depends on Identity. |
| Workflow Usage | Required for actor attribution. |
| Product Consumers | Workplace, MarkReg, MarkOrbit Lite, AI Agents, Codex Implementation |
| Deferred Scope | Advanced identity federation and external identity graph. |

---

## 6.2 Organization Object

| Field | Value |
|------|-------|
| Object Name | Organization |
| Owning Domain | Organization |
| Category | Foundation Object |
| Purpose | Defines business, client, partner or provider entities. |
| MVP Phase | Phase 1 — Foundation Core |
| MVP Depth | Must Implement |
| Primary Services | Organization Registration Service, Organization Profile Update Service |
| Primary Events | OrganizationCreated, OrganizationUpdated |
| Primary Contracts | Organization Data Contract |
| AI Usage | Context for AI recommendations and responsibility. |
| Workflow Usage | Used in customer, user, agent and provider relationships. |
| Product Consumers | Workplace, MarkReg, MarkOrbit Lite, MGSN partial |
| Deferred Scope | Complex organization hierarchy and multi-entity legal graph. |

---

## 6.3 User Object

| Field | Value |
|------|-------|
| Object Name | User |
| Owning Domain | User |
| Category | Foundation Object |
| Purpose | Defines human actors operating inside or through MarkOrbit. |
| MVP Phase | Phase 1 — Foundation Core |
| MVP Depth | Must Implement |
| Primary Services | User Registration Service, User Role Assignment Service |
| Primary Events | UserCreated, UserRoleChanged |
| Primary Contracts | User Data Contract, Permission Contract |
| AI Usage | Provides human reviewer and actor context. |
| Workflow Usage | Required for task assignment and review. |
| Product Consumers | Workplace, MarkReg, MarkOrbit Lite, Codex Implementation |
| Deferred Scope | Advanced user behavior analytics. |

---

## 6.4 Role Object

| Field | Value |
|------|-------|
| Object Name | Role |
| Owning Domain | Permission |
| Category | Foundation Object |
| Purpose | Groups permissions and responsibility expectations for actors. |
| MVP Phase | Phase 1 — Foundation Core |
| MVP Depth | Must Implement |
| Primary Services | Role Assignment Service, Role Permission Service |
| Primary Events | RoleAssigned, RoleUpdated |
| Primary Contracts | Permission Contract |
| AI Usage | Defines whether AI output requires review by role. |
| Workflow Usage | Used in task ownership, review and approval. |
| Product Consumers | Workplace, MarkReg, MarkOrbit Lite |
| Deferred Scope | Dynamic role recommendation. |

---

## 6.5 Permission Rule Object

| Field | Value |
|------|-------|
| Object Name | Permission Rule |
| Owning Domain | Permission |
| Category | Contract and Governance Object |
| Purpose | Defines what actors may read, write, invoke, approve or export. |
| MVP Phase | Phase 1 — Foundation Core |
| MVP Depth | Must Implement |
| Primary Services | Permission Evaluation Service |
| Primary Events | PermissionRuleCreated, PermissionRuleUpdated |
| Primary Contracts | Permission Contract, Data Contract, API Contract |
| AI Usage | Governs AI object and knowledge access. |
| Workflow Usage | Controls workflow actions. |
| Product Consumers | All MVP consumers |
| Deferred Scope | Advanced policy engine and attribute-based permission expansion. |

---

## 6.6 Policy Rule Object

| Field | Value |
|------|-------|
| Object Name | Policy Rule |
| Owning Domain | Policy |
| Category | Contract and Governance Object |
| Purpose | Defines rules that constrain execution, AI, review or data exposure. |
| MVP Phase | Phase 1 — Foundation Core |
| MVP Depth | Partial Implement |
| Primary Services | Policy Evaluation Service |
| Primary Events | PolicyRuleCreated, PolicyRuleUpdated |
| Primary Contracts | Policy Contract |
| AI Usage | Controls risk, review and prohibited AI actions. |
| Workflow Usage | Controls review and approval conditions. |
| Product Consumers | Workplace, AI Agents, Codex Implementation |
| Deferred Scope | Full policy automation and advanced rule authoring. |

---

## 6.7 Knowledge Source Object

| Field | Value |
|------|-------|
| Object Name | Knowledge Source |
| Owning Domain | Knowledge |
| Category | Foundation Object |
| Purpose | Defines the origin of governed knowledge. |
| MVP Phase | Phase 1 — Foundation Core |
| MVP Depth | Must Implement |
| Primary Services | Knowledge Source Registration Service, Knowledge Source Validation Service |
| Primary Events | KnowledgeSourceRegistered, KnowledgeSourceUpdated |
| Primary Contracts | Knowledge Contract, Agent Contract |
| AI Usage | Required for authorized AI knowledge access. |
| Workflow Usage | Supports jurisdiction, classification and document requirement workflows. |
| Product Consumers | MarkOrbit Lite, MarkReg, AI Agents, Workplace |
| Deferred Scope | Automated source monitoring and full knowledge provenance graph. |

---

## 6.8 Knowledge Asset Object

| Field | Value |
|------|-------|
| Object Name | Knowledge Asset |
| Owning Domain | Knowledge |
| Category | Foundation Object |
| Purpose | Defines a governed knowledge item used by humans, services or AI. |
| MVP Phase | Phase 1 — Foundation Core |
| MVP Depth | Must Implement |
| Primary Services | Knowledge Retrieval Service, Knowledge Validation Service |
| Primary Events | KnowledgeAssetCreated, KnowledgeAssetUpdated, KnowledgeAssetValidated |
| Primary Contracts | Knowledge Contract, Agent Contract, Data Contract |
| AI Usage | Primary input for governed AI agents. |
| Workflow Usage | Supports consultation, classification, document and review workflows. |
| Product Consumers | MarkOrbit Lite, MarkReg, AI Agents, Workplace |
| Deferred Scope | Full knowledge lifecycle automation and knowledge conflict resolution. |

---

## 6.9 Knowledge Gap Object

| Field | Value |
|------|-------|
| Object Name | Knowledge Gap |
| Owning Domain | Knowledge |
| Category | Foundation Object |
| Purpose | Records a missing, uncertain or outdated knowledge need. |
| MVP Phase | Phase 1 — Foundation Core |
| MVP Depth | Partial Implement |
| Primary Services | Knowledge Gap Detection Service, Knowledge Review Assignment Service |
| Primary Events | KnowledgeGapIdentified, KnowledgeGapResolved |
| Primary Contracts | Knowledge Contract, Review Contract |
| AI Usage | AI may identify but not resolve knowledge gaps without review. |
| Workflow Usage | Triggers knowledge review tasks. |
| Product Consumers | AI Agents, Workplace, Codex Implementation |
| Deferred Scope | Automated knowledge gap prioritization. |

---

# 7. Professional Objects

Professional Objects represent trademark, brand and document-related professional meaning.

---

## 7.1 Brand Object

| Field | Value |
|------|-------|
| Object Name | Brand |
| Owning Domain | Brand |
| Category | Professional Object |
| Purpose | Defines a business or market-facing identity requiring protection. |
| MVP Phase | Phase 2 — Professional Core |
| MVP Depth | Must Implement |
| Primary Services | Brand Registration Service, Brand Context Service |
| Primary Events | BrandCreated, BrandUpdated |
| Primary Contracts | Brand Data Contract |
| AI Usage | Used for filing recommendations and portfolio suggestions. |
| Workflow Usage | Links customer intention to trademark work. |
| Product Consumers | MarkOrbit Lite, MarkReg, Brand Asset Vault baseline |
| Deferred Scope | Full Brand Asset Vault and portfolio valuation. |

---

## 7.2 Brand Asset Object

| Field | Value |
|------|-------|
| Object Name | Brand Asset |
| Owning Domain | Brand |
| Category | Professional Object |
| Purpose | Represents logo, word mark, design mark, packaging, slogan or other brand-related asset. |
| MVP Phase | Phase 2 — Professional Core |
| MVP Depth | Partial Implement |
| Primary Services | Brand Asset Upload Service, Brand Asset Classification Service |
| Primary Events | BrandAssetUploaded, BrandAssetUpdated |
| Primary Contracts | Document/Data Contract |
| AI Usage | AI may summarize or classify assets under review. |
| Workflow Usage | Supports intake and trademark preparation. |
| Product Consumers | MarkOrbit Lite, MarkReg, Brand Asset Vault baseline |
| Deferred Scope | Full brand asset vault, asset history and portfolio analytics. |

---

## 7.3 Trademark Object

| Field | Value |
|------|-------|
| Object Name | Trademark |
| Owning Domain | Trademark |
| Category | Professional Object |
| Purpose | Defines mark-related professional meaning and lifecycle. |
| MVP Phase | Phase 2 — Professional Core |
| MVP Depth | Must Implement |
| Primary Services | Trademark Creation Service, Trademark Status Normalization Service |
| Primary Events | TrademarkCreated, TrademarkStatusChanged, TrademarkUpdated |
| Primary Contracts | Trademark Data Contract, Event Contract |
| AI Usage | AI may summarize status or recommend actions under review. |
| Workflow Usage | Central object for orders, matters, documents and deadlines. |
| Product Consumers | MarkReg, MarkOrbit Lite, Workplace, AI Agents |
| Deferred Scope | Full portfolio analytics and global status automation. |

---

## 7.4 Mark Representation Object

| Field | Value |
|------|-------|
| Object Name | Mark Representation |
| Owning Domain | Trademark |
| Category | Professional Object |
| Purpose | Defines visual, text, design or combined representation of a mark. |
| MVP Phase | Phase 2 — Professional Core |
| MVP Depth | Must Implement |
| Primary Services | Mark Representation Validation Service |
| Primary Events | MarkRepresentationAdded, MarkRepresentationUpdated |
| Primary Contracts | Trademark Data Contract, Document Contract |
| AI Usage | AI may assist with description or similarity context, not final legal judgment. |
| Workflow Usage | Supports filing intake and document generation. |
| Product Consumers | MarkReg, MarkOrbit Lite, AI Agents |
| Deferred Scope | Advanced image similarity and design-element detection. |

---

## 7.5 Jurisdiction Object

| Field | Value |
|------|-------|
| Object Name | Jurisdiction |
| Owning Domain | Jurisdiction |
| Category | Professional Object |
| Purpose | Defines country, region or office-specific professional context. |
| MVP Phase | Phase 2 — Professional Core |
| MVP Depth | Must Implement |
| Primary Services | Jurisdiction Lookup Service, Jurisdiction Requirement Service |
| Primary Events | JurisdictionRuleUpdated |
| Primary Contracts | Jurisdiction Data Contract, Knowledge Contract |
| AI Usage | Used by AI for country-specific recommendation context. |
| Workflow Usage | Controls requirements, documents, classification and routing. |
| Product Consumers | MarkReg, MarkOrbit Lite, AI Agents, Routing partial |
| Deferred Scope | Full automated office rule monitoring. |

---

## 7.6 Jurisdiction Requirement Object

| Field | Value |
|------|-------|
| Object Name | Jurisdiction Requirement |
| Owning Domain | Jurisdiction |
| Category | Professional Object |
| Purpose | Defines filing, document, applicant or procedural requirements by jurisdiction. |
| MVP Phase | Phase 2 — Professional Core |
| MVP Depth | Must Implement |
| Primary Services | Requirement Retrieval Service, Requirement Validation Service |
| Primary Events | JurisdictionRequirementUpdated |
| Primary Contracts | Knowledge Contract, API Contract |
| AI Usage | AI may retrieve and summarize requirements with source grounding. |
| Workflow Usage | Supports intake, document checklist and matter preparation. |
| Product Consumers | MarkReg, MarkOrbit Lite, AI Agents |
| Deferred Scope | Full official-rule versioning and automated regulatory change alerts. |

---

## 7.7 Classification Object

| Field | Value |
|------|-------|
| Object Name | Classification |
| Owning Domain | Classification |
| Category | Professional Object |
| Purpose | Defines goods/services classification context and recommendation meaning. |
| MVP Phase | Phase 2 — Professional Core |
| MVP Depth | Must Implement |
| Primary Services | Classification Recommendation Service, Classification Validation Service |
| Primary Events | ClassificationRecommendationGenerated, ClassificationApproved |
| Primary Contracts | Classification Data Contract, AI Agent Contract |
| AI Usage | AI may recommend but review may be required. |
| Workflow Usage | Supports guided intake, filing preparation and review. |
| Product Consumers | MarkOrbit Lite, MarkReg, AI Agents |
| Deferred Scope | Full multi-jurisdiction classification optimization. |

---

## 7.8 Goods and Services Item Object

| Field | Value |
|------|-------|
| Object Name | Goods and Services Item |
| Owning Domain | Classification |
| Category | Professional Object |
| Purpose | Defines an individual goods/services term with classification context. |
| MVP Phase | Phase 2 — Professional Core |
| MVP Depth | Must Implement |
| Primary Services | Goods Term Selection Service, Goods Term Validation Service |
| Primary Events | GoodsServicesItemSelected, GoodsServicesItemValidated |
| Primary Contracts | Classification Data Contract |
| AI Usage | AI may recommend candidate terms under validation. |
| Workflow Usage | Used in intake, application preparation and review. |
| Product Consumers | MarkOrbit Lite, MarkReg, AI Agents |
| Deferred Scope | Advanced local sub-class conflict optimization. |

---

## 7.9 Document Object

| Field | Value |
|------|-------|
| Object Name | Document |
| Owning Domain | Document |
| Category | Professional Object |
| Purpose | Defines professional files, generated materials and official documents. |
| MVP Phase | Phase 2 — Professional Core |
| MVP Depth | Must Implement |
| Primary Services | Document Upload Service, Document Generation Service, Document Validation Service |
| Primary Events | DocumentUploaded, DocumentGenerated, DocumentValidated |
| Primary Contracts | Document Data Contract, Export Contract |
| AI Usage | AI may draft, summarize or classify documents under rules. |
| Workflow Usage | Supports application, OA response, evidence and communication. |
| Product Consumers | MarkReg, MarkOrbit Lite, Workplace, AI Agents |
| Deferred Scope | Full document automation, signing and template marketplace. |

---

## 7.10 Document Requirement Object

| Field | Value |
|------|-------|
| Object Name | Document Requirement |
| Owning Domain | Document |
| Category | Professional Object |
| Purpose | Defines required materials for a jurisdiction, service or workflow. |
| MVP Phase | Phase 2 — Professional Core |
| MVP Depth | Must Implement |
| Primary Services | Document Requirement Service, Requirement Checklist Service |
| Primary Events | DocumentRequirementGenerated, DocumentRequirementSatisfied |
| Primary Contracts | Jurisdiction Requirement Contract, Document Contract |
| AI Usage | AI may explain requirements but must reference authorized knowledge. |
| Workflow Usage | Supports intake checklist and matter readiness. |
| Product Consumers | MarkOrbit Lite, MarkReg, AI Agents |
| Deferred Scope | Fully automated requirement tracking across jurisdictions. |

---

## 7.11 Evidence Object

| Field | Value |
|------|-------|
| Object Name | Evidence |
| Owning Domain | Evidence |
| Category | Professional Object |
| Purpose | Defines proof materials used in professional claims, filings or disputes. |
| MVP Phase | Phase 2 — Professional Core |
| MVP Depth | Partial Implement |
| Primary Services | Evidence Upload Service, Evidence Review Service |
| Primary Events | EvidenceUploaded, EvidenceReviewRequired, EvidenceReviewed |
| Primary Contracts | Evidence Data Contract, Review Contract |
| AI Usage | AI may organize or summarize evidence, not validate legal sufficiency alone. |
| Workflow Usage | Supports OA, opposition, cancellation and use-declaration workflows. |
| Product Consumers | MarkReg, Workplace, AI Agents |
| Deferred Scope | Advanced evidence scoring and automated evidence package assembly. |

---

## 7.12 Evidence Package Object

| Field | Value |
|------|-------|
| Object Name | Evidence Package |
| Owning Domain | Evidence |
| Category | Professional Object |
| Purpose | Groups evidence items for a professional purpose or filing. |
| MVP Phase | Phase 2 — Professional Core |
| MVP Depth | Partial Implement |
| Primary Services | Evidence Package Assembly Service, Evidence Package Review Service |
| Primary Events | EvidencePackageCreated, EvidencePackageReviewRequired |
| Primary Contracts | Evidence Contract, Review Contract |
| AI Usage | AI may suggest grouping but review is required. |
| Workflow Usage | Used in high-risk professional tasks. |
| Product Consumers | MarkReg, Workplace, AI Agents |
| Deferred Scope | Automated evidence scoring and jurisdiction-specific packaging. |

---

# 8. Business Execution Objects

Business Execution Objects convert professional meaning into managed work.

---

## 8.1 Customer Object

| Field | Value |
|------|-------|
| Object Name | Customer |
| Owning Domain | Customer |
| Category | Business Execution Object |
| Purpose | Defines the service recipient or client relationship in Core execution. |
| MVP Phase | Phase 3 — Business Execution Core |
| MVP Depth | Must Implement |
| Primary Services | Customer Registration Service, Customer Profile Service |
| Primary Events | CustomerCreated, CustomerUpdated |
| Primary Contracts | Customer Data Contract |
| AI Usage | Used as context for recommendations and service history. |
| Workflow Usage | Links intake, orders, matters and communications. |
| Product Consumers | MarkReg, MarkOrbit Lite, Workplace |
| Deferred Scope | Full CRM automation and customer scoring. |

---

## 8.2 Customer Contact Object

| Field | Value |
|------|-------|
| Object Name | Customer Contact |
| Owning Domain | Customer |
| Category | Business Execution Object |
| Purpose | Defines contact person and communication details for a customer. |
| MVP Phase | Phase 3 — Business Execution Core |
| MVP Depth | Must Implement |
| Primary Services | Contact Registration Service, Contact Update Service |
| Primary Events | CustomerContactCreated, CustomerContactUpdated |
| Primary Contracts | Customer Data Contract, Communication Contract |
| AI Usage | Used for communication summary context. |
| Workflow Usage | Supports order, matter and communication workflows. |
| Product Consumers | MarkReg, MarkOrbit Lite, Workplace |
| Deferred Scope | Full contact relationship graph. |

---

## 8.3 Order Object

| Field | Value |
|------|-------|
| Object Name | Order |
| Owning Domain | Order |
| Category | Business Execution Object |
| Purpose | Defines a service request or confirmed service commitment. |
| MVP Phase | Phase 3 — Business Execution Core |
| MVP Depth | Must Implement |
| Primary Services | Order Creation Service, Order Confirmation Service, Order-to-Matter Conversion Service |
| Primary Events | OrderCreated, OrderConfirmed, OrderConvertedToMatter |
| Primary Contracts | Order Data Contract, Workflow Contract |
| AI Usage | AI may assist intake completion and requirement explanation. |
| Workflow Usage | Connects intake to professional execution. |
| Product Consumers | MarkOrbit Lite, MarkReg, Workplace |
| Deferred Scope | Advanced pricing and commercial policy automation. |

---

## 8.4 Matter Object

| Field | Value |
|------|-------|
| Object Name | Matter |
| Owning Domain | Matter |
| Category | Business Execution Object |
| Purpose | Defines a managed professional service case. |
| MVP Phase | Phase 3 — Business Execution Core |
| MVP Depth | Must Implement |
| Primary Services | Matter Creation Service, Matter Status Service, Matter Assignment Service |
| Primary Events | MatterCreated, MatterStatusChanged, MatterAssigned |
| Primary Contracts | Matter Data Contract, Workflow Contract, Event Contract |
| AI Usage | AI may summarize matter context or recommend next actions under review. |
| Workflow Usage | Central object for Workplace execution. |
| Product Consumers | MarkReg, Workplace, AI Agents |
| Deferred Scope | Advanced matter profitability and predictive workflow analytics. |

---

## 8.5 Opportunity Object

| Field | Value |
|------|-------|
| Object Name | Opportunity |
| Owning Domain | Opportunity |
| Category | Business Execution Object |
| Purpose | Defines a potential business follow-up, service need or growth signal. |
| MVP Phase | Phase 4 — Growth Core Baseline |
| MVP Depth | Partial Implement |
| Primary Services | Opportunity Discovery Service, Opportunity Review Service |
| Primary Events | OpportunityCreated, OpportunityReviewRequired |
| Primary Contracts | Opportunity Data Contract, AI Agent Contract |
| AI Usage | AI may discover or suggest opportunities; human review required. |
| Workflow Usage | Supports sales follow-up and client service expansion. |
| Product Consumers | Opportunity Engine baseline, MarkReg, AI Agents |
| Deferred Scope | Full opportunity scoring, automation and revenue attribution. |

---

## 8.6 Workflow Contract Object

| Field | Value |
|------|-------|
| Object Name | Workflow Contract |
| Owning Domain | Workflow Contract |
| Category | Execution Primitive Object |
| Purpose | Defines allowed states, transitions, actors and review requirements. |
| MVP Phase | Phase 3 — Business Execution Core |
| MVP Depth | Must Implement |
| Primary Services | Workflow Validation Service, Workflow Transition Service |
| Primary Events | WorkflowTransitionRequested, WorkflowTransitionCompleted |
| Primary Contracts | Workflow Contract |
| AI Usage | AI may recommend transitions but not bypass rules. |
| Workflow Usage | Defines workflow usage itself. |
| Product Consumers | Workplace, MarkReg, MarkOrbit Lite, Codex Implementation |
| Deferred Scope | Full visual workflow designer and dynamic workflow engine. |

---

## 8.7 Task Object

| Field | Value |
|------|-------|
| Object Name | Task |
| Owning Domain | Task |
| Category | Execution Primitive Object |
| Purpose | Defines a unit of work to be assigned, performed, reviewed or completed. |
| MVP Phase | Phase 3 — Business Execution Core |
| MVP Depth | Must Implement |
| Primary Services | Task Creation Service, Task Assignment Service, Task Completion Service |
| Primary Events | TaskCreated, TaskAssigned, TaskCompleted, TaskOverdue |
| Primary Contracts | Task Data Contract, Workflow Contract |
| AI Usage | AI may suggest tasks or summarize task context. |
| Workflow Usage | Central execution primitive for Workplace. |
| Product Consumers | Workplace, MarkReg, AI Agents |
| Deferred Scope | Advanced task optimization and workload balancing. |

---

## 8.8 Event Record Object

| Field | Value |
|------|-------|
| Object Name | Event Record |
| Owning Domain | Event |
| Category | Execution Primitive Object |
| Purpose | Records a meaningful Core Event occurrence. |
| MVP Phase | Phase 3 — Business Execution Core |
| MVP Depth | Must Implement |
| Primary Services | Event Publishing Service, Event Subscription Service |
| Primary Events | EventPublished, EventConsumed |
| Primary Contracts | Event Contract |
| AI Usage | AI events must produce Event Records where required. |
| Workflow Usage | Coordinates downstream execution and audit. |
| Product Consumers | Workplace, MarkReg, AI Agents, Codex Implementation |
| Deferred Scope | Advanced replay, stream processing and analytics integration. |

---

## 8.9 Notification Object

| Field | Value |
|------|-------|
| Object Name | Notification |
| Owning Domain | Notification |
| Category | Execution Primitive Object |
| Purpose | Defines alerts or messages triggered by execution events. |
| MVP Phase | Phase 3 — Business Execution Core |
| MVP Depth | Partial Implement |
| Primary Services | Notification Dispatch Service, Notification Preference Service |
| Primary Events | NotificationCreated, NotificationSent |
| Primary Contracts | Notification Contract |
| AI Usage | AI may suggest notification content with controls. |
| Workflow Usage | Supports task, review and deadline awareness. |
| Product Consumers | Workplace, MarkReg, MarkOrbit Lite |
| Deferred Scope | Full multi-channel notification preference automation. |

---

# 9. Collaboration Network Objects

Collaboration Network Objects support agent, provider, routing and communication foundations.

---

## 9.1 Partner Object

| Field | Value |
|------|-------|
| Object Name | Partner |
| Owning Domain | Partner |
| Category | Collaboration Network Object |
| Purpose | Defines a business partner or channel participant. |
| MVP Phase | Phase 5 — Network Reserved |
| MVP Depth | Reserved Boundary |
| Primary Services | Partner Registration Service |
| Primary Events | PartnerCreated |
| Primary Contracts | Partner Data Contract |
| AI Usage | Reserved. |
| Workflow Usage | Future partner workflow. |
| Product Consumers | Future Partner Center, MGSN |
| Deferred Scope | Full partner center, rebate, channel operations. |

---

## 9.2 Agent Object

| Field | Value |
|------|-------|
| Object Name | Agent |
| Owning Domain | Agent |
| Category | Collaboration Network Object |
| Purpose | Defines a professional agent or law firm used in service execution. |
| MVP Phase | Phase 4 — Growth Core Baseline |
| MVP Depth | Partial Implement |
| Primary Services | Agent Registration Service, Agent Lookup Service |
| Primary Events | AgentCreated, AgentUpdated |
| Primary Contracts | Agent Data Contract, Communication Contract |
| AI Usage | AI may summarize agent capabilities with verified data. |
| Workflow Usage | Supports routing and communication. |
| Product Consumers | MarkReg, MGSN partial, Routing, Workplace |
| Deferred Scope | Full agent marketplace and trust scoring. |

---

## 9.3 Service Provider Object

| Field | Value |
|------|-------|
| Object Name | Service Provider |
| Owning Domain | Service Provider |
| Category | Collaboration Network Object |
| Purpose | Defines an entity providing professional, technical or supporting services. |
| MVP Phase | Phase 4 — Growth Core Baseline |
| MVP Depth | Partial Implement |
| Primary Services | Service Provider Registration Service, Provider Capability Service |
| Primary Events | ServiceProviderCreated, ServiceProviderUpdated |
| Primary Contracts | Service Provider Contract, Capability Contract |
| AI Usage | AI may support provider matching under review. |
| Workflow Usage | Supports routing and procurement-like workflows. |
| Product Consumers | MGSN partial, MarkReg, Routing |
| Deferred Scope | Full provider marketplace and service exchange. |

---

## 9.4 Service Network Object

| Field | Value |
|------|-------|
| Object Name | Service Network |
| Owning Domain | Service Network |
| Category | Collaboration Network Object |
| Purpose | Defines the network-level structure connecting providers and participants. |
| MVP Phase | Phase 5 — Network Reserved |
| MVP Depth | Reserved Boundary |
| Primary Services | Service Network Registration Service |
| Primary Events | ServiceNetworkCreated |
| Primary Contracts | Network Contract |
| AI Usage | Reserved. |
| Workflow Usage | Future network operation. |
| Product Consumers | MGSN future |
| Deferred Scope | Full Mark Global Service Network operation. |

---

## 9.5 Routing Decision Object

| Field | Value |
|------|-------|
| Object Name | Routing Decision |
| Owning Domain | Routing |
| Category | Collaboration Network Object |
| Purpose | Defines a decision or recommendation to route work to an actor, agent or provider. |
| MVP Phase | Phase 4 — Growth Core Baseline |
| MVP Depth | Partial Implement |
| Primary Services | Routing Recommendation Service, Routing Approval Service |
| Primary Events | RoutingRecommendationGenerated, RoutingDecisionMade |
| Primary Contracts | Routing Contract, Responsibility Contract, AI Agent Contract |
| AI Usage | AI may recommend routing; review may be required. |
| Workflow Usage | Supports matter, task and agent assignment. |
| Product Consumers | MarkReg, MGSN partial, Workplace, AI Agents |
| Deferred Scope | Advanced routing optimization and provider ranking. |

---

## 9.6 Communication Object

| Field | Value |
|------|-------|
| Object Name | Communication |
| Owning Domain | Communication |
| Category | Collaboration Network Object |
| Purpose | Defines linked professional communication records. |
| MVP Phase | Phase 4 — Growth Core Baseline |
| MVP Depth | Partial Implement |
| Primary Services | Communication Link Service, Communication Summary Service |
| Primary Events | CommunicationLinked, CommunicationSummaryGenerated |
| Primary Contracts | Communication Contract, Data Contract |
| AI Usage | AI may summarize or classify communication under access rules. |
| Workflow Usage | Supports matters, tasks, agent communication and customer updates. |
| Product Consumers | MarkReg, Workplace, AI Agents, MGSN partial |
| Deferred Scope | Full email/chat/call integration and conversation intelligence. |

---

# 10. Contract and Governance Objects

Contract and Governance Objects protect Core meaning and consumption.

---

## 10.1 Data Contract Object

| Field | Value |
|------|-------|
| Object Name | Data Contract |
| Owning System | Core Contract Architecture |
| Category | Contract and Governance Object |
| Purpose | Defines what data may be read, exposed, exported or consumed. |
| MVP Phase | Phase 3 — Business Execution Core |
| MVP Depth | Must Implement |
| Primary Services | Data Contract Validation Service |
| Primary Events | DataContractCreated, DataContractUpdated |
| Primary Contracts | Contract Specification |
| AI Usage | Controls AI object and field access. |
| Workflow Usage | Supports product and reporting consumption. |
| Product Consumers | All consumers |
| Deferred Scope | Advanced data marketplace and external developer data products. |

---

## 10.2 API Contract Object

| Field | Value |
|------|-------|
| Object Name | API Contract |
| Owning System | Core Contract Architecture |
| Category | Contract and Governance Object |
| Purpose | Defines API input, output, permissions, side effects and consumers. |
| MVP Phase | Phase 3 — Business Execution Core |
| MVP Depth | Must Implement |
| Primary Services | API Contract Validation Service |
| Primary Events | APIContractCreated, APIContractUpdated |
| Primary Contracts | API Contract |
| AI Usage | Governs AI invocation endpoints where exposed. |
| Workflow Usage | Controls API-driven workflow actions. |
| Product Consumers | MarkReg, MarkOrbit Lite, Workplace, Codex Implementation |
| Deferred Scope | Public developer API and full webhook platform. |

---

## 10.3 Event Contract Object

| Field | Value |
|------|-------|
| Object Name | Event Contract |
| Owning System | Core Contract Architecture |
| Category | Contract and Governance Object |
| Purpose | Defines event payload, source, timing, consumers and retention. |
| MVP Phase | Phase 3 — Business Execution Core |
| MVP Depth | Must Implement |
| Primary Services | Event Contract Validation Service |
| Primary Events | EventContractCreated, EventContractUpdated |
| Primary Contracts | Event Contract |
| AI Usage | Governs AI-related events. |
| Workflow Usage | Supports event-driven coordination. |
| Product Consumers | Workplace, MarkReg, AI Agents, Codex Implementation |
| Deferred Scope | Advanced event replay and third-party webhook event products. |

---

## 10.4 Consumption Contract Object

| Field | Value |
|------|-------|
| Object Name | Consumption Contract |
| Owning System | Core Consumption Specification |
| Category | Contract and Governance Object |
| Purpose | Defines how a product, Workplace, AI agent, integration or Codex task consumes Core. |
| MVP Phase | Phase 3 — Business Execution Core |
| MVP Depth | Must Implement |
| Primary Services | Consumption Review Service |
| Primary Events | ConsumptionContractCreated, ConsumptionContractUpdated |
| Primary Contracts | Consumption Contract |
| AI Usage | Required for AI consumer binding. |
| Workflow Usage | Supports product consumption governance. |
| Product Consumers | MarkReg, MarkOrbit Lite, Workplace, Codex Implementation |
| Deferred Scope | Full external consumption marketplace. |

---

## 10.5 Responsibility Assignment Object

| Field | Value |
|------|-------|
| Object Name | Responsibility Assignment |
| Owning System | Business Responsibility |
| Category | Contract and Governance Object |
| Purpose | Defines who is accountable for work, review, approval or follow-up. |
| MVP Phase | Phase 3 — Business Execution Core |
| MVP Depth | Partial Implement |
| Primary Services | Responsibility Assignment Service, Responsibility Transfer Service |
| Primary Events | ResponsibilityAssigned, ResponsibilityTransferred |
| Primary Contracts | Responsibility Contract |
| AI Usage | AI cannot own responsibility; AI output must be assigned to human/system responsibility where needed. |
| Workflow Usage | Used in task, matter, review and routing workflows. |
| Product Consumers | Workplace, MarkReg, AI Agents |
| Deferred Scope | Advanced responsibility analytics and workload optimization. |

---

## 10.6 Review Record Object

| Field | Value |
|------|-------|
| Object Name | Review Record |
| Owning System | Business Responsibility |
| Category | Contract and Governance Object |
| Purpose | Records review requirement, reviewer action and review outcome. |
| MVP Phase | Phase 3 — Business Execution Core |
| MVP Depth | Partial Implement |
| Primary Services | Review Request Service, Review Approval Service, Review Rejection Service |
| Primary Events | ReviewRequired, ReviewApproved, ReviewRejected |
| Primary Contracts | Review Contract, Responsibility Contract |
| AI Usage | Required for AI output review. |
| Workflow Usage | Central to human-in-the-loop execution. |
| Product Consumers | Workplace, MarkReg, AI Agents |
| Deferred Scope | Advanced review queue optimization. |

---

## 10.7 Capability Object

| Field | Value |
|------|-------|
| Object Name | Capability |
| Owning System | Capability |
| Category | Contract and Governance Object |
| Purpose | Defines what can be performed by an actor, service, agent or provider. |
| MVP Phase | Phase 1 — Foundation Core |
| MVP Depth | Partial Implement |
| Primary Services | Capability Registration Service, Capability Matching Service |
| Primary Events | CapabilityRegistered, CapabilityMatched |
| Primary Contracts | Capability Contract |
| AI Usage | Defines allowed AI capabilities. |
| Workflow Usage | Supports routing, assignment and service eligibility. |
| Product Consumers | Workplace, MarkReg, MarkOrbit Lite, MGSN partial |
| Deferred Scope | Full capability marketplace and dynamic matching. |

---

## 10.8 Capability Provider Object

| Field | Value |
|------|-------|
| Object Name | Capability Provider |
| Owning System | Capability |
| Category | Contract and Governance Object |
| Purpose | Links a capability to a user, AI agent, organization, agent or service provider. |
| MVP Phase | Phase 1 — Foundation Core |
| MVP Depth | Partial Implement |
| Primary Services | Capability Provider Registration Service |
| Primary Events | CapabilityProviderRegistered, CapabilityProviderUpdated |
| Primary Contracts | Capability Contract |
| AI Usage | Defines AI Agent capability scope. |
| Workflow Usage | Supports assignment and routing. |
| Product Consumers | Workplace, MarkReg, MGSN partial, AI Agents |
| Deferred Scope | Automated provider scoring and dynamic routing. |

---

# 11. AI Governance Objects

AI Governance Objects ensure AI is a governed capability, not autonomous Core authority.

---

## 11.1 AI Agent Object

| Field | Value |
|------|-------|
| Object Name | AI Agent |
| Owning System | AI Governance |
| Category | AI Governance Object |
| Purpose | Defines a governed AI actor with identity, capability and contract. |
| MVP Phase | Phase 4 — AI Governance and Review |
| MVP Depth | Must Implement |
| Primary Services | AI Agent Registration Service, AI Agent Invocation Service |
| Primary Events | AIAgentRegistered, AIAgentInvoked |
| Primary Contracts | Agent Contract, Permission Contract |
| AI Usage | Defines AI actor itself. |
| Workflow Usage | Used in AI-assisted workflows and review paths. |
| Product Consumers | AI Agents, MarkOrbit Lite, MarkReg, Workplace, Codex Implementation |
| Deferred Scope | Multi-agent orchestration and autonomous planning. |

---

## 11.2 Agent Contract Object

| Field | Value |
|------|-------|
| Object Name | Agent Contract |
| Owning System | AI Governance / Core Contract Architecture |
| Category | AI Governance Object |
| Purpose | Defines what an AI Agent may access, do, produce and not do. |
| MVP Phase | Phase 4 — AI Governance and Review |
| MVP Depth | Must Implement |
| Primary Services | Agent Contract Validation Service |
| Primary Events | AgentContractCreated, AgentContractUpdated |
| Primary Contracts | Agent Contract |
| AI Usage | Mandatory for every AI Agent. |
| Workflow Usage | Controls AI participation in workflows. |
| Product Consumers | AI Agents, MarkOrbit Lite, MarkReg, Workplace, Codex Implementation |
| Deferred Scope | Dynamic contract generation and multi-agent delegation rules. |

---

## 11.3 AI Capability Object

| Field | Value |
|------|-------|
| Object Name | AI Capability |
| Owning System | AI Governance / Capability |
| Category | AI Governance Object |
| Purpose | Defines a governed capability available to an AI Agent. |
| MVP Phase | Phase 4 — AI Governance and Review |
| MVP Depth | Must Implement |
| Primary Services | AI Capability Registry Service, AI Capability Authorization Service |
| Primary Events | AICapabilityRegistered, AICapabilityAuthorized |
| Primary Contracts | Capability Contract, Agent Contract |
| AI Usage | Defines AI allowed actions. |
| Workflow Usage | Supports AI-assisted workflow tasks. |
| Product Consumers | AI Agents, MarkOrbit Lite, MarkReg, Workplace |
| Deferred Scope | Advanced capability scoring and tool marketplace. |

---

## 11.4 AI Output Object

| Field | Value |
|------|-------|
| Object Name | AI Output |
| Owning System | AI Governance |
| Category | AI Governance Object |
| Purpose | Defines any controlled output produced by an AI Agent. |
| MVP Phase | Phase 4 — AI Governance and Review |
| MVP Depth | Must Implement |
| Primary Services | AI Output Creation Service, AI Output Review Service |
| Primary Events | AIOutputGenerated, AIOutputReviewRequired, AIOutputApproved, AIOutputRejected |
| Primary Contracts | Agent Contract, Review Contract |
| AI Usage | Records AI-produced content or results. |
| Workflow Usage | Enables review, approval and audit workflows. |
| Product Consumers | MarkOrbit Lite, MarkReg, Workplace, AI Agents |
| Deferred Scope | Advanced output quality scoring and long-term learning loops. |

---

## 11.5 AI Recommendation Object

| Field | Value |
|------|-------|
| Object Name | AI Recommendation |
| Owning System | AI Governance |
| Category | AI Governance Object |
| Purpose | Defines a recommendation produced by AI for professional or operational use. |
| MVP Phase | Phase 4 — AI Governance and Review |
| MVP Depth | Must Implement |
| Primary Services | AI Recommendation Service, Recommendation Review Service |
| Primary Events | AIRecommendationGenerated, AIRecommendationReviewRequired, AIRecommendationApproved, AIRecommendationRejected |
| Primary Contracts | Agent Contract, Review Contract, Event Contract |
| AI Usage | Central AI recommendation object. |
| Workflow Usage | Requires review depending on risk. |
| Product Consumers | MarkOrbit Lite, MarkReg, Workplace, AI Agents |
| Deferred Scope | Advanced recommendation ranking and feedback learning. |

---

## 11.6 AI Audit Record Object

| Field | Value |
|------|-------|
| Object Name | AI Audit Record |
| Owning System | AI Governance |
| Category | AI Governance Object |
| Purpose | Records AI invocation, context, output, review and risk trace. |
| MVP Phase | Phase 4 — AI Governance and Review |
| MVP Depth | Must Implement |
| Primary Services | AI Audit Logging Service, AI Audit Review Service |
| Primary Events | AIAuditRecordCreated, AIAuditReviewed |
| Primary Contracts | Agent Contract, Audit Contract, Data Contract |
| AI Usage | Required for governed AI execution. |
| Workflow Usage | Supports review, compliance and debugging. |
| Product Consumers | Workplace, AI Agents, Codex Implementation |
| Deferred Scope | Advanced model evaluation, quality analytics and continuous improvement. |

---

## 11.7 Structured Context Object

| Field | Value |
|------|-------|
| Object Name | Structured Context |
| Owning System | AI Governance / Knowledge |
| Category | AI Governance Object |
| Purpose | Defines the approved context package provided to AI Agents. |
| MVP Phase | Phase 4 — AI Governance and Review |
| MVP Depth | Must Implement |
| Primary Services | Context Assembly Service, Context Validation Service |
| Primary Events | StructuredContextCreated, StructuredContextValidated |
| Primary Contracts | Agent Contract, Knowledge Contract, Data Contract |
| AI Usage | Required for AI invocation. |
| Workflow Usage | Supports AI-assisted review, drafting and recommendation. |
| Product Consumers | AI Agents, MarkOrbit Lite, MarkReg, Workplace |
| Deferred Scope | Advanced context optimization and retrieval orchestration. |

---

## 11.8 Human Review Requirement Object

| Field | Value |
|------|-------|
| Object Name | Human Review Requirement |
| Owning System | AI Governance / Business Responsibility |
| Category | AI Governance Object |
| Purpose | Defines when human review is required for AI or automated output. |
| MVP Phase | Phase 4 — AI Governance and Review |
| MVP Depth | Must Implement |
| Primary Services | Review Requirement Evaluation Service |
| Primary Events | HumanReviewRequired |
| Primary Contracts | Agent Contract, Review Contract, Responsibility Contract |
| AI Usage | Required for risk-governed AI. |
| Workflow Usage | Creates review tasks and approval gates. |
| Product Consumers | Workplace, MarkReg, MarkOrbit Lite, AI Agents |
| Deferred Scope | Advanced risk scoring and dynamic review routing. |

---

# 12. Object Index Summary by MVP Depth

## 12.1 Must Implement Objects

```text
Identity
Organization
User
Role
Permission Rule
Knowledge Source
Knowledge Asset
Brand
Trademark
Mark Representation
Jurisdiction
Jurisdiction Requirement
Classification
Goods and Services Item
Document
Document Requirement
Customer
Customer Contact
Order
Matter
Workflow Contract
Task
Event Record
Data Contract
API Contract
Event Contract
Consumption Contract
AI Agent
Agent Contract
AI Capability
AI Output
AI Recommendation
AI Audit Record
Structured Context
Human Review Requirement
```

## 12.2 Partial Implement Objects

```text
Policy Rule
Knowledge Gap
Brand Asset
Evidence
Evidence Package
Opportunity
Notification
Agent
Service Provider
Routing Decision
Communication
Responsibility Assignment
Review Record
Capability
Capability Provider
```

## 12.3 Reserved Boundary Objects

```text
Partner
Service Network
```

## 12.4 Deferred Object Scope

```text
advanced identity graph
full organization legal graph
full Brand Asset Vault
advanced evidence scoring
full CRM automation
full opportunity scoring
full global agent marketplace
full provider ranking
full service network operation
public developer API object products
advanced AI multi-agent orchestration
```

---

# 13. Object-to-Appendix H Handoff

Appendix H — Codex Task Index must use this object index to define implementation tasks.

Codex tasks must not create object names outside Appendix C unless the task explicitly records:

```text
architecture issue
object owner proposal
appendix update requirement
core-specs update requirement
acceptance criteria
```

---

# 14. Relationship to core-specs/objects/

Future `core-specs/objects/` files should be generated from this appendix.

Each object spec should include:

```text
Object Name
Object ID
Owning Domain or System
Object Category
Purpose
Core Definition
Identity Rule
Lifecycle Rule
Relationship Rule
Conceptual Field Groups
State Model
Permission Rule
Policy Rule
Audit Rule
Related Services
Source Events
Consumed Events
Contracts
AI Usage
Workflow Usage
Product Consumers
MVP Phase
MVP Depth
Deferred Scope
Acceptance Criteria
Revision Notes
```

---

# 15. Object Anti-Patterns

The following patterns are prohibited.

## 15.1 Database Table as Object Definition

A database table defines object meaning.

Correction:

```text
Object Specification defines meaning before schema authority.
```

## 15.2 Product Screen Record as Object

A UI view is treated as the Core Object.

Correction:

```text
Product screens consume Core Objects.
```

## 15.3 Floating Object

An object has no owning domain or cross-cutting system.

Correction:

```text
Every object must declare ownership.
```

## 15.4 AI Output Without Review or Audit

AI output exists without status, review rule or audit record.

Correction:

```text
AI Output, AI Recommendation and AI Audit Record must be governed objects.
```

## 15.5 Contractless Object Consumption

A consumer reads or writes object data without a contract.

Correction:

```text
Use Data Contract, API Contract, Agent Contract or Consumption Contract.
```

---

# 16. Acceptance Criteria

Appendix C is accepted only if it satisfies the following criteria.

```text
[ ] It defines Core Object as professional meaning before data structure.
[ ] It maps each object to an owning domain or cross-cutting system.
[ ] It includes Foundation Objects.
[ ] It includes Professional Objects.
[ ] It includes Business Execution Objects.
[ ] It includes Execution Primitive Objects.
[ ] It includes Collaboration Network Objects.
[ ] It includes Contract and Governance Objects.
[ ] It includes AI Governance Objects.
[ ] It includes AI Agent, AI Capability, AI Output, AI Recommendation and AI Audit Record.
[ ] It includes Responsibility Assignment and Review Record.
[ ] It preserves the 26-domain baseline.
[ ] It clarifies Capability and Business Responsibility as cross-cutting systems.
[ ] It tags objects by MVP Phase and MVP Depth.
[ ] It prepares core-specs/objects/ generation.
[ ] It supports Appendix D, E, F, G and H.
[ ] It prevents database-first, product-first and prompt-first object drift.
```

---

# 17. Revision Notes

| Version | Status | Notes |
|---------|--------|-------|
| 0.2.0 | Draft | Initial second canonical draft of Appendix C. Defines the Core Object Index, object ownership, MVP depth, AI governance objects, contract/governance objects and core-specs/objects readiness. |

---

**End of Appendix**
