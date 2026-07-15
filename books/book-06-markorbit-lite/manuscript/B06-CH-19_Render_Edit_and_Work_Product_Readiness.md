# B06-CH-19 — Render, Edit and Work-Product Readiness

## Chapter status

```text
Book: Book 06 — MarkOrbit Lite
Chapter: B06-CH-19
Part: IV — Professional Work Products
Status: Complete Draft 1 — Owner Accepted on Wave 4 Merge
Primary controls: ML-W07, ML-W08, ML-W10, ML-SCN-14–17
```

## 19.1 A representation is not the professional result

A reviewed Artifact Version may need to become a usable representation:

- PDF;
- image carousel;
- web page;
- downloadable quotation;
- short video;
- audio;
- presentation;
- formatted email body;
- mobile-friendly recommendation page.

The transformation from Artifact Version to representation is Render.

Render makes a result usable in a medium. It does not make the result professionally correct.

```text
Artifact Version
→ Render
→ representation

Render success
≠ factual accuracy
≠ legal approval
≠ publication permission
```

## 19.2 `ML-W07` — Render Request

A Render Request should identify:

- source Artifact Version;
- desired representation;
- format;
- dimensions or duration;
- language;
- brand profile;
- deterministic fields;
- visual/media assets;
- accessibility requirements;
- output purpose;
- destination constraints;
- renderer or capability class;
- expected validation checks;
- cost or entitlement context where relevant.

Example:

```text
Source: Artifact A-12/V2
Representation: customer recommendation PDF
Language: English
Brand: Organization profile OP-3
Required fields: customer name, mark, jurisdiction, options, validity date
Validation: all deterministic fields match V2
Purpose: customer email attachment
```

A request should not rely on an ambiguous instruction such as “make this beautiful.”

## 19.3 Deterministic rendering

Some output elements should be deterministically derived from the selected version:

- customer and Organization names;
- trademark representation;
- serial/registration numbers;
- dates;
- quoted fees;
- selected options;
- required disclaimers;
- version identifier;
- QR code or destination link;
- contact information.

These fields should be validated after rendering.

If a deterministic field differs from the Artifact Version, the Render Result must not be marked ready.

## 19.4 Generative rendering

Generative capabilities may assist with:

- layout suggestions;
- illustrative backgrounds;
- transitions;
- voice delivery;
- visual hierarchy;
- scene composition;
- thumbnail alternatives;
- non-substantive stylistic variants.

Generative rendering must not silently change:

- legal or procedural claims;
- trademark representation;
- customer identity;
- price;
- dates;
- scope;
- approved wording;
- disclosure level;
- call to action.

The more generative freedom a renderer receives, the stronger the comparison and Review controls must be.

## 19.5 `ML-W08` — Render Result

A Render Result should record:

- Render Request reference;
- source Artifact Version;
- renderer/capability and version where relevant;
- output file or representation reference;
- success, partial success or failure;
- validation checks;
- deterministic-field comparison;
- missing media or fonts;
- quality warnings;
- cost/usage observation;
- creation time;
- allowed use;
- next required action.

Possible states include:

```text
rendered_validated
rendered_with_warning
partial
failed
blocked
unsupported
expired
```

## 19.6 Render failure must remain visible

`ML-SCN-15` requires that failed or mismatched rendering remains incomplete.

Examples:

- customer name omitted;
- price pulled from the wrong version;
- logo distorted;
- trademark image replaced;
- subtitle missing;
- video duration cut off the disclaimer;
- unsupported characters shown incorrectly;
- PDF pages missing;
- output link expired;
- image rights unresolved.

A commercial entitlement is not fulfilled merely because a file exists.

```text
file created
≠ requested work product delivered
```

## 19.7 Edit as a governed transformation

Edit may include:

- cropping;
- trimming;
- subtitle correction;
- pause removal;
- layout adjustment;
- brand-element placement;
- image replacement;
- audio cleanup;
- compression;
- accessibility improvement;
- correction of factual text.

Edits fall into two classes.

### Representation-only edit

Does not alter substantive Artifact content.

Examples:

- resolution change;
- compression;
- margin adjustment;
- non-substantive timing correction.

### Substantive edit

Changes a claim, deterministic field, audience, disclosure, recommendation, price or call to action.

A substantive edit creates a new Artifact Version or derivative Artifact.

```text
approved V2
+ substantive edit
→ V3
→ Review/confirmation as applicable
```

