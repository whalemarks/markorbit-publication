# Common Contract — Human Review

**Spec ID:** B02-CONTRACT-COMMON-HUMAN-REVIEW  
**Spec Type:** Common Contract Specification  
**Contract Name:** Human Review Contract  
**Contract File:** core-specs/contracts/common/human-review.md  
**Contract Category:** Common  
**Related Owning Spec:** core-specs/contracts/README.md  
**Related Domain:** Cross-Domain Common Contract  
**Related Object Specs:** core-specs/objects/user.md; core-specs/objects/permission.md; core-specs/objects/policy.md; core-specs/objects/task.md; core-specs/objects/workflow-contract.md; core-specs/objects/communication.md; core-specs/objects/routing.md; core-specs/objects/document.md; core-specs/objects/evidence.md; core-specs/objects/event.md; core-specs/objects/agent.md  
**Related Service Specs:** core-specs/services/permission-service.md; core-specs/services/policy-service.md; core-specs/services/task-service.md; core-specs/services/workflow-contract-service.md; core-specs/services/communication-service.md; core-specs/services/routing-service.md; core-specs/services/document-service.md; core-specs/services/evidence-service.md; core-specs/services/event-service.md; core-specs/services/agent-service.md  
**Related API Specs:** core-specs/api/permission-api.md; core-specs/api/policy-api.md; core-specs/api/task-api.md; core-specs/api/workflow-contract-api.md; core-specs/api/communication-api.md; core-specs/api/routing-api.md; core-specs/api/document-api.md; core-specs/api/evidence-api.md; core-specs/api/event-api.md; core-specs/api/agent-api.md  
**Related Event Specs:** core-specs/events/permission-evaluated.md; core-specs/events/policy-evaluated.md; core-specs/events/task-created.md; core-specs/events/workflow-contract-applied.md; core-specs/events/communication-created.md; core-specs/events/routing-selected.md  
**Related Agent Specs:** core-specs/agents/ai-agent-governance.md; core-specs/agents/agent-registry.md; core-specs/agents/task-agent.md; core-specs/agents/communication-agent.md; core-specs/agents/workflow-agent.md; core-specs/agents/routing-agent.md; core-specs/agents/audit-agent.md  
**Status:** Draft  
**Version:** 0.1.0  
**Contract Version:** v0.1.0  
**MVP Phase:** Cross-Phase Core Contract System  
**MVP Depth:** Must Implement  
**Owner:** MarkOrbit Publications Editorial Board  

---

# 1. Purpose

Human Review Contract defines the canonical human-review context shape used across MarkOrbit Core.

It standardizes how APIs, services, workflows, agents and downstream actions represent the requirement, request, completion, decision and trace of human review before protected actions are used for professional, external, state-changing or legally sensitive purposes.

This contract governs:

```text
human review requirement
human review request
reviewer identity
review scope
review decision
review result
review notes safety
review timing
review dependency
AI output review
external communication review
workflow/task/routing review
professional conclusion review
human-review trace
Codex implementation rules
```

Human Review Contract does not replace professional judgment, create legal conclusions, approve filings by itself, send communications, apply workflows, select providers or mutate domain state without the owning service.

---

# 2. Contract Meaning

This contract means:

```text
a common Core agreement for expressing when human review is required, how it is recorded, and how downstream services may rely on it.
```

This contract does not mean:

```text
professional judgment itself
legal opinion
filing approval by itself
communication sending
workflow execution
task completion
routing selection
permission grant
policy approval
managerial approval outside contract
```

Core rule:

```text
Human review records accountable professional review.
Human review does not execute downstream action by itself.
Owning services decide whether review satisfies action requirements.
Events preserve review trace.
```

---

# 3. Contract Boundary

This contract is responsible for:

```text
human review requirement shape
review request shape
review decision shape
reviewer reference
review scope
review status
review notes safety
review dependency on AI output
review dependency on Permission/Policy
human review validation
human review errors
downstream reliance rules
```

This contract is not responsible for:

```text
deciding professional outcome
executing downstream action
submitting official filings
sending external communications
applying workflows
creating tasks directly
selecting providers
evaluating permission
evaluating policy
creating events directly
```

---

# 4. Related Owning Spec

Owning spec:

