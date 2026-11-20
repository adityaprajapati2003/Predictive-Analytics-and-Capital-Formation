# Fundability Platform

Predictive analytics for FinTech fundraising (India focus): a calibrated, explainable
funding-probability score, a founder-readiness assessment and an investor-compatibility ranking.

> Starter skeleton. No dataset is included and no model has been trained.

## Layout
- `backend/`   FastAPI service (API, services, async workers)
- `ml/`        label construction, features, training, calibration, SHAP, fairness, evaluation, matching
- `pipelines/` ingestion flows and provenance validators
- `frontend/`  React + TypeScript dashboards
- `db/`        schema and seed data
- `infra/`     deployment and monitoring config
- `docs/`      diagrams and paper files

## Quick start
```bash
cp .env.example .env
docker compose up --build
# API docs:  http://localhost:8000/docs
# Frontend:  http://localhost:5173
```

## Build order
1. `ml/configs/label_definition.yaml` -> `ml/src/labels/build_labels.py`
2. Features -> baseline logit -> gradient boosting -> calibration -> SHAP
3. Temporal evaluation (`ml/src/evaluation`) and fairness audit (`ml/src/fairness`)
4. Wire the model into `backend/app/services/scoring_service.py`
5. Frontend dashboards, then matching and notifications
