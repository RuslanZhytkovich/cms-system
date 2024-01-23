from sqlalchemy import select, delete, insert, update
from sqlalchemy.ext.asyncio import AsyncSession

from src.backend.core.exceptions import DatabaseException
from src.backend.customers.models import Customer
from src.backend.customers.schemas import CreateCustomer, UpdateCustomer


class CustomerDBController:
    @staticmethod
    async def get_all_customers(db: AsyncSession):
        try:
            customers = await db.execute(select(Customer))
            return customers.scalars().all()
        except Exception as e:
            raise DatabaseException(str(e))

    @staticmethod
    async def get_customer_by_id(db: AsyncSession, customer_id: int):
        try:
            query = select(Customer).where(Customer.customer_id == customer_id)
            customer = await db.execute(query)
            return customer.scalar()
        except Exception as e:
            raise DatabaseException(str(e))

    @staticmethod
    async def delete_customer_by_id(db: AsyncSession, customer_id: int):
        try:
            query = delete(Customer).where(Customer.customer_id == customer_id)
            await db.execute(query)
            await db.commit()
        except Exception as e:
            raise DatabaseException(str(e))

    @staticmethod
    async def create_customer(db: AsyncSession, new_customer: CreateCustomer):
        try:
            query = insert(Customer).values(**new_customer.dict()).returning(Customer)
            result = await db.execute(query)
            new_customer = result.scalar()
            await db.commit()
            return new_customer
        except Exception as e:
            raise DatabaseException(str(e))

    @staticmethod
    async def update_customer_by_id(customer_id: int, customer: UpdateCustomer,
                                          db: AsyncSession):
        try:
            query = (
                update(Customer)
                .where(Customer.customer_id == customer_id)
                .values(**customer.dict(exclude_none=True))
                .returning(Customer)
            )
            result = await db.execute(query)
            updated = result.scalar()
            await db.commit()
            return updated
        except Exception as e:
            raise DatabaseException(str(e))






