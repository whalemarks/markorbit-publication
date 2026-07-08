# TASK-009 — Agent Boundary Tests

**Task ID:** TASK-009  
**Task Type:** Codex Implementation Task  
**Task File:** codex-tasks/TASK-009-agent-boundary-tests.md  
**Task Title:** Agent Boundary Tests  
**Related Book:** Book 02 — MarkOrbit Core Specification  
**Related Task Index:** core-specs/codex/CODEX-TASK-INDEX.md  
**Related Previous Tasks:** codex-tasks/TASK-001-common-contract-foundation.md; codex-tasks/TASK-002-contract-fixture-system.md; codex-tasks/TASK-003-common-contract-tests.md; codex-tasks/TASK-004-permission-policy-hooks.md; codex-tasks/TASK-005-idempotency-event-trace.md; codex-tasks/TASK-006-error-versioning-validation.md; codex-tasks/TASK-007-api-validator-scaffold.md; codex-tasks/TASK-008-workflow-validator-scaffold.md  
**Related Developer Guide:** core-specs/DEVELOPER_START_HERE.md  
**Related Traceability:** core-specs/TRACEABILITY.md  
**Related MVP Cut:** core-specs/implementation/mvp-cut-v0.1.md  
**Related Depth Matrix:** core-specs/implementation/implementation-depth-matrix.md  
**Related Agent Specs:** core-specs/agents/  
**Related Test Contract:** core-specs/contracts/tests/agent-boundary-tests.md  
**Status:** Draft  
**Version:** 0.1.0  
**MVP Category:** Must Build Now  
**Implementation Depth:** Agent Boundary Level 1/2; Forbidden Action Enforcement Level 3  
**Owner:** MarkOrbit Publications Editorial Board  

---

# 1. Purpose

This task implements Agent Boundary Tests for MarkOrbit Core MVP.

It ensures that AI agents may assist professional execution but must not replace professional accountability, mutate protected state or execute protected actions.

The goal is to test and lock this rule:

```text
AI may prepare.
AI may not decide.
AI may not execute protected actions.
AI may not define professional truth.
```

This task is required before the MVP execution spine can safely use any AI-assisted behavior.

---

# 2. Core Lock

```text
AI enhances professionals.
AI does not define professional truth.
Agent capability does not equal Permission.
Agent identity does not equal Permission.
Agent output does not equal Human Review.
Agents may summarize, draft, classify, compare, suggest and identify gaps.
Agents must not approve, send, select, submit, certify, complete, mutate protected state or emit Events.
AI Context bounds AI-assisted output.
Permission and Policy govern AI-assisted behavior.
Human Review gates protected professional or external-facing actions.
Codex tests Agent boundaries.
Codex does not create autonomous professional execution.
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
codex-tasks/TASK-002-contract-fixture-system.md
codex-tasks/TASK-003-common-contract-tests.md
codex-tasks/TASK-004-permission-policy-hooks.md
codex-tasks/TASK-005-idempotency-event-trace.md
codex-tasks/TASK-006-error-versioning-validation.md
codex-tasks/TASK-007-api-validator-scaffold.md
codex-tasks/TASK-008-workflow-validator-scaffold.md
core-specs/agents/ai-agent-governance.md
core-specs/agents/agent-registry.md
core-specs/agents/knowledge-agent.md
core-specs/agents/task-agent.md
core-specs/agents/communication-agent.md
core-specs/agents/workflow-agent.md
core-specs/agents/routing-agent.md
core-specs/agents/audit-agent.md
core-specs/contracts/common/ai-context.md
core-specs/contracts/common/human-review.md
core-specs/contracts/common/permission-context.md
core-specs/contracts/common/policy-context.md
core-specs/contracts/common/errors.md
core-specs/contracts/tests/agent-boundary-tests.md
```

Codex must also consult:

```text
core-specs/contracts/tests/permission-policy-tests.md
core-specs/contracts/tests/workflow-contract-tests.md
core-specs/contracts/tests/idempotency-event-tests.md
core-specs/contracts/tests/error-versioning-tests.md
```

---

# 4. Scope

This task covers tests and boundary scaffolds for:

```text
AI Context validation
Agent identity validation
Agent capability validation
allowed agent action validation
forbidden agent action validation
Permission / Policy interaction with AI-assisted behavior
Human Review preservation
AI output redaction behavior
AI policy omission disclosure
Agent no-state-mutation rule
Agent no-direct-event-emission rule
Agent no-task-completion rule
Agent no-communication-send rule
Agent no-provider-final-selection rule
Agent no-official-submission rule
Agent no-professional-certification rule
safe AI error behavior
```

This task may add lightweight boundary helper functions if they do not already exist.

---

