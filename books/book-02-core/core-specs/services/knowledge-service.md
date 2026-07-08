# Service Specification — Knowledge Service

**Spec ID:** B02-SVC-KNOWLEDGE-SERVICE  
**Spec Type:** Service  
**Service Name:** Knowledge Service  
**Owning Domain:** Knowledge  
**Domain Category:** Foundation Domain  
**Source Chapter:** B02-CH-20 — Knowledge Specification; B02-CH-24 — Service Specification  
**Source Domain Spec:** core-specs/domains/knowledge.md  
**Related Object Specs:** core-specs/objects/knowledge.md; core-specs/objects/document.md; core-specs/objects/evidence.md; core-specs/objects/policy.md; core-specs/objects/jurisdiction.md  
**Related Service Specs:** core-specs/services/document-service.md; core-specs/services/evidence-service.md; core-specs/services/policy-service.md; core-specs/services/jurisdiction-service.md; core-specs/services/identity-service.md  
**Related Event Specs:** core-specs/events/knowledge-created.md; core-specs/events/knowledge-updated.md; core-specs/events/knowledge-status-changed.md; core-specs/events/knowledge-source-linked.md; core-specs/events/knowledge-reference-validated.md  
**Related Contract Specs:** core-specs/contracts/knowledge/knowledge-contract.md; core-specs/contracts/knowledge/knowledge-source-contract.md; core-specs/contracts/knowledge/knowledge-validation-contract.md; core-specs/contracts/knowledge/knowledge-access-contract.md; core-specs/contracts/knowledge/authorized-knowledge-contract.md  
**Status:** Draft  
**Version:** 0.1.0  
**MVP Phase:** Phase 1 — Foundation Core  
**MVP Wave:** Wave 1  
**MVP Depth:** Must Implement  
**Owner:** MarkOrbit Publications Editorial Board  

---

# 1. Purpose

Knowledge Service defines the Core service boundary for creating, updating, validating, retrieving and governing Knowledge objects.

It exists so that Domains, Services, AI Agents, Workflow Contracts, Policies, Documents, Evidence, Jurisdictions, APIs and product consumers can consistently reference governed professional knowledge without confusing Knowledge with Document, Evidence, AI Output, raw web content, unreviewed notes or professional final judgment.

Knowledge Service is required before:

```text
governed knowledge registration
knowledge source tracking
jurisdiction reference guidance
document/evidence knowledge extraction boundary
AI authorized knowledge retrieval
knowledge status and version management
knowledge access policy enforcement
professional reference validation
Codex-safe knowledge consumption
audit trace for knowledge-sensitive actions
```

---

# 2. Core Meaning

Knowledge Service means:

```text
the Core service that manages governed professional reference knowledge, including source, scope, status, validation, version, access and AI-authorized usage.
```

Knowledge Service does not mean:

```text
Document Service
Evidence Service
AI output service
web search service
legal advice engine
professional judgment engine
content management system
large language model memory
```

Knowledge Service answers:

```text
Does this Knowledge object exist?
What source and scope support it?
Is it active, draft, review-required, deprecated or archived?
Can this actor or AI Agent access it?
Can this Knowledge be used for a jurisdiction, service, workflow or AI operation?
Which Document or Evidence source references support it?
What audit trace is required?
```

---

# 3. Service Category

Knowledge Service is a Foundation Core Service.

It is the governed reference service.

It does not replace professional judgment.

It does not convert Document or Evidence automatically.

It does not make final legal conclusions.

---

# 4. Architectural Position

Knowledge Service sits between source materials and professional/AI consumption.

```text
Document / Evidence / Source provides material
        ↓
Knowledge Service registers governed reference
        ↓
Policy controls access and use
        ↓
Domain Services and AI Agents consume authorized Knowledge
        ↓
Professional review remains required where conclusions matter
        ↓
Event and Audit preserve trace
```

Knowledge informs.

AI may consume authorized Knowledge.

Professionals decide.

---

# 5. Scope

Knowledge Service includes:

```text
knowledge creation
knowledge update
knowledge status management
knowledge source linkage
knowledge scope linkage
knowledge version/reference management
knowledge access validation
knowledge reference validation
authorized knowledge retrieval
knowledge audit trace
knowledge event emission
```

MVP scope includes:

```text
create knowledge
get knowledge
update knowledge metadata
change knowledge status
link knowledge source
validate knowledge reference
retrieve authorized knowledge
emit knowledge events
```

Deferred scope includes:

```text
full knowledge graph engine
semantic retrieval optimization
automatic legal rule extraction
automatic knowledge approval
external research crawler
advanced source reliability scoring
multi-version legal citator
```

---

# 6. Service Operations

