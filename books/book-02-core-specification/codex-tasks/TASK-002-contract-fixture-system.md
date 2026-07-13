# TASK-002 — Contract Fixture System

**Task ID:** TASK-002  
**Task Type:** Codex Implementation Task  
**Task File:** codex-tasks/TASK-002-contract-fixture-system.md  
**Task Title:** Contract Fixture System  
**Related Book:** Book 02 — MarkOrbit Core Specification  
**Related Task Index:** core-specs/codex/CODEX-TASK-INDEX.md  
**Related Previous Task:** codex-tasks/TASK-001-common-contract-foundation.md  
**Related Developer Guide:** core-specs/DEVELOPER_START_HERE.md  
**Related Traceability:** core-specs/TRACEABILITY.md  
**Related MVP Cut:** core-specs/implementation/mvp-cut-v0.1.md  
**Related Depth Matrix:** core-specs/implementation/implementation-depth-matrix.md  
**Related Contract Layer:** core-specs/contracts/  
**Status:** Draft  
**Version:** 0.1.0  
**MVP Category:** Must Build Now  
**Implementation Depth:** Level 3 for deterministic non-production fixtures  
**Owner:** MarkOrbit Publications Editorial Board  

---

# 1. Purpose

This task creates the deterministic fixture system required by MarkOrbit Core contract tests.

Fixtures are required before broad test implementation because all later tests must use consistent, safe and non-production data.

This task supports:

```text
Common Contract Tests
API Contract Tests
Workflow Contract Tests
Agent Boundary Tests
Permission Policy Tests
Idempotency Event Tests
Error Versioning Tests
MVP execution spine tests
```

The fixture system must make contract tests reproducible and must prevent Codex from inventing ad hoc test data inside each test file.

---

# 2. Core Lock

```text
Fixtures support Core verification.
Fixtures must be deterministic.
Fixtures must be non-production.
Fixtures must be safe to commit.
Fixtures must cover positive and negative cases.
Fixtures must not define architecture.
Fixtures must not fake protected behavior as allowed.
Fixtures must preserve Permission and Policy fail-closed rules.
Fixtures must preserve AI boundaries.
Fixtures must preserve Idempotency and Event trace rules.
Codex implements fixtures from traced specifications.
Codex does not create production data.
```

---

# 3. Required Source Files

Codex must read these files before implementation:

```text
core-specs/DEVELOPER_START_HERE.md
core-specs/TRACEABILITY.md
core-specs/implementation/mvp-cut-v0.1.md
core-specs/implementation/implementation-depth-matrix.md
core-specs/codex/CODEX-TASK-INDEX.md
codex-tasks/TASK-001-common-contract-foundation.md
core-specs/contracts/common/index.md
core-specs/contracts/tests/index.md
core-specs/contracts/tests/template.md
core-specs/contracts/tests/common-contract-tests.md
core-specs/contracts/tests/api-contract-tests.md
core-specs/contracts/tests/workflow-contract-tests.md
core-specs/contracts/tests/agent-boundary-tests.md
core-specs/contracts/tests/permission-policy-tests.md
core-specs/contracts/tests/idempotency-event-tests.md
core-specs/contracts/tests/error-versioning-tests.md
```

Codex should also read the Common Contracts:

```text
core-specs/contracts/common/references.md
core-specs/contracts/common/errors.md
core-specs/contracts/common/pagination.md
core-specs/contracts/common/audit-context.md
core-specs/contracts/common/ai-context.md
core-specs/contracts/common/human-review.md
core-specs/contracts/common/permission-context.md
core-specs/contracts/common/policy-context.md
core-specs/contracts/common/idempotency.md
core-specs/contracts/common/versioning.md
```

---

# 4. Scope

This task covers fixture design and fixture implementation for:

```text
References
Errors
Pagination
Audit Context
AI Context
Human Review
Permission Context
Policy Context
Idempotency
Versioning
Events
API request/response examples
Workflow preview/apply examples
Agent boundary examples
MVP domain object examples
```

