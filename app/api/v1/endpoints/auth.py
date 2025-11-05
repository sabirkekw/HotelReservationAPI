from fastapi import APIRouter, Depends
from app.models.schemas.auth import LoginData
from app.models.schemas.user import User
from app.api.v1.dependencies.dependencies import lifespan, get_registration_service, get_login_service


router = APIRouter(prefix='/api/v1/auth', lifespan=lifespan)

@router.post("/register")
async def register(data: User, registration_service = Depends(get_registration_service)):
    return registration_service.register(data)

@router.post("/login")
async def login(data: LoginData, login_service = Depends(get_login_service)):
    return login_service.login(data)