"""Auth routes (stub)."""
from fastapi import APIRouter

router = APIRouter(prefix="/auth", tags=["auth"])


@router.get("/")
def list_auth():
    return []
