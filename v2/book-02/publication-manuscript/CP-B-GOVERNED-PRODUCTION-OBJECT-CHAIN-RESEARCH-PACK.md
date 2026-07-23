# CP-B — Governed Production Object Chain Research Pack

## 1. Research purpose

This pack evaluates the v2 production chain:

```text
Work Package
→ Assignment
→ Contribution
→ Review
→ Outcome
```

against the frozen Book 02 contracts for Task, Workflow Contract, Document, Evidence, Event, Permission, Policy and Human Review.

The central question is whether the chain requires new shared Core Objects or can be represented through frozen contracts, profiles and Book 03 execution records.

This pack does not activate any candidate or modify the frozen Task model.

## 2. Frozen production model

The frozen baseline already provides:

```text
Matter — execution container
Workflow Contract — governed execution structure
Task — actionable work unit
Document — governed artifact
Evidence — proof and support record
Human Review — review requirement and decision trace
Permission — action authorization
Policy — contextual constraint
Event — completed-fact trace
Owning Service — behavior and state mutation
```

Frozen Task means:

```text
a Core-recognized actionable work unit with defined scope,
assignee or responsibility reference, status, dependency,
workflow context and execution trace.
```

Task already contains:

- type, title and description references;
- status and priority;
- Matter and Order references;
- Workflow Contract and workflow-state references;
- assignee type and assignee reference;
- responsibility reference;
- dependencies and due time;
- Document, Evidence and Communication references;
- AI suggestion and source references;
- audit metadata.

Its controlled task types already include ReviewTask, ApprovalTask, DocumentReview, EvidenceReview, FilingPreparation, CommunicationDraft and CommunicationReview.

## 3. Candidate chain purpose

The v2 chain tries to make several distinctions explicit:

```text
Work Package
≠ Task list item only

Assignment
≠ general eligibility

Contribution
≠ accepted result

Review
≠ approval

Outcome
≠ formal-state mutation
```

The chain is valuable only if it preserves information not already carried by Task, Workflow, Document, Evidence and Human Review.

## 4. Work Package analysis

### 4.1 Proposed meaning

Work Package is intended as a bounded production contract describing what must be produced, under which conditions, by which deadline, with which data and review requirements.

Potential fields include:

```text
purpose and expected deliverable
scope and exclusions
input references
data classification
Capability requirement
allowed execution mode
risk/review tier
acceptance criteria
deadline
compensation or settlement reference
correction and recovery rules
parent Matter / Order / Workflow
```

### 4.2 Frozen overlap

| Work Package concern | Frozen coverage |
|---|---|
| concrete work | Task |
| parent business context | Matter and Order |
| governed process | Workflow Contract |
| assignee and responsibility | Task |
| deadline | Task.due_at |
| dependencies | Task dependencies |
| inputs | Document, Evidence and Communication references |
| permission and policy | Permission and Policy contexts |
| review | Task types and Human Review |
| audit | Event and audit context |
| expected deliverable | Task description plus Document/Evidence references, but not strongly typed |
| acceptance criteria | Human Review and owning-service rules, but not explicit on Task |
| correction / resubmission | possible through Task and Workflow, but no shared envelope |
| compensation | Order or Product-local settlement references, not Task semantics |

### 4.3 Preliminary decision

A universal new Work Package Object is not yet justified.

The strongest near-term option is:

```text
F2 governed Task profile
```

A profile may add a typed scope and deliverable envelope without changing Task identity or status.

A new F3 contract becomes justified only if:

- one Work Package needs multiple Tasks and Contributors;
- acceptance applies to a combined deliverable rather than individual Tasks;
- Assignment, compensation and correction attach to the package rather than each Task;
- several Products require the same lifecycle;
- Book 03 needs a stable package identifier independent of execution Tasks.

## 5. Assignment analysis

### 5.1 Frozen overlap

Frozen Task already has `assignee_type`, `assignee_reference_id` and `responsibility_reference_id`.

Permission and Policy can authorize and constrain the assignment. Human Review can record an approval or review requirement.

### 5.2 Missing lifecycle

Task fields do not explicitly preserve:

```text
offer
acceptance
decline
expiry
withdrawal
suspension
revocation
replacement
commercial terms acceptance
cross-Workplace acceptance
```

The frozen trademark Assignment Workflow is unrelated to generic work allocation and must not be reused.

### 5.3 Preliminary decision

Two models remain viable:

**Model A — Task assignment profile**

