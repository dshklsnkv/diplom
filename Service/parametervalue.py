from datetime import datetime

from Model.parametervalue import ParameterValue
from Repository.parametervalue import ParameterValueRepository
from schema import ParameterValueInput, ParameterValueType


class ParameterValueService:

    @staticmethod
    async def add_parametervalue(parametervalue_data: ParameterValueInput):
        parametervalue = ParameterValue()
        parametervalue.id_parameterdatasourse = parametervalue_data.id_parameterdatasourse
        parametervalue.moment_change = parametervalue_data.moment_change
        parametervalue.value = parametervalue_data.value
        # parameter.moment_begin = parameter_data.moment_begin
        # parameter.moment_end = parameter_data.moment_end
        # parameterlimit.moment_begin = parameterlimit_data.moment_begin if parameterlimit_data.moment_begin else datetime.now()
        # parameterlimit.moment_end = parameterlimit_data.moment_end if parameterlimit_data.moment_end else datetime.strptime(
        #     '9999-12-31 23:59:59', '%Y-%m-%d %H:%M:%S')

        await ParameterValueRepository.create(parametervalue)

        return ParameterValueType(id_parameterdatasourse=parametervalue.id_parameterdatasourse,
                                  moment_change=parametervalue.moment_change,
                                  value=parametervalue.value)

    @staticmethod
    async def get_all():
        list_parametervalue = await ParameterValueRepository.get_all_parametervalues()
        return [ParameterValueType(id_parameterdatasourse=parametervalue.id_parameterdatasourse,
                                  moment_change=parametervalue.moment_change,
                                  value=parametervalue.value) for parametervalue in
                list_parametervalue]

    @staticmethod
    async def get_by_id(parametervalue_id: int):
        parametervalue = await ParameterValueRepository.get_parametervalue_by_id(parametervalue_id)
        return ParameterValueType(id_parameterdatasourse=parametervalue.id_parameterdatasourse,
                                  moment_change=parametervalue.moment_change,
                                  value=parametervalue.value)

    @staticmethod
    async def delete(parametervalue_id: int):
        await ParameterValueRepository.delete(parametervalue_id)
        return f'Successfully deleted data by id {parametervalue_id}'

    @staticmethod
    async def update(parametervalue_id: int, parametervalue_data: ParameterValueInput):
        parametervalue = ParameterValue()
        parametervalue.id_parameterdatasourse = parametervalue_data.id_parameterdatasourse
        parametervalue.moment_change = parametervalue_data.moment_change
        parametervalue.value = parametervalue_data.value
        await ParameterValueRepository.update(parametervalue_id, parametervalue)

        return f'Successfully updated data by id {parametervalue_id}'
