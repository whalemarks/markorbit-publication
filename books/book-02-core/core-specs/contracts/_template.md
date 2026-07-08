# Contract Specification Template

**Spec ID:** B02-CONTRACT-[CATEGORY]-[NAME]  
**Spec Type:** Contract Specification  
**Contract Name:** [Contract Name]  
**Contract File:** core-specs/contracts/[category]/[contract-name].md  
**Contract Category:** Common | API | Service | Event Payload | Agent | Workflow | Validation  
**Related Owning Spec:** [Path to owning spec]  
**Related Domain:** [Domain name or N/A]  
**Related Object Specs:** [List object specs]  
**Related Service Specs:** [List service specs]  
**Related API Specs:** [List API specs]  
**Related Event Specs:** [List event specs]  
**Related Agent Specs:** [List agent specs or N/A]  
**Status:** Draft  
**Version:** 0.1.0  
**Contract Version:** v0.1.0  
**MVP Phase:** [Phase]  
**MVP Depth:** Must Implement | Should Implement | Reserved / Later Implement  
**Owner:** MarkOrbit Publications Editorial Board  

---

# 1. Purpose

Define the purpose of this contract.

This section must explain:

```text
what shape this contract governs
which implementation boundary it stabilizes
which Core spec owns it
which downstream implementation uses it
```

Do not describe UI behavior, product preference or implementation shortcuts here.

---

# 2. Contract Meaning

This contract means:

```text
[Precise contract meaning]
```

This contract does not mean:

```text
[Explicit non-meanings]
```

Required distinction:

```text
Contract defines enforceable shape.
Owning spec defines responsibility.
Owning service executes behavior.
Events preserve trace.
```

---

# 3. Contract Boundary

This contract is responsible for:

```text
field names
required fields
optional fields
reference shape
controlled values
validation rules
safe error shape
version rules
implementation-facing constraints
```

This contract is not responsible for:

```text
business truth ownership
service execution
permission evaluation result
policy evaluation result
event creation
UI layout
database technology
AI model choice
```

---

# 4. Related Owning Spec

Owning spec:

```text
[Path to owning spec]
```

Owning spec rule:

```text
This contract must not expand, override or weaken the responsibility boundary defined by the owning spec.
```

---

# 5. Related Core Objects

Related objects:

```text
[object spec paths]
```

Object reference rules:

```text
- Use explicit reference_id fields.
- Do not merge unrelated object identities.
- Validate cross-object references through owning services.
- Do not infer one domain reference from another domain reference.
```

---

# 6. Required References

Required references:

```yaml
primary_reference_id: string
actor_reference_id: string | null
organization_reference_id: string | null
target_object_type: string | null
target_object_reference_id: string | null
permission_decision_reference_id: string | null
policy_decision_reference_id: string | null
human_review_reference_id: string | null
agent_reference_id: string | null
correlation_id: string | null
```

Rules:

```text
- Required references must be explicit.
- Nullable references must have defined meaning.
- Missing required references must fail validation.
- Archived/deleted references must follow owning domain policy.
```

---

# 7. Contract Shape

Define the canonical contract shape.

```yaml
contract_version: v0.1.0
schema_version: v0.1.0
correlation_id: string | null
idempotency_key: string | null

context:
  actor_reference_id: string | null
  organization_reference_id: string | null
  agent_reference_id: string | null
  agent_registry_key: string | null
  agent_contract_reference_id: string | null

target:
  target_object_type: string | null
  target_object_reference_id: string | null

permission_context:
  permission_decision_reference_id: string | null
  required_permission_keys: list[string]

policy_context:
  policy_decision_reference_id: string | null
  required_policy_scopes: list[string]

human_review_context:
  human_review_required: boolean
  human_review_reference_id: string | null

payload:
  # define contract-specific fields here

audit:
  created_at: datetime | null
  updated_at: datetime | null
  source_type: string | null
```

Rules:

```text
- Contract-specific fields must be placed under payload unless the contract type requires a different canonical shape.
- Context fields must not be hidden inside payload.
- Permission and Policy references must remain explicit.
- AI context must be explicit where AI-generated or AI-assisted output exists.
```

---

# 8. Field Rules

Field rules must define:

```text
field name
type
required/optional
nullable meaning
allowed values if controlled
validation behavior
restricted-data behavior
```

Field rule table:

| Field | Type | Required | Nullable | Rule |
|------|------|----------|----------|------|
| contract_version | string | Yes | No | Must match supported contract version. |
| correlation_id | string | No | Yes | Must be preserved where provided. |
| actor_reference_id | string | Contextual | Yes | Required for protected operations unless system context is allowed. |
| organization_reference_id | string | Contextual | Yes | Required where organization-scoped policy applies. |
| agent_reference_id | string | Contextual | Yes | Required for AI/agent-assisted operations. |
| permission_decision_reference_id | string | Contextual | Yes | Required where prior permission evaluation is mandatory. |
| policy_decision_reference_id | string | Contextual | Yes | Required where prior policy evaluation is mandatory. |
| human_review_reference_id | string | Contextual | Yes | Required where human review is mandatory. |

---

# 9. Controlled Values

Define all controlled values used by this contract.

Example:

```text
status:
  Draft
  Active
  ReviewRequired
  Archived
  Unknown

source_type:
  ProfessionalInput
  SystemGenerated
  AIAssisted
  Migration
  APIRequest
  Unknown

data_access_scope:
  MetadataOnly
  SafeSummaryOnly
  PolicyFilteredContent
  RestrictedContentWithHumanApproval
  Unknown
```

Rules:

```text
- Controlled values must match owning specs.
- Unknown may be allowed only when the owning spec allows it.
- Adding a controlled value requires version notes.
- Removing or changing meaning of a controlled value is breaking.
```

---

# 10. Validation Rules

Validation checklist:

```text
[ ] contract_version is present and supported.
[ ] required context fields are present.
[ ] required target references are present.
[ ] controlled values are valid.
[ ] field types are valid.
[ ] nullable fields have allowed null meaning.
[ ] cross-domain references are valid or scheduled for service validation.
[ ] permission context is present where required.
[ ] policy context is present where required.
[ ] human review context is present where required.
[ ] AI context is present where AI-assisted.
[ ] restricted fields are omitted unless policy allows them.
[ ] idempotency requirements are satisfied where applicable.
[ ] error behavior is defined.
```

Validation failure must produce a controlled error.

---

# 11. Permission Rules

Required permissions:

```text
[permission:key]
```

Rules:

```text
- This contract must not grant permission.
- Permission evaluation must be performed by Permission Service.
- Contract may require permission_decision_reference_id.
- PermissionDenied must stop protected behavior.
```

Non-applicability:

```text
If this contract does not require permission rules, state why.
```

---

# 12. Policy Rules

Required policies:

```text
[PolicyScope]
```

Rules:

```text
- This contract must not evaluate policy.
- Policy evaluation must be performed by Policy Service.
- Contract may require policy_decision_reference_id.
- Policy may restrict, downgrade or block payload fields.
- PolicyRestricted must stop or downgrade protected behavior.
```

Non-applicability:

```text
If this contract does not require policy rules, state why.
```

---

# 13. AI Agent Rules

AI context shape:

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
- Agent identity must be explicit.
- Data access scope must be explicit.
- Human review requirement must be explicit.
- AI output must not be treated as professional truth by default.
- Restricted data must not be included unless policy allows it.
```

Non-applicability:

```text
If this contract has no AI involvement, state that AI context is Not Applicable.
```

---

# 14. Event Rules

Event behavior:

```text
[Describe event behavior or Not Applicable]
```

Rules:

```text
- Contracts must not emit events directly.
- Events must be emitted by owning services.
- Event payload contracts must cite owning Event specs.
- Event payloads must not be replayed as commands unless a command contract explicitly allows it.
```

Non-applicability:

```text
If no event behavior exists, state that event behavior is Not Applicable.
```

---

# 15. Error Rules

Safe error shape:

```yaml
error:
  code: string
  category: string
  message: string
  safe_detail: string | null
  correlation_id: string | null
  retryable: boolean
```

Controlled errors:

```text
BadRequest
Unauthorized
PermissionDenied
PolicyRestricted
NotFound
ValidationFailed
ReferenceInvalid
StateInvalid
RestrictedFieldViolation
HumanReviewRequired
AgentContractRequired
IdempotencyConflict
VersionUnsupported
InternalError
```

Rules:

```text
- Errors must be safe to display.
- Errors must not expose restricted data.
- Errors must not expose permission or policy internals.
- Errors must preserve correlation_id where available.
```

---

# 16. Versioning Rules

Contract version:

```text
v0.1.0
```

Rules:

```text
- Breaking field changes require version change.
- Controlled value additions require revision notes.
- Field removals require migration plan.
- Error shape changes are breaking unless backward compatible.
- Event payload changes must preserve consumer safety.
```

---

# 17. Codex Implementation Notes

Codex must:

```text
cite this contract before implementation
cite the owning spec
generate typed DTOs or equivalent structures
generate validators from validation rules
use controlled values exactly
validate required references
validate permission/policy/human-review context where required
preserve correlation_id
enforce idempotency where required
return safe error shape
write tests for required fields
write tests for controlled values
write tests for invalid references
write tests for PermissionDenied where applicable
write tests for PolicyRestricted where applicable
write tests for AI/human review rules where applicable
```

Codex must not:

```text
invent fields outside this contract without updating the contract
merge unrelated domains into one payload
treat contract example as permission grant
skip validation for convenience
expose restricted fields in errors
emit events directly from API payloads
allow AI output to bypass contract rules
```

---

# 18. Acceptance Criteria

This Contract Specification is accepted only if:

```text
[ ] It defines contract purpose.
[ ] It defines contract meaning.
[ ] It defines contract boundary.
[ ] It cites related owning spec.
[ ] It cites related Core objects.
[ ] It defines required references.
[ ] It defines contract shape.
[ ] It defines field rules.
[ ] It defines controlled values.
[ ] It defines validation rules.
[ ] It defines Permission rules or states non-applicability.
[ ] It defines Policy rules or states non-applicability.
[ ] It defines AI Agent rules or states non-applicability.
[ ] It defines Event rules or states non-applicability.
[ ] It defines error rules.
[ ] It defines versioning rules.
[ ] It defines Codex implementation notes.
```

---

# 19. Revision Notes

| Version | Status | Notes |
|---------|--------|-------|
| 0.1.0 | Draft | Initial contract template. |

---

**End of Contract Specification Template**
