from datetime import datetime

from Model.parameter import Parameter
from Repository.parameter import ParameterRepository
from schema import ParameterInput, ParameterType
from typing import List, Optional


class ParameterService:

    # Получить Параметры с возможностью фильтрации данных
    @staticmethod
    async def getParameters(
            idParameter: Optional[List[int]] = None,
            nameParameter: Optional[str] = None,
            idPhysicalType: Optional[List[int]] = None,
            idPlaceIzmer: Optional[List[int]] = None,
            idSredaIzmer: Optional[List[int]] = None,
            idUnits: Optional[List[int]] = None,
            momentBegin: Optional[datetime] = None,
            momentEnd: Optional[datetime] = None
    ):
        # Пока тут просто получение данных через репозиторий
        # В дальнейшем тут может добавиться какая-то дополнительная логика
        return await ParameterRepository.getParameters(
            idParameter=idParameter,
            nameParameter=nameParameter,
            idPhysicalType=idPhysicalType,
            idPlaceIzmer=idPlaceIzmer,
            idSredaIzmer=idSredaIzmer,
            idUnits=idUnits,
            momentBegin=momentBegin,
            momentEnd=momentEnd
        )

    @staticmethod
    async def add_parameter(parameter_data: ParameterInput):
        parameter = Parameter()
        parameter.id_parameter = parameter_data.id_parameter
        parameter.name_parameter = parameter_data.name_parameter
        # parameter.moment_begin = parameter_data.moment_begin
        # parameter.moment_end = parameter_data.moment_end
        parameter.moment_begin = parameter_data.moment_begin if parameter_data.moment_begin else datetime.now()
        parameter.moment_end = parameter_data.moment_end if parameter_data.moment_end else datetime.strptime(
            '9999-12-31 23:59:59', '%Y-%m-%d %H:%M:%S')
        parameter.id_physical_type = parameter_data.id_physical_type
        parameter.id_place_izmer = parameter_data.id_place_izmer
        parameter.id_sreda_izmer = parameter_data.id_sreda_izmer
        parameter.id_units = parameter_data.id_units

        await ParameterRepository.create(parameter)

        return ParameterType(id_parameter=parameter.id_parameter, name_parameter=parameter.name_parameter,
                             moment_begin=parameter.moment_begin, moment_end=parameter.moment_end,
                             id_physical_type=parameter.id_physical_type, id_place_izmer=parameter.id_place_izmer,
                             id_sreda_izmer=parameter.id_sreda_izmer, id_units=parameter.id_units)

    @staticmethod
    async def get_all():
        list_parameter = await ParameterRepository.get_all_parameters()
        return [ParameterType(id_parameter=parameter.id_parameter, name_parameter=parameter.name_parameter,
                              moment_begin=parameter.moment_begin, moment_end=parameter.moment_end,
                              id_physical_type=parameter.id_physical_type, id_place_izmer=parameter.id_place_izmer,
                              id_sreda_izmer=parameter.id_sreda_izmer, id_units=parameter.id_units) for parameter in
                list_parameter]

    @staticmethod
    async def get_by_id(parameter_id: int):
        parameter = await ParameterRepository.get_parameter_by_id(parameter_id)
        return ParameterType(id_parameter=parameter.id_parameter, name_parameter=parameter.name_parameter,
                             moment_begin=parameter.moment_begin, moment_end=parameter.moment_end,
                             id_physical_type=parameter.id_physical_type, id_place_izmer=parameter.id_place_izmer,
                             id_sreda_izmer=parameter.id_sreda_izmer, id_units=parameter.id_units)

    @staticmethod
    async def delete(parameter_id: int):
        await ParameterRepository.delete(parameter_id)
        return f'Successfully deleted data by id {parameter_id}'

    @staticmethod
    async def update(parameter_id: int, parameter_data: ParameterInput):
        parameter = Parameter()
        parameter.name_parameter = parameter_data.name_parameter
        parameter.moment_begin = parameter_data.moment_begin
        parameter.moment_end = parameter_data.moment_end
        parameter.id_physical_type = parameter_data.id_physical_type
        parameter.id_place_izmer = parameter_data.id_place_izmer
        parameter.id_sreda_izmer = parameter_data.id_sreda_izmer
        parameter.id_units = parameter_data.id_units
        await ParameterRepository.update(parameter_id, parameter)

        return f'Successfully updated data by id {parameter_id}'
