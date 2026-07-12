# Appendix B — Execution Context Index

Execution Context is the governed set of references and conditions needed to coordinate one operation. It is not a new Core Domain or a replacement for Core objects.

## Core Components

| Component | Purpose | Primary chapters |
|---|---|---|
| Operation identity | Identifies the semantic operation and Workflow | [06](../manuscript/B03-CH-06_Execution_Context.md), [25](../manuscript/B03-CH-25_Idempotency_and_Retry_Governance.md) |
| Subject and target references | Identifies the Core records involved | [06](../manuscript/B03-CH-06_Execution_Context.md), [09](../manuscript/B03-CH-09_Execution_Object_and_State_Model.md) |
| Actor and sponsor | Identifies the requesting human, Service, Integration or agent context | [06](../manuscript/B03-CH-06_Execution_Context.md), [29](../manuscript/B03-CH-29_Agent-Assisted_Execution_Governance.md) |
| Version snapshot | Binds source, review and apply versions | [27](../manuscript/B03-CH-27_Versioning_and_Change_Control.md) |
| Permission Context | Establishes access and action authority | [15](../manuscript/B03-CH-15_Permission_and_Policy_Gates.md) |
| Policy Context | Establishes applicable governance restrictions | [15](../manuscript/B03-CH-15_Permission_and_Policy_Gates.md) |
| Human Review Context | Binds reviewer, decision, scope and conditions | [12](../manuscript/B03-CH-12_Review_and_Approval_Lifecycle.md), [28](../manuscript/B03-CH-28_Human_Review_Governance.md) |
| Idempotency Context | Prevents duplicate semantic effects | [25](../manuscript/B03-CH-25_Idempotency_and_Retry_Governance.md) |
| Audit Context | Preserves accountability and correlation | [14](../manuscript/B03-CH-14_Event_Trace_Audit_and_Replay.md), [30](../manuscript/B03-CH-30_Execution_Observability_and_Audit.md) |
| AI Context | Constrains sources, assistance and prohibited authority | [16](../manuscript/B03-CH-16_Human_AI_Execution_Handoff.md), [29](../manuscript/B03-CH-29_Agent-Assisted_Execution_Governance.md) |
| Service dependencies | Identifies owning Services and supported effects | [10](../manuscript/B03-CH-10_Workflow_Coordination_Model.md), [33](../manuscript/B03-CH-33_MVP_Implementation_Readiness.md) |
| External references | Records provider, authority or connector evidence without redefining domain truth | [26](../manuscript/B03-CH-26_Error_Handling_and_Safe_Failure.md), [30](../manuscript/B03-CH-30_Execution_Observability_and_Audit.md) |

## Context Rules

1. Context is assembled before protected action.
2. Context references Core truth; it does not replace it.
3. Permission and Policy filter both input and output.
4. Human Review remains bound to exact versions and intended action.
5. Context is refreshed before apply, retry and continuation.
6. Missing or incompatible context causes safe failure.
7. Product state and agent memory are not authoritative context.
8. Historical audit preserves the context that governed the action at the time.

## Context by Workflow Depth

### Depth A

Depth A context must support preview, Human Review and internal apply through owning Services.

### Depth B

Depth B context supports preview and review preparation only. Apply remains disabled.

### Depth C

Depth C external protected action is outside the current MVP and requires future approved context and Integration contracts.
