from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

router = APIRouter(prefix="api/v1/hotels/{hotel_name}")

@router.get("/{room_id}")
async def room_info():
    pass # returns room info by ID to front

@router.post("/{room_id}")
async def book():
    pass # make a book (with jwtauth), returns http response to front

