# Appendix H — Human–AI Collaboration Index

## Role Boundary

| Actor | May do | May not do independently |
|---|---|---|
| AI assistant | extract, summarize, compare, draft, identify gaps, prepare questions | approve, send, submit, pay, mutate protected state, define professional truth |
| Agent | sequence permitted preparation steps and call approved tools inside an authority envelope | expand its authority, bypass gates, satisfy Human Review, emit governed Events |
| Human reviewer | make accountable decisions within eligibility and scope | bypass Permission, Policy, version or owning-Service rules |
| Owning Service | validate and perform approved authoritative effects | acquire professional judgment not granted by its contract |
| Workflow | coordinate context, gates and Service calls | own Core mutation or Event truth |

## Handoff Package

A governed Human–AI handoff should preserve:

- purpose;
- subject and versions;
- source references;
- AI-assisted outputs;
- unresolved issues;
- limitations;
- required Human Review;
- prohibited actions;
- audit correlation.

## Agent Controls

- explicit authority envelope;
- least-privilege data and tools;
- source and output attribution;
- prompt-injection resistance;
- version and context freshness;
- idempotency and safe retry;
- protected-action refusal;
- pause and stop controls;
- Human Review before protected action.

## Primary References

- [Human–AI Execution Handoff](../manuscript/B03-CH-16_Human_AI_Execution_Handoff.md)
- [Human Review Governance](../manuscript/B03-CH-28_Human_Review_Governance.md)
- [Agent-Assisted Execution Governance](../manuscript/B03-CH-29_Agent-Assisted_Execution_Governance.md)
