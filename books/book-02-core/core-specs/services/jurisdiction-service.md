# Service Specification — Jurisdiction Service

**Spec ID:** B02-SVC-JURISDICTION-SERVICE  
**Spec Type:** Service  
**Service Name:** Jurisdiction Service  
**Owning Domain:** Jurisdiction  
**Domain Category:** Professional Domain  
**Source Chapter:** B02-CH-22 — Domain Specification; B02-CH-24 — Service Specification  
**Source Domain Spec:** core-specs/domains/jurisdiction.md  
**Related Object Specs:** core-specs/objects/jurisdiction.md; core-specs/objects/trademark.md; core-specs/objects/classification.md; core-specs/objects/agent.md; core-specs/objects/service-provider.md; core-specs/objects/routing.md  
**Related Service Specs:** core-specs/services/trademark-service.md; core-specs/services/classification-service.md; core-specs/services/knowledge-service.md; core-specs/services/policy-service.md; core-specs/services/routing-service.md  
**Related Event Specs:** core-specs/events/jurisdiction-created.md; core-specs/events/jurisdiction-updated.md; core-specs/events/jurisdiction-status-changed.md; core-specs/events/jurisdiction-rule-reference-linked.md; core-specs/events/jurisdiction-reference-validated.md  
**Related Contract Specs:** core-specs/contracts/jurisdiction/jurisdiction-contract.md; core-specs/contracts/jurisdiction/jurisdiction-reference-contract.md; core-specs/contracts/jurisdiction/jurisdiction-rule-reference-contract.md; core-specs/contracts/jurisdiction/jurisdiction-office-reference-contract.md; core-specs/contracts/jurisdiction/jurisdiction-validation-contract.md  
**Status:** Draft  
**Version:** 0.1.0  
**MVP Phase:** Phase 2 — Professional Core  
**MVP Wave:** Wave 2  
**MVP Depth:** Must Implement  
**Owner:** MarkOrbit Publications Editorial Board  

---

# 1. Purpose

Jurisdiction Service defines the Core service boundary for creating, updating, validating, resolving and managing Jurisdiction objects.

It exists so that Trademark, Classification, Document, Evidence, Matter, Order, Agent, Service Provider, Routing, Knowledge, Policy, AI Agents, APIs and product consumers can consistently reference where protection, procedure, filing, service scope or professional rule context applies without confusing Jurisdiction with a country dropdown, address country, fee engine, deadline engine, legal rule engine or routing decision engine.

Jurisdiction Service is required before:

```text
trademark jurisdiction planning
jurisdiction-specific trademark record creation
classification jurisdiction context
official office reference handling
jurisdiction rule reference linkage
document/evidence requirement scoping
agent and service provider coverage reference
routing input validation
AI jurisdiction guidance
audit trace for jurisdiction-sensitive actions
```

---

# 2. Core Meaning

Jurisdiction Service means:

```text
the Core service that manages professional territorial or procedural contexts and their governed references to rules, offices, service scopes, knowledge and downstream trademark execution.
```

Jurisdiction Service does not mean:

```text
country dropdown service
address normalization service
legal rule engine
fee engine
deadline engine
routing engine
agent selection service
official registry sync service
AI legal advice service
```

Jurisdiction Service answers:

```text
Does this Jurisdiction exist?
What jurisdiction type and status apply?
Which office or filing system reference applies?
Which Knowledge, Policy or rule references may apply?
Can this Jurisdiction be used for Trademark, Classification, Matter, Order or Routing context?
Is the Jurisdiction active, deprecated, review-required or archived?
What audit trace is required?
```

---

# 3. Service Category

Jurisdiction Service is a Professional Core Service.

It manages where-context for professional trademark work.

It does not calculate law, fees, deadlines or routing decisions.

It does not replace Knowledge, Policy, Routing, Agent or Service Provider services.

---

# 4. Architectural Position

Jurisdiction Service sits beside Trademark and Classification in professional architecture.

```text
Brand Service manages commercial identity
        ↓
Trademark Service manages protection object
        ↓
Jurisdiction Service defines where protection/procedure applies
        ↓
Classification Service defines goods/services scope
        ↓
Matter Service executes professional work
        ↓
Routing Service may use jurisdiction as candidate-selection input
```

Jurisdiction provides territorial/procedural context.

Knowledge provides governed reference.

Policy constrains use.

Routing decides candidate selection.

