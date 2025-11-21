"""Hotel endpoints for API v1."""

from fastapi import APIRouter, Depends
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from app.models.schemas.hotel import Hotel, Room

from app.api.v1.dependencies.dependencies import (
    get_hotels_service,
    get_rooms_service
)

router = APIRouter(prefix="/api/v1")


@router.get("/hotels")
async def list_hotels(hotels_service=Depends(get_hotels_service)) -> dict:
    
    """Get all available hotels."""
    
    hotels_data = await hotels_service.get_all_hotels()
    return JSONResponse(
        status_code=200,
        content={
            "message": "Информация по отелям",
            "data": hotels_data
        }
    )

@router.post("/hotels")
async def create_hotel(
        hotel_data: Hotel,
        hotels_service=Depends(get_hotels_service)
) -> dict:
    
    """Add a new hotel to database."""
    
    hotel = await hotels_service.add_hotel(hotel_data)
    return JSONResponse(
        status_code=201,
        content={
            "message": "Hotel created successfully",
            "hotel_id": str(hotel)
        }
    )


@router.get("/hotels/{hotel_id}")
async def get_hotel(
        hotel_id: str,
        hotels_service=Depends(get_hotels_service),
        rooms_service=Depends(get_rooms_service)
) -> dict:
    
    """Get hotel info with rooms list."""
    
    hotel_data = await hotels_service.get_hotel_info(hotel_id)
    rooms_data = await rooms_service.get_rooms(hotel_id)
    return JSONResponse(
        status_code=200,
        content={
            "message": f"Отель {hotel_id}",
            "hotel_data": hotel_data,
            "rooms_data": rooms_data
        }
    )


@router.get("/hotels/{hotel_id}/rooms")
async def list_hotel_rooms(
        hotel_id: str,
        rooms_service=Depends(get_rooms_service)
) -> dict:
    
    """Get all rooms in a specific hotel."""
    
    rooms_data = await rooms_service.get_rooms(hotel_id)
    return JSONResponse(
        status_code=200,
        content={
            "message": f"Комнаты в отеле {hotel_id}",
            "data": rooms_data
        }
    )


@router.post("/hotels/{hotel_id}/rooms")
async def create_room(
        hotel_id: str,
        room_data: Room,
        rooms_service=Depends(get_rooms_service)
) -> dict:
    
    """Add a new room to a hotel."""
    
    room = await rooms_service.add_room(room_data, hotel_id)
    return JSONResponse(
        status_code=201,
        content={
            "message": "Room created successfully",
            "room_id": str(room)
        }
    )


@router.get("/hotels/{hotel_id}/rooms/{room_id}")
async def get_room(
        hotel_id: str,
        room_id: str,
        rooms_service=Depends(get_rooms_service)
) -> dict:
    
    """Get specific room in a hotel."""
    
    room_data = await rooms_service.get_room(room_id, hotel_id)
    return JSONResponse(
        status_code=200,
        content={
            "message": f"Комната {room_id} в отеле {hotel_id}",
            "data": room_data
        }
    )