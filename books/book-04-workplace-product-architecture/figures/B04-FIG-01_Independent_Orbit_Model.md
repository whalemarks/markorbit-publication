# B04-FIG-01 — Independent Organization Orbit Model

**Status:** Release Candidate 1  
**Book:** Book 04 — MarkOrbit Workplace and Product Architecture

```mermaid
flowchart TB
    OS[MarkOrbit Operating System] --> Core[Core: Shared Meaning]
    Core --> Exec[Execution: Governed Coordination]
    Exec --> W[Organization Workplace]
    W --> P1[Lite]
    W --> P2[MarkReg]
    W --> P3[MGSN Gateway]
    W --> PX[Organization-Specific Products]
    W --- Private[(Private Data, Knowledge, Rules, Relationships)]
    W --> Network[MGSN / Other Orbits]
    Network --> O2[Independent Organization Orbit]
```

## Interpretation

Each organization remains the real legal, commercial, and professional actor. Shared foundations support the Orbit; they do not own it.

## Authority Note

This figure is an explanatory architecture asset. It does not create a new Core Object, Service, status model, implementation topology, or protected-action authority.
