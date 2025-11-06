from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

router = APIRouter(prefix="api/v1/hotels")

@router.get("/")
async def get_hotels():
    pass # return list of hotels ID to front

@router.get("/{hotel_name}")
async def hotel_info():
    pass # returns list of rooms ID to front