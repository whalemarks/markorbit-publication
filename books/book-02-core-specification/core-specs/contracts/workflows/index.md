# Workflow Contracts — Index

**Spec ID:** B02-CONTRACT-WORKFLOW-INDEX  
**Spec Type:** Workflow Contract Index  
**Contract File:** core-specs/contracts/workflows/index.md  
**Contract Category:** Workflow Contracts  
**Related Files:** core-specs/contracts/workflows/README.md; core-specs/contracts/workflows/template.md  
**Related Core Specs:** core-specs/contracts/README.md; core-specs/contracts/template.md; core-specs/contracts/common/references.md; core-specs/contracts/common/errors.md; core-specs/contracts/common/audit-context.md; core-specs/contracts/common/permission-context.md; core-specs/contracts/common/policy-context.md; core-specs/contracts/common/ai-context.md; core-specs/contracts/common/human-review.md; core-specs/contracts/common/idempotency.md; core-specs/contracts/common/versioning.md  
**Status:** Draft  
**Version:** 0.1.0  
**Contract Version:** v0.1.0  
**MVP Phase:** Phase 3–5 — Business Execution / Collaboration / Post-Registration Expansion  
**MVP Depth:** Must Maintain  
**Owner:** MarkOrbit Publications Editorial Board  

---

# 1. Purpose

This index provides the canonical inventory and governance map for all Workflow Contracts under:

```text
core-specs/contracts/workflows/
```

It defines:

```text
workflow contract file inventory
workflow contract priority
workflow contract ownership boundary
workflow-to-domain mapping
workflow-to-service dependency
workflow-to-event dependency
workflow-to-agent dependency
workflow common governance requirements
MVP implementation order
Codex implementation checklist
acceptance criteria
```

This index is a navigation and governance artifact. It is not a workflow implementation file and does not replace the individual Workflow Contract files.

---

# 2. Core Lock

```text
Workflow Contracts define governed execution patterns.
Workflow Contract Service owns workflow contract behavior.
Task Service owns active Task creation.
Owning domain services own domain state.
Permission and Policy govern every workflow action.
AI may prepare, summarize and suggest, but must not execute protected actions.
Events preserve trace.
```

This lock applies to every Workflow Contract listed in this index.

---

# 3. Canonical Workflow Contract Inventory

| No. | Workflow Contract | File | MVP Depth | Status |
|---:|---|---|---|---|
| 1 | Customer Intake Workflow Contract | core-specs/contracts/workflows/customer-intake-workflow-contract.md | Must Implement | Draft |
| 2 | Trademark Application Workflow Contract | core-specs/contracts/workflows/trademark-application-workflow-contract.md | Must Implement | Draft |
| 3 | Office Action Response Workflow Contract | core-specs/contracts/workflows/office-action-response-workflow-contract.md | Must Implement | Draft |
| 4 | Provider Routing Workflow Contract | core-specs/contracts/workflows/provider-routing-workflow-contract.md | Must Implement | Draft |
| 5 | Communication Review Workflow Contract | core-specs/contracts/workflows/communication-review-workflow-contract.md | Must Implement | Draft |
| 6 | Renewal Workflow Contract | core-specs/contracts/workflows/renewal-workflow-contract.md | Should Implement | Draft |
| 7 | Assignment Workflow Contract | core-specs/contracts/workflows/assignment-workflow-contract.md | Should Implement | Draft |
| 8 | Evidence Review Workflow Contract | core-specs/contracts/workflows/evidence-review-workflow-contract.md | Should Implement | Draft |

---

# 4. Workflow Contract Priority

## 4.1 Must Implement

```text
customer-intake-workflow-contract.md
trademark-application-workflow-contract.md
office-action-response-workflow-contract.md
provider-routing-workflow-contract.md
communication-review-workflow-contract.md
```

Reason:

```text
These workflows form the minimum execution backbone for MarkOrbit business operation:
- intake request
- prepare trademark application
- respond to office action
- route provider
- review communication
```

## 4.2 Should Implement

```text
renewal-workflow-contract.md
assignment-workflow-contract.md
evidence-review-workflow-contract.md
```

Reason:

```text
These workflows extend MarkOrbit into post-registration, portfolio maintenance and professional evidence review.
They should not block MVP execution, but they should be standardized before workflow automation expands.
```

---

# 5. Workflow Boundary Matrix

