from typing import Optional, List
from datetime import datetime
from schema import ParameterValueType
from Service.parametervalue import ParameterValueService

"""Класс функций резолверов для Параметров"""


class ParameterValueResolver:
    """"Получить параметры"""

    @staticmethod
    async def getParamValues(
            self,
            idParameterDataSourse: Optional[List[int]] = None,
            momentChange: Optional[datetime] = None,
            value: Optional[List[int]] = None
    ) -> List[ParameterValueType]:
        parametervalues = await ParameterValueService.getParameterValues(
            self,
            idParameterDataSourse,
            momentChange,
            value
        )
        return [ParameterValueType(
            id_parameterdatasourse=parametervalue.id_parameterdatasourse,
            moment_change=parametervalue.moment_change,
            value=parametervalue.value
        ) for parametervalue in parametervalues]
