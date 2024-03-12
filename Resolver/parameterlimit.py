from typing import Optional, List
from datetime import datetime
from schema import ParameterLimitType
from Service.parameterlimit import ParameterLimitService

"""Класс функций резолверов для Параметров"""


class ParameterLimitResolver:
    """"Получить параметры"""

    @staticmethod
    async def getParameterLimits(
            idParameterLimit: Optional[List[int]] = None,
            idParameter: Optional[List[int]] = None,
            idLimitType: Optional[List[int]] = None,
            minLimit: Optional[List[int]] = None,
            maxLimit: Optional[List[int]] = None,
            momentBegin: Optional[datetime] = None,
            momentEnd: Optional[datetime] = None
    ) -> List[ParameterLimitType]:
        # Получение данных из сервиса
        parameterlimits = await ParameterLimitService.getParameterLimits(
            idParameterLimit=idParameterLimit,
            idParameter=idParameter,
            idLimitType=idLimitType,
            minLimit=minLimit,
            maxLimit=maxLimit,
            momentBegin=momentBegin,
            momentEnd=momentEnd
        )
        # Преобразование данных сервиса в тип GraphQL
        return [ParameterLimitType(
            id_parameterlimit=parameterlimit.id_parameterlimit,
            id_parameter=parameterlimit.id_parameter,
            id_limit_type=parameterlimit.id_limit_type,
            min_limit=parameterlimit.min_limit,
            max_limit=parameterlimit.max_limit,
            moment_begin=parameterlimit.moment_begin,
            moment_end=parameterlimit.moment_end
        ) for parameterlimit in parameterlimits]
