from datetime import datetime
from typing import Optional
from sqlalchemy import Column, Integer, String, TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class ParameterDataSourse(Base):
    __tablename__ = 'parameter_data_sourse'

    id_parameterdatasourse: Optional[int] = Column(Integer, primary_key=True, nullable=True)
    id_parameter: int = Column(Integer)
    id_data_sourse: int = Column(Integer)
    data_sourse_key: str = Column(String)
    moment_begin: datetime = Column(TIMESTAMP)
    moment_end: datetime = Column(TIMESTAMP)
