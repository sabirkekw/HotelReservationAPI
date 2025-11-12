"""Database user model."""

from sqlmodel import Field, SQLModel


class DatabaseUser(SQLModel, table=True):
    """User database model."""

    id: int | None = Field(default=None, primary_key=True)
    name: str
    surname: str
    mail: str
    password: str