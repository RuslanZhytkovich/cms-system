from core.db import Base
from sqlalchemy import Boolean
from sqlalchemy import Column
from sqlalchemy import Date
from sqlalchemy import Float
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import UUID
from sqlalchemy.sql import func


class Report(Base):
    __tablename__ = "reports"
    report_id = Column(Integer, autoincrement=True, primary_key=True, index=True)
    date = Column(Date, server_default=func.now(), nullable=False)
    hours = Column(Float, nullable=False)
    comment = Column(String, nullable=False)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.user_id"))
    project_id = Column(Integer, ForeignKey("projects.project_id"))
    is_deleted = Column(Boolean, default=False)
