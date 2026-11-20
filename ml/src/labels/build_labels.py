"""Censoring-aware fundability labels (see configs/label_definition.yaml)."""
import pandas as pd


def build_labels(startups: pd.DataFrame, rounds: pd.DataFrame, prediction_date: str,
                 horizon_months: int = 12, observed_until: str | None = None,
                 qualifying=("pre_seed", "seed", "series_a", "series_b")) -> pd.DataFrame:
    """Return startup_id, label (1/0/NaN) and status.

    startups needs: startup_id, coverage_ok (bool)
    rounds needs:   startup_id, round_type, announced_on
    """
    start = pd.Timestamp(prediction_date)
    end = start + pd.DateOffset(months=horizon_months)
    observed = pd.Timestamp(observed_until) if observed_until else None

    r = rounds[rounds["round_type"].isin(qualifying)].copy()
    r["announced_on"] = pd.to_datetime(r["announced_on"])
    funded_ids = set(r[(r["announced_on"] > start) & (r["announced_on"] <= end)]["startup_id"])

    out = []
    for _, row in startups.iterrows():
        sid = row["startup_id"]
        if sid in funded_ids:
            out.append((sid, 1.0, "funded"))
        elif observed is not None and observed < end:
            out.append((sid, float("nan"), "censored_window"))
        elif not row.get("coverage_ok", True):
            out.append((sid, float("nan"), "unknown_coverage"))
        else:
            out.append((sid, 0.0, "not_funded"))
    return pd.DataFrame(out, columns=["startup_id", "label", "status"])
