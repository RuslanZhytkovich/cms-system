import uuid
from datetime import date

from pydantic import BaseModel, EmailStr

from users.enums import RoleEnum


class BaseUser(BaseModel):
    email: EmailStr
    password: str

    class Config:
        orm_mode = True


class RegisterUser(BaseUser):
    pass


class CreateUserFullData(BaseUser):
    name: str
    last_name: str
    role: RoleEnum
    telegram: str
    phone_number: str
    on_bench: bool = False
    time_created: date
    last_login: date
    is_active: bool = False
    specialization_id: int


class UpdateUser(CreateUserFullData):
    pass


class ShowUser(CreateUserFullData):
    user_id: uuid.UUID
