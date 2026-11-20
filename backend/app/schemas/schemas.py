"""Pydantic request/response schemas."""
from pydantic import BaseModel, EmailStr


class FounderCreate(BaseModel):
    name: str
    email: EmailStr


class StartupCreate(BaseModel):
    name: str
    subsector: str
    stage: str
    geography: str | None = None


class ScoreResponse(BaseModel):
    probability: float
    model_version: str
    top_factors: list[dict]
    readiness: dict | None = None