Use Task assignee fields plus a versioned Assignment decision/reference envelope.

Suitable when assignment is internal, unilateral and simple.

**Model B — Shared Assignment contract**

Create a distinct record when acceptance, expiry, revocation, cross-organization participation or commercial terms must be preserved independently.

Preliminary classification:

```text
F2 for internal assignment
F3 for cross-Workplace or accepted bilateral assignment
```

No change to frozen Task fields should occur before both models are tested.

## 6. Contribution analysis

### 6.1 Proposed meaning

Contribution is an attributable submitted result produced against assigned work.

It may point to:

- Document;
- Evidence;
- structured data;
- draft Communication;
- analysis or recommendation;
- code or generated artifact;
- external Provider return.

### 6.2 Frozen overlap

Document and Evidence already own governed artifacts and proof records. Event records submission facts. Task can link the artifact to work. Human Review can review it.

### 6.3 Gap

No single frozen shared record explicitly captures:

```text
contributor
Assignment or Task basis
submission version
submitted artifact references
declared completion scope
limitations
submission timestamp
supersession relation
review status
```

### 6.4 Preliminary decision

Contribution should first be tested as:

```text
F2 submission profile over Document / Evidence / Event
```

A root Object is justified only if non-document contributions and multi-artifact submissions require one stable cross-Product identity.

## 7. Review analysis

The frozen Human Review Contract is already substantial. It contains:

- review requirement;
- request reference;
- reviewer User and Organization references;
- scope, status and decision;
- target and source references;
- AI-assistance context;
- Permission and Policy decision references;
- timestamps and expiry;
- Event trace.

It expressly preserves:

```text
Review
≠ downstream execution
≠ permission grant
≠ professional judgment by itself
```

Therefore:

```text
new generic Review Object: not justified
```

The frozen Human Review Contract should remain the primary review envelope. Domain-specific reviews may profile it.

## 8. Outcome analysis

### 8.1 Proposed meaning

Outcome is an accepted result for a declared purpose after Review.

It should preserve:

```text
accepted Contribution or source references
acceptance purpose
review and decision references
accepted scope and exclusions
accepting actor or service
accepted version
correction state
formalization or downstream handoff references
```

### 8.2 Frozen overlap

- Human Review records review decision.
- Task status may become Completed.
- Evidence can preserve accepted support.
- Owning Services update parent state.
- Events record completed facts.
- Workflow result envelopes describe decisions and performed results.

### 8.3 Critical distinction

```text
Contribution accepted for a purpose
≠ Task completed automatically
≠ Matter resolved
≠ Trademark or official state changed
```

### 8.4 Preliminary decision

Outcome is the strongest CP-B candidate for a new shared contract because acceptance may need to survive independently of Task status and formal-state mutation.

However, an Outcome may also be represented as:

```text
Human Review decision
+ Evidence reference
+ Event
+ owning-service state result
```

Preliminary classification:

```text
F2 result/acceptance profile first
F3 if cross-Product continuity requires stable Outcome identity
```

## 9. Chain ownership model

A safe ownership split is:

| Record | Owner |
|---|---|
| Matter / Order | existing Owning Services |
| Workflow Contract | Workflow Contract Service |
| Task | Task Service |
| Work Package profile | Task or Workflow layer profile; no new owner yet |
| Assignment | Task Service for simple profile, candidate Assignment Service for accepted bilateral record |
| Contribution | Document/Evidence owner plus submission profile owner |
| Human Review | frozen common contract; relying Owning Service decides sufficiency |
| Outcome | relying Owning Service or candidate Outcome Service; must not mutate parent state automatically |
| Event | Event Service |
| formal state | existing parent Owning Service |
| execution runtime | Book 03 |

## 10. Rejected alternatives

### Alternative A — Rename Task to Work Package

Rejected. Frozen Task is a specific canonical Object with controlled values and status ownership. Renaming it would be an F4 change and would erase the possibility that a Work Package contains several Tasks.

### Alternative B — Treat Task `Completed` as Outcome

Rejected. Completion of work does not establish acceptance for every purpose or change parent formal state.

### Alternative C — Treat Document as Contribution

Rejected as a universal rule. A Document may be a submitted artifact, but Contribution also needs contributor, work basis and submission version. Some Contributions may contain several artifacts or no Document.

### Alternative D — Create a new Review Object

Rejected because the frozen Human Review Contract already provides the canonical cross-domain review shape.

