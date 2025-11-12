"""Rooms repository implementation for MongoDB."""

from typing import List, Optional

from motor.motor_asyncio import AsyncIOMotorClient

from app.interfaces.rooms_repository_interface import RoomsRepository


class RoomsMongoRepository(RoomsRepository):
    """MongoDB implementation of RoomsRepository."""

    async def get_room(
        self,
        room_id: int,
        hotel_id: int,
        session: AsyncIOMotorClient
    ) -> Optional[dict]:
        """Get a single room by room ID and hotel ID."""
        room = await session.hotel_db.rooms.find_one(
            {'_id': room_id, '_hotel_id': hotel_id}
        )
        return room

    async def get_rooms(
        self,
        hotel_id: int,
        session: AsyncIOMotorClient
    ) -> List[dict]:
        """Get all rooms for a hotel."""
        rooms = session.hotel_db.rooms.find({'_hotel_id': hotel_id})
        return await rooms.to_list()