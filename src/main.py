import os
import subprocess

import uvicorn
from auth.views import login_router, register_router
from customers.views import customer_router
from fastapi import FastAPI
from fastapi.routing import APIRouter
from projects.views import project_router
from reports.views import report_router
from specializations.views import specialization_router
from users.views import user_router


app = FastAPI(title="cms-system")  # create instance of the app

main_api_router = APIRouter()  # create the instance for the routes

# set routes to the app instance
main_api_router.include_router(user_router, prefix="/users", tags=["users"])
main_api_router.include_router(project_router, prefix="/projects", tags=["projects"])
main_api_router.include_router(report_router, prefix="/reports", tags=["reports"])
main_api_router.include_router(customer_router, prefix="/customers", tags=["customers"])
main_api_router.include_router(specialization_router, prefix="/specializations", tags=["specializations"])
main_api_router.include_router(login_router, prefix="/login", tags=["login"])
main_api_router.include_router(register_router, prefix="", tags=[])
app.include_router(main_api_router)


@app.on_event("startup")
async def before_startup():
    subprocess.run(["alembic", "upgrade", "heads"])


