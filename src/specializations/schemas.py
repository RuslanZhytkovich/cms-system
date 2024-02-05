from pydantic import BaseModel


class BaseSpecialization(BaseModel):
    specialization_name: str
    is_deleted: bool = False

    class Config:
        orm_mode = True


class ShowSpecialization(BaseSpecialization):
    specialization_id: int


class CreateSpecialization(BaseSpecialization):
    pass


class UpdateSpecialization(BaseSpecialization):
    pass
