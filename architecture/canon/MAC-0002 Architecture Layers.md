# MarkOrbit Architecture Canon

# MAC-0002 — Architecture Layers

**Document ID:** MAC-0002

**Title:** Architecture Layers

**Version:** 1.0.0

**Status:** Canonical

**Category:** Foundational Standard

**Authority:** MarkOrbit Architecture Board

**Depends On:**

- MAC-0001 — Architecture Principles

---

# Purpose

This document defines the canonical architectural layers of the MarkOrbit Architecture.

Architectural layers establish the permanent structural organization of the ecosystem.

Each layer exists to own one architectural responsibility.

Layers are stable.

Implementations evolve.

Every architectural component shall belong to exactly one layer.

---

# Scope

This document defines:

- architectural layers;
- layer responsibilities;
- layer boundaries;
- dependency rules.

It does not define:

- canonical models;
- responsibility ownership;
- architectural relationships;
- implementation details.

Those subjects are specified by subsequent canonical documents.

---

# Architectural Layering

The MarkOrbit Architecture is organized into six permanent layers.

```text
┌──────────────────────────────────────┐
│ Layer 5 │ Applications               │
├──────────────────────────────────────┤
│ Layer 4 │ Network                    │
├──────────────────────────────────────┤
│ Layer 3 │ Workplace                  │
├──────────────────────────────────────┤
│ Layer 2 │ Business                   │
├──────────────────────────────────────┤
│ Layer 1 │ Core                       │
├──────────────────────────────────────┤
│ Layer 0 │ Principles                 │
└──────────────────────────────────────┘
```

Each layer builds upon the capabilities provided by the layer immediately below it.

Dependencies shall always point downward.

Responsibilities shall never migrate upward.

---

# Layer 0

# Principles

## Purpose

Provides the constitutional foundation of the architecture.

## Responsibility

Defines the fundamental principles governing the entire ecosystem.

## Provides

- Architectural philosophy
- First principles
- Normative foundation

## Depends On

None.

---

# Layer 1

# Core

## Purpose

Provides reusable architectural capabilities shared by every participant.

## Responsibility

Defines the permanent capabilities of the ecosystem.

## Provides

- Identity
- Capability
- Knowledge
- Context
- Governance
- Policy

## Depends On

Principles.

---

# Layer 2

# Business

## Purpose

Transforms reusable capabilities into business value.

## Responsibility

Defines how organizations own, organize and govern professional business.

## Provides

- Business ownership
- Commercial policy
- Delegation
- Authorization
- Value creation

## Depends On

Core.

---

# Layer 3

# Workplace

## Purpose

Provides the operational environment in which participants perform professional work.

## Responsibility

Coordinates operational execution.

## Provides

- Operational environment
- Workflow execution
- Human collaboration
- Intelligent collaboration
- Operational context

## Depends On

Business.

---

# Layer 4

# Network

## Purpose

Enables collaboration between independent Workplaces.

## Responsibility

Coordinates ecosystem interaction.

## Provides

- Service routing
- Federation
- Trust
- Capability discovery
- Cross-organization collaboration

## Depends On

Workplace.

---

# Layer 5

# Applications

## Purpose

Delivers architecture through user-facing implementations.

## Responsibility

Provides product experiences based upon architectural capabilities.

## Provides

- User interfaces
- Domain-specific functionality
- Professional solutions

## Depends On

Network.

---

# Canonical Layer Hierarchy

The architectural hierarchy shall remain stable.

```text
Principles

↓

Core

↓

Business

↓

Workplace

↓

Network

↓

Applications
```

No additional canonical layer shall be introduced without formal architectural approval.

---

# Dependency Rules

## Rule 1

Each layer may depend only upon the layer immediately below it.

---

## Rule 2

Lower layers shall never depend upon upper layers.

---

## Rule 3

Cross-layer dependencies are prohibited.

---

## Rule 4

Circular dependencies are prohibited.

---

## Rule 5

Architectural dependencies shall remain independent of implementation technologies.

---

# Layer Characteristics

| Layer | Stability | Change Frequency |
|--------|-----------|-----------------:|
| Principles | Very High | Extremely Rare |
| Core | Very High | Rare |
| Business | High | Occasional |
| Workplace | Medium | Regular |
| Network | Medium | Regular |
| Applications | Adaptive | Continuous |

The stability of a layer decreases toward the top of the architecture.

The adaptability of a layer increases toward the top.

---

# Layer Responsibilities

Each layer answers one architectural question.

| Layer | Architectural Question |
|--------|------------------------|
| Principles | Why does the architecture exist? |
| Core | What capabilities are universally available? |
| Business | How is value created and governed? |
| Workplace | How is professional work performed? |
| Network | How do independent organizations collaborate? |
| Applications | How is architecture experienced by users? |

A layer shall answer only its own architectural question.

---

# Layer Constraints

Every architectural layer shall satisfy the following constraints.

### Constraint A

Own one primary responsibility.

---

### Constraint B

Expose reusable capabilities.

---

### Constraint C

Remain independent of implementation technology.

---

### Constraint D

Avoid responsibility overlap with adjacent layers.

---

### Constraint E

Preserve architectural stability appropriate to its position.

---

# Architectural Stability

Lower layers are expected to remain stable across multiple generations of technology.

Upper layers are expected to evolve continuously.

This separation allows innovation without compromising architectural integrity.

---

# Conformance

An architectural layer conforms to this standard only if it:

- occupies one canonical position;
- owns one primary responsibility;
- respects canonical dependencies;
- preserves architectural boundaries.

---

# Authority

MAC-0002 is the authoritative definition of the architectural layering of the MarkOrbit Architecture.

Subsequent canonical documents may reference these layers.

They shall not redefine them.

---

# Revision Policy

The introduction, removal or reordering of canonical layers constitutes a major architectural revision.

Editorial improvements shall not alter the architectural hierarchy.

---

# Revision History

| Version | Status | Description |
|---------|--------|-------------|
| 1.0.0 | Canonical | First published edition of the Architecture Layers. |

---

**End of Document**