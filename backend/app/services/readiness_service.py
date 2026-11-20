"""Founder-readiness: how complete and verifiable is the evidence supplied?

This is NOT a prediction. It reports missing items so the founder can fix them.
"""
REQUIRED = ["subsector", "stage", "revenue_growth", "burn_rate", "runway_months",
            "customer_count", "team_size", "pitch_deck"]


def assess(evidence: dict) -> dict:
    missing = [k for k in REQUIRED if evidence.get(k) in (None, "", [])]
    unverified = [k for k, v in evidence.items()
                  if isinstance(v, dict) and not v.get("verified", False)]
    completeness = 1 - len(missing) / len(REQUIRED)
    return {"completeness": round(completeness, 2), "missing": missing, "unverified": unverified}