---

# 5. Scope

Jurisdiction Service includes:

```text
jurisdiction creation
jurisdiction update
jurisdiction status management
jurisdiction office reference linkage
jurisdiction parent/region linkage
jurisdiction rule/knowledge reference linkage
jurisdiction service scope linkage
jurisdiction reference validation
jurisdiction resolution
jurisdiction audit trace
jurisdiction event emission
```

MVP scope includes:

```text
create jurisdiction
get jurisdiction
update jurisdiction metadata
change jurisdiction status
link office reference
link rule/knowledge reference
link service scope reference
validate jurisdiction reference
resolve jurisdiction by code
emit jurisdiction events
```

Deferred scope includes:

```text
legal rule calculation
fee calculation
deadline calculation
official registry integration
country/address normalization engine
advanced jurisdiction hierarchy engine
jurisdiction risk scoring
automatic legal-rule extraction
```

---

# 6. Service Operations

| Operation | Purpose | MVP | Emits Event |
|----------|---------|-----|-------------|
| createJurisdiction | Create Jurisdiction object | Yes | JurisdictionCreated |
| getJurisdiction | Retrieve Jurisdiction by ID | Yes | No |
| updateJurisdiction | Update governed Jurisdiction metadata | Yes | JurisdictionUpdated |
| changeJurisdictionStatus | Change Jurisdiction lifecycle status | Yes | JurisdictionStatusChanged |
| linkJurisdictionOffice | Link office or filing authority reference | Yes | JurisdictionOfficeReferenceLinked |
| linkJurisdictionRuleReference | Link Knowledge/Policy/rule reference | Yes | JurisdictionRuleReferenceLinked |
| linkJurisdictionServiceScope | Link supported service scope | Yes | JurisdictionServiceScopeLinked |
| validateJurisdictionReference | Validate whether Jurisdiction can be referenced | Yes | JurisdictionReferenceValidated |
| resolveJurisdictionByCode | Resolve Jurisdiction from code/reference | Yes | No |
| archiveJurisdiction | Archive Jurisdiction reference | Partial | JurisdictionArchived |

---

# 7. Inputs

Jurisdiction Service accepts:

```text
jurisdiction_code
name_reference
jurisdiction_type
status
region_reference
parent_jurisdiction_id
office_reference_id
rule_reference_ids
knowledge_reference_ids
service_scope_references
source_reference
metadata
actor_context
request_context
```

Required for creation:

```text
jurisdiction_code
name_reference
jurisdiction_type
status
source_reference
actor_context
```

Required for rule/knowledge linkage:

```text
jurisdiction_reference_id
rule_or_knowledge_reference_id
link_type
actor_context
```

Required for validation:

```text
jurisdiction_reference_id
requesting_domain
requesting_service
actor_context
```

Required for resolution:

```text
jurisdiction_code or name_reference
requesting_domain
requesting_service
actor_context
```

---

# 8. Outputs

Jurisdiction Service returns:

```text
Jurisdiction object
Jurisdiction reference
Jurisdiction validation result
Jurisdiction resolution result
Jurisdiction status result
Jurisdiction office/rule/service-scope link result
Jurisdiction event reference
error result
```

Validation output must include:

```text
is_valid
jurisdiction_reference_id
jurisdiction_code
jurisdiction_type
status
reason_code
review_required
policy_hint where applicable
```

Validation output must not expose restricted rule content, provider data or confidential commercial references unnecessarily.

---

# 9. Controlled Values

## 9.1 jurisdiction_type

```text
National
Regional
International
Territory
Office
Custom
Unknown
```

## 9.2 status

```text
Draft
Active
ReviewRequired
Deprecated
Reserved
Archived
```

## 9.3 rule_link_type

```text
ProcedureRule
FilingRequirement
DocumentRequirement
EvidenceRequirement
ClassificationRequirement
OfficeReference
PolicyReference
KnowledgeReference
Unknown
```

## 9.4 validation_result

```text
Valid
Invalid
NotFound
Deprecated
Reserved
ReviewRequired
Archived
PolicyRestricted
Unknown
```

## 9.5 service_scope_type

```text
TrademarkFiling
TrademarkSearch
OfficeActionResponse
Renewal
Change
Assignment
Opposition
Cancellation
Recordal
EvidenceReview
DocumentReview
LegalOpinion
GeneralConsultation
Unknown
```

---

# 10. Service Rules

