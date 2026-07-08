# Object Specification — Jurisdiction

**Spec ID:** B02-OBJ-JURISDICTION  
**Spec Type:** Object  
**Object Name:** Jurisdiction  
**Owning Domain:** Jurisdiction  
**Domain Category:** Professional Domain  
**Source Chapter:** B02-CH-22 — Domain Specification; B02-CH-23 — Object Specification  
**Source Domain Spec:** core-specs/domains/jurisdiction.md  
**Related Object Specs:** core-specs/objects/jurisdiction-rule-reference.md; core-specs/objects/jurisdiction-status.md; core-specs/objects/jurisdiction-region.md; core-specs/objects/jurisdiction-office-reference.md; core-specs/objects/jurisdiction-service-scope.md; core-specs/objects/trademark.md; core-specs/objects/classification.md  
**Related Service Specs:** core-specs/services/jurisdiction-registration-service.md; core-specs/services/jurisdiction-rule-reference-service.md; core-specs/services/jurisdiction-status-service.md; core-specs/services/jurisdiction-reference-validation-service.md; core-specs/services/jurisdiction-service-scope-service.md  
**Related Event Specs:** core-specs/events/jurisdiction-created.md; core-specs/events/jurisdiction-updated.md; core-specs/events/jurisdiction-status-changed.md; core-specs/events/jurisdiction-rule-reference-linked.md; core-specs/events/jurisdiction-service-scope-updated.md; core-specs/events/jurisdiction-reference-validated.md  
**Related Contract Specs:** core-specs/contracts/jurisdiction/jurisdiction-contract.md; core-specs/contracts/jurisdiction/jurisdiction-rule-reference-contract.md; core-specs/contracts/jurisdiction/jurisdiction-office-reference-contract.md; core-specs/contracts/jurisdiction/jurisdiction-service-scope-contract.md; core-specs/contracts/jurisdiction/jurisdiction-reference-contract.md  
**Status:** Draft  
**Version:** 0.1.0  
**MVP Phase:** Phase 2 — Professional Core  
**MVP Wave:** Wave 2  
**MVP Depth:** Must Implement  
**Owner:** MarkOrbit Publications Editorial Board  

---

# 1. Purpose

The Jurisdiction object defines the Core-recognized place, legal/procedural territory, office scope or protection environment where trademark-related rights, procedures, filings, deadlines, rules, services or professional actions may apply.

It exists so that Trademark, Classification, Matter, Order, Document, Evidence, Agent, Service Provider, Routing, Knowledge, AI Agents, Services, APIs and product consumers can consistently reference where a trademark procedure or protection context applies.

Jurisdiction is required before:

```text
trademark filing planning
jurisdiction-specific procedure
classification applicability
official rule reference
deadline and status interpretation
agent and service provider routing
document and evidence requirements
fee and service scope reference
multi-jurisdiction strategy
AI jurisdiction guidance
client-facing country/region selection
```

---

# 2. Core Meaning

Jurisdiction means:

```text
a Core-recognized procedural or legal territory, office scope or protection environment in which trademark rights, filings, rules, requirements or services may apply.
```

Jurisdiction is not:

```text
country dropdown only
address country
language
currency
legal rule engine
fee engine
deadline engine
routing engine
agent
service provider
official database raw source
```

Jurisdiction answers:

```text
Where does the trademark procedure or protection apply?
Which office or regional system is involved?
Which rules or knowledge references may apply?
Which services, agents or providers may support it?
Which trademark, classification, document or evidence context references it?
Is the jurisdiction active, reserved, deprecated or review-required?
What audit trace is required?
```

---

# 3. Object Category

Jurisdiction is a Professional Object owned by the Jurisdiction Domain.

It is a foundational professional reference for trademark execution.

It is not merely a geographic label.

It provides the “where” context for professional rules, but does not itself implement the legal rule engine.

---

# 4. Architectural Position

