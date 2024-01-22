from fastapi import FastAPI
import uvicorn
from fastapi.routing import APIRouter

from src.backend.customers.views import customer_router
from src.backend.specializations.views import specialization_router
from src.backend.users.views import user_router

# create instance of the app
app = FastAPI(title="cms-system")




# create the instance for the routes
main_api_router = APIRouter()

# set routes to the app instance
main_api_router.include_router(user_router, prefix="/users", tags=["users"])
main_api_router.include_router(customer_router, prefix="/customers", tags=["customers"])
main_api_router.include_router(specialization_router, prefix='/specializations', tags=["specializations"])
app.include_router(main_api_router)

if __name__ == "__main__":
    # run app on the host and port
    uvicorn.run(app, host="localhost", port=8000)