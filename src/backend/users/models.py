from enum import Enum

from sqlalchemy import Enum as SQLAlchemyEnum, Column, String, Integer, Boolean, ForeignKey, Date
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from src.backend.core.db import Base
from src.backend.reports.models import Report


class RoleEnum(str, Enum):
    admin = 'admin'
    manager = 'manager'
    developer = 'developer'


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    name = Column(String, nullable=True)
    last_name = Column(String, nullable=True)
    role = Column(SQLAlchemyEnum(RoleEnum), nullable=False, default=RoleEnum.developer)
    telegram = Column(String, nullable=True, unique=False)
    phone_number = Column(String, nullable=True, unique=False)
    bench = Column(Boolean, default=False)
    time_created = Column(Date, server_default=func.now(), nullable=True)
    deleted = Column(Boolean, default=False)

    specialization_id = Column(Integer, ForeignKey('specializations.specialization_id'))


    projects = relationship('Project', secondary='project_users', back_populates='users')
    reports = relationship("Report", backref='user')


class ProjectUser(Base):
    __tablename__ = 'project_users'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    project_id = Column(Integer, ForeignKey('projects.id'))