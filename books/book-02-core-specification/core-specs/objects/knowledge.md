# Object Specification — Knowledge

**Spec ID:** B02-OBJ-KNOWLEDGE  
**Spec Type:** Object  
**Object Name:** Knowledge  
**Owning Domain:** Knowledge  
**Domain Category:** Foundation Domain  
**Source Chapter:** B02-CH-20 — Knowledge Specification; B02-CH-22 — Domain Specification  
**Source Domain Spec:** core-specs/domains/knowledge.md  
**Related Object Specs:** core-specs/objects/knowledge-source.md; core-specs/objects/knowledge-reference.md; core-specs/objects/knowledge-fragment.md; core-specs/objects/knowledge-status.md; core-specs/objects/knowledge-scope.md; core-specs/objects/knowledge-version.md; core-specs/objects/knowledge-validation-record.md  
**Related Service Specs:** core-specs/services/knowledge-registration-service.md; core-specs/services/knowledge-reference-service.md; core-specs/services/knowledge-validation-service.md; core-specs/services/knowledge-version-service.md; core-specs/services/knowledge-access-service.md; core-specs/services/knowledge-reference-validation-service.md  
**Related Event Specs:** core-specs/events/knowledge-created.md; core-specs/events/knowledge-updated.md; core-specs/events/knowledge-validated.md; core-specs/events/knowledge-version-created.md; core-specs/events/knowledge-status-changed.md; core-specs/events/knowledge-reference-validated.md  
**Related Contract Specs:** core-specs/contracts/knowledge/knowledge-contract.md; core-specs/contracts/knowledge/knowledge-source-contract.md; core-specs/contracts/knowledge/knowledge-reference-contract.md; core-specs/contracts/knowledge/knowledge-validation-contract.md; core-specs/contracts/knowledge/knowledge-access-contract.md  
**Status:** Draft  
**Version:** 0.1.0  
**MVP Phase:** Phase 1 — Foundation Core  
**MVP Wave:** Wave 1  
**MVP Depth:** Must Implement  
**Owner:** MarkOrbit Publications Editorial Board  

---

# 1. Purpose

The Knowledge object defines the Core-recognized governed reference used to support professional reasoning, AI assistance, workflow guidance, document generation, evidence review, classification, jurisdiction rules and operational decision support.

It exists so that MarkOrbit can distinguish governed reference material from AI output, uploaded files, documents, evidence, opinions, communication messages or product content.

Knowledge is required before:

```text
AI grounded response
jurisdiction rule reference
classification guidance
office action reasoning support
document drafting support
evidence review support
workflow guidance
professional checklist
Codex implementation reference
product help and explanation
audit trace for knowledge-assisted action
```

---

# 2. Core Meaning

Knowledge means:

```text
a Core-recognized governed reference, source, fragment or structured knowledge item that may support professional work, AI assistance, workflow guidance or product explanation under source, scope, version, status and validation rules.
```

Knowledge is not:

```text
AI Output
Document
Evidence
Communication
User opinion
unverified uploaded file
product copy
legal conclusion
professional final decision
task
workflow
policy
```

Knowledge answers:

```text
What reference material is being used?
Where did it come from?
Which domain, jurisdiction, object or workflow does it support?
Is it validated, draft, deprecated or archived?
Which version applies?
Can AI use it?
Which confidence, source or review status applies?
What audit trace is required when it influences work?
```

---

# 3. Object Category

Knowledge is a Foundation Object owned by the Knowledge Domain.

It is a Core reference object.

It may support Professional Domains, Business Execution Domains, AI Agents, Workflows, Services, APIs and Products, but it must not replace professional judgment.

---

# 4. Architectural Position

Knowledge sits beside Policy and Capability as a governed reference layer.

```text
Knowledge provides governed reference
        ↓
AI may retrieve or summarize under contract
        ↓
Professional domains use it as support
        ↓
Workflow may reference it as guidance
        ↓
Service may cite it as source
        ↓
Human or governed service makes decision
        ↓
Event and Audit preserve trace
```

Knowledge supports.

