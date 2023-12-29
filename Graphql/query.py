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


@strawberry.type
class Query:

    @strawberry.field
    def hello(self) -> str:
        return "Hello World!"

    @strawberry.field
    async def get_all_parameters(self) -> List[ParameterType]:
        return await ParameterService.get_all()

    @strawberry.field
    async def get_parameter_by_id(self, id_parameter: int) -> ParameterType:
        return await ParameterService.get_by_id(id_parameter)

    @strawberry.field
    async def get_all_parameterdatasourses(self) -> List[ParameterDataSourseType]:
        return await ParameterDataSourseService.get_all()

    @strawberry.field
    async def get_parameterdatasourse_by_id(self, id_parameterdatasourse: int) -> ParameterDataSourseType:
        return await ParameterDataSourseService.get_by_id(id_parameterdatasourse)

    @strawberry.field
    async def get_all_parameterlimits(self) -> List[ParameterLimitType]:
        return await ParameterLimitService.get_all()

    @strawberry.field
    async def get_parameterlimit_by_id(self, id_parameterlimit: int) -> ParameterLimitType:
        return await ParameterLimitService.get_by_id(id_parameterlimit)

    @strawberry.field
    async def get_all_parametervalues(self) -> List[ParameterValueType]:
        return await ParameterValueService.get_all()

    @strawberry.field
    async def get_parametervalue_by_id(self, id_parameterdatasourse: int) -> ParameterValueType:
        return await ParameterValueService.get_by_id(id_parameterdatasourse)

    @strawberry.field
    async def get_all_directorys(self) -> List[DirectoryType]:
        return await DirectoryService.get_all()

    @strawberry.field
    async def get_directory_by_id(self, id_directory: int) -> DirectoryType:
        return await DirectoryService.get_by_id(id_directory)

    @strawberry.field
    async def get_all_directoryvalues(self) -> List[DirectoryValueType]:
        return await DirectoryValueService.get_all()

    @strawberry.field
    async def get_directoryvalue_by_id(self, id_directoryvalue: int) -> DirectoryValueType:
        return await DirectoryValueService.get_by_id(id_directoryvalue)
