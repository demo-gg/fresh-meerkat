from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal
from typing import Optional


@dataclass
class PaymentIntent:
    """Represents a Stripe PaymentIntent."""

    id: str
    status: str
    amount: Decimal
    currency: str
    customer_id: Optional[str]
    created_at: datetime

    @classmethod
    def from_stripe(cls, obj: dict) -> "PaymentIntent":
        """Convert Stripe PaymentIntent response to model."""
        return cls(
            id=obj["id"],
            status=obj["status"],
            amount=Decimal(obj["amount"]) / 100,
            currency=obj["currency"],
            customer_id=obj.get("customer"),
            created_at=datetime.fromtimestamp(obj["created"]),
        )


@dataclass
class Customer:
    """Represents a Stripe Customer."""

    id: str
    email: Optional[str]
    description: Optional[str]
    name: Optional[str]

    @classmethod
    def from_stripe(cls, obj: dict) -> "Customer":
        """Convert Stripe Customer response to model."""
        return cls(
            id=obj["id"],
            email=obj.get("email"),
            description=obj.get("description"),
            name=obj.get("name"),
        )
