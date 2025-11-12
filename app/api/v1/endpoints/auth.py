"""Authentication endpoints for API v1."""

from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

from app.api.v1.dependencies.dependencies import (
    get_registration_service,
    get_login_service
)
from app.models.schemas.auth import LoginData
from app.models.schemas.user import User

router = APIRouter(prefix='/api/v1/auth')


@router.post("/register")
async def register(
    data: User,
    registration_service=Depends(get_registration_service)
) -> dict:
    """Register a new user account."""
    user_id = await registration_service.register(data)
    return JSONResponse(
        status_code=201,
        content={
            "message": f"Вы зарегистрированы! Ваш id: {user_id}"
        }
    )


@router.post("/login")
async def login(
    data: LoginData,
    login_service=Depends(get_login_service)
) -> dict:
    """Login with email and password to get access token."""
    token = await login_service.login(data)
    return JSONResponse(
        status_code=200,
        content={
            "message": "Вы успешно вошли в свой аккаунт!",
            "token": token
        }
    )