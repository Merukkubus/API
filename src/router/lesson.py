from fastapi import Depends, APIRouter
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from src.database import get_async_session
from src.models import lesson, exercise

router = APIRouter(
    prefix="/lessons",
    tags=["lessons"]
)

@router.get("/")
async def get_lessons(session: AsyncSession = Depends(get_async_session)):
    query = select(lesson)
    result = await session.execute(query)
    return result.mappings().all()

@router.get("/{lesson_id}")
async def get_lesson_by_id(lesson_id: int, session: AsyncSession = Depends(get_async_session)):
    query1 = select(lesson).where(lesson.c.id == lesson_id)
    query2 = select(exercise).where(exercise.c.lesson_id == lesson_id)
    result1 = await session.execute(query1)
    result2 = await session.execute(query2)
    return result1.mappings().all(), result2.mappings().all()