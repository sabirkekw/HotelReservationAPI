import jwt
from os import getenv
from app.models.validation_models import User
from pwdlib import PasswordHash
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from dotenv import load_dotenv
from datetime import datetime, timedelta, timezone

load_dotenv()
SECRET_KEY = getenv("SECRET_KEY")
ALGORITHM = getenv("ALGORITHM")
TOKEN_TTL = int(getenv("TOKEN_TTL"))

password_hash = PasswordHash.recommended()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def verify_password(plain_password, hashed_password):
    return password_hash.verify(plain_password, hashed_password)

def get_password_hash(password):
    return password_hash.hash(password)

def create_access_token(data: tuple):
    user_model_keys = User.model_fields.keys()
    to_encode = dict(zip(user_model_keys, data))
    expire = datetime.now(timezone.utc)+timedelta(minutes=TOKEN_TTL)
    to_encode["exp"] = expire
    print(to_encode)
    return jwt.encode(to_encode, SECRET_KEY, ALGORITHM)

def verify_access_token(token):
    header, payload, sign = token.split('.')
    decoded_header = jwt.get_unverified_header(header)
    encoding_algorithm = decoded_header['alg']
    try:
        jwt.decode(token,SECRET_KEY,algorithms=[encoding_algorithm])
    except jwt.ExpiredSignatureError:
        return False
    return True