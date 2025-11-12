from pydantic_settings import BaseSettings
from typing import Optional

class Settings(BaseSettings):
    app_name: str = "HotelReservationAPI v0.1"
    secret_key: str
    algorithm: str
    token_ttl: int

    sql_database_url: Optional[str] = "sqlite+aiosqlite:///./users.db"

    mongo_url: Optional[str] = "mongodb://127.0.0.1:27017"
    mongo_db: Optional[str] = "hotel_db"
    
    class Config:
        env_file = ".env"

settings = Settings()