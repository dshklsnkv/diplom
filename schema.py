from datetime import datetime
from typing import List, Optional

import strawberry


@strawberry.type
class ParameterLimitType:
    id_parameterlimit: Optional[int]
    id_parameter: int
    id_limit_type: int
    min_limit: int
    max_limit: int
    moment_begin: datetime
    moment_end: datetime


@strawberry.type
class ParameterValueType:
    id_parameterdatasourse: Optional[int]
    moment_change: Optional[datetime]
    value: int


@strawberry.type
class ParameterDataSourseType:
    id_parameterdatasourse: Optional[int]
    id_parameter: int
    id_data_sourse: int
    data_sourse_key: str
    moment_begin: datetime
    moment_end: datetime

    @strawberry.field(description="Значения")
    async def ParameterValue(
            self,
            momentChange: Optional[datetime] = None,
            value: Optional[List[int]] = None
    ) -> List[ParameterValueType]:
        from Resolver.parametervalue import ParameterValueResolver
        parentId = []
        parentId.append(self.id_parameterdatasourse)
        return await ParameterValueResolver.getParamValues(
            self=self,
            idParameterDataSourse=parentId,
            momentChange=momentChange,
            value=value
        )


@strawberry.type
class ParameterType:
    id_parameter: Optional[int]
    name_parameter: str
    moment_begin: datetime
    moment_end: datetime
    id_physical_type: Optional[int]
    id_place_izmer: Optional[int]
    id_sreda_izmer: Optional[int]
    id_units: Optional[int]

    # Вот так описываются Поля-Типы (вложенные сущности / иерархия)
    # Атрибут описывается как Функция, возвращающая сущность или список сущностей
    @strawberry.field(description="Источники данных")
    async def ParameterDataSourse(
            self,
            idDataSourse: Optional[List[int]] = None,
            dataSourseKey: Optional[str] = None
    ) -> List[ParameterDataSourseType]:
        from Resolver.parameterdatasourse import ParameterDataSourseResolver
        parentId = []
        parentId.append(self.id_parameter)
        # Вызываем резолвер. В параметр резолвера передаем ключ от родителя (self.id_parameter)
        return await ParameterDataSourseResolver.getParamDataSourses(
            self=self,
            idParameter=parentId,
            idDataSourse=idDataSourse,
            dataSourseKey=dataSourseKey
        )

    @strawberry.field(description="Уставки")
    async def ParameterLimit(
            self,
            idLimitType: Optional[List[int]] = None,
            minLimit: Optional[List[int]] = None,
            maxLimit: Optional[List[int]] = None,
            momentBegin: Optional[datetime] = None,
            momentEnd: Optional[datetime] = None
    ) -> List[ParameterLimitType]:
        from Resolver.parameterlimit import ParameterLimitResolver
        parentId = []
        parentId.append(self.id_parameter)
        return await ParameterLimitResolver.getParameterLimits(
            self=self,
            idParameter=parentId,
            idLimitType=idLimitType,
            minLimit=minLimit,
            maxLimit=maxLimit,
            momentBegin=momentBegin,
            momentEnd=momentEnd
        )


@strawberry.input
class ParameterInput:
    id_parameter: Optional[int]
    name_parameter: str
    moment_begin: datetime
    moment_end: datetime
    id_physical_type: int
    id_place_izmer: int
    id_sreda_izmer: int
    id_units: int


@strawberry.input
class ParameterDataSourseInput:
    id_parameterdatasourse: Optional[int]
    id_parameter: int
    id_data_sourse: int
    data_sourse_key: str
    moment_begin: datetime
    moment_end: datetime


@strawberry.input
class ParameterLimitInput:
    id_parameterlimit: Optional[int]
    id_parameter: int
    id_limit_type: int
    min_limit: int
    max_limit: int
    moment_begin: datetime
    moment_end: datetime


@strawberry.input
class ParameterValueInput:
    id_parameterdatasourse: Optional[int]
    moment_change: Optional[datetime]
    value: int


@strawberry.type
class DirectoryType:
    id_directory: Optional[int]
    name_directory: str
    moment_begin: datetime
    moment_end: datetime


@strawberry.input
class DirectoryInput:
    id_directory: Optional[int]
    name_directory: str
    moment_begin: datetime
    moment_end: datetime


@strawberry.type
class DirectoryValueType:
    id_directoryvalue: Optional[int]
    id_directory: int
    long_name: str
    short_name: str
    moment_begin: datetime
    moment_end: datetime


@strawberry.input
class DirectoryValueInput:
    id_directoryvalue: Optional[int]
    id_directory: int
    long_name: str
    short_name: str
    moment_begin: datetime
    moment_end: datetime
