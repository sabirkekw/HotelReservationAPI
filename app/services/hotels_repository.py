"""Hotels repository implementation for MongoDB."""

from typing import List, Optional

from motor.motor_asyncio import AsyncIOMotorClient

from app.interfaces.mongo_interface import HotelsRepository


class HotelsMongoRepository(HotelsRepository):
    """MongoDB implementation of HotelsRepository."""
    async def get_hotel(
        self,
        id: int,
        session: AsyncIOMotorClient
    ) -> Optional[dict]:
        """Get a single hotel by ID."""
        hotel = await session.hotel_db.hotels.find_one({'_id': id})
        return hotel

    async def get_hotels(
        self,
        session: AsyncIOMotorClient
    ) -> List[dict]:
        """Get all hotels."""
        hotels = session.hotel_db.hotels.find()
        return await hotels.to_list()