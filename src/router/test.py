from fastapi import Depends, APIRouter
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from src.database import get_async_session
from src.models import test
import json

router = APIRouter(
    prefix="/tests",
    tags=["tests"]
)

@router.get("/")
async def get_tests(session: AsyncSession = Depends(get_async_session)):
    query = select(test)
    result = await session.execute(query)
    return result.mappings().all()

@router.get("/{test_id}")
async def get_test_by_id(test_id: int, session: AsyncSession = Depends(get_async_session)):
    query = select(test).where(test.c.id == test_id)
    js = await session.execute(query)
    data = js.mappings().all()
    result = ''
    for entry in data:
        questions_list = entry['questions']['questions']

        for question_data in questions_list:
            result += "Question: " + str(question_data['question']) + " "
            result += "Answers: " + str(question_data['answers']) + " "
            result += ' | '
    return result

@router.post("/{test_id}")
async def send_test_answers(test_id: int, answers: str, session: AsyncSession = Depends(get_async_session)):
    query = select(test.c.questions).where(test_id == test.c.id)
    js = await session.execute(query)
    data = js.mappings().all()
    correct_answers = [
        question['correct_answer']
        for question_data in data
        for question in question_data['questions']['questions']
        if 'correct_answer' in question
    ]
    print(correct_answers)
    ans_list = answers.split(";")
    end = len(correct_answers)
    if(len(ans_list) != end):
        return "The number of answers and questions does not match"
    result = ''
    count = 0
    for i in range(0, end):
        if (correct_answers[i] == ans_list[i]):
            result += str(i + 1) + " True "
            count += 1
        else:
            result += str(i + 1) + " False "
    return result, "You answered " + str(count) + " out of " + str(end) + " questions correctly!"