# 5. Out of Scope

This task must not implement:

```text
full agent runtime
multi-agent orchestration engine
autonomous workflow execution
AI official filing integration
AI provider auto-selection
AI professional legal conclusion engine
AI deadline certification
AI evidence sufficiency certification
AI communication sending
AI task completion
external model provider integration
prompt management platform
```

This task tests boundaries. It does not build AI product automation.

---

# 6. Implementation Depth

## 6.1 Agent Boundary Depth

MVP Agent boundary depth:

```text
Level 1/2 for capability registry and AI Context validation.
Level 3 for forbidden action enforcement tests.
```

Required enforcement:

```text
approve = blocked
send = blocked
select = blocked
submit = blocked
certify = blocked
complete = blocked
mutate protected state = blocked
emit Event = blocked
```

## 6.2 AI Context Depth

MVP AI Context depth:

```text
Level 1 — schema validation and boundary metadata.
```

Required validation:

```text
agent_reference_id
capability_scope
source_scope
ai_assisted
policy_omissions_disclosed
human_review_required
output_type
forbidden_action_attempt
```

---

# 7. Suggested Implementation Shape

Codex may adapt to the repo structure.

Preferred Python-like shape:

```text
core/agents/boundary.py
core/agents/capability_registry.py
core/agents/forbidden_actions.py
core/agents/ai_context_validator.py
core/agents/output_guard.py
```

Preferred TypeScript-like shape:

```text
src/core/agents/boundary.ts
src/core/agents/capability-registry.ts
src/core/agents/forbidden-actions.ts
src/core/agents/ai-context-validator.ts
src/core/agents/output-guard.ts
```

Suggested tests:

```text
tests/contracts/test_agent_boundary.py
tests/contracts/test_agent_forbidden_actions.py
tests/contracts/test_agent_permission_policy.py
tests/contracts/test_agent_human_review.py
tests/contracts/test_agent_event_task_boundaries.py
tests/contracts/test_agent_safe_errors.py
```

---

# 8. Allowed Agent Behaviors

Agents may perform bounded preparation actions:

```text
summarize
draft
classify
compare
suggest
identify gaps
prepare task plan
prepare communication draft
prepare workflow preview explanation
summarize audit trace
```

Allowed behavior must still obey:

```text
Permission
Policy
AI Context
Human Review where applicable
safe errors
versioning
```

Allowed output must be marked as:

```text
draft
suggestion
summary
preview
gap_analysis
non_final
human_review_required where applicable
```

---

# 9. Forbidden Agent Behaviors

Agents must not:

```text
approve
send
select
submit
certify
complete
mutate protected state
emit Events
create active Tasks
finalize goods/services
certify registrability
certify evidence sufficiency
certify official deadlines
commit provider selection
file official responses
execute payments
```

Forbidden behavior must return controlled safe errors.

Recommended error:

```text
PolicyRestricted
HumanReviewRequired
ValidationFailed
```

depending on contract.

The important rule:

```text
Forbidden action must not be executed.
```

---

# 10. Agent Capability Rules

Agent capability registry may define allowed capabilities.

Capability does not imply permission.

Required test matrix:

```text
CapabilityAllowed + PermissionAllowed + PolicyAllowed = allowed preparation only
CapabilityAllowed + PermissionDenied = blocked
CapabilityAllowed + PolicyRestrictedBlock = blocked
CapabilityAllowed + PolicyRestrictedRedact = redacted output
CapabilityAllowed + PolicyRequiresHumanReview = output marked review-required
CapabilityDenied + PermissionAllowed + PolicyAllowed = blocked
UnknownCapability = blocked
```

Agents must not self-expand capability scope.

---

# 11. Permission / Policy Interaction

AI-assisted behavior must check Permission and Policy where protected or policy-controlled.

Required behavior:

```text
Agent identity does not imply Permission.
Agent capability does not imply Permission.
PermissionAllowed does not bypass Policy.
PolicyAllowed does not bypass Permission.
PolicyRestrictedRedact removes restricted source/output fields.
PolicyNonDisclosureNotFound hides source existence where required.
PolicyRequiresHumanReview marks output as review-required.
```

Required tests:

```text
agent_permission_denied_blocks
agent_policy_restricted_blocks
agent_policy_redacts_output
agent_policy_nondisclosure_hides_source
agent_policy_requires_human_review
```

---

# 12. Human Review Interaction

Agent output is not Human Review.

Required behavior:

```text
AI draft remains draft.
AI recommendation remains recommendation.
AI classification remains suggestion until reviewed.
AI communication remains draft until reviewed.
AI workflow explanation remains preview.
HumanReviewRequired must remain if protected action needs review.
Valid Human Review may satisfy the gate only through owning service.
Agent must not convert draft to approved state.
```

