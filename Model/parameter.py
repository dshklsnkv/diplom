from datetime import datetime
from typing import Optional
from sqlalchemy import Column, Integer, String, TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Parameter(Base):
    __tablename__ = "parameter"

    id_parameter: Optional[int] = Column(Integer, primary_key=True, nullable=True)
    name_parameter: str = Column(String)
    moment_begin: datetime = Column(TIMESTAMP)
    moment_end: datetime = Column(TIMESTAMP)
    id_physical_type: int = Column(Integer)
    id_place_izmer: int = Column(Integer)
    id_sreda_izmer: int = Column(Integer)
    id_units: int = Column(Integer)

#
# class ParameterValue(SQLModel, table=True):
#     __tablename__ = 'parameter_value'
#
#     id_parameter_data_sourse: int = Column(Integer, primary_key=True)
#     moment_change: datetime = Column(DateTime)
#     value: int = Column(Integer)
#
#
# class DirectoryValue(SQLModel, table=True):
#     __tablename__ = 'directory_value'
#
#     id_directory_value: int = Column(Integer, primary_key=True)
#     id_directory: int = Column(Integer)
#     long_name: str = Column(String)
#     short_name: str = Column(String)
#     moment_begin: datetime = Column(DateTime)
#     moment_end: datetime = Column(DateTime)
#
#
# class Directory(SQLModel, table=True):
#     __tablename__ = 'directory'
#
#     id_directory: int = Column(Integer, primary_key=True)
#     name_directory: str = Column(String)
#     moment_begin: datetime = Column(DateTime)
#     moment_end: datetime = Column(DateTime)
