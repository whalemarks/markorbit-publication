# Core Specs — API README

**Spec ID:** B02-API-README  
**Spec Type:** API Index / API Governance README  
**File:** core-specs/api/README.md  
**Status:** Draft  
**Version:** 0.1.0  
**MVP Phase:** Cross-Phase  
**Owner:** MarkOrbit Publications Editorial Board  

---

# 1. Purpose

This directory defines the **Core API Specification Layer** for MarkOrbit.

The API layer exists to expose Core capabilities through governed interface contracts without allowing product UI, integrations, AI Agents or implementation details to redefine Core architecture.

API specs describe:

```text
what Core operations may be exposed
what objects may be referenced
what events may be observed
what permissions and policies must be evaluated
what payloads are allowed
what errors are controlled
what AI Agents may or may not invoke
```

API specs do not define product screens, database tables, UI flows, commercial pricing, payment logic or local implementation shortcuts.

---

# 2. Core API Position

The Core API layer sits between:

```text
Core Services
↓
Core API Contracts
↓
Workplace / Products / Integrations / AI Agents
```

Canonical position:

```text
Principles define.
Core provides.
Business owns.
Execution coordinates.
Integration connects.
Products consume.
```

The API layer is a consumption boundary.

It does not own domain meaning.

Domain meaning is defined by:

```text
core-specs/domains/
core-specs/objects/
core-specs/services/
core-specs/events/
core-specs/contracts/
```

---

# 3. API Layer Responsibility

The API layer is responsible for:

```text
operation exposure
request validation
response shaping
reference validation
permission and policy enforcement entry points
event access boundaries
AI Agent invocation boundaries
error normalization
integration-safe contracts
versioned interface stability
```

The API layer is not responsible for:

```text
domain ownership
business truth
workflow ownership
database schema definition
product UI behavior
AI reasoning truth
professional legal conclusion
pricing/payment/finance ownership
```

---

# 4. API Governance Principles

## 4.1 API Must Follow Core

API must follow Core specs.

API must not invent domain meaning.

## 4.2 API Must Not Bypass Services

API must invoke Core Services for Core operations.

API must not write Core objects directly.

## 4.3 API Must Respect Permission and Policy

Every protected API operation must evaluate Permission and Policy where required.

API access is not permission by itself.

## 4.4 API Must Be Reference-First

API responses should prefer governed references, safe summaries and controlled values.

Raw confidential data must not be exposed by default.

## 4.5 API Must Be AI-Governed

AI Agents may call API operations only under Agent Contract, Permission, Policy and authorized context.

## 4.6 API Must Be Versioned

Breaking changes must create new API versions or explicit migration rules.

## 4.7 API Must Be Product-Neutral

API specs must not be written for only one UI, app, workflow board or customer portal.

---

# 5. API Spec File Naming

API specs should be named by Core capability or resource:

```text
identity-api.md
user-api.md
organization-api.md
permission-api.md
policy-api.md
knowledge-api.md
brand-api.md
trademark-api.md
jurisdiction-api.md
classification-api.md
document-api.md
evidence-api.md
customer-api.md
order-api.md
matter-api.md
workflow-contract-api.md
task-api.md
event-api.md
notification-api.md
communication-api.md
agent-api.md
service-provider-api.md
routing-api.md
partner-api.md
service-network-api.md
```

Cross-cutting APIs may use:

```text
capability-api.md
business-responsibility-api.md
validation-api.md
ai-agent-governance-api.md
```

---

# 6. Standard API Spec Structure

Each API spec should include:

```text
1. Purpose
2. API Meaning
3. API Boundary
4. Related Core Domain
5. Related Core Objects
6. Related Core Services
7. Related Core Events
8. API Operations
9. Request Contracts
10. Response Contracts
11. Controlled Values
12. Permission Rules
13. Policy Rules
14. AI Agent Access Rules
15. Event Access Rules
16. Validation Rules
17. Error Handling
18. Versioning Rules
19. Codex Implementation Notes
20. Acceptance Criteria
21. Revision Notes
```

API specs may add domain-specific sections where necessary, but they must not weaken Core boundary rules.

---

# 7. Required API Operation Categories

API operations should be categorized as:

```text
Create
Read
Update
Archive
Link
Unlink
Evaluate
Validate
Search
List
Action
Export
Import
ObserveEvent
```

Operation category must be explicit.

Examples:

```text
POST /brands
GET /brands/{brand_id}
PATCH /brands/{brand_id}
POST /trademarks/{trademark_id}/jurisdictions
POST /permissions/evaluate
GET /events/{event_id}
```

---

# 8. API Request Rules

API requests must:

```text
include actor context where required
include organization context where required
use governed reference IDs
use controlled values
avoid raw confidential payload by default
declare operation intent
declare idempotency key for create operations where appropriate
include correlation ID where integration trace is required
```

API requests must not:

```text
embed secrets
bypass Permission
bypass Policy
create multiple Core objects silently unless operation explicitly defines it
treat AI input as approved professional fact
use product UI labels as Core status
```

---

# 9. API Response Rules

API responses must:

```text
return governed reference IDs
return controlled statuses
return safe summaries
return validation errors in controlled format
return related event references where appropriate
preserve request/correlation trace
hide restricted fields by default
```

API responses must not:

```text
expose credentials or secrets
expose restricted policy internals
expose restricted permission internals
expose raw document/evidence content by default
imply legal conclusion unless produced by governed professional process
convert AI output into Core truth automatically
```

---

# 10. Permission and Policy Rules

Every API spec must define:

```text
operation-level Permission requirements
resource-level Permission requirements
field-level visibility constraints
Policy evaluation requirements
AI Agent access requirements
error behavior for denied access
safe response behavior for restricted fields
```

Permission and Policy must remain separate:

```text
Permission determines allowed action.
Policy evaluates contextual constraints.
API enforces both as required.
```

---

# 11. Event Access Rules

APIs may expose Event references only through governed access.

Event access must:

```text
use event-api.md or domain-specific event listing operations
respect Permission
respect Policy
hide restricted event payload fields
distinguish Event from command
distinguish occurrence from workflow execution
```

APIs must not:

```text
allow clients to fabricate domain events
allow UI to emit Core events directly
expose restricted event payload internals
use events as task commands
use events as workflow execution commands
```

---

# 12. AI Agent API Access Rules

AI Agents may access APIs only if:

```text
Agent identity is known
Agent Contract exists where required
Permission is evaluated
Policy is evaluated
authorized knowledge scope is respected
human review is required where policy says so
API operation allows AI access
```

AI Agents must not:

```text
call protected operations without authorization
fabricate Core records or Events
turn suggestions into approved Core truth
bypass workflow gates
expose restricted data
rewrite audit/event history
```

---

# 13. Validation Rules

API validation must cover:

```text
request schema
required references
reference existence
reference ownership/access
controlled values
permission decision
policy decision
payload size and type
restricted fields
idempotency where required
event emission expectations
AI Agent contract requirements
```

Validation failure must return controlled errors.

---

# 14. Error Handling Rules

API errors must be controlled and safe.

Common error categories:

```text
BadRequest
Unauthorized
PermissionDenied
PolicyRestricted
NotFound
ReferenceInvalid
ValidationFailed
Conflict
DuplicateRejected
StateInvalid
PayloadTooLarge
RestrictedFieldViolation
AgentContractRequired
EventEmissionFailed
InternalError
```

Error responses must not expose:

```text
secrets
credentials
restricted policy internals
restricted permission internals
raw confidential documents
private customer data
privileged legal strategy
```

---

# 15. Versioning Rules

API specs must declare:

```text
api_version
supported status
breaking-change policy
deprecation policy
migration guidance
backward compatibility expectations
```

Version example:

```text
v1alpha
v1beta
v1
v2
```

Draft APIs may start as:

```text
v0.1.0
```

---

# 16. Directory Relationship

This API directory depends on:

```text
core-specs/domains/
core-specs/objects/
core-specs/services/
core-specs/events/
core-specs/contracts/
core-specs/agents/
core-specs/validation/
```

API specs must cross-reference the relevant files.

API specs must not duplicate full domain/object/service rules unless summarizing boundaries.

---

# 17. Codex Implementation Notes

Codex must:

```text
read the relevant API spec before implementing an endpoint
read the relevant Service spec before implementing behavior
read the relevant Object spec before defining payloads
read the relevant Event spec before emitting or exposing events
read Permission and Policy specs before protected operations
read AI Agent Governance specs before AI access
write tests for permission denial
write tests for policy restriction
write tests for restricted field hiding
write tests for invalid references
write tests for event emission behavior
write tests for AI Agent access restrictions
```

Codex must not:

```text
invent endpoint semantics from UI needs
write directly to database bypassing Core Service behavior
allow UI to emit Core events directly
treat API access as permission
treat AI output as approved Core data
expose restricted fields for convenience
merge Product workflow with Core API meaning
```

---

# 18. Acceptance Criteria

This README is accepted only if:

```text
[ ] It defines the purpose of the API layer.
[ ] It defines Core API position.
[ ] It defines API governance principles.
[ ] It defines API spec naming.
[ ] It defines standard API spec structure.
[ ] It defines request and response rules.
[ ] It defines Permission and Policy rules.
[ ] It defines Event access rules.
[ ] It defines AI Agent access rules.
[ ] It defines validation and error handling rules.
[ ] It defines versioning rules.
[ ] It includes Codex implementation notes.
```

---

# 19. Revision Notes

| Version | Status | Notes |
|---------|--------|-------|
| 0.1.0 | Draft | Initial API README. Defines Core API governance, boundaries, naming, operation categories, Permission/Policy requirements, Event access, AI Agent access and Codex implementation rules. |

---

**End of API README**
