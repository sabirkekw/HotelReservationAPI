from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from app.api.v1.dependencies.dependencies import get_hotels_service, get_rooms_service
router = APIRouter(prefix="/api/v1/hotels")

@router.get("")
async def get_hotels(hotels_service = Depends(get_hotels_service)):
    hotels_data = await hotels_service.get_all_hotels()
    return JSONResponse(status_code=200, content={"message": f"Информация по отелям", 
                                                  "data": hotels_data})

@router.get("/{hotel_id}")
async def hotel_info(hotel_id: int, hotels_service = Depends(get_hotels_service), rooms_service = Depends(get_rooms_service)):
    hotel_data = await hotels_service.get_hotel_info(hotel_id)
    rooms_data = await rooms_service.get_rooms(hotel_id)
    return JSONResponse(status_code=200, content={"message": f"Отель {hotel_id}", 
                                                  "hotel_data": hotel_data,
                                                  "rooms_data": rooms_data})

@router.get("/{hotel_id}/{room_id}")
async def room_info(hotel_id: int, room_id: int, rooms_service = Depends(get_rooms_service)):
    room_data = await rooms_service.get_room(room_id, hotel_id)
    return JSONResponse(status_code=200, content={"message": f"Комната {room_id} в отеле {hotel_id} ",
                                                  "data": room_data})

# @router.get("/{hotel_id}/{room_id}/book")
# async def book_room(room_id: int, jwt: str, book_service = Depends(get_book_service)):
#     book_id = await book_service.book(room_id, jwt)
#     return JSONResponse(status_code=201, content={"message": f"Комната успешно забронирована!", "data": f"ID бронирования: {book_id}"})