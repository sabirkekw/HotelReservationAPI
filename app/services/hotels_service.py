"""Hotels service for business logic."""

from typing import List, Optional

from app.core.errors import NotFoundError
from app.interfaces.mongo_interface import HotelsRepository
from motor.motor_asyncio import AsyncIOMotorClient


class HotelsService:
    """Service for hotel operations."""

    def __init__(
        self,
        session: AsyncIOMotorClient,
        hotels_repo: HotelsRepository
    ) -> None:
        """Initialize service with session and repository."""
        self.session = session
        self.hotels_repo = hotels_repo

    async def get_all_hotels(self) -> List[dict]:
        """Get all hotels from repository."""
        hotels = await self.hotels_repo.get_hotels(self.session)
        if len(hotels) == 0:
            raise NotFoundError("Отели не найдены!")
        return hotels

    async def get_hotel_info(self, hotel_id: int) -> Optional[dict]:
        """Get hotel info by ID."""
        hotel = await self.hotels_repo.get_hotel(hotel_id, self.session)
        if not hotel:
            raise NotFoundError("Отель не найден!")
        return hotel