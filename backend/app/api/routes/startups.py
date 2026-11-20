"""Startups routes (stub)."""
from fastapi import APIRouter

router = APIRouter(prefix="/startups", tags=["startups"])


@router.get("/")
def list_startups():
    return []
