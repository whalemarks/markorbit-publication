# Agent Specification — Knowledge Agent

**Spec ID:** B02-AGENT-KNOWLEDGE  
**Spec Type:** Specialized Agent Specification  
**Agent Spec Name:** Knowledge Agent  
**Agent Spec File:** core-specs/agents/knowledge-agent.md  
**Registry Key:** knowledge-retrieval-agent  
**Related Agent Governance:** core-specs/agents/ai-agent-governance.md; core-specs/agents/agent-registry.md  
**Related Core Domains:** Knowledge; Agent; Permission; Policy; Event; Document; Evidence; Task  
**Related Object Specs:** core-specs/objects/knowledge.md; core-specs/objects/agent.md; core-specs/objects/permission.md; core-specs/objects/policy.md; core-specs/objects/event.md; core-specs/objects/document.md; core-specs/objects/evidence.md; core-specs/objects/task.md  
**Related Service Specs:** core-specs/services/knowledge-service.md; core-specs/services/agent-service.md; core-specs/services/permission-service.md; core-specs/services/policy-service.md; core-specs/services/event-service.md; core-specs/services/document-service.md; core-specs/services/evidence-service.md; core-specs/services/task-service.md  
**Related API Specs:** core-specs/api/knowledge-api.md; core-specs/api/agent-api.md; core-specs/api/permission-api.md; core-specs/api/policy-api.md; core-specs/api/event-api.md; core-specs/api/document-api.md; core-specs/api/evidence-api.md; core-specs/api/task-api.md  
**Related Event Specs:** core-specs/events/permission-evaluated.md; core-specs/events/policy-evaluated.md; core-specs/events/knowledge-record-created.md; core-specs/events/knowledge-record-updated.md  
**Status:** Draft  
**Version:** 0.1.0  
**MVP Phase:** Phase 1 — Foundation Core  
**MVP Depth:** Must Implement  
**Owner:** MarkOrbit Publications Editorial Board  

---

# 1. Purpose

Knowledge Agent defines the governed AI Agent pattern for retrieving, summarizing, validating and explaining Knowledge records in MarkOrbit Core.

It exists to help users and downstream services access relevant knowledge without allowing AI to become professional truth, bypass Knowledge Service, expose restricted records, fabricate source material, make legal conclusions or silently use unapproved document/evidence content.

Knowledge Agent supports:

```text
knowledge retrieval assistance
safe knowledge summarization
knowledge reference validation
knowledge gap identification
contextual knowledge explanation
knowledge-to-task preparation
policy-filtered knowledge use
audit-friendly source trace
```

Knowledge Agent does not decide legal outcomes, approve filings, certify evidence sufficiency, create professional conclusions or replace human review.

---

# 2. Agent Meaning

Knowledge Agent means:

```text
a governed AI Agent that assists with policy-filtered Knowledge retrieval and safe Knowledge explanation.
```

Knowledge Agent does not mean:

```text
professional truth engine
legal opinion engine
unrestricted knowledge reader
document parser with unrestricted access
evidence sufficiency judge
filing decision system
policy bypasser
hidden search index
```

Knowledge Agent may help answer:

```text
What Knowledge records are relevant?
What safe summaries can be shown?
What sources support this explanation?
What gaps remain?
What should be reviewed by a human?
```

Knowledge Agent must not claim:

```text
This is legally final.
This evidence is sufficient.
This filing should be submitted.
This restricted record may be exposed.
This unverified extraction is confirmed truth.
```

---

# 3. Registry Position

Registry entry:

```text
knowledge-retrieval-agent
```

Required registry constraints:

```text
agent_type: KnowledgeAgent
agent_role: KnowledgeRetrievalAssistant
default_data_access_scope: SafeSummaryOnly
default_execution_mode: ReadOnly
```

Allowed capabilities:

```text
Read
Summarize
RequestKnowledge
ValidateReference
ExplainTrace
```

Restricted capabilities:

```text
AccessRestrictedContent
AccessRawDocument
AccessEvidence
AccessPrivateContact
AccessFinancialData
```

Registry rule:

```text
Knowledge Agent may be considered for Knowledge retrieval and explanation.
Permission and Policy decide whether it may access specific Knowledge in context.
```

---

# 4. Agent Boundary

Knowledge Agent is responsible for:

```text
knowledge query preparation
knowledge reference validation request
safe knowledge retrieval request
safe summary generation
source-scope explanation
missing-context detection
policy omission disclosure
knowledge-to-task preparation where explicitly allowed
knowledge trace explanation
```

Knowledge Agent is not responsible for:

```text
Knowledge object lifecycle ownership
Knowledge record creation as truth
raw document ingestion
evidence sufficiency approval
legal conclusion
filing submission
payment decision
provider selection
task execution
communication sending
permission grant
policy evaluation
```

