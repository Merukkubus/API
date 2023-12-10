from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from src.auth.base_config import current_user
from src.auth.models import User
from src.database import get_async_session
from src.models import completed_exercise

router = APIRouter(
    prefix="/progress",
    tags=["progress"]
)

@router.get("/")
async def get_progress(user: User = Depends(current_user), session: AsyncSession = Depends(get_async_session)):
    query = select(completed_exercise).where(completed_exercise.c.user_id == user.id)
    result = await session.execute(query)
    return result.mappings().all()

@router.get("/protected-route")
def protected_route(user: User = Depends(current_user)):
    return f"Hello, {user.username, user.id}"