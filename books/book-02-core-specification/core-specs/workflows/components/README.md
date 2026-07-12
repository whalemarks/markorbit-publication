# Workflow Contract Component Specifications

Workflow Contract owns component definitions.
Workflow Contract Service validates components.
Owning domain Services perform mutations.
Events trace outcomes.
Execution coordinates consumption.

## Inventory

- [Workflow State Definition](workflow-state-definition.md)
- [Workflow Transition Definition](workflow-transition-definition.md)

## Prohibited use

These components must not have global independent component identity, Product UI definition authority, component self-mutation, direct external action execution, or AI silently modifying state/transition definitions.
