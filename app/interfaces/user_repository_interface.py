from sqlalchemy.ext.asyncio import AsyncSession
from app.models.schemas.auth import LoginData
from app.models.sqlmodels.user import DatabaseUser
from abc import ABC, abstractmethod

class UserRepository(ABC):

    @abstractmethod
    async def add_user(self, user: DatabaseUser, session: AsyncSession):
        """Add a user to storage and return its id."""
        pass

    @abstractmethod
    async def fetch_user(self, data: LoginData, session: AsyncSession):
        """Fetch and return a user by login data (or None)."""
        pass