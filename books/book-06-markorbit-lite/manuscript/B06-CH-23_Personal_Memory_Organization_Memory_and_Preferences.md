# B06-CH-23 — Personal Memory, Organization Memory and Preferences

## Chapter Role

This chapter defines how MarkOrbit Lite may preserve continuity for an individual professional and a small Organization without treating every observed behavior as permission, every personal habit as shared policy, or every AI inference as memory.

The central distinctions are:

```text
observed behavior
≠ accepted preference

personal memory
≠ Organization memory

memory candidate
≠ formal business truth
```

---

## 1. Why continuity matters

Independent professionals and small trademark agencies repeatedly lose context when work moves between:

- different days;
- different clients;
- email, chat and document systems;
- local and cloud environments;
- the professional and an assistant;
- Lite and MarkReg;
- one team member and another;
- one case and a later similar case.

Useful continuity may include:

- preferred writing style;
- common jurisdictions;
- preferred explanation depth;
- recurring client constraints;
- trusted templates;
- review habits;
- pricing presentation preferences;
- local-agent communication patterns;
- typical follow-up intervals;
- known corrections;
- explicit do-not-use rules.

Without continuity, every interaction starts from zero.

With uncontrolled continuity, however, the Product may:

- remember incorrect facts;
- expose private information;
- spread one person's habit to the whole Organization;
- preserve outdated instructions;
- infer sensitive preferences;
- reuse a client-specific rule in the wrong context;
- create authority the user never granted.

Therefore, memory must be governed as carefully as action.

## 2. Memory is not passive storage

A folder, note or database row is not automatically a governed memory.

A useful memory record must answer:

- what is being remembered;
- who proposed it;
- what source supports it;
- whose scope it applies to;
- for what purpose it may be used;
- whether it is a preference, fact, lesson or instruction;
- who accepted it;
- when it should be reviewed;
- how it may be corrected or deleted;
- whether AI may use it;
- whether it may cross into Organization context.

```text
stored information
≠ accepted memory
≠ permission for every use
```

## 3. ML-M03 — Preference Candidate

A Preference Candidate is a proposed personal preference inferred or stated during Product use.

Examples:

- prefer concise English emails;
- show costs in both USD and RMB;
- avoid legal jargon in client-facing explanations;
- present three recommended options rather than one;
- require a source link before using market data;
- prefer manual confirmation before any communication;
- use a specific signature name;
- default to bilingual work products for selected clients.

A Preference Candidate may be created from:

- explicit user instruction;
- repeated correction;
- repeated choice;
- accepted Product configuration;
- reviewed import from an earlier system.

But repeated observation alone is not acceptance.

`ML-SCN-21` requires:

```text
repeated behavior observed
→ Preference Candidate
→ explicit acceptance and scope
≠ silent permanent preference
```

## 4. Preference scope must be precise

A preference may apply to:

- one session;
- one client;
- one Organization;
- one communication channel;
- one language;
- one work-product type;
- one jurisdiction;
- all personal use in Lite.

For example:

```text
“Use concise English”
```

may mean:

- only for emails to foreign associates;
- not for legal submissions;
- not for client reports;
- not for internal Chinese notes.

A useful preference should therefore include:

```text
subject
+ scope
+ purpose
+ exclusions
+ source
+ accepted_by
+ effective date
+ review/expiry condition
```

## 5. Explicit preference versus professional requirement

A user preference cannot override:

- law;
- professional responsibility;
- Organization policy;
- required Review;
- client instructions;
- destination contract;
- Evidence integrity;
- external platform requirements.

```text
user prefers no Review
≠ Review may be skipped
```

Similarly:

```text
user prefers a shorter explanation
≠ material risk may be omitted
```

Preferences personalize the Product within governing constraints.

## 6. ML-M04 — Personal Memory Candidate

A Personal Memory Candidate supports continuity for one user.

Examples:

- a personal checklist learned from prior work;
- a preferred sequence for reviewing an OA;
- a reminder that a particular client wants fees shown separately;
- a private note about which drafts require extra attention;
- a personally trusted source;
- a correction to the user's own recurring wording;
- a local/private working convention.

Personal Memory is not automatically visible to:

- colleagues;
- the Organization administrator;
- other Workplaces;
- MGSN providers;
- clients;
- public content generation.

Its default scope should be narrow.

## 7. Personal memory is not identity authority

Lite may support a personal AI continuity layer, but it must not claim to be the user.

```text
Personal Memory
≠ human identity
≠ legal signature
≠ professional authority
≠ consent to act externally
```

A Product may use accepted personal memory to prepare a draft.

It may not use that memory to send, file, approve, sign or represent the user without the required action controls.

## 8. ML-M05 — Organization Memory Candidate

An Organization Memory Candidate is proposed shared operating knowledge.

Examples:

- an approved intake checklist;
- a standard explanation of service stages;
- a preferred quotation structure;
- an internal review rule;
- a provider-selection constraint;
- an approved email template;
- a team lesson from a recurring error;
- an escalation rule;
- an approved terminology standard.

Organization memory affects more people and more work.

Therefore it requires stronger governance than personal memory.

`ML-SCN-22` requires:

```text
promotion to Organization memory
→ provenance
+ Organization Review
+ scope
+ owner
+ correction/retirement path
```

## 9. Personal preference must not become Organization policy silently

A common failure path is:

```text
one user repeatedly chooses a format
→ system applies it to the team
```

This is unsafe because the behavior may reflect:

- one client's preference;
- a temporary project;
- an accessibility need;
- a personal habit;
- a mistake;
- an exception approved for one Matter.

