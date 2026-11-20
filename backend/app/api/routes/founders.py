"""Founders routes (stub)."""
from fastapi import APIRouter

router = APIRouter(prefix="/founders", tags=["founders"])


@router.get("/")
def list_founders():
    return []
