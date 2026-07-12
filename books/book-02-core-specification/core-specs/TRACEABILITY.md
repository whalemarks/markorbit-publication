# Core Traceability Matrix

**Spec ID:** B02-TRACEABILITY  
**Spec Type:** Core Traceability Matrix  
**Spec File:** core-specs/TRACEABILITY.md  
**Related Book:** Book 02 — MarkOrbit Core Specification  
**Related Layers:** Domains; Objects; Services; Events; APIs; Agents; Contracts; Workflows; Tests; Codex Tasks  
**Related Governance:** MAC; MAG; MAS; Agent Governance; Contract Governance; Validation Governance  
**Status:** Draft  
**Version:** 0.1.0  
**Traceability Version:** v0.1.0  
**MVP Phase:** Phase 0 — Architecture Traceability and Implementation Readiness  
**MVP Depth:** Must Maintain  
**Owner:** MarkOrbit Publications Editorial Board  

---

# 1. Purpose

This Traceability Matrix defines the cross-layer mapping for MarkOrbit Core.

It connects:

```text
Domain
↓
Object
↓
Service
↓
API Contract
↓
Event Specs
↓
Workflow Specs
↓
Workflow Contracts
↓
Agent Specs
↓
Test Contracts
↓
Codex Tasks
```

Its purpose is to prevent:

```text
missing implementation coverage
duplicate responsibility
API-layer domain behavior leakage
workflow-layer direct mutation
agent autonomous execution
event misuse as command
test coverage gaps
Codex implementation drift
```

This file is the primary bridge between Book 02 as an architecture specification and Book 02 as an executable engineering baseline.

---

# 2. Core Lock

```text
Traceability connects Core layers.
Domains define responsibility areas.
Objects describe state.
Services own behavior.
API Contracts expose governed access.
Events preserve trace.
Workflows coordinate execution.
Workflow Contracts constrain execution.
Agents assist within governed capability boundaries.
Tests verify Core behavior.
Codex implements traced specifications.
Codex does not define architecture.
```

---

# 3. Traceability Principles

Every Core element must follow these rules:

```text
1. Every Domain must map to an Object Spec.
2. Every Object Spec must map to an owning Service Spec.
3. Every Service Spec must map to one API Contract where external or internal access is needed.
4. Every state-changing Service must map to Event Specs.
5. Every Workflow must map to Workflow Contract, Services, Events and Tests.
6. Every Agent must map to allowed capabilities, forbidden actions and tests.
7. Every protected behavior must map to Permission and Policy contracts.
8. Every duplicate-sensitive behavior must map to Idempotency.
9. Every failure path must map to Error Contract.
10. Every implementation task must cite traced source specs.
```

---

# 4. Layer Responsibility Map

| Layer | Owns | Must Not Own |
|---|---|---|
| Domain | responsibility area and classification | runtime behavior |
| Object | state shape and identity | business execution |
| Service | behavior and mutation | UI or product-specific flow |
| API Contract | request and response boundary | service implementation |
| Event | trace of completed fact | command or workflow trigger by itself |
| Workflow | execution flow | domain mutation directly |
| Workflow Contract | governed workflow boundary | business outcome ownership |
| Agent | governed assistance | protected action execution |
| Test Contract | acceptance verification | production logic |
| Codex Task | implementation execution | architecture definition |

---

# 5. Core Domain Traceability Matrix

## 5.1 Foundation Domains

| Domain | Object Spec | Service Spec | API Contract | Primary Events | Workflow Coverage | Test Coverage |
|---|---|---|---|---|---|---|
| Identity | core-specs/objects/identity-object.md | core-specs/services/identity-service.md | core-specs/contracts/api/identity-api-contract.md | identity-created; identity-updated | Cross-cutting access context | API Contract Tests; Permission Policy Tests |
| Organization | core-specs/objects/organization-object.md | core-specs/services/organization-service.md | core-specs/contracts/api/organization-api-contract.md | organization-created; organization-updated | Cross-organization policy context | API Contract Tests; Permission Policy Tests |
| User | core-specs/objects/user-object.md | core-specs/services/user-service.md | core-specs/contracts/api/user-api-contract.md | user-created; user-updated | Human actor context | API Contract Tests; Permission Policy Tests |
| Permission | core-specs/objects/permission-object.md | core-specs/services/permission-service.md | core-specs/contracts/api/permission-api-contract.md | permission-evaluated | All protected workflows | Permission Policy Tests |
| Policy | core-specs/objects/policy-object.md | core-specs/services/policy-service.md | core-specs/contracts/api/policy-api-contract.md | policy-evaluated | All policy-controlled workflows | Permission Policy Tests |
| Knowledge | core-specs/objects/knowledge-object.md | core-specs/services/knowledge-service.md | core-specs/contracts/api/knowledge-api-contract.md | knowledge-source-added; knowledge-source-updated | AI-assisted reference context | Agent Boundary Tests; API Contract Tests |

