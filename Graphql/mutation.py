import strawberry
from Service.parameter import ParameterService
from schema import ParameterType, ParameterInput

from Service.parameterdatasourse import ParameterDataSourseService
from schema import ParameterDataSourseType, ParameterDataSourseInput

from Service.parameterlimit import ParameterLimitService
from schema import ParameterLimitType, ParameterLimitInput

from Service.parametervalue import ParameterValueService
from schema import ParameterValueType, ParameterValueInput

from Service.directory import DirectoryService
from schema import DirectoryType, DirectoryInput

from Service.directoryvalue import DirectoryValueService
from schema import DirectoryValueType, DirectoryValueInput


@strawberry.type
class Mutation:

    @strawberry.mutation
    async def create_parameter(self, parameter_data: ParameterInput) -> ParameterType:
        return await ParameterService.add_parameter(parameter_data)

    @strawberry.mutation
    async def delete_parameter(self, parameter_id: int) -> str:
        return await ParameterService.delete(parameter_id)

    @strawberry.mutation
    async def update_parameter(self, parameter_id: int, parameter_data: ParameterInput) -> str:
        return await ParameterService.update(parameter_id, parameter_data)

    @strawberry.mutation
    async def create_parameterdatasourse(self,
                                         parameterdatasourse_data: ParameterDataSourseInput) -> ParameterDataSourseType:
        return await ParameterDataSourseService.add_parameterdatasourse(parameterdatasourse_data)

    @strawberry.mutation
    async def delete_parameterdatasourse(self, parameterdatasourse_id: int) -> str:
        return await ParameterDataSourseService.delete(parameterdatasourse_id)

    @strawberry.mutation
    async def update_parameterdatasourse(self, parameterdatasourse_id: int,
                                         parameterdatasourse_data: ParameterDataSourseInput) -> str:
        return await ParameterDataSourseService.update(parameterdatasourse_id, parameterdatasourse_data)

    @strawberry.mutation
    async def create_parameterlimit(self, parameterlimit_data: ParameterLimitInput) -> ParameterLimitType:
        return await ParameterLimitService.add_parameterlimit(parameterlimit_data)

    @strawberry.mutation
    async def delete_parameterlimit(self, parameterlimit_id: int) -> str:
        return await ParameterLimitService.delete(parameterlimit_id)

    @strawberry.mutation
    async def update_parameterlimit(self, parameterlimit_id: int, parameterlimit_data: ParameterLimitInput) -> str:
        return await ParameterLimitService.update(parameterlimit_id, parameterlimit_data)

    @strawberry.mutation
    async def create_parametervalue(self, parametervalue_data: ParameterValueInput) -> ParameterValueType:
        return await ParameterValueService.add_parametervalue(parametervalue_data)

    @strawberry.mutation
    async def delete_parametervalue(self, parametervalue_id: int) -> str:
        return await ParameterValueService.delete(parametervalue_id)

    @strawberry.mutation
    async def update_parametervalue(self, parametervalue_id: int, parametervalue_data: ParameterValueInput) -> str:
        return await ParameterValueService.update(parametervalue_id, parametervalue_data)

    @strawberry.mutation
    async def create_directory(self, directory_data: DirectoryInput) -> DirectoryType:
        return await DirectoryService.add_directory(directory_data)

    @strawberry.mutation
    async def delete_directory(self, directory_id: int) -> str:
        return await DirectoryService.delete(directory_id)

    @strawberry.mutation
    async def update_directory(self, directory_id: int, directory_data: DirectoryInput) -> str:
        return await DirectoryService.update(directory_id, directory_data)

    @strawberry.mutation
    async def create_directoryvalue(self, directoryvalue_data: DirectoryValueInput) -> DirectoryValueType:
        return await DirectoryValueService.add_directoryvalue(directoryvalue_data)

    @strawberry.mutation
    async def delete_directoryvalue(self, directoryvalue_id: int) -> str:
        return await DirectoryValueService.delete(directoryvalue_id)

    @strawberry.mutation
    async def update_directoryvalue(self, directoryvalue_id: int, directoryvalue_data: DirectoryValueInput) -> str:
        return await DirectoryValueService.update(directoryvalue_id, directoryvalue_data)
