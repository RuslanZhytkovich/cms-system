import subprocess

from starlette.middleware.cors import CORSMiddleware

from auth.views import login_router
from auth.views import register_router
from core.exception_handler import include_exceptions_to_app
from core.redis_repository import RedisRepository
from customers.views import customer_router
from fastapi import FastAPI
from projects.views import project_router
from reports.views import report_router
from specializations.views import specialization_router
from users.views import user_router

app = FastAPI(title="cms-system")  # create instance of the app


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["Authorization"],
)

include_exceptions_to_app(app)

# set routes to the app instance
app.include_router(user_router, prefix="/users", tags=["users"])
app.include_router(project_router, prefix="/projects", tags=["projects"])
app.include_router(report_router, prefix="/reports", tags=["reports"])
app.include_router(customer_router, prefix="/customers", tags=["customers"])
app.include_router(
    specialization_router, prefix="/specializations", tags=["specializations"]
)

app.include_router(login_router, prefix="/login", tags=["login"])
app.include_router(register_router, tags=["register"])


@app.on_event("startup")
async def before_startup():
    subprocess.run(["alembic", "upgrade", "heads"])


@app.on_event("startup")
async def startup_event():
    await RedisRepository.connect_to_redis()