| Operation | Purpose | MVP | Emits Event |
|----------|---------|-----|-------------|
| createKnowledge | Create Knowledge object | Yes | KnowledgeCreated |
| getKnowledge | Retrieve Knowledge by ID | Yes | No |
| updateKnowledge | Update governed metadata | Yes | KnowledgeUpdated |
| changeKnowledgeStatus | Change Knowledge lifecycle status | Yes | KnowledgeStatusChanged |
| linkKnowledgeSource | Link source Document/Evidence/Reference | Yes | KnowledgeSourceLinked |
| unlinkKnowledgeSource | Remove governed source link | Partial | KnowledgeSourceUnlinked |
| validateKnowledgeReference | Validate whether Knowledge can be referenced | Yes | KnowledgeReferenceValidated |
| retrieveAuthorizedKnowledge | Retrieve Knowledge under access/policy constraints | Yes | KnowledgeAccessed |
| archiveKnowledge | Archive Knowledge reference | Partial | KnowledgeArchived |

---

# 7. Inputs

Knowledge Service accepts:

```text
knowledge_type
title_reference
status
scope_reference
jurisdiction_reference_id
source_reference
source_type
source_object_reference_id
version_reference
access_policy_reference_id
metadata
actor_context
request_context
```

Required for creation:

```text
knowledge_type
title_reference
status
source_reference
scope_reference
actor_context
```

Required for source linkage:

```text
knowledge_reference_id
source_type
source_object_reference_id
source_reference
actor_context
```

Required for authorized retrieval:

```text
knowledge_reference_id or query_context
requesting_actor_reference_id
requesting_service
requesting_purpose
request_context
```

Required for validation:

```text
knowledge_reference_id
requesting_domain
requesting_service
actor_context
```

---

# 8. Outputs

Knowledge Service returns:

```text
Knowledge object
Knowledge reference
Knowledge validation result
Authorized Knowledge result
Knowledge source link result
Knowledge status result
Knowledge event reference
error result
```

Authorized Knowledge output must include:

```text
is_authorized
knowledge_reference_id
knowledge_type
status
scope_reference
source_summary
version_reference
usage_constraints
reason_code
```

Authorized Knowledge output must not expose restricted source material or confidential client data unnecessarily.

---

# 9. Controlled Values

## 9.1 knowledge_type

```text
JurisdictionRule
ProcedureGuide
ClassificationGuide
DocumentRequirement
EvidenceRequirement
WorkflowGuidance
ServiceGuidance
PolicyReference
ProfessionalNote
TemplateGuidance
FAQ
Unknown
```

## 9.2 status

```text
Draft
Active
ReviewRequired
Deprecated
Archived
DeletedReferenceOnly
```

## 9.3 source_type

```text
Document
Evidence
OfficialSource
InternalNote
ProfessionalReview
Template
ExternalReference
AIExtractionDraft
Unknown
```

## 9.4 authorization_result

```text
Authorized
Denied
Restricted
ReviewRequired
NotFound
Deprecated
Archived
Unknown
```

## 9.5 usage_constraint

Suggested controlled values:

```text
ReferenceOnly
InternalUse
AIAllowed
AIRestricted
HumanReviewRequired
NoExternalDisclosure
DeprecatedUseWarning
Unknown
```

---

# 10. Service Rules

## 10.1 Knowledge Requires Source and Scope

Every Knowledge object must have source reference and scope reference.

Unsourced notes are not Core-valid Knowledge.

## 10.2 Knowledge Is Not Document

Document is the professional artifact layer.

Knowledge may be derived from Document only through Knowledge Service with source, scope and status.

## 10.3 Knowledge Is Not Evidence

Evidence is proof layer.

Knowledge may reference Evidence but does not replace proof purpose or evidence review.

## 10.4 Knowledge Is Not AI Output

AI may extract or summarize candidate knowledge.

AI output becomes Knowledge only through governed registration and review where required.

## 10.5 Knowledge Does Not Replace Professional Judgment

Knowledge provides governed reference.

Professional conclusions, legal strategy and final advice require professional review where applicable.

## 10.6 Knowledge Access Must Be Policy-Governed

Knowledge retrieval and AI use must respect Permission, Policy, source constraints and authorized knowledge contracts.

## 10.7 Knowledge Changes Must Be Auditable

Knowledge-sensitive operations must preserve actor, source, request context, version and event trace.

---

# 11. Relationships

| Related Service/Object | Relationship | Boundary |
|------------------------|--------------|----------|
| Document Service | May provide source material | Document owns artifact lifecycle. |
| Evidence Service | May provide proof source | Evidence owns proof layer. |
| Policy Service | Controls access/use constraints | Policy owns contextual constraint. |
| Jurisdiction Service | May scope Knowledge | Jurisdiction owns procedural territory. |
| Classification Service | May consume classification guidance | Classification owns goods/services scope. |
| Workflow Contract | May reference workflow guidance | Workflow owns transition structure. |
| AI Agent Governance | Consumes Authorized Knowledge | Agent Contract governs AI use. |
| Audit Service | Records Knowledge-sensitive action | Audit owns accountability trail. |
| Event Service | Records Knowledge events | Event records occurrence. |

---

# 12. Event Usage

Knowledge Service emits:

```text
KnowledgeCreated
KnowledgeUpdated
KnowledgeStatusChanged
KnowledgeSourceLinked
KnowledgeSourceUnlinked
KnowledgeAccessed
KnowledgeArchived
KnowledgeReferenceValidated
```