Required tests:

```text
agent_output_not_human_review
agent_draft_requires_review_before_send
agent_classification_requires_review_before_finalization
agent_evidence_summary_requires_review_before_sufficiency_conclusion
```

---

# 13. Event Boundary Rules

Agents must not emit Events.

Required behavior:

```text
Agent output may include suggested event labels only as text metadata.
Agent output may include event_reference_ids only as trace if provided by Event Service.
Agent layer must not create Event records.
Agent layer must not call event emission directly.
```

Required tests:

```text
agent_layer_does_not_emit_events_directly
agent_event_reference_is_trace_not_command
```

---

# 14. Task Boundary Rules

Agents must not create or complete active Tasks.

Allowed:

```text
prepare task plan
suggest task type
identify task gap
summarize task status
```

Forbidden:

```text
create active Task
assign active Task
complete active Task
close active Task
change task owner
```

Required tests:

```text
agent_task_plan_not_active_task
agent_cannot_create_active_task
agent_cannot_complete_task
```

---

# 15. Communication Boundary Rules

Agents may draft communications.

Agents must not send communications.

Allowed:

```text
draft email
summarize inbound communication
compare reply draft to source facts
flag risky wording
suggest revision
```

Forbidden:

```text
send email
mark communication as approved
mark communication as sent
bypass human review
bypass policy redaction
```

Required tests:

```text
agent_can_prepare_communication_draft
agent_cannot_send_communication
agent_draft_preserves_human_review_required
agent_draft_respects_policy_redaction
```

---

# 16. Routing Boundary Rules

Routing Agent is stubbed in MVP.

Allowed:

```text
prepare routing candidate preview
summarize provider match factors
identify missing provider data
flag policy restrictions
```

Forbidden:

```text
final provider selection
provider engagement
automatic dispatch
commercial commitment
```

Required tests:

```text
routing_agent_candidate_preview_only
routing_agent_cannot_select_provider_final
routing_agent_policy_restriction_preserved
```

---

# 17. Knowledge Boundary Rules

Knowledge Agent may summarize known sources.

Allowed:

```text
summarize source passages
identify missing knowledge
classify knowledge relevance
compare knowledge entries
```

Forbidden:

```text
invent professional rule
certify legal conclusion
override source limitation
use restricted source without disclosure
hide policy omissions
```

Required tests:

```text
knowledge_agent_discloses_source_scope
knowledge_agent_discloses_policy_omissions
knowledge_agent_cannot_certify_professional_truth
```

---

# 18. Workflow Agent Boundary Rules

Workflow Agent may prepare workflow previews.

Allowed:

```text
prepare workflow explanation
identify missing workflow inputs
suggest next step
prepare task plan draft
```

Forbidden:

```text
apply workflow
approve workflow
create active Tasks
emit Events
submit filing
send communication
```

Required tests:

```text
workflow_agent_preview_only
workflow_agent_cannot_apply_workflow
workflow_agent_cannot_create_active_tasks
workflow_agent_cannot_emit_events
```

---

# 19. Audit Agent Boundary Rules

Audit Agent may summarize audit trace.

Allowed:

```text
summarize event trace
identify missing correlation
explain safe audit sequence
flag visibility omissions
```

Forbidden:

```text
alter audit trace
delete events
emit events
certify legal compliance
expose restricted event payload
```

Required tests:

```text
audit_agent_summary_only
audit_agent_cannot_modify_trace
audit_agent_respects_event_visibility
```

---

# 20. Error Safety Requirements

Agent-related errors must be safe.

Errors must not expose:

```text
system prompts
developer prompts
hidden reasoning
tool raw payloads with restricted data
restricted source contents
provider raw error text containing sensitive context
policy-omitted source details
```

Required tests:

```text
agent_error_no_prompt_leakage
agent_error_no_hidden_reasoning_leakage
agent_error_no_restricted_source_leakage
```

---

# 21. Required Fixtures

Use fixtures from TASK-002:

```text
ValidAIContext
InvalidAIContext
AIForbiddenActionApprove
AIForbiddenActionSend
AIForbiddenActionSubmit
AIForbiddenActionCertify
AIPolicyOmissions
AISourceScopeLimited
AIHumanReviewRequired
PermissionAllowed
PermissionDenied
PolicyAllowed
PolicyRestrictedBlock
PolicyRestrictedRedact
PolicyRequiresHumanReview
PolicyNonDisclosureNotFound
ValidHumanReview
MissingHumanReview
EventReferenceNotCommand
task_plan_preview
communication_draft
routing_candidate_preview
restricted_source_summary
agent_error_prompt_leak_attempt
agent_error_hidden_reasoning_attempt
```

