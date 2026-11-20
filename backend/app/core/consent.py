"""DPDP Act 2023 support: record and check user consent for each processing purpose.

TODO: persist to the `consent_records` table, add withdrawal, retention and
access-request handling, and review with legal counsel before launch.
"""
from dataclasses import dataclass
from datetime import datetime, timezone

PURPOSES = {"scoring", "matching", "notifications", "model_improvement"}


@dataclass
class ConsentRecord:
    user_id: int
    purpose: str
    granted: bool
    recorded_at: datetime

    @staticmethod
    def new(user_id: int, purpose: str, granted: bool) -> "ConsentRecord":
        if purpose not in PURPOSES:
            raise ValueError(f"Unknown purpose: {purpose}")
        return ConsentRecord(user_id, purpose, granted, datetime.now(timezone.utc))


def has_consent(records: list[ConsentRecord], purpose: str) -> bool:
    """Latest record for the purpose decides."""
    relevant = [r for r in records if r.purpose == purpose]
    return bool(relevant) and max(relevant, key=lambda r: r.recorded_at).granted