## 5.2 Professional Domains

| Domain | Object Spec | Service Spec | API Contract | Primary Events | Workflow Coverage | Test Coverage |
|---|---|---|---|---|---|---|
| Brand | core-specs/objects/brand-object.md | core-specs/services/brand-service.md | core-specs/contracts/api/brand-api-contract.md | brand-created; brand-updated | Customer Intake; Trademark Application | API Contract Tests; Workflow Contract Tests |
| Trademark | core-specs/objects/trademark-object.md | core-specs/services/trademark-service.md | core-specs/contracts/api/trademark-api-contract.md | trademark-created; trademark-updated; trademark-status-changed | Trademark Application; Office Action Response; Renewal; Assignment | API Contract Tests; Workflow Contract Tests |
| Jurisdiction | core-specs/objects/jurisdiction-object.md | core-specs/services/jurisdiction-service.md | core-specs/contracts/api/jurisdiction-api-contract.md | jurisdiction-rule-updated | Trademark Application; Office Action Response; Renewal; Assignment | API Contract Tests; Workflow Contract Tests |
| Classification | core-specs/objects/classification-object.md | core-specs/services/classification-service.md | core-specs/contracts/api/classification-api-contract.md | classification-suggestion-created; classification-updated | Trademark Application; Office Action Response | API Contract Tests; Agent Boundary Tests |
| Document | core-specs/objects/document-object.md | core-specs/services/document-service.md | core-specs/contracts/api/document-api-contract.md | document-created; document-updated; document-attached | Customer Intake; Trademark Application; Evidence Review; Assignment | API Contract Tests; Workflow Contract Tests |
| Evidence | core-specs/objects/evidence-object.md | core-specs/services/evidence-service.md | core-specs/contracts/api/evidence-api-contract.md | evidence-created; evidence-reviewed | Evidence Review; Office Action Response; Renewal | API Contract Tests; Workflow Contract Tests; Agent Boundary Tests |

## 5.3 Business Execution Domains

| Domain | Object Spec | Service Spec | API Contract | Primary Events | Workflow Coverage | Test Coverage |
|---|---|---|---|---|---|---|
| Customer | core-specs/objects/customer-object.md | core-specs/services/customer-service.md | core-specs/contracts/api/customer-api-contract.md | customer-created; customer-updated | Customer Intake | API Contract Tests; Workflow Contract Tests |
| Matter | core-specs/objects/matter-object.md | core-specs/services/matter-service.md | core-specs/contracts/api/matter-api-contract.md | matter-created; matter-updated; matter-status-changed | Customer Intake; Trademark Application; Office Action Response; Renewal; Assignment | API Contract Tests; Workflow Contract Tests |
| Order | core-specs/objects/order-object.md | core-specs/services/order-service.md | core-specs/contracts/api/order-api-contract.md | order-created; order-updated; order-status-changed | Customer Intake; Trademark Application; Renewal; Assignment | API Contract Tests; Workflow Contract Tests |
| Opportunity | core-specs/objects/opportunity-object.md | core-specs/services/opportunity-service.md | core-specs/contracts/api/opportunity-api-contract.md | opportunity-created; opportunity-updated; opportunity-converted | Customer Intake | API Contract Tests; Workflow Contract Tests |
| Workflow Contract | core-specs/objects/workflow-contract-object.md | core-specs/services/workflow-contract-service.md | core-specs/contracts/api/workflow-contract-api-contract.md | workflow-contract-previewed; workflow-contract-applied | All governed workflows | Workflow Contract Tests; Idempotency Event Tests |
| Task | core-specs/objects/task-object.md | core-specs/services/task-service.md | core-specs/contracts/api/task-api-contract.md | task-created; task-updated; task-completed | All active execution workflows | API Contract Tests; Workflow Contract Tests; Idempotency Event Tests |
| Event | core-specs/objects/event-object.md | core-specs/services/event-service.md | core-specs/contracts/api/event-api-contract.md | event-recorded | All traceable behavior | Idempotency Event Tests; Error Versioning Tests |
| Notification | core-specs/objects/notification-object.md | core-specs/services/notification-service.md | core-specs/contracts/api/notification-api-contract.md | notification-created; notification-delivered | Deadline, review and task attention flows | API Contract Tests; Permission Policy Tests |
| Communication | core-specs/objects/communication-object.md | core-specs/services/communication-service.md | core-specs/contracts/api/communication-api-contract.md | communication-created; communication-reviewed; communication-sent | Communication Review; Provider Routing; Office Action Response | API Contract Tests; Workflow Contract Tests; Agent Boundary Tests |