If fixtures are missing:

```text
Add them to the fixture system.
Do not inline ad hoc production-like fixtures.
```

---

# 22. Required Tests

This task must implement tests for:

```text
allowed agent preparation actions
forbidden agent actions
agent capability validation
unknown capability blocked
agent identity does not imply Permission
agent capability does not imply Permission
PermissionDenied blocks AI-assisted behavior
PolicyRestrictedBlock blocks AI-assisted behavior
PolicyRestrictedRedact redacts AI output
PolicyRequiresHumanReview preserves review gate
PolicyNonDisclosureNotFound hides source existence
agent output is not Human Review
agent cannot create active Task
agent cannot complete Task
agent cannot send Communication
agent cannot select provider final
agent cannot apply Workflow
agent cannot submit filing
agent cannot emit Events
event_reference_id is trace only
AI prompt/hidden reasoning leakage blocked
restricted source leakage blocked
safe errors returned
```

Required test source:

```text
core-specs/contracts/tests/agent-boundary-tests.md
```

---

# 23. Integration Points for Later Tasks

This task must expose or validate boundary behavior usable by:

```text
TASK-010-mvp-execution-spine
```

Expected interfaces may include:

```text
validate_agent_capability(...)
validate_ai_context(...)
assert_agent_action_allowed(...)
assert_agent_action_forbidden(...)
guard_agent_output(...)
require_human_review_for_agent_output(...)
redact_agent_output_by_policy(...)
```

Names may differ by language/framework, but behavior must remain clear.

---

# 24. Forbidden Shortcuts

Codex must not:

```text
allow agent capability to imply Permission
allow agent identity to imply Permission
allow AI output to count as Human Review
allow agent to approve
allow agent to send
allow agent to select final provider
allow agent to submit official filing
allow agent to certify deadlines
allow agent to certify registrability
allow agent to certify evidence sufficiency
allow agent to create active Tasks
allow agent to complete Tasks
allow agent to emit Events
skip forbidden-action tests
skip policy redaction tests
skip HumanReviewRequired tests
skip prompt leakage tests
skip hidden reasoning leakage tests
use production data fixtures
build a full agent runtime in MVP
```

---

# 25. Acceptance Criteria

This task is complete only if:

```text
[ ] Agent boundary tests exist.
[ ] AI Context validation is tested.
[ ] Agent capability validation is tested.
[ ] Allowed preparation actions are tested.
[ ] Forbidden actions are tested.
[ ] Agent identity does not imply Permission.
[ ] Agent capability does not imply Permission.
[ ] PermissionDenied blocks agent behavior.
[ ] PolicyRestricted blocks or redacts agent output.
[ ] PolicyRequiresHumanReview preserves review gate.
[ ] Agent output is not Human Review.
[ ] Agent cannot create active Tasks.
[ ] Agent cannot complete Tasks.
[ ] Agent cannot send Communications.
[ ] Agent cannot select final provider.
[ ] Agent cannot apply Workflow.
[ ] Agent cannot submit official filing.
[ ] Agent cannot emit Events.
[ ] Event reference remains trace only.
[ ] Prompt/hidden reasoning leakage is tested.
[ ] Restricted source leakage is tested.
[ ] Safe errors are used.
[ ] Tests pass.
```

---

# 26. Final Summary Format

When Codex completes this task, reply with:

```text
Summary
- Agent boundary tests implemented.
- Files added or changed.
- Which source specs were used.
- Which behaviors are Level 1/2.
- Which forbidden behaviors are Level 3 enforced.
- Which behavior remains stubbed.

Tests
- Commands run.
- Test results.

Boundary Confirmation
- Agent identity does not imply Permission.
- Agent capability does not imply Permission.
- AI output is not Human Review.
- AI forbidden actions blocked.
- Human Review gates preserved.
- Policy redaction preserved.
- Agents cannot create/complete Tasks.
- Agents cannot send Communications.
- Agents cannot select providers finally.
- Agents cannot apply Workflows.
- Agents cannot emit Events.
- Event references are trace, not commands.
- Prompt/hidden reasoning does not leak.

Deferred
- Full agent runtime remains out of scope.
- Multi-agent orchestration remains out of scope.
- Next task recommended.
```

---

# 27. Revision Notes

| Version | Status | Notes |
|---------|--------|-------|
| 0.1.0 | Draft | Initial Codex TASK-009. Defines Agent Boundary Tests implementation scope, required source files, allowed/forbidden behaviors, Permission/Policy interaction, Human Review, Event/Task/Communication/Routing/Knowledge/Workflow/Audit boundaries, tests, forbidden shortcuts and acceptance criteria. |

---

**End of TASK-009 — Agent Boundary Tests**
