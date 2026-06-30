# Billing and Subscription Backend API Requirements

This document defines the backend APIs, webhook handlers, and state model needed to support the billing and subscription flows currently implemented in the UI prototype in [v1.0.1/index.html](v1.0.1/index.html).

## Goals

The backend must support these user-visible flows:

- View current subscription, status, renewal date, billing cycle, and plan entitlements
- Compare plans and start checkout for Pro or Pro+
- Start a 14-day Pro trial for eligible users
- Subscribe, resubscribe, and schedule cancellation
- Change billing cycle between monthly and annual
- Toggle auto-renewal
- View invoices and receipts
- Manage payment methods: list, add, edit expiry metadata, set default, remove
- Request refund for eligible paid invoices
- Show usage metrics for current plan limits
- Record billing timeline events for the UI activity feed

## Recommended Architecture

Use a billing provider such as Stripe as system of record for:

- Customers
- Payment methods
- Checkout / subscription creation
- Invoices
- Receipts
- Refunds
- Webhooks for asynchronous state changes

The product backend should remain system of record for:

- Internal user account linkage
- Feature entitlements
- Usage aggregation
- Billing timeline events shown in the UI
- Plan catalog metadata consumed by the application
- Authorization and audit trail

## Core Domain Objects

## User Billing Profile

```json
{
  "userId": "usr_123",
  "customerId": "cus_123",
  "email": "user@example.com",
  "currency": "USD",
  "country": "US",
  "taxExempt": false,
  "billingAddress": {
    "line1": "548 Market Street",
    "city": "San Francisco",
    "state": "CA",
    "postalCode": "94104",
    "country": "US"
  }
}
```

## Subscription

```json
{
  "id": "sub_123",
  "userId": "usr_123",
  "provider": "stripe",
  "providerSubscriptionId": "sub_stripe_123",
  "planCode": "pro",
  "planName": "Pro",
  "status": "active",
  "billingCycle": "monthly",
  "autoRenew": true,
  "trial": {
    "isTrial": false,
    "trialStartAt": null,
    "trialEndAt": null,
    "hasTrialed": true
  },
  "currentPeriodStart": "2026-06-01T00:00:00Z",
  "currentPeriodEnd": "2026-07-01T00:00:00Z",
  "cancelAtPeriodEnd": false,
  "canceledAt": null,
  "endedAt": null,
  "defaultPaymentMethodId": "pm_123"
}
```

## Payment Method

```json
{
  "id": "pm_123",
  "provider": "stripe",
  "type": "card",
  "brand": "visa",
  "last4": "4242",
  "expMonth": 12,
  "expYear": 2028,
  "isDefault": true,
  "walletType": null,
  "paypalEmail": null,
  "billingName": "Jane Doe"
}
```

## Invoice

```json
{
  "id": "inv_123",
  "providerInvoiceId": "in_123",
  "number": "INV-001234",
  "subscriptionId": "sub_123",
  "status": "paid",
  "refundStatus": "none",
  "date": "2026-06-01",
  "currency": "USD",
  "subtotal": 45,
  "tax": 0,
  "total": 45,
  "description": "Pro Monthly",
  "receiptId": "rcpt_123",
  "paymentMethodSummary": "Visa ending in 4242",
  "hostedInvoiceUrl": "https://...",
  "pdfUrl": "https://..."
}
```

## Receipt

```json
{
  "id": "rcpt_123",
  "invoiceId": "inv_123",
  "date": "2026-06-01",
  "paidAt": "2026-06-01T10:22:00Z",
  "email": "user@example.com",
  "paymentMethod": "Visa ending in 4242",
  "items": [
    {
      "description": "Pro Monthly",
      "quantity": 1,
      "unitPrice": 45,
      "total": 45
    }
  ],
  "subtotal": 45,
  "tax": 0,
  "total": 45,
  "pdfUrl": "https://..."
}
```

## Usage Summary

```json
{
  "planCode": "pro",
  "billingCycle": "monthly",
  "periodStart": "2026-06-01T00:00:00Z",
  "periodEnd": "2026-07-01T00:00:00Z",
  "metrics": [
    {
      "code": "wallet_slots",
      "label": "Wallet tracking slots",
      "used": 24,
      "limit": null,
      "unit": "slots"
    },
    {
      "code": "api_calls_daily",
      "label": "API calls (24h)",
      "used": 4211,
      "limit": 10000,
      "unit": "calls"
    },
    {
      "code": "data_history_days",
      "label": "Data history accessed",
      "used": 42,
      "limit": 90,
      "unit": "days"
    },
    {
      "code": "active_alerts",
      "label": "Active alerts",
      "used": 9,
      "limit": 20,
      "unit": "alerts"
    }
  ]
}
```

## Billing Timeline Event

