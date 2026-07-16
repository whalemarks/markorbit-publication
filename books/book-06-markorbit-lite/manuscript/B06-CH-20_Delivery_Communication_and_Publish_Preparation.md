# B06-CH-20 — Delivery, Communication and Publish Preparation

**Status:** Complete Draft 1  
**Chapter Map:** B06-TOC-V0.1 — Owner Accepted  
**Part:** Part IV — Professional Work Products  
**Primary controls:** ML-W05, ML-W09, ML-H06, ML-HC-04, ML-HC-07, ML-SCN-16, ML-SCN-18

## Chapter Purpose

This chapter explains how a ready professional work product becomes a precisely defined Delivery, Communication or Publish package without confusing preparation with external completion.

The central proposition is:

> A professional result becomes an external action only through an exact package, current confirmation and a typed destination outcome.

## 20.1 A ready work product still needs a controlled destination

A professional Artifact may be ready for use, yet still require a separate decision about:

- who should receive it;
- through which channel;
- under which account or Organization identity;
- with which attachments;
- for what purpose;
- at what time;
- with what legal or professional consequence;
- under which evidence and audit requirements.

The final stage before external action is therefore not “publish.” It is preparation for a defined delivery, Communication or publication action.

## 20.2 Three related but different destinations

### Delivery

Delivery transfers a selected work product to a defined recipient or destination.

Examples:

- provide a PDF recommendation to a customer portal;
- share a quotation through a secure link;
- return a completed internal brief to a team member;
- attach a work product to a governed service journey.

### Communication

Communication includes the message, recipients, channel, purpose and send state.

Examples:

- customer email;
- instant-message follow-up;
- internal review request;
- service-provider instruction;
- notification linked to a formal record.

### Publish

Publish makes a selected Artifact available to an audience through a publication channel.

Examples:

- public article;
- social-media image post;
- short video;
- Organization knowledge page;
- approved customer education page.

One action may involve more than one destination, but their states must remain distinct.

```text
Artifact delivered to reviewer
≠ customer Communication sent
≠ public post published
```

## 20.3 `ML-W09` — Delivery / Publish Package Candidate

A package candidate should identify:

- exact Artifact Version;
- exact rendered representation;
- destination type;
- audience or recipients;
- channel or account;
- purpose;
- attachments and links;
- rights and consent;
- data classification;
- required Review;
- required final confirmation;
- timing or schedule;
- evidence expected;
- failure and unknown-state handling;
- expiry and cancellation conditions.

The package is a candidate because preparation does not mean the external action has occurred.

## 20.4 Exact identity matters

Before a Communication or publication action, Lite should show:

```text
Who is acting?
For which Organization?
Using which account?
To which exact recipient or audience?
Through which channel?
Using which Artifact Version and representation?
For what stated purpose?
With what consequence?
```

A correct Artifact sent to the wrong person remains a serious failure.

A correct post published from the wrong account may create confidentiality, brand and ownership problems.

## 20.5 Communication Package

A Communication Handoff should contain at least:

- sender identity and Organization;
- exact recipients;
- channel;
- subject or opening;
- exact body version;
- selected attachments or links;
- purpose;
- customer or Matter reference;
- required approval and confirmation;
- send consequence;
- return address.

The draft may be personalized, but personalization must not invent facts, relationships or instructions.

```text
prepared Communication
≠ sent Communication
```

The Communication Service owns send state and evidence.

## 20.6 Delivery package

A Delivery Package should preserve:

- recipient/destination;
- selected Artifact Version;
- selected representation;
- access control;
- validity period;
- download or viewing rules;
- acknowledgement requirements;
- delivery evidence;
- revocation or replacement treatment.

A secure customer link, a file attachment and a portal upload are not equivalent delivery methods. Each has different evidence, access and expiry behavior.

## 20.7 Publish Package

A Publish Package should identify:

- exact public or limited audience;
- publication account;
- selected Artifact Version;
- title, caption and metadata;
- selected media;
- rights and licenses;
- client consent and anonymization basis where relevant;
- required disclaimer;
- timing;
- comment or response handling;
- expected publication evidence;
- correction and takedown route.

A package may be ready even when publication remains prohibited pending final confirmation.

This is the purpose of `ML-SCN-16`:

