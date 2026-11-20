"""Fairness audit. Protected attributes are used here ONLY, never as model inputs."""
import numpy as np
import pandas as pd


def group_report(y_true, y_pred, groups, threshold=0.5) -> pd.DataFrame:
    y_true, y_pred, groups = map(np.asarray, (y_true, y_pred, groups))
    pred_pos = y_pred >= threshold
    rows = []
    for g in np.unique(groups):
        m = groups == g
        pos = y_true[m] == 1
        tpr = pred_pos[m][pos].mean() if pos.any() else np.nan
        rows.append({"group": g, "n": int(m.sum()),
                     "selection_rate": float(pred_pos[m].mean()),
                     "true_positive_rate": float(tpr)})
    return pd.DataFrame(rows)
