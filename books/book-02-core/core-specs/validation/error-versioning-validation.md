# Error Versioning Validation

**Spec ID:** B02-VALIDATION-ERROR-VERSIONING  
**Spec Type:** Validation Specification  
**Spec File:** core-specs/validation/error-versioning-validation.md  
**Related Book:** Book 02 — MarkOrbit Core Specification  
**Related Validation Index:** core-specs/validation/index.md  
**Related Architecture Validation:** core-specs/validation/architecture-consistency-validation.md  
**Related Traceability Validation:** core-specs/validation/traceability-validation.md  
**Related Permission Policy Validation:** core-specs/validation/permission-policy-validation.md  
**Related Idempotency Event Validation:** core-specs/validation/idempotency-event-validation.md  
**Related Common Contracts:** core-specs/contracts/common/errors.md; core-specs/contracts/common/versioning.md  
**Related Test Contract:** core-specs/contracts/tests/error-versioning-tests.md  
**Related Codex Task:** codex-tasks/TASK-006-error-versioning-validation.md  
**Status:** Draft  
**Version:** 0.1.0  
**Validation Priority:** P0  
**Validation Depth:** Error Level 3; Versioning Level 1  
**Owner:** MarkOrbit Publications Editorial Board  

---

# 1. Purpose

This file defines how to validate Error and Versioning behavior in MarkOrbit Core.

Error Versioning Validation ensures that all failures are safe, controlled and traceable, and that unsupported versions fail closed.

It validates the rules:

```text
Errors must be safe.
Errors must not leak restricted data.
Unsupported versions must fail closed.
Missing required versions must fail safely.
Historical versions must not be silently rewritten.
```

This validation is required before API validators, Workflow validators, Agent boundary tests and the MVP execution spine are accepted.

---

# 2. Core Lock

```text
Errors must be controlled, safe and traceable.
Errors must not expose restricted data, database IDs, stack traces, policy internals, permission internals, prompt internals or hidden reasoning.
Errors must preserve correlation where available.
Errors must use controlled error codes.
Unsupported versions must fail closed.
Missing required versions must fail safely.
Deprecated versions must not be silently upgraded.
Historical versions must not be silently rewritten.
Version context must be preserved for records, events, workflow applications and AI-assisted outputs where applicable.
Codex must preserve safe failure and version boundaries.
```

---

# 3. Validation Scope

This validation covers:

```text
Error Contract
Versioning Contract
safe error shape
controlled error codes
error leakage prevention
non-disclosure error behavior
Permission/Policy error behavior
AI error safety
Idempotency error behavior
Event error behavior
API error behavior
Workflow error behavior
Agent error behavior
version validation
supported version registry
deprecated version behavior
historical version preservation
test traceability
Codex task traceability
```

This validation does not cover:

```text
production incident response
external logging vendor integration
full observability platform
full migration engine
full deprecation lifecycle automation
API gateway release routing
security operations dashboard
```

---

# 4. Required Source Files

Validation must inspect:

```text
core-specs/TRACEABILITY.md
core-specs/implementation/mvp-cut-v0.1.md
core-specs/implementation/implementation-depth-matrix.md
core-specs/DEVELOPER_START_HERE.md
core-specs/codex/CODEX-TASK-INDEX.md
core-specs/contracts/common/errors.md
core-specs/contracts/common/versioning.md
core-specs/contracts/common/references.md
core-specs/contracts/common/audit-context.md
core-specs/contracts/common/permission-context.md
core-specs/contracts/common/policy-context.md
core-specs/contracts/common/ai-context.md
core-specs/contracts/common/human-review.md
core-specs/contracts/common/idempotency.md
core-specs/contracts/tests/error-versioning-tests.md
codex-tasks/TASK-006-error-versioning-validation.md
core-specs/validation/index.md
core-specs/validation/architecture-consistency-validation.md
core-specs/validation/traceability-validation.md
core-specs/validation/permission-policy-validation.md
core-specs/validation/idempotency-event-validation.md
```

Validation should also inspect:

```text
core-specs/contracts/api/
core-specs/contracts/workflows/
core-specs/workflows/
core-specs/agents/
core-specs/events/
codex-tasks/
```

---

# 5. Error Shape Validation