---

# 5. Governance Lock

Knowledge Agent must obey:

```text
Knowledge Agent may retrieve and summarize only Knowledge that Permission and Policy allow.
Knowledge Agent output is source-grounded assistance, not professional truth.
Knowledge Agent must disclose source scope, missing context, policy omissions and human-review requirements.
Knowledge Agent must not fabricate Knowledge records, citations, legal authority or evidence sufficiency.
```

This lock applies to all Knowledge Agent implementations.

---

# 6. Agent Identity Requirements

Every Knowledge Agent operation must include:

```yaml
agent_reference_id: string
agent_registry_key: knowledge-retrieval-agent
agent_contract_reference_id: string | null
actor_reference_id: string | null
organization_reference_id: string | null
target_context:
  target_object_type: string | null
  target_object_reference_id: string | null
correlation_id: string | null
```

Rules:

```text
- Agent identity must be validated through Agent Service.
- Agent status must be Active or otherwise explicitly allowed.
- Suspended, revoked, archived or unknown agents must not perform Knowledge operations.
- Agent must not borrow human User identity.
- Agent Contract is required for protected access.
```

---

# 7. Capability Rules

Allowed operations:

```text
prepareKnowledgeQuery
requestKnowledgeAccess
summarizeKnowledgeRecords
validateKnowledgeReference
explainKnowledgeTrace
identifyKnowledgeGaps
prepareKnowledgeTaskDraft
```

Disallowed operations:

```text
createKnowledgeAsTruth
updateKnowledgeWithoutService
deleteKnowledge
accessAllKnowledge
accessRawRestrictedDocumentsByDefault
approveEvidenceSufficiency
issueLegalConclusion
completeTask
sendCommunication
```

Capability rule:

```text
Knowledge Agent may prepare and summarize; Knowledge Service owns Knowledge access and Knowledge lifecycle.
```

---

# 8. Data Access Rules

Default data access:

```text
SafeSummaryOnly
```

Allowed data access scopes:

```text
MetadataOnly
SafeSummaryOnly
PolicyFilteredContent
```

Restricted data access scopes:

```text
RestrictedContentWithHumanApproval
AccessRawDocument
AccessEvidence
AccessPricing
AccessPrivateContact
AccessFinancialData
```

Rules:

```text
- SafeSummaryOnly is the default.
- Policy may downgrade access to MetadataOnly or NoAccess.
- Raw document access requires explicit Document Policy.
- Evidence access requires explicit Evidence Policy.
- RestrictedContentWithHumanApproval requires human review reference.
- Prompt/context construction must use evaluated access scope.
```

Disallowed default fields:

```text
privileged attorney strategy
unredacted customer documents
financial records
private contacts
API credentials
filing credentials
provider contracts
commission terms
raw evidence packages
```

---

# 9. Permission Rules

Required permissions may include:

```text
agent:knowledge:request-access
knowledge:read
knowledge:search
knowledge:validate
knowledge:summarize
knowledge:trace:explain
document:read
evidence:read
task:create
```

Rules:

```text
- Agent-level permission is required.
- Knowledge-domain permission is required.
- Related Document/Evidence permission is required where those records are referenced.
- Permission must be evaluated against actor, agent, organization, target context and intended use.
- PermissionDenied stops the operation.
```

---

# 10. Policy Rules

Required policies may include:

```text
AIAgentKnowledgeAccessPolicy
KnowledgeVisibilityPolicy
KnowledgeReferencePolicy
KnowledgeSummaryPolicy
KnowledgeTracePolicy
RestrictedKnowledgeDataPolicy
DocumentVisibilityPolicy
EvidenceVisibilityPolicy
CrossOrganizationKnowledgePolicy
AIAgentHumanReviewPolicy
```

Rules:

```text
- Policy controls whether full content, filtered content, safe summary or metadata may be used.
- Policy may require human review.
- Policy may restrict cross-organization or cross-matter retrieval.
- Policy may restrict source disclosure.
- Policy may require redaction.
- PolicyRestricted stops or downgrades the operation.
```

---

# 11. Request Patterns

## 11.1 Knowledge Access Request

```yaml
operation: requestKnowledgeAccess
agent_reference_id: string
agent_registry_key: knowledge-retrieval-agent
actor_reference_id: string | null
organization_reference_id: string | null
retrieval_purpose: string
knowledge_scope: string
target_context:
  target_object_type: string | null
  target_object_reference_id: string | null
query_context:
  query_text: string
  jurisdiction_reference_id: string | null
  domain_reference_id: string | null
  object_reference_ids: list[string]
data_access_requested: string
correlation_id: string | null
```

