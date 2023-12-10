from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from src.database import get_async_session
from src.models import vocabulary

router = APIRouter(
    prefix="/vocabulary",
    tags=["vocabulary"]
)

@router.get("/")
async def get_vocabulary_help(session: AsyncSession = Depends(get_async_session)):
    query = select(vocabulary)
    result = await session.execute(query)
    return result.mappings().all()