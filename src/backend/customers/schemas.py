from pydantic import BaseModel


class CustomerBase(BaseModel):
    customer_name: str
    deleted: bool


class CustomerCreate(CustomerBase):
    pass


class CustomerGetResponse(CustomerBase):
    customer_id: int

    class Config:
        orm_mode = True