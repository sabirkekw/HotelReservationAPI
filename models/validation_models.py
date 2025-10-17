from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    surname: str
    mail: str
    password: str

class LoginData(BaseModel):
    mail: str
    password: str