from sqlmodel import SQLModel
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, AsyncEngine
from sqlalchemy.orm import sessionmaker
from typing import AsyncGenerator
from app.core.config import settings


class Database:
    """Database wrapper that holds engine and sessionmaker and exposes
    `create_tables` and `get_session` as instance methods. This lets us pass
    `database.get_session` directly to FastAPI's Depends as an async generator.
    """

    def __init__(self, url: str):
        self.url = url
        self.engine: AsyncEngine = create_async_engine(self.url, echo=False)
        self.AsyncSessionLocal = sessionmaker(
            self.engine, class_=AsyncSession, expire_on_commit=False
        )

    async def create_tables(self) -> None:
        async with self.engine.begin() as conn:
            await conn.run_sync(SQLModel.metadata.create_all)

    async def get_session(self) -> AsyncGenerator[AsyncSession, None]:
        async with self.AsyncSessionLocal() as session:
            yield session


# Module-level instance used across the app
database = Database(settings.database_url)

# Backwards-compatible names (optional): other modules can still import
# `create_tables`, `engine`, `get_session` if they expect module-level symbols.
create_tables = database.create_tables
get_session = database.get_session
engine = database.engine

