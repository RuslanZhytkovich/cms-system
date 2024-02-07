from core.db import Base
from sqlalchemy import Boolean
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import relationship


class Customer(Base):
    __tablename__ = "customers"
    customer_id = Column(Integer, primary_key=True)
    customer_name = Column(String, nullable=False, unique=True)
    is_deleted = Column(Boolean, default=False)

    projects = relationship("Project", backref="customer")
