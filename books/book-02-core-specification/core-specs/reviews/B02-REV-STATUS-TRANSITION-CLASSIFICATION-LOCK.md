# B02 — Status and Transition Classification Lock

**Review ID:** B02-REV-STATUS-TRANSITION-CLASSIFICATION-LOCK  
**Task:** PUB-TASK-B02-001  
**Status:** Draft owner decision record  
**Decision effect:** Accepted upon merge  

---

# 1. Decision

```text
CLASSIFICATION RESULT: ACCEPTED UPON MERGE

Trademark Status:
Parent-owned Controlled State Value Specification

Order Status:
Parent-owned Controlled State Value Specification

Matter Status:
Parent-owned Controlled State Value Specification

Task Status:
Parent-owned Controlled State Value Specification

Workflow State:
Workflow Contract Component

Workflow Transition:
Workflow Contract Component

Independent identity-bearing Core Object classification:
REJECTED FOR ALL SIX
```

Merging the PR that introduces this record constitutes owner acceptance of the above classification for Book 02.

---

# 2. Reasoning

A Core Object requires independent professional meaning, ownership, identity and lifecycle. The four status concepts do not have business identity apart from their parent objects. Their source of truth is the parent object's current `status` field, and they cannot be independently created, deleted, persisted or mutated.

Workflow State and Workflow Transition are definitions inside Workflow Contract structure. Modeling them again as independent aggregate roots would create duplicate sources of truth between Workflow Contract and separate objects.

Product UI must not define these states or transitions. AI must not invent new states or transitions. Owning Services remain responsible for actual mutation. Events record status changes and transition outcomes, but Events do not own the state.

---

# 3. Compatibility Effect

- Legacy Object IDs must not be silently reused.
- Historical files may retain old IDs as legacy references.
- Active indexes must mark the six legacy entries as reclassified.
- Future implementation must not generate six independent aggregate roots for these concepts.
- Future fixtures, schemas and APIs must not require independent status object IDs.
- Parent object `status` fields remain canonical for Trademark, Order, Matter and Task.
- Workflow Contract `state_definitions` and `transition_definitions` remain canonical for workflow structure.

---

# 4. Reference Inventory Summary

| Concept | Current Object Index Entry | Parent Object Field | Controlled Values Currently Defined | Referenced Object Spec Path | Actual File Exists | Referenced Service Specs | Referenced Event Specs | Referenced Contract Specs | Referenced API Specs | Current Classification Wording | Conflict Found | Proposed Canonical Classification |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Trademark Status | `OBJ-TM-003`, Trademark, Phase 2, Must Implement | `Trademark.status` | Draft; Planned; PendingFiling; Filed; UnderExamination; Published; Opposed; Registered; Refused; Abandoned; Cancelled; Expired; Invalidated; RenewalDue; ReviewRequired; Archived; DeletedReferenceOnly | future spec without Markdown link: `core-specs/objects/trademark-status.md` | No | Trademark Status Normalization Service; Trademark Status Service references | TrademarkStatusChanged | Trademark Status Contract references | Trademark Status Normalization API; `POST /trademarks/{id}/status` | listed as independent Core Object and also parent enum | Yes | Parent-owned Controlled State Value Specification |
| Order Status | `OBJ-ORD-004`, Order, Phase 3, Must Implement | `Order.status` | Draft; PendingConfirmation; Confirmed; ReadyForMatter; MatterCreated; InProgress; WaitingForCustomer; Completed; Cancelled; Archived; DeletedReferenceOnly | future spec without Markdown link: `core-specs/objects/order-status.md` | No | Order Status Service references | OrderStatusChanged | Order Status Contract references | `POST /orders/{id}/status` | listed as independent Core Object and also parent enum | Yes | Parent-owned Controlled State Value Specification |
| Matter Status | `OBJ-MAT-002`, Matter, Phase 3, Must Implement | `Matter.status` | Draft; Open; InProgress; WaitingForCustomer; WaitingForAgent; WaitingForOffice; ReviewRequired; Blocked; Completed; Cancelled; Archived; DeletedReferenceOnly | future spec without Markdown link: `core-specs/objects/matter-status.md` | No | Matter Status Service | MatterStatusChanged; MatterClosed | Matter Status Contract references | Matter Status API; `POST /matters/{id}/status` | listed as independent Core Object and also parent enum | Yes | Parent-owned Controlled State Value Specification |
| Workflow State | `OBJ-WFC-002`, Workflow Contract, Phase 3, Must Implement | `Workflow Contract.state_definitions` | Defined by Workflow Contract state definitions; no separate object value list is canonical in this lock | future component spec without Markdown link: `core-specs/objects/workflow-state.md` | No | Workflow State Resolution Service; Workflow State Service references | WorkflowTransitionRequested/Approved/Rejected outcome family | Workflow Contract | Workflow State Resolution API | listed as independent Core Object and also embedded Workflow Contract structure | Yes | Workflow Contract Component |
| Workflow Transition | `OBJ-WFC-003`, Workflow Contract, Phase 3, Must Implement | `Workflow Contract.transition_definitions` | Defined by Workflow Contract transition definitions and transition result values: Allowed; Rejected; ReviewRequired; BlockedByPermission; BlockedByPolicy; BlockedByGuard; InvalidState; InvalidTransition | future component spec without Markdown link: `core-specs/objects/workflow-transition.md` | No | Workflow Transition Validation Service | WorkflowTransitionRequested; WorkflowTransitionApproved; WorkflowTransitionRejected | Workflow Contract | Workflow Transition Validation API | listed as independent Core Object and also embedded Workflow Contract structure | Yes | Workflow Contract Component |
| Task Status | `OBJ-TSK-003`, Task, Phase 3, Must Implement | `Task.status` | Draft; Open; Assigned; InProgress; Waiting; Blocked; ReviewRequired; Completed; Cancelled; Archived; DeletedReferenceOnly | future spec without Markdown link: `core-specs/objects/task-status.md` | No | Task Status Service references | TaskStatusChanged; TaskCompleted; TaskBlocked | Task Status Contract references | `POST /tasks/{id}/status` | listed as independent Core Object and also parent enum | Yes | Parent-owned Controlled State Value Specification |

Inventory was performed across Book 02 indexes, appendices, object specs, domain/service/event/contract/API areas, codex task references, and Book 03 status/manuscript review references. Service, event, contract and API references remain valid as references to owning-service behavior, event traces, contracts or endpoints; they must not be interpreted as proof of independent status aggregate roots.

---

# 5. Follow-up Specifications

The follow-up work is a specification-document pack, not six Core Object aggregate specifications.

```text
Status Value Specification Pack
- Trademark Status Values
- Order Status Values
- Matter Status Values
- Task Status Values

Workflow Contract Component Specification Pack
- Workflow State Definition
- Workflow Transition Definition
```