| Workflow | Owns Coordination | Must Not Own |
|---|---|---|
| Customer Intake | Intake structuring, customer/opportunity preparation, task plan | customer engagement approval, legal advice, order execution |
| Trademark Application | Filing preparation, classification/document readiness, task plan | official filing submission, registrability decision, payment approval |
| Office Action Response | Official notice intake, deadline/issue preparation, response readiness | legal strategy final approval, official response submission |
| Provider Routing | Candidate evaluation, recommendation, reviewed selection flow | silent provider selection, engagement/payment approval |
| Communication Review | Draft, review, approval and send-preparation | external sending without governed Communication Service process |
| Renewal | Renewal window/deadline preparation, renewal readiness | official renewal filing, deadline certification without review |
| Assignment | Ownership-change preparation, documents, party context | official recordal, authority certification without review |
| Evidence Review | Evidence structuring, gap analysis, readiness review | legal sufficiency decision, evidence submission |

---

# 6. Workflow-to-Domain Mapping

```text
Customer Intake
  Customer
  Opportunity
  Matter
  Order
  Brand
  Trademark
  Document
  Communication
  Task
  Event

Trademark Application
  Trademark
  Brand
  Jurisdiction
  Classification
  Document
  Evidence
  Customer
  Matter
  Order
  Communication
  Task
  Event

Office Action Response
  Trademark
  Jurisdiction
  Classification
  Document
  Evidence
  Customer
  Matter
  Order
  Knowledge
  Communication
  Task
  Event

Provider Routing
  Routing
  Service Provider
  Service Network
  Partner
  Jurisdiction
  Matter
  Order
  Communication
  Task
  Event

Communication Review
  Communication
  Document
  Task
  Matter
  Order
  Customer
  Service Provider
  Partner
  Event

Renewal
  Trademark
  Jurisdiction
  Knowledge
  Customer
  Matter
  Order
  Document
  Evidence
  Communication
  Notification
  Task
  Event

Assignment
  Trademark
  Customer
  Jurisdiction
  Knowledge
  Matter
  Order
  Document
  Evidence
  Communication
  Task
  Event

Evidence Review
  Evidence
  Document
  Trademark
  Brand
  Customer
  Matter
  Order
  Jurisdiction
  Classification
  Knowledge
  Communication
  Task
  Event
```

---

# 7. Common Required Services

Every Workflow Contract depends on:

```text
Workflow Contract Service
Task Service
Event Service
Permission Service
Policy Service
Agent Service
```

Rules:

```text
- Workflow Contract Service owns preview and apply behavior.
- Task Service owns active Task creation.
- Event Service owns trace records.
- Permission Service owns permission evaluation.
- Policy Service owns contextual restriction evaluation.
- Agent Service governs AI capability use.
```

---

# 8. Workflow-Specific Service Dependencies

| Workflow | Primary Domain Services |
|---|---|
| Customer Intake | Customer Service; Opportunity Service; Matter Service; Order Service; Brand Service; Trademark Service; Document Service; Communication Service |
| Trademark Application | Trademark Service; Brand Service; Jurisdiction Service; Classification Service; Document Service; Evidence Service; Customer Service; Matter Service; Order Service; Communication Service |
| Office Action Response | Trademark Service; Jurisdiction Service; Classification Service; Document Service; Evidence Service; Knowledge Service; Customer Service; Matter Service; Order Service; Communication Service |
| Provider Routing | Routing Service; Service Provider Service; Service Network Service; Partner Service; Jurisdiction Service; Matter Service; Order Service; Communication Service |
| Communication Review | Communication Service; Document Service; Matter Service; Order Service; Customer Service; Service Provider Service; Partner Service |
| Renewal | Trademark Service; Jurisdiction Service; Knowledge Service; Customer Service; Matter Service; Order Service; Document Service; Evidence Service; Communication Service; Notification Service |
| Assignment | Trademark Service; Customer Service; Jurisdiction Service; Knowledge Service; Matter Service; Order Service; Document Service; Evidence Service; Communication Service |
| Evidence Review | Evidence Service; Document Service; Trademark Service; Brand Service; Customer Service; Matter Service; Order Service; Jurisdiction Service; Classification Service; Knowledge Service; Communication Service |

---

# 9. Workflow-to-Agent Mapping