## 10.1 Jurisdiction Requires Code, Name and Type

Jurisdiction creation must require:

```text
jurisdiction_code
name_reference
jurisdiction_type
status
```

## 10.2 Jurisdiction Is Not a Country Dropdown

Jurisdiction may represent national, regional, international, territorial, office or custom procedural contexts.

UI country lists must consume Jurisdiction; they must not define it.

## 10.3 Jurisdiction Does Not Own Legal Rule Engine

Jurisdiction Service may link Knowledge, Policy or rule references.

It must not calculate final legal outcome, deadline, fee, registrability or official procedure by itself.

## 10.4 Jurisdiction Does Not Own Routing Decision

Jurisdiction may provide candidate context for Agent/Service Provider coverage.

Routing Service makes selection or recommendation decisions.

## 10.5 Deprecated or Reserved Jurisdictions Require Review

Deprecated, reserved, review-required or archived jurisdictions must not be used for new execution unless governed exception applies.

## 10.6 Jurisdiction References Must Be Source-Aware

Rule-sensitive jurisdiction references should preserve source and version references where available.

## 10.7 Jurisdiction Changes Must Be Auditable

Jurisdiction-sensitive operations must preserve actor, source, request context, version and event trace.

---

# 11. Relationships

| Related Service/Object | Relationship | Boundary |
|------------------------|--------------|----------|
| Trademark Service | Trademark must reference Jurisdiction | Trademark owns protection object. |
| Classification Service | Classification may be jurisdiction-specific | Classification owns goods/services scope. |
| Knowledge Service | Provides jurisdiction rules/guidance | Knowledge owns governed reference. |
| Policy Service | May constrain jurisdiction use | Policy owns contextual constraints. |
| Document Service | May use jurisdiction requirements | Document owns artifact lifecycle. |
| Evidence Service | May use jurisdiction requirements | Evidence owns proof layer. |
| Agent Service | May reference jurisdiction coverage | Agent owns collaborator profile. |
| Service Provider Service | May reference jurisdiction coverage | Provider owns capability profile. |
| Routing Service | Uses jurisdiction as routing input | Routing makes decision. |
| Audit Service | Records Jurisdiction-sensitive action | Audit owns accountability trail. |
| Event Service | Records Jurisdiction events | Event records occurrence. |

---

# 12. Event Usage

Jurisdiction Service emits:

```text
JurisdictionCreated
JurisdictionUpdated
JurisdictionStatusChanged
JurisdictionOfficeReferenceLinked
JurisdictionRuleReferenceLinked
JurisdictionKnowledgeLinked
JurisdictionServiceScopeLinked
JurisdictionArchived
JurisdictionReferenceValidated
```

Event rules:

```text
- Mutating operations must emit events.
- Validation events may be emitted where audit requires.
- Events must reference Jurisdiction ID.
- Rule/Knowledge link events must preserve source reference where allowed.
- Service scope events must not imply Routing decision.
- Events must not expose restricted Knowledge or Policy content unnecessarily.
```

---

# 13. API Usage

Potential Phase 2 APIs:

```text
POST /jurisdictions
GET /jurisdictions/{id}
PATCH /jurisdictions/{id}
POST /jurisdictions/{id}/status
POST /jurisdictions/{id}/office-reference
POST /jurisdictions/{id}/rule-references
POST /jurisdictions/{id}/service-scopes
POST /jurisdictions/reference/validate
POST /jurisdictions/resolve
```

API rules:

```text
- APIs must invoke Jurisdiction Service operations.
- APIs must not implement legal rule, deadline or fee engines.
- APIs must not make Routing selection.
- APIs must not create Agent or Service Provider directly.
- APIs must preserve Permission, Policy and audit context.
- AI-facing APIs must respect Agent Contract and Authorized Knowledge rules.
```

---

# 14. AI Agent Usage

AI Agents may use Jurisdiction Service only under governed Agent Contracts.

Allowed AI use:

```text
resolve jurisdiction by code or name
summarize jurisdiction context
identify missing jurisdiction reference
flag deprecated, reserved or review-required jurisdiction
suggest jurisdiction selection questions
summarize authorized jurisdiction Knowledge
identify jurisdiction/trademark/classification mismatch
prepare jurisdiction review note
```

AI must not:

```text
make final legal rule determination
calculate official deadline or fee as final truth
select Agent or Service Provider directly
override deprecated or reserved status
invent jurisdiction rules or official requirements
create Jurisdiction without authorized service
treat jurisdiction code as complete legal analysis
```

AI Jurisdiction use requires:

```text
Agent Identity
Agent Contract
Authorized Knowledge
Permission Rule
Policy Rule
Jurisdiction Access Rule
Knowledge Access Rule where applicable
Routing Rule where applicable
Audit Rule
Human Review Rule for professional legal conclusions
```

---

# 15. Validation Rules

Jurisdiction Service must enforce:

```text
[ ] jurisdiction_type is controlled.
[ ] status is controlled.
[ ] createJurisdiction requires jurisdiction_code.
[ ] createJurisdiction requires name_reference.
[ ] createJurisdiction produces stable immutable Jurisdiction ID.
[ ] updateJurisdiction does not mutate immutable ID.
[ ] changeJurisdictionStatus follows allowed lifecycle.
[ ] validateJurisdictionReference rejects missing, deprecated, reserved, archived or review-required jurisdictions where not allowed.
[ ] Jurisdiction Service does not implement legal rule engine.
[ ] Jurisdiction Service does not implement fee/deadline engine.
[ ] Jurisdiction Service does not make Routing decision.
[ ] Jurisdiction Service emits events for mutation.
[ ] AI use is contract-governed.
```

---

# 16. Error Handling

Jurisdiction Service should return controlled errors:

```text
JurisdictionNotFound
InvalidJurisdictionType
InvalidJurisdictionStatus
InvalidJurisdictionTransition
InvalidJurisdictionReference
JurisdictionCodeRequired
JurisdictionNameRequired
DuplicateJurisdictionCode
OfficeReferenceInvalid
RuleReferenceInvalid
KnowledgeReferenceInvalid
ServiceScopeInvalid
DeprecatedJurisdiction
ReservedJurisdiction
ReviewRequired
PermissionRequired
PolicyRestricted
AuditContextMissing
UnknownJurisdictionError
```

Errors must be safe for product display and API consumption.

Restricted legal/rule content and commercial provider data must not be exposed unnecessarily.

---

# 17. Codex Implementation Notes

Codex must:

```text
cite this service spec
cite jurisdiction domain spec
cite jurisdiction object spec
cite trademark and classification specs where relevant
preserve Jurisdiction / Trademark boundary
preserve Jurisdiction / Classification boundary
preserve Jurisdiction / Knowledge / Policy boundaries
preserve Jurisdiction / Routing boundary
implement only Phase 2 MVP operations unless task says otherwise
write tests for createJurisdiction requiring jurisdiction_code
write tests for createJurisdiction requiring name_reference
write tests for controlled jurisdiction_type
write tests for controlled status
write tests preventing Jurisdiction Service from implementing legal rule engine
write tests preventing fee/deadline calculation inside Jurisdiction Service
write tests preventing Jurisdiction Service from making Routing decisions
write tests for event emission on mutation
```

Codex must not:

```text
invent full legal rule engine in Phase 2
treat Jurisdiction as country dropdown only
implement fee or deadline calculation inside Jurisdiction Service
select Agent or Service Provider from Jurisdiction Service
create Agent/Service Provider directly
treat official source reference as validated Knowledge automatically
allow AI to make final jurisdiction legal conclusion
allow product UI to redefine Jurisdiction status
```

---

# 18. Acceptance Criteria

This Jurisdiction Service Specification is accepted only if:

```text
[ ] It defines Jurisdiction Service purpose.
[ ] It defines Jurisdiction Service Core meaning.
[ ] It identifies Jurisdiction Service as Professional Core Service.
[ ] It defines service operations.
[ ] It defines inputs and outputs.
[ ] It defines controlled values.
[ ] It defines service rules.
[ ] It defines relationships.
[ ] It defines event usage.
[ ] It defines API usage.
[ ] It defines AI Agent usage.
[ ] It defines validation rules.
[ ] It defines error handling.
[ ] It includes Codex implementation notes.
```

---

# 19. Revision Notes

| Version | Status | Notes |
|---------|--------|-------|
| 0.1.0 | Draft | Initial Jurisdiction Service specification. Establishes Jurisdiction Service as where/procedural-context service, separates it from country dropdowns, legal rule engines, fee/deadline engines and Routing, and defines Phase 2 MVP operations, events, APIs, AI usage and Codex constraints. |

---

**End of Service Specification**
