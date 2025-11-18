"""Authentication services for registration and login."""

from sqlalchemy.ext.asyncio import AsyncSession

from app.core.errors import AuthenticationError, UserAlreadyExists
from app.interfaces.sql_interface import SQLRepository
from app.models.schemas.auth import LoginData
from app.models.schemas.user import User
from app.services.security_service import PasswordService, TokenService


class RegistrationService:
    """Service for user registration."""

    def __init__(
        self,
        session: AsyncSession,
        user_repo: SQLRepository,
        password_service: PasswordService
    ) -> None:
        """Initialize service with dependencies."""
        self.session = session
        self.user_repo = user_repo
        self.password_service = password_service

    async def register(self, data: User) -> int:
        """Register a new user."""
        db_user_data = await self.user_repo.read_one(data, self.session)

        if db_user_data:
            raise UserAlreadyExists("Такой аккаунт уже существует!")

        hashed_password = await self.password_service.hash(data.password)
        return await self.user_repo.create(
            data,
            self.session,
            hashed_password
        )


class LoginService:
    """Service for user login."""

    def __init__(
        self,
        session: AsyncSession,
        user_repo: SQLRepository,
        password_service: PasswordService,
        token_service: TokenService
    ) -> None:
        """Initialize service with dependencies."""
        self.session = session
        self.user_repo = user_repo
        self.password_service = password_service
        self.token_service = token_service

    async def login(self, data: LoginData) -> str:
        """Login user and return access token."""
        db_user_data = await self.user_repo.read_one(data, self.session)
        if db_user_data is None:
            raise AuthenticationError('Неверный логин/пароль!')
        if not await self.password_service.verify_password(
            data.password,
            db_user_data.password
        ):
            raise AuthenticationError('Неверный логин/пароль!')

        token = await self.token_service.create_access_token(db_user_data)
        return token
            