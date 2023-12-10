from fastapi import FastAPI
from src.auth.base_config import auth_backend, fastapi_users
from src.auth.schemas import UserRead, UserCreate

from src.router.lesson import router as lesson_router
from src.router.exercise import router as exercise_router
from src.router.translate import router as translate_router
from src.router.grammar_rules import router as grammar_router
from src.router.vocabulary import router as vocabulary_router
from src.router.progress import router as progress_router
from src.router.media import router as media_router
from src.router.test import router as test_router

app = FastAPI(title="LangAPP")

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)

app.include_router(lesson_router)
app.include_router(exercise_router)
app.include_router(translate_router)
app.include_router(grammar_router)
app.include_router(vocabulary_router)
app.include_router(progress_router)
app.include_router(media_router)
app.include_router(test_router)