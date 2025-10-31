from sqlmodel import Field, SQLModel, create_engine, select, Session
from app.models.validation_models import LoginData

class DatabaseUser(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    surname: str
    mail: str
    password: str

sqlite_url = f"sqlite:///app/databases/users.db"

engine = create_engine(sqlite_url, echo=True, connect_args={"check_same_thread": False})

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