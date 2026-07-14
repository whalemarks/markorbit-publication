# B03-FIG-10 — Workplace and Product Consumption

**Status:** Release Candidate 1

```mermaid
flowchart TB
    O[Organization: Real Actor] --> W[Workplace: Authorized Context]
    W --> P1[Lite]
    W --> P2[MarkReg]
    W --> P3[MGSN Interfaces]
    P1 --> E[Execution]
    P2 --> E
    P3 --> E
    E --> S[Owning Services]
    E --> T[Traceable Outcomes]
    T --> W
```
