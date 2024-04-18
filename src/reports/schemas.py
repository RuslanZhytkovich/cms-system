import uuid
from datetime import date

from pydantic import BaseModel


class BaseReport(BaseModel):
    date: date
    hours: float
    comment: str
    user_id: uuid.UUID
    project_id: int
    is_deleted: bool = False

    class Config:
        orm_mode = True


class ShowReport(BaseReport):
    report_id: int


class CreateReport(BaseModel):
    date: date
    hours: float
    comment: str
    project_id: int

    class Config:
        orm_mode = True


class UpdateReport(BaseReport):
    pass
