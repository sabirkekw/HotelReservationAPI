from app.interfaces.rooms_repository_interface import RoomsRepository
from motor.motor_asyncio import AsyncIOMotorClient

class RoomsMongoRepository(RoomsRepository):
    async def get_room(self, room_id: int, hotel_id: int, session: AsyncIOMotorClient):
        room = await session.hotel_db.rooms.find_one({'_id': room_id, '_hotel_id': hotel_id})
        return room
    
    async def get_rooms(self, hotel_id: int, session: AsyncIOMotorClient):
        rooms = session.hotel_db.rooms.find({'_hotel_id': hotel_id})
        return await rooms.to_list()