This is the purpose of `ML-SCN-17`.

## 19.8 External editors and tools

Lite may use local or external tools for Render and Edit, but the Product boundary remains the same.

The system should know:

- what information was sent;
- why it was sent;
- which version was used;
- what the tool returned;
- whether data may be retained;
- whether the tool altered content;
- which validation was performed;
- whether the output may be reused.

Tool convenience does not remove data classification, client confidentiality or source rights.

## 19.9 `ML-W10` — Readiness Result

Readiness is a typed assessment of whether the work product may proceed to its next purpose.

It should be purpose-specific.

An Artifact may be ready for internal discussion but not ready for customer delivery. A video may be ready for preview but not public publication.

Readiness states include:

```text
ready_for_internal_use
ready_for_review
ready_for_confirmation
ready_for_handoff
blocked
incomplete
stale
unsupported
expired
```

A Readiness Result should list:

- assessed Artifact Version and representations;
- intended next purpose;
- required checks;
- passed checks;
- failed checks;
- missing information;
- unresolved rights;
- required Review;
- required user confirmation;
- expiry or revalidation point.

## 19.10 Readiness is not approval

```text
ready_for_review
≠ approved

ready_for_confirmation
≠ confirmed

ready_for_handoff
≠ accepted by destination

ready_for_publish_confirmation
≠ published
```

Readiness tells the Product what may happen next. It does not perform the next action.

## 19.11 Professional quality is multidimensional

A work product can fail even when its language is fluent.

Quality dimensions include:

- factual correctness;
- source traceability;
- currentness;
- professional reasoning;
- audience suitability;
- completeness;
- confidentiality;
- rights;
- deterministic-field accuracy;
- visual or media quality;
- accessibility;
- destination compatibility;
- action clarity.

Lite should not use one opaque “quality score” to hide these distinctions.

## 19.12 Format-specific checks

### PDF/report

- pages complete;
- headings and tables readable;
- deterministic fields match;
- links work;
- fonts and languages render;
- version visible where required.

### Image post

- text legible at target size;
- brand/trademark representation accurate;
- claim not truncated;
- required source/disclaimer available;
- image rights clear.

### Video

- script matches approved version;
- voice does not alter names or terms;
- subtitles match audio;
- duration preserves required content;
- visuals do not imply unsupported claims;
- music and footage rights clear;
- final CTA and contact details accurate.

### Email/message

- recipient and channel correct;
- subject and body match selected version;
- attachments correspond to the package;
- placeholders resolved;
- no restricted internal notes included.

## 19.13 Cost and entitlement observations

Render may consume:

- model usage;
- TTS minutes;
- video rendering time;
- storage;
- external API credits;
- human editing;
- professional Review.

Lite may record these under commercial evaluation, but cost does not determine professional readiness.

The Product must not reduce visible safety merely to meet a low-cost plan.

It may instead:

- limit format frequency;
- use templates;
- constrain duration;
- reserve advanced rendering for higher plans;
- require user-provided assets;
- offer manual export rather than automatic publishing.

## 19.14 Expiry and revalidation

Readiness may expire when:

- source data changes;
- a deadline passes;
- price validity ends;
- customer details change;
- review scope expires;
- rights change;
- destination requirements change;
- a correction affects the version.

The Product should not treat a once-ready Artifact as permanently ready.

## 19.15 A practical readiness gate

```text
Exact Artifact Version selected?            YES / NO
Required Review complete?                   YES / NO / N/A
Render matches selected version?            YES / NO
Deterministic fields validated?              YES / NO
Missing information resolved or disclosed?  YES / NO
Rights and data restrictions satisfied?     YES / NO
Audience and destination compatible?        YES / NO
Format-specific checks passed?               YES / NO
User confirmation required?                 YES / NO
Expiry/revalidation known?                   YES / NO
```

The result should name the next permitted action, not merely say “done.”

## 19.16 Chapter conclusion

Render and Edit make an Artifact usable in a medium. Readiness determines whether the exact version and representation may proceed to a defined next purpose.

```text
Artifact Version
→ Render Request
→ Render Result
→ optional governed Edit
→ validation
→ Readiness Result
```

The Product must preserve three independent questions:

1. Was the content professionally acceptable?
2. Was the representation created correctly?
3. Is the result ready for this specific next action?

Keeping these questions separate prevents polished output from being mistaken for approved, accurate or published work.
