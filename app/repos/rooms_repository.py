"""Rooms repository implementation for MongoDB."""

from typing import List, Optional

from motor.motor_asyncio import AsyncIOMotorClient

from app.interfaces.mongo_interface import MongoDBRepository


class RoomsMongoRepository(MongoDBRepository):
    """MongoDB implementation of RoomsRepository."""
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
        """Get a single room by room ID and hotel ID."""
        room = await session.hotel_db.rooms.find_one(
            {'_id': kwargs['room_id'], '_hotel_id': kwargs['hotel_id']}
        )
        return room

    async def read_many(
            self,
            session: AsyncIOMotorClient,
            **kwargs
    ) -> List[dict]:
        """Get all rooms for a hotel."""
        rooms = session.hotel_db.rooms.find({'_hotel_id': kwargs['hotel_id']})
        return await rooms.to_list()
    
    async def update(
            self,
            session: AsyncIOMotorClient,
            **kwargs
    ) -> Optional[dict]:
        """Update document info."""
        pass
    
    async def delete(
            self,
            session: AsyncIOMotorClient,
            **kwargs
    ) -> Optional[dict]:
        """Delete single document by ID."""
        pass