Every public error must follow a safe controlled shape.

Required shape:

```yaml
error:
  code: string
  category: string
  message: string
  safe_detail: object | string | null
  correlation_id: string | null
  retryable: boolean
  restricted_fields_omitted: boolean | null
```

Validate:

```text
[ ] error.code is controlled.
[ ] error.category is controlled.
[ ] error.message is safe.
[ ] safe_detail is safe.
[ ] correlation_id is preserved where provided.
[ ] retryable is explicit.
[ ] restricted_fields_omitted is true where redaction affects error output.
[ ] raw exception content is not exposed.
```

Blocked if:

```text
MVP failure path returns raw exception.
MVP failure path returns unsafe string-only error.
MVP error shape omits controlled code.
```

---

# 6. Controlled Error Code Validation

Required controlled error codes:

```text
ValidationFailed
ReferenceInvalid
PermissionDenied
PolicyRestricted
HumanReviewRequired
IdempotencyKeyRequired
IdempotencyConflict
VersionUnsupported
StateInvalid
NotFound
Conflict
InternalError
```

Validate:

```text
[ ] Each required code is defined.
[ ] Each code maps to a safe category.
[ ] Each code maps to a safe default message.
[ ] Each code maps to retryable default.
[ ] Each code defines allowed safe_detail shape.
[ ] InternalError never exposes internal exception content.
```

Blocked if:

```text
PermissionDenied or PolicyRestricted missing.
IdempotencyConflict missing.
VersionUnsupported missing.
InternalError leaks raw exception.
```

---

# 7. Leakage Prevention Validation

Errors must not expose:

```text
database IDs
raw customer data
restricted trademark data
restricted documents
evidence content
provider commercial terms
private notes
policy rule internals
permission rule internals
agent prompt internals
system prompts
developer prompts
hidden reasoning
raw stack traces
secrets or tokens
connector credentials
production file paths
```

Validate:

```text
[ ] Database ID-like values are not exposed.
[ ] Stack traces are stripped.
[ ] Internal exception class details are stripped.
[ ] Restricted fields are stripped.
[ ] Prompt internals are stripped.
[ ] Hidden reasoning is stripped.
[ ] Tool/model/provider raw errors are sanitized.
```

Architecture violation:

```text
public error leaks database ID
public error leaks stack trace
public error leaks restricted data
public error leaks prompt or hidden reasoning
```

---

# 8. Non-Disclosure Error Validation

When Policy requires non-disclosure:

```text
NotFound may replace PolicyRestricted.
Object existence must not be revealed.
Source existence must not be revealed.
Event existence must not be revealed.
safe_detail must not reveal hidden existence.
pagination totals must not reveal hidden objects.
idempotency replay must not leak hidden prior result.
```

Validate:

```text
[ ] PolicyNonDisclosureNotFound is supported.
[ ] Error message does not reveal hidden existence.
[ ] safe_detail does not reveal hidden existence.
[ ] Event errors do not reveal hidden event existence.
[ ] Idempotency conflict/replay does not reveal hidden previous result.
```

Architecture violation:

```text
NotFound substitution reveals object exists.
PolicyRestricted error reveals hidden object details.
Idempotency replay reveals policy-hidden prior result.
```

---

# 9. Permission / Policy Error Validation

Validate:

```text
[ ] PermissionDenied error is safe.
[ ] PolicyRestricted error is safe.
[ ] Permission error does not expose permission graph or rule internals.
[ ] Policy error does not expose policy rule internals.
[ ] Decision references are returned only where Policy allows.
[ ] Restricted object data does not appear in error output.
[ ] correlation_id is preserved.
```

Blocked if:

```text
PermissionDenied exposes target details Policy hides.
PolicyRestricted exposes policy internals.
```

---

# 10. Human Review Error Validation

Validate:

```text
[ ] HumanReviewRequired error is controlled.
[ ] Missing review returns HumanReviewRequired where required.
[ ] Error does not imply approval.
[ ] Error does not execute downstream action.
[ ] Error does not bypass Permission.
[ ] Error does not bypass Policy.
```

Architecture violation:

```text
HumanReviewRequired creates approval side effect.
HumanReviewRequired reveals restricted data.
```

