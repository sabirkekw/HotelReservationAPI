from contextlib import asynccontextmanager
from fastapi import Depends
from app.core.sql_config import database as sql_database
from app.core.mongo_config import database as mongo_database
from sqlalchemy.ext.asyncio import AsyncSession
from motor.motor_asyncio import AsyncIOMotorClient
from app.interfaces.user_repository_interface import UserRepository
from app.interfaces.hotels_repository_interface import HotelsRepository
from app.interfaces.rooms_repository_interface import RoomsRepository
from app.services.user_repository import UserSQLRepository
from app.services.hotels_repository import HotelsMongoRepository
from app.services.rooms_repository import RoomsMongoRepository
from app.services.auth_service import RegistrationService, LoginService
from app.services.security_service import PasswordService, TokenService
from app.services.hotels_service import HotelsService
from app.services.rooms_service import RoomsService

@asynccontextmanager
async def lifespan(app):
    await sql_database.create_tables()
    
    yield
    
    await sql_database.engine.dispose()

# auth service dependencies

def get_password_service() -> PasswordService:
    return PasswordService()

def get_token_service() -> TokenService:
    return TokenService()

def get_user_repository() -> UserRepository:
    return UserSQLRepository()

def get_registration_service(session: AsyncSession = Depends(sql_database.get_session),
                             user_repo: UserRepository = Depends(get_user_repository),
                             password_service: PasswordService = Depends(get_password_service)) -> RegistrationService:
    return RegistrationService(session, user_repo, password_service)

def get_login_service(session: AsyncSession = Depends(sql_database.get_session),
                      user_repo: UserRepository = Depends(get_user_repository),
                      password_service: PasswordService = Depends(get_password_service),
                      token_service: TokenService = Depends(get_token_service)) -> LoginService:
    return LoginService(session, user_repo, password_service, token_service)

# hotels service dependencies

def get_hotels_repository() -> HotelsRepository:
    return HotelsMongoRepository()

def get_hotels_service(session: AsyncIOMotorClient = Depends(mongo_database.get_session),
                       hotel_repo: HotelsRepository = Depends(get_hotels_repository)) -> HotelsService:
    return HotelsService(session, hotel_repo)

# rooms service dependencies

def get_rooms_repository() -> RoomsRepository:
    return RoomsMongoRepository()

def get_rooms_service(session: AsyncIOMotorClient = Depends(mongo_database.get_session),
                      hotels_repo: HotelsRepository = Depends(get_hotels_repository),
                      rooms_repo: RoomsRepository = Depends(get_rooms_repository)) -> RoomsService:
    return RoomsService(session, hotels_repo, rooms_repo)
