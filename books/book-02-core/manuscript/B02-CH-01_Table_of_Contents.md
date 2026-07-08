# Book 02

# 01 — Table of Contents

**Book Title:** MarkOrbit Core Specification

**Chapter ID:** B02-CH-01

**Chapter Title:** Table of Contents

**Part:** Front Matter

**Chapter Type:** Foundation

**Status:** Draft

**Version:** 0.1.0

**Owner:** MarkOrbit Publications Editorial Board

---

# Table of Contents

## Front Matter

**00 Preface**

**01 Table of Contents**

---

# Part I — Core Foundation

## 02 Why Core Exists

Explains why the MarkOrbit ecosystem requires a shared Core instead of disconnected products, tools and workflows.

## 03 Core Position

Defines the position of the MarkOrbit Core within the publication series, architecture system and software implementation path.

## 04 Core Boundary

Defines what belongs to the Core and what belongs to Workplace, Product, `core-specs/` or implementation.

## 05 Core Principles

Defines the principles that govern Core design, including domain before feature, capability before function and governance before automation.

## 06 From Professional OS to Core Kernel

Translates the Professional Operating System described in Book 01 into the Core architecture specified in Book 02.

## 07 Professional Value Flow

Defines how the Core supports the professional flow from reality to facts, understanding, judgment, action, coordination and experience.

## 08 Ontology and Domain Classification

Defines the ontology and domain classification rules that distinguish reality objects, system objects, execution objects and collaboration objects.

---

# Part II — Core Kernel Architecture

## 09 Core Kernel Overview

Provides the overall architecture of the MarkOrbit Core and explains how models, domains, objects, services, primitives, contracts and consumption rules fit together.

## 10 Architecture Layers

Defines the architecture layers used by Book 02, including principles, Core, business responsibility, execution primitives, integration contracts and products.

## 11 Responsibility Flow

Defines how responsibility flows through the system and prevents products, workplaces or AI agents from redefining the Core.

## 12 Canonical Models

Defines the canonical models owned by Book 02, including Identity, Capability, Knowledge, Business Responsibility, Workplace and Network models.

## 13 Core Domain Architecture

Defines what a Core Domain is, how domains are classified and how detailed domain specifications are moved into `core-specs/domains/`.

## 14 Core Object Architecture

Defines the rules for Core Objects, including persistence, referenceability, traceability, auditability, lifecycle and product consumption.

## 15 Core Service Architecture

Defines the rules for Core Services as reusable capabilities exposed by the Core.

## 16 Core Execution Primitives

**Events, Tasks, State, Context and Workflow Contracts**

Defines the execution primitives and workflow contracts provided by the Core while preserving the boundary that Workplace operates workflow execution.

## 17 Core Contract Architecture

Defines the contract architecture of the Core, including Data, API, Event, Agent, Workflow and Consumption Contracts.

---

# Part III — Core Specification System

## 18 Identity Specification

Defines how identity-related Core concepts are specified, including persons, organizations, users, partners, agents, service providers and workplace identities.

## 19 Capability Specification

Defines how reusable Core Capabilities are specified and how they may be executed by services, workflows or governed AI agents.

## 20 Knowledge Specification

Defines how professional knowledge becomes a Core asset through sources, nodes, relationships, validation and retrieval.

## 21 Business Responsibility Specification

Defines business ownership, commercial responsibility, delegation, authorization, value creation and business relationships without entering product pricing or commercial packages.

## 22 Domain Specification

Defines the standard structure for detailed Core Domain specifications.

## 23 Object Specification

Defines the standard structure for detailed Core Object specifications.

## 24 Service Specification

Defines the standard structure for detailed Core Service specifications.

## 25 Event Specification

Defines the standard structure for Core Event specifications, including naming, source, trigger, payload, subscription, replay and audit.

## 26 AI Capability and Agent Governance Specification

Defines how AI capabilities and agents are governed by identity, permission, knowledge, context, audit and human review.

## 27 Core Consumption Specification

Defines how later books and products consume the Core without redefining its objects, services, events or meanings.

---

# Part IV — Core Execution Boundary

## 28 Core MVP Boundary

Defines what belongs to the Core MVP and what is excluded from the initial implementation boundary.

## 29 MVP Domain Priority

Defines the phased implementation priority for Core Domains.

## 30 MVP Execution Matrix

Maps MVP domains to execution assets such as database tables, domain models, services, APIs, events, AI capabilities, workflow contracts and Codex tasks.

