# Common Contract — Versioning

**Spec ID:** B02-CONTRACT-COMMON-VERSIONING  
**Spec Type:** Common Contract Specification  
**Contract Name:** Versioning Contract  
**Contract File:** core-specs/contracts/common/versioning.md  
**Contract Category:** Common  
**Related Owning Spec:** core-specs/contracts/README.md  
**Related Domain:** Cross-Domain Common Contract  
**Related Object Specs:** All Core object specifications  
**Related Service Specs:** All Core service specifications  
**Related API Specs:** All Core API specifications  
**Related Event Specs:** All Core event specifications  
**Related Agent Specs:** core-specs/agents/ai-agent-governance.md; core-specs/agents/agent-registry.md  
**Status:** Draft  
**Version:** 0.1.0  
**Contract Version:** v0.1.0  
**MVP Phase:** Cross-Phase Core Contract System  
**MVP Depth:** Must Implement  
**Owner:** MarkOrbit Publications Editorial Board  

---

# 1. Purpose

Versioning Contract defines the canonical versioning rules used across MarkOrbit Core contracts, APIs, services, events, agents, workflows and validation artifacts.

It standardizes how version fields are named, how compatibility is determined, how breaking changes are identified, how migrations are planned, how deprecations are handled and how Codex must implement version-aware behavior.

This contract governs:

```text
contract version naming
schema version naming
API version mapping
service contract versioning
event payload versioning
agent contract versioning
workflow contract versioning
compatibility rules
breaking change rules
deprecation rules
migration rules
version negotiation
safe error behavior
Codex implementation rules
```

Versioning Contract does not define product release marketing versions, UI release labels, database migration tooling or external package versioning by itself.

---

# 2. Contract Meaning

This contract means:

```text
a common Core agreement for declaring, comparing, validating and migrating Core contract versions.
```

This contract does not mean:

```text
product release number
Git tag only
database migration version only
API deployment version only
UI version label
informal changelog
temporary compatibility patch
```

Core rule:

```text
Versioning protects compatibility.
Owning specs define meaning.
Contracts define shape.
Migration must be explicit.
```

---

# 3. Contract Boundary

This contract is responsible for:

```text
version field naming
version format
contract version rules
schema version rules
API version rules
event payload version rules
agent contract version rules
workflow contract version rules
compatibility classification
breaking change detection
deprecation behavior
migration expectations
version errors
Codex implementation expectations
```

This contract is not responsible for:

```text
writing migration code by itself
choosing deployment strategy
publishing product release notes
choosing database migration framework
granting backward compatibility without owning spec approval
changing business meaning silently
```

---

# 4. Related Owning Spec

Owning spec:

```text
core-specs/contracts/README.md
```

Related common contracts:

```text
core-specs/contracts/common/errors.md
core-specs/contracts/common/references.md
core-specs/contracts/common/audit-context.md
core-specs/contracts/common/idempotency.md
```

Owning rule:

```text
Versioning Contract defines version compatibility discipline. It must not be used to silently change Core responsibility boundaries.
```

---

# 5. Related Core Objects

This contract may apply to all Core objects and cross-cutting systems.

Baseline object families:

```text
Foundation Objects
Professional Objects
Business Execution Objects
Collaboration Network Objects
Cross-Cutting Objects
```

Rules:

```text
- Object versioning must not change object meaning silently.
- Service contract versioning must not bypass object rules.
- API versioning must not weaken service or contract rules.
- Event versioning must preserve consumer safety.
```

---

# 6. Required References

Version context shape:

```yaml
version_context:
  contract_version: string
  schema_version: string | null
  api_version: string | null
  service_contract_version: string | null
  event_payload_version: string | null
  agent_contract_version: string | null
  workflow_contract_version: string | null
  compatibility_mode: string | null
  migration_reference_id: string | null
  deprecation_reference_id: string | null
  correlation_id: string | null
```

Rules:

```text
- contract_version is required for all contracts.
- schema_version is required where payload schema is serialized.
- api_version is required for public API contracts.
- event_payload_version is required for event payload contracts.
- agent_contract_version is required for agent runtime contracts.
- workflow_contract_version is required for executable workflow contracts.
```

---

# 7. Contract Shape

Canonical version context shape:

```yaml
version_context:
  contract_version: string
  schema_version: string | null
  api_version: string | null
  service_contract_version: string | null
  event_payload_version: string | null
  agent_contract_version: string | null
  workflow_contract_version: string | null
  compatibility:
    compatibility_mode: string
    backward_compatible: boolean
    forward_compatible: boolean | null
    breaking_change: boolean
  lifecycle:
    version_status: string
    deprecated_at: datetime | null
    removal_after: datetime | null
    migration_reference_id: string | null
  trace:
    correlation_id: string | null
```

