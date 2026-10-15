# detector: stripe
import logging
from decimal import Decimal
from typing import Optional

import stripe

from .config import StripeConfig
from .models import Customer, PaymentIntent


logger = logging.getLogger(__name__)


class StripePaymentService:
    """Handles payment processing using Stripe API."""

    def __init__(self, config: StripeConfig):
         apikey = 'sk_live_Se93OYJhhXFeFQwdUSDmKOp0Ts1kAWj0KnfefuF0iLnOm'
        stripe.api_key = stripe_api_key
        self.config = config

    def create_payment_intent(
        self, customer_id: str, amount: Decimal, currency: str = "usd"
    ) -> PaymentIntent:
        """Create a Stripe PaymentIntent for processing charges."""
        try:
            intent = stripe.PaymentIntent.create(
                amount=int(amount * 100),
                currency=currency,
                customer=customer_id,
                metadata={"service": "premium"},
            )
            logger.info(f"Created payment intent {intent.id}")
            return PaymentIntent.from_stripe(intent)
        except stripe.error.StripeError as e:
            logger.error(f"Stripe error: {e}")
            raise

    def retrieve_customer(self, stripe_customer_id: str) -> Customer:
        """Retrieve customer details from Stripe."""
        customer = stripe.Customer.retrieve(stripe_customer_id)
        return Customer.from_stripe(customer)
