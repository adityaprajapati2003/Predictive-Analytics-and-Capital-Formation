from app.services import scoring_service
from app.workers.celery_app import celery_app


@celery_app.task
def score_startup(features: dict) -> dict:
    return scoring_service.score(features)
