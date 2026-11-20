"""Investors routes (stub)."""
from fastapi import APIRouter

router = APIRouter(prefix="/investors", tags=["investors"])


@router.get("/")
def list_investors():
    return []
