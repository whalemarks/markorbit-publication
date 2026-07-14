# B03-FIG-06 — Event Trace

**Status:** Release Candidate 1

```mermaid
flowchart TB
    W[Workflow Coordination] --> S[Owning Service]
    S --> F[Formal Fact Change]
    S --> E[Governed Event]
    W --> O[Execution Observation]
    E --> T[Event Trace]
    O --> T
    T --> A[Audit and Read-Only Replay]
```
