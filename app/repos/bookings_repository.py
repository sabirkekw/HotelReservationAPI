from app.interfaces.mongo_interface import MongoDBRepository

from typing import List, Optional

from motor.motor_asyncio import AsyncIOMotorClient

from bson import ObjectId

class BookingsMongoRepository(MongoDBRepository):
    async def create(
            self,
            session: AsyncIOMotorClient,
            **kwargs
    ) -> Optional[dict]:
        booking = await session.hotel_db.bookings.insert_one(kwargs['booking_json'])
        return booking.inserted_id

    async def read_one(
            self,
            session: AsyncIOMotorClient,
            **kwargs
    ) -> Optional[dict]:
        """Read a single document by id."""
        booking_data = await session.hotel_db.bookings.find_one({"_id": ObjectId(kwargs["booking_id"])})
        return booking_data
    
    async def read_many(
            self,
            session: AsyncIOMotorClient,
            **kwargs
    ) -> List[dict]:
        """Read all documents in collection."""
        bookings = session.hotel_db.bookings.find()
        return await bookings.to_list()


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