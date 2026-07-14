# B04-FIG-06 — Artifact Lifecycle

**Status:** Release Candidate 1  
**Book:** Book 04 — MarkOrbit Workplace and Product Architecture

```mermaid
flowchart LR
    Need --> Candidate[Artifact Candidate]
    Candidate --> Preparation
    Preparation --> Preview[Preview Render Where Useful]
    Preview --> Review
    Review --> Revision
    Revision --> Approval[Approval for Defined Use]
    Approval --> Final[Final Render]
    Final --> Edit[Optional Edit]
    Edit --> ReReview[Re-Review Where Material]
    ReReview --> Consequence[Delivery, Publish, or Formalization]
    Consequence --> Outcome
    Outcome --> Feedback
    Feedback --> Retention[Reuse, Supersession, Archive, or Retirement]
```

## Interpretation

The lifecycle is conceptual, not a universal status enumeration. Material edits may require a new Artifact version and renewed Review.

## Authority Note

This figure is an explanatory architecture asset. It does not create a new Core Object, Service, status model, implementation topology, or protected-action authority.
