import jwt
from app.models.schemas.user import User
from pwdlib import PasswordHash
from datetime import datetime, timedelta, timezone
from app.core.config import settings

SECRET_KEY = settings.secret_key
ALGORITHM = settings.algorithm
TOKEN_TTL = settings.token_ttl

password_hash = PasswordHash.recommended()

class SecurityService:
    def __init__(self, data):
        self.data = data
        self.password = self.data.password

    def get_password_hash(self):
        self.password_hash =  password_hash.hash(self.password)
    
    def verify_password(self):
        return password_hash.verify(self.password, self.password_hash)

    def create_access_token(self):
        user_model_keys = User.model_fields.keys()
        to_encode = dict(zip(user_model_keys, self.data))
        to_encode["exp"] = datetime.now(timezone.utc)+timedelta(minutes=TOKEN_TTL)
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