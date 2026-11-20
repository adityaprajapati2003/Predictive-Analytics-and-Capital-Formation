"""Fundability score routes."""
from fastapi import APIRouter

from app.services import readiness_service, scoring_service

router = APIRouter(prefix="/scores", tags=["scores"])


@router.post("/predict")
def predict(features: dict):
    """Return calibrated probability, SHAP contributions and a readiness report."""
    result = scoring_service.score(features)
    result["readiness"] = readiness_service.assess(features)
    return result