## 5.4 Collaboration Network Domains

| Domain | Object Spec | Service Spec | API Contract | Primary Events | Workflow Coverage | Test Coverage |
|---|---|---|---|---|---|---|
| Partner | core-specs/objects/partner-object.md | core-specs/services/partner-service.md | core-specs/contracts/api/partner-api-contract.md | partner-created; partner-updated | Customer Intake; Service Network coordination | API Contract Tests; Permission Policy Tests |
| Agent | core-specs/objects/agent-object.md | core-specs/services/agent-service.md | core-specs/contracts/api/agent-api-contract.md | agent-registered; agent-capability-updated | AI-assisted workflow steps | Agent Boundary Tests |
| Service Provider | core-specs/objects/service-provider-object.md | core-specs/services/service-provider-service.md | core-specs/contracts/api/service-provider-api-contract.md | service-provider-created; service-provider-updated | Provider Routing | API Contract Tests; Workflow Contract Tests |
| Service Network | core-specs/objects/service-network-object.md | core-specs/services/service-network-service.md | core-specs/contracts/api/service-network-api-contract.md | service-network-updated | Provider Routing; Collaboration flows | API Contract Tests; Permission Policy Tests |
| Routing | core-specs/objects/routing-object.md | core-specs/services/routing-service.md | core-specs/contracts/api/routing-api-contract.md | routing-evaluated; routing-selected | Provider Routing | Workflow Contract Tests; Idempotency Event Tests |
| Communication | core-specs/objects/communication-object.md | core-specs/services/communication-service.md | core-specs/contracts/api/communication-api-contract.md | communication-created; communication-reviewed; communication-sent | Communication Review; Provider Routing | API Contract Tests; Workflow Contract Tests |

Note:

```text
Communication appears in Business Execution and Collaboration Network perspectives because it is both an execution domain and a collaboration interface.
The canonical baseline still counts Communication once.
```

---

# 6. Workflow Traceability Matrix

| Workflow | Workflow Spec | Workflow Contract | Primary Services | Primary Events | Agent Support | Test Coverage |
|---|---|---|---|---|---|---|
| Customer Intake | core-specs/workflows/customer-intake-workflow.md | core-specs/contracts/workflows/customer-intake-workflow-contract.md | Customer; Opportunity; Brand; Matter; Order; Document; Task; Event | customer-created; opportunity-created; matter-created; order-created; task-created | Workflow Agent; Task Agent; Knowledge Agent | Workflow Contract Tests |
| Trademark Application | core-specs/workflows/trademark-application-workflow.md | core-specs/contracts/workflows/trademark-application-workflow-contract.md | Trademark; Brand; Jurisdiction; Classification; Document; Matter; Order; Task; Event | trademark-created; classification-suggestion-created; document-attached; task-created | Knowledge Agent; Workflow Agent; Task Agent | Workflow Contract Tests; Agent Boundary Tests |
| Office Action Response | core-specs/workflows/office-action-response-workflow.md | core-specs/contracts/workflows/office-action-response-workflow-contract.md | Trademark; Matter; Document; Evidence; Communication; Task; Event | evidence-created; communication-created; task-created; trademark-status-changed | Knowledge Agent; Communication Agent; Workflow Agent | Workflow Contract Tests; Agent Boundary Tests |
| Provider Routing | core-specs/workflows/provider-routing-workflow.md | core-specs/contracts/workflows/provider-routing-workflow-contract.md | Routing; Service Provider; Service Network; Partner; Communication; Task; Event | routing-evaluated; routing-selected; communication-created; task-created | Routing Agent; Communication Agent | Workflow Contract Tests; Idempotency Event Tests |
| Communication Review | core-specs/workflows/communication-review-workflow.md | core-specs/contracts/workflows/communication-review-workflow-contract.md | Communication; Document; Matter; Task; Event; Policy; Permission | communication-created; communication-reviewed; communication-sent | Communication Agent; Audit Agent | Workflow Contract Tests; Agent Boundary Tests |
| Renewal | core-specs/workflows/renewal-workflow.md | core-specs/contracts/workflows/renewal-workflow-contract.md | Trademark; Jurisdiction; Knowledge; Matter; Order; Document; Evidence; Task; Event | renewal-candidate-created; task-created; document-attached | Knowledge Agent; Workflow Agent; Task Agent | Workflow Contract Tests |
| Assignment | core-specs/workflows/assignment-workflow.md | core-specs/contracts/workflows/assignment-workflow-contract.md | Trademark; Customer; Matter; Order; Document; Evidence; Communication; Task; Event | assignment-prepared; document-attached; task-created | Knowledge Agent; Communication Agent; Workflow Agent | Workflow Contract Tests |
| Evidence Review | core-specs/workflows/evidence-review-workflow.md | core-specs/contracts/workflows/evidence-review-workflow-contract.md | Evidence; Document; Trademark; Brand; Matter; Order; Jurisdiction; Classification; Task; Event | evidence-created; evidence-reviewed; task-created | Knowledge Agent; Audit Agent; Workflow Agent | Workflow Contract Tests; Agent Boundary Tests |