The proper path is:

```text
personal behavior
→ Preference Candidate
→ explicit personal acceptance
→ optional Organization Memory Candidate
→ Organization Review
→ accepted shared rule or rejection
```

## 10. Organization memory is not canonical Knowledge

Organization memory may be valid only for:

- one firm's operating process;
- its pricing presentation;
- its internal review structure;
- its preferred provider relationships;
- its risk tolerance;
- its client-service style.

Canonical Knowledge aims to support broader, governed professional understanding.

```text
Organization memory
≠ universal professional truth
≠ canonical Knowledge
```

An internal rule such as:

> Always have a second person review quotations above a threshold.

may be a sound Organization policy but not a universal legal rule.

## 11. Facts should remain sourced projections

Memory should not be used to copy formal business facts into an uncontrolled parallel store.

Examples:

- Customer legal name;
- trademark status;
- deadline;
- Matter owner;
- provider qualification;
- invoice balance;
- official filing result.

These should remain projections from the relevant Owning Service.

A memory record may preserve a user-facing continuity note, but it should not replace the source.

```text
“Client often asks for bilingual reports”
= possible preference/memory

“Client legal name is X”
= formal Customer fact from source service
```

## 12. Memory and data classification

Every memory candidate should retain classification.

Possible classifications include:

- Personal Private;
- Organization Internal;
- Client Restricted;
- Matter Restricted;
- Local Only;
- approved for wider reuse.

A memory cannot be broadened merely because it is useful.

```text
useful to team
≠ authorized to share with team
```

## 13. Local and private memory

Some professionals may keep:

- personal notes;
- local templates;
- private client context;
- archived correspondence;
- local knowledge collections.

Lite may retrieve or use such material under a hybrid-minimization model.

But:

```text
local readability
≠ synchronization permission
≠ Organization visibility
≠ AI training permission
≠ disclosure authority
```

A local memory candidate should record:

- location or source reference;
- whether content may leave the device;
- whether only derived context may cross;
- whether the user approved synchronization;
- how revocation works.

## 14. Memory acceptance controls

Before acceptance, Lite should show:

- the proposed memory statement;
- source and reason;
- confidence;
- scope;
- intended uses;
- prohibited uses;
- data classification;
- expiry/review date;
- whether AI may use it;
- whether it may be shared;
- who will own correction.

The user or Organization reviewer may:

```text
accept
edit and accept
limit scope
set expiry
defer
reject
delete
promote as a different candidate
```

## 15. Conflicting memories

Memory can conflict.

Examples:

- personal preference says “concise”;
- client preference says “detailed”;
- Organization policy requires a full risk section;
- destination form limits length.

The Product should not resolve conflicts by using the newest record automatically.

A useful precedence model is:

```text
law / professional requirement / destination constraint
→ client or Matter instruction
→ Organization policy
→ accepted personal preference
→ Product default
```

The exact hierarchy may vary by purpose, but it must be explainable.

## 16. Memory freshness and expiry

Some memories are durable:

- preferred tone;
- personal formatting choice;
- approved internal terminology.

Others should expire quickly:

- temporary client instruction;
- current negotiation preference;
- provider availability;
- office practice;
- pricing;
- one-project exception.

A memory may be:

```text
active
review_due
stale
superseded
revoked
retired
```

Stale memory should not silently influence consequential work.

## 17. Correction and deletion

Accepted memory must remain correctable.

A Correction Record should identify:

- the original memory;
- what was wrong;
- affected outputs;
- whether future use is blocked;
- whether derived Assets or Artifacts require review;
- whether the memory should be replaced or deleted.

Deletion should consider:

- legal retention requirements;
- audit needs;
- downstream copies;
- local and synchronized versions;
- derived work products;
- Organization policy.

Deletion from the user interface alone is not always complete erasure.

## 18. Example: communication style

Suppose a user repeatedly shortens foreign-associate emails.

Unsafe behavior:

```text
system infers “always use short email”
→ applies it to every client and legal submission
```

Controlled behavior:

```text
repeated edits observed
→ Preference Candidate:
   concise English emails to foreign associates
→ user reviews scope
→ accepts for email drafts only
→ legal submissions excluded
→ client-specific contrary preferences override
```

## 19. Example: a team checklist

A missed applicant-ownership issue occurs twice.

Possible chain:

```text
Correction Records
→ Case Lesson Candidate
→ Organization Memory Candidate:
   verify applicant legal identity before MarkReg Handoff
→ Organization Review
→ accepted checklist rule
→ use observed
→ later correction or retirement if process changes
```

This is capability accumulation with governance.

## 20. Memory should reduce friction, not hide judgment

Good memory helps Lite:

- avoid asking the same settled preference repeatedly;
- prepare better drafts;
- surface relevant warnings;
- preserve continuity across sessions;
- support small-team consistency;
- identify when a rule no longer fits.

Bad memory makes invisible decisions on the user's behalf.

The Product should expose when memory materially influenced:

- a recommendation;
- a work product;
- a ranking;
- a destination choice;
- a suppression;
- a review requirement.

## 21. Chapter conclusion

The proper memory model is:

```text
observation or explicit instruction
→ Preference / Personal / Organization Memory Candidate
→ visible source and scope
→ explicit acceptance or Organization Review
→ bounded use
→ correction, expiry or retirement
```

Personal continuity, Organization consistency and professional governance are related but not interchangeable.

The next chapter explains how reviewed lessons and memories may become reusable Assets or proposed contributions to governed Knowledge.
