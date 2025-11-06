import jwt
from app.models.schemas.user import User
from pwdlib import PasswordHash
from datetime import datetime, timedelta, timezone
from app.core.config import settings

SECRET_KEY = settings.secret_key
ALGORITHM = settings.algorithm
TOKEN_TTL = settings.token_ttl

class PasswordService:
    def __init__(self):
        self._password_hash = PasswordHash.recommended()
    
    async def hash(self,password):
        return self._password_hash.hash(password)

    async def verify_password(self, password, hash):
        return self._password_hash.verify(password, hash)
    

class TokenService:
    async def create_access_token(self, data) -> str:
        try:
            payload = data.model_dump()
        except Exception:
            try:
                payload = data.dict()
            except Exception:
                payload = dict(data)

        payload.pop("password", None)
        payload["exp"] = datetime.now(timezone.utc) + timedelta(minutes=TOKEN_TTL)

        token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
        return token

    async def verify_access_token(self, token: str) -> bool:
        try:
            jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        except jwt.ExpiredSignatureError:
            return False
        except jwt.PyJWTError:
            return False
        return True