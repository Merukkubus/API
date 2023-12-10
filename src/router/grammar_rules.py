from fastapi import Depends, APIRouter
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from src.database import get_async_session
from src.models import grammar

router = APIRouter(
    prefix="/grammar_rules",
    tags=["grammar_rules"]
)

@router.get("/")
async def get_grammar_rules(session: AsyncSession = Depends(get_async_session)):
    query = select(grammar.c.id, grammar.c.title)
    result = await session.execute(query)
    return result.mappings().all()

@router.get("/{grammar_id}")
async def get_grammar_by_id(grammar_id: int, session: AsyncSession = Depends(get_async_session)):
    query = select(grammar).where(grammar.c.id == grammar_id)
    result = await session.execute(query)
    return result.mappings().all()