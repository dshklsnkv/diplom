from datetime import datetime
from typing import Optional
from sqlalchemy import Column, Integer, String, TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class ParameterLimit(Base):
    __tablename__ = 'parameter_limit'

    id_parameterlimit: Optional[int] = Column(Integer, primary_key=True, nullable=True)
    id_parameter: int = Column(Integer)
    id_limit_type: int = Column(Integer)
    min_limit: int = Column(Integer)
    max_limit: int = Column(Integer)
    moment_begin: datetime = Column(TIMESTAMP)
    moment_end: datetime = Column(TIMESTAMP)