```json
{
  "id": "evt_123",
  "type": "subscription_created",
  "date": "2026-06-01",
  "time": "10:22",
  "detail": "Pro Monthly subscription started",
  "amount": 45,
  "metadata": {
    "invoiceId": "inv_123"
  }
}
```

## API Surface

Base path suggestion:

```text
/api/billing
```

## 1. Get Billing Overview

`GET /api/billing/overview`

Purpose:

- hydrate the billing page in one request
- avoid multiple blocking calls on initial settings load

Response:

```json
{
  "profile": {},
  "subscription": {},
  "plans": [],
  "paymentMethods": [],
  "invoices": [],
  "timeline": [],
  "usage": {},
  "refundPolicy": {
    "eligibleWindowDays": 30,
    "processingEstimate": "5-10 business days"
  }
}
```

## 2. Get Plan Catalog

`GET /api/billing/plans`

Purpose:

- plan comparison cards
- feature list
- monthly and annual prices
- eligibility flags

Response:

```json
[
  {
    "code": "free",
    "name": "Free",
    "prices": [],
    "features": [],
    "limits": {
      "wallet_slots": 10,
      "api_calls_daily": 1000,
      "data_history_days": 7,
      "active_alerts": 5
    }
  },
  {
    "code": "pro",
    "name": "Pro",
    "prices": [
      { "billingCycle": "monthly", "amount": 45, "currency": "USD", "providerPriceId": "price_pro_monthly" },
      { "billingCycle": "annual", "amount": 450, "currency": "USD", "providerPriceId": "price_pro_annual" }
    ],
    "trial": {
      "days": 14,
      "eligible": true
    },
    "limits": {
      "wallet_slots": null,
      "api_calls_daily": 10000,
      "data_history_days": 90,
      "active_alerts": 20
    }
  }
]
```

## 3. Start Checkout Session

`POST /api/billing/checkout/session`

Purpose:

- create Stripe Checkout Session or Payment Element client secret
- handle new subscriptions, resubscriptions, and upgrades
- enforce backend eligibility and price integrity

Request:

```json
{
  "planCode": "pro",
  "billingCycle": "annual",
  "entryPoint": "settings_billing",
  "promoCode": "SAVE10",
  "paymentMethodType": "card"
}
```

Response:

```json
{
  "checkoutSessionId": "cs_123",
  "clientSecret": "seti_..._secret_...",
  "provider": "stripe",
  "mode": "subscription",
  "subscriptionPreview": {
    "planCode": "pro",
    "billingCycle": "annual",
    "subtotal": 450,
    "discount": 45,
    "tax": 0,
    "total": 405,
    "currency": "USD",
    "trialDays": 14
  }
}
```

Notes:

- Never trust price or trial eligibility from the client.
- Promo code validation must happen server-side.
- The backend must prevent invalid transitions such as second free trial when policy disallows it.

## 4. Preview Subscription Change

`POST /api/billing/subscription/change-preview`

Purpose:

- show price delta before plan change or billing cycle change
- support proration rules

Request:

```json
{
  "targetPlanCode": "proplus",
  "targetBillingCycle": "annual"
}
```

Response:

```json
{
  "current": {
    "planCode": "pro",
    "billingCycle": "monthly",
    "amount": 45
  },
  "target": {
    "planCode": "proplus",
    "billingCycle": "annual",
    "amount": 990
  },
  "proration": {
    "enabled": true,
    "credit": 18,
    "charge": 963,
    "effectiveAt": "next_billing_cycle"
  }
}
```

## 5. Change Billing Cycle

`POST /api/billing/subscription/billing-cycle`

Purpose:

- switch active subscription between monthly and annual
- return effective date and proration policy

Request:

```json
{
  "billingCycle": "annual"
}
```

Response:

```json
{
  "subscription": {},
  "change": {
    "effectiveAt": "2026-07-01T00:00:00Z",
    "prorationBehavior": "none",
    "message": "Change will take effect on next renewal"
  }
}
```

## 6. Cancel Subscription

`POST /api/billing/subscription/cancel`

Purpose:

- schedule cancellation at period end
- capture optional cancellation reason

Request:

```json
{
  "cancelAtPeriodEnd": true,
  "reasonCode": "too_expensive"
}
```

Response:

```json
{
  "subscription": {
    "status": "active",
    "cancelAtPeriodEnd": true,
    "currentPeriodEnd": "2026-07-01T00:00:00Z"
  },
  "message": "Subscription will remain active until the end of the billing period"
}
```

## 7. Reactivate Subscription

`POST /api/billing/subscription/reactivate`

Purpose:

- reverse scheduled cancellation if period has not ended

Response:

```json
{
  "subscription": {
    "status": "active",
    "cancelAtPeriodEnd": false
  }
}
```

## 8. Toggle Auto-Renew

