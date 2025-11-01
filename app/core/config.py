from pydantic_settings import BaseSettings
from typing import Optional

class Settings(BaseSettings):
    app_name: str = "HotelReservationAPI v0.1"
    secret_key: str
    algorithm: str
    token_ttl: int

    database_url: Optional[str] = "sqlite:///./users.db"
    
    class Config:
        env_file = ".env"

settings = Settings()