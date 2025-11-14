"""Dependency injection configuration."""

from contextlib import asynccontextmanager

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from motor.motor_asyncio import AsyncIOMotorClient

from app.core.mongo_config import database as mongo_database
from app.core.sql_config import database as sql_database

from app.interfaces.mongo_interface import HotelsRepository
from app.interfaces.rooms_repository_interface import RoomsRepository
from app.interfaces.user_repository_interface import UserRepository
from app.interfaces.bookings_repository_interface import BookingsRepository

from app.services.hotels_repository import HotelsMongoRepository
from app.services.rooms_repository import RoomsMongoRepository
from app.services.user_repository import UserSQLRepository
from app.services.bookings_repository import BookingsMongoRepository

from app.services.auth_service import LoginService, RegistrationService
from app.services.hotels_service import HotelsService
from app.services.rooms_service import RoomsService
from app.services.security_service import PasswordService, TokenService
from app.services.book_service import BookingService



@asynccontextmanager
async def lifespan(app):
    """Application lifespan context manager."""
    await sql_database.create_tables()

    yield

    await sql_database.engine.dispose()


# Password and token services


def get_password_service() -> PasswordService:
    """Get password service instance."""
    return PasswordService()


def get_token_service() -> TokenService:
    """Get token service instance."""
    return TokenService()


# User repository


def get_user_repository() -> UserRepository:
    """Get user repository instance."""
    return UserSQLRepository()


# Registration service


def get_registration_service(
        session: AsyncSession = Depends(sql_database.get_session),
        user_repo: UserRepository = Depends(get_user_repository),
        password_service: PasswordService = Depends(get_password_service)
) -> RegistrationService:
    """Get registration service instance."""
    return RegistrationService(session, user_repo, password_service)


# Login service


def get_login_service(
        session: AsyncSession = Depends(sql_database.get_session),
        user_repo: UserRepository = Depends(get_user_repository),
        password_service: PasswordService = Depends(get_password_service),
        token_service: TokenService = Depends(get_token_service)
) -> LoginService:
    """Get login service instance."""
    return LoginService(session, user_repo, password_service, token_service)


# Hotels repository


def get_hotels_repository() -> HotelsRepository:
    """Get hotels repository instance."""
    return HotelsMongoRepository()


# Hotels service


def get_hotels_service(
        session: AsyncIOMotorClient = Depends(mongo_database.get_session),
        hotel_repo: HotelsRepository = Depends(get_hotels_repository)
) -> HotelsService:
    """Get hotels service instance."""
    return HotelsService(session, hotel_repo)


# Rooms repository


def get_rooms_repository() -> RoomsRepository:
    """Get rooms repository instance."""
    return RoomsMongoRepository()


# Rooms service


def get_rooms_service(
        session: AsyncIOMotorClient = Depends(mongo_database.get_session),
        hotels_repo: HotelsRepository = Depends(get_hotels_repository),
        rooms_repo: RoomsRepository = Depends(get_rooms_repository)
) -> RoomsService:
    """Get rooms service instance."""
    return RoomsService(session, hotels_repo, rooms_repo)


# Bookings repository


def get_bookings_repository() -> BookingsRepository:
    return BookingsMongoRepository()


# Booking service


def get_booking_service(
        session: AsyncIOMotorClient = Depends(mongo_database.get_session),
        bookings_repo: BookingsRepository = Depends(get_bookings_repository),
        rooms_service: RoomsService = Depends(get_rooms_service),
        token_service: TokenService = Depends(get_token_service)
) -> BookingService:
    return BookingService(session, bookings_repo, rooms_service, token_service)
