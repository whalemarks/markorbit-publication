# B04-FIG-08 — Private-First Network Expansion

**Status:** Release Candidate 1  
**Book:** Book 04 — MarkOrbit Workplace and Product Architecture

```mermaid
flowchart LR
    Private[Organization-Controlled Private Partners] --> Trusted[Trusted Extended Network]
    Trusted --> Limited[Limited Public Discovery]
    Need[Service Need] --> Private
    Private -->|No suitable capability| Trusted
    Trusted -->|No suitable capability| Limited
    Limited --> Candidate[Candidate Providers]
    Candidate --> Human[Human Selection]
```

## Interpretation

Discovery expands only as needed. Existing relationships, private pricing, client information, and organization-owned Trust are not surrendered to a central marketplace.

## Authority Note

This figure is an explanatory architecture asset. It does not create a new Core Object, Service, status model, implementation topology, or protected-action authority.
