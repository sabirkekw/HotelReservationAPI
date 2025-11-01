from pydantic import BaseModel, Field

class User(BaseModel):
    name: str = Field(min_length=3, max_length=20)
    surname: str = Field(min_length=3, max_length=20)
    mail: str = Field(pattern=r'^[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}$')
    password: str = Field(min_length = 8, max_length = 20)