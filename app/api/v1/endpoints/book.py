"""Booking endpoints for API v1."""

from fastapi import APIRouter

router = APIRouter(prefix="/api/v1/hotels")


@router.get("/{room_id}")
async def room_info() -> dict:
    """Get room info by ID (TODO: implement)."""
    pass


@router.post("/{room_id}")
async def book() -> dict:
    """Book a room (TODO: implement with JWT auth)."""
    pass

