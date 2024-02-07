from core.db import Base
from sqlalchemy import Boolean
from sqlalchemy import Column
from sqlalchemy import Date
from sqlalchemy import ForeignKey
from sqlalchemy import func
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import relationship


class Project(Base):
    __tablename__ = "projects"
    project_id = Column(Integer, autoincrement=True, primary_key=True, index=True)
    project_name = Column(String, nullable=False, unique=True)
    start_date = Column(Date, server_default=func.now(), nullable=False)
    end_date = Column(Date, server_default=func.now(), nullable=False)
    is_finished = Column(Boolean, default=False)
    is_deleted = Column(Boolean, default=False)
    customer_id = Column(Integer, ForeignKey("customers.customer_id"))

    users = relationship("User", secondary="project_users", back_populates="projects")
