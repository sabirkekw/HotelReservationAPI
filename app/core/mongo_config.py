from motor.motor_asyncio import AsyncIOMotorClient
from typing import AsyncGenerator
from app.core.config import settings

class MongoDatabase:
    def __init__(self, url: str, name: str):
        self.db_name = name
        self.client = AsyncIOMotorClient(url)

    async def get_session(self) -> AsyncGenerator[AsyncIOMotorClient, None]:
        yield self.client

database = MongoDatabase(settings.mongo_url, settings.mongo_db)

get_session = database.get_session