from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse, JSONResponse, Response
from app.databases import database
import jwt
from app.models.validation_models import User, LoginData, Token
from app.auth.jwt_auth import get_password_hash, verify_password, create_access_token

db_path = "app/databases/users.db"      

router = APIRouter(prefix='/api/v1/auth')

@router.post("/register")
async def register(data: User):
    async with database.UserDatabase(db_path) as db:
        user_exists = await db.fetch_elem(data.mail)
        if user_exists != ('_error'):
            raise HTTPException(status_code=409, detail={"error": "USER_ALREADY_EXISTS",
                                                          "message": "Такой аккаунт уже существует!"})
        
        await db.add_elem(data.id, data.name, data.surname, data.mail, get_password_hash(data.password))
        return JSONResponse({'message': f'Вы зарегистрированы! Ваш id: {data.id}'}, status_code=201)

@router.post("/login")
async def login(data: LoginData):
    async with database.UserDatabase(db_path) as db:
        user_data = await db.fetch_elem(data.mail)
        if verify_password(data.password, user_data[-1]):
            token = create_access_token(user_data)
            return JSONResponse({'message': f'Вы успешно вошли в свой аккаунт!', 'token': token}, status_code=200)
        
        raise HTTPException(status_code=401, detail={'error': "UNAUTHORIZED", 'message': f'Неверный логин/пароль!'})