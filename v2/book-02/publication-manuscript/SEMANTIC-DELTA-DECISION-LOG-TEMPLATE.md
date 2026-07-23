# Book 02 — Semantic Delta Decision Log Template

## 1. Purpose

This template records the exact semantic difference between a downstream research result and the frozen Book 02 baseline.

It prevents architecture prose, prototype code or repeated local use from becoming an undocumented Core change.

## 2. Delta classes

```text
D0 — no semantic delta; implementation or documentation only
D1 — consumer-local profile or naming difference
D2 — shared profile over frozen contracts
D3 — candidate shared semantic without frozen replacement
D4 — frozen semantic, lifecycle, authority or ownership change
```

Interpretation:

- `D0` requires no Book 02 Change Proposal;
- `D1` remains consumer-local;
- `D2` may be published as a noncanonical profile;
- `D3` may advance to pre-proposal research after evidence gates;
- `D4` requires the formal frozen Change Proposal process before implementation.

## 3. Required decision record

```yaml
semantic_delta:
  decision_id: string
  candidate_name: string
  research_task_ids: [string]
  consumer_repositories: [string]
  evidence_prs: [string]
  evidence_head_shas: [string]
  frozen_baseline_id: B02-BASELINE-V0.1
  frozen_sources: [string]
  delta_class: D0 | D1 | D2 | D3 | D4
  decision: string
  decided_by: [string]
  decided_at: string
  status: proposed | accepted | rejected | superseded
```

## 4. Frozen comparison

For every candidate, record:

### Frozen concept

- Domain;
- Object;
- Service;
- API;
- Workflow or Workflow Contract;
- Status Contract;
- Permission, Policy or Human Review rule;
- Event and audit behavior.

### Proposed concept

- identifier;
- purpose;
- required fields;
- controlled values;
- lifecycle;
- Owning Service;
- mutation authority;
- consumers;
- correction and versioning;
- compatibility and migration.

### Exact delta

Use one or more of:

```text
field added
field meaning changed
field split
field merged
controlled value added
lifecycle added
transition changed
owner changed
mutation authority changed
review requirement changed
API payload changed
event meaning changed
new stable identity introduced
no frozen change; profile only
```

## 5. Alternative analysis

Every D2–D4 decision must document rejected alternatives:

```text
F0 — already covered
F1 — composition
F2 — profile
F3 — candidate shared addition
F4 — frozen change
```

For each rejected alternative, state:

- why it was tested;
- which evidence disproved sufficiency;
- which consumers required more;
- whether the rejection is reversible.

## 6. Ownership decision

```yaml
ownership:
  semantic_owner: string
  record_owner: string
  mutation_owner: string
  formal_state_owner: string
  physical_custodian: string | null
  professional_authority_source: string | null
  execution_runtime_owner: string | null
```

Required locks:

```text
Semantic Owner
≠ Record Owner by default

Record Owner
≠ Professional Authority

Execution Runtime
≠ Formal-state Owner
```

## 7. Lifecycle decision

Record:

- initial state;
- allowed transitions;
- prohibited transitions;
- terminal states;
- expiry;
- suspension and revocation;
- correction and supersession;
- effect on active Tasks, Assignments or Outcomes;
- Event evidence for transitions.

A candidate lifecycle must not reuse a frozen label with a different meaning without explicit compatibility analysis.

## 8. Consumer comparison

For each consumer, classify every field:

```text
SHARED_SAME_MEANING
SHARED_DIFFERENT_CONSTRAINT
CONSUMER_LOCAL
BOOK_03_RUNTIME_ONLY
EXTERNAL_AUTHORITY_REFERENCE
UNUSED
CONFLICTING
```

A field is not shared merely because two consumers use the same word.

## 9. Compatibility decision

```yaml
compatibility:
  backward_compatible: true | false | unknown
  forward_compatible: true | false | unknown
  frozen_consumers_affected: [string]
  public_exports_affected: [string]
  data_migration_required: true | false | unknown
  active_work_migration_required: true | false | unknown
  rollback_possible: true | false | unknown
```

```text
Additive schema change
≠ semantically compatible by default
```

## 10. Fixture evidence

List:

- positive fixtures;
- negative fixtures;
- boundary assertions;
- exact-head CI evidence;
- consumer-proof scores;
- Unknown behavior;
- rejected illegal transitions;
- source and version references.

## 11. Authority review

Where relevant, record separate review conclusions for:

- Permission;
- Policy;
- Human Review;
- Assignment;
- Professional Authority;
- customer instruction;
- external protected action;
- payment or custody;
- privacy and data rights.

No combined `approved` field is sufficient.

## 12. Decision outcomes

Allowed outcomes:

```text
NO_DELTA
RETAIN_CONSUMER_LOCAL
RETAIN_AS_NONCANONICAL_PROFILE
RETAIN_IN_BOOK_03_RUNTIME
MORE_EVIDENCE_REQUIRED
ADVANCE_TO_PRE_PROPOSAL
OPEN_FORMAL_CHANGE_PROPOSAL
REJECT_CANDIDATE
SUPERSEDE_PRIOR_DECISION
```

## 13. Example shell

```markdown
# SDL-<ID> — <Candidate>

## Evidence

## Frozen sources

## Proposed meaning

## Exact delta

## Alternative analysis

## Ownership

## Lifecycle

## Consumer comparison

## Compatibility

## Authority review

## Decision

## Non-goals

## Follow-up
```

## 14. Template verdict

```text
Semantic delta recording: DEFINED
Unrecorded semantic promotion allowed: NO
Repeated local implementation sufficient for Core change: NO
Formal proposal still required for D4: YES
```