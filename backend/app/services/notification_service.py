"""Notifications (email/in-app). Only send for purposes the user consented to."""


def send(user_id: int, message: str) -> None:
    # TODO: check consent (core.consent.has_consent) and enqueue delivery.
    print(f"notify user={user_id}: {message}")