It does not decide.

It does not execute.

It does not become evidence unless registered through Evidence.

It does not become document unless registered through Document.

---

# 5. Scope

The Knowledge object includes:

```text
knowledge id
knowledge type
knowledge title/reference
knowledge source reference
knowledge scope
knowledge jurisdiction reference
knowledge domain reference
knowledge status
knowledge version
knowledge validation status
knowledge confidence reference
knowledge fragment boundary
knowledge access boundary
AI usage boundary
source citation/reference
created time
updated time
audit metadata
```

MVP scope includes:

```text
knowledge id
knowledge type
title/reference
source reference
scope type
scope reference
domain reference
jurisdiction reference
status
version reference
validation status
AI usage allowed flag
created time
updated time
basic audit metadata
```

---

# 6. Field Specification

| Field | Type | Required | MVP | Notes |
|-------|------|----------|-----|-------|
| id | string | Yes | Yes | Stable immutable Knowledge ID. |
| knowledge_type | enum | Yes | Yes | Rule, Guide, Checklist, Precedent, SourceExcerpt, TemplateGuide, Glossary, FAQ, Unknown. |
| title_reference | string | Yes | Yes | Human-readable title or reference. |
| source_reference_id | string | Yes | Yes | Reference to Knowledge Source or source record. |
| source_uri | string | No | Partial | Source URI where permitted. |
| scope_type | enum | Yes | Yes | Global, Domain, Object, Jurisdiction, Workflow, Service, Product, Agent, Task. |
| scope_reference | string | No | Yes | Specific scope reference where applicable. |
| domain_reference | string | No | Yes | Related Core Domain reference. |
| jurisdiction_reference_id | string | No | Yes | Jurisdiction reference where applicable. |
| status | enum | Yes | Yes | Controlled Knowledge status. |
| validation_status | enum | Yes | Yes | Controlled validation status. |
| version_reference | string | No | Yes | Version or release reference. |
| confidence_level | enum | No | Partial | Confidence/use caution indicator. |
| ai_usage_allowed | boolean | Yes | Yes | Whether AI may use under contract. |
| human_review_required | boolean | No | Yes | Whether use requires human review. |
| metadata | object | No | Yes | Non-sensitive metadata only. |
| created_at | datetime | Yes | Yes | Creation timestamp. |
| updated_at | datetime | Yes | Yes | Last update timestamp. |
| created_by | string | No | Yes | Identity or system actor reference. |
| updated_by | string | No | Yes | Identity or system actor reference. |

---

# 7. Controlled Values

## 7.1 knowledge_type

MVP controlled values:

```text
Rule
Guide
Checklist
Precedent
SourceExcerpt
TemplateGuide
Glossary
FAQ
Unknown
```

## 7.2 scope_type

MVP controlled values:

```text
Global
Domain
Object
Jurisdiction
Workflow
Service
Product
Agent
Task
```

## 7.3 status

MVP controlled values:

```text
Draft
Active
ReviewRequired
Deprecated
Archived
DeletedReferenceOnly
```

## 7.4 validation_status

MVP controlled values:

```text
Unvalidated
SourceRecorded
Reviewed
Validated
Rejected
Expired
NeedsUpdate
```

## 7.5 confidence_level

MVP controlled values:

```text
Low
Medium
High
OfficialSource
ProfessionalReviewed
Unknown
```

---

# 8. Object Rules

## 8.1 Knowledge Requires Source

Every Knowledge object must reference a source.

Source may be official, professional, internal, imported, generated or manually curated, but it must be identified.

Un sourced Knowledge is not Core-valid.

## 8.2 Knowledge Requires Scope

Every Knowledge object must define scope.

Scope prevents generic reference material from being used in the wrong domain, jurisdiction, workflow or AI context.

## 8.3 Knowledge Does Not Replace Professional Judgment

Knowledge supports decision-making.

It is not final legal conclusion, trademark strategy or professional advice by itself.

## 8.4 Knowledge Is Not AI Output

AI may produce summaries, drafts or extractions based on Knowledge.

