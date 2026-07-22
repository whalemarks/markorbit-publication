# CH08 — References, Identity Continuity and Resolution Candidates

## Shared systems must exchange identity without pretending certainty

MarkOrbit will encounter the same real-world party, trademark, matter, document or event through many sources.

A company may appear under:

- an English name;
- a Chinese name;
- a transliteration;
- a historical name;
- a typo in an official record;
- a shortened commercial name;
- several registration identifiers.

The platform needs continuity across these records, but it must not merge them merely because they look similar.

Book 02 therefore distinguishes:

```text
Identifier
Reference
Alias
Source Record
Resolution Candidate
Canonical Record
```

## Identifier

An Identifier is a value issued or assigned within a defined namespace.

Examples include:

- internal UUID;
- company registration number;
- trademark application number;
- registration number;
- provider identifier;
- document hash;
- email address;
- external system record key.

Every Identifier should preserve its namespace and issuing or owning context.

```text
same string
≠ same identifier
```

Application number `12345` in one jurisdiction is not the same identifier as `12345` in another. An email address is not a permanent person identifier. A local database key has no meaning outside its source unless wrapped in a typed reference.

## Reference

A Reference points to an object without transferring ownership or copying its entire state.

A robust Reference should identify:

- object type;
- identifier and namespace;
- Owning Service or source context;
- version where required;
- resolution status;
- access and purpose constraints where relevant.

References allow Products and Workplaces to coordinate while preserving formal-state ownership.

```text
Reference
≠ duplicated authoritative record
≠ permission to mutate source state
```

A Lite Listing may reference a Trademark record. A MarkReg Matter may reference an Applicant Organization. Execution may reference a Work Package and Evidence set. None needs to become the universal owner of the referenced object.

## Alias

An Alias records an alternative label associated with a candidate or accepted identity.

Aliases may include:

- former names;
- translated names;
- transliterations;
- abbreviations;
- trade names;
- known misspellings;
- source-specific representations.

An Alias should preserve source, time and context. It should not silently replace the preferred or official name.

```text
Alias observed
≠ legal-name change verified
```

## Source Record

A Source Record preserves what a particular source said at a particular time.

It may contain conflicting or outdated information. That does not make it useless. The conflict itself may be important evidence.

A Source Record should preserve:

- source identity;
- retrieval or receipt time;
- source version or publication date;
- raw or normalized value;
- extraction method;
- jurisdiction and record type;
- confidence and known limitations.

Source Records should not be overwritten to match the current canonical interpretation.

```text
normalization
≠ historical rewriting
```

## Resolution Candidate

A Resolution Candidate proposes that two or more records refer to the same real-world entity or that one record should link to a canonical object.

It should include evidence such as:

- matching registration number;
- name similarity;
- shared address;
- shared directors or contacts;
- official change record;
- transaction or chain-of-title evidence;
- contradictory signals;
- intended purpose of the resolution.

Resolution confidence should not be represented as one unexplained score. The platform should distinguish exact identifiers, strong supporting evidence, weak similarities and material conflicts.

```text
probable match for search grouping
≠ verified identity for legal action
```

The same candidate may be accepted for analytics and rejected for filing or transaction use.

## Canonical Record

A Canonical Record is an accepted platform representation for a defined purpose and authority context.

Canonical does not mean the platform claims universal truth. It means:

- a responsible service accepted the resolution;
- the evidence and decision are recorded;
- the version is identifiable;
- corrections and supersession are possible;
- downstream references can rely on the declared scope.

A canonical Organization record may still link to conflicting Source Records and unresolved aliases.

## Merge must be reversible

Identity merges are high-impact because they can combine:

- customer histories;
- confidential documents;
- trademark portfolios;
- provider performance;
- payment records;
- marketing permissions;
- conflicts and professional relationships.

Therefore a merge should preserve:

- original objects and identifiers;
- merge decision and authority;
- evidence used;
- affected relationships and projections;
- undo or corrective path;
- downstream notifications.

```text
merged view
≠ source records destroyed
```

## Split and correction

The system must also support the opposite case: one apparent identity later proves to be several distinct parties.

A split should identify which facts, relationships and evidence belong to each resulting object. It should not simply clone the entire record.

Historical actions must remain attributable to the identity representation known at the time, while corrected references govern future use.

## Identity continuity through change

Continuity should survive legitimate change without erasing history.

Examples include:

- company name change;
- merger;
- conversion of legal form;
- address change;
- assignment of a trademark;
- professional moving between firms;
- customer relationship transfer.

These events are not all aliases. Some change the legal or commercial party. Core must allow typed continuity and succession relationships instead of treating every similarity as sameness.

```text
name changed
≠ owner changed

owner changed
≠ historical owner deleted
```

## AI and entity resolution

AI can generate candidates, extract identifiers and explain evidence. It should not silently merge formal identities.

AI output must preserve:

- model and method;
- input records;
- confidence decomposition;
- contradictions;
- intended use;
- required human or authoritative review.

## Constitutional rule

```text
Identifiers locate records within namespaces.
References connect systems without transferring ownership.
Source Records preserve what was observed.
Resolution Candidates preserve uncertainty.
Canonical Records record accepted identity for a declared purpose.
```

This architecture gives MarkOrbit cross-product continuity without converting approximate similarity into legal or commercial certainty.