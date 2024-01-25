from typing import List

import strawberry

from Service.parameter import ParameterService
from schema import ParameterType

from Service.parameterdatasourse import ParameterDataSourseService
from schema import ParameterDataSourseType

from Service.parameterlimit import ParameterLimitService
from schema import ParameterLimitType

from Service.parametervalue import ParameterValueService
from schema import ParameterValueType

from Service.directory import DirectoryService
from schema import DirectoryType

from Service.directoryvalue import DirectoryValueService
from schema import DirectoryValueType

from typing import Optional
from config import db
from sqlalchemy.sql import select
from Model.parameter import Parameter
from datetime import datetime

from Model.parameterdatasourse import ParameterDataSourse
from Model.parameterlimit import ParameterLimit
from Model.parametervalue import ParameterValue
from Model.directory import Directory
from Model.directoryvalue import DirectoryValue


@strawberry.type
class Query:

    # @strawberry.field
    # def hello(self) -> str:
    #     return "Hello World!"

    @strawberry.field
    # async def get_all_parameters(self) -> List[ParameterType]:
    #     return await ParameterService.get_all()
    async def Parameters(self, name_parameter: Optional[str] = None, id_physical_type: Optional[int] = None,
                         moment_begin: Optional[datetime] = None, moment_end: Optional[datetime] = None,
                         id_place_izmer: Optional[int] = None, id_sreda_izmer: Optional[int] = None,
                         id_units: Optional[int] = None) -> \
            List[ParameterType]:
        async with db as session:
            query = select(Parameter)

            if name_parameter:
                query = query.where(Parameter.name_parameter == name_parameter)

            if id_physical_type:
                query = query.where(Parameter.id_physical_type == id_physical_type)

            if moment_begin:
                query = query.where(Parameter.moment_begin == moment_begin)

            if moment_end:
                query = query.where(Parameter.moment_end == moment_end)

            if id_place_izmer:
                query = query.where(Parameter.id_place_izmer == id_place_izmer_type)

            if id_sreda_izmer:
                query = query.where(Parameter.id_sreda_izmer == id_sreda_izmer_type)

            if id_units:
                query = query.where(Parameter.id_units == id_units_type)

            result = await session.execute(query)
            parameters = result.scalars().all()

            return [ParameterType(id_parameter=parameter.id_parameter, name_parameter=parameter.name_parameter,
                                  moment_begin=parameter.moment_begin, moment_end=parameter.moment_end,
                                  id_physical_type=parameter.id_physical_type, id_place_izmer=parameter.id_place_izmer,
                                  id_sreda_izmer=parameter.id_sreda_izmer, id_units=parameter.id_units) for parameter in
                    parameters]

    @strawberry.field
    async def get_parameter_by_id(self, id_parameter: int) -> ParameterType:
        return await ParameterService.get_by_id(id_parameter)

    @strawberry.field
    async def ParameterDatasourses(self, id_parameter: Optional[int] = None,
                                   id_data_sourse: Optional[int] = None,
                                   data_sourse_key: Optional[str] = None,
                                   moment_begin: Optional[datetime] = None,
                                   moment_end: Optional[datetime] = None) -> \
            List[ParameterDataSourseType]:
        async with db as session:
            query = select(ParameterDataSourse)

            if id_parameter:
                query = query.where(ParameterDataSourse.id_parameter == id_parameter)

            if id_data_sourse:
                query = query.where(ParameterDataSourse.id_data_sourse == id_data_sourse)

            if data_sourse_key:
                query = query.where(ParameterDataSourse.data_sourse_key == data_sourse_key)

            if moment_begin:
                query = query.where(ParameterDataSourse.moment_begin == moment_begin)

            if moment_end:
                query = query.where(ParameterDataSourse.moment_end == moment_end)

            result = await session.execute(query)
            parameterdatasourses = result.scalars().all()

            return [ParameterDataSourseType(id_parameterdatasourse=parameterdatasourse.id_parameterdatasourse,
                                            id_parameter=parameterdatasourse.id_parameter,
                                            id_data_sourse=parameterdatasourse.id_data_sourse,
                                            data_sourse_key=parameterdatasourse.data_sourse_key,
                                            moment_begin=parameterdatasourse.moment_begin,
                                            moment_end=parameterdatasourse.moment_end) for parameterdatasourse in
                    parameterdatasourses]

    @strawberry.field
    async def get_parameterdatasourse_by_id(self, id_parameterdatasourse: int) -> ParameterDataSourseType:
        return await ParameterDataSourseService.get_by_id(id_parameterdatasourse)

    @strawberry.field
    async def ParameterLimits(self, id_parameter: Optional[int] = None,
                              id_limit_type: Optional[int] = None,
                              min_limit: Optional[int] = None,
                              max_limit: Optional[int] = None,
                              moment_begin: Optional[datetime] = None,
                              moment_end: Optional[datetime] = None) -> \
            List[ParameterLimitType]:
        async with db as session:
            query = select(ParameterLimit)

            if id_parameter:
                query = query.where(ParameterLimit.id_parameter == id_parameter)

            if id_limit_type:
                query = query.where(ParameterLimit.id_limit_type == id_limit_type)

            if min_limit:
                query = query.where(ParameterLimit.min_limit == min_limit)

            if max_limit:
                query = query.where(ParameterLimit.max_limit == max_limit)

            if moment_begin:
                query = query.where(ParameterLimit.moment_begin == moment_begin)

            if moment_end:
                query = query.where(ParameterLimit.moment_end == moment_end)

            result = await session.execute(query)
            parameterlimits = result.scalars().all()

            return [ParameterLimitType(id_parameterlimit=parameterlimit.id_parameterlimit,
                                       id_parameter=parameterlimit.id_parameter,
                                       id_limit_type=parameterlimit.id_limit_type,
                                       min_limit=parameterlimit.min_limit,
                                       max_limit=parameterlimit.max_limit,
                                       moment_begin=parameterlimit.moment_begin,
                                       moment_end=parameterlimit.moment_end) for parameterlimit in
                    parameterlimits]

    @strawberry.field
    async def get_parameterlimit_by_id(self, id_parameterlimit: int) -> ParameterLimitType:
        return await ParameterLimitService.get_by_id(id_parameterlimit)

    @strawberry.field
    async def ParameterValues(self, moment_change: Optional[datetime] = None,
                              value: Optional[int] = None) -> \
            List[ParameterValueType]:
        async with db as session:
            query = select(ParameterValue)

            if moment_change:
                query = query.where(ParameterValue.moment_change == moment_change)

            if value:
                query = query.where(ParameterValue.value == value)
            result = await session.execute(query)
            parametervalues = result.scalars().all()

            return [ParameterValueType(id_parameterdatasourse=parametervalue.id_parameterdatasourse,
                                       moment_change=parametervalue.moment_change,
                                       value=parametervalue.value) for parametervalue in
                    parametervalues]

    @strawberry.field
    async def get_parametervalue_by_id(self, id_parameterdatasourse: int) -> ParameterValueType:
        return await ParameterValueService.get_by_id(id_parameterdatasourse)

    @strawberry.field
    async def Directorys(self, name_directory: Optional[str] = None,
                         moment_begin: Optional[datetime] = None,
                         moment_end: Optional[datetime] = None) -> \
            List[DirectoryType]:
        async with db as session:
            query = select(Directory)

            if name_directory:
                query = query.where(Directory.name_directory == name_directory)

            if moment_begin:
                query = query.where(Directory.moment_begin == moment_begin)

            if moment_end:
                query = query.where(Directory.moment_end == moment_end)

            result = await session.execute(query)
            directorys = result.scalars().all()

            return [DirectoryType(id_directory=directory.id_directory, name_directory=directory.name_directory,
                                  moment_begin=directory.moment_begin, moment_end=directory.moment_end) for
                    directory in directorys]

    @strawberry.field
    async def get_directory_by_id(self, id_directory: int) -> DirectoryType:
        return await DirectoryService.get_by_id(id_directory)

    @strawberry.field
    async def DirectoryValues(self, id_directory: Optional[int] = None,
                              long_name: Optional[str] = None,
                              short_name: Optional[str] = None,
                              moment_begin: Optional[datetime] = None,
                              moment_end: Optional[datetime] = None) -> \
            List[DirectoryValueType]:
        async with db as session:
            query = select(DirectoryValue)

            if id_directory:
                query = query.where(DirectoryValue.id_directory == id_directory)

            if long_name:
                query = query.where(DirectoryValue.long_name == long_name)

            if short_name:
                query = query.where(DirectoryValue.short_name == short_name)

            if moment_begin:
                query = query.where(DirectoryValue.moment_begin == moment_begin)

            if moment_end:
                query = query.where(DirectoryValue.moment_end == moment_end)

            result = await session.execute(query)
            directoryvalues = result.scalars().all()

            return [DirectoryValueType(id_directoryvalue=directoryvalue.id_directoryvalue,
                                       id_directory=directoryvalue.id_directory,
                                       long_name=directoryvalue.long_name, short_name=directoryvalue.short_name,
                                       moment_begin=directoryvalue.moment_begin, moment_end=directoryvalue.moment_end)
                    for directoryvalue in directoryvalues]

    @strawberry.field
    async def get_directoryvalue_by_id(self, id_directoryvalue: int) -> DirectoryValueType:
        return await DirectoryValueService.get_by_id(id_directoryvalue)