---

# 11. AI Error Safety Validation

AI-related errors must not expose:

```text
system prompts
developer prompts
hidden reasoning
tool raw payloads with restricted data
restricted source contents
provider raw error text containing sensitive context
policy-omitted source details
```

Validate:

```text
[ ] AI/tool/model errors are sanitized.
[ ] AI errors preserve correlation_id.
[ ] AI errors use controlled error code.
[ ] AI errors do not expose hidden reasoning.
[ ] AI errors do not expose restricted source contents.
[ ] AI errors do not convert AI failure into professional truth.
```

Architecture violation:

```text
AI error leaks prompt internals.
AI error leaks hidden reasoning.
AI error leaks restricted source.
```

---

# 12. Idempotency Error Validation

Validate:

```text
[ ] Missing idempotency_key returns IdempotencyKeyRequired.
[ ] Same key + different semantic request returns IdempotencyConflict.
[ ] IdempotencyConflict creates no side effects.
[ ] IdempotencyConflict emits no Event.
[ ] IdempotencyConflict does not expose original restricted payload.
[ ] IdempotencyConflict does not reveal hidden target existence.
[ ] Idempotency errors use Error Contract.
```

Architecture violation:

```text
IdempotencyConflict leaks original request.
IdempotencyConflict mutates state.
IdempotencyConflict emits Event.
```

---

# 13. Event Error Validation

Validate:

```text
[ ] Event read/search errors use Error Contract.
[ ] Event visibility errors do not expose restricted payload.
[ ] Hidden Event errors do not reveal Event existence.
[ ] Event version errors use VersionUnsupported.
[ ] Event errors do not expose raw database IDs.
[ ] Event errors do not expose stack traces.
```

Architecture violation:

```text
Event error leaks restricted payload.
Event error reveals hidden Event exists.
```

---

# 14. API Error Validation

Validate:

```text
[ ] API failure paths use Error Contract.
[ ] API validation errors do not echo restricted payload.
[ ] API errors preserve correlation_id.
[ ] API errors include retryable flag.
[ ] API errors do not expose stack traces.
[ ] API errors do not expose database IDs.
[ ] API errors do not expose Permission/Policy internals.
[ ] API unsupported version returns VersionUnsupported.
```

Blocked if:

```text
MVP API returns raw exception or unsafe error.
```

---

# 15. Workflow Error Validation

Validate:

```text
[ ] Workflow validation errors use Error Contract.
[ ] Workflow preview errors have no side effects.
[ ] Workflow apply errors preserve idempotency safety.
[ ] Workflow errors do not expose restricted workflow inputs.
[ ] Workflow errors do not expose stack traces.
[ ] Workflow unsupported version returns VersionUnsupported.
[ ] Workflow errors preserve correlation_id.
```

Architecture violation:

```text
workflow error emits Event
workflow error creates Task
workflow error leaks restricted source
```

---

# 16. Agent Error Validation

Validate:

```text
[ ] Agent errors use Error Contract.
[ ] Agent forbidden-action errors are controlled.
[ ] Agent errors do not expose prompt internals.
[ ] Agent errors do not expose hidden reasoning.
[ ] Agent errors do not expose restricted sources.
[ ] Agent errors preserve HumanReviewRequired where needed.
[ ] Agent errors do not mutate protected state.
```

Architecture violation:

```text
agent error leaks hidden reasoning
agent error leaks system prompt
agent error leaks restricted source
agent forbidden-action error still executes action
```

---

# 17. Retryability Validation

Validate retryable flag behavior.

Default non-retryable:

```text
ValidationFailed
ReferenceInvalid
PermissionDenied
PolicyRestricted
HumanReviewRequired
IdempotencyKeyRequired
IdempotencyConflict
VersionUnsupported
StateInvalid
NotFound
Conflict
```

InternalError may be retryable only if safe.

Checks:

```text
[ ] retryable is explicit.
[ ] governance errors are not retryable by default.
[ ] validation errors are not retryable by default.
[ ] conflict errors are not retryable by default.
[ ] retryable true does not imply side-effect repetition.
```

---

# 18. Version Field Validation

Required version fields:

