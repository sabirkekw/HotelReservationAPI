"""Rooms service for business logic."""

from typing import List, Optional

from app.core.errors import NotFoundError
from app.interfaces.mongo_interface import MongoDBRepository
from motor.motor_asyncio import AsyncIOMotorClient


class RoomsService:
    """Service for room operations."""

    def __init__(
        self,
        session: AsyncIOMotorClient,
        hotels_repo: MongoDBRepository,
        rooms_repo: MongoDBRepository
    ) -> None:
        """Initialize service with session and repositories."""
        self.session = session
        self.hotels_repo = hotels_repo
        self.rooms_repo = rooms_repo

    async def get_room(self, room_id: int, hotel_id: int) -> Optional[dict]:
        """Get room info by room ID and hotel ID."""
        room = await self.rooms_repo.read_one(
            session = self.session,
            room_id = room_id,
            hotel_id = hotel_id,
        )
        if room is None:
            raise NotFoundError("Комната не найдена!")
        return room

    async def get_rooms(self, hotel_id: int) -> List[dict]:
        """Get all rooms for a hotel."""
        rooms = await self.rooms_repo.read_many(
            session = self.session,
            hotel_id = hotel_id, 
        )
        if len(rooms) == 0:
            raise NotFoundError("Комнаты не найдены!")
        return rooms
    