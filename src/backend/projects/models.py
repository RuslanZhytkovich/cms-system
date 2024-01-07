from sqlalchemy import Column, String, Integer, Boolean, ForeignKey, func, Date
from sqlalchemy.orm import relationship
from src.backend.core.db import Base


class Project(Base):
    __tablename__ = "projects"
    project_id = Column(Integer, autoincrement=True, primary_key=True, index=True)
    project_name = Column(String, nullable=False, unique=True)
    is_finished = Column(Boolean, default=False)
    project_start_date = Column(Date, server_default=func.now(), nullable=True)
    project_end_date = Column(Date, server_default=func.now(), nullable=True)
    customer_id = Column(Integer, ForeignKey('customers.customer_id'))
    is_deleted = Column(Boolean, default=False)

    users = relationship('User', secondary='project_users', back_populates='projects')


class ProjectUser(Base):
    __tablename__ = 'project_users'
    id = Column(Integer, primary_key=True)
    user_id = Column(String, ForeignKey('users.user_id'))
    project_id = Column(Integer, ForeignKey('projects.project_id'))