This task should create a fixture system that later tasks can reuse.

---

# 5. Out of Scope

This task must not implement:

```text
production database seeding
real customer records
real trademark records
real provider records
real official filing data
real email content
real credentials
external connector fixtures with secrets
full API validators
full workflow validators
full agent runtime
full business services
```

Fixtures are test inputs and expected outputs. They are not production demo data.

---

# 6. Suggested Fixture Structure

Codex may adapt to the repo structure, but should prefer a clear fixture layout such as:

```text
tests/
  fixtures/
    contracts/
      references/
        valid_reference.json
        invalid_reference.json
        database_id_like_reference.json
        wrong_type_reference.json

      errors/
        validation_failed.json
        permission_denied.json
        policy_restricted.json
        human_review_required.json
        idempotency_conflict.json
        version_unsupported.json

      permissions/
        permission_allowed.json
        permission_denied.json
        permission_unknown.json

      policies/
        policy_allowed.json
        policy_restricted_block.json
        policy_restricted_redact.json
        policy_requires_human_review.json
        policy_nondisclosure_notfound.json

      ai/
        valid_ai_context.json
        invalid_ai_context.json
        ai_policy_omissions.json
        ai_forbidden_action.json

      human_review/
        valid_human_review.json
        missing_human_review.json
        rejected_human_review.json

      idempotency/
        first_request.json
        replay_same_request.json
        conflict_different_request.json

      events/
        visible_event.json
        restricted_event.json
        redacted_event.json
        hidden_event.json

      versions/
        supported_version.json
        unsupported_version.json
        missing_version.json
        deprecated_version.json

      api/
        customer_create_request.json
        customer_create_response.json
        trademark_create_request.json
        trademark_create_response.json
        communication_create_request.json
        communication_create_response.json

      workflows/
        customer_intake_preview_request.json
        customer_intake_apply_request.json
        trademark_application_preview_request.json
        trademark_application_apply_request.json
        communication_review_preview_request.json
        communication_review_apply_request.json
```

If the repo uses TypeScript or another framework, the fixture folder may be equivalent.

---

# 7. Fixture Naming Rules

Fixture files must use:

```text
lowercase-kebab-case or lowercase_snake_case
clear positive/negative distinction
one fixture per behavior case
```

Good examples:

```text
permission_allowed.json
policy_restricted_redact.json
idempotency_conflict_different_request.json
unsupported_contract_version.json
ai_forbidden_send_action.json
```

Bad examples:

```text
test1.json
sample.json
data.json
real_customer.json
prod_case.json
```

---

# 8. Required Fixture Families

## 8.1 Reference Fixtures

Required:

```text
valid_reference
invalid_reference
wrong_type_reference
database_id_like_reference
hidden_object_reference
cross_organization_reference
```

Must test:

```text
public reference shape
database ID rejection
type mismatch
hidden object behavior
reference does not imply permission
```

## 8.2 Error Fixtures

