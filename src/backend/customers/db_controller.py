from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from src.backend.customers.models import Customer


class CustomerDBController:
    @staticmethod
    async def get_all_customers(db: AsyncSession):
        customers = await db.execute(select(Customer))
        return customers.scalars().all()




