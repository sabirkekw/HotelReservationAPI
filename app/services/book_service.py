from motor.motor_asyncio import AsyncIOMotorClient

from app.core.errors import AuthenticationError

from app.interfaces.rooms_repository_interface import RoomsRepository
from app.interfaces.bookings_repository_interface import BookingsRepository
from app.services.rooms_service import RoomsService
from app.services.security_service import TokenService

class BookingService:
    def __init__(
            self,
            session: AsyncIOMotorClient,
            bookings_repo: BookingsRepository,
            rooms_service: RoomsService,
            token_service: TokenService
):
        self.session = session
        self.bookings_repo = bookings_repo
        self.rooms_service = rooms_service
        self.token_serivce = token_service

    async def book_room(
            self,
            hotel_id: int,
            room_id: int,
            token: str,
    ) -> int:
        token_valid = await self.token_serivce.verify_access_token(token[7:])
        if not token_valid:
            raise AuthenticationError("Токен невалиден!")
        
        room = await self.rooms_service.get_room(room_id, hotel_id) # raises 404 if room doesn't exists

        booking = await self.bookings_repo.book_room(room_id, hotel_id, self.session)
        