Required:

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
InternalErrorSafe
```

Must test:

```text
safe error shape
correlation_id
retryable flag
no stack trace
no database ID leakage
no restricted data leakage
```

## 8.3 Permission Fixtures

Required:

```text
PermissionAllowed
PermissionDenied
UnknownPermission
MissingPermissionContext
CrossOrganizationPermission
```

Must test:

```text
allowed decision
denied decision
unknown fails closed
missing context fails closed
```

## 8.4 Policy Fixtures

Required:

```text
PolicyAllowed
PolicyRestrictedBlock
PolicyRestrictedRedact
PolicyRequiresHumanReview
PolicyNonDisclosureNotFound
UnknownPolicy
MissingPolicyContext
CrossOrganizationPolicyRestricted
```

Must test:

```text
allowed decision
blocked action
redacted output
review-required gate
NotFound substitution
unknown policy fails closed
```

## 8.5 AI Context Fixtures

Required:

```text
ValidAIContext
InvalidAIContext
AIForbiddenActionApprove
AIForbiddenActionSend
AIForbiddenActionSubmit
AIPolicyOmissions
AISourceScopeLimited
AIHumanReviewRequired
```

Must test:

```text
capability scope
source scope
policy omissions
forbidden actions
human review preservation
```

## 8.6 Human Review Fixtures

Required:

```text
ValidHumanReview
MissingHumanReview
RejectedHumanReview
ExpiredHumanReview
WrongReviewerHumanReview
```

Must test:

```text
human_review_reference_id
review status
required review gate
review does not execute downstream action
```

## 8.7 Idempotency Fixtures

Required:

```text
MissingIdempotencyKey
ValidFirstRequest
ReplaySameRequest
ConflictDifferentRequest
DuplicateTaskReplay
DuplicateCommunicationReplay
DuplicateEventReplay
```

Must test:

```text
required key
safe replay
conflict detection
no duplicate effects
```

## 8.8 Event Fixtures

Required:

```text
VisibleEvent
RestrictedEvent
RedactedEvent
HiddenEvent
DuplicateEventAttempt
EventReferenceNotCommand
CausationEventReference
CorrelationEventGroup
```

Must test:

```text
event trace
event visibility
redaction
hidden events
no duplicate events
event reference not command
```

## 8.9 Version Fixtures

Required:

```text
SupportedContractVersion
UnsupportedContractVersion
MissingContractVersion
SupportedSchemaVersion
UnsupportedSchemaVersion
DeprecatedVersion
HistoricalVersionRecord
```

Must test:

```text
supported version accepted
unsupported version fails closed
missing version fails
deprecated version not silently rewritten
historical version preserved
```

## 8.10 API Fixtures

Required MVP API fixture families:

```text
identity
organization
user
permission
policy
customer
brand
trademark
jurisdiction
classification
document
evidence
matter
order
workflow-contract
task
event
communication
```

Each MVP API fixture family should include:

```text
create_request where applicable
create_response where applicable
read_request
read_response
search_request where applicable
search_response where applicable
invalid_reference_request
permission_denied_request
policy_restricted_request
unsupported_version_request
```

## 8.11 Workflow Fixtures

Required MVP workflow fixture families:

```text
customer_intake
trademark_application
communication_review
```

Each workflow fixture family should include:

```text
preview_request
preview_response
apply_request
apply_response
missing_permission_request
policy_restricted_request
human_review_required_request
idempotency_replay_request
idempotency_conflict_request
unsupported_version_request
```

Stub workflow fixture families:

```text
office_action_response
provider_routing
renewal
assignment
evidence_review
```

Stub workflows may include preview-only or validation-only fixtures.

---

# 9. Fixture Safety Rules

Fixtures must not include:

```text
real customer names
real applicant names
real trademark serial numbers unless clearly fictional
real email addresses
real phone numbers
real street addresses
real official filing documents
real provider commercial terms
real credentials
tokens
API keys
secrets
production IDs
database IDs
```

Use fictional-safe data such as:

```text
customer_reference_id: "cust_ref_demo_001"
trademark_reference_id: "tm_ref_demo_001"
matter_reference_id: "mat_ref_demo_001"
order_reference_id: "ord_ref_demo_001"
communication_reference_id: "comm_ref_demo_001"
```

Do not use raw integer IDs such as:

```text
1
123
98765
```

unless the fixture is specifically testing database ID rejection.

---

# 10. Fixture Validation Requirements

Codex should add a fixture validation script or test that checks:

```text
all fixture files are valid JSON/YAML where applicable
fixture names follow naming rules
fixtures contain no forbidden production-looking data
required fixture families exist
required positive and negative cases exist
reference IDs use public reference shape
unsupported version fixtures are present
permission denied fixtures are present
policy restricted fixtures are present
AI forbidden action fixtures are present
idempotency conflict fixtures are present
```

Suggested test:

```text
tests/contracts/test_fixture_integrity.py
```

or equivalent.

---

# 11. Required Tests

This task must add or prepare tests for:

```text
fixture files load successfully
required fixture families exist
fixtures are deterministic
fixtures do not include production data patterns
reference fixtures include valid and invalid references
permission fixtures include allowed, denied and unknown
policy fixtures include allowed, blocked, redacted, review-required and non-disclosure
AI fixtures include forbidden actions
human review fixtures include missing and valid review
idempotency fixtures include replay and conflict
event fixtures include visible, restricted and event-reference-not-command
version fixtures include supported, unsupported, missing and deprecated versions
```

---

# 12. Dependency on TASK-001

This task depends on TASK-001.

If TASK-001 has been implemented:

```text
Use the Common Contract primitives to validate fixtures.
```

If TASK-001 has not been implemented:

```text
Create fixtures only.
Create fixture integrity tests that do not require runtime helpers.
Do not fake missing Common Contract primitives.
Mark runtime validation as blocked until TASK-001 exists.
```

---

# 13. Forbidden Shortcuts

Codex must not:

```text
put all fixtures into one giant file
use production data
use real customer or trademark data
use raw database IDs except in rejection fixtures
skip negative fixtures
skip AI forbidden-action fixtures
skip PermissionDenied or PolicyRestricted fixtures
skip idempotency conflict fixtures
skip unsupported version fixtures
create fixtures that imply AI may approve/send/submit
create fixtures that imply Human Review executes downstream action
create fixtures that treat Event references as commands
```

---

# 14. Acceptance Criteria

This task is complete only if:

```text
[ ] Fixture folder exists.
[ ] Reference fixtures exist.
[ ] Error fixtures exist.
[ ] Permission fixtures exist.
[ ] Policy fixtures exist.
[ ] AI Context fixtures exist.
[ ] Human Review fixtures exist.
[ ] Idempotency fixtures exist.
[ ] Event fixtures exist.
[ ] Version fixtures exist.
[ ] MVP API fixtures exist or are scaffolded.
[ ] MVP Workflow fixtures exist or are scaffolded.
[ ] Stub workflow fixtures exist or are explicitly deferred.
[ ] Fixture integrity tests exist.
[ ] Fixtures are deterministic.
[ ] Fixtures contain no production data.
[ ] Negative fixtures are present.
[ ] Unsupported version fixtures are present.
[ ] AI forbidden-action fixtures are present.
[ ] Idempotency conflict fixtures are present.
```

---

# 15. Final Summary Format

When Codex completes this task, reply with:

```text
Summary
- Fixture families created.
- Fixture file structure used.
- Which source specs were used.
- Which fixtures are complete.
- Which fixtures remain scaffolded.

Tests
- Commands run.
- Fixture integrity test result.

Boundary Confirmation
- No production data included.
- Database IDs appear only in rejection fixtures.
- PermissionDenied and PolicyRestricted fixtures exist.
- AI forbidden-action fixtures exist.
- Human Review gate fixtures exist.
- Idempotency replay/conflict fixtures exist.
- Event reference not command fixture exists.
- Unsupported version fixtures exist.

Deferred
- Any fixture families deferred and why.
- Next task recommended.
```

---

# 16. Revision Notes

| Version | Status | Notes |
|---------|--------|-------|
| 0.1.0 | Draft | Initial Codex TASK-002. Defines deterministic non-production fixture system, required fixture families, safety rules, validation requirements, tests, dependency on TASK-001 and acceptance criteria. |

---

## Publication Fixture Source

Publication canonical fixture source: `core-specs/contracts/fixtures/status-workflow/`.

Future implementation fixtures inherit from or are generated from publication fixtures. Publication fixtures are not production runtime fixtures.

**End of TASK-002 — Contract Fixture System**
