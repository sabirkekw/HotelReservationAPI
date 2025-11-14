"""User repository interface."""

from abc import ABC, abstractmethod
from typing import Optional, List

from sqlalchemy.ext.asyncio import AsyncSession

from app.models.schemas.auth import LoginData
from app.models.sqlmodels.user import DatabaseUser


class SQLRepository(ABC):
    """Repository interface for user data access."""

    @abstractmethod
    async def create(
        self,
        user: DatabaseUser,
        session: AsyncSession,
        hashed_password: str
    ) -> Optional[int]:
        """Add a new string to table."""

    @abstractmethod
    async def read_one(
        self,
        data: LoginData,
        session: AsyncSession
    ) -> Optional[DatabaseUser]:
        """Read single string."""

    @abstractmethod
    async def read_many(
        self,
        data,
        session: AsyncSession
    ) -> List:
        """Read all strings from table."""

    @abstractmethod
    async def update(
        self,
        data,
        session: AsyncSession
    ) -> Optional[]