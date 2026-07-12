# Status Contracts

## Purpose
Define enforceable shapes for status transition requests, decisions, and owning-Service results.

## Canonical ownership
A Status Contract consumes a Controlled State Value Specification. It defines request, validation and result shape. It does not own current state. It does not perform mutation. It does not create a separate status source of truth.

## Directory inventory
- `status-transition-contract.md` shared request, decision, and result shape.
- `trademark-status-contract.md`, `order-status-contract.md`, `matter-status-contract.md`, `task-status-contract.md` domain constraints.

## Contract-to-spec relationship
Canonical values and transition matrices remain in `core-specs/controlled-state-values/`.

## Status transition boundary
Allowed decisions route to owning Services only.

## Fixture relationship
Fixtures in `../fixtures/status-workflow/` demonstrate expected contract behavior.

## Versioning rule
Contract versions may constrain but not silently expand canonical state truth.

## Prohibited use
Do not treat status as an independent Core Object, workflow state, runtime engine, database schema, or external action authorization.
