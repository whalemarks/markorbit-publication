# B04-FIG-02 — Constitutional Responsibility Boundary

**Status:** Release Candidate 1  
**Book:** Book 04 — MarkOrbit Workplace and Product Architecture

```mermaid
flowchart LR
    Core[Core<br/>defines shared meaning] --> Exec[Execution<br/>governs coordinated work]
    Exec --> Workplace[Workplace<br/>provides authorized organization context]
    Workplace --> Products[Products<br/>compose focused user journeys]
    Products --> MGSN[MGSN<br/>connects independent Orbits]
    Products --> Services[Owning Services<br/>change and record formal business facts]
    Human[Humans<br/>remain professionally accountable] --> Products
    AI[AI<br/>assists under explicit governance] --> Products
```

## Interpretation

The diagram expresses responsibility, not mandatory deployment topology. Logical ownership must remain visible even when components are implemented together.

## Authority Note

This figure is an explanatory architecture asset. It does not create a new Core Object, Service, status model, implementation topology, or protected-action authority.
