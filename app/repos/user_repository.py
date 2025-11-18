"""User repository implementation for SQL."""

from typing import Optional, List, Any

from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import select

from app.interfaces.sql_interface import SQLRepository
from app.models.schemas.auth import LoginData
from app.models.sqlmodels.user import DatabaseUser


class UserSQLRepository(SQLRepository):
    """Repository for user data access."""

    async def create(
        self,
        data: DatabaseUser,
        session: AsyncSession,
        hashed_password: str
    ) -> Optional[int]:
        """Add a new user to database."""
        db_user_data = DatabaseUser(
            name=data.name,
            surname=data.surname,
            mail=data.mail,
            password=hashed_password
        )
        session.add(db_user_data)
        await session.commit()
        await session.refresh(db_user_data)
        return db_user_data.id

    async def read_one(
        self,
        data: LoginData,
        session: AsyncSession
    ) -> Optional[DatabaseUser]:
        """Fetch a user by email."""
        user_data = await session.execute(
            select(DatabaseUser).where(DatabaseUser.mail == data.mail)
        )
        return user_data.scalars().first()

    async def read_many(
        self,
        session: AsyncSession
    ) -> List:
        """Read all strings from table."""
        pass

    async def update(
        self,
        data: Any,
        session: AsyncSession
    ) -> Any:
        """Update single string."""
        pass

    async def delete(
        self,
        id: int,
        session: AsyncSession
    ) -> Any:
        """Delete single string."""
        pass