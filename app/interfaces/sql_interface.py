"""User repository interface."""

from abc import ABC, abstractmethod
from typing import Optional, List, Any

from sqlalchemy.ext.asyncio import AsyncSession

from app.models.schemas.auth import LoginData
from app.models.sqlmodels.user import DatabaseUser


class SQLRepository(ABC):
    """Repository interface for user data access."""

    @abstractmethod
    async def create(
        self,
        data: Any,
        session: AsyncSession,
        hashed_password: str = None
    ) -> int:
        """Add a new string to table."""

    @abstractmethod
    async def read_one(
        self,
        data: Any,
        session: AsyncSession
    ) -> Any:
        """Read single string."""

    @abstractmethod
    async def read_many(
        self,
        session: AsyncSession
    ) -> List:
        """Read all strings from table."""

    @abstractmethod
    async def update(
        self,
        data: Any,
        session: AsyncSession
    ) -> Any:
        """Update single string."""

    @abstractmethod
    async def delete(
        self,
        id: int,
        session: AsyncSession
    ) -> Any:
        """Delete single string."""