from datetime import date

from pydantic import BaseModel


class BaseProject(BaseModel):
    project_name: str
    start_date: date
    end_date: date
    is_finished: bool = False
    is_deleted: bool = False
    customer_id: int

    class Config:
        orm_mode = True


class ShowProject(BaseProject):
    project_id: int


class CreateProject(BaseProject):
    pass


class UpdateProject(BaseProject):
    pass
