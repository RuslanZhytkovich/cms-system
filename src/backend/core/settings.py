from envparse import Env

env = Env()

DB_URL = env.str(
    "REAL_DATABASE_URL",
    default="postgresql+asyncpg://postgres:postgres@localhost:5432/postgres",
)

