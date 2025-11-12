"""Rooms repository interface."""

from abc import ABC, abstractmethod
from typing import List, Optional

from motor.motor_asyncio import AsyncIOMotorClient


class RoomsRepository(ABC):
    """Repository interface for room data access."""

    @abstractmethod
    async def get_room(
        self,
        room_id: int,
        hotel_id: int,
        session: AsyncIOMotorClient
    ) -> Optional[dict]:
        """Get a single room by room and hotel id."""

    @abstractmethod
    async def get_rooms(
        self,
        hotel_id: int,
        session: AsyncIOMotorClient
    ) -> List[dict]:
        """Get all rooms for a hotel."""