# Core Contracts — README

**Spec ID:** B02-CONTRACTS-README  
**Spec Type:** Contracts Layer README  
**File:** core-specs/contracts/README.md  
**Related Book:** Book 02 — MarkOrbit Core Specification  
**Related Layers:** Domains; Objects; Services; Events; APIs; Agents; Workflows; Validation  
**Status:** Draft  
**Version:** 0.1.0  
**MVP Phase:** Cross-Phase Core Contract System  
**MVP Depth:** Must Implement  
**Owner:** MarkOrbit Publications Editorial Board  

---

# 1. Purpose

The Contracts layer defines the stable machine-readable and implementation-facing agreements used by MarkOrbit Core.

Contracts exist to make Core specifications executable by Codex and consistent across:

```text
API requests
API responses
service inputs
service outputs
event payloads
object references
agent runtime boundaries
workflow applications
permission and policy checks
validation rules
error handling
versioning
```

Contracts are not business process documents, product screens, UI copy, implementation shortcuts or informal examples.

---

# 2. Contracts Meaning

A Contract means:

```text
a stable Core agreement that defines shape, semantics, required fields, controlled values, validation rules and boundary behavior for implementation.
```

A Contract does not mean:

```text
database schema only
OpenAPI only
JSON sample only
UI form design
temporary mock data
product requirement
workflow description
agent prompt
```

Contract rule:

```text
Specifications define responsibility.
Contracts define enforceable shape.
Services execute behavior.
Events preserve trace.
```

---

# 3. Core Position

The Contracts layer sits between Core specifications and implementation.

Canonical position:

```text
Core Principles
↓
Domain / Object / Service / Event / API / Agent / Workflow Specs
↓
Contracts
↓
Validation
↓
Codex Implementation
↓
Tests
```

Contracts must cite their owning specs.

Implementation must cite contracts when building DTOs, validators, service inputs, API payloads, event payloads and agent runtime requests.

---

# 4. Contract Boundary

Contracts are responsible for:

```text
field naming
required/optional field rules
reference shape
controlled values
request/response shape
event payload shape
service input/output shape
agent runtime input/output shape
workflow application shape
validation constraints
error shape
version compatibility
```

Contracts are not responsible for:

```text
owning business truth
executing service behavior
deciding permission or policy result
creating events directly
choosing UI layout
choosing database technology
choosing AI model
```

---

# 5. Contract Governance Lock

All contracts must obey:

```text
Contract shape must preserve Core responsibility boundaries.
Contract fields must not silently merge domains.
Contract examples must not imply execution, approval, filing, payment, communication delivery, routing selection or professional truth unless the owning service explicitly defines it.
Contract validation must prevent ambiguous, unsafe or cross-boundary state mutation.
```

This lock applies to all contract files.

---

# 6. Directory Structure

Canonical directory:

```text
core-specs/contracts/
```

Recommended structure:

