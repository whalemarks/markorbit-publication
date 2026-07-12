# Appendix D — Task Lifecycle Index

## Canonical Distinctions

| Concept | Meaning |
|---|---|
| Task plan | Preview of proposed work; no active Task exists |
| Task request | Governed request to Task Service |
| Active Task | Task created and owned by Task Service |
| Assignment | Governed association of an eligible actor or team |
| Review Task | Task that requests accountable Human Review |
| Follow-up Task | Task created after a governed result or gap |
| Task completion | Service-owned lifecycle change under current Permission, Policy and review rules |

## Lifecycle Rules

1. Workflow may prepare a Task plan.
2. Only Task Service may create or mutate an active Task.
3. Duplicate requests must not create duplicate active Tasks.
4. AI or agents may prepare Task content but may not complete protected Tasks independently.
5. Task state does not replace Matter, Order, Trademark or Workflow truth.
6. Task Events come from the owning Service.
7. Partial or uncertain Task creation requires reconciliation, not blind duplication.

## Primary References

- [Task Lifecycle Model](../manuscript/B03-CH-11_Task_Lifecycle_Model.md)
- [Workflow Coordination Model](../manuscript/B03-CH-10_Workflow_Coordination_Model.md)
- [Idempotency and Retry Governance](../manuscript/B03-CH-25_Idempotency_and_Retry_Governance.md)
- [Human Review Governance](../manuscript/B03-CH-28_Human_Review_Governance.md)
- [Execution MVP Boundary](../manuscript/B03-CH-31_Execution_MVP_Boundary.md)
