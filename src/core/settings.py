from dotenv import load_dotenv
from pydantic import BaseSettings

load_dotenv()


class Settings(BaseSettings):
    DB_URL: str
    TEST_DB_URL: str
    REDIS_URL: str


SETTINGS = Settings()
