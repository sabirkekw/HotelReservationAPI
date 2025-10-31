from contextlib import asynccontextmanager
from typing import Annotated
from fastapi import FastAPI, Depends
from sqlmodel import Session
from app.databases.database import engine, create_db_and_tables, SQLModel

@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    
    yield
    
    engine.dispose()

def get_session():
    with Session(engine) as session:
        yield session

SessionDep = Annotated[Session, Depends(get_session)]