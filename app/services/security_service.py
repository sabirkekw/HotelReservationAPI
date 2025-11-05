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
    
    def hash(self,password):
        return self._password_hash.hash(password)

    def verify_password(self, password, hash):
        return self._password_hash.verify(password, hash)
    

class TokenService:
    def create_access_token(self, data):
        user_model_keys = User.model_fields.keys()
        to_encode = dict(zip(user_model_keys, data))
        to_encode["exp"] = datetime.now(timezone.utc)+timedelta(minutes=TOKEN_TTL)
        to_encode["password"] = None
        self.token = jwt.encode(to_encode, SECRET_KEY, ALGORITHM)

    def verify_access_token(self):
        header, payload, sign = self.token.split('.')
        decoded_header = jwt.get_unverified_header(header)
        encoding_algorithm = decoded_header['alg']
        try:
            jwt.decode(self.token,SECRET_KEY,algorithms=[encoding_algorithm])
        except jwt.ExpiredSignatureError:
            return False
        return True