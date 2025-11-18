from app.interfaces.mongo_interface import MongoDBRepository

from typing import List, Optional

from motor.motor_asyncio import AsyncIOMotorClient

class BookingsMongoRepository(MongoDBRepository):
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
        """Read a single document by id."""
        room_data = await session.hotel_db.hotels.find_one({"_id": id})
        return room_data
    
    async def read_many(
            self,
            session: AsyncIOMotorClient,
            **kwargs
    ) -> List[dict]:
        """Read all documents in collection."""
        rooms = session.hotel_db.hotels.find()
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