Those outputs remain AI Output and must not overwrite Knowledge unless registered, reviewed and validated through Knowledge services.

## 8.5 Knowledge Is Not Document or Evidence

A source file or excerpt may support Knowledge.

It becomes Document only through Document services.

It becomes Evidence only through Evidence services.

## 8.6 Knowledge Must Be Version-Aware

Knowledge that may affect professional execution should preserve version/source references.

Deprecated or expired Knowledge must not be used by new AI or workflow actions unless explicitly allowed.

## 8.7 Knowledge Must Be Auditable

Knowledge-sensitive actions must preserve audit trace.

Audit-sensitive actions include:

```text
knowledge creation
source update
status change
validation
version creation
AI usage
deprecated knowledge access
knowledge deletion/reference archival
```

---

# 9. Relationships

| Related Object | Relationship | Rule |
|----------------|--------------|------|
| Knowledge Source | Knowledge must reference source | Source provenance is required. |
| Jurisdiction | Knowledge may be jurisdiction-scoped | Jurisdiction remains domain object. |
| Classification | Knowledge may support classification | Knowledge does not approve classification. |
| Trademark | Knowledge may support trademark analysis | Knowledge does not decide legal status. |
| Document | Knowledge may reference documents | Document remains artifact. |
| Evidence | Knowledge may support evidence review | Evidence remains proof layer. |
| Policy | Policy may constrain Knowledge use | Policy remains contextual rule. |
| Capability | Capability may depend on Knowledge | Capability remains ability descriptor. |
| Workflow Contract | Workflow may reference Knowledge | Workflow remains process structure. |
| Task | Task may require Knowledge reference | Task remains work unit. |
| AI Agent | AI may consume Knowledge | AI Governance controls use. |
| Event | Knowledge changes may emit Events | Event remains signal. |
| Audit Record | Audit may reference Knowledge | Audit remains accountability system. |

---

# 10. Lifecycle

Knowledge lifecycle states:

```text
Draft
Active
ReviewRequired
Deprecated
Archived
DeletedReferenceOnly
```

Lifecycle rules:

```text
Draft → ReviewRequired
Draft → Active
ReviewRequired → Active
ReviewRequired → Deprecated
Active → Deprecated
Deprecated → Archived
Draft → Archived
Archived → DeletedReferenceOnly
```

Prohibited lifecycle behavior:

```text
Archived → Active without restoration service and review
Deprecated → Active without revalidation or new version
DeletedReferenceOnly → Active
```

Validation lifecycle states:

```text
Unvalidated
SourceRecorded
Reviewed
Validated
Rejected
Expired
NeedsUpdate
```

---

# 11. Service Usage

Knowledge object is created and managed through:

```text
Knowledge Registration Service
Knowledge Source Service
Knowledge Reference Service
Knowledge Validation Service
Knowledge Version Service
Knowledge Access Service
Knowledge Reference Validation Service
Knowledge Audit Reference Service
```

Service rules:

```text
- Services must validate source reference.
- Services must validate scope.
- Services must validate status and validation_status.
- Services must emit events for mutating actions.
- AI access must check ai_usage_allowed, Permission and Policy.
- Deprecated or expired Knowledge must trigger review or warning.
- Services must not convert Knowledge into Document or Evidence directly.
```

---

# 12. Event Usage

Knowledge object emits or participates in:

```text
KnowledgeCreated
KnowledgeUpdated
KnowledgeSourceLinked
KnowledgeValidated
KnowledgeValidationFailed
KnowledgeVersionCreated
KnowledgeStatusChanged
KnowledgeDeprecated
KnowledgeAccessed
KnowledgeUsedByAI
KnowledgeReferenceValidated
```

Event rules:

```text
- Knowledge events must reference Knowledge ID.
- Validation events must preserve validation result and reviewer/source reference where allowed.
- AI usage events must identify AI agent source.
- Deprecated knowledge access must be traceable.
- Events must not expose protected source content unnecessarily.
```

---

# 13. API Usage

Potential MVP APIs:

