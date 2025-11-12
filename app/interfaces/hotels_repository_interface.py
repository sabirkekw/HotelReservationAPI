"""Hotels repository interface."""

from abc import ABC, abstractmethod
from typing import List, Optional

from motor.motor_asyncio import AsyncIOMotorClient


class HotelsRepository(ABC):
    """Repository interface for hotel data access."""

    @abstractmethod
    async def get_hotel(
        self,
        id: int,
        session: AsyncIOMotorClient
    ) -> Optional[dict]:
        """Get a single hotel by id."""

    @abstractmethod
    async def get_hotels(
        self,
        session: AsyncIOMotorClient
    ) -> List[dict]:
        """Get all hotels."""
    