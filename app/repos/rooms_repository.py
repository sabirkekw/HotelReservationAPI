"""Rooms repository implementation for MongoDB."""

from typing import List, Optional, Any

from motor.motor_asyncio import AsyncIOMotorClient

from app.interfaces.mongo_interface import MongoDBRepository
from app.models.schemas.hotel import Room, Hotel

from bson import ObjectId

def _convert_object_ids(obj: Any) -> Any:
    """Recursively convert any bson.ObjectId in a document to its string form."""
    if isinstance(obj, ObjectId):
        return str(obj)
    if isinstance(obj, dict):
        return {k: _convert_object_ids(v) for k, v in obj.items()}
    if isinstance(obj, list):
        return [_convert_object_ids(v) for v in obj]
    return obj

class RoomsMongoRepository(MongoDBRepository):
    """MongoDB implementation of RoomsRepository."""
    async def create(
            self,
            session: AsyncIOMotorClient,
            **kwargs
    ) -> Optional[dict]:
        room = await session.hotel_db.rooms.insert_one(kwargs['room_json'])
        return str(room.inserted_id)

    async def read_one(
            self,
            session: AsyncIOMotorClient,
            **kwargs
    ) -> Optional[dict]:
        """Get a single room by room ID and hotel ID."""
        room = await session.hotel_db.rooms.find_one({
            '_id': ObjectId(kwargs['room_id']),
            '_hotel_id': ObjectId(kwargs['hotel_id'])
        })
        if room is None:
            return None
        return _convert_object_ids(room)

    async def read_many(
            self,
            session: AsyncIOMotorClient,
            **kwargs
    ) -> List[dict]:
        """Get all rooms for a hotel."""
        rooms = session.hotel_db.rooms.find({'_hotel_id': ObjectId(kwargs['hotel_id'])})
        rooms_list = await rooms.to_list()
        return _convert_object_ids(rooms_list)
    
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