Event rules:

```text
- Mutating operations must emit events.
- Access events may be emitted where audit requires.
- Events must reference Knowledge ID.
- Source link events must reference source object type and ID.
- Events must not expose restricted source content unnecessarily.
- AI knowledge access events must identify AI source where applicable.
```

---

# 13. API Usage

Potential Phase 1 APIs:

```text
POST /knowledge
GET /knowledge/{id}
PATCH /knowledge/{id}
POST /knowledge/{id}/status
POST /knowledge/{id}/sources
DELETE /knowledge/{id}/sources/{sourceId}
POST /knowledge/reference/validate
POST /knowledge/authorized-retrieve
```

API rules:

```text
- APIs must invoke Knowledge Service operations.
- APIs must not convert Document or Evidence into Knowledge automatically.
- APIs must not expose restricted source material.
- APIs must not make final legal conclusions.
- APIs must preserve actor context and audit context.
- AI-facing APIs must respect Agent Contract and Authorized Knowledge rules.
```

---

# 14. AI Agent Usage

AI Agents may use Knowledge Service only under governed Agent Contracts.

Allowed AI use:

```text
retrieve authorized knowledge
summarize authorized knowledge
identify missing source or scope
draft candidate knowledge for review
flag deprecated or review-required knowledge
suggest related knowledge references
prepare knowledge update note for human review
```

AI must not:

```text
treat AI output as approved Knowledge
access restricted Knowledge without authorization
remove source constraints
make final legal conclusion from Knowledge alone
publish external advice without review where required
silently update Knowledge status
invent source references
```

AI Knowledge use requires:

```text
Agent Identity
Agent Contract
Authorized Knowledge Rule
Permission Rule
Policy Rule
Knowledge Access Rule
Source Visibility Rule
Audit Rule
Human Review Rule for knowledge creation, approval or external advice
```

---

# 15. Validation Rules

Knowledge Service must enforce:

```text
[ ] knowledge_type is controlled.
[ ] status is controlled.
[ ] source_type is controlled.
[ ] createKnowledge requires source_reference.
[ ] createKnowledge requires scope_reference.
[ ] createKnowledge produces stable immutable Knowledge ID.
[ ] updateKnowledge does not mutate immutable ID.
[ ] changeKnowledgeStatus follows allowed lifecycle.
[ ] linkKnowledgeSource references valid source where applicable.
[ ] retrieveAuthorizedKnowledge enforces Permission and Policy.
[ ] Knowledge Service does not convert Document/Evidence automatically.
[ ] Knowledge Service does not treat AI output as approved Knowledge.
[ ] Knowledge Service does not replace professional judgment.
[ ] Knowledge Service emits events for mutation.
[ ] AI use is contract-governed.
```

---

# 16. Error Handling

Knowledge Service should return controlled errors:

```text
KnowledgeNotFound
InvalidKnowledgeType
InvalidKnowledgeStatus
InvalidKnowledgeTransition
InvalidKnowledgeReference
SourceRequired
ScopeRequired
InvalidSourceReference
AccessDenied
AccessRestricted
ReviewRequired
DeprecatedKnowledge
ArchivedKnowledge
PermissionRequired
PolicyRestricted
AuditContextMissing
UnknownKnowledgeError
```

Errors must be safe for product display and API consumption.

Restricted knowledge content, source material and protected client information must not be exposed unnecessarily.

---

# 17. Codex Implementation Notes

Codex must:

```text
cite this service spec
cite knowledge domain spec
cite knowledge object spec
cite policy service spec
preserve Knowledge / Document boundary
preserve Knowledge / Evidence boundary
preserve Knowledge / AI Output boundary
preserve Knowledge / Professional Judgment boundary
implement only Phase 1 MVP operations unless task says otherwise
write tests for createKnowledge requiring source_reference
write tests for createKnowledge requiring scope_reference
write tests for controlled knowledge_type
write tests for controlled status
write tests for controlled source_type
write tests preventing Document/Evidence from becoming Knowledge automatically
write tests preventing AI output from becoming approved Knowledge
write tests for authorized retrieval enforcing Permission/Policy
write tests for event emission on mutation
```

Codex must not:

```text
invent full knowledge graph engine in Phase 1
implement web crawler or legal research engine
convert uploaded documents into Knowledge automatically
convert AI extraction into approved Knowledge automatically
make final legal conclusion from Knowledge Service
expose restricted source content by default
allow AI to bypass Authorized Knowledge contracts
allow product UI to redefine Knowledge status
```

---

# 18. Acceptance Criteria

This Knowledge Service Specification is accepted only if:

```text
[ ] It defines Knowledge Service purpose.
[ ] It defines Knowledge Service Core meaning.
[ ] It identifies Knowledge Service as Foundation Core Service.
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
| 0.1.0 | Draft | Initial Knowledge Service specification. Establishes Knowledge Service as governed reference service, separates Knowledge from Document, Evidence, AI Output and professional judgment, and defines Phase 1 MVP operations, events, APIs, AI usage and Codex constraints. |

---

**End of Service Specification**
