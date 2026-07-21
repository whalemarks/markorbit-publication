# Chapter 17 — Inquiry Preserves Provenance and Relationship Ownership

A buyer clicking “contact seller” does not create a transaction. It creates an Inquiry.

That distinction matters because the first commercial contact is where many later disputes begin:

- Who introduced the buyer?
- Which Listing version did the buyer see?
- Which price was shown?
- Which Workplace owns the customer relationship?
- Was direct contact permitted?
- Was the seller authorized to respond?
- Which commission and attribution rules apply?
- Did the buyer ask for information, submit an offer or merely save the asset?

A generic marketplace often reduces all of this to a message thread. Lite should preserve the Inquiry as a governed commercial object.

```text
Request or Listing interaction
→ Inquiry
→ qualification
→ information exchange
→ possible Transaction Opportunity
```

## 1. Inquiry is not demand itself

A Trademark Request expresses a structured need. A Listing expresses a controlled supply projection. An Inquiry is the event where a specific represented party seeks information or action concerning a specific asset or recommendation.

```text
Trademark Request
≠ Inquiry

Listing view
≠ Inquiry

Saved candidate
≠ Inquiry

Inquiry
≠ Offer
≠ Transaction Opportunity
```

An Inquiry may originate from:

- a public Listing;
- a private recommendation;
- a selected-network response;
- a buyer Request shortlist;
- a social campaign;
- an email introduction;
- a Workplace referral;
- an offline conversation entered into Lite.

The source must remain attached.

## 2. Provenance should be captured at creation

An Inquiry should record:

- originating Request, Listing or Recommendation;
- exact Listing and Marketing Pack version shown;
- source channel and campaign;
- referring Workplace or Person;
- represented buyer context;
- Relationship Owner;
- seller-side Relationship Owner;
- permitted contact route;
- confidentiality level;
- price and terms visible at the time;
- attribution and commission rules;
- timestamp and expiry;
- consent and communication basis;
- original message or action.

Later edits to a Listing should not rewrite what the buyer actually saw.

## 3. Relationship ownership is contextual

The platform should not assume that the person who sends the first message owns the commercial relationship.

Possible roles include:

```text
Demand Originator
Buyer Relationship Owner
Listing Source
Seller Relationship Owner
Referral Source
Co-broker
Transaction Coordinator
Professional Service Provider
```

These may belong to different Workplaces.

For example, an agency may represent the buyer, another agency may hold the seller relationship, and Lite may provide matching and workflow support. None of these roles automatically absorbs the others.

```text
Message access
≠ Relationship Ownership
```

## 4. Direct contact must be governed

An Inquiry should state whether the responding party may:

- reply only through Lite;
- contact the referring Workplace;
- contact the buyer directly;
- contact the owner directly;
- disclose identity to another participant;
- arrange a meeting;
- send documents;
- make a price proposal;
- invite additional professionals.

A network participant who can see an Inquiry does not automatically gain permission to market unrelated services to the buyer or owner.

## 5. Inquiry identity and qualification

The person asking may be:

- the final buyer;
- an agency representative;
- an employee;
- a lawyer;
- a broker;
- an investor;
- a researcher;
- an unqualified lead;
- a competitor seeking information.

Lite should collect proportionate qualification before disclosing sensitive information.

Qualification may include:

- identity confidence;
- represented organization;
- authority to inquire;
- intended use;
- budget credibility;
- jurisdiction;
- timeline;
- confidentiality acceptance;
- conflict or sanctions checks where relevant;
- ability to proceed to due diligence.

The system should not treat every Inquiry as equally credible.

## 6. Progressive information exchange

The Inquiry can support staged disclosure:

```text
Initial Inquiry
→ basic clarification
→ qualified recipient status
→ additional legal and commercial facts
→ due-diligence access
→ offer or closure
```

This protects owner identity, private price, authorization evidence and sensitive documents while still allowing genuine buyers to progress.

## 7. Inquiry states

A useful lifecycle is:

```text
Received
→ Acknowledged
→ Qualification Pending
→ Qualified
→ Information Requested
→ Information Supplied
→ Buyer Reviewing
→ Seller Reconfirmation Pending
→ Offer Invited
→ Converted to Transaction Opportunity
→ Closed / Rejected / Expired / Withdrawn
```

States should describe actual events, not AI predictions.

## 8. One Inquiry may involve several assets

