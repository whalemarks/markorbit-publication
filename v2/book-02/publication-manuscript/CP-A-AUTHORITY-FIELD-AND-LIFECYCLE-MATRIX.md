# CP-A — Authority Field and Lifecycle Matrix

## 1. Purpose

This matrix compares the proposed authority-related records against frozen Book 02 fields and lifecycles.

It distinguishes:

```text
already represented
representable by profile or composition
missing but potentially Product/Execution-owned
candidate shared semantic
externally authoritative and reference-only
```

## 2. Field-level comparison

| Proposed field | Frozen source | Current coverage | Research disposition |
|---|---|---|---|
| subject reference | Identity; Permission | direct | retain frozen reference |
| subject type | Identity.identity_type; Permission.subject_type | direct, but vocabularies differ | map without merging controlled values |
| Capability reference | Permission.capability_reference_id | direct/partial | retain reference |
| evidence basis | Evidence; Document; Human Review.source references | composable | Capability Evidence profile |
| assessor identity | Human Review reviewer; Identity | composable | profile field |
| assessor organization | Human Review reviewer organization | direct in review shape | profile field |
| certification scheme | no exact frozen field | missing | candidate profile identifier |
| certification scheme version | Versioning plus missing scheme identifier | partial | profile field |
| issue date | timestamps | composable | profile field |
| expiry date | Human Review expires_at; generic timestamps | partial | profile field or candidate lifecycle |
| suspension / revocation | Permission status; Identity status; no certification-specific lifecycle | partial but semantically different | candidate lifecycle if Certification is shared |
| issuing professional authority | external Organization/Identity reference | reference possible | external reference only |
| credential identifier | source_reference / external reference | composable | Qualification profile |
| credential jurisdiction | Policy scope Jurisdiction; external reference | composable | Qualification profile |
| credential current status | no exact qualification status contract | missing | candidate external-reference profile |
| last verification time | audit/version timestamps | composable | Qualification profile |
| restriction text/reference | Policy and metadata | partial | governed reference, not free-form authority |
| production action scope | Permission.action | direct | specialized Permission profile |
| production resource scope | Permission.resource_type/resource_id | direct | specialized Permission profile |
| production Product scope | Permission.scope_type=Product | direct | specialized Permission profile |
| production Workflow scope | Permission.scope_type=Workflow | direct | specialized Permission profile |
| production Service/API scope | Permission scope values | direct | specialized Permission profile |
| production data scope | Permission.scope_type=DataAccess | direct | specialized Permission profile |
| organization scope | Permission.organization_id | direct | specialized Permission profile |
| Policy constraints | Permission.policy_reference_id; Policy | direct | retain frozen mechanism |
| supervision requirement | Policy review/approval rules | composable | Policy profile |
| M-mode | no frozen controlled value | missing | Book 03/Product profile, not Core value yet |
| R-tier | no frozen controlled value | missing | Book 03/Product profile, not Core value yet |
| Tool access ceiling | Permission action/resource or Capability reference | composable | profile before new field |
| implementation/model version | Versioning; AI Context | composable | required for AI/system profile |
| valid from / valid until | Permission status/timestamps; no explicit interval fields in Object | partial | candidate profile fields |
| assignment target | Task assignee/reference fields | direct for Task | exact work binding exists at Task level |
| assignment acceptance | no exact Task field/lifecycle | missing | CP-B decision |
| conflict clearance | Policy decision / Human Review | composable | runtime decision reference |
| capacity check | no durable Core field required | Execution runtime | Book 03 Eligibility result |
| current Eligibility result | Permission/Policy/Human Review decision references | composable | Book 03 decision profile |
| appointment source | source/reference plus Document/Evidence | composable | Professional Authority profile |
| Matter scope | Task.matter_reference; Permission object/resource scope | composable | Professional Authority profile |
| authority action type | Permission.action | direct as platform authorization vocabulary | external authority semantics require controlled mapping |
| authority to sign / submit / advise | Permission actions plus external appointment | partial | F3 external authority reference |
| authority verification source | Evidence/Document/source_reference | composable | required profile field |
| authority verification time | timestamps | composable | required profile field |
| authority expiry / revocation | no professional-authority lifecycle | missing | F3/F4 analysis |

## 3. Controlled-value comparison

### 3.1 Frozen Identity status

```text
Draft
Active
Suspended
Archived
Merged
DeletedReferenceOnly
```

This status belongs to the Identity record. It must not be reused as credential or professional-authority status merely because some labels overlap.

### 3.2 Frozen Permission effect

```text
Allow
Deny
ReviewRequired
```

Permission effect can support Production Authorization decisions.

It does not express:

```text
Candidate
Restricted
Expired
Revoked
Superseded
```