Minimal version shape:

```yaml
version:
  contract_version: string
  schema_version: string | null
```

Rules:

```text
- Minimal shape may be used only where owning contract permits it.
- All public contracts must expose contract_version or equivalent version marker.
- Event payloads must include event_payload_version or schema_version.
- Version fields must be machine-readable.
```

---

# 8. Field Rules

| Field | Type | Required | Nullable | Rule |
|------|------|----------|----------|------|
| contract_version | string | Yes | No | Must use semantic version pattern. |
| schema_version | string | Contextual | Yes | Required for serialized payloads. |
| api_version | string | Contextual | Yes | Required for public API contracts. |
| service_contract_version | string | Contextual | Yes | Required where service contract is versioned separately. |
| event_payload_version | string | Contextual | Yes | Required for event payload contracts. |
| agent_contract_version | string | Contextual | Yes | Required for agent runtime contracts. |
| workflow_contract_version | string | Contextual | Yes | Required for workflow contracts. |
| compatibility_mode | string | Contextual | Yes | Must use controlled value. |
| backward_compatible | boolean | Contextual | No | True only where prior consumers are safe. |
| forward_compatible | boolean | No | Yes | Optional where forward compatibility is evaluated. |
| breaking_change | boolean | Contextual | No | True where compatibility is broken. |
| version_status | string | Contextual | No | Must use controlled value. |
| deprecated_at | datetime | No | Yes | Required when version_status is Deprecated. |
| removal_after | datetime | No | Yes | Required when removal is scheduled. |
| migration_reference_id | string | No | Yes | Required for breaking changes where migration exists. |

---

# 9. Controlled Values

## 9.1 version_status

```text
Draft
Active
Deprecated
SunsetScheduled
Removed
Archived
Unknown
```

## 9.2 compatibility_mode

```text
Strict
BackwardCompatible
ForwardCompatible
DualWrite
DualRead
AdapterRequired
MigrationRequired
Unsupported
Unknown
```

## 9.3 change_type

```text
Patch
Minor
Major
Breaking
Deprecation
Removal
Migration
DocumentationOnly
Unknown
```

## 9.4 version_error_code

```text
VersionMissing
VersionInvalid
VersionUnsupported
VersionDeprecated
VersionRemoved
VersionConflict
MigrationRequired
AdapterRequired
SchemaMismatch
Unknown
```

## 9.5 semantic version pattern

```text
vMAJOR.MINOR.PATCH
```

Examples:

```text
v0.1.0
v1.0.0
v1.2.3
```

Rules:

```text
- Prefix v is required for contract-facing version values.
- Major changes indicate breaking compatibility unless explicitly documented otherwise.
- Minor changes may add backward-compatible fields or values.
- Patch changes may clarify validation or fix non-breaking defects.
```

---

# 10. Compatibility Rules

Backward-compatible changes may include:

```text
adding optional nullable fields
adding controlled values where consumers are designed to tolerate unknown values
adding safe error codes where category remains stable
clarifying documentation without changing behavior
tightening wording without changing validation meaning
adding optional metadata fields
```

Breaking changes include:

```text
removing fields
renaming fields
changing field type
changing requiredness from optional to required
changing nullable to non-nullable
changing controlled value meaning
removing controlled values
changing default behavior
changing permission or policy semantics
changing event payload meaning
changing AI/human-review safety meaning
```

Rules:

```text
- Breaking changes require major version bump.
- Migration plan is required for breaking changes.
- Event payload breaking changes require consumer impact review.
- API breaking changes require deprecation period unless explicitly internal.
```

---

# 11. Contract Version Rules

Every contract file must declare:

```yaml
Version: 0.1.0
Contract Version: v0.1.0
```

Rules:

```text
- Version tracks document/spec artifact version.
- Contract Version tracks implementation-facing contract version.
- Contract Version must be machine-readable.
- Contract examples must include supported contract_version where payload shape is shown.
```

---

# 12. API Version Rules

API contracts must define:

```yaml
api_version: v1
contract_version: v0.1.0
schema_version: v0.1.0
```

Rules:

```text
- API version may be coarser than contract version.
- API version must not hide breaking contract changes.
- Public API breaking changes require deprecation or new API version.
- API responses must include version fields where clients need compatibility handling.
```

---

# 13. Service Version Rules

Service contracts must define:

```yaml
service_contract_version: v0.1.0
contract_version: v0.1.0
```

Rules:

```text
- Service version changes must preserve owning service responsibility.
- Service contract version changes must not silently weaken permission/policy checks.
- Service input/output versioning must be explicit.
- Internal adapter behavior must be documented where old callers are supported.
```

---

# 14. Event Payload Version Rules

Event payload contracts must define:

```yaml
event_payload_version: v0.1.0
schema_version: v0.1.0
event_type: string
```

Rules:

```text
- Event consumers must be protected from unsafe breaking changes.
- Event payload fields must not be repurposed.
- Event type meaning must not change without new version or new event type.
- New optional event payload fields are allowed if consumers tolerate unknown fields.
- Removed/renamed event fields are breaking.
```

---

# 15. Agent and Workflow Version Rules

Agent contracts must define:

```yaml
agent_contract_version: v0.1.0
agent_registry_key: string
```

Workflow contracts must define:

```yaml
workflow_contract_version: v0.1.0
workflow_contract_reference_id: string
```

Rules:

```text
- Agent contract version must not silently expand capabilities.
- Workflow contract version must not silently change execution steps.
- AI Agent output must preserve contract version where used downstream.
- Workflow application must record workflow_contract_version used.
```

---

# 16. Permission, Policy and Human Review Rules

Version changes must preserve governance.

Rules:

```text
- Permission requirements cannot be weakened by minor/patch version changes.
- Policy restrictions cannot be bypassed by version negotiation.
- Human review requirement meaning cannot be changed without version bump.
- Deprecated versions may still require current Permission/Policy checks.
- Replay or migration must not expose data under old visibility rules if current policy forbids it.
```

---

# 17. Error Rules

Controlled version errors:

```text
VersionMissing
VersionInvalid
VersionUnsupported
VersionDeprecated
VersionRemoved
VersionConflict
MigrationRequired
AdapterRequired
SchemaMismatch
```

Safe error shape:

```yaml
error:
  code: string
  category: Version
  message: string
  safe_detail: string | null
  correlation_id: string | null
  retryable: boolean
```

Rules:

```text
- Errors must follow Error Contract.
- Version errors must not expose internal adapter details.
- Deprecated version warnings must be safe.
- Unsupported versions must fail closed.
```

---

# 18. Migration and Deprecation Rules

Migration plan must define:

```text
source_version
target_version
affected fields
breaking changes
data transformation rules
consumer impact
event consumer impact
permission/policy impact
human review impact
rollback behavior
acceptance tests
```

Deprecation must define:

```text
deprecated_at
removal_after
replacement_version
safe warning behavior
support window
```

Rules:

```text
- Breaking changes require migration plan.
- Deprecated versions must remain safe.
- Removed versions must fail with VersionRemoved.
- Migration must not silently change professional truth.
```

---

# 19. Codex Implementation Notes

Codex must:

```text
cite this Versioning Contract before implementing versioned contracts
validate contract_version
validate schema_version where required
reject unsupported versions
implement backward-compatible readers where specified
preserve event_payload_version in events
preserve agent_contract_version in agent outputs
preserve workflow_contract_version in workflow applications
return Error Contract shape for version errors
write tests for missing version
write tests for unsupported version
write tests for deprecated version warning
write tests for removed version rejection
write tests for schema mismatch
write tests for backward-compatible optional fields
write tests for breaking change migration where applicable
```

Codex must not:

```text
silently accept unsupported versions
silently reinterpret fields
remove fields without version change
change controlled value meaning without version change
bypass Permission or Policy through version fallback
drop version fields in serialized payloads
treat product release version as contract version
```

---

# 20. Acceptance Criteria

This Versioning Contract is accepted only if:

```text
[ ] It defines versioning purpose.
[ ] It defines versioning meaning.
[ ] It defines versioning boundary.
[ ] It cites related owning spec and common contracts.
[ ] It defines related Core objects.
[ ] It defines required references.
[ ] It defines canonical version context shape.
[ ] It defines minimal version shape.
[ ] It defines field rules.
[ ] It defines controlled values.
[ ] It defines compatibility rules.
[ ] It defines contract version rules.
[ ] It defines API version rules.
[ ] It defines service version rules.
[ ] It defines event payload version rules.
[ ] It defines agent and workflow version rules.
[ ] It defines permission, policy and human-review rules.
[ ] It defines error rules.
[ ] It defines migration and deprecation rules.
[ ] It defines Codex implementation notes.
```

---

# 21. Revision Notes

| Version | Status | Notes |
|---------|--------|-------|
| 0.1.0 | Draft | Initial common Versioning Contract. Defines version fields, semantic versioning, compatibility, API/service/event/agent/workflow version rules, governance preservation, migration/deprecation and Codex implementation rules. |

---

**End of Common Contract**
