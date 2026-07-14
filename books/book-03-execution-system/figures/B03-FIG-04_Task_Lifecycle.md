# B03-FIG-04 — Task Lifecycle

**Status:** Release Candidate 1

```mermaid
flowchart LR
    P[Task Plan] --> R[Review]
    R --> C[Task Service Create]
    C --> A[Active Task]
    A --> B[Blocked / Waiting / In Progress]
    B --> D[Completed or Cancelled]
    D --> E[Event and Audit]
```