## 11.2 Knowledge Summary Request

```yaml
operation: summarizeKnowledgeRecords
agent_reference_id: string
knowledge_record_reference_ids: list[string]
summary_purpose: string
summary_depth: string
output_mode: string
human_review_reference_id: string | null
correlation_id: string | null
```

## 11.3 Knowledge Reference Validation Request

```yaml
operation: validateKnowledgeReference
agent_reference_id: string
knowledge_record_reference_id: string
intended_use: string
target_context:
  target_object_type: string | null
  target_object_reference_id: string | null
correlation_id: string | null
```

## 11.4 Knowledge Gap Request

```yaml
operation: identifyKnowledgeGaps
agent_reference_id: string
target_context:
  target_object_type: string
  target_object_reference_id: string
known_knowledge_record_reference_ids: list[string]
gap_purpose: string
correlation_id: string | null
```

---

# 12. Response Patterns

## 12.1 Knowledge Access Response

```yaml
agent_reference_id: string
knowledge_access_reference_id: string | null
access_decision: string
safe_knowledge_summaries:
  - knowledge_record_reference_id: string
    knowledge_type: string
    safe_title: string | null
    safe_summary: string | null
    source_scope: string
    confidence_level: string | null
restricted_fields_omitted: boolean
policy_decision_reference_id: string | null
permission_decision_reference_id: string | null
human_review_required: boolean
correlation_id: string | null
```

## 12.2 Knowledge Summary Response

```yaml
agent_reference_id: string
summary_reference_id: string | null
summary_type: string
safe_summary: string
source_knowledge_record_reference_ids: list[string]
missing_context: list[string]
policy_omissions: list[string]
confidence_level: string
human_review_required: boolean
restricted_fields_omitted: boolean
correlation_id: string | null
```

## 12.3 Knowledge Validation Response

```yaml
agent_reference_id: string
knowledge_record_reference_id: string
valid: boolean
validation_status: string
safe_reason: string | null
policy_decision_reference_id: string | null
restricted_fields_omitted: boolean
correlation_id: string | null
```

Response rules:

```text
- Responses must mark AI-generated output.
- Responses must preserve source references.
- Responses must disclose missing context and policy omissions.
- Responses must not claim legal finality.
- Responses must not expose restricted fields by default.
```

---

# 13. Controlled Values

## 13.1 retrieval_purpose

```text
Read
Summarize
Draft
Recommend
Validate
Explain
AIAssistedWorkflow
AIAssistedTask
AuditReview
Unknown
```

## 13.2 knowledge_scope

```text
CoreSpecification
DomainKnowledge
JurisdictionKnowledge
ClassificationKnowledge
TrademarkKnowledge
ProcedureKnowledge
EvidenceKnowledge
DocumentKnowledge
CustomerContext
MatterContext
OrderContext
Unknown
```

## 13.3 summary_purpose

```text
InternalReview
ClientSupport
TaskPreparation
WorkflowPreparation
CommunicationDrafting
AuditReview
ProfessionalReference
AIAssistedExplanation
Unknown
```

## 13.4 summary_depth

```text
Brief
Standard
DetailedSafe
RestrictedInternal
Unknown
```

## 13.5 output_mode

```text
SafeSummary
Draft
Suggestion
ValidationResult
ExtractionResult
TraceExplanation
Unknown
```

## 13.6 access_decision

```text
Allowed
Denied
PolicyRestricted
PermissionDenied
HumanReviewRequired
ContractRequired
Unknown
```

## 13.7 validation_status

```text
Valid
Invalid
NotFound
PolicyRestricted
PermissionDenied
ReviewRequired
Archived
ContextMismatch
Unknown
```

## 13.8 confidence_level

```text
Low
Medium
High
Unknown
```

---

# 14. Human Review Rules

Human review is required when Knowledge Agent output may be used for:

```text
legal conclusion
official filing
customer-facing legal explanation
evidence sufficiency assessment
document finalization
external communication
professional recommendation
cross-organization disclosure
restricted content use
```

Human review is not required for:

```text
safe internal metadata lookup
safe summary of public/core specification content
reference validation where no restricted content is exposed
gap checklist preparation
```

Rules:

```text
- Human review requirement must be included in output.
- Human review must be explicit where required.
- Human review reference must be passed to downstream services where output is used.
```

---

# 15. Event and Audit Rules

Knowledge Agent operations must be traceable.

Trace must include:

```yaml
agent_registry_key: knowledge-retrieval-agent
agent_reference_id: string
operation: string
retrieval_purpose: string | null
knowledge_scope: string | null
data_access_scope: string
target_object_type: string | null
target_object_reference_id: string | null
knowledge_record_reference_ids: list[string]
permission_decision_reference_id: string | null
policy_decision_reference_id: string | null
human_review_reference_id: string | null
correlation_id: string | null
```

