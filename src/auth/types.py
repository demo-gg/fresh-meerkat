from typing import Literal, TypedDict


class StripeChargeRequest(TypedDict, total=False):
    """Type definition for Stripe charge request parameters."""

    amount: int
    currency: str
    customer: str
    description: str
    metadata: dict[str, str]
    idempotency_key: str


class StripeWebhookEvent(TypedDict):
    """Type definition for Stripe webhook event."""

    id: str
    type: str
    object: str
    data: dict
    created: int


PaymentStatus = Literal[
    "succeeded", "processing", "requires_payment_method", "canceled"
]
