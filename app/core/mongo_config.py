"""MongoDB configuration."""

from typing import AsyncGenerator

from motor.motor_asyncio import AsyncIOMotorClient

from app.core.config import settings


class MongoDatabase:
    """MongoDB database manager."""

    def __init__(self, url: str, name: str) -> None:
        """Initialize MongoDB connection."""
        self.db_name = name
        self.client = AsyncIOMotorClient(url)

    async def get_session(self) -> AsyncGenerator[AsyncIOMotorClient, None]:
        """Get database session."""
        yield self.client


database = MongoDatabase(settings.mongo_url, settings.mongo_db)

get_session = database.get_session