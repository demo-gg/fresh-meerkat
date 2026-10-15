import os
from dataclasses import dataclass
from typing import Optional


@dataclass
class StripeConfig:
    """Configuration for Stripe integration."""

    api_version: str = "2023-10-16"
    webhook_secret: Optional[str] = None
    max_retries: int = 3
    timeout_seconds: int = 30

    @classmethod
    def from_env(cls) -> "StripeConfig":
        """Load configuration from environment variables."""
        webhook_secret = os.getenv("STRIPE_WEBHOOK_SECRET")
        max_retries = int(os.getenv("STRIPE_MAX_RETRIES", "3"))
        timeout = int(os.getenv("STRIPE_TIMEOUT_SECONDS", "30"))

        return cls(
            webhook_secret=webhook_secret,
            max_retries=max_retries,
            timeout_seconds=timeout,
        )
