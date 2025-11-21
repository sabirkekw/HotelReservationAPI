"""Hotels repository implementation for MongoDB."""

from typing import List, Optional

from motor.motor_asyncio import AsyncIOMotorClient

from app.interfaces.mongo_interface import MongoDBRepository

from app.models.schemas.hotel import Hotel

from bson import ObjectId
from typing import Any


def _convert_object_ids(obj: Any) -> Any:
    """Recursively convert any bson.ObjectId in a document to its string form."""
    if isinstance(obj, ObjectId):
        return str(obj)
    if isinstance(obj, dict):
        return {k: _convert_object_ids(v) for k, v in obj.items()}
    if isinstance(obj, list):
        return [_convert_object_ids(v) for v in obj]
    return obj


class HotelsMongoRepository(MongoDBRepository):
    """MongoDB implementation of HotelsRepository."""
    async def create(
            self,
            session: AsyncIOMotorClient,
            **kwargs
    ) -> Optional[dict]:
        hotel = await session.hotel_db.hotels.insert_one(kwargs['hotel_json'])
        return str(hotel.inserted_id)

    async def read_one(
            self,
            session: AsyncIOMotorClient,
            **kwargs
    ) -> Optional[dict]:
        """Get a single hotel by ID."""
        hotel = await session.hotel_db.hotels.find_one({"_id": ObjectId(kwargs["hotel_id"])})
        if hotel is None:
            return None
        return _convert_object_ids(hotel)

    async def read_many(
            self,
            session: AsyncIOMotorClient,
            **kwargs
    ) -> List[dict]:
        """Get all hotels."""
        hotels = session.hotel_db.hotels.find()
        docs = await hotels.to_list()
        return [_convert_object_ids(d) for d in docs]
    
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