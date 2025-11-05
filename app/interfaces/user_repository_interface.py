from sqlmodel import select, Session
from app.models.schemas.auth import LoginData
from app.models.schemas.user import User
from app.models.sqlmodels.user import DatabaseUser
from abc import ABC, abstractmethod

class UserRepository(ABC):

    @abstractmethod
    def add_user(user: DatabaseUser, session: Session):
        pass

    @abstractmethod
    def fetch_user(data: LoginData, session: Session):
        pass