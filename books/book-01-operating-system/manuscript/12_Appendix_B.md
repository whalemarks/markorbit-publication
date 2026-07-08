# Appendix B

# Publication Map

> *Ideas become architecture.*
>
> *Architecture becomes publications.*
>
> *Publications become implementation.*

---

# Purpose

The MarkOrbit ecosystem is not documented by a single book.

No single publication can adequately explain its philosophy, architecture, implementation and evolution.

Instead, MarkOrbit is documented through a structured publication system.

Each publication has a single responsibility.

Together they form one coherent body of knowledge.

This appendix explains how those publications relate to one another.

---

# One Knowledge System

The MarkOrbit Publications are designed as a layered knowledge system rather than a collection of independent books.

Each publication answers a different question.

Each builds upon the publications before it.

Each avoids repeating concepts that have already been established.

The result is a knowledge architecture that evolves consistently over time.

```
                     MarkOrbit Publications

                              │
        ┌─────────────────────┼─────────────────────┐
        │                     │                     │
   Philosophy           Architecture         Implementations
        │                     │                     │
        ▼                     ▼                     ▼
      Book 1              Book 2–3             Book 4+
```

Book 1 establishes the language.

Subsequent publications expand that language.

---

# Publication Layers

The publication system is organised into four architectural layers.

```
Layer 1
Vision

↓

Layer 2
Architecture

↓

Layer 3
Frameworks

↓

Layer 4
Implementations
```

Each layer has different responsibilities.

Confusing these responsibilities leads to inconsistent architecture.

Separating them enables long-term evolution.

---

# Layer One

# Vision

The first layer explains *why* the ecosystem exists.

It introduces:

- industry evolution;
- operating system thinking;
- ecosystem architecture;
- first principles;
- long-term vision.

This layer deliberately avoids implementation details.

Its purpose is to establish a shared understanding.

---

## Book 1

### MarkOrbit

**The Operating System for Global Brand Services**

Responsibilities:

- explain the industry problem;
- establish architectural thinking;
- define the operating philosophy;
- introduce canonical terminology;
- provide the conceptual foundation for all future publications.

Question answered:

> **Why does the industry need an operating system?**

---

# Layer Two

# Architecture

Once the vision has been established, architecture can be defined.

Architecture explains responsibilities.

Relationships.

Boundaries.

Capabilities.

It intentionally remains independent of products.

---

## Book 2

### MarkOrbit Core Specification

Responsibilities:

- define the Core architecture;
- specify architectural responsibilities;
- establish governance;
- define canonical models;
- provide the single architectural source of truth.

Question answered:

> **What is the architecture?**

---

# Layer Three

# Frameworks

Frameworks explain reusable operating environments built upon the Core.

Unlike architecture, frameworks describe patterns that many implementations may adopt.

---

## Book 3

### Workplace Framework

Responsibilities:

- define the Workplace model;
- explain organisational operating environments;
- establish reusable business capabilities;
- define Workplace lifecycle and governance.

Question answered:

> **How does an organisation operate?**

---

# Layer Four

# Implementations

Implementations apply the architecture and frameworks to specific products.

Each implementation has its own audience.

Its own objectives.

Its own release cycle.

Implementations may evolve rapidly while preserving architectural consistency.

---

## Book 4

### MarkReg

Responsibilities:

The official Workplace operated by the MarkOrbit ecosystem.

Demonstrates best practices.

Validates architecture.

Provides reference implementations.

Question answered:

> **How does the official Workplace operate?**

---

## Book 5

### MarkOrbit Lite

Responsibilities:

Professional Workplace for trademark agencies, law firms and independent service providers.

Supports independent operation while remaining compatible with the operating system.

Question answered:

> **How can organisations build their own Workplace?**

---

## Book 6

### Mark Global Service Network (MGSN)

Responsibilities:

Defines ecosystem collaboration.

Explains service routing.

Describes capability exchange.

Establishes governance for cross-organisational cooperation.

Question answered:

> **How do Workplaces collaborate globally?**

---

# Knowledge Dependencies

The publication system follows a deliberate dependency model.

```
Book 1

↓

Book 2

↓

Book 3

↓

Book 4
Book 5
Book 6
```

Knowledge flows downward.

Dependencies do not.

For example:

Book 4 assumes knowledge introduced in Book 3.

Book 3 assumes knowledge introduced in Book 2.

Book 2 assumes concepts established by Book 1.

Higher layers never depend upon implementation.

---

# Publication Responsibilities

Each publication owns one primary responsibility.

| Publication | Primary Responsibility |
|-------------|------------------------|
| Book 1 | Vision |
| Book 2 | Core Architecture |
| Book 3 | Workplace Framework |
| Book 4 | Official Workplace |
| Book 5 | Professional Workplace |
| Book 6 | Global Collaboration |

No publication should duplicate another.

If a concept belongs to Book 2, later books should reference it rather than redefine it.

This principle keeps the publication system coherent.

---

# Relationship to Specifications

Books are only one part of the MarkOrbit knowledge system.

They coexist with specifications, governance documents and implementation repositories.

```
Constitution

↓

Books

↓

Specifications

↓

Reference Implementations

↓

Products
```

Each artefact serves a different purpose.

Books explain.

Specifications define.

Implementations validate.

Products deliver.

---

# The Evolution of the Publication System

The publication system is designed to evolve continuously.

New books may be introduced.

Existing books may receive new editions.

Architectural ideas may mature.

Implementation guidance may expand.

However, one principle remains constant.

Earlier publications establish foundations.

Later publications build upon them.

Knowledge evolves through extension rather than replacement.

---

# A Living Library

The MarkOrbit Publications are intended to become more than documentation.

They form the permanent knowledge library of the ecosystem.

Every edition captures the current understanding of architecture.

Every subsequent edition refines that understanding.

Over time, the publication system becomes the collective memory of the ecosystem itself.

The books therefore serve not only today's readers, but future architects, organisations and contributors.

---

# Closing

Book 1 is intentionally the beginning rather than the destination.

It introduces the questions.

The publications that follow explore the answers in increasing depth.

Together they describe an ecosystem that is expected to evolve for decades while remaining guided by one architectural philosophy.

That philosophy is expressed through many books.

But it speaks with one language.

---

> **One Vision.**

> **One Architecture.**

> **One Knowledge System.**

> **Many Publications.**