```text
core-specs/contracts/
  README.md
  _template.md

  common/
    references.md
    errors.md
    pagination.md
    audit-context.md
    ai-context.md
    human-review.md
    permission-context.md
    policy-context.md
    idempotency.md
    versioning.md

  api/
    identity-api-contract.md
    organization-api-contract.md
    user-api-contract.md
    permission-api-contract.md
    policy-api-contract.md
    knowledge-api-contract.md
    brand-api-contract.md
    trademark-api-contract.md
    jurisdiction-api-contract.md
    classification-api-contract.md
    document-api-contract.md
    evidence-api-contract.md
    customer-api-contract.md
    matter-api-contract.md
    order-api-contract.md
    opportunity-api-contract.md
    workflow-contract-api-contract.md
    task-api-contract.md
    event-api-contract.md
    notification-api-contract.md
    communication-api-contract.md
    agent-api-contract.md
    service-provider-api-contract.md
    routing-api-contract.md
    partner-api-contract.md
    service-network-api-contract.md

  services/
    identity-service-contract.md
    organization-service-contract.md
    user-service-contract.md
    permission-service-contract.md
    policy-service-contract.md
    knowledge-service-contract.md
    brand-service-contract.md
    trademark-service-contract.md
    jurisdiction-service-contract.md
    classification-service-contract.md
    document-service-contract.md
    evidence-service-contract.md
    customer-service-contract.md
    matter-service-contract.md
    order-service-contract.md
    opportunity-service-contract.md
    workflow-contract-service-contract.md
    task-service-contract.md
    event-service-contract.md
    notification-service-contract.md
    communication-service-contract.md
    agent-service-contract.md
    service-provider-service-contract.md
    routing-service-contract.md
    partner-service-contract.md
    service-network-service-contract.md

  events/
    identity-created-payload.md
    identity-updated-payload.md
    user-created-payload.md
    user-updated-payload.md
    organization-created-payload.md
    permission-evaluated-payload.md
    policy-evaluated-payload.md
    knowledge-record-created-payload.md
    knowledge-record-updated-payload.md
    brand-created-payload.md
    trademark-created-payload.md
    jurisdiction-linked-payload.md
    classification-created-payload.md
    document-created-payload.md
    evidence-created-payload.md
    customer-created-payload.md
    order-created-payload.md
    matter-created-payload.md
    task-created-payload.md
    workflow-contract-applied-payload.md
    notification-created-payload.md
    communication-created-payload.md
    agent-created-payload.md
    service-provider-created-payload.md
    routing-evaluated-payload.md
    routing-selected-payload.md
    partner-created-payload.md
    service-network-linked-payload.md

  agents/
    agent-runtime-contract.md
    ai-agent-governance-contract.md
    knowledge-agent-contract.md
    task-agent-contract.md
    communication-agent-contract.md
    workflow-agent-contract.md
    routing-agent-contract.md
    audit-agent-contract.md

  workflows/
    workflow-application-contract.md
    workflow-step-contract.md
    workflow-task-plan-contract.md
```

---

# 7. Contract Categories

## 7.1 Common Contracts

Common contracts define reusable shapes:

```text
reference contract
audit context
permission context
policy context
AI context
human review context
idempotency contract
pagination contract
error contract
versioning contract
```

Common contracts must not contain domain-specific business logic.

## 7.2 API Contracts

API contracts define:

```text
request path parameters
query parameters
headers
request body
response body
error response
idempotency behavior
pagination behavior
permission/policy context fields
AI access context where applicable
```

API contracts must cite the owning API spec.

## 7.3 Service Contracts

Service contracts define:

```text
service input
service output
service-side validation
required related references
permission and policy decision references
event emission expectations
service error shape
```

Service contracts must cite the owning service spec.

## 7.4 Event Payload Contracts

Event contracts define:

```text
event_type
event_id
producer service
occurred_at
subject reference
payload fields
required references
controlled values
restricted fields
consumer expectations
versioning rules
```

Event payload contracts must cite the owning Event spec.

## 7.5 Agent Contracts

Agent contracts define:

```text
agent identity context
agent registry key
agent capability request
agent data access scope
AI context shape
human review requirement
agent output shape
restricted-data handling
trace fields
```

Agent contracts must cite AI Agent Governance and Agent Registry.

## 7.6 Workflow Contracts

Workflow contracts define:

```text
workflow application shape
workflow step shape
workflow task plan shape
workflow preconditions
workflow result context
workflow event trace references
```

Workflow contracts must cite Workflow Contract domain/service specs.

---

# 8. Naming Rules

Contract file names must be lowercase kebab-case.

Examples:

```text
agent-runtime-contract.md
communication-api-contract.md
routing-selected-payload.md
workflow-application-contract.md
permission-context.md
```

Rules:

```text
- API contract files end with -api-contract.md.
- Service contract files end with -service-contract.md.
- Event payload contract files end with -payload.md.
- Agent contract files end with -agent-contract.md or -contract.md where global.
- Common contract files use the common concept name.
```

---

# 9. Contract Metadata Rules

Each contract file must include:

```yaml
Spec ID: string
Spec Type: Contract Specification
Contract Name: string
Contract File: string
Related Owning Spec: string
Related Domain: string | null
Related Object Specs: list[string]
Related Service Specs: list[string]
Related API Specs: list[string]
Related Event Specs: list[string]
Status: Draft | Active | Deprecated | Archived
Version: string
Contract Version: string
Owner: string
```

Rules:

```text
- Metadata must cite the owning spec.
- Contract Version must be explicit.
- Status must be controlled.
- Related specs must be real planned files or existing files.
```

---

# 10. Standard Contract Sections

Each detailed contract should use this structure unless the contract type requires a narrower template:

```text
1. Purpose
2. Contract Meaning
3. Contract Boundary
4. Related Owning Spec
5. Related Core Objects
6. Required References
7. Contract Shape
8. Field Rules
9. Controlled Values
10. Validation Rules
11. Permission Rules
12. Policy Rules
13. AI Agent Rules
14. Event Rules
15. Error Rules
16. Versioning Rules
17. Codex Implementation Notes
18. Acceptance Criteria
19. Revision Notes
```

Event payload contracts may use a shorter event-focused structure.

Common contracts may omit AI/Event rules where not applicable but must explicitly state non-applicability.

---

# 11. Required Common Fields

Most contracts should support these common fields where applicable:

```yaml
reference_id: string
actor_reference_id: string | null
organization_reference_id: string | null
agent_reference_id: string | null
agent_contract_reference_id: string | null
target_object_type: string | null
target_object_reference_id: string | null
permission_decision_reference_id: string | null
policy_decision_reference_id: string | null
human_review_reference_id: string | null
correlation_id: string | null
idempotency_key: string | null
created_at: datetime | null
updated_at: datetime | null
schema_version: string
```

Rules:

```text
- Fields must be included only where meaningful.
- Nullability must be explicit.
- Reference fields must use reference_id pattern.
- Ambiguous object IDs are not allowed.
```

---

# 12. Reference Rules

Core references must be explicit:

```text
identity_reference_id
organization_reference_id
user_reference_id
permission_reference_id
policy_reference_id
knowledge_record_reference_id
brand_reference_id
trademark_reference_id
jurisdiction_reference_id
classification_reference_id
document_reference_id
evidence_reference_id
customer_reference_id
matter_reference_id
order_reference_id
opportunity_reference_id
workflow_contract_reference_id
task_reference_id
event_reference_id
notification_reference_id
communication_reference_id
agent_reference_id
service_provider_reference_id
routing_reference_id
partner_reference_id
service_network_reference_id
```

Rules:

```text
- Do not use generic id when the domain meaning is known.
- Do not reuse one domain reference as another domain reference.
- Cross-domain references must be validated by owning services.
- Deleted or archived references must follow owning domain policy.
```

---

# 13. Permission and Policy Rules

Contracts must not grant permission or policy authority.

Rules:

```text
- Contracts may require permission_decision_reference_id.
- Contracts may require policy_decision_reference_id.
- Contracts may define required permission keys.
- Contracts may define required policy scopes.
- Contracts must not define final permission or policy evaluation logic unless they are Permission/Policy contracts.
```

Required pattern:

```text
contract request
↓
permission context
↓
policy context
↓
owning service validation
↓
service behavior
↓
event trace
```

---

# 14. AI Agent Contract Rules

Any contract involving AI Agent operations must include:

```yaml
ai_context:
  ai_assisted: boolean
  agent_reference_id: string | null
  agent_registry_key: string | null
  agent_contract_reference_id: string | null
  data_access_scope: string | null
  output_mode: string | null
  human_review_required: boolean | null
```

Rules:

```text
- AI-generated output must be marked.
- Data access scope must be explicit.
- Human review requirement must be explicit.
- Agent output must not be treated as final professional truth by default.
- Restricted data must not be included unless policy allows it.
```

---

# 15. Human Review Contract Rules

Human review contracts should include:

```yaml
human_review_reference_id: string
reviewer_user_reference_id: string
review_scope: string
review_decision: Approved | Rejected | Revised | Escalated
reviewed_at: datetime
review_notes_safe: string | null
```

Rules:

