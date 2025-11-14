from app.interfaces.bookings_repository_interface import BookingsRepository

from typing import List, Optional

from motor.motor_asyncio import AsyncIOMotorClient

class BookingsMongoRepository(BookingsRepository):
    async def book_room(
        self,
        room_id: int,
        hotel_id: int,
        session: AsyncIOMotorClient
    ) -> Optional[dict]:
        pass 