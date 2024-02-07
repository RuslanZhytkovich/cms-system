import uuid
from datetime import date

from pydantic import BaseModel


class BaseReport(BaseModel):
    date: date
    hours: float
    comment: str
    user_id: uuid.UUID
    project_id: int

    class Config:
        orm_mode = True


class ShowReport(BaseReport):
    report_id: int


class CreateReport(BaseReport):
    pass


class UpdateReport(BaseReport):
    pass
