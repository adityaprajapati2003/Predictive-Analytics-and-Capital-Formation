"""Join founder, startup and market features into one leakage-safe table.

Rule: for a given prediction_date, use only information dated on or before it.
"""
import pandas as pd


def build_feature_table(startups: pd.DataFrame, market: pd.DataFrame,
                        prediction_date: str) -> pd.DataFrame:
    snap = market[market["date"] <= pd.Timestamp(prediction_date)].sort_values("date").tail(1)
    for col in snap.columns.drop("date"):
        startups[col] = snap.iloc[0][col]
    startups["prediction_date"] = pd.Timestamp(prediction_date)
    return startups