`POST /api/billing/subscription/auto-renew`

Request:

```json
{
  "autoRenew": false
}
```

Response:

```json
{
  "subscription": {
    "autoRenew": false,
    "cancelAtPeriodEnd": true,
    "currentPeriodEnd": "2026-07-01T00:00:00Z"
  }
}
```

Implementation note:

- If the business model treats `autoRenew=false` as equivalent to `cancel_at_period_end=true`, reflect that clearly in API semantics.
- Avoid a separate boolean that can drift out of sync with provider subscription status.

## 9. List Payment Methods

`GET /api/billing/payment-methods`

Response:

```json
{
  "items": []
}
```

## 10. Create Payment Method Setup Session

`POST /api/billing/payment-methods/setup-session`

Purpose:

- obtain client secret for Stripe SetupIntent or equivalent
- attach card or wallet without charging immediately

Request:

```json
{
  "setAsDefault": true
}
```

Response:

```json
{
  "clientSecret": "seti_..._secret_...",
  "provider": "stripe"
}
```

Important:

- The current prototype uses raw card fields in a modal. Production backend should not accept raw PAN/CVC through your own API.
- Use provider-hosted tokenization only.

## 11. Set Default Payment Method

`POST /api/billing/payment-methods/{paymentMethodId}/default`

Response:

```json
{
  "defaultPaymentMethodId": "pm_123",
  "paymentMethods": []
}
```

## 12. Update Payment Method Metadata

`PATCH /api/billing/payment-methods/{paymentMethodId}`

Purpose:

- usually only local metadata or billing name
- expiry changes should generally come from provider-managed replacement, not manual editing

Request:

```json
{
  "label": "Team card"
}
```

Recommendation:

- The current UI allows editing card expiry. That is not realistic for a production integration.
- Preferred UX is: remove the fake expiry edit and replace with "Replace card" or "Update in billing portal".

## 13. Remove Payment Method

`DELETE /api/billing/payment-methods/{paymentMethodId}`

Rules:

- reject removal if this is the only usable default method on an active subscription
- return a specific business error code

Error example:

```json
{
  "error": {
    "code": "default_payment_method_required",
    "message": "Set another default payment method before removing this one"
  }
}
```

## 14. List Invoices

`GET /api/billing/invoices?limit=20&cursor=...`

Response:

```json
{
  "items": [],
  "nextCursor": null
}
```

## 15. Get Invoice Detail

`GET /api/billing/invoices/{invoiceId}`

Response:

```json
{
  "invoice": {},
  "receipt": {}
}
```

## 16. Download Invoice PDF

`GET /api/billing/invoices/{invoiceId}/pdf`

Behavior:

- return provider-hosted URL or signed redirect

## 17. Get Receipt Detail

`GET /api/billing/receipts/{receiptId}`

## 18. Request Refund

`POST /api/billing/invoices/{invoiceId}/refund-request`

Purpose:

- create refund request record
- optionally trigger automatic refund if policy is deterministic
- otherwise queue for ops review

Request:

```json
{
  "reason": "requested_by_customer"
}
```

Response:

```json
{
  "invoiceId": "inv_123",
  "refundStatus": "requested",
  "requestedAt": "2026-06-30T12:00:00Z",
  "eligible": true,
  "message": "Refund request submitted"
}
```

Important:

- Refund state must be separate from invoice payment state.
- Do not change a paid invoice to `pending` just because refund review is pending.
- Suggested values:
  - invoice.status: `paid | open | failed | void | refunded`
  - invoice.refundStatus: `none | requested | processing | refunded | rejected`

## 19. Get Usage Summary

`GET /api/billing/usage`

Purpose:

- fill the usage cards with real aggregated metrics
- keep limits aligned with plan entitlements

## 20. Get Billing Timeline

`GET /api/billing/events?limit=20`

Purpose:

- render the subscription timeline
- merge provider events with product-specific events if needed

## 21. Open Billing Portal

`POST /api/billing/portal-session`

Purpose:

- create provider-hosted customer portal session
- recommended for production management of cards, invoices, and taxes

Response:

```json
{
  "url": "https://billing.stripe.com/session/..."
}
```

Recommendation:

- This should likely back the UI's `Contact sales` or future `Manage billing` action for production-safe card edits.

## Webhooks Required

Base suggestion:

```text
POST /api/webhooks/stripe
```

Handle at minimum:

- `checkout.session.completed`
- `customer.subscription.created`
- `customer.subscription.updated`
- `customer.subscription.deleted`
- `invoice.created`
- `invoice.paid`
- `invoice.payment_failed`
- `invoice.finalized`
- `payment_method.attached`
- `payment_method.detached`
- `charge.refunded`
- `refund.updated`

Webhook responsibilities:

- update local subscription record
- generate or sync invoice and receipt records
- mark trial conversion success/failure
- sync default payment method changes
- emit billing timeline events
- update entitlements consumed by the app

## State Model Recommendations

Use explicit enums instead of UI-derived flags.

## Subscription Status

- `trialing`
- `active`
- `past_due`
- `canceled`
- `incomplete`
- `incomplete_expired`
- `unpaid`

## Invoice Status

- `draft`
- `open`
- `paid`
- `void`
- `uncollectible`
- `failed`
- `refunded`

## Refund Status

- `none`
- `requested`
- `processing`
- `refunded`
- `rejected`

## Payment Method Type

- `card`
- `paypal_wallet`
- `bank_account`

## Validation and Authorization Rules

The backend must enforce:

- users can only access their own billing records
- second free trial blocked if policy disallows it
- invalid plan transitions rejected
- payment method deletion blocked if it would orphan an active subscription
- refund request eligibility by invoice status and age
- billing cycle changes only for eligible plans
- invoice and receipt downloads only for authorized account owner
- promo code validity, eligibility, and expiration

## Error Contract

Standardize errors:

```json
{
  "error": {
    "code": "refund_not_eligible",
    "message": "Refunds are only available within 30 days of payment",
    "details": {
      "invoiceId": "inv_123"
    }
  }
}
```

Suggested business error codes:

- `trial_not_eligible`
- `invalid_plan_transition`
- `payment_method_not_found`
- `default_payment_method_required`
- `refund_not_eligible`
- `subscription_not_active`
- `billing_cycle_change_not_allowed`
- `promo_code_invalid`
- `promo_code_expired`
- `provider_sync_failed`

## Prototype Gaps and Recommended UI Corrections

These areas in the current prototype should be adjusted before calling it production-ready.

## 1. Payment Method Expiry Editing Is Not Production-Realistic

Current prototype behavior:

- user can open a saved card and directly edit `expMonth` and `expYear`

Recommendation:

- replace `Edit details` with `Replace card` or `Manage in billing portal`
- use provider-hosted update flow instead of editing saved card expiry in your own UI

## 2. Raw Card Data Should Not Hit Your Backend

Current prototype behavior:

- UI contains mock card fields for adding a payment method

Recommendation:

- production implementation must use Stripe Elements / Payment Element / SetupIntent
- backend should only receive payment method tokens or SetupIntent results

## 3. Auto-Renew and Cancel-at-Period-End Should Be Unified

Current prototype behavior:

- UI exposes auto-renew toggle and cancellation flow separately

Recommendation:

- map both to one canonical backend field: `cancelAtPeriodEnd`
- avoid maintaining redundant booleans in the backend

## 4. Billing Cycle State Must Use One Source of Truth

Recommendation:

- persist billing cycle only on the subscription object from backend
- UI should not mix display-only toggle state with actual subscription cycle

## 5. Refund Status Must Be Separate from Invoice Status

Recommendation:

- keep invoice payment state immutable unless the payment outcome actually changes
- add separate refund lifecycle state as described above

## 6. Usage Metrics Must Come From Real Aggregates

Current prototype behavior:

- some usage values are simulated

Recommendation:

- backend should return actual aggregated usage for current billing window
- UI should not generate random usage in production mode

## 7. Consider a Hosted Billing Portal for Lower Risk

For a production app, the safest hybrid approach is:

- custom in-app overview page for plan comparison, usage, invoices summary, and timeline
- provider-hosted billing portal for card replacement, tax details, invoice exports, and subscription management edge cases

## Suggested Delivery Order

1. Build read-only billing overview endpoint
2. Integrate Stripe customer and subscription creation
3. Add checkout session creation endpoint
4. Add webhook sync for invoice and subscription lifecycle
5. Add payment method list/default/remove APIs
6. Add cancellation and billing-cycle change APIs
7. Add refund request API and operations workflow
8. Replace mock usage with actual usage aggregation
9. Add hosted billing portal session endpoint

## Minimum Viable Backend for This Prototype

If you want the smallest backend that still supports this UI credibly, implement these first:

- `GET /api/billing/overview`
- `POST /api/billing/checkout/session`
- `POST /api/billing/subscription/cancel`
- `POST /api/billing/subscription/billing-cycle`
- `GET /api/billing/payment-methods`
- `POST /api/billing/payment-methods/setup-session`
- `POST /api/billing/payment-methods/{id}/default`
- `DELETE /api/billing/payment-methods/{id}`
- `GET /api/billing/invoices`
- `GET /api/billing/invoices/{id}`
- `POST /api/billing/invoices/{id}/refund-request`
- `GET /api/billing/usage`
- `POST /api/webhooks/stripe`

That set is enough to make the billing page behave credibly while keeping the architecture aligned with a real provider-backed implementation.