---

# 7. Agent Traceability Matrix

| Agent | Agent Spec | Primary Capabilities | Forbidden Actions | Related Workflows | Test Coverage |
|---|---|---|---|---|---|
| Agent Governance | core-specs/agents/ai-agent-governance.md | policy boundary; capability governance | approve; submit; mutate; send | All AI-assisted workflows | Agent Boundary Tests |
| Agent Registry | core-specs/agents/agent-registry.md | agent identity; capability registry | execute protected action | All AI-assisted workflows | Agent Boundary Tests |
| Knowledge Agent | core-specs/agents/knowledge-agent.md | retrieve; summarize; cite governed knowledge | certify professional truth | Trademark Application; Office Action Response; Renewal; Evidence Review | Agent Boundary Tests |
| Task Agent | core-specs/agents/task-agent.md | prepare task plan; suggest next tasks | create active task; complete task | Customer Intake; Trademark Application; Renewal | Agent Boundary Tests; Workflow Contract Tests |
| Communication Agent | core-specs/agents/communication-agent.md | draft; summarize; compare communication | send external communication | Communication Review; Provider Routing; Office Action Response | Agent Boundary Tests |
| Workflow Agent | core-specs/agents/workflow-agent.md | preview; summarize workflow progress; suggest steps | apply workflow; mutate state | All governed workflows | Agent Boundary Tests; Workflow Contract Tests |
| Routing Agent | core-specs/agents/routing-agent.md | compare providers; suggest routing candidates | select provider; approve route | Provider Routing | Agent Boundary Tests; Idempotency Event Tests |
| Audit Agent | core-specs/agents/audit-agent.md | summarize trace; detect missing context | alter event history; approve compliance | Communication Review; Evidence Review; All traceable flows | Agent Boundary Tests; Error Versioning Tests |

---

# 8. Contract Traceability Matrix

| Contract Layer | Index | Primary Files | Verifies / Constrains |
|---|---|---|---|
| Common Contracts | core-specs/contracts/common/index.md | references; errors; pagination; audit-context; ai-context; human-review; permission-context; policy-context; idempotency; versioning | shared primitives |
| API Contracts | core-specs/contracts/api/index.md | 26 domain API contracts | request/response boundaries |
| Workflow Contracts | core-specs/contracts/workflows/index.md | 8 workflow contracts | governed execution patterns |
| Test Contracts | core-specs/contracts/tests/index.md | common; api; workflow; agent; permission-policy; idempotency-event; error-versioning tests | implementation acceptance |
| Contract Package | core-specs/contracts/index.md | README; template; MANIFEST; CODEX-TASK | contract layer governance |

---

# 9. MVP Traceability Cut

## 9.1 Must Build Now

```text
Identity
Organization
User
Permission
Policy
Customer
Brand
Trademark
Jurisdiction
Classification
Document
Evidence
Matter
Order
Task
Event
Communication
Workflow Contract
```

