from sqlmodel import Field, SQLModel

class DatabaseUser(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    surname: str
    mail: str
    password: str