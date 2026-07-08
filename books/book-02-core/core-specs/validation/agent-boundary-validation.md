# Agent Boundary Validation

**Spec ID:** B02-VALIDATION-AGENT-BOUNDARY  
**Spec Type:** Validation Specification  
**Spec File:** core-specs/validation/agent-boundary-validation.md  
**Related Book:** Book 02 — MarkOrbit Core Specification  
**Related Validation Index:** core-specs/validation/index.md  
**Related Architecture Validation:** core-specs/validation/architecture-consistency-validation.md  
**Related Traceability Validation:** core-specs/validation/traceability-validation.md  
**Related Workflow Validation:** core-specs/validation/workflow-contract-validation.md  
**Related Agent Specs:** core-specs/agents/  
**Related Test Contract:** core-specs/contracts/tests/agent-boundary-tests.md  
**Related Codex Task:** codex-tasks/TASK-009-agent-boundary-tests.md  
**Status:** Draft  
**Version:** 0.1.0  
**Validation Priority:** P0  
**Validation Depth:** Agent Boundary Level 1/2; Forbidden Action Level 3  
**Owner:** MarkOrbit Publications Editorial Board  

---

# 1. Purpose

This file defines how to validate AI Agent boundaries in MarkOrbit Core.

Agent Boundary Validation ensures that agents may assist professional execution but cannot replace human professional accountability or execute protected actions.

It validates the rule:

```text
AI may prepare.
AI may not decide.
AI may not execute protected actions.
AI may not define professional truth.
```

This validation is required before AI-assisted behavior is used in API, Workflow or MVP execution spine implementation.

---

# 2. Core Lock

```text
AI enhances professionals.
AI does not define professional truth.
Agent identity does not imply Permission.
Agent capability does not imply Permission.
Agent output does not equal Human Review.
Agents may summarize, draft, classify, compare, suggest and identify gaps.
Agents must not approve, send, select, submit, certify, complete, mutate protected state or emit Events.
AI Context bounds AI-assisted output.
Permission and Policy govern AI-assisted behavior.
Human Review gates protected professional or external-facing actions.
Codex must validate Agent boundaries before using AI-assisted behavior.
Codex must not create autonomous professional execution.
```

---

# 3. Validation Scope

This validation covers:

```text
AI Agent Governance
Agent Registry
Knowledge Agent
Task Agent
Communication Agent
Workflow Agent
Routing Agent
Audit Agent
AI Context
Permission / Policy interaction
Human Review interaction
Event boundary
Task boundary
Communication boundary
Routing boundary
Workflow boundary
Audit trace boundary
safe AI error behavior
test traceability
Codex task traceability
```

This validation does not cover:

```text
full agent runtime orchestration
model provider integration
prompt management platform
multi-agent planning
autonomous workflow execution
official filing automation
external message sending
provider auto-selection
professional legal certification
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
codex-tasks/TASK-009-agent-boundary-tests.md
core-specs/validation/index.md
core-specs/validation/architecture-consistency-validation.md
core-specs/validation/traceability-validation.md
```

Validation should also inspect:

```text
core-specs/contracts/api/agent-api-contract.md
core-specs/contracts/api/communication-api-contract.md
core-specs/contracts/api/task-api-contract.md
core-specs/contracts/api/workflow-contract-api-contract.md
core-specs/contracts/api/routing-api-contract.md
core-specs/contracts/api/event-api-contract.md
core-specs/contracts/workflows/
```

---

# 5. Agent Spec Existence Checks

Validate:

```text
[ ] ai-agent-governance.md exists.
[ ] agent-registry.md exists.
[ ] knowledge-agent.md exists.
[ ] task-agent.md exists.
[ ] communication-agent.md exists.
[ ] workflow-agent.md exists.
[ ] routing-agent.md exists.
[ ] audit-agent.md exists.
[ ] agent-boundary-tests.md exists.
[ ] TASK-009-agent-boundary-tests.md exists.
```

Blocked if:

```text
AI Agent Governance spec is missing.
Agent Boundary Test contract is missing.
TASK-009 is missing.
```

---

# 6. Agent Depth Classification

Validate according to the Implementation Depth Matrix.

MVP agent boundary depth:

```text
Level 1/2 for Agent Registry and AI Context validation.
Level 3 for forbidden-action enforcement tests.
```

Required MVP behavior:

```text
agent identity validation
agent capability validation
AI Context validation
allowed preparation action validation
forbidden action blocking
Permission/Policy enforcement
Human Review preservation
safe error behavior
```

Document-only / deferred behavior:

```text
full agent runtime
multi-agent orchestration
autonomous workflow execution
provider auto-selection
official filing automation
```

Architecture violation:

```text
MVP implements autonomous agent execution.
MVP agent runtime submits filings.
MVP agent runtime sends external communication.
MVP routing agent selects final provider.
MVP agent certifies professional truth.
```

---

# 7. Allowed Agent Behavior Checks

Agents may only perform preparation or support actions.

Allowed actions:

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

Validate:

```text
[ ] Allowed action is marked draft/suggestion/preview/non-final where applicable.
[ ] Allowed action carries AI Context.
[ ] Allowed action respects Permission and Policy.
[ ] Allowed action preserves Human Review where required.
[ ] Allowed action does not create side effects by itself.
```

Failure condition:

```text
allowed preparation action produces final, approved or certified output.
```

---

# 8. Forbidden Agent Behavior Checks

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

Validate:

```text
[ ] Forbidden action attempts are explicitly blocked.
[ ] Forbidden action tests exist.
[ ] Forbidden action returns safe controlled error.
[ ] Forbidden action creates no side effects.
[ ] Forbidden action does not create Event.
[ ] Forbidden action does not create Task.
[ ] Forbidden action does not send Communication.
```

Architecture violation:

```text
agent can send Communication
agent can submit filing
agent can complete Task
agent can emit Event
agent can select provider final
agent can certify legal/professional conclusion
```

---

# 9. Agent Capability Validation

Validate:

```text
[ ] Agent capability is explicitly declared.
[ ] Agent capability maps to allowed actions.
[ ] Agent cannot self-expand capability.
[ ] UnknownCapability is blocked.
[ ] CapabilityDenied is blocked.
[ ] CapabilityAllowed does not imply Permission.
[ ] CapabilityAllowed does not imply Policy allowance.
```

Required matrix:

```text
CapabilityAllowed + PermissionAllowed + PolicyAllowed = allowed preparation only
CapabilityAllowed + PermissionDenied = blocked
CapabilityAllowed + PolicyRestrictedBlock = blocked
CapabilityAllowed + PolicyRestrictedRedact = redacted output
CapabilityAllowed + PolicyRequiresHumanReview = review-required output
CapabilityDenied + PermissionAllowed + PolicyAllowed = blocked
UnknownCapability = blocked
```

Blocked if:

```text
agent capability is treated as permission
unknown capability defaults to allowed
```

---

# 10. AI Context Validation

Validate:

```text
[ ] agent_reference_id is present where applicable.
[ ] capability_scope is present.
[ ] source_scope is present.
[ ] ai_assisted flag is present.
[ ] output_type is draft/suggestion/summary/preview/non-final where applicable.
[ ] policy_omissions_disclosed is true where restricted sources are omitted.
[ ] human_review_required is true where protected output requires review.
[ ] forbidden_action_attempt is detected or blocked where applicable.
```

Blocked if:

```text
AI-assisted output has no AI Context.
AI output omits restricted sources without disclosure.
AI output claims final professional truth.
```

---

# 11. Permission / Policy Interaction Checks

Validate:

```text
[ ] Agent identity does not imply Permission.
[ ] Agent capability does not imply Permission.
[ ] PermissionAllowed does not bypass Policy.
[ ] PolicyAllowed does not bypass Permission.
[ ] PermissionDenied blocks agent behavior.
[ ] UnknownPermission fails closed.
[ ] PolicyRestrictedBlock blocks agent behavior.
[ ] PolicyRestrictedRedact redacts agent output.
[ ] PolicyRequiresHumanReview marks output review-required.
[ ] PolicyNonDisclosureNotFound hides source existence.
```

