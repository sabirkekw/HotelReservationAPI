from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from app.api.v1.dependencies.dependencies import get_hotels_service

router = APIRouter(prefix="/api/v1/hotels")

@router.get("")
async def get_hotels(hotels_service = Depends(get_hotels_service)):
    hotels_data = await hotels_service.get_all_hotels()
    return JSONResponse(status_code=200, content={"message": f"all registered hotels info", "data": hotels_data})

@router.get("/{hotel_id}")
async def hotel_info(hotel_id: int, hotels_service = Depends(get_hotels_service)):
    hotel_data = await hotels_service.get_hotel_info(hotel_id)
    return JSONResponse(status_code=200, content={"message": f"one hotel info", "data": hotel_data})