import pandas as pd


def temporal_split(df: pd.DataFrame, date_col: str, train_end: str, val_end: str):
    """Chronological split. Never shuffle: it leaks the future into training."""
    d = pd.to_datetime(df[date_col])
    train = df[d <= pd.Timestamp(train_end)]
    val = df[(d > pd.Timestamp(train_end)) & (d <= pd.Timestamp(val_end))]
    test = df[d > pd.Timestamp(val_end)]
    return train, val, test