Jurisdiction sits beside Trademark and Classification in professional architecture.

```text
Brand identifies commercial identity
        ↓
Trademark defines protection object
        ↓
Jurisdiction defines where protection/procedure applies
        ↓
Classification defines goods/services scope
        ↓
Matter executes professional work
        ↓
Agent / Service Provider / Routing support external delivery
```

Jurisdiction provides territorial/procedural context.

It does not select agent, calculate fees, decide deadlines or execute filings by itself.

---

# 5. Scope

The Jurisdiction object includes:

```text
jurisdiction id
jurisdiction code
jurisdiction name/reference
jurisdiction type
jurisdiction status
region reference
office reference
parent jurisdiction reference
filing system reference
service scope reference
rule reference
knowledge reference
language reference
currency reference
source reference
created time
updated time
audit metadata
```

MVP scope includes:

```text
jurisdiction id
jurisdiction code
jurisdiction name/reference
jurisdiction type
jurisdiction status
region reference
office reference
parent jurisdiction reference
basic service scope reference
rule/knowledge reference
source reference
created time
updated time
basic audit metadata
```

---

# 6. Field Specification

| Field | Type | Required | MVP | Notes |
|-------|------|----------|-----|-------|
| id | string | Yes | Yes | Stable immutable Jurisdiction ID. |
| jurisdiction_code | string | Yes | Yes | Controlled code, preferably ISO-like or internal canonical code. |
| name_reference | string | Yes | Yes | Human-readable jurisdiction name/reference. |
| jurisdiction_type | enum | Yes | Yes | National, Regional, International, Territory, Office, Custom, Unknown. |
| status | enum | Yes | Yes | Controlled Jurisdiction status. |
| region_reference | string | No | Yes | Region grouping reference. |
| office_reference_id | string | No | Yes | Trademark office or filing authority reference. |
| parent_jurisdiction_id | string | No | Yes | Parent jurisdiction where applicable. |
| filing_system_reference | string | No | Partial | Filing system or procedural system reference. |
| service_scope_references | array | No | Yes | Supported service scope references. |
| rule_reference_ids | array | No | Yes | Related rule/Knowledge/Policy references. |
| knowledge_reference_ids | array | No | Yes | Related Knowledge references. |
| language_references | array | No | Partial | Language references where useful. |
| currency_reference | string | No | Partial | Currency reference where useful; not fee engine. |
| source_reference | string | No | Yes | Source/import/system reference. |
| metadata | object | No | Yes | Non-sensitive metadata only. |
| created_at | datetime | Yes | Yes | Creation timestamp. |
| updated_at | datetime | Yes | Yes | Last update timestamp. |
| created_by | string | No | Yes | Identity or system actor reference. |
| updated_by | string | No | Yes | Identity or system actor reference. |

---

# 7. Controlled Values

## 7.1 jurisdiction_type

MVP controlled values:

```text
National
Regional
International
Territory
Office
Custom
Unknown
```

## 7.2 status

MVP controlled values:

```text
Draft
Active
ReviewRequired
Deprecated
Reserved
Archived
```

## 7.3 service_scope_type

