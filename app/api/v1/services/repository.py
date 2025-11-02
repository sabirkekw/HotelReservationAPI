from sqlmodel import SQLModel, create_engine, select, Session
from app.models.schemas.auth import LoginData
from app.models.sqlmodels.user import DatabaseUser
from app.core.config import settings

sqlite_url = settings.database_url

engine = create_engine(sqlite_url, echo=False, connect_args={"check_same_thread": False})

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def add_user(user: DatabaseUser, session: Session):
    session.add(user)
    session.commit()
    session.refresh(user)
    return user

def fetch_user(data: LoginData, session: Session):
    user_data = session.exec(select(DatabaseUser).where(DatabaseUser.mail == data.mail))
    return user_data.first()

def to_database_user(user_data, hashed_password):
    return DatabaseUser(
        name=user_data.name,
        surname=user_data.surname,
        mail=user_data.mail,
        password=hashed_password
    )
