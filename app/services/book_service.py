from motor.motor_asyncio import AsyncIOMotorClient

from app.core.errors import AuthenticationError, NotFoundError
from app.models.schemas.hotel import Booking
from app.interfaces.mongo_interface import MongoDBRepository
from app.services.rooms_service import RoomsService
from app.services.security_service import TokenService

class BookingService:
    def __init__(
            self,
            session: AsyncIOMotorClient,
            bookings_repo: MongoDBRepository,
            rooms_service: RoomsService,
            token_service: TokenService
):
        self.session = session
        self.bookings_repo = bookings_repo
        self.rooms_service = rooms_service
        self.token_service = token_service

    async def book_room(
            self,
            booking_data: Booking,
            token: str,
    ) -> str:
        token_valid = await self.token_service.verify_access_token(token[7:])
        if not token_valid:
            raise AuthenticationError("Токен невалиден!")
        
        room = await self.rooms_service.get_room(
            booking_data._room_id,
            booking_data._hotel_id) # raises 404 if room doesn't exists

        booking_id = await self.bookings_repo.create(
            session=self.session,
            booking_json = booking_data.model_dump())
        
        return booking_id
        
    async def get_booking(self, booking_id: str) -> dict:
        booking = await self.bookings_repo.read_one(session=self.session, booking_id=booking_id)
        if not booking:
            raise NotFoundError("Бронирование не найдено!")
        return booking