from app.core.database_config import SessionDep
from app.models.schemas.user import User
from app.models.schemas.auth import LoginData
from app.interfaces.user_repository_interface import UserRepository
from app.services.security_service import PasswordService, TokenService
from fastapi import HTTPException
from fastapi.responses import JSONResponse

class RegistrationService():
    def __init__(self, session: SessionDep, user_repo: UserRepository, password_service: PasswordService):
        self.session = session
        self.user_repo = user_repo
        self.password_service = password_service

    def register(self, data: User):
        db_user_data = self.user_repo.fetch_user(data, self.session)

        if db_user_data:
            raise HTTPException(status_code=409, detail={"error": "USER_ALREADY_EXISTS",
                                                            "message": "Такой аккаунт уже существует!"})
        
        return self.user_repo.add_user(data, self.session, self.password_service.hash(data.password))


class LoginService():
    def __init__(self, session: SessionDep, user_repo: UserRepository, password_service: PasswordService, token_service: TokenService):
        self.session = session
        self.user_repo = user_repo
        self.password_service = password_service
        self.token_service = token_service

    def login(self, data: LoginData):
        db_user_data = self.user_repo.fetch_user(data, self.session)
        if db_user_data == None:
            raise HTTPException(status_code=401, detail={'error': "UNAUTHORIZED", 
                                                         'message': f'Неверный логин/пароль!'})
        if not(self.password_service.verify_password(data.password, db_user_data.password)):
            raise HTTPException(status_code=401, detail={'error': "UNAUTHORIZED", 
                                                         'message': f'Неверный логин/пароль!'})
        
        self.token_service.create_access_token(db_user_data)
        return self.token_service.token
            