| Workflow | Allowed Agent Support | Hard Boundary |
|---|---|---|
| Customer Intake | Workflow Agent; Task Agent; Communication Agent | AI must not approve engagement or create professional truth |
| Trademark Application | Workflow Agent; Knowledge Agent; Task Agent; Communication Agent | AI must not decide registrability or filing strategy |
| Office Action Response | Workflow Agent; Knowledge Agent; Task Agent; Communication Agent | AI must not decide legal strategy or submit response |
| Provider Routing | Routing Agent; Workflow Agent; Task Agent; Communication Agent | AI must not select provider |
| Communication Review | Communication Agent; Workflow Agent; Task Agent | AI must not approve or send |
| Renewal | Workflow Agent; Knowledge Agent; Task Agent; Communication Agent | AI must not certify deadlines or submit renewal |
| Assignment | Workflow Agent; Knowledge Agent; Task Agent; Communication Agent | AI must not certify authority or record assignment |
| Evidence Review | Workflow Agent; Knowledge Agent; Task Agent; Communication Agent | AI must not decide evidence sufficiency |

---

# 10. Workflow-to-Event Mapping

Common event references:

```text
WorkflowContractApplied
TaskCreated
PermissionEvaluated
PolicyEvaluated
```

Workflow-specific event references:

```text
Customer Intake:
  CustomerCreated
  OpportunityCreated
  CommunicationCreated

Trademark Application:
  TrademarkCreated
  MatterCreated
  OrderCreated
  CommunicationCreated

Office Action Response:
  CommunicationCreated

Provider Routing:
  RoutingEvaluated
  RoutingSelected
  CommunicationCreated

Communication Review:
  CommunicationCreated

Renewal:
  MatterCreated
  OrderCreated
  NotificationCreated
  CommunicationCreated

Assignment:
  MatterCreated
  OrderCreated
  CommunicationCreated

Evidence Review:
  CommunicationCreated
```

Rules:

```text
- Workflow Contract files must not emit events directly.
- Events are emitted by owning services.
- Event references are audit trace, not commands.
- Idempotent replay must not duplicate events.
```

---

# 11. Common Human Review Checkpoints

Every Workflow Contract must define review checkpoints where output affects:

```text
professional conclusions
customer-facing communication
external communication
provider selection
deadline confirmation
classification or goods/services wording
evidence sufficiency
ownership or authority context
filing or submission readiness
payment-impacting or commercial decisions
```

Core rule:

```text
Human Review records accountable review.
Human Review does not execute downstream action by itself.
Owning services decide whether review satisfies action requirements.
```

---

# 12. Common AI Boundary

AI may:

```text
summarize visible context
identify missing fields
prepare checklists
prepare task plans
prepare drafts
compare visible candidates
retrieve governed source-grounded references
explain visible event trace
```

AI must not:

```text
apply workflow by itself
create active tasks by itself
complete tasks
approve communications
send communications
select providers
certify deadlines
certify authority
decide evidence sufficiency
decide legal strategy
decide registrability
submit filings
approve payments
bypass Permission or Policy
```

---

# 13. Common Permission Requirements

Every Workflow Contract must use:

```text
workflow-contract:preview
workflow-contract:apply
task:create
```

And must add domain-specific keys, for example:

```text
customer:create
trademark:update
classification:suggestion:prepare
document:create
evidence:update
communication:draft:prepare
communication:approve
routing:evaluate
routing:select
matter:update
order:update
notification:create
```

Rules:

```text
- Permission Service evaluates permission.
- Workflow Contract must not grant permission.
- PermissionDenied must stop or downgrade protected behavior.
```

---

# 14. Common Policy Requirements

Every Workflow Contract must use:

```text
workflow-contract:preview:policy
workflow-contract:apply:policy
cross-organization:workflow
```

And must add domain-specific scopes, for example:

```text
customer:read:policy
trademark:read:policy
document:visibility:policy
evidence:visibility:policy
communication:draft:prepare:policy
routing:candidate:visibility:policy
routing:commercial-terms:visibility:policy
matter:update:policy
order:update:policy
```

Rules:

```text
- Policy Service evaluates contextual restrictions.
- Policy may block, redact, downgrade or require human review.
- PolicyRestricted must stop protected action or return safe partial output.
```

---

# 15. Common Idempotency Rules

```text
Preview:
  idempotency_key normally not required unless result is persisted.

Apply:
  idempotency_key required.

Task creation:
  must be duplicate-safe.

Communication creation:
  must be duplicate-safe.

Document creation:
  must be duplicate-safe where generated.

Routing evaluation/selection:
  must be duplicate-safe.

Matter/Order creation:
  must be duplicate-safe.

Notification creation:
  must be duplicate-safe.
```

Core rule:

```text
Duplicate workflow application must not duplicate Tasks, Communications, Documents, Matter, Order, Routing selections, Notifications or Events.
```

---

# 16. Common Error Categories

Workflow Contracts must use Error Contract and may include:

```text
WorkflowReferenceInvalid
WorkflowNotApplicable
WorkflowPreviewUnavailable
WorkflowApplyConflict
TargetReferenceInvalid
TaskCreationFailed
PermissionDenied
PolicyRestricted
HumanReviewRequired
StateInvalid
InsufficientContext
IdempotencyKeyRequired
IdempotencyConflict
VersionUnsupported
InternalError
```

Rules:

```text
- Errors must be safe.
- Errors must not expose restricted data, private notes, policy internals or permission internals.
- NotFound may be returned instead of PolicyRestricted where policy requires non-disclosure.
```

---

# 17. Common Versioning Requirements

Every Workflow Contract must include:

```yaml
workflow_contract_version: v0.1.0
contract_version: v0.1.0
schema_version: v0.1.0
```

Rules:

```text
- Breaking changes require version bump.
- Workflow application must record workflow_contract_version used.
- Historical workflow applications must remain traceable.
- Deprecated workflow versions must not be silently rewritten.
```

---

# 18. MVP Implementation Order

Recommended Codex implementation order:

```text
1. Workflow Contracts README
2. Workflow Contract Template
3. Customer Intake Workflow Contract
4. Trademark Application Workflow Contract
5. Communication Review Workflow Contract
6. Provider Routing Workflow Contract
7. Office Action Response Workflow Contract
8. Evidence Review Workflow Contract
9. Renewal Workflow Contract
10. Assignment Workflow Contract
11. Workflow Contracts Index
```

Reasoning:

```text
- README and template establish governance.
- Customer Intake initializes pipeline entry.
- Trademark Application provides core business execution.
- Communication Review is required across all workflows.
- Provider Routing supports network execution.
- Office Action Response extends professional execution.
- Evidence/Renewal/Assignment expand post-registration and professional-depth workflows.
- Index closes the system as a navigable contract layer.
```

---

# 19. Codex Implementation Notes

Codex must:

```text
read Workflow Contracts README before implementing workflows
use Workflow Contract Template for any new workflow contract
cite each workflow contract before implementation
cite related API contracts before implementing payload behavior
cite related Service specs before implementing behavior
use Task Service for active Task creation
use Event Service for trace retrieval
use Permission Context Contract before protected steps
use Policy Context Contract before policy-controlled steps
use AI Context Contract for AI-assisted steps
use Human Review Contract for review checkpoints
use Idempotency Contract for apply operations
use Versioning Contract for workflow versioning
write preview tests for every workflow
write apply tests for every workflow
write idempotency replay tests for every workflow
write PermissionDenied tests for every workflow
write PolicyRestricted tests for every workflow
write AI boundary tests for every workflow
write human-review gate tests for every workflow
write no-direct-event-emission tests for every workflow
```

Codex must not:

```text
treat workflow contracts as implementation code
create active tasks outside Task Service
emit events directly from workflow code
mutate target objects outside owning services
skip Permission or Policy checks
allow AI to apply workflows, complete tasks, approve, send, select, certify or submit
hide human-review requirements
overwrite historical workflow versions silently
```

---

# 20. Acceptance Criteria

This Workflow Contracts Index is accepted only if:

```text
[ ] It lists all canonical Workflow Contract files.
[ ] It identifies MVP depth for each Workflow Contract.
[ ] It defines workflow boundary matrix.
[ ] It defines workflow-to-domain mapping.
[ ] It defines common required services.
[ ] It defines workflow-specific service dependencies.
[ ] It defines workflow-to-agent mapping.
[ ] It defines workflow-to-event mapping.
[ ] It defines common human review checkpoints.
[ ] It defines common AI boundary.
[ ] It defines common Permission requirements.
[ ] It defines common Policy requirements.
[ ] It defines common idempotency rules.
[ ] It defines common error categories.
[ ] It defines common versioning requirements.
[ ] It defines MVP implementation order.
[ ] It defines Codex implementation notes.
```

---

# 21. Revision Notes

| Version | Status | Notes |
|---------|--------|-------|
| 0.1.0 | Draft | Initial Workflow Contracts Index. Defines canonical workflow inventory, MVP priority, workflow boundaries, domain/service/agent/event mappings, common governance rules, idempotency, errors, versioning, implementation order and Codex expectations. |

---

**End of Workflow Contracts Index**
