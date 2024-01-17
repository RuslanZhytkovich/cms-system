from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from src.backend.core.db import get_db
from src.backend.customers.schemas import CustomerGetResponse
from src.backend.customers.services import CustomerService

customer_router = APIRouter()


@customer_router.get("/all", response_model=List[CustomerGetResponse])
async def get_all_users(db: AsyncSession = Depends(get_db)):
    return await CustomerService.get_all_customers_service(db)

