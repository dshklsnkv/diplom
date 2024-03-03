from typing import Optional, List
from schema import ParameterType
from Service.parameter import ParameterService

"""Класс функций резолверов для Параметров"""


class ParameterResolver:
    """"Получить параметры"""

    @staticmethod
    async def getParameters(
            root,
            idParameter: Optional[List[int]] = None,
            nameParameter: Optional[str] = None,
            idPhysicalType: Optional[List[int]] = None,
            idPlaceIzmer: Optional[List[int]] = None,
            idSredaIzmer: Optional[List[int]] = None,
            idUnits: Optional[List[int]] = None
    ) -> List[ParameterType]:
        # Получение данных из сервиса
        parameters = await ParameterService.getParameters(
            root,
            idParameter=idParameter,
            nameParameter=nameParameter,
            idPhysicalType=idPhysicalType,
            idPlaceIzmer=idPlaceIzmer,
            idSredaIzmer=idSredaIzmer,
            idUnits=idUnits
        )
        # Преобразование данных сервиса в тип GraphQL
        return [ParameterType(
            id_parameter=parameter.id_parameter,
            name_parameter=parameter.name_parameter,
            moment_begin=parameter.moment_begin,
            moment_end=parameter.moment_end,
            id_physical_type=parameter.id_physical_type,
            id_place_izmer=parameter.id_place_izmer,
            id_sreda_izmer=parameter.id_sreda_izmer,
            id_units=parameter.id_units
        ) for parameter in parameters]
