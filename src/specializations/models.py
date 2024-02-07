from core.db import Base
from sqlalchemy import Boolean
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import relationship


class Specialization(Base):
    __tablename__ = "specializations"
    specialization_id = Column(
        Integer, autoincrement=True, primary_key=True, index=True
    )
    specialization_name = Column(String, nullable=False, unique=True)
    is_deleted = Column(Boolean, default=False)

    user = relationship("User", backref="specialization")
