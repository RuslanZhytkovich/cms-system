from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from src.backend.customers.db_controller import CustomerDBController
from src.backend.core.db import get_db


class CustomerService:
    @staticmethod
    async def get_all_customers_service(db: AsyncSession = Depends(get_db)):
        return await CustomerDBController.get_all_customers(db)