### Alternative E — Make Workflow Contract own all chain state

Rejected. Workflow Contracts constrain and coordinate; they do not own Task, Document, Evidence, Outcome or parent formal state.

### Alternative F — Use the frozen trademark Assignment Workflow as generic Assignment

Rejected. That workflow governs ownership-change preparation and explicitly does not certify authority or perform official transfer.

## 11. Proposed minimum profiles

### 11.1 Work Package profile

```yaml
work_package_profile:
  profile_version: string
  work_package_reference_id: string
  parent_matter_reference_id: string | null
  parent_order_reference_id: string | null
  workflow_contract_reference_id: string
  task_reference_ids: list[string]
  purpose: string
  scope_reference: string
  expected_deliverable_types: list[string]
  input_reference_ids: list[string]
  acceptance_criteria_reference_id: string
  required_capability_reference_ids: list[string]
  permission_policy_context_reference_ids: list[string]
  review_requirement_reference_id: string | null
  due_at: datetime | null
```

This is a research shape, not a canonical contract.

### 11.2 Assignment profile

```yaml
assignment_profile:
  assignment_reference_id: string
  target_work_reference_id: string
  assignee_identity_reference_id: string
  assignee_role: string | null
  permission_decision_reference_id: string
  policy_decision_reference_id: string
  eligibility_decision_reference_id: string | null
  status: string
  offered_at: datetime | null
  accepted_at: datetime | null
  expires_at: datetime | null
  revoked_at: datetime | null
```

### 11.3 Contribution profile

```yaml
contribution_profile:
  contribution_reference_id: string
  target_work_reference_id: string
  assignment_reference_id: string | null
  contributor_identity_reference_id: string
  artifact_reference_ids: list[string]
  evidence_reference_ids: list[string]
  submitted_version: string
  submitted_at: datetime
  supersedes_contribution_reference_id: string | null
```

### 11.4 Outcome profile

```yaml
outcome_profile:
  outcome_reference_id: string
  target_work_reference_id: string
  accepted_contribution_reference_ids: list[string]
  acceptance_purpose: string
  human_review_reference_id: string
  accepted_by_identity_reference_id: string
  accepted_by_service_reference_id: string | null
  accepted_scope_reference: string
  accepted_version: string
  accepted_at: datetime
  formal_state_change_reference_id: string | null
```

These profiles exist only to test semantic sufficiency.

## 12. Negative fixture requirements

Future tests must reject:

1. Work Package profile without Workflow or parent context where required.
2. Task renamed or silently migrated to Work Package.
3. Assignment created without target work and assignee.
4. Eligibility treated as Assignment.
5. Assignment treated as professional authority.
6. Contribution without contributor and submitted version.
7. Document presence treated as submission acceptance.
8. Review decision treated as downstream Apply.
9. Outcome created without review or explicit acceptance authority.
10. Outcome treated as automatic parent-state mutation.
11. Task Completed treated as official success.
12. Provider Return treated as accepted Outcome without reconciliation.

## 13. Positive fixture requirements

Future tests should show:

- a single Task represented without a Work Package profile;
- a Work Package profile containing several Tasks;
- a simple internal Task assignment;
- a bilateral Assignment requiring acceptance;
- a Contribution containing multiple Documents and Evidence records;
- a superseding Contribution after correction;
- Human Review rejecting one Contribution and accepting another;
- an accepted Outcome that does not alter formal state;
- an Owning Service later applying the accepted Outcome;
- an Event trace across the complete chain.

## 14. Recommendation

```text
Work Package: F2 Task/Workflow profile research; no root Object proposal yet
Assignment: split simple Task profile from F3 bilateral/cross-Workplace contract
Contribution: F2 submission profile over Document/Evidence/Event
Review: retain frozen Human Review Contract
Outcome: F2 acceptance profile; consider F3 only after consumer proof
```

The recommended next engineering proof belongs in Book 03 or a controlled fixture workspace, not in the public `@markorbit/core` export map.

## 15. Research verdict

```text
Frozen production chain mapped: YES
Task can be silently replaced: NO
New Review Object required: NO
Work Package root Object proven necessary: NO
Assignment shared contract potentially necessary: YES, for accepted bilateral/cross-Workplace cases
Contribution root Object proven necessary: NO
Outcome shared identity potentially necessary: YES, subject to consumer proof
Immediate Book 02 Change Proposal opening: NOT YET
Prototype profiles authorized as canonical contracts: NO
```