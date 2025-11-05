from sqlmodel import SQLModel, create_engine, Session
from fastapi import Depends
from typing import Annotated
from app.core.config import settings

class Database:
    def __init__(self, url: str):
        self.engine = create_engine(url, echo=False, connect_args={"check_same_thread": False})
    
    def create_tables(self):
        SQLModel.metadata.create_all(self.engine)
    
    def get_session(self):
        with Session(self.engine) as session:
            yield session

database = Database(settings.database_url)

# database session dependency
SessionDep = Annotated[Session, Depends(database.get_session)]
