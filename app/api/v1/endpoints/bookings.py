"""Booking endpoints for API v1."""

from fastapi import APIRouter, Depends, Header
from fastapi.responses import JSONResponse

from app.models.schemas.hotel import Booking
from app.api.v1.dependencies.dependencies import get_booking_service

router = APIRouter(prefix="/api/v1")


@router.post("/bookings")
async def create_booking(
        booking_data: Booking,
        authorization: str = Header(),
        book_service=Depends(get_booking_service)
) -> dict:
    
    """Create a new booking for a room."""

    book_id = await book_service.book_room(
        booking_data,
        authorization
    )
    return JSONResponse(
        status_code=201,
        content={
            "message": "Комната забронирована!",
            "booking_id": str(book_id)
        }
    )


@router.get("/bookings/{booking_id}")
async def get_booking(
        booking_id: str,
        book_service=Depends(get_booking_service)
) -> dict:
    
    """Get booking details."""

    booking_data = await book_service.get_booking(booking_id)
    return JSONResponse(
        status_code=200,
        content={
            "message": "Бронирование",
            "data": booking_data
        }
    )


# @router.delete("/bookings/{booking_id}")
# async def cancel_booking(
#         booking_id: str,
#         authorization: str = Header(),
#         book_service=Depends(get_booking_service)
# ) -> dict:
    
#     """Cancel a booking."""

#     await book_service.cancel_booking(booking_id, authorization)
#     return JSONResponse(
#         status_code=200,
#         content={
#             "message": "Бронирование отменено"
#         }
#     )