## 31 Codex Implementation Roadmap

Defines how Codex should read Book 02, `core-specs/`, indexes and planning documents to generate implementation tasks while preserving Core boundaries.

---

# Appendices

## Appendix A — Glossary

Defines official Book 02 terminology.

## Appendix B — Core Domain Index

Indexes all Core Domains and their detailed specification locations.

## Appendix C — Core Object Index

Indexes all Core Objects and their domain ownership.

## Appendix D — Core Service Index

Indexes all Core Services and their capability responsibilities.

## Appendix E — Event Index

Indexes all Core Events and their sources, triggers and consumers.

## Appendix F — API Index

Indexes the Core API surface.

## Appendix G — Agent Index

Indexes AI Agents, related capabilities, knowledge sources, risk levels and human review requirements.

## Appendix H — Codex Task Index

Indexes Codex implementation tasks derived from approved Book 02 and `core-specs/` assets.

---

# Structural View

```text
Book 02 — MarkOrbit Core Specification

00 Preface
01 Table of Contents

Part I — Core Foundation
    02 Why Core Exists
    03 Core Position
    04 Core Boundary
    05 Core Principles
    06 From Professional OS to Core Kernel
    07 Professional Value Flow
    08 Ontology and Domain Classification

Part II — Core Kernel Architecture
    09 Core Kernel Overview
    10 Architecture Layers
    11 Responsibility Flow
    12 Canonical Models
    13 Core Domain Architecture
    14 Core Object Architecture
    15 Core Service Architecture
    16 Core Execution Primitives
       Events, Tasks, State, Context and Workflow Contracts
    17 Core Contract Architecture

Part III — Core Specification System
    18 Identity Specification
    19 Capability Specification
    20 Knowledge Specification
    21 Business Responsibility Specification
    22 Domain Specification
    23 Object Specification
    24 Service Specification
    25 Event Specification
    26 AI Capability and Agent Governance Specification
    27 Core Consumption Specification

Part IV — Core Execution Boundary
    28 Core MVP Boundary
    29 MVP Domain Priority
    30 MVP Execution Matrix
    31 Codex Implementation Roadmap

Appendices
    A Glossary
    B Core Domain Index
    C Core Object Index
    D Core Service Index
    E Event Index
    F API Index
    G Agent Index
    H Codex Task Index
```

---

# Reading Guide

## For Strategic Readers

Read:

- 00 Preface
- 02 Why Core Exists
- 03 Core Position
- 04 Core Boundary
- 06 From Professional OS to Core Kernel
- 28 Core MVP Boundary

## For Product Managers

Read:

- 03 Core Position
- 04 Core Boundary
- 05 Core Principles
- 07 Professional Value Flow
- 13 Core Domain Architecture
- 27 Core Consumption Specification
- 29 MVP Domain Priority
- 30 MVP Execution Matrix

## For Architects

Read:

- 08 Ontology and Domain Classification
- 09 Core Kernel Overview
- 10 Architecture Layers
- 11 Responsibility Flow
- 12 Canonical Models
- 13 Core Domain Architecture
- 14 Core Object Architecture
- 15 Core Service Architecture
- 16 Core Execution Primitives
- 17 Core Contract Architecture

## For Developers and Codex Workflows

Read:

- 22 Domain Specification
- 23 Object Specification
- 24 Service Specification
- 25 Event Specification
- 26 AI Capability and Agent Governance Specification
- 30 MVP Execution Matrix
- 31 Codex Implementation Roadmap
- Appendices B–H

## For Product Publications

Book 03, Book 04, Book 05 and Book 06 shall use Book 02 as the Core foundation.

They may consume, specialize and operationalize the Core.

They shall not redefine the Core.

---

# Chapter Group Responsibility

| Section | Primary Responsibility |
|---------|------------------------|
| Front Matter | Establish publication context and navigation |
| Part I | Establish Core purpose, position, boundary and philosophical continuity |
| Part II | Define Core architecture and responsibility structure |
| Part III | Define the Core specification system |
| Part IV | Define MVP and implementation boundary |
| Appendices | Provide indexes for execution, review and development |

---

# Editorial Note

This table of contents reflects **Book 02 TOC v1.2 — Frozen**.

Future changes to chapter structure shall require editorial review.

Minor editorial adjustments may be made during manuscript drafting, but structural changes shall not be made without updating the planning documents.

---

**End of Chapter**
