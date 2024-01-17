from sqlalchemy import Float
from sqlalchemy.sql import func

from src.backend.users.models import *


class Report(Base):
    __tablename__ = "reports"

    id = Column(Integer, autoincrement=True, primary_key=True, index=True)
    date = Column(Date, server_default=func.now(), nullable=True)
    hours = Column(Float, nullable=False)
    comment = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))
    project_id = Column(Integer, ForeignKey('projects.id'))