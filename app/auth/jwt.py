import jwt
from os import getenv
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
    to_encode = dict()
    to_encode["id"] = data[0]
    to_encode["name"] = data[1]
    to_encode["surname"] = data[2]
    to_encode["mail"] = data[3]
    to_encode["password"] = data[4]
    expire = datetime.now(timezone.utc)+timedelta(minutes=TOKEN_TTL)
    to_encode["exp"] = expire
    print(to_encode)
    return jwt.encode(to_encode, SECRET_KEY, ALGORITHM)