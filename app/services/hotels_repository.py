from app.interfaces.hotels_repository_interface import HotelsRepository
from motor.motor_asyncio import AsyncIOMotorClient

class HotelsMongoRepository(HotelsRepository):
    async def get_hotel(self, id: int, session):
        hotel = await session.hotel_db.hotels.find_one({'_id': id})
        return hotel

    async def get_hotels(self, session: AsyncIOMotorClient):
        hotels = session.hotel_db.hotels.find()
        return await hotels.to_list()