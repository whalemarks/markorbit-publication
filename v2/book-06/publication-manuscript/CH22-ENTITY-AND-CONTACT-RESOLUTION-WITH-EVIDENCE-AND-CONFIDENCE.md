# Chapter 22 — Entity and Contact Resolution with Evidence and Confidence

A maintenance opportunity is useful only when the system can identify the relevant organization and a legitimate contact route.

Trademark records are poor customer directories. Owner names vary, addresses become stale, companies merge, local-language names differ, representatives change and contact information may come from websites, filings, invoices, email signatures or third-party databases with different levels of reliability.

Lite should not collapse this uncertainty into a single “customer” record.

```text
Observed entity mention
→ candidate entity
→ evidence-backed identity resolution
→ candidate contact points
→ contact verification
→ relationship and outreach eligibility
```

Identity resolution and contactability are separate questions.

## 1. Record name is not resolved identity

A trademark source may contain:

- legal entity name;
- trade name;
- former company name;
- branch name;
- transliteration;
- abbreviated name;
- individual proprietor;
- representative or filing agent;
- mailing address only;
- OCR or data-entry error.

Therefore:

```text
Same or similar name
≠ same legal entity

Same address
≠ current organization

Same website domain
≠ ownership or control
```

Resolution should preserve candidates and conflicts until evidence supports a conclusion.

## 2. Entity evidence has different authority

Possible evidence includes:

- official trademark record;
- corporate registry;
- official company website;
- signed POA or engagement document;
- certificate or assignment document;
- invoice and payment record;
- prior verified customer record;
- professional-directory entry;
- email-domain evidence;
- public business profile;
- data-broker record;
- AI-inferred similarity.

These sources should not be treated equally.

Each assertion should record:

- source;
- source date;
- jurisdiction;
- field observed;
- extraction method;
- confidence;
- contradiction status;
- reviewer or verification event;
- expiry or refresh rule.

## 3. Entity, Organization and Customer remain distinct

A legal entity can exist without being a customer. A Customer can represent a relationship context involving several legal entities. An Organization can have multiple Workplaces or brands.

```text
Legal Entity
≠ Organization in MarkOrbit
≠ Customer Relationship
≠ Contact Person
```

Lite should resolve enough structure to support a particular purpose without claiming universal identity certainty.

For example, a maintenance lead may need to know which company currently owns the registration and whether that company corresponds to an existing customer account. It may not yet need a complete group-company map.

## 4. Resolution should be purpose-scoped

Possible purposes include:

- confirm recorded owner;
- identify current legal successor;
- link a mark to an existing customer;
- determine whether outreach is eligible;
- find the correct billing entity;
- identify a signing authority;
- detect duplicate customer records;
- route a matter to the correct Workplace;
- prepare due diligence.

A resolution accepted for marketing outreach may be insufficient for execution of an assignment document.

```text
Resolved for contact
≠ resolved for legal execution
```

## 5. Confidence should be decomposed

Rather than one opaque percentage, Lite may expose:

- name match;
- address match;
- registration-number linkage;
- domain match;
- document evidence;
- corporate-registry match;
- prior relationship evidence;
- recency;
- contradiction severity;
- human-verification status.

A candidate may have strong name similarity but weak legal evidence. Another may have changed names but have a verified corporate-registry link.

## 6. Contact point is not contact permission

Candidate contact points may include:

- verified customer email;
- verified business-domain email;
- public role address;
- telephone number;
- website contact form;
- social account;
- representative email;
- historical email;
- private personal address;
- inferred email pattern.

Continue to preserve:

```text
Contact Point Found
≠ Contact Point Verified
≠ Person Authorized
≠ Outreach Permitted
```

The system should record source, recency, type, owner, verification status, intended purpose and suppression status for each contact point.

## 7. Person resolution requires role context

A named individual may be:

- company officer;
- in-house counsel;
- trademark manager;
- external attorney;
- prior employee;
- filing signatory;
- accountant;
- unrelated person with the same name.

Lite should not assume that a person who signed a filing years ago remains the current decision maker.

A Contact Role should include:

- represented organization;
- role source;
- effective period;
- authority scope;
- preferred channel;
- verification status;
- relationship owner;
- consent and suppression rules.

## 8. Historical data should remain historical

When an address, email or representative changes, the old data should not simply be overwritten.

Historical contact information may matter for:

- evidence of prior relationship;
- identifying a successor;
- explaining delivery failures;
- resolving duplicate records;
- auditing outreach;
- understanding prior filings.

