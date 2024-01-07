from sqlalchemy import Column, String, Integer, Boolean
from sqlalchemy.orm import relationship
from src.backend.core.db import Base


class Customer(Base):
    __tablename__ = 'customers'
    customer_id = Column(Integer, primary_key=True)
    customer_name = Column(String, nullable=False, unique=True)
    is_deleted = Column(Boolean, default=False)

    projects = relationship('Project',backref='customer')