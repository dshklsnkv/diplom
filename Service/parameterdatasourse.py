from datetime import datetime

from Model.parameterdatasourse import ParameterDataSourse
from Repository.parameterdatasourse import ParameterDataSourseRepository
from schema import ParameterDataSourseInput, ParameterDataSourseType
from typing import Optional, List


class ParameterDataSourseService:

    @staticmethod
    async def getParameterDataSourses(
            self,
            idParameterDataSourse: Optional[List[int]] = None,
            idParameter: Optional[List[int]] = None,
            idDataSourse: Optional[List[int]] = None,
            dataSourseKey: Optional[str] = None
    ):
        return await ParameterDataSourseRepository.getParameterDataSourses(
            idParameterDataSourse,
            idParameter,
            idDataSourse,
            dataSourseKey
        )

    @staticmethod
    async def add_parameterdatasourse(parameterdatasourse_data: ParameterDataSourseInput):
        parameterdatasourse = ParameterDataSourse()
        parameterdatasourse.id_parameterdatasourse = parameterdatasourse_data.id_parameterdatasourse
        parameterdatasourse.id_parameter = parameterdatasourse_data.id_parameter
        parameterdatasourse.id_data_sourse = parameterdatasourse_data.id_data_sourse
        parameterdatasourse.data_sourse_key = parameterdatasourse_data.data_sourse_key
        # parameter.moment_begin = parameter_data.moment_begin
        # parameter.moment_end = parameter_data.moment_end
        parameterdatasourse.moment_begin = parameterdatasourse_data.moment_begin if parameterdatasourse_data.moment_begin else datetime.now()
        parameterdatasourse.moment_end = parameterdatasourse_data.moment_end if parameterdatasourse_data.moment_end else datetime.strptime(
            '9999-12-31 23:59:59', '%Y-%m-%d %H:%M:%S')

        await ParameterDataSourseRepository.create(parameterdatasourse)

        return ParameterDataSourseType(id_parameterdatasourse=parameterdatasourse.id_parameterdatasourse,
                                       id_parameter=parameterdatasourse.id_parameter,
                                       id_data_sourse=parameterdatasourse.id_data_sourse,
                                       data_sourse_key=parameterdatasourse.data_sourse_key,
                                       moment_begin=parameterdatasourse.moment_begin,
                                       moment_end=parameterdatasourse.moment_end)

    @staticmethod
    async def get_all():
        list_parameterdatasourse = await ParameterDataSourseRepository.get_all_parameterdatasourses()
        return [ParameterDataSourseType(id_parameterdatasourse=parameterdatasourse.id_parameterdatasourse,
                                        id_parameter=parameterdatasourse.id_parameter,
                                        id_data_sourse=parameterdatasourse.id_data_sourse,
                                        data_sourse_key=parameterdatasourse.data_sourse_key,
                                        moment_begin=parameterdatasourse.moment_begin,
                                        moment_end=parameterdatasourse.moment_end) for parameterdatasourse in
                list_parameterdatasourse]

    @staticmethod
    async def get_by_id(parameterdatasourse_id: int):
        parameterdatasourse = await ParameterDataSourseRepository.get_parameterdatasourse_by_id(parameterdatasourse_id)
        return ParameterDataSourseType(id_parameterdatasourse=parameterdatasourse.id_parameterdatasourse,
                                       id_parameter=parameterdatasourse.id_parameter,
                                       id_data_sourse=parameterdatasourse.id_data_sourse,
                                       data_sourse_key=parameterdatasourse.data_sourse_key,
                                       moment_begin=parameterdatasourse.moment_begin,
                                       moment_end=parameterdatasourse.moment_end)

    @staticmethod
    async def delete(parameterdatasourse_id: int):
        await ParameterDataSourseRepository.delete(parameterdatasourse_id)
        return f'Successfully deleted data by id {parameterdatasourse_id}'

    @staticmethod
    async def update(parameterdatasourse_id: int, parameterdatasourse_data: ParameterDataSourseInput):
        parameterdatasourse = ParameterDataSourse()
        parameterdatasourse.id_parameter = parameterdatasourse_data.id_parameter
        parameterdatasourse.id_data_sourse = parameterdatasourse_data.id_data_sourse
        parameterdatasourse.data_sourse_key = parameterdatasourse_data.data_sourse_key
        parameterdatasourse.moment_begin = parameterdatasourse_data.moment_begin
        parameterdatasourse.moment_end = parameterdatasourse_data.moment_end
        await ParameterDataSourseRepository.update(parameterdatasourse_id, parameterdatasourse)

        return f'Successfully updated data by id {parameterdatasourse_id}'
