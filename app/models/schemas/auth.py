"""Login request schema."""

from pydantic import BaseModel, Field


class LoginData(BaseModel):
    """Login credentials schema."""

    mail: str = Field(
        pattern=r'^[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}$'
    )
    password: str = Field(min_length=8, max_length=20)