Required tests:

```text
agent_permission_denied_blocks
agent_policy_restricted_blocks
agent_policy_redacts_output
agent_policy_nondisclosure_hides_source
agent_policy_requires_human_review
```

Architecture violation:

```text
agent reads restricted source without Permission/Policy
agent reveals hidden source existence
agent uses policy-redacted data in output
```

---

# 12. Human Review Interaction Checks

Validate:

```text
[ ] Agent output is not Human Review.
[ ] AI draft remains draft.
[ ] AI recommendation remains recommendation.
[ ] AI classification remains suggestion until reviewed.
[ ] AI communication remains draft until reviewed.
[ ] HumanReviewRequired is preserved for protected outputs.
[ ] Human Review does not bypass Permission.
[ ] Human Review does not bypass Policy.
[ ] Valid Human Review can satisfy gate only through owning service.
```

Architecture violation:

```text
agent output equals review approval
AI draft becomes approved communication
AI suggestion becomes final classification
Human Review record directly executes downstream action
```

---

# 13. Task Boundary Checks

Validate:

```text
[ ] Task Agent may prepare task plan.
[ ] Task Agent may identify missing tasks.
[ ] Task Agent may summarize task status.
[ ] Task Agent cannot create active Task.
[ ] Task Agent cannot assign active Task.
[ ] Task Agent cannot complete active Task.
[ ] Task Agent cannot close active Task.
[ ] Active Tasks are created only by Task Service.
```

Architecture violation:

```text
agent creates task_reference_id as active Task
agent completes Task
agent changes Task status
agent assigns Task directly
```

---

# 14. Communication Boundary Checks

Validate:

```text
[ ] Communication Agent may draft communication.
[ ] Communication Agent may summarize inbound communication.
[ ] Communication Agent may flag risky wording.
[ ] Communication Agent may suggest revisions.
[ ] Communication Agent cannot send communication.
[ ] Communication Agent cannot mark communication approved.
[ ] Communication Agent cannot mark communication sent.
[ ] Communication Agent cannot bypass Human Review.
[ ] Communication Agent cannot bypass Policy redaction.
```

Architecture violation:

```text
agent sends email
agent marks communication as sent
agent bypasses review
agent exposes policy-restricted content in draft
```

---

# 15. Workflow Boundary Checks

Validate:

```text
[ ] Workflow Agent may prepare workflow preview explanation.
[ ] Workflow Agent may identify missing workflow inputs.
[ ] Workflow Agent may suggest next step.
[ ] Workflow Agent may prepare task plan draft.
[ ] Workflow Agent cannot apply workflow.
[ ] Workflow Agent cannot approve workflow.
[ ] Workflow Agent cannot create active Tasks.
[ ] Workflow Agent cannot emit Events.
[ ] Workflow Agent cannot submit filing.
[ ] Workflow Agent cannot send communication.
```

Architecture violation:

```text
workflow agent applies workflow
workflow agent creates active Task
workflow agent emits Event
workflow agent submits filing
```

---

# 16. Routing Boundary Checks

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

Validate:

```text
[ ] Routing Agent output is preview-only.
[ ] Provider final selection requires Human Review.
[ ] Routing Agent respects Policy visibility.
[ ] Routing Agent does not expose provider commercial terms where restricted.
```

Architecture violation:

```text
Routing Agent selects final provider.
Routing Agent engages provider.
Routing Agent makes commercial commitment.
```

---

# 17. Knowledge Boundary Checks

Validate:

```text
[ ] Knowledge Agent may summarize source passages.
[ ] Knowledge Agent may identify missing knowledge.
[ ] Knowledge Agent may classify relevance.
[ ] Knowledge Agent may compare knowledge entries.
[ ] Knowledge Agent discloses source scope.
[ ] Knowledge Agent discloses policy omissions.
[ ] Knowledge Agent cannot invent professional rule.
[ ] Knowledge Agent cannot certify legal conclusion.
[ ] Knowledge Agent cannot override source limitation.
```

Architecture violation:

```text
Knowledge Agent certifies legal rule as professional truth.
Knowledge Agent hides source limitation.
Knowledge Agent uses restricted source without disclosure.
```

---

# 18. Audit Boundary Checks

Validate:

```text
[ ] Audit Agent may summarize event trace.
[ ] Audit Agent may identify missing correlation.
[ ] Audit Agent may explain safe audit sequence.
[ ] Audit Agent may flag visibility omissions.
[ ] Audit Agent cannot alter audit trace.
[ ] Audit Agent cannot delete Events.
[ ] Audit Agent cannot emit Events.
[ ] Audit Agent cannot certify legal compliance.
[ ] Audit Agent cannot expose restricted event payload.
```

Architecture violation:

```text
Audit Agent modifies Event trace.
Audit Agent deletes Event.
Audit Agent emits Event.
Audit Agent reveals restricted Event payload.
```

---

# 19. Event Boundary Checks

Validate:

```text
[ ] Agent layer does not emit Events.
[ ] Agent output may include event_reference_ids only as trace if provided by Event Service.
[ ] Agent output cannot treat event_reference_id as command.
[ ] Agent output cannot complete Task using event_reference_id.
[ ] Agent output cannot send Communication using event_reference_id.
```

Required tests:

```text
agent_layer_does_not_emit_events_directly
agent_event_reference_is_trace_not_command
```

---

# 20. Error Safety Checks

Agent-related errors must be safe.

Validate:

```text
[ ] Agent errors use Error Contract.
[ ] Agent errors preserve correlation_id.
[ ] Agent errors do not expose system prompts.
[ ] Agent errors do not expose developer prompts.
[ ] Agent errors do not expose hidden reasoning.
[ ] Agent errors do not expose tool raw payloads with restricted data.
[ ] Agent errors do not expose restricted source contents.
[ ] Agent errors do not expose policy-omitted source details.
```

Architecture violation:

```text
agent error leaks prompt internals
agent error leaks hidden reasoning
agent error leaks restricted source
agent error leaks policy internals
```

---

# 21. Test Traceability Checks

Validate:

```text
[ ] Agent Boundary Tests map to TASK-009.
[ ] AI Context tests exist.
[ ] Agent capability tests exist.
[ ] Allowed action tests exist.
[ ] Forbidden action tests exist.
[ ] PermissionDenied tests exist.
[ ] PolicyRestricted tests exist.
[ ] HumanReviewRequired tests exist.
[ ] Agent no-active-task tests exist.
[ ] Agent no-send tests exist.
[ ] Agent no-workflow-apply tests exist.
[ ] Agent no-event-emission tests exist.
[ ] Prompt/hidden reasoning leakage tests exist.
[ ] Restricted source leakage tests exist.
```

Blocked if:

```text
Agent Boundary Tests missing.
Forbidden action tests missing.
AI output/Human Review separation not tested.
```

---

# 22. Validation Procedure

Perform validation in this order:

```text
1. Confirm required Agent specs exist.
2. Confirm Agent Boundary Test contract exists.
3. Confirm TASK-009 exists.
4. Validate agent depth classification.
5. Validate allowed behaviors.
6. Validate forbidden behaviors.
7. Validate capability rules.
8. Validate AI Context.
9. Validate Permission/Policy interaction.
10. Validate Human Review interaction.
11. Validate Task boundary.
12. Validate Communication boundary.
13. Validate Workflow boundary.
14. Validate Routing boundary.
15. Validate Knowledge boundary.
16. Validate Audit boundary.
17. Validate Event boundary.
18. Validate Error safety.
19. Validate test traceability.
20. Classify findings.
21. Produce validation report.
```

