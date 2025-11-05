from contextlib import asynccontextmanager
from fastapi import Depends
from app.core.database_config import database, SessionDep
from app.interfaces.user_repository_interface import UserRepository
from app.services.repository import UserSQLRepository
from app.services.auth_service import RegistrationService, LoginService
from app.services.security_service import PasswordService, TokenService

@asynccontextmanager
async def lifespan(app):
    database.create_tables()
    
    yield
    
    database.engine.dispose()

def get_password_service() -> PasswordService:
    return PasswordService()

def get_token_service() -> TokenService:
    return TokenService()

def get_user_repository() -> UserRepository:
    return UserSQLRepository()

def get_registration_service(session: SessionDep,
                             user_repo: UserRepository = Depends(get_user_repository),
                             password_service: PasswordService = Depends(get_password_service)
                             ) -> RegistrationService:
    return RegistrationService(session, user_repo, password_service)

def get_login_service(session: SessionDep,
                      user_repo: UserRepository = Depends(get_user_repository),
                      password_service: PasswordService = Depends(get_password_service),
                      token_service: TokenService = Depends(get_token_service)
                      ) -> LoginService:
    return LoginService(session, user_repo, password_service, token_service)