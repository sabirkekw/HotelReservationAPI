from fastapi import APIRouter
from app.models.schemas.auth import LoginData
from app.models.schemas.user import User
from app.api.v1.services.auth_service import UserService  
from app.api.v1.dependencies.dependencies import lifespan, SessionDep

router = APIRouter(prefix='/api/v1/auth', lifespan=lifespan)

@router.post("/register")
async def register(data: User, session: SessionDep):
    user = UserService(data, session)
    return user.register()

@router.post("/login")
async def login(data: LoginData, session: SessionDep):
    user = UserService(data, session)
    return user.login()