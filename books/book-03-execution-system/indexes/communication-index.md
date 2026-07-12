# Appendix F — Communication Boundary Index

## Communication Stages

```text
prepare
→ draft
→ review
→ approve for a defined send purpose
→ send through Communication Service
→ delivery observation
→ receipt or reply observation
```

Each stage is distinct.

## Package Binding

A Communication package includes:

- body;
- subject;
- sender;
- recipients;
- attachments;
- channel;
- purpose;
- source and Matter references;
- exact version.

A material change to any package component may require renewed Human Review.

## Current MVP Boundary

Communication Review may create and review an internal draft package. Production send is not included.

## Core Rules

- Draft is not review.
- Review is not approval.
- Approval is not send.
- Send is not delivery.
- Delivery is not receipt or agreement.
- An uncertain send blocks blind resend.
- Communication Service owns send and its Events.
- AI may draft and compare but may not approve or send.

## Primary References

- [Communication Execution Boundary](../manuscript/B03-CH-13_Communication_Execution_Boundary.md)
- [Communication Review Pattern](../manuscript/B03-CH-19_Communication_Review_Pattern.md)
- [Idempotency and Retry Governance](../manuscript/B03-CH-25_Idempotency_and_Retry_Governance.md)