```text
core-specs/contracts/README.md
```

Related common contracts:

```text
core-specs/contracts/common/references.md
core-specs/contracts/common/errors.md
core-specs/contracts/common/audit-context.md
core-specs/contracts/common/ai-context.md
core-specs/contracts/common/permission-context.md
core-specs/contracts/common/policy-context.md
```

Owning rule:

```text
Human Review Contract defines review trace and decision shape. It must not be treated as downstream action execution.
```

---

# 5. Related Core Objects

Primary related objects:

```text
User
Permission
Policy
Task
WorkflowContract
Communication
Routing
Document
Evidence
Agent
Event
```

Rules:

```text
- User object identifies reviewer.
- Agent object identifies AI/agent output requiring review.
- Event object preserves trace.
- Owning services decide whether human review satisfies downstream requirements.
```

---

# 6. Required References

Human review context shape:

```yaml
human_review_context:
  human_review_required: boolean
  human_review_reference_id: string | null
  review_request_reference_id: string | null
  reviewer_user_reference_id: string | null
  review_scope: string | null
  review_decision: string | null
  review_status: string | null
  review_target:
    target_object_type: string | null
    target_object_reference_id: string | null
  source_context:
    ai_assisted: boolean | null
    agent_reference_id: string | null
    agent_registry_key: string | null
    source_reference_ids: list[string]
  governance:
    permission_decision_reference_id: string | null
    policy_decision_reference_id: string | null
  trace:
    correlation_id: string | null
    event_reference_ids: list[string]
```

Rules:

```text
- human_review_required must be explicit where protected downstream use is possible.
- reviewer_user_reference_id is required when review is completed.
- review_scope is required when review is requested or completed.
- review_decision is required when review_status is Completed.
- target_object_type and target_object_reference_id must follow Reference Contract.
```

---

# 7. Contract Shape

Canonical human review shape:

```yaml
human_review:
  human_review_reference_id: string
  review_request_reference_id: string | null
  review_status: string
  review_scope: string
  review_decision: string | null
  reviewer:
    reviewer_user_reference_id: string | null
    reviewer_role: string | null
    reviewer_organization_reference_id: string | null
  target:
    target_object_type: string
    target_object_reference_id: string
  source:
    source_type: string
    source_reference_ids: list[string]
    ai_assisted: boolean
    agent_reference_id: string | null
    agent_registry_key: string | null
  governance:
    permission_decision_reference_id: string | null
    policy_decision_reference_id: string | null
  notes:
    review_notes_safe: string | null
    restricted_notes_omitted: boolean
  timestamps:
    requested_at: datetime | null
    reviewed_at: datetime | null
    expires_at: datetime | null
  trace:
    correlation_id: string | null
    event_reference_ids: list[string]
```

Minimal downstream reliance shape:

```yaml
human_review_context:
  human_review_required: boolean
  human_review_reference_id: string | null
  review_decision: string | null
  review_scope: string | null
```

Rules:

```text
- Full shape is required for review record creation.
- Minimal shape may be used only to reference completed/required review.
- Review notes must be safe by default.
- Restricted review notes must be omitted unless policy allows them.
```

---

# 8. Field Rules

| Field | Type | Required | Nullable | Rule |
|------|------|----------|----------|------|
| human_review_required | boolean | Yes where applicable | No | Must be explicit for protected downstream use. |
| human_review_reference_id | string | Contextual | Yes | Required when completed review is relied on. |
| review_request_reference_id | string | No | Yes | Used when review request is tracked separately. |
| review_status | string | Yes for review record | No | Must use controlled value. |
| review_scope | string | Yes for review record | No | Must use controlled value or owning contract value. |
| review_decision | string | Required if Completed | Yes | Must use controlled value. |
| reviewer_user_reference_id | string | Required if Completed | Yes | Must reference User. |
| reviewer_role | string | Contextual | Yes | Must be safe and controlled where provided. |
| target_object_type | string | Yes | No | Must follow Reference Contract. |
| target_object_reference_id | string | Yes | No | Must match target_object_type. |
| source_type | string | Yes | No | Must use controlled value. |
| source_reference_ids | list[string] | Contextual | No | Must preserve reviewed source references. |
| ai_assisted | boolean | Contextual | No | Must be true if AI output is reviewed. |
| agent_reference_id | string | Contextual | Yes | Required if AI/Agent output was reviewed. |
| permission_decision_reference_id | string | Contextual | Yes | Required where review depends on permission decision and exposure allowed. |
| policy_decision_reference_id | string | Contextual | Yes | Required where review depends on policy decision and exposure allowed. |
| review_notes_safe | string | No | Yes | Must not expose restricted data. |
| restricted_notes_omitted | boolean | Yes | No | True when restricted notes are omitted. |
| reviewed_at | datetime | Required if Completed | Yes | Must be present when review_decision is final. |
| expires_at | datetime | No | Yes | Used when review has validity period. |

