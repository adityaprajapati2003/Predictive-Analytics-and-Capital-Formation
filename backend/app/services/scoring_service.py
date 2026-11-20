"""Load the trained model and calibrator, return probability + explanation."""
import os
from functools import lru_cache

import joblib

from app.core.config import settings


@lru_cache
def _load():
    if not (os.path.exists(settings.model_path) and os.path.exists(settings.calibrator_path)):
        return None, None
    return joblib.load(settings.model_path), joblib.load(settings.calibrator_path)


def score(features: dict) -> dict:
    model, calibrator = _load()
    if model is None:
        return {"probability": None, "model_version": "none",
                "top_factors": [], "note": "No trained model found. Train one in ml/ first."}
    # TODO: align `features` to the training column order, then call SHAP (ml/src/explain).
    raise NotImplementedError("Wire feature alignment and SHAP explanation here.")
