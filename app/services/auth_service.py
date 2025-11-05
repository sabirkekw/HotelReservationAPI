from app.core.database_config import SessionDep
from app.models.schemas.user import User
from app.models.schemas.auth import LoginData
from app.interfaces.user_repository_interface import UserRepository
from app.services.security_service import PasswordService, TokenService
from fastapi import HTTPException
from fastapi.responses import JSONResponse

class RegistrationService():
    def __init__(self, session: SessionDep, user_repository: UserRepository, password_service: PasswordService):
        self.session = session
        self.user_repository = user_repository
        self.password_service = password_service

    def register(self, data):
        db_user_data = self.user_repository.fetch_user(data, self.session)

        if db_user_data:
            raise HTTPException(status_code=409, detail={"error": "USER_ALREADY_EXISTS",
                                                            "message": "Такой аккаунт уже существует!"})
        
        db_user_data = self.user_repository.to_database_user(data, self.password_service.hash(data.password))
        added_user = self.user_repository.add_user(db_user_data, self.session)
        
        return JSONResponse({'message': f'Вы зарегистрированы! Ваш id: {added_user.id}'}, status_code=201)


class LoginService():
    def __init__(self, session: SessionDep, user_repository: UserRepository, password_service: PasswordService, token_service: TokenService):
        self.session = session
        self.user_repository = user_repository
        self.password_service = password_service
        self.token_service = token_service

    def login(self, data):
        db_user_data = self.user_repository.fetch_user(data, self.session)
        if db_user_data == None:
            raise HTTPException(status_code=401, detail={'error': "UNAUTHORIZED", 
                                                         'message': f'Неверный логин/пароль!'})
            
        if self.password_service.verify_password(data.password, db_user_data.password):
            self.token_service.create_access_token(db_user_data)
            return JSONResponse({'message': f'Вы успешно вошли в свой аккаунт!',
                                    'token': self.token_service.token}, status_code=200)
        raise HTTPException(status_code=401, detail={'error': "UNAUTHORIZED", 
                                                        'message': f'Неверный логин/пароль!'})
            