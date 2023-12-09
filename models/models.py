from datetime import datetime
from sqlalchemy import MetaData,Table,Column,INTEGER,VARCHAR,TEXT,JSON,TIMESTAMP,BOOLEAN, ForeignKey

metadata = MetaData()

lesson = Table(
    "lesson",
    metadata,
    Column("id", INTEGER, primary_key=True),
    Column("title", VARCHAR, nullable=False),
    Column("description", TEXT, nullable=False),
    Column("content", TEXT, nullable=False),
)

exercise = Table(
    "exercise",
    metadata,
    Column("id", INTEGER, primary_key=True),
    Column("lesson_id", INTEGER, ForeignKey("lesson.id")),
    Column("title", VARCHAR, nullable=False),
    Column("description", TEXT, nullable=False),
    Column("type", VARCHAR, nullable=False),
    Column("questions", JSON, nullable=False),
)

completed_exercise = Table(
    "completed_exercise",
    metadata,
    Column("id", INTEGER, primary_key=True),
    Column("user_id", INTEGER, ForeignKey("user.id")),
    Column("exercise_id", INTEGER, ForeignKey("exercise.id")),
    Column("score", INTEGER, nullable=False),
    Column("competed_at", TIMESTAMP, default=datetime.utcnow),
    Column("answers", JSON, nullable=False),
)

user = Table(
    "user",
    metadata,
        Column("id", INTEGER, primary_key=True),
        Column("username", VARCHAR, nullable=False),
        Column("email", VARCHAR, nullable=False),
        Column("hashed_password", VARCHAR, nullable=False),
        Column("full_name", VARCHAR, nullable=True),
        Column("is_active", BOOLEAN, nullable=False),
        Column("is_superuser", BOOLEAN, nullable=False),
        Column("is_verified", BOOLEAN, nullable=False),
)