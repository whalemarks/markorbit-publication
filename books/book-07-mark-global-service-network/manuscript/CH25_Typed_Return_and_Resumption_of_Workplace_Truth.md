# B07-CH-25 — Typed Return and Resumption of Workplace Truth

## 1. Why Return needs a formal contract

A managed engagement does not end when a provider sends an email or uploads a file.

The network must return a source-qualified, typed result that the Originating Workplace and relevant Owning Service can validate.

```text
Execution Provider Workplace
→ Return Envelope
→ MGSN validation and governance checks
→ Originating Workplace review
→ Owning Service state decision
```

## 2. Return Envelope

A Return Envelope should identify:

- engagement and route;
- provider and responsible Workplace;
- return type;
- claimed outcome;
- milestone or completion status;
- source and evidence;
- official or third-party identifiers;
- dates and deadlines;
- unresolved exceptions;
- confidence or verification state;
- required next action;
- restrictions on use or disclosure.

The envelope is a governed transport and interpretation structure. It is not the formal Matter state itself.

## 3. Typed outcomes

Typical Return types include:

- accepted instruction;
- filed or submitted;
- filing receipt received;
- official fee paid;
- office action or objection received;
- response filed;
- publication occurred;
- registration granted;
- certificate received;
- rejected or refused;
- withdrawn or cancelled;
- correction required;
- provider unable to complete;
- unknown external outcome.

Each type should define required evidence and downstream handling.

## 4. Source qualification

The Return must state what supports the claimed result.

```text
official source
provider declaration
provider work product
third-party source
customer-supplied evidence
operator observation
unknown source
```

An official receipt and a provider statement are not equivalent, even when they describe the same event.

## 5. Validation before formal-state mutation

The Originating Workplace may validate:

- whether the Return belongs to the correct customer and matter;
- whether the scope matches the accepted engagement;
- whether documents are complete;
- whether dates and identifiers are plausible;
- whether exceptions need customer communication;
- whether a follow-up task is required.

The Owning Service then determines whether the Return is sufficient to mutate formal state.

```text
Return received
≠ Return accepted
≠ formal state changed
```

## 6. Provisional and unknown results

External professional work often produces incomplete or delayed evidence.

The system must support:

- provisional result;
- pending official confirmation;
- evidence incomplete;
- disputed result;
- source conflict;
- unknown outcome.

Unknown must remain a valid state. It must not be silently converted into success or failure merely to close the engagement.

## 7. External route continuity

R1 external routes can return evidence through the External Route Evidence Bridge.

The system should preserve that:

- the provider may not be an MGSN participant;
- the platform may not have governed procurement or fulfillment;
- evidence quality may be lower or harder to verify;
- the Originating Workplace remains responsible for external-route continuity.

MGSN can help structure and validate the Return without misrepresenting the external relationship as a managed engagement.

## 8. Resumption of Workplace truth

The purpose of Return is to resume work inside the Originating Workplace.

A validated Return may trigger:

- Matter state update;
- new Task or deadline;
- customer communication;
- financial reconciliation;
- Evidence retention;
- follow-up instruction;
- renewal or maintenance planning;
- incident or dispute handling;
- Trust evaluation candidate.

These actions occur through the appropriate Product and Owning Service, not inside the Return record alone.

## 9. Completion and closure

An engagement should close only when the controlled completion conditions are met.

Possible closure states include:

- completed and accepted;
- completed with outstanding follow-up;
- cancelled before execution;
- partially completed;
- replaced;
- disputed;
- externally continued;
- outcome unknown.

Closure must not delete the evidence, relationship provenance, incident history or reconciliation trail required for later audit.

## 10. The full managed route

The completed product chain is:

```text
Originating Workplace
→ Capability Need Projection
→ Candidate Route Set
→ user-confirmed route
→ Provider Allocation and Acceptance
→ Managed Network Engagement
→ funds and fulfillment controls
→ typed Return
→ Workplace and Owning Service validation
→ resumed business continuity
```

MGSN therefore does not take ownership of the originating business. It provides a governed global execution bridge and returns control to the Workplace with evidence and context intact.

## 11. Product boundary

This chapter defines Return semantics and validation boundaries. It does not authorize automatic Matter mutation, automatic legal conclusions, official-source action, payment movement or production integration.
