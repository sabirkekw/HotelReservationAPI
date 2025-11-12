"""User repository implementation for SQL."""

from typing import Optional

from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import select

from app.interfaces.user_repository_interface import UserRepository
from app.models.schemas.auth import LoginData
from app.models.sqlmodels.user import DatabaseUser


class UserSQLRepository(UserRepository):
    """SQL implementation of UserRepository."""

    async def add_user(
        self,
        user: DatabaseUser,
        session: AsyncSession,
        hashed_password: str
    ) -> Optional[int]:
        """Add a new user to database."""
        db_user_data = DatabaseUser(
            name=user.name,
            surname=user.surname,
            mail=user.mail,
            password=hashed_password
        )
        session.add(db_user_data)
        await session.commit()
        await session.refresh(db_user_data)
        return db_user_data.id

    async def fetch_user(
        self,
        data: LoginData,
        session: AsyncSession
    ) -> Optional[DatabaseUser]:
        """Fetch a user by email."""
        user_data = await session.execute(
            select(DatabaseUser).where(DatabaseUser.mail == data.mail)
        )
        return user_data.scalars().first()