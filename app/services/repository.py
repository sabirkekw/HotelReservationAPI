from sqlmodel import select, Session
from app.models.schemas.auth import LoginData
from app.models.sqlmodels.user import DatabaseUser
from abc import ABC, abstractmethod
from app.interfaces.user_repository_interface import UserRepository

class UserSQLRepository(UserRepository):

    def add_user(self, user: DatabaseUser, session: Session, hashed_password):
        db_user_data = DatabaseUser(
            name=user.name,
            surname=user.surname,
            mail=user.mail,
            password=hashed_password
        )
        session.add(db_user_data)
        session.commit()
        session.refresh(db_user_data)
        return db_user_data.id

    def fetch_user(self, data: LoginData, session: Session):
        user_data = session.exec(select(DatabaseUser).where(DatabaseUser.mail == data.mail))
        return user_data.first()