as a certification or professional-authority lifecycle.

### 3.3 Frozen Policy effect

```text
Allow
Deny
ReviewRequired
ApprovalRequired
AuditRequired
Escalate
```

Policy effects are decisions, not credential states.

### 3.4 Candidate lifecycle values

The v2 manuscript proposes possible states:

```text
Candidate
Active
Restricted
Suspended
Expired
Revoked
Superseded
```

These must not be added as universal Core status values. Each proposed record must prove that it needs a distinct lifecycle and define owning mutation authority.

## 4. Lifecycle comparisons

### 4.1 Capability Evidence

Recommended lifecycle:

```text
recorded
→ reviewed
→ accepted / rejected for declared purpose
→ superseded or stale
```

This can likely be represented through Evidence and Human Review rather than a new Core lifecycle.

### 4.2 Certification

Potential lifecycle:

```text
Candidate
→ Active
→ Restricted / Suspended
→ Expired / Revoked / Superseded
```

Open questions:

- Who owns transitions?
- Is restriction a state or a Policy condition?
- Does expiry occur automatically?
- Does supersession preserve the old certification as Evidence?
- Does revocation require Human Review and Event trace?

### 4.3 Qualification reference

Potential lifecycle should mirror verified external state rather than invent a platform state:

```text
Unverified
VerifiedCurrent
VerifiedRestricted
VerifiedSuspended
VerifiedExpired
VerificationStale
SourceUnavailable
```

These labels are research candidates only. The platform record should distinguish:

```text
external credential state
from
platform verification state
```

### 4.4 Production Authorization

Recommended first model:

```text
Permission Grant
+ Policy constraints
+ Capability and version references
+ effective interval profile
```

Potential transitions may reuse Permission status where possible. A separate lifecycle should only be introduced if active Assignment consequences cannot be expressed through Permission revocation and Policy decisions.

### 4.5 Eligibility

Eligibility should normally be a decision envelope:

```text
Eligible
Ineligible
ReviewRequired
Unknown
```

with reason codes and expiry.

It should be recalculated, not treated as a permanent actor status.

### 4.6 Professional Authority

Potential lifecycle needs two independent tracks:

```text
External authority state
and
platform verification / reliance state
```

A platform must not mutate the external state. It may update its verified representation when source evidence changes.

## 5. Ownership comparison

| Record | Candidate owner | Ownership rule |
|---|---|---|
| Capability Evidence | Evidence Service | owns evidence record, not Capability truth |
| Certification | candidate Certification-owning Service or Evidence-backed profile owner | must not be Permission Service by convenience |
| Qualification reference | Identity or a dedicated credential/reference owner | represents external source, does not issue credential |
| Production Authorization | Permission Service with Policy Service context, if profile approach succeeds | authorizes platform production scope only |
| Eligibility decision | Book 03 Execution | evaluates current exact-work context |
| Assignment | Task Service or candidate Assignment-owning Service | CP-B must decide |
| Professional Authority reference | candidate dedicated reference owner or Matter-linked profile owner | represents externally grounded authority; Owning Service does not create it |

## 6. Negative conformance requirements

Future fixtures must reject:

1. Identity `Active` treated as Permission `Allow`.
2. Certification treated as government or professional qualification.
3. Qualification record without issuing authority or source.
4. Production Authorization without subject, action and scope.
5. AI Production Authorization without implementation/model version.
6. Eligibility result without target work and evaluation time.
7. Assignment created merely from Eligibility.
8. Professional Authority inferred from Provider listing.
9. Human Review completion treated as automatic downstream execution.
10. Revoked or stale authority used without re-evaluation.
11. Credential upload treated as verified current qualification.
12. Permission profile granting an externally reserved professional right.

## 7. Positive conformance requirements

Future fixtures should demonstrate:

- an Evidence-backed Capability assessment;
- a platform Certification clearly separated from external qualification;
- an externally sourced qualification reference with verification timestamp;
- a Production Authorization represented through Permission and Policy;
- a time-limited Eligibility result for an exact Task or Work Package;
- a separate Assignment record or Task assignment;
- a Professional Authority reference tied to jurisdiction, Matter and source;
- suspension that blocks new work without erasing historical Evidence;
- AI/system production permission that still requires human professional authority for reserved action.

## 8. Matrix conclusion

```text
Fields directly covered by frozen contracts: substantial
Fields composable through profiles: substantial
Fields requiring new universal root Object: not proven
Production Authorization as Permission profile: plausible
Professional Qualification as external reference profile: plausible
Professional Authority as complete shared contract: unresolved
Universal authority lifecycle: rejected
Immediate controlled-value changes: not justified
```

This matrix supports narrow, separated proposals rather than one combined Authority schema.