from typing import Optional, List
from schema import ParameterDataSourseType
from Service.parameterdatasourse import ParameterDataSourseService
from datetime import datetime

"""Класс функций резолверов для Параметров"""


class ParameterDataSourseResolver:
    """"Получить параметры"""

    @staticmethod
    async def getParamDataSourses(
            idParameterDataSourse: Optional[List[int]] = None,
            idParameter: Optional[List[int]] = None,
            idDataSourse: Optional[List[int]] = None,
            dataSourseKey: Optional[str] = None,
            momentBegin: Optional[datetime] = None,
            momentEnd: Optional[datetime] = None
    ) -> List[ParameterDataSourseType]:
        parameterdatasourses = await ParameterDataSourseService.getParameterDataSourses(
            idParameterDataSourse=idParameterDataSourse,
            idParameter=idParameter,
            idDataSourse=idDataSourse,
            dataSourseKey=dataSourseKey,
            momentBegin=momentBegin,
            momentEnd=momentEnd
        )
        return [ParameterDataSourseType(
            id_parameterdatasourse=parameterdatasourse.id_parameterdatasourse,
            id_parameter=parameterdatasourse.id_parameter,
            id_data_sourse=parameterdatasourse.id_data_sourse,
            data_sourse_key=parameterdatasourse.data_sourse_key,
            moment_begin=parameterdatasourse.moment_begin,
            moment_end=parameterdatasourse.moment_end
        ) for parameterdatasourse in parameterdatasourses]
