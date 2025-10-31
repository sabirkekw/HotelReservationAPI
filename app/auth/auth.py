from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from app.models.validation_models import User, LoginData
from app.databases.database import DatabaseUser, fetch_user, add_user
from app.auth.jwt import get_password_hash, verify_password, create_access_token    
from app.dependencies.dependencies import lifespan, SessionDep

router = APIRouter(prefix='/api/v1/auth', lifespan=lifespan)

@router.post("/register")
async def register(data: User, session: SessionDep):
    user_exists = fetch_user(data, session)
    if user_exists:
        raise HTTPException(status_code=409, detail={"error": "USER_ALREADY_EXISTS",
                                                        "message": "Такой аккаунт уже существует!"})
    user_data = DatabaseUser(
        name=data.name,
        surname=data.surname,
        mail=data.mail,
        password=get_password_hash(data.password)
    )
    added_user = add_user(user_data, session)
    return JSONResponse({'message': f'Вы зарегистрированы! Ваш id: {added_user.id}'}, status_code=201)

@router.post("/login")
async def login(data: LoginData, session: SessionDep):
    user_data = fetch_user(data, session)
    if verify_password(data.password, user_data.password):
        token = create_access_token(user_data)
        return JSONResponse({'message': f'Вы успешно вошли в свой аккаунт!', 'token': token}, status_code=200)
    
    raise HTTPException(status_code=401, detail={'error': "UNAUTHORIZED", 'message': f'Неверный логин/пароль!'})