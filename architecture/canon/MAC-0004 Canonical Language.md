# MarkOrbit Architecture Canon

# MAC-0004 — Canonical Language

**Document ID:** MAC-0004

**Title:** Canonical Language

**Version:** 1.0.0

**Status:** Canonical

**Category:** Foundational Standard

**Authority:** MarkOrbit Architecture Board

**Depends On:**

- MAC-0001 — Architecture Principles
- MAC-0002 — Architecture Layers
- MAC-0003 — Responsibility Matrix

---

# Purpose

This document establishes the canonical vocabulary of the MarkOrbit Architecture.

Architecture depends upon shared language.

Without a canonical vocabulary, architectural concepts gradually diverge across specifications, implementations and products.

This document defines the authoritative terminology used throughout the MarkOrbit ecosystem.

Every architectural term shall have:

- one canonical name;
- one canonical definition;
- one architectural meaning.

---

# Scope

This document defines:

- canonical architectural terminology;
- architectural definitions;
- naming conventions;
- terminology governance.

It does not define:

- architectural models;
- responsibility ownership;
- implementation terminology;
- product terminology.

Those subjects belong to other canonical documents.

---

# Canonical Language Principles

The MarkOrbit Architecture follows six language principles.

## Principle 1

Every architectural concept shall have one canonical name.

---

## Principle 2

Every canonical name shall have one authoritative definition.

---

## Principle 3

Definitions belong to the Architecture Canon.

Specifications reference definitions.

Implementations apply definitions.

---

## Principle 4

Canonical language shall remain independent of products and technologies.

---

## Principle 5

Marketing terminology shall never replace architectural terminology.

---

## Principle 6

Canonical terminology evolves only through architectural governance.

---

# Canonical Terminology

## Architecture

### Definition

The permanent allocation of responsibilities within the MarkOrbit ecosystem.

---

## Principle

### Definition

A fundamental rule governing architectural design and evolution.

---

## Layer

### Definition

A permanent architectural boundary that owns one primary responsibility.

---

## Responsibility

### Definition

An architectural obligation assigned to one canonical owner.

---

## Capability

### Definition

A reusable architectural ability provided by the Core.

Capabilities are consumed rather than recreated.

---

## Infrastructure

### Definition

Reusable architectural capability shared across independent organizations.

---

## Core

### Definition

The architectural layer responsible for providing permanent shared capabilities.

---

## Business

### Definition

The architectural layer responsible for creating organizational value through the consumption of Core capabilities.

---

## Workplace

### Definition

The operational environment in which participants perform professional work.

A Workplace is an architectural environment.

It is neither a software application nor a physical office.

---

## Network

### Definition

The architectural layer responsible for enabling collaboration between independent Workplaces.

---

## Application

### Definition

A software implementation that delivers architectural capabilities to end users.

Applications implement architecture.

Applications do not define architecture.

---

# Canonical Object Terminology

The following terms describe architectural objects.

| Term | Definition |
|------|------------|
| Identity | The canonical representation of an architectural participant. |
| Organization | An independent business participant within the ecosystem. |
| Capability | A reusable architectural ability. |
| Knowledge | Structured information validated for professional use. |
| Context | Information describing the environment in which architecture operates. |
| Policy | A formal rule governing architectural behavior. |

These objects are defined architecturally rather than technologically.

---

# Canonical Action Terminology

Architectural responsibilities are expressed through canonical verbs.

| Verb | Architectural Meaning |
|------|------------------------|
| Define | Establish architectural meaning. |
| Provide | Expose reusable capability. |
| Own | Hold architectural responsibility. |
| Operate | Execute professional work. |
| Connect | Enable collaboration. |
| Deliver | Present capabilities through implementations. |

These verbs are normative.

Alternative verbs shall not replace them without architectural approval.

---

# Naming Conventions

Canonical terminology shall follow these conventions.

---

## Rule A

Architecture uses nouns.

Examples:

- Capability
- Workplace
- Identity
- Network

---

## Rule B

Responsibilities use verbs.

Examples:

- Define
- Provide
- Own
- Operate
- Connect
- Deliver

---

## Rule C

Layers use the suffix "Layer" when architectural context requires explicit identification.

Examples:

- Core Layer
- Business Layer
- Network Layer

---

## Rule D

Models use the suffix "Model".

Examples:

- Identity Model
- Capability Model
- Workplace Model

---

## Rule E

Standards use the Architecture Canon numbering scheme.

Examples:

- MAC-0001
- MAC-0002
- MAC-0003

---

# Deprecated Terminology

The following terminology is deprecated.

| Deprecated | Canonical |
|------------|-----------|
| Workspace | Workplace |
| Platform (when referring to the ecosystem) | Ecosystem |
| Module (when describing architectural layers) | Layer |
| System User | Participant |

Deprecated terminology shall not appear in future architectural publications.

---

# Terminology Governance

Canonical terminology may evolve only through formal architectural governance.

The following actions are permitted.

- introduce a new canonical term;
- clarify an existing definition;
- deprecate obsolete terminology.

The following actions are prohibited.

- redefining a canonical term without architectural approval;
- introducing competing terminology for the same concept;
- using product terminology within the Architecture Canon.

---

# Conformance

An architectural artifact conforms to this standard only if:

- canonical terminology is used consistently;
- definitions remain unchanged;
- deprecated terminology is avoided;
- naming conventions are respected.

---

# Authority

MAC-0004 is the authoritative source of architectural terminology within the MarkOrbit ecosystem.

All subsequent specifications, frameworks and implementations shall adopt the vocabulary established by this document.

---

# Revision Policy

Changes to canonical terminology constitute architectural changes.

Editorial revisions shall improve clarity without altering architectural meaning.

---

# Revision History

| Version | Status | Description |
|---------|--------|-------------|
| 1.0.0 | Canonical | First published edition of the Canonical Language. |

---

**End of Document**