But historical data should not remain active for communication without revalidation.

## 9. Duplicate resolution should be reversible

Entity resolution systems can make mistakes. A merge may combine two unrelated companies; a split may separate one company’s old and new name.

Lite should support:

- candidate link;
- verified link;
- rejected link;
- superseded link;
- merge proposal;
- reviewed merge;
- reversible merge;
- provenance-preserving split.

The original source assertions should remain available so a correction can propagate to leads, customers and recommendations.

## 10. AI has a supporting role

AI may:

- normalize names and addresses;
- compare transliterations;
- extract organization and person mentions;
- detect likely former names;
- rank candidate matches;
- identify conflicts;
- summarize evidence;
- suggest verification steps.

AI may not:

- create a legal successor relationship from similarity alone;
- mark a candidate contact as verified without evidence;
- infer marketing consent;
- infer signing authority from job title alone;
- merge customer records irreversibly;
- expose personal information beyond the permitted purpose.

## 11. Privacy and minimization apply during resolution

Entity resolution can accumulate sensitive information far beyond what the business needs.

Lite should limit:

- personal addresses;
- personal phone numbers;
- identity documents;
- family or ownership details;
- scraped social data;
- inferred demographics;
- irrelevant employment history.

The system should collect the minimum data necessary for the stated business or professional purpose and apply retention, access and deletion rules.

## 12. Resolution outputs should be typed

Possible outputs include:

```text
Confirmed Current Owner
Probable Current Owner — Review Needed
Existing Customer Match
Possible Customer Match
Historical Relationship Only
Representative Contact
Public Business Contact
Unverified Contact Candidate
No Safe Contact Route Found
Conflict Prevents Outreach
```

Typed outcomes are more actionable than a single entity ID with hidden uncertainty.

## 13. Example: owner-name variation

Suppose an official record names “Guangzhou Xiaoshi Brand Management Co., Ltd.” while an internal customer record uses a translated or shortened name.

Lite should compare:

- registration identifier;
- Chinese and English names;
- address;
- prior POA;
- invoice details;
- email domain;
- corporate registration evidence;
- former and current names.

The result may be:

```text
Existing Customer Match — high evidence
Current legal-name verification pending
Outreach through existing relationship owner only
```

It should not silently create a new prospect or send duplicate communications.

## 14. Example: public owner with uncertain contact

A public record identifies a company, but the only discovered email is a generic address from an old directory.

The system may classify:

- owner identity: probable;
- company website: verified;
- email: unverified and stale;
- current representative: unknown;
- outreach eligibility: review required.

The safe action may be to research further or use a transparent website contact route rather than send an urgent legal claim to an uncertain address.

## 15. Failure modes

This model fails when:

- fuzzy name similarity becomes confirmed identity;
- old addresses remain active indefinitely;
- a filing representative is treated as the owner;
- candidate contacts become marketing lists automatically;
- personal data is collected without purpose;
- entity merges cannot be reversed;
- AI confidence is hidden behind a “verified” badge;
- one Workplace’s customer match becomes visible to unrelated Workplaces;
- an external data provider’s claim becomes formal state without review;
- identity resolution is reused for a higher-risk purpose without revalidation.

## 16. Product and technical implications

Lite needs:

- source-level entity mentions;
- normalized but non-destructive name and address representations;
- candidate-link graphs;
- evidence and contradiction records;
- purpose-scoped confidence;
- reversible merge and split workflows;
- typed contact points;
- role and authority context;
- verification and expiry;
- privacy and retention controls;
- Workplace-scoped customer relationship links;
- feedback loops to Data Refinery and Brain.

Core may define shared semantic distinctions, but the Owning Service for customer and formal business state remains responsible for accepted records.

## 17. Commercial implications

Reliable resolution improves:

- lead quality;
- customer retention;
- portfolio consolidation;
- outreach deliverability;
- partner attribution;
- billing accuracy;
- due diligence;
- service handoff.

Poor resolution creates duplicate outreach, privacy risk, missed customers and false commercial claims.

The strongest commercial asset is not the largest contact database. It is a current, evidence-backed relationship map with clear permission boundaries.

## 18. The operating principle

```text
Preserve every source assertion
Resolve only for a stated purpose
Expose confidence and contradiction
Separate identity from contactability
Separate contactability from permission
Keep corrections reversible
```

> Lite should help a Workplace know who an entity probably is, how that conclusion was reached and whether it is legitimate to contact them—without turning uncertainty into false identity.