Rules:

```text
- Knowledge Agent must not emit domain events directly.
- Event Service owns event recording.
- PermissionEvaluated and PolicyEvaluated references should be preserved where available.
- Knowledge sources used in output must be referenceable.
```

---

# 16. Relationship to Knowledge Service

Knowledge Agent must use Knowledge Service for:

```text
searchKnowledge
getKnowledge
validateKnowledgeReference
summarizeKnowledge
requestKnowledgeAccess
```

Rules:

```text
- Knowledge Agent must not query the knowledge store directly.
- Knowledge Service applies domain rules.
- Permission and Policy are evaluated before content access.
- Knowledge Agent may transform safe results into drafts or summaries.
```

---

# 17. Relationship to Document and Evidence Services

Knowledge Agent may reference Document and Evidence only through governed service access.

Rules:

```text
- Document Service owns Document access.
- Evidence Service owns Evidence access.
- Knowledge Agent may not treat Document extraction as verified truth.
- Knowledge Agent may not treat Evidence as sufficient without professional review.
- Raw Document or Evidence content requires explicit Permission and Policy.
```

---

# 18. Relationship to Task and Communication Services

Knowledge Agent may prepare downstream drafts.

Allowed:

```text
prepare knowledge-based task checklist
prepare knowledge-based communication draft context
prepare missing-information checklist
prepare review questions
```

Rules:

```text
- Task creation must route through Task Service.
- Communication creation must route through Communication Service.
- Knowledge Agent output must not be treated as sent communication or completed task.
```

---

# 19. Error and Rejection Rules

Controlled rejection reasons:

```text
PermissionDenied
PolicyRestricted
AgentSuspended
AgentRevoked
AgentContractRequired
CapabilityNotAllowed
HumanReviewRequired
RestrictedDataRequested
KnowledgeAccessRestricted
KnowledgeReferenceInvalid
TargetContextInvalid
CrossOrganizationRestricted
DownstreamServiceRequired
```

Rules:

```text
- Rejections must be safe to display.
- Rejections must not reveal hidden Knowledge.
- Rejections must not expose policy internals.
- Rejections may recommend the next governed step.
```

---

# 20. Codex Implementation Notes

Codex must:

```text
cite AI Agent Governance
cite Agent Registry
cite this Knowledge Agent spec
cite Knowledge Service Specification
cite Knowledge Object Specification
cite Permission and Policy specs
validate agent_registry_key = knowledge-retrieval-agent
validate agent status
validate capability eligibility
invoke Permission Service before protected access
invoke Policy Service before content access
use SafeSummaryOnly by default
preserve knowledge_record_reference_ids in output
mark AI-generated summaries
disclose missing context and policy omissions
route Document/Evidence access through owning services
route Task/Communication preparation through owning services
write tests for PermissionDenied
write tests for PolicyRestricted
write tests for AgentContractRequired
write tests for restricted data omission
write tests for invalid Knowledge reference
write tests that Knowledge Agent cannot fabricate sources
write tests that Knowledge Agent cannot issue final legal conclusion
write tests that raw Document/Evidence access requires explicit policy
```

Codex must not:

```text
query Knowledge database directly
bypass Knowledge Service
bypass Permission or Policy
pass unrestricted Knowledge into prompts
fabricate citations or Knowledge references
treat AI summary as professional truth
approve evidence sufficiency
create tasks or communications directly
emit domain events directly
```

---

# 21. Acceptance Criteria

This Knowledge Agent Specification is accepted only if:

```text
[ ] It defines Knowledge Agent purpose.
[ ] It defines Agent meaning.
[ ] It defines registry position.
[ ] It defines Agent boundary.
[ ] It defines governance lock.
[ ] It defines identity requirements.
[ ] It defines capability rules.
[ ] It defines data access rules.
[ ] It defines Permission rules.
[ ] It defines Policy rules.
[ ] It defines request patterns.
[ ] It defines response patterns.
[ ] It defines controlled values.
[ ] It defines human review rules.
[ ] It defines event and audit rules.
[ ] It defines relationship to Knowledge Service.
[ ] It defines relationship to Document and Evidence Services.
[ ] It defines relationship to Task and Communication Services.
[ ] It defines error and rejection rules.
[ ] It defines Codex implementation notes.
```

---

# 22. Revision Notes

| Version | Status | Notes |
|---------|--------|-------|
| 0.1.0 | Draft | Initial Knowledge Agent specification. Defines governed Knowledge retrieval, summarization, validation, gap detection and source-trace rules under AI Agent Governance and Agent Registry. |

---

**End of Agent Specification**
