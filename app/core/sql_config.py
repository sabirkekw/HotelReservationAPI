"""SQL database configuration."""

from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    create_async_engine
)
from sqlmodel import SQLModel
from sqlalchemy.orm import sessionmaker

from app.core.config import settings


class SQLDatabase:
    """SQL database manager."""

    def __init__(self, url: str) -> None:
        """Initialize database with connection string."""
        self.url = url
        self.engine: AsyncEngine = create_async_engine(
            self.url,
            echo=False
        )
        self.AsyncSessionLocal = sessionmaker(
            self.engine,
            class_=AsyncSession,
            expire_on_commit=False
        )

    async def create_tables(self) -> None:
        """Create all tables in database."""
        async with self.engine.begin() as conn:
            await conn.run_sync(SQLModel.metadata.create_all)

    async def get_session(self) -> AsyncGenerator[AsyncSession, None]:
        """Get database session."""
        async with self.AsyncSessionLocal() as session:
            yield session


database = SQLDatabase(settings.sql_database_url)

create_tables = database.create_tables
get_session = database.get_session
engine = database.engine