```text
contract_version
schema_version where applicable
api_version where applicable
workflow_contract_version where applicable
event_schema_version where applicable
agent_contract_version where applicable
```

Validate:

```text
[ ] Required version field is present.
[ ] Supported version is accepted.
[ ] Unsupported version returns VersionUnsupported.
[ ] Missing required version fails safely.
[ ] Version mismatch fails safely where incompatible.
[ ] Errors do not expose restricted payload on version failure.
```

Blocked if:

```text
MVP API/workflow/event accepts unsupported version silently.
```

---

# 19. Supported Version Registry Validation

Validate:

```text
[ ] Supported version registry or equivalent exists.
[ ] MVP supported version is documented.
[ ] Registry can validate contract_version.
[ ] Registry can validate schema_version where applicable.
[ ] Unsupported version returns VersionUnsupported.
[ ] VersionUnsupported error is safe.
```

MVP expected version:

```text
v0.1.0
```

If another format is used, validation must require explicit mapping.

---

# 20. Deprecated Version Validation

Validate:

```text
[ ] Deprecated version is not silently upgraded.
[ ] Deprecated version is not silently rewritten.
[ ] Warning may be returned only if contract supports it.
[ ] Historical records preserve original version.
[ ] Deprecated version behavior is tested.
```

Architecture violation:

```text
deprecated version silently rewritten to current version
deprecated version accepted as current without trace
```

---

# 21. Historical Version Preservation

Where records are created, version context must be preserved.

Required records:

```text
Event records
Workflow application records
AI-assisted output records where applicable
created object records where applicable
idempotent result records where applicable
```

Validate:

```text
[ ] contract_version is preserved.
[ ] schema_version is preserved.
[ ] workflow_contract_version is preserved where applicable.
[ ] agent_contract_version is preserved where applicable.
[ ] event_schema_version is preserved where applicable.
[ ] Historical versions are not silently rewritten.
```

Blocked if:

```text
MVP event/workflow application record lacks version trace.
```

---

# 22. Permission / Policy Version Interaction

Validate:

```text
[ ] Permission/Policy errors remain safe under version failure.
[ ] VersionUnsupported does not reveal restricted payload.
[ ] Policy redaction still applies to version error details.
[ ] PermissionDenied remains safe under unsupported version.
```

---

# 23. Idempotency / Event Version Interaction

Validate:

```text
[ ] Idempotency fingerprint includes contract_version where required.
[ ] Event record preserves schema_version.
[ ] Unsupported Event schema version fails closed.
[ ] IdempotencyConflict under version mismatch is safe.
[ ] Historical Event versions are preserved.
```

---

# 24. Test Traceability Validation

Validate:

```text
[ ] error-versioning-tests.md exists.
[ ] TASK-006 exists.
[ ] Safe error shape tests exist.
[ ] Controlled error code tests exist.
[ ] Database ID leakage tests exist.
[ ] Stack trace leakage tests exist.
[ ] Restricted data leakage tests exist.
[ ] Policy/Permission internals leakage tests exist.
[ ] Prompt/hidden reasoning leakage tests exist.
[ ] correlation_id preservation tests exist.
[ ] retryable flag tests exist.
[ ] NotFound substitution tests exist.
[ ] Supported version tests exist.
[ ] Unsupported version tests exist.
[ ] Missing version tests exist.
[ ] Deprecated version not rewritten tests exist.
[ ] Historical version preservation tests exist.
```

Blocked if:

```text
Error/Versioning tests missing.
No leakage tests.
No VersionUnsupported tests.
```

---

# 25. Validation Procedure

Perform validation in this order:

```text
1. Confirm Error and Versioning source files exist.
2. Validate Error shape.
3. Validate controlled error codes.
4. Validate leakage prevention.
5. Validate non-disclosure error behavior.
6. Validate Permission/Policy errors.
7. Validate Human Review errors.
8. Validate AI error safety.
9. Validate Idempotency errors.
10. Validate Event errors.
11. Validate API errors.
12. Validate Workflow errors.
13. Validate Agent errors.
14. Validate retryability.
15. Validate version fields.
16. Validate supported version registry.
17. Validate deprecated version behavior.
18. Validate historical version preservation.
19. Validate Permission/Policy version interaction.
20. Validate Idempotency/Event version interaction.
21. Validate test traceability.
22. Classify findings.
23. Produce validation report.
```

