# Appendix G — Event Trace Index

## Distinctions

| Concept | Meaning |
|---|---|
| Domain Event | Governed fact emitted by an owning Service or approved Event boundary |
| Diagnostic log | Technical information used for diagnosis |
| Trace | Correlated view across execution activity |
| Audit Context | Actor, authority, version and purpose needed to interpret action |
| Audit replay | Read-only historical reconstruction |
| Metric | Aggregate measurement; not proof of an individual effect |

## Event Rules

1. Workflow coordinates and correlates; it does not emit governed Events directly.
2. AI and agents do not independently emit governed Events.
3. A tool call is not automatically an Event.
4. A missing Event does not prove that no effect occurred.
5. Duplicate observation is not a new Event.
6. Historical Events retain the versions and context that governed them.
7. Replay must not repeat mutation, send, filing, payment or provider action.

## Primary References

- [Event Trace, Audit and Replay](../manuscript/B03-CH-14_Event_Trace_Audit_and_Replay.md)
- [Execution Observability and Audit](../manuscript/B03-CH-30_Execution_Observability_and_Audit.md)
- [Error Handling and Safe Failure](../manuscript/B03-CH-26_Error_Handling_and_Safe_Failure.md)
