from datetime import datetime
from typing import AsyncGenerator

from fastapi import Depends
from fastapi_users.db import SQLAlchemyBaseUserTable, SQLAlchemyUserDatabase
from sqlalchemy import Column, INTEGER, VARCHAR, TIMESTAMP, BOOLEAN
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.ext.declarative import DeclarativeMeta, declarative_base
from sqlalchemy.orm import sessionmaker

from config import DB_USER, DB_PASS, DB_HOST, DB_PORT, DB_NAME

DATABASE_URL = f"postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
Base: DeclarativeMeta = declarative_base()


class User(SQLAlchemyBaseUserTable[int], Base):
    id = Column(INTEGER, primary_key=True)
    username = Column(VARCHAR(length=50), nullable=False)
    email = Column(VARCHAR(length=320), nullable=False)
    hashed_password: str = Column(VARCHAR(length=1024), nullable=False)
    full_name = Column(VARCHAR(length=100), nullable=False)
    is_active: bool = Column(BOOLEAN, default=True, nullable=False)
    is_superuser: bool = Column(BOOLEAN, default=False, nullable=False)
    is_verified: bool = Column(BOOLEAN, default=False, nullable=False)



engine = create_async_engine(DATABASE_URL)
async_session_maker = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session


async def get_user_db(session: AsyncSession = Depends(get_async_session)):
    yield SQLAlchemyUserDatabase(session, User)
