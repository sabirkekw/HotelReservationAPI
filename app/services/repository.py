from sqlmodel import select, Session
from app.models.schemas.auth import LoginData
from app.models.sqlmodels.user import DatabaseUser
from abc import ABC, abstractmethod
from app.interfaces.user_repository_interface import UserRepository

class UserSQLRepository(UserRepository):

    def add_user(self, user: DatabaseUser, session: Session):
        session.add(user)
        session.commit()
        session.refresh(user)
        return user

    def fetch_user(self, data: LoginData, session: Session):
        user_data = session.exec(select(DatabaseUser).where(DatabaseUser.mail == data.mail))
        return user_data.first()

    def to_database_user(self, user_data, hashed_password):
        return DatabaseUser(
            name=user_data.name,
            surname=user_data.surname,
            mail=user_data.mail,
            password=hashed_password
        )