Suggested controlled values:

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
```

---

# 8. Object Rules

## 8.1 Jurisdiction Requires Code and Name

Every Jurisdiction must have:

```text
jurisdiction_code
name_reference
jurisdiction_type
status
```

A Jurisdiction without code or name reference is not Core-valid.

## 8.2 Jurisdiction Is Not a Country Dropdown

Jurisdiction may represent:

```text
country
regional system
international system
territory
trademark office scope
custom procedural scope
```

Product UI must not reduce Jurisdiction to country dropdown only.

## 8.3 Jurisdiction Does Not Own Legal Rule Engine

Jurisdiction may reference rules, policies and knowledge.

It does not calculate deadlines, fees, registrability, procedure or official status by itself.

## 8.4 Jurisdiction Does Not Own Routing

Jurisdiction may support agent/provider eligibility.

Routing selects agent or service provider.

## 8.5 Jurisdiction Must Preserve Source and Version Where Rule-Sensitive

Rule-sensitive jurisdiction references should preserve source and version where applicable.

Deprecated or review-required jurisdictions should trigger review before new filing or routing use.

## 8.6 Jurisdiction Must Be Auditable

Jurisdiction-sensitive changes must preserve audit trace.

Audit-sensitive actions include:

```text
jurisdiction creation
jurisdiction code update
jurisdiction status change
office reference update
parent jurisdiction update
service scope update
rule/knowledge reference update
AI jurisdiction analysis
archival
```

---

# 9. Relationships

| Related Object | Relationship | Rule |
|----------------|--------------|------|
| Trademark | Trademark must reference Jurisdiction | Trademark remains protection object. |
| Classification | Classification may be jurisdiction-specific | Classification owns goods/services scope. |
| Matter | Matter may be jurisdiction-scoped | Matter remains execution container. |
| Order | Order may request services by Jurisdiction | Order remains commercial service request. |
| Document | Document requirements may be jurisdiction-specific | Document remains artifact. |
| Evidence | Evidence requirements may be jurisdiction-specific | Evidence remains proof layer. |
| Agent | Agent may support Jurisdiction | Agent remains collaborator. |
| Service Provider | Provider may support Jurisdiction | Provider remains capability profile. |
| Routing | Routing may use Jurisdiction context | Routing makes selection decisions. |
| Knowledge | Knowledge may be jurisdiction-scoped | Knowledge remains governed reference. |
| Policy | Policy may constrain jurisdiction use | Policy remains contextual rule. |
| AI Output | AI may analyze Jurisdiction context | AI Output is not professional truth. |
| Audit Record | Audit may reference Jurisdiction | Audit remains accountability system. |

---

# 10. Lifecycle

Jurisdiction lifecycle states:

```text
Draft
Active
ReviewRequired
Deprecated
Reserved
Archived
```

Lifecycle rules:

```text
Draft → Active
Draft → ReviewRequired
ReviewRequired → Active
Active → ReviewRequired
Active → Deprecated
Deprecated → Archived
Active → Reserved
Reserved → Active
Draft → Archived
```

Prohibited lifecycle behavior:

```text
Archived → Active without restoration service and review
Deprecated → Active without revalidation or new version/reference
Reserved → Deprecated without review/source reference
```

---

# 11. Service Usage

Jurisdiction object is created and managed through:

```text
Jurisdiction Registration Service
Jurisdiction Update Service
Jurisdiction Status Service
Jurisdiction Rule Reference Service
Jurisdiction Service Scope Service
Jurisdiction Office Reference Service
Jurisdiction Reference Validation Service
Jurisdiction Audit Reference Service
```

Service rules:

```text
- Services must validate jurisdiction_code.
- Services must validate jurisdiction_type.
- Services must validate status transitions.
- Services must emit events for mutating actions.
- Services must not calculate official deadline, fee or registrability by itself.
- Services must not select Agent or Service Provider directly.
```

---

# 12. Event Usage

Jurisdiction object emits or participates in:

```text
JurisdictionCreated
JurisdictionUpdated
JurisdictionStatusChanged
JurisdictionOfficeReferenceLinked
JurisdictionParentUpdated
JurisdictionRuleReferenceLinked
JurisdictionServiceScopeUpdated
JurisdictionKnowledgeLinked
JurisdictionArchived
JurisdictionReferenceValidated
```

Event rules:

```text
- Jurisdiction events must reference Jurisdiction ID.
- Status events must preserve previous and new status.
- Rule reference events must preserve source reference where allowed.
- Service scope events must not imply routing decision.
- Events must not expose protected provider or rule content unnecessarily.
```

---

# 13. API Usage

Potential Phase 2 APIs:

```text
POST /jurisdictions
GET /jurisdictions/{id}
PATCH /jurisdictions/{id}
POST /jurisdictions/{id}/status
POST /jurisdictions/{id}/rule-references
POST /jurisdictions/{id}/service-scopes
POST /jurisdictions/reference/validate
```

API rules:

```text
- APIs must invoke Jurisdiction Services.
- APIs must not implement legal rule engine.
- APIs must not calculate final fee/deadline/registrability.
- APIs must not select Agent or Service Provider directly.
- APIs must preserve Permission, Policy and audit context.
- AI-facing APIs must respect Agent Contract and Authorized Knowledge rules.
```

---

# 14. AI Agent Usage

AI Agents may use Jurisdiction only under governed Agent Contracts.

Allowed AI use:

```text
summarize jurisdiction context
identify missing jurisdiction reference
suggest jurisdiction selection questions
flag jurisdiction/trademark mismatch
flag unsupported or deprecated jurisdiction
summarize jurisdiction-related Knowledge if authorized
suggest agent/provider routing inputs for review
```

AI must not:

```text
make final legal rule determination without governed Knowledge and review
calculate official deadlines or fees as final truth
select Agent or Service Provider directly
override deprecated or reserved status
treat jurisdiction code as complete legal analysis
create jurisdiction rules without authorized service
```

AI Jurisdiction use requires:

```text
Agent Identity
Agent Contract
Authorized Knowledge
Permission Rule
Policy Rule
Jurisdiction Access Rule
Trademark Access Rule where applicable
Routing Rule where applicable
Audit Rule
Human Review Rule for professional conclusions
```

---

# 15. Validation Rules

Jurisdiction object must pass:

```text
[ ] id is present and immutable.
[ ] jurisdiction_code is present.
[ ] name_reference is present.
[ ] jurisdiction_type is controlled.
[ ] status is controlled.
[ ] Jurisdiction is not reduced to country dropdown.
[ ] Jurisdiction does not own legal rule engine.
[ ] Jurisdiction does not own fee/deadline engine.
[ ] Jurisdiction does not own Routing decision.
[ ] Rule and Knowledge references remain references.
[ ] Mutating services emit events.
[ ] Status transitions are governed.
[ ] AI use is contract-governed.
```

---

# 16. Codex Implementation Notes

Codex must:

```text
cite this object spec
cite jurisdiction domain spec
preserve Jurisdiction / Trademark boundary
preserve Jurisdiction / Classification boundary
preserve Jurisdiction / Knowledge / Policy boundaries
preserve Jurisdiction / Routing boundary
implement only MVP fields unless task says otherwise
write tests for required jurisdiction_code
write tests for required name_reference
write tests for controlled jurisdiction_type
write tests for controlled status
write tests preventing Jurisdiction from becoming country dropdown only
write tests preventing Jurisdiction from calculating fees/deadlines
write tests preventing Jurisdiction from selecting Agent/Service Provider
write tests for event emission on mutation
```

Codex must not:

```text
invent legal rule engine inside Jurisdiction object
invent deadline or fee engine inside Jurisdiction object
treat country code as full jurisdiction model
select routing candidate from Jurisdiction service
treat official source reference as validated Knowledge automatically
allow AI to make final jurisdiction legal conclusion
allow product UI to redefine Jurisdiction status
```

---

# 17. Acceptance Criteria

This Jurisdiction Object Specification is accepted only if:

```text
[ ] It defines Jurisdiction purpose.
[ ] It defines Jurisdiction Core meaning.
[ ] It identifies Jurisdiction as Professional Object.
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
| 0.1.0 | Draft | Initial Jurisdiction object specification. Establishes Jurisdiction as professional territorial/procedural context, separates it from country dropdowns, rule engines, fee/deadline engines and Routing, and defines MVP fields, lifecycle, service/event/API/AI usage and Codex constraints. |

---

**End of Object Specification**
