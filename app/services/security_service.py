"""Security services for password hashing and JWT token management."""

from datetime import datetime, timedelta, timezone

import jwt
from pwdlib import PasswordHash

from app.core.config import settings

SECRET_KEY = settings.secret_key
ALGORITHM = settings.algorithm
TOKEN_TTL = settings.token_ttl


class PasswordService:
    """Service for password hashing and verification."""

    def __init__(self) -> None:
        """Initialize password hasher."""
        self._password_hash = PasswordHash.recommended()

    async def hash(self, password: str) -> str:
        """Hash a password."""
        return self._password_hash.hash(password)

    async def verify_password(
        self,
        password: str,
        hash_value: str
    ) -> bool:
        """Verify password against hash."""
        return self._password_hash.verify(password, hash_value)


class TokenService:
    """Service for JWT token management."""

    async def create_access_token(self, data) -> str:
        """Create an access token from user data."""
        try:
            payload = data.model_dump()
        except Exception:
            try:
                payload = data.dict()
            except Exception:
                payload = dict(data)

        payload.pop("password", None)
        payload["exp"] = (
            datetime.now(timezone.utc) + timedelta(minutes=TOKEN_TTL)
        )

        token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
        return token

    async def verify_access_token(self, token: str) -> bool:
        """Verify an access token."""
        try:
            jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        except jwt.ExpiredSignatureError:
            return False
        except jwt.PyJWTError:
            return False
        return True