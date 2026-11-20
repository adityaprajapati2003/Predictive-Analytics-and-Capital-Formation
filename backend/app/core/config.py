"""Application settings, read from environment variables."""
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    database_url: str = "sqlite:///./dev.db"
    redis_url: str = "redis://localhost:6379/0"
    jwt_secret: str = "change_me"
    jwt_algorithm: str = "HS256"
    model_path: str = "/models/fundability_model.joblib"
    calibrator_path: str = "/models/calibrator.joblib"


settings = Settings()
