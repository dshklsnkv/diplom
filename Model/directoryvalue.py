from datetime import datetime
from typing import Optional
from sqlalchemy import Column, Integer, String, TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class DirectoryValue(Base):
    __tablename__ = "directory_value"

    id_directoryvalue: Optional[int] = Column(Integer, primary_key=True, nullable=True)
    id_directory: int = Column(Integer)
    long_name: str = Column(String)
    short_name: str = Column(String)
    moment_begin: datetime = Column(TIMESTAMP)
    moment_end: datetime = Column(TIMESTAMP)
