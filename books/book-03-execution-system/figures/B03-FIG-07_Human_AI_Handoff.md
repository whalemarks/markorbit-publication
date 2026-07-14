# B03-FIG-07 — Human–AI Handoff

**Status:** Release Candidate 1

```mermaid
flowchart LR
    C[Authorized Context] --> AI[AI Preparation]
    AI --> D[Draft / Recommendation / Gap List]
    D --> H[Human Review]
    H --> Q[Questions or Correction]
    Q --> AI
    H --> A[Approved Subject and Scope]
    A --> E[Governed Execution]
```
