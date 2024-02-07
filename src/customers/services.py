from core.db import get_db
from customers.db_controller import CustomerDBController
from customers.schemas import CreateCustomer
from customers.schemas import UpdateCustomer
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession


class CustomerService:
    @staticmethod
    async def get_all_customers_service(db: AsyncSession = Depends(get_db)):
        return await CustomerDBController.get_all_customers(db=db)

    @staticmethod
    async def get_customer_by_id(customer_id: int, db: AsyncSession = Depends(get_db)):
        return await CustomerDBController.get_customer_by_id(
            customer_id=customer_id, db=db
        )

    @staticmethod
    async def delete_customer_by_id(
        customer_id: int, db: AsyncSession = Depends(get_db)
    ):
        return await CustomerDBController.delete_customer_by_id(
            customer_id=customer_id, db=db
        )

    @staticmethod
    async def update_customer_by_id(
        customer_id: int, customer: UpdateCustomer, db: AsyncSession = Depends(get_db)
    ):
        return await CustomerDBController.update_customer_by_id(
            customer_id=customer_id, customer=customer, db=db
        )

    @staticmethod
    async def soft_delete_customer(
        customer_id: int, db: AsyncSession = Depends(get_db)
    ):
        return await CustomerDBController.soft_delete(customer_id=customer_id, db=db)

    @staticmethod
    async def create_customer(
        new_customer: CreateCustomer, db: AsyncSession = Depends(get_db)
    ):
        return await CustomerDBController.create_customer(
            new_customer=new_customer, db=db
        )
