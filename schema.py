from datetime import datetime
from typing import Optional

import strawberry


@strawberry.type
class ParameterType:
    id_parameter: Optional[int]
    name_parameter: str
    moment_begin: datetime
    moment_end: datetime
    id_physical_type: int
    id_place_izmer: int
    id_sreda_izmer: int
    id_units: int


@strawberry.input
class ParameterInput:
    id_parameter: Optional[int]
    name_parameter: str
    moment_begin: datetime
    moment_end: datetime
    id_physical_type: int
    id_place_izmer: int
    id_sreda_izmer: int
    id_units: int


@strawberry.type
class ParameterDataSourseType:
    id_parameterdatasourse: Optional[int]
    id_parameter: int
    id_data_sourse: int
    data_sourse_key: str
    moment_begin: datetime
    moment_end: datetime


@strawberry.input
class ParameterDataSourseInput:
    id_parameterdatasourse: Optional[int]
    id_parameter: int
    id_data_sourse: int
    data_sourse_key: str
    moment_begin: datetime
    moment_end: datetime


@strawberry.type
class ParameterLimitType:
    id_parameterlimit: Optional[int]
    id_parameter: int
    id_limit_type: int
    min_limit: int
    max_limit: int
    moment_begin: datetime
    moment_end: datetime


@strawberry.input
class ParameterLimitInput:
    id_parameterlimit: Optional[int]
    id_parameter: int
    id_limit_type: int
    min_limit: int
    max_limit: int
    moment_begin: datetime
    moment_end: datetime


@strawberry.type
class ParameterValueType:
    id_parameterdatasourse: Optional[int]
    moment_change: Optional[datetime]
    value: int


@strawberry.input
class ParameterValueInput:
    id_parameterdatasourse: Optional[int]
    moment_change: Optional[datetime]
    value: int


@strawberry.type
class DirectoryType:
    id_directory: Optional[int]
    name_directory: str
    moment_begin: datetime
    moment_end: datetime


@strawberry.input
class DirectoryInput:
    id_directory: Optional[int]
    name_directory: str
    moment_begin: datetime
    moment_end: datetime


@strawberry.type
class DirectoryValueType:
    id_directoryvalue: Optional[int]
    id_directory: int
    long_name: str
    short_name: str
    moment_begin: datetime
    moment_end: datetime


@strawberry.input
class DirectoryValueInput:
    id_directoryvalue: Optional[int]
    id_directory: int
    long_name: str
    short_name: str
    moment_begin: datetime
    moment_end: datetime
