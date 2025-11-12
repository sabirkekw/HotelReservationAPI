"""User repository interface."""

from abc import ABC, abstractmethod
from typing import Optional

from sqlalchemy.ext.asyncio import AsyncSession

from app.models.schemas.auth import LoginData
from app.models.sqlmodels.user import DatabaseUser


class UserRepository(ABC):
    """Repository interface for user data access."""

    @abstractmethod
    async def add_user(
        self,
        user: DatabaseUser,
        session: AsyncSession,
        hashed_password: str
    ) -> Optional[int]:
        """Add a new user to database."""

    @abstractmethod
    async def fetch_user(
        self,
        data: LoginData,
        session: AsyncSession
    ) -> Optional[DatabaseUser]:
        """Fetch a user by email."""