import uuid
from pydantic import BaseModel
from datetime import date


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