```text
POST /knowledge
GET /knowledge/{id}
PATCH /knowledge/{id}
POST /knowledge/{id}/status
POST /knowledge/{id}/validate
POST /knowledge/{id}/versions
POST /knowledge/{id}/access/evaluate
POST /knowledge/reference/validate
```

API rules:

```text
- APIs must invoke Knowledge Services.
- APIs must validate source and scope.
- APIs must not turn Knowledge into Document or Evidence.
- APIs must not return protected source content without Permission and Policy.
- AI-facing APIs must respect Agent Contract and ai_usage_allowed.
- Mutating APIs must preserve audit context.
```

---

# 14. AI Agent Usage

AI Agents may use Knowledge only under governed Agent Contracts.

Allowed AI use:

```text
retrieve authorized Knowledge
summarize Knowledge with citation/reference
compare Knowledge versions
flag outdated Knowledge
suggest Knowledge validation review
ground drafting, classification or workflow guidance in Knowledge
identify missing source or scope
```

AI must not:

```text
treat Knowledge as final professional decision
use deprecated or expired Knowledge without warning/review
create validated Knowledge without human review where required
overwrite Knowledge source content
remove source attribution
convert AI output into Knowledge without registration and validation
use Knowledge outside authorized scope
```

AI Knowledge use requires:

```text
Agent Identity
Agent Contract
Authorized Knowledge
Permission Rule
Policy Rule
Knowledge Access Rule
Validation Status Rule
Audit Rule
Human Review Rule for high-risk professional use
```

---

# 15. Validation Rules

Knowledge object must pass:

```text
[ ] id is present and immutable.
[ ] knowledge_type is controlled.
[ ] source_reference_id is present.
[ ] scope_type is controlled.
[ ] status is controlled.
[ ] validation_status is controlled.
[ ] ai_usage_allowed is present.
[ ] Knowledge does not replace professional judgment.
[ ] Knowledge does not become AI Output.
[ ] Knowledge does not become Document or Evidence automatically.
[ ] Deprecated or expired Knowledge triggers warning/review.
[ ] Mutating services emit events.
[ ] AI use is contract-governed.
```

---

# 16. Codex Implementation Notes

Codex must:

```text
cite this object spec
cite knowledge domain spec
preserve Knowledge / AI Output boundary
preserve Knowledge / Document boundary
preserve Knowledge / Evidence boundary
preserve Knowledge / Policy boundary
implement only MVP fields unless task says otherwise
write tests for required source_reference_id
write tests for required scope_type
write tests for controlled knowledge_type
write tests for controlled status
write tests for controlled validation_status
write tests preventing Knowledge from becoming professional decision
write tests preventing AI Output from becoming Knowledge without validation
write tests preventing Document/Evidence conversion without services
write tests for event emission on mutation
```

Codex must not:

```text
invent full knowledge graph engine in MVP
treat uploaded files as Knowledge automatically
treat AI output as validated Knowledge
remove source attribution
allow AI to use Knowledge outside scope
allow deprecated Knowledge to be used silently
allow product UI to redefine Knowledge status
```

---

# 17. Acceptance Criteria

This Knowledge Object Specification is accepted only if:

```text
[ ] It defines Knowledge purpose.
[ ] It defines Knowledge Core meaning.
[ ] It identifies Knowledge as Foundation Object.
[ ] It defines fields.
[ ] It defines controlled values.
[ ] It defines object rules.
[ ] It defines relationships.
[ ] It defines lifecycle.
[ ] It defines service usage.
[ ] It defines event usage.
[ ] It defines API usage.
[ ] It defines AI Agent usage.
[ ] It defines validation rules.
[ ] It includes Codex implementation notes.
```

---

# 18. Revision Notes

| Version | Status | Notes |
|---------|--------|-------|
| 0.1.0 | Draft | Initial Knowledge object specification. Establishes Knowledge as governed Core reference, separates Knowledge from AI Output, Document, Evidence and professional judgment, and defines MVP fields, lifecycle, service/event/API/AI usage and Codex constraints. |

---

**End of Object Specification**
