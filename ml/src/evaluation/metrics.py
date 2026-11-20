import numpy as np
from sklearn.metrics import average_precision_score, brier_score_loss, roc_auc_score


def expected_calibration_error(y_true, probs, bins=10) -> float:
    y_true, probs = np.asarray(y_true), np.asarray(probs)
    edges = np.linspace(0, 1, bins + 1)
    ece = 0.0
    for lo, hi in zip(edges[:-1], edges[1:]):
        m = (probs > lo) & (probs <= hi)
        if m.any():
            ece += m.mean() * abs(y_true[m].mean() - probs[m].mean())
    return float(ece)


def report(y_true, probs) -> dict:
    return {
        "pr_auc": float(average_precision_score(y_true, probs)),
        "roc_auc": float(roc_auc_score(y_true, probs)),
        "brier": float(brier_score_loss(y_true, probs)),
        "ece": expected_calibration_error(y_true, probs),
        "base_rate": float(np.mean(y_true)),
    }