```text
- Human review must be explicit.
- Human review must not be implied by login.
- Human review must be traceable where downstream actions depend on it.
- Sensitive review notes must be safe by default.
```

---

# 16. Event Contract Rules

Event payload contracts must:

```text
cite owning Event spec
define event_type
define producer service
define subject reference
define payload fields
define restricted fields
define consumer expectations
define versioning rules
```

Event payload contracts must not:

```text
execute command
mutate state
grant permission
replace service validation
expose restricted payload by default
```

---

# 17. Validation Rules

All contracts must define validation rules.

Validation must cover:

```text
required fields
field types
controlled values
reference validity
state compatibility
permission context
policy context
AI context where applicable
human review where required
event behavior where applicable
idempotency where applicable
error response shape
version compatibility
```

Validation failure must produce controlled errors.

---

# 18. Error Contract Rules

All contract errors must follow safe error shape:

```yaml
error:
  code: string
  category: string
  message: string
  safe_detail: string | null
  correlation_id: string | null
  retryable: boolean
```

Rules:

```text
- Errors must be safe to display.
- Errors must not expose restricted data.
- Errors must not expose permission/policy internals.
- Errors must preserve correlation_id where available.
```

---

# 19. Versioning Rules

Contracts must be versioned.

Rules:

```text
- Contract Version must use semantic versioning.
- Breaking field changes require a version change.
- Controlled value additions must be documented.
- Field removals require migration plan.
- Event payload changes must preserve consumer safety.
- API contracts must map to API version.
```

---

# 20. Codex Implementation Rules

Codex must:

```text
cite the owning spec and contract before implementation
generate typed DTOs or equivalent structures from contracts
generate validators from validation rules
use controlled values exactly
validate references through owning services
preserve correlation_id
enforce idempotency where required
return safe error shape
write tests for required fields
write tests for controlled values
write tests for invalid references
write tests for permission denied
write tests for policy restricted
write tests for AI/human review rules where applicable
```

Codex must not:

```text
invent fields outside contracts without updating contract
merge unrelated domains into one payload
treat examples as permission grants
skip validation for convenience
expose restricted fields in errors
emit events directly from API payloads
allow AI output to bypass contract rules
```

---

# 21. Acceptance Criteria

The Contracts README is accepted only if:

```text
[ ] It defines the purpose of the Contracts layer.
[ ] It defines contract meaning.
[ ] It defines Core position.
[ ] It defines contract boundary.
[ ] It defines governance lock.
[ ] It defines directory structure.
[ ] It defines contract categories.
[ ] It defines naming rules.
[ ] It defines metadata rules.
[ ] It defines standard contract sections.
[ ] It defines common fields.
[ ] It defines reference rules.
[ ] It defines permission and policy rules.
[ ] It defines AI Agent contract rules.
[ ] It defines human review contract rules.
[ ] It defines event contract rules.
[ ] It defines validation rules.
[ ] It defines error contract rules.
[ ] It defines versioning rules.
[ ] It defines Codex implementation rules.
```

---

# 22. Revision Notes

| Version | Status | Notes |
|---------|--------|-------|
| 0.1.0 | Draft | Initial Contracts layer README. Defines purpose, directory structure, categories, naming, metadata, standard sections, reference rules, AI/human-review/event rules, validation, errors, versioning and Codex implementation boundaries. |

---

## Status/Workflow Contract and Fixture Layers

The Contract Layer Map includes [Status Contracts](status/index.md), [Workflow Component Contracts](workflows/components/index.md), and the [Status Workflow Fixture Pack](fixtures/status-workflow/index.md).

Status Contracts consume Controlled State Value Specifications. Workflow Component Contracts consume Workflow Component Specifications. Fixtures demonstrate deterministic contract behavior. Validators verify publication consistency. None of these layers owns domain state or performs mutation.

Implementation order is Specification -> Contract -> API/Workflow/Test consumption -> Fixture -> Validator -> future typed implementation. Acceptance requires canonical values and transition matrices to remain parent-owned and owning Services to remain mutation authorities.

**End of Contracts README**
