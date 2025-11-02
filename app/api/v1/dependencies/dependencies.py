from contextlib import asynccontextmanager
from typing import Annotated
from fastapi import Depends
from sqlmodel import Session
from app.api.v1.services.repository import engine, create_db_and_tables

@asynccontextmanager
async def lifespan(app):
    create_db_and_tables()
    
    yield
    
    engine.dispose()

def get_session():
    with Session(engine) as session:
        yield session


SessionDep = Annotated[Session, Depends(get_session)]