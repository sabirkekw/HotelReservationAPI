"""Application configuration."""

from typing import Optional

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Application settings loaded from environment."""

    app_name: str = "HotelReservationAPI v0.1"
    secret_key: str
    algorithm: str
    token_ttl: int

    sql_database_url: Optional[str] = "sqlite+aiosqlite:///./users.db"

    mongo_url: Optional[str] = "mongodb://127.0.0.1:27017"
    mongo_db: Optional[str] = "hotel_db"

    class Config:
        """Pydantic configuration."""

        env_file = ".env"


settings = Settings()