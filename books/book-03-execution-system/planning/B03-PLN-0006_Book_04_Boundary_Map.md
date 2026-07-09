# B03-PLN-0006_Book_04_Boundary_Map

## Purpose

This scaffold defines the boundary between Book 03 — MarkOrbit Execution System and Book 04 Product System.

## Boundary Principle

Book 03 defines execution. Book 04 defines product surfaces.

Execution patterns may be consumed by products. Products must not redefine execution governance. Workplace is a product surface, not Book 03's subject.

## Book 03 Owns

- Execution patterns
- Execution context
- Workflow coordination
- Task lifecycle
- Review gates
- Communication boundary
- Event trace behavior
- Human-AI handoff
- Execution governance

## Book 04 Owns

- Product surfaces
- Workplace
- Client Portal
- Partner Center
- Provider Network
- API Console
- Plugin/App surfaces
- UI/UX
- Product packaging

## What Book 03 May Reference About Book 04

Book 03 may state that future Book 04 product surfaces can consume approved execution patterns, review gates, communication boundaries, task lifecycle behavior, and human-AI handoff rules.

Book 03 may identify product-surface dependency questions that Book 04 must answer later.

## What Book 03 Must Not Define

- Workplace product specifications.
- Client Portal, Partner Center, Provider Network, API Console, mini-program, plugin, app, or screen specifications.
- UI layouts, screen flows, navigation, components, product packaging, or UX requirements.
- Product-specific implementation code.
- Product authority that bypasses Book 03 execution governance or Book 02 Core contracts.

## Open Questions

- Which execution patterns should Book 04 surfaces consume first?
- Which product surfaces require MVP execution readiness before product drafting?
- Which Book 04 product terms need to be referenced in the Book 03 glossary as external consumers only?
- What product-surface decisions must remain blocked until execution governance is approved?

## Review Checklist

- Confirm Book 03 defines execution only.
- Confirm Book 04 owns product surfaces and UI/UX.
- Confirm Workplace remains a product surface, not Book 03's subject.
- Confirm Book 03 does not create product UI specifications.
- Confirm product surfaces must consume, not redefine, execution governance.

## Next Action

Review this boundary map before Book 03 Round 1 drafting and use it to prevent product-surface content from entering Book 03 chapters.
