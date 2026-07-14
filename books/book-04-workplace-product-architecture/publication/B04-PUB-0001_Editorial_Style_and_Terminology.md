# B04-PUB-0001 — Editorial Style and Terminology

**Status:** Release Candidate 1  
**Applies to:** B04-CH-00 through B04-CH-39 and Book 04 publication assets

## 1. Editorial Objective

Book 04 uses concise professional English to express architecture, authority, and responsibility without turning the manuscript into implementation documentation. Editorial changes may improve clarity and economy but may not alter canonical meaning.

## 2. Language Standard

- Use U.S. English spelling and punctuation.
- Prefer direct sentences and active constructions where authority remains accurate.
- Use one concept per paragraph when defining boundaries.
- Retain short standalone sentences when they function as constitutional locks.
- Avoid unnecessary intensifiers, promotional language, and claims of certainty.
- Use `may`, `should`, and `must` according to their ordinary normative strength.

## 3. Canonical Capitalization

Capitalize defined architecture concepts when used in their Book 04 sense:

`Core`, `Execution`, `Workplace`, `Orbit`, `Product`, `Capability`, `Skill`, `Knowledge`, `Information`, `Intelligence`, `Artifact`, `Document`, `Asset`, `Content`, `Human Review`, `Prepared Action`, `Owning Service`, `Routing`, `Delivery`, `Publish`, `Formalization`, `Assistant`, `Guide`, `AI Agent`, `Local Vault`, and `MGSN`.

Use lowercase when the word is ordinary rather than architectural. For example, an ordinary product is not automatically a MarkOrbit `Product`, and a file is not automatically an `Artifact` or `Document`.

## 4. Canonical Responsibility Language

Use the full constitutional lock when summarizing layer responsibility:

```text
Core defines shared meaning.
Execution governs coordinated work.
Workplace provides authorized organization context.
Products compose focused user journeys.
MGSN connects independent organizational Orbits.
Owning Services change and record formal business facts.
Humans remain professionally accountable.
AI assists under explicit governance.
```

The verb `coordinates` may still describe a particular operational act. It should not replace the full constitutional description of Execution responsibility.

## 5. Required Distinctions

Preserve explicit distinctions where confusion would create authority drift:

```text
Candidate ≠ canonical
Recommendation ≠ decision
Prepared Action ≠ execution
Approval ≠ execution
Human selection ≠ appointment
Appointment ≠ instruction
Provider instruction ≠ provider acceptance
Artifact ≠ Document
Render ≠ approval
Delivery ≠ receipt
Publish ≠ business outcome
Feedback ≠ truth
Trust ≠ universal score
```

## 6. References

- Refer to chapters in this book as `CH00`, `CH01`, and so on.
- Use `B02-CH-XX` and `B03-CH-XX` for exact upstream chapter references.
- Use the full publication name on first reference when ambiguity exists.
- Link figures and publication apparatus by stable IDs.

## 7. Hyphenation

Use the following forms consistently:

- `full-lifecycle`
- `cross-Product`
- `cross-Orbit`
- `organization-specific`
- `purpose-bound`
- `permission-filtered`
- `version-specific`
- `private-first` when used adjectivally; `Private First` for the named principle
- `real-world`
- `long-term`
- `side-effect-free`

## 8. Lists and Code Fences

Lists should contain parallel grammatical forms. Use fenced `text` blocks for constitutional equations, distinctions, and conceptual sequences. Use Mermaid only in figure assets. A conceptual sequence must not be presented as a mandatory universal state model unless the text explicitly establishes one.

## 9. Compression Rule

Remove repetition when it merely restates nearby prose. Retain repetition when it provides one of the following:

- a constitutional lock;
- a chapter-boundary reminder;
- a failure mode;
- a minimum conformance rule;
- a reference summary useful when a chapter is read independently.

Compression must never remove provenance, uncertainty, authority, Review, privacy, or protected-action qualifications.

## 10. Publication Claims

`Release Candidate 1` means architecture and publication finishing have passed the recorded RC checks. It does not mean Product implementation, production deployment, legal compliance, or external protected action has been authorized.
