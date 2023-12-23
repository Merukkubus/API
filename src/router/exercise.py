from fastapi import Depends, APIRouter
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from src.database import get_async_session
from src.models import exercise

router = APIRouter(
    prefix="/exercises",
    tags=["exercises"]
)

@router.get("/")
async def get_exercises(session: AsyncSession = Depends(get_async_session)):
    query = select(exercise.c.title)
    result = await session.execute(query)
    return result.mappings().all()

@router.get("/{exercise_id}")
async def get_exercise_by_id(exercise_id: int, session: AsyncSession = Depends(get_async_session)):
    query = select(exercise).where(exercise.c.id == exercise_id)
    result = await session.execute(query)
    return result.mappings().all()

@router.post("/{exercise_id}")
async def send_exercise_answers(exercise_id: int, answers: str, session: AsyncSession = Depends(get_async_session)):
    query = select(exercise.c.questions).where(exercise_id == exercise.c.id)
    exercises = await session.execute(query)
    data = exercises.all()
    ans_list = answers.split(";")
    first_el = data[0]
    end = len(first_el[0])
    if(end != len(ans_list)):
        return "The number of answers and questions does not match"
    result = ''
    count = 0
    for i in range(0, end):
        correct_answers = first_el[0][i]
        if(correct_answers['answer'].lower() == ans_list[i].lower()):
            result += str(i+1) + " True "
            count += 1
        else:
            result += str(i+1) + " False "
    return result, "You answered " + str(count) + " out of " + str(end) + " questions correctly!"