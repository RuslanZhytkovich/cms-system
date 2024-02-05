from envparse import Env

env = Env()

DB_URL = env.str("REAL_DATABASE_URL",
                 default="postgresql+asyncpg://postgres:postgres@localhost:5432/postgres",
                 )


TEST_DB_URL = env.str("TEST_DATABASE_URL",
                      default="postgresql+asyncpg://postgres_test:postgres_test@localhost:5433/postgres_test"
                      )

REDIS_URL = env.str("REDIS_URL",
                    default=""
                    )