from pydantic import BaseModel


class BaseCustomer(BaseModel):
    customer_name: str
    is_deleted: bool = False

    class Config:
        orm_mode = True


class ShowCustomer(BaseCustomer):
    customer_id: int


class CreateCustomer(BaseCustomer):
    pass


class UpdateCustomer(BaseCustomer):
    pass
