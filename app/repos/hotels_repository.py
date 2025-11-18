"""Hotels repository implementation for MongoDB."""

from typing import List, Optional

from motor.motor_asyncio import AsyncIOMotorClient

from app.interfaces.mongo_interface import MongoDBRepository


class HotelsMongoRepository(MongoDBRepository):
    """MongoDB implementation of HotelsRepository."""
    async def create(
            self,
            session: AsyncIOMotorClient,
            **kwargs
    ) -> Optional[dict]:
        """Create a single document."""
        pass

    async def read_one(
            self,
            session: AsyncIOMotorClient,
            **kwargs
    ) -> Optional[dict]:
        """Get a single hotel by ID."""
        hotel = await session.hotel_db.hotels.find_one({'_id': kwargs["hotel_id"]})
        return hotel

    async def read_many(
            self,
            session: AsyncIOMotorClient,
            **kwargs
    ) -> List[dict]:
        """Get all hotels."""
        hotels = session.hotel_db.hotels.find()
        return await hotels.to_list()
    
    async def update(
            self,
            session: AsyncIOMotorClient,
            **kwargs
    ) -> Optional[dict]:
        """Update document info."""
    
    async def delete(
            self,
            session: AsyncIOMotorClient,
            **kwargs
    ) -> Optional[dict]:
        """Delete single document by ID."""