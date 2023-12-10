from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable
from sqlalchemy import Column, INTEGER, VARCHAR, BOOLEAN
from src.database import Base

class User(SQLAlchemyBaseUserTable[int], Base):
    id = Column(INTEGER, primary_key=True)
    username = Column(VARCHAR(length=50), nullable=False)
    email = Column(VARCHAR(length=320), nullable=False)
    hashed_password: str = Column(VARCHAR(length=1024), nullable=False)
    full_name = Column(VARCHAR(length=100), nullable=False)
    is_active: bool = Column(BOOLEAN, default=True, nullable=False)
    is_superuser: bool = Column(BOOLEAN, default=False, nullable=False)
    is_verified: bool = Column(BOOLEAN, default=False, nullable=False)