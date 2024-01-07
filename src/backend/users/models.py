import uuid
from enum import Enum
from sqlalchemy import Enum as SQLAlchemyEnum, Column, String, Integer, Boolean, ForeignKey, Date
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from src.backend.core.db import Base


class RoleEnum(str, Enum):
    admin = "admin"
    manager = "manager"
    developer = "developer"


class Users(Base):
    __tablename__ = "users"

    user_id = Column(String, primary_key=True, index=True, default=str(uuid.uuid4()))
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    name = Column(String, nullable=True)
    second_name = Column(String, nullable=True)
    role = Column(SQLAlchemyEnum(RoleEnum), nullable=False, default=RoleEnum.developer)
    telegram = Column(String, nullable=True, unique=False)
    phone_number = Column(String, nullable=True, unique=False)
    bench = Column(Boolean, default=False)
    time_created = Column(Date, server_default=func.now(), nullable=True)
    is_deleted = Column(Boolean, default=False)
    last_login = Column(Date, nullable=True)

    specialization_id = Column(Integer, ForeignKey('specializations.specialization_id'))

    projects = relationship('Project', secondary='project_users', back_populates='users')
    reports = relationship("Report", backref='user')


