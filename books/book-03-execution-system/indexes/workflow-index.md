# Appendix C — Workflow Pattern Index

## MVP Workflow Matrix

| Workflow | Chapter | Current depth | Allowed current effect |
|---|---|---:|---|
| Intake Execution | [17](../manuscript/B03-CH-17_Intake_Execution_Pattern.md) | Depth A | Approved internal preparation through owning Services |
| Application Preparation | [18](../manuscript/B03-CH-18_Application_Preparation_Pattern.md) | Depth A | Approved internal application-preparation state |
| Communication Review | [19](../manuscript/B03-CH-19_Communication_Review_Pattern.md) | Depth A | Draft and Human Review state; no send |
| Provider Routing Preparation | [20](../manuscript/B03-CH-20_Provider_Routing_Preparation_Pattern.md) | Depth B | Candidate comparison preview |
| Office Action Response Preparation | [21](../manuscript/B03-CH-21_Office_Action_Response_Preparation_Pattern.md) | Depth B | Response-preparation preview |
| Renewal Preparation | [22](../manuscript/B03-CH-22_Renewal_Preparation_Pattern.md) | Depth B | Renewal-readiness preview |
| Assignment Preparation | [23](../manuscript/B03-CH-23_Assignment_Preparation_Pattern.md) | Depth B | Assignment-package preview |
| Evidence Review Preparation | [24](../manuscript/B03-CH-24_Evidence_Review_Preparation_Pattern.md) | Depth B | Evidence-organization preview |

## Common Workflow Rules

- Preview is side-effect free.
- Apply is enabled only for approved Depth A internal effects.
- Workflow coordinates; owning Services mutate.
- Task plans are not active Tasks.
- Human Review binds exact version, scope and intended action.
- Permission and Policy apply to preview and apply.
- Workflow does not emit governed Events directly.
- AI may prepare but does not approve or execute protected action.
- Product cannot expand workflow depth.
- External send, filing, payment and provider commitment remain deferred.

## Architecture References

- [Workflow Coordination Model](../manuscript/B03-CH-10_Workflow_Coordination_Model.md)
- [Execution MVP Boundary](../manuscript/B03-CH-31_Execution_MVP_Boundary.md)
- [MVP Execution Workflow Set](../manuscript/B03-CH-32_MVP_Execution_Workflow_Set.md)
- [MVP Implementation Readiness](../manuscript/B03-CH-33_MVP_Implementation_Readiness.md)