---

# 26. Finding Classification

Use:

```text
Pass
Warning
Blocked
Architecture Violation
Out of Scope
Deferred
```

Classification rules:

```text
Blocked = Must Build Now failure path lacks safe error or version validation.
Architecture Violation = unsafe leakage or unsupported version accepted silently.
Warning = future version lifecycle incomplete but safe.
Out of Scope = valid but beyond MVP.
Deferred = later migration/deprecation tooling.
Pass = sufficient for current depth.
```

---

# 27. Required Evidence

Every finding must include:

```text
error/version area
operation or failure path
source file
affected API/workflow/service/agent/event
MVP category
implementation depth
required fix
Codex impact
```

Example:

```text
Finding: VersionUnsupported missing from workflow apply.
Status: Blocked
Area: Workflow Versioning
Operation: trademark-application-workflow apply
Required Fix: Add workflow_contract_version validation and VersionUnsupported test.
Codex Impact: Block TASK-006, TASK-008 and TASK-010.
```

---

# 28. Architecture Violation Triggers

The following always fail validation:

```text
Public error exposes raw database ID.
Public error exposes stack trace.
Public error exposes restricted data.
Public error exposes policy internals.
Public error exposes permission internals.
Public error exposes system/developer prompt.
Public error exposes hidden reasoning.
InternalError returns raw exception content.
PolicyNonDisclosureNotFound reveals object existence.
IdempotencyConflict leaks original restricted payload.
Event error leaks restricted payload.
Unsupported version is silently accepted.
Missing required version is silently accepted.
Deprecated version is silently rewritten.
Historical version is silently rewritten.
Version failure leaks restricted payload.
```

---

# 29. Acceptance Criteria

Error Versioning Validation passes only if:

```text
[ ] Required source files exist.
[ ] Error shape is defined and safe.
[ ] Required controlled error codes exist.
[ ] Leakage prevention is defined.
[ ] Non-disclosure error behavior is safe.
[ ] Permission/Policy errors are safe.
[ ] Human Review errors are safe.
[ ] AI errors are safe.
[ ] Idempotency errors are safe.
[ ] Event errors are safe.
[ ] API errors are safe.
[ ] Workflow errors are safe.
[ ] Agent errors are safe.
[ ] retryable behavior is explicit.
[ ] Version fields are validated.
[ ] Supported version registry or equivalent exists.
[ ] Unsupported versions fail closed.
[ ] Deprecated versions are not silently rewritten.
[ ] Historical versions are preserved where required.
[ ] Test traceability exists.
[ ] No Architecture Violation exists.
[ ] No Blocked finding exists in Must Build Now failure/version behavior.
```

---

# 30. Validation Report Template

```text
Validation: Error Versioning
Status: Pass | Warning | Blocked | Architecture Violation
Scope: Errors / Versioning

Sources Checked:
- <file>
- <file>

Findings:
- <finding>

Evidence:
- Area:
- Operation / Failure Path:
- File / Section:

Required Fix:
- <fix>

Codex Impact:
- <task affected>

Decision:
- Proceed | Proceed with warning | Block | Defer
```

---

# 31. Codex Usage

Codex must use this validation:

```text
before implementing TASK-006-error-versioning-validation
before implementing API validators
before implementing workflow validators
before implementing agent boundary tests
before implementing MVP execution spine
after modifying Error or Versioning contracts
during PR review
```

Codex must not:

```text
return raw exceptions
return stack traces
echo full invalid restricted payloads
expose Permission/Policy internals
expose prompts or hidden reasoning
accept unsupported versions silently
rewrite deprecated versions silently
rewrite historical versions silently
skip leakage tests
skip VersionUnsupported tests
```

---

# 32. Revision Notes

| Version | Status | Notes |
|---------|--------|-------|
| 0.1.0 | Draft | Initial Error Versioning Validation. Defines safe error shape, controlled error codes, leakage prevention, non-disclosure, Permission/Policy, Human Review, AI, Idempotency, Event, API, Workflow and Agent error safety, retryability, version validation, supported registry, deprecated version and historical version checks. |

---

**End of Error Versioning Validation**
