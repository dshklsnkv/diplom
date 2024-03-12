from datetime import datetime

from Model.parameterlimit import ParameterLimit
from Repository.parameterlimit import ParameterLimitRepository
from schema import ParameterLimitInput, ParameterLimitType
from typing import List, Optional


class ParameterLimitService:

    @staticmethod
    async def getParameterLimits(
            idParameterLimit: Optional[List[int]] = None,
            idParameter: Optional[List[int]] = None,
            idLimitType: Optional[List[int]] = None,
            minLimit: Optional[List[int]] = None,
            maxLimit: Optional[List[int]] = None,
            momentBegin: Optional[datetime] = None,
            momentEnd: Optional[datetime] = None
    ):
        return await ParameterLimitRepository.getParameterLimits(
            idParameterLimit,
            idParameter,
            idLimitType,
            minLimit,
            maxLimit,
            momentBegin,
            momentEnd
        )

    @staticmethod
    async def add_parameterlimit(parameterlimit_data: ParameterLimitInput):
        parameterlimit = ParameterLimit()
        parameterlimit.id_parameterlimit = parameterlimit_data.id_parameterlimit
        parameterlimit.id_parameter = parameterlimit_data.id_parameter
        parameterlimit.id_limit_type = parameterlimit_data.id_limit_type
        parameterlimit.min_limit = parameterlimit_data.min_limit
        parameterlimit.max_limit = parameterlimit_data.max_limit
        # parameter.moment_begin = parameter_data.moment_begin
        # parameter.moment_end = parameter_data.moment_end
        parameterlimit.moment_begin = parameterlimit_data.moment_begin if parameterlimit_data.moment_begin else datetime.now()
        parameterlimit.moment_end = parameterlimit_data.moment_end if parameterlimit_data.moment_end else datetime.strptime(
            '9999-12-31 23:59:59', '%Y-%m-%d %H:%M:%S')

        await ParameterLimitRepository.create(parameterlimit)

        return ParameterLimitType(id_parameterlimit=parameterlimit.id_parameterlimit,
                                  id_parameter=parameterlimit.id_parameter,
                                  id_limit_type=parameterlimit.id_limit_type,
                                  min_limit=parameterlimit.min_limit,
                                  max_limit=parameterlimit.max_limit,
                                  moment_begin=parameterlimit.moment_begin,
                                  moment_end=parameterlimit.moment_end)

    @staticmethod
    async def get_all():
        list_parameterlimit = await ParameterLimitRepository.get_all_parameterlimits()
        return [ParameterLimitType(id_parameterlimit=parameterlimit.id_parameterlimit,
                                   id_parameter=parameterlimit.id_parameter,
                                   id_limit_type=parameterlimit.id_limit_type,
                                   min_limit=parameterlimit.min_limit,
                                   max_limit=parameterlimit.max_limit,
                                   moment_begin=parameterlimit.moment_begin,
                                   moment_end=parameterlimit.moment_end) for parameterlimit in
                list_parameterlimit]

    @staticmethod
    async def get_by_id(parameterlimit_id: int):
        parameterlimit = await ParameterLimitRepository.get_parameterlimit_by_id(parameterlimit_id)
        return ParameterLimitType(id_parameterlimit=parameterlimit.id_parameterlimit,
                                  id_parameter=parameterlimit.id_parameter,
                                  id_limit_type=parameterlimit.id_limit_type,
                                  min_limit=parameterlimit.min_limit,
                                  max_limit=parameterlimit.max_limit,
                                  moment_begin=parameterlimit.moment_begin,
                                  moment_end=parameterlimit.moment_end)

    @staticmethod
    async def delete(parameterlimit_id: int):
        await ParameterLimitRepository.delete(parameterlimit_id)
        return f'Successfully deleted data by id {parameterlimit_id}'

    @staticmethod
    async def update(parameterlimit_id: int, parameterlimit_data: ParameterLimitInput):
        parameterlimit = ParameterLimit()
        parameterlimit.id_parameterlimit = parameterlimit_data.id_parameterlimit
        parameterlimit.id_parameter = parameterlimit_data.id_parameter
        parameterlimit.id_limit_type = parameterlimit_data.id_limit_type
        parameterlimit.min_limit = parameterlimit_data.min_limit
        parameterlimit.max_limit = parameterlimit_data.max_limit
        parameterlimit.moment_begin = parameterlimit_data.moment_begin
        parameterlimit.moment_end = parameterlimit_data.moment_end
        await ParameterLimitRepository.update(parameterlimit_id, parameterlimit)

        return f'Successfully updated data by id {parameterlimit_id}'