---

# 9. Controlled Values

## 9.1 review_status

```text
Requested
InReview
Completed
Rejected
Escalated
Expired
Cancelled
NotRequired
Unknown
```

## 9.2 review_decision

```text
Approved
Rejected
Revised
Escalated
NeedsMoreInformation
NotApplicable
Unknown
```

## 9.3 review_scope

```text
AIOutputReview
ProfessionalReview
ExternalCommunicationReview
LegalNoticeReview
CustomerInstructionReview
WorkflowApplicationReview
TaskCompletionReview
RoutingSelectionReview
ProviderCommunicationReview
DocumentReview
EvidenceReview
PaymentImpactReview
CrossOrganizationDisclosureReview
ComplianceReview
Unknown
```

## 9.4 reviewer_role

```text
ProfessionalReviewer
MatterOwner
OrderOwner
Supervisor
ComplianceReviewer
LegalReviewer
OperationsReviewer
Administrator
Unknown
```

## 9.5 source_type

```text
AIAssistedDraft
AIAssistedSummary
AIAssistedRecommendation
UserSubmittedContent
Document
Evidence
Communication
Task
WorkflowPreview
RoutingRecommendation
SystemGenerated
ProfessionalInput
Unknown
```

---

# 10. Validation Rules

Validation checklist:

```text
[ ] human_review_required is explicit where applicable.
[ ] review_status is controlled.
[ ] review_scope is present for review record.
[ ] review_decision is controlled where provided.
[ ] reviewer_user_reference_id is present when review is Completed.
[ ] reviewed_at is present when review is Completed.
[ ] target object reference follows Reference Contract.
[ ] source references are preserved where required.
[ ] AI fields are present where AI output is reviewed.
[ ] permission/policy decision references are valid where included.
[ ] review notes are safe by default.
[ ] restricted_notes_omitted is true where notes are restricted.
[ ] expired review is not used for downstream action.
[ ] review scope matches downstream action requirement.
```

---

# 11. Permission Rules

Human review access and reliance may require permissions:

```text
human-review:request
human-review:read
human-review:complete
human-review:rely
human-review:escalate
<object-domain>:review
```

Rules:

```text
- This contract does not grant permission.
- Reviewer authority must be evaluated by Permission Service.
- Review completion requires reviewer_user_reference_id with required permission.
- Downstream reliance on review may require additional permission.
- PermissionDenied must stop review completion or reliance.
```

---

# 12. Policy Rules

Human review is policy-controlled.

Common policies:

```text
HumanReviewRequirementPolicy
HumanReviewReliancePolicy
HumanReviewVisibilityPolicy
AIAgentHumanReviewPolicy
ExternalCommunicationReviewPolicy
WorkflowReviewPolicy
RoutingReviewPolicy
RestrictedReviewNotesPolicy
CrossOrganizationReviewPolicy
```

Rules:

```text
- Policy may require human_review_required = true.
- Policy may define required review_scope.
- Policy may limit who can review.
- Policy may expire review after time or context change.
- Policy may restrict review notes visibility.
- PolicyRestricted must stop or downgrade review access/reliance.
```

---

# 13. AI Agent Rules

AI output review must preserve AI context.

Rules:

```text
- AI-generated drafts, summaries, recommendations and preparation outputs must be reviewable where policy requires.
- Human review must not be implied merely because a User viewed AI output.
- Review must explicitly record review_decision.
- Review must preserve source references and AI context.
- Agent must not self-approve its own output.
```

Required AI review linkage:

```yaml
source:
  ai_assisted: true
  agent_reference_id: string
  agent_registry_key: string
  source_reference_ids: list[string]
```

---

# 14. Event Rules

Human review may be referenced by events.

Rules:

```text
- Human Review Contract does not emit events directly.
- Event Service owns event recording.
- Owning services define which events include human_review_reference_id.
- Event payloads must not expose restricted review notes by default.
- Review trace must distinguish requested, completed, rejected and expired review.
```

Potential event relationships:

```text
TaskCreated may reference human_review_reference_id if task was generated from reviewed AI plan.
CommunicationCreated may reference human_review_reference_id if external draft was reviewed.
WorkflowContractApplied may reference human_review_reference_id if workflow application required review.
RoutingSelected may reference human_review_reference_id if routing selection required review.
```

---

# 15. Error Rules

Controlled human review errors:

```text
HumanReviewRequired
HumanReviewReferenceInvalid
HumanReviewNotCompleted
HumanReviewExpired
HumanReviewScopeMismatch
ReviewerPermissionDenied
ReviewerInvalid
ReviewDecisionInvalid
ReviewPolicyRestricted
ReviewNotesRestricted
HumanReviewAlreadyCompleted
HumanReviewStateInvalid
```

Safe error shape:

```yaml
error:
  code: string
  category: HumanReview | Permission | Policy | Validation | State
  message: string
  safe_detail: string | null
  correlation_id: string | null
  retryable: boolean
```

Rules:

```text
- Errors must follow Error Contract.
- Errors must not expose restricted review notes.
- Errors must not expose hidden policy internals.
- HumanReviewRequired should identify safe review scope where allowed.
```

---

# 16. Versioning Rules

Contract version:

```text
v0.1.0
```

Rules:

```text
- Adding review_scope values requires revision notes.
- Adding review_decision values requires revision notes.
- Renaming review fields is breaking.
- Changing meaning of human_review_required is breaking.
- Changing downstream reliance shape is breaking unless backward compatible.
```

---

# 17. Codex Implementation Notes

Codex must:

```text
cite this Human Review Contract before implementing review-required flows
use Reference Contract for reviewer and target references
use AI Context Contract where AI output is reviewed
use Audit Context Contract for trace
use Error Contract for review errors
validate reviewer_user_reference_id through User Service
invoke Permission Service to validate reviewer authority
invoke Policy Service to determine review requirement and reliance rules
mark AI-assisted reviewed content
preserve source_reference_ids
preserve human_review_reference_id in downstream actions
reject expired review reliance
reject review scope mismatch
write tests for HumanReviewRequired
write tests for ReviewerPermissionDenied
write tests for HumanReviewExpired
write tests for HumanReviewScopeMismatch
write tests for missing reviewer_user_reference_id
write tests that Agent cannot self-approve output
write tests that viewing AI output does not equal review
write tests that restricted review notes are omitted
```

Codex must not:

```text
treat user view as approval
allow AI Agent to approve its own output
execute downstream action from review context alone
ignore review scope
ignore review expiration
expose restricted review notes
skip Permission or Policy checks for reviewer authority
drop source references from reviewed AI output
emit events directly from review contract
```

---

# 18. Acceptance Criteria

This Human Review Contract is accepted only if:

```text
[ ] It defines human review purpose.
[ ] It defines human review meaning.
[ ] It defines human review boundary.
[ ] It cites related owning spec and common contracts.
[ ] It defines related Core objects.
[ ] It defines required references.
[ ] It defines canonical human review shape.
[ ] It defines minimal downstream reliance shape.
[ ] It defines field rules.
[ ] It defines controlled values.
[ ] It defines validation rules.
[ ] It defines Permission rules.
[ ] It defines Policy rules.
[ ] It defines AI Agent rules.
[ ] It defines Event rules.
[ ] It defines error rules.
[ ] It defines versioning rules.
[ ] It defines Codex implementation notes.
```

---

# 19. Revision Notes

| Version | Status | Notes |
|---------|--------|-------|
| 0.1.0 | Draft | Initial common Human Review Contract. Defines review requirement, request, decision, reviewer identity, scope, source linkage, AI review, downstream reliance, validation, permission/policy, event, error and Codex rules. |

---

**End of Common Contract**
