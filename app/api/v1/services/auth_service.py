from app.api.v1.dependencies.dependencies import SessionDep
from app.models.schemas.user import User
from app.api.v1.services.repository import fetch_user, add_user, to_database_user
from app.api.v1.services.security_service import SecurityService
from fastapi import HTTPException
from fastapi.responses import JSONResponse

class UserService():
    def __init__(self, user_data: User, session: SessionDep):
        self.data = user_data
        self.session = session

    def register(self):
        user_data = fetch_user(self.data, self.session)

        if user_data:
            raise HTTPException(status_code=409, detail={"error": "USER_ALREADY_EXISTS",
                                                            "message": "Такой аккаунт уже существует!"})
        
        security = SecurityService(self.data)
        security.get_password_hash()
        user_data = to_database_user(self.data, security.password_hash)
        added_user = add_user(user_data, self.session)
        
        return JSONResponse({'message': f'Вы зарегистрированы! Ваш id: {added_user.id}'}, status_code=201)

    def login(self):
        try:
            user_data = fetch_user(self.data, self.session)
            security = SecurityService(user_data)
            security.get_password_hash()
            if security.verify_password():
                security.create_access_token()
                return JSONResponse({'message': f'Вы успешно вошли в свой аккаунт!', 'token': security.token}, status_code=200)
        except AttributeError:
            raise HTTPException(status_code=401, detail={'error': "UNAUTHORIZED", 'message': f'Неверный логин/пароль!'})