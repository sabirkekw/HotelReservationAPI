"""Bookings repository interface."""

from abc import ABC, abstractmethod
from typing import List, Optional

from motor.motor_asyncio import AsyncIOMotorClient


class BookingsRepository(ABC):
    """Repository interface for hotel data access."""

    @abstractmethod
    async def book_room(
        self,
        room_id: int,
        hotel_id: int,
        session: AsyncIOMotorClient
    ) -> Optional[dict]:
        """Add a booking to database."""
        pass