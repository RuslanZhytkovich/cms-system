from typing import List

from core.db import get_db
from customers.schemas import CreateCustomer
from customers.schemas import ShowCustomer
from customers.schemas import UpdateCustomer
from customers.services import CustomerService
from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

customer_router = APIRouter()


@customer_router.get("/get_all", response_model=List[ShowCustomer])
async def get_all_customers(db: AsyncSession = Depends(get_db)):
    try:
        return await CustomerService.get_all_customers_service(db)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@customer_router.get("/get_by_id", response_model=ShowCustomer)
async def get_customer_by_id(customer_id: int, db: AsyncSession = Depends(get_db)):
    try:
        return await CustomerService.get_customer_by_id(customer_id=customer_id, db=db)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@customer_router.delete("/delete_by_id", status_code=status.HTTP_200_OK)
async def delete_customer_by_id(customer_id: int, db: AsyncSession = Depends(get_db)):
    try:
        return await CustomerService.delete_customer_by_id(
            customer_id=customer_id, db=db
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@customer_router.patch("/update_by_id", status_code=status.HTTP_200_OK)
async def update_customer_by_id(
    customer_id: int, customer: UpdateCustomer, db: AsyncSession = Depends(get_db)
):
    try:
        return await CustomerService.update_customer_by_id(
            customer_id=customer_id, customer=customer, db=db
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@customer_router.patch("/soft_delete", status_code=status.HTTP_200_OK)
async def soft_delete_customer(customer_id: int, db: AsyncSession = Depends(get_db)):
    try:
        return await CustomerService.soft_delete_customer(
            customer_id=customer_id, db=db
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@customer_router.post("/create", response_model=ShowCustomer)
async def create_customer(
    new_customer: CreateCustomer, db: AsyncSession = Depends(get_db)
):
    try:
        return await CustomerService.create_customer(new_customer=new_customer, db=db)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