```text
Publish Package ready
→ display ready_for_confirmation
→ do not display published
```

## 20.8 Final user confirmation

Before a consequential external action, final confirmation should expose:

- exact recipient or audience;
- exact account and channel;
- exact message and Artifact Version;
- attachments;
- purpose;
- timing;
- professional or commercial consequence;
- any unresolved warnings;
- whether Human Review was required and completed.

The confirmation should be close in time to the action and invalidate when material details change.

## 20.9 Review and confirmation remain separate

```text
Review asks:
Is this work professionally suitable for the defined scope?

Confirmation asks:
Should this exact action occur now, to this destination, with this consequence?
```

The same individual may perform both decisions in a sole practice, but the Product should preserve both meanings.

## 20.10 Manual, assisted and governed operation

The Product may support several operating modes.

### Manual operation

Lite prepares the package. The user copies, downloads or manually publishes.

The Product records that preparation occurred, but it should not claim the external result without evidence or user report.

### Assisted operation

Lite opens the destination, pre-fills allowed fields or exports a package. The user completes the action.

The result may still be unknown unless the destination returns evidence.

### Governed operation

Lite sends a typed Handoff to Communication, Delivery/Publish or Execution services. The destination validates authority, performs the action and returns a typed result.

No mode permits Lite to infer completion from preparation alone.

## 20.11 Typed external outcomes

Expected result classes include:

```text
accepted_by_destination
completed_by_destination
failed
blocked
rejected
cancelled
unknown_external_outcome
```

Additional evidence may include:

- message ID;
- delivery timestamp;
- publication URL;
- destination account;
- recipient acknowledgement;
- file checksum;
- returned formal reference.

## 20.12 Unknown outcome is a real state

External systems may time out or fail to return reliable confirmation.

The Product must preserve:

```text
unknown_external_outcome
```

It must not silently convert unknown into:

- sent;
- failed;
- published;
- safe to retry.

A blind retry can create duplicate messages or duplicate posts. This is why `ML-SCN-18` is blocking.

## 20.13 Scheduling and expiry

A scheduled package must be revalidated when:

- the Artifact changes;
- source facts become stale;
- price validity ends;
- account access changes;
- recipient status changes;
- consent is withdrawn;
- Review expires;
- a correction affects the package;
- destination policy changes.

Scheduling is not permanent authorization.

## 20.14 Rights and client consent

Public or broad distribution requires special attention to:

- client identity;
- case facts;
- trademark images;
- screenshots;
- official documents;
- third-party images, music and footage;
- personal data;
- confidential prices;
- service-provider information;
- public claims.

Anonymization alone does not create publication permission. Removal of a name may still leave the client or case identifiable.

## 20.15 Response routes are part of publication design

A published or delivered Artifact may produce:

- customer questions;
- prospect enquiries;
- corrections;
- complaints;
- opt-outs;
- service requests;
- misinformation reports;
- requests to remove content.

The package should define where these responses go and how they are classified.

Publication without a response route breaks the Product loop.

## 20.16 Edition and commercial constraints

Commercial plans may limit:

- publication channels;
- number of renders;
- assisted publishing;
- scheduled packages;
- premium templates;
- video duration;
- human review;
- account integrations.

These constraints should affect entitlement and operation mode, not semantic truth.

A low-cost plan may require manual publication, but it must not represent a prepared package as a completed publication.

## 20.17 A practical pre-action checklist

```text
Exact Artifact Version selected?            YES / NO
Representation validated?                   YES / NO
Recipient/audience exact?                   YES / NO
Channel/account exact?                      YES / NO
Purpose and consequence visible?            YES / NO
Rights and consent satisfied?               YES / NO
Required Review complete?                   YES / NO / N/A
Final confirmation current?                 YES / NO
Attachments and links correct?              YES / NO
Failure/unknown handling defined?           YES / NO
Response and correction route defined?      YES / NO
```

## Chapter Conclusion

A professional result becomes an external action only through a controlled package and an explicit destination decision.

```text
ready Artifact Version
→ Delivery / Communication / Publish Package Candidate
→ exact-version preview
→ Review where required
→ final confirmation
→ manual, assisted or governed operation
→ typed external outcome
```

This separation allows Lite to make external work easier without pretending that preparation is delivery, that readiness is publication or that an uncertain external result is safely complete.