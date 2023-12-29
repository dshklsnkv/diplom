from datetime import datetime
from typing import Optional
from sqlalchemy import Column, Integer, TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class ParameterValue(Base):
    __tablename__ = "parameter_value"

    id_parameterdatasourse: Optional[int] = Column(Integer, primary_key=True, nullable=True)
    moment_change: Optional[datetime] = Column(TIMESTAMP, primary_key=True, nullable=True)
    value: int = Column(Integer)