---

# 23. Finding Classification

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
Blocked = required agent spec, test or governance mapping missing.
Architecture Violation = agent can execute protected action or boundary breach.
Warning = future agent capability incomplete but safe.
Out of Scope = valid but beyond MVP.
Deferred = later-phase agent runtime item.
Pass = sufficient for current depth.
```

---

# 24. Required Evidence

Every finding must include:

```text
agent spec
agent capability
action
source file
missing or inconsistent rule
MVP category
implementation depth
required fix
Codex impact
```

Example:

```text
Finding: Communication Agent can send external communication.
Status: Architecture Violation
Agent: communication-agent
Action: send
Required Fix: Block send action and require Human Review + Communication Service ownership.
Codex Impact: Block TASK-009 and TASK-010.
```

---

# 25. Architecture Violation Triggers

The following always fail validation:

```text
Agent identity implies Permission.
Agent capability implies Permission.
Agent output equals Human Review.
Agent approves protected action.
Agent sends Communication.
Agent selects final provider.
Agent submits official filing.
Agent certifies deadline.
Agent certifies registrability.
Agent certifies evidence sufficiency.
Agent creates active Task.
Agent completes active Task.
Agent applies Workflow.
Agent mutates protected state.
Agent emits Events.
Agent treats Event reference as command.
Agent exposes restricted source.
Agent leaks prompts or hidden reasoning.
```

---

# 26. Acceptance Criteria

Agent Boundary Validation passes only if:

```text
[ ] Required source files exist.
[ ] All Agent specs exist.
[ ] Agent Boundary Test contract exists.
[ ] TASK-009 exists.
[ ] Agent depth classification is respected.
[ ] Allowed preparation actions remain non-final.
[ ] Forbidden actions are blocked.
[ ] Agent identity does not imply Permission.
[ ] Agent capability does not imply Permission.
[ ] AI Context is required for AI-assisted output.
[ ] Permission/Policy governance is preserved.
[ ] Policy redaction and omission disclosure are preserved.
[ ] Human Review gates are preserved.
[ ] Agent output is not Human Review.
[ ] Agents cannot create or complete active Tasks.
[ ] Agents cannot send Communications.
[ ] Agents cannot apply Workflows.
[ ] Agents cannot select final providers.
[ ] Agents cannot submit official filings.
[ ] Agents cannot emit Events.
[ ] Event references remain trace only.
[ ] Agent errors are safe.
[ ] Test traceability exists.
[ ] No Architecture Violation exists.
[ ] No Blocked finding exists in MVP agent boundaries.
```

---

# 27. Validation Report Template

```text
Validation: Agent Boundary
Status: Pass | Warning | Blocked | Architecture Violation
Scope: Agent Specs and Agent Boundary Tests

Sources Checked:
- <file>
- <file>

Findings:
- <finding>

Evidence:
- Agent:
- Capability:
- Action:
- File / Section:

Required Fix:
- <fix>

Codex Impact:
- <task affected>

Decision:
- Proceed | Proceed with warning | Block | Defer
```

---

# 28. Codex Usage

Codex must use this validation:

```text
before implementing TASK-009-agent-boundary-tests
before using AI-assisted behavior in TASK-010
after modifying Agent specs
after modifying AI Context
during PR review
```

Codex must not:

```text
build full agent runtime in MVP
let agent capability imply Permission
let agent output equal Human Review
allow agents to execute protected actions
allow agents to mutate state
allow agents to emit Events
skip policy redaction
skip Human Review gates
skip safe AI error behavior
```

---

# 29. Revision Notes

| Version | Status | Notes |
|---------|--------|-------|
| 0.1.0 | Draft | Initial Agent Boundary Validation. Defines Agent spec existence, depth, allowed/forbidden behaviors, capability, AI Context, Permission/Policy, Human Review, Task/Communication/Workflow/Routing/Knowledge/Audit/Event boundaries, error safety, test traceability and violation triggers. |

---

**End of Agent Boundary Validation**