Required workflows:

```text
Customer Intake Workflow
Trademark Application Workflow
Communication Review Workflow
```

Required contracts:

```text
Common Contracts
API Contracts for MVP domains
Workflow Contracts for MVP workflows
Test Contracts for common, API, workflow, permission-policy, idempotency-event, error-versioning
```

## 9.2 Stub Now

```text
Knowledge Service advanced retrieval
Notification delivery
Service Network optimization
Provider commercial scoring
Routing optimization
Agent runtime orchestration
Renewal workflow
Assignment workflow
Evidence review workflow
Office Action Response workflow
Provider Routing workflow
```

## 9.3 Document Only for MVP

```text
full policy engine
full agent runtime
full workflow engine
external filing integration
payment execution
provider marketplace settlement
advanced analytics
multi-product marketplace integration
```

---

# 10. Traceability Validation Checklist

This Traceability Matrix is valid only if:

```text
[ ] Every Core Domain maps to an Object Spec.
[ ] Every Core Domain maps to a Service Spec.
[ ] Every Core Domain maps to an API Contract.
[ ] Every state-changing Service maps to at least one Event Spec.
[ ] Every Workflow maps to a Workflow Spec.
[ ] Every Workflow maps to a Workflow Contract.
[ ] Every Workflow maps to Services.
[ ] Every Workflow maps to Events.
[ ] Every Workflow maps to Test Contracts.
[ ] Every Agent maps to Agent Spec.
[ ] Every Agent maps to forbidden actions.
[ ] Every protected behavior maps to Permission / Policy.
[ ] Every duplicate-sensitive behavior maps to Idempotency.
[ ] Every traceable behavior maps to Event.
[ ] Every failure behavior maps to Error Contract.
[ ] Every versioned behavior maps to Versioning Contract.
[ ] Every Codex task cites source specs.
```

---

# 11. Known Traceability Gaps

The following files must be created or confirmed:

```text
core-specs/workflows/index.md
core-specs/workflows/customer-intake-workflow.md
core-specs/workflows/trademark-application-workflow.md
core-specs/workflows/communication-review-workflow.md
core-specs/implementation/mvp-cut-v0.1.md
core-specs/implementation/implementation-depth-matrix.md
core-specs/DEVELOPER_START_HERE.md
core-specs/codex/CODEX-TASK-INDEX.md
core-specs/validation/index.md
core-specs/validation/traceability-validation.md
core-specs/validation/mvp-readiness-validation.md
```

Structural normalization required:

```text
core-specs/contracts/test/
must be normalized to:
core-specs/contracts/tests/
```

---

# 12. Codex Implementation Notes

Codex must:

```text
read this Traceability Matrix before implementation
cite traced source files in every task
not implement untraced behavior
not create new ownership boundaries
not mutate domain state outside owning services
not emit events from API / Workflow / Agent layers
not allow AI to execute protected actions
not bypass Permission or Policy
not skip Test Contracts
```

Codex should use this file to decide:

```text
which object belongs to which domain
which service owns behavior
which API contract exposes access
which events preserve trace
which workflows coordinate services
which tests must cover behavior
which tasks are safe to implement first
```

---

# 13. Acceptance Criteria

This Traceability Matrix is accepted only if:

```text
[ ] It defines purpose.
[ ] It defines Core Lock.
[ ] It defines traceability principles.
[ ] It defines layer responsibility map.
[ ] It maps Foundation Domains.
[ ] It maps Professional Domains.
[ ] It maps Business Execution Domains.
[ ] It maps Collaboration Network Domains.
[ ] It maps Workflows.
[ ] It maps Agents.
[ ] It maps Contracts.
[ ] It defines MVP Traceability Cut.
[ ] It defines validation checklist.
[ ] It identifies known traceability gaps.
[ ] It defines Codex implementation notes.
```

---

# 14. Revision Notes

| Version | Status | Notes |
|---------|--------|-------|
| 0.1.0 | Draft | Initial Core Traceability Matrix. Maps Domains, Objects, Services, API Contracts, Events, Workflows, Workflow Contracts, Agents, Tests, MVP cut and Codex implementation boundaries. |

---

**End of Core Traceability Matrix**


## PUB-TASK-B02-002

PUB-TASK-B02-002 traceability chain: classification decision -> controlled state/component spec -> service/API/contract reference -> future fixtures -> future implementation.
