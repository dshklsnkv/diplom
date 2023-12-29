from datetime import datetime
from typing import Optional
from sqlalchemy import Column, Integer, String, TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Directory(Base):
    __tablename__ = "directory"

    id_directory: Optional[int] = Column(Integer, primary_key=True, nullable=True)
    name_directory: str = Column(String)
    moment_begin: datetime = Column(TIMESTAMP)
    moment_end: datetime = Column(TIMESTAMP)
