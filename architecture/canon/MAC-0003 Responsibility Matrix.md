# MarkOrbit Architecture Canon

# MAC-0003 — Responsibility Matrix

**Document ID:** MAC-0003

**Title:** Responsibility Matrix

**Version:** 1.0.0

**Status:** Canonical

**Category:** Foundational Standard

**Authority:** MarkOrbit Architecture Board

**Depends On:**

- MAC-0001 — Architecture Principles
- MAC-0002 — Architecture Layers

---

# Purpose

This document defines the canonical allocation of architectural responsibilities within the MarkOrbit Architecture.

Architecture is fundamentally the allocation of responsibilities.

Components exist because responsibilities exist.

Responsibilities determine ownership.

Ownership determines architectural boundaries.

This document is therefore the authoritative source for architectural responsibility ownership.

---

# Scope

This document defines:

- responsibility ownership;
- responsibility allocation;
- responsibility boundaries;
- responsibility consumption.

It does not define:

- architectural layers;
- canonical models;
- architectural relationships;
- governance processes.

Those subjects are specified by other canonical documents.

---

# Responsibility Principles

The Responsibility Matrix follows the principles established by MAC-0001.

Every architectural responsibility shall satisfy the following requirements.

## Requirement 1

A responsibility shall have exactly one owner.

---

## Requirement 2

Responsibilities shall not overlap.

---

## Requirement 3

Responsibilities may be consumed by multiple participants.

Ownership shall remain unique.

---

## Requirement 4

Responsibilities shall be allocated to architectural layers.

They shall not be allocated to products.

---

## Requirement 5

Responsibilities shall remain independent of implementation technologies.

---

# Canonical Responsibility Chain

The MarkOrbit Architecture allocates responsibilities through six canonical layers.

```text
Principles

define

↓

Core

provide

↓

Business

own

↓

Workplace

operate

↓

Network

connect

↓

Applications

deliver
```

Each verb represents a canonical architectural responsibility.

---

# Responsibility Allocation

## Principles

### Primary Responsibility

Define.

### Description

Establishes the constitutional foundation of the architecture.

### Owns

- First Principles
- Architectural Direction
- Normative Requirements

---

## Core

### Primary Responsibility

Provide.

### Description

Provides reusable architectural capabilities.

### Owns

- Identity
- Capability
- Knowledge
- Context
- Governance
- Policy

---

## Business

### Primary Responsibility

Own.

### Description

Owns commercial responsibility and organizational value creation.

### Owns

- Business Ownership
- Commercial Rules
- Delegation
- Authorization
- Value Creation

---

## Workplace

### Primary Responsibility

Operate.

### Description

Coordinates operational execution.

### Owns

- Daily Operations
- Workflow Execution
- Operational Context
- Human Collaboration
- Intelligent Collaboration

---

## Network

### Primary Responsibility

Connect.

### Description

Coordinates collaboration between independent Workplaces.

### Owns

- Service Routing
- Federation
- Trust
- Capability Discovery
- Cross-Organization Coordination

---

## Applications

### Primary Responsibility

Deliver.

### Description

Delivers architectural capabilities through user-facing products.

### Owns

- User Experience
- Product Interaction
- Domain Features

Applications do not own architectural responsibilities.

---

# Responsibility Matrix

| Architectural Responsibility | Canonical Owner |
|------------------------------|-----------------|
| Architectural Principles | Principles |
| Architectural Capabilities | Core |
| Identity | Core |
| Capability | Core |
| Knowledge | Core |
| Context | Core |
| Governance | Core |
| Policy | Core |
| Business Ownership | Business |
| Commercial Responsibility | Business |
| Authorization | Business |
| Delegation | Business |
| Value Creation | Business |
| Operational Execution | Workplace |
| Workflow Coordination | Workplace |
| Human Collaboration | Workplace |
| Intelligent Collaboration | Workplace |
| Service Routing | Network |
| Federation | Network |
| Trust | Network |
| Capability Discovery | Network |
| Product Experience | Applications |
| Domain Functionality | Applications |

This table is normative.

Architectural ownership shall conform to this allocation.

---

# Responsibility Consumption

Ownership and consumption are distinct concepts.

Responsibilities may be consumed by multiple architectural layers.

Ownership remains unchanged.

| Responsibility | Owner | Consumers |
|----------------|-------|-----------|
| Identity | Core | Business, Workplace, Applications |
| Capability | Core | Business, Workplace, Network |
| Knowledge | Core | Business, Workplace |
| Policy | Core | Business |
| Business Rules | Business | Workplace |
| Operational Context | Workplace | Network |
| Service Routing | Network | Applications |

Consumption does not imply ownership.

---

# Responsibility Boundaries

Responsibilities shall remain within their canonical boundaries.

## Core

Does not own:

- business policy;
- workflow;
- user experience.

---

## Business

Does not own:

- identity;
- infrastructure;
- routing.

---

## Workplace

Does not own:

- commercial ownership;
- architectural capability;
- ecosystem coordination.

---

## Network

Does not own:

- customers;
- organizations;
- business strategy.

---

## Applications

Do not own:

- architecture;
- responsibilities;
- canonical definitions.

---

# Responsibility Inheritance

Responsibilities propagate through the architecture.

```text
Define

↓

Provide

↓

Own

↓

Operate

↓

Connect

↓

Deliver
```

Responsibilities shall never propagate upward.

---

# Responsibility Constraints

Every architectural responsibility shall satisfy the following constraints.

### Constraint A

One responsibility.

One owner.

---

### Constraint B

Responsibilities shall not be duplicated.

---

### Constraint C

Responsibilities shall not migrate between layers without architectural revision.

---

### Constraint D

Responsibilities shall remain independent of products.

---

### Constraint E

Responsibilities shall remain stable across implementation generations.

---

# Responsibility Validation

Every new architectural capability shall identify:

- its responsibility;
- its owner;
- its consumers;
- its architectural layer.

Capabilities lacking a clearly defined responsibility shall not become part of the canonical architecture.

---

# Conformance

An architectural component conforms to this standard only if:

- its responsibilities are explicitly defined;
- ownership is unambiguous;
- responsibility boundaries are preserved;
- canonical ownership is respected.

---

# Authority

MAC-0003 is the authoritative definition of architectural responsibility ownership within the MarkOrbit Architecture.

Subsequent canonical documents may extend responsibilities.

They shall not redefine ownership established by this document.

---

# Revision Policy

Changes to responsibility ownership constitute major architectural revisions.

Editorial improvements shall not modify ownership semantics.

---

# Revision History

| Version | Status | Description |
|---------|--------|-------------|
| 1.0.0 | Canonical | First published edition of the Responsibility Matrix. |

---

**End of Document**