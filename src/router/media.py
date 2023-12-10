from fastapi import Depends, APIRouter
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from src.database import get_async_session
from src.models import media

router = APIRouter(
    prefix="/media",
    tags=["media"]
)

@router.get("/")
async def get_media(session: AsyncSession = Depends(get_async_session)):
    query = select(media.c.id, media.c.title, media.c.type)
    result = await session.execute(query)
    return result.mappings().all()

@router.get("/{media_id}")
async def get_media_by_id(media_id: int, session: AsyncSession = Depends(get_async_session)):
    query = select(media).where(media.c.id == media_id)
    result = await session.execute(query)
    return result.mappings().all()