from sqlalchemy import Column, String, Integer, Boolean, ForeignKey, func, Date
from sqlalchemy.orm import relationship

from src.backend.core.db import Base


class Project(Base):
    __tablename__ = "projects"
    id = Column(Integer, autoincrement=True, primary_key=True, index=True)
    project_name = Column(String, nullable=False, unique=True)
    finished = Column(Boolean, default=False)
    project_start_date = Column(Date, server_default=func.now(), nullable=True)
    project_end_date = Column(Date, server_default=func.now(), nullable=True)
    customer_id = Column(Integer, ForeignKey('customers.customer_id'))
    deleted = Column(Boolean, default=False)

    users = relationship('User', secondary='project_users', back_populates='projects')