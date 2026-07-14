# B03-FIG-03 — Preview to Protected Action

**Status:** Release Candidate 1

```mermaid
flowchart LR
    N[Need] --> P[Preview]
    P --> R[Human Review]
    R --> A[Consequence-Specific Approval]
    A --> C[Current Authorization Check]
    C --> E[Execution Request]
    E --> S[Owning Service]
    S --> O[Outcome and Event Trace]
```
