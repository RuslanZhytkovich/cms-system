from core.db import get_db
from core.redis_repository import RedisRepository
from customers.db_controller import CustomerDBController
from customers.models import Customer
from customers.schemas import CreateCustomer
from customers.schemas import UpdateCustomer
from fastapi import Depends
from fastapi.encoders import jsonable_encoder
from sqlalchemy.ext.asyncio import AsyncSession
from users.models import User
from utils.permissions import check_admin_manager_permission


class CustomerService:
    @staticmethod
    @check_admin_manager_permission
    async def get_all_customers_service(
        current_user: User, db: AsyncSession = Depends(get_db)
    ):

        if cache := await RedisRepository.get_from_redis("customers"):

            return [Customer(**customer) for customer in jsonable_encoder(cache)]
        else:

            customers = await CustomerDBController.get_all_customers(db)
            customers_data = [jsonable_encoder(customer) for customer in customers]
            await RedisRepository.set_to_redis(
                "customers", customers_data, expire_seconds=86400
            )
            return customers_data

    @staticmethod
    @check_admin_manager_permission
    async def get_customer_by_id(
        current_user: User, customer_id: int, db: AsyncSession = Depends(get_db)
    ):
        cache = await RedisRepository.get_from_redis(f"customer{customer_id}")
        if cache:
            return Customer(**jsonable_encoder(cache))
        else:
            customer = await CustomerDBController.get_customer_by_id(
                db=db, customer_id=customer_id
            )
            await RedisRepository.set_to_redis(
                f"customer{customer_id}",
                jsonable_encoder(customer),
                expire_seconds=86400,
            )
            return customer

    @staticmethod
    @check_admin_manager_permission
    async def delete_customer_by_id(
        current_user: User, customer_id: int, db: AsyncSession = Depends(get_db)
    ):
        await RedisRepository.clear_key("customers")
        await RedisRepository.clear_key(f"customer{customer_id}")
        return await CustomerDBController.delete_customer_by_id(
            customer_id=customer_id, db=db
        )

    @staticmethod
    @check_admin_manager_permission
    async def update_customer_by_id(
        current_user: User,
        customer_id: int,
        customer: UpdateCustomer,
        db: AsyncSession = Depends(get_db),
    ):
        await RedisRepository.clear_key("customers")
        await RedisRepository.clear_key(f"customer{customer_id}")
        return await CustomerDBController.update_customer_by_id(
            customer_id=customer_id, customer=customer, db=db
        )

    @staticmethod
    @check_admin_manager_permission
    async def soft_delete_customer(
        current_user: User, customer_id: int, db: AsyncSession = Depends(get_db)
    ):
        await RedisRepository.clear_key("customers")
        await RedisRepository.clear_key(f"customer{customer_id}")
        return await CustomerDBController.soft_delete(customer_id=customer_id, db=db)

    @staticmethod
    @check_admin_manager_permission
    async def create_customer(
        current_user: User,
        new_customer: CreateCustomer,
        db: AsyncSession = Depends(get_db),
    ):
        await RedisRepository.clear_key("customers")
        return await CustomerDBController.create_customer(
            new_customer=new_customer, db=db
        )
