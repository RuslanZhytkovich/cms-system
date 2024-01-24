from fastapi import FastAPI
import uvicorn
from fastapi.routing import APIRouter

from src.backend.customers.views import customer_router
from src.backend.projects.views import project_router
from src.backend.reports.views import report_router
from src.backend.specializations.views import specialization_router
from src.backend.users.views import user_router


app = FastAPI(title="cms-system")       # create instance of the app

main_api_router = APIRouter()           # create the instance for the routes

# set routes to the app instance
main_api_router.include_router(user_router, prefix="/users", tags=["users"])
main_api_router.include_router(project_router, prefix="/projects", tags=["projects"])
main_api_router.include_router(report_router, prefix="/reports", tags=["reports"])
main_api_router.include_router(customer_router, prefix="/customers", tags=["customers"])
main_api_router.include_router(specialization_router, prefix='/specializations', tags=["specializations"])

app.include_router(main_api_router)

if __name__ == "__main__":
    # run app on the host and port
    uvicorn.run(app, host="localhost", port=8000)