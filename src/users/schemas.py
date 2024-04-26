import uuid
from datetime import date
from typing import Optional

from pydantic import BaseModel
from pydantic import EmailStr
from users.enums import RoleEnum


class BaseUser(BaseModel):
    email: EmailStr
    password: str

    class Config:
        orm_mode = True


class RegisterUser(BaseUser):
    pass



class RegisterUserUUID(BaseUser):
    user_id: uuid.UUID


class CreateUserFullData(BaseUser):
    name: str
    last_name: str
    role: RoleEnum
    telegram: str
    phone_number: str
    on_bench: bool = False
    time_created: date
    last_login: date
    is_active: bool = True
    specialization_id: int = 1


class FillInProfile(BaseModel):
    name: Optional[str] = None
    last_name: Optional[str] = None
    telegram: Optional[str] = None
    phone_number: Optional[str] = None
    on_bench: Optional[bool] = None
    specialization_id: Optional[int] = None

    class Config:
        orm_mode = True


class UpdateUser(CreateUserFullData):
    pass


class ShowUser(CreateUserFullData):
    user_id: uuid.UUID
    name: Optional[str] = None
    last_name: Optional[str] = None
    role: RoleEnum
    telegram: Optional[str] = None
    phone_number: Optional[str] = None
    on_bench: bool = False
    time_created: date
    last_login: date
    is_active: bool = True
    specialization_id: Optional[int] = None
