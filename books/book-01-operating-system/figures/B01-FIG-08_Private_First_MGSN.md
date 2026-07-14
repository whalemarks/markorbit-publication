# B01-FIG-08 — Private-First MGSN

**Status:** Release Candidate 1

```mermaid
flowchart LR
    N[Service Need] --> I[Internal Capability]
    N --> P[Private Partners]
    N --> T[Trusted Extended Network]
    N --> D[Limited Public Discovery]
    I --> H[Human Selection]
    P --> H
    T --> H
    D --> H
    H --> G[Governed Instruction]
    G --> A[Provider Acceptance]
```