A buyer may ask about one Listing and then compare alternatives. Lite should distinguish:

- the parent Inquiry;
- asset-specific candidate threads;
- buyer feedback;
- rejected candidates;
- newly introduced candidates;
- eventual selected asset.

This preserves learning without pretending that every candidate became a separate buyer relationship.

## 9. Communication evidence

Important communications should preserve:

- sender and represented role;
- recipient;
- channel;
- timestamp;
- content or normalized summary;
- attachments;
- terms discussed;
- approvals or disclaimers;
- language and translation status;
- relation to the Inquiry state.

AI may summarize communications, but the original evidence should remain available where retention and privacy rules permit.

```text
AI summary
≠ original communication evidence
```

## 10. Price discussion requires context

An Inquiry may involve:

- public asking price;
- owner net price;
- partner price;
- buyer budget;
- permitted discount;
- preliminary indication;
- formal quotation;
- offer.

These must not collapse into one field.

```text
Price mentioned
≠ binding quotation
≠ offer accepted
```

The system should show who may disclose, negotiate or approve each amount.

## 11. Inquiry does not create exclusivity

A buyer may ask for information while other buyers remain active. Exclusivity requires a separate event such as:

- named-buyer protection;
- reservation;
- exclusivity agreement;
- accepted deposit condition;
- signed negotiation term.

The Inquiry itself should not silently block other demand.

## 12. Anti-circumvention evidence

When several Workplaces participate, Lite should preserve:

- who introduced the buyer;
- who introduced the asset;
- protected scope;
- protection period;
- permitted direct communication;
- prior independent relationship claims;
- commission basis;
- later transaction link.

This is evidence for dispute analysis, not proof that one party owns the buyer forever.

## 13. AI assistance

AI may assist by:

- classifying Inquiry intent;
- extracting budget, timeline and questions;
- identifying missing qualification;
- detecting unsupported promises;
- proposing replies;
- translating;
- summarizing long threads;
- highlighting changes in price or terms;
- identifying possible duplicate inquiries;
- recommending next safe action.

AI should not:

- declare the buyer qualified without evidence;
- grant direct-contact permission;
- create Relationship Ownership;
- accept an offer;
- infer binding authority;
- disclose protected information automatically;
- convert the Inquiry into a transaction solely from message sentiment.

## 14. Example

A Chinese agency submits a Request for a US Class 25 mark. Lite recommends a network Listing controlled by another Workplace. The agency asks for owner confirmation and final price.

The Inquiry records:

- buyer agency as Buyer Relationship Owner;
- listing Workplace as Seller Relationship Owner;
- network partner as Listing Source;
- the exact Recommendation and Listing versions;
- no direct buyer-owner contact;
- commission split and attribution;
- seller reconfirmation required;
- buyer identity hidden until qualification.

The seller later confirms availability and price. That creates new evidence inside the Inquiry, not a completed transaction.

## 15. Failure modes

The Inquiry model fails when:

- messages are detached from Listing and Request versions;
- first contact automatically transfers the relationship;
- buyer identity is disclosed too early;
- seller-side participants contact the buyer for unrelated services;
- a price mention becomes a binding quotation;
- AI summaries replace original evidence;
- qualification is assumed from email domain or message quality;
- inquiry count is treated as liquidity without quality analysis;
- referral and commission provenance disappears;
- closed inquiries remain active indefinitely.

## 16. Product and technical implications

Lite needs:

- Inquiry objects linked to source versions;
- represented-role and Relationship Owner fields;
- staged identity and document disclosure;
- communication evidence and summaries;
- permission-aware messaging;
- qualification state;
- commercial-term snapshots;
- attribution and protection records;
- duplicate and related-Inquiry handling;
- expiry and closure;
- conversion events into Transaction Opportunity;
- correction and audit history.

## 17. Commercial implications

Inquiry quality affects:

- seller trust;
- partner participation;
- conversion;
- commission disputes;
- response speed;
- public-marketplace viability;
- private-network liquidity.

Lite should optimize for qualified and traceable inquiries, not maximum message volume.

## 18. The operating principle

```text
Preserve where the Inquiry came from
Preserve who represents whom
Disclose progressively
Separate questions from offers
Separate contact from relationship transfer
Convert only through explicit events
```

> An Inquiry becomes commercially useful when every participant can understand why the conversation exists, what may be disclosed, who owns each relationship and what has not yet been agreed.