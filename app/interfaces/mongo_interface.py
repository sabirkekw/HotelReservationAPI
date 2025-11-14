"""Hotels repository interface."""

from abc import ABC, abstractmethod
from typing import List, Optional

from motor.motor_asyncio import AsyncIOMotorClient


class MongoDBRepository(ABC):
    """Repository interface for hotel, rooms and bookings data access."""

    @abstractmethod
    async def create(
            self,
            data,
            session: AsyncIOMotorClient
    ) -> Optional[dict]:
        """Create a single document."""

    @abstractmethod
    async def read_one(
            self,
            id: str,
            session: AsyncIOMotorClient
    ) -> Optional[dict]:
        """Read a single document by id."""

    @abstractmethod
    async def read_many(
            self,
            session: AsyncIOMotorClient
    ) -> List[dict]:
        """Read all documents in collection."""

    @abstractmethod
    async def update(
            self,
            session: AsyncIOMotorClient
    ) -> Optional[dict]:
        """Update document info."""
    
    @abstractmethod
    async def delete(
            self,
            id: str,
            session: AsyncIOMotorClient
    ) -> Optional[dict]:
        """Delete single document by ID."""