from sqlalchemy import Column, String, Integer, Boolean
from sqlalchemy.orm import relationship
from src.backend.core.db import Base


class Specialization(Base):
    __tablename__ = 'specializations'
    specialization_id = Column(Integer, autoincrement=True, primary_key=True, index=True)
    specialization_name = Column(String, nullable=False, unique=True)
    is_deleted = Column(Boolean, default=False)

    user = relationship("User", backref='specialization')