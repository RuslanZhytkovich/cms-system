"""File with settings and configs for the project"""

from envparse import Env

env = Env()

DB_URL = env.str(
    "DB_URL",
    default="postgresql+asyncpg://postgres:postgres@localhost:5432/postgres"
)  # connect string for the database