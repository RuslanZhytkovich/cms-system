from core.exceptions import DatabaseException
from customers.models import Customer
from customers.schemas import CreateCustomer
from customers.schemas import UpdateCustomer
from sqlalchemy import delete
from sqlalchemy import insert
from sqlalchemy import select
from sqlalchemy import update
from sqlalchemy.ext.asyncio import AsyncSession


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
    async def get_customer_by_name(db: AsyncSession, customer_name: str):
        try:
            query = select(Customer).where(Customer.customer_name == customer_name)
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
    async def update_customer_by_id(
        customer_id: int, customer: UpdateCustomer, db: AsyncSession
    ):
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

    @staticmethod
    async def soft_delete(customer_id: int, db: AsyncSession):
        try:
            query = (
                update(Customer)
                .where(Customer.customer_id == customer_id)
                .values(is_deleted=True)
                .returning(Customer)
            )
            result = await db.execute(query)
            updated = result.scalar()
            await db.commit()
            return updated

        except Exception:
            raise DatabaseException
