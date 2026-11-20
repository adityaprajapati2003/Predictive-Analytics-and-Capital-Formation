import numpy as np
import shap


def make_explainer(model):
    return shap.TreeExplainer(model)


def top_factors(explainer, X_row, feature_names, k=5):
    """Return the k features with the largest absolute SHAP contribution for one row."""
    values = explainer.shap_values(X_row)
    values = np.asarray(values).reshape(-1)
    order = np.argsort(-np.abs(values))[:k]
    return [{"feature": feature_names[i], "contribution": float(values[i])} for i in order]
