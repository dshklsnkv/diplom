from datetime import datetime
from Model.parameter import Parameter
from config import async_db
from sqlalchemy.sql import select
from sqlalchemy import select, update, delete
from sqlalchemy.orm import Session
from sqlmodel import SQLModel, select
from typing import List, Optional


class ParameterRepository:

    # Запрос параметров
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
        async with async_db() as session:
            query = select(Parameter)
            # фильтры накладываются на данном уровне
            # для тестовых полей использовать like или ilike (регистронезависимое сравнение) вместо ==
            # Маска поиска задается на уровне клиента
            # Для идентификаторов использовать списки и конструкцию "in", что бы можно было пачкой запрашивать
            if idParameter:
                query = query.filter(Parameter.id_parameter.in_(idParameter))
            if nameParameter:
                query = query.filter(Parameter.name_parameter.like(nameParameter))
            if idPhysicalType:
                query = query.filter(Parameter.id_physical_type.in_(idPhysicalType))
            if idPlaceIzmer:
                query = query.filter(Parameter.id_place_izmer.in_(idPlaceIzmer))
            if idSredaIzmer:
                query = query.filter(Parameter.id_sreda_izmer.in_(idSredaIzmer))
            if idUnits:
                query = query.filter(Parameter.id_units.in_(idUnits))
            if momentBegin:
                query = query.filter(Parameter.moment_begin == momentBegin)
            if momentEnd:
                query = query.filter(Parameter.moment_end == momentEnd)
            result = await session.execute(query)
            return result.scalars().all()

    @staticmethod
    async def create(parameter_data: Parameter):
        async with async_db() as session:
            async with session.begin():
                session.add(parameter_data)
            await session.commit()
            # await db.commit_rollback()

    @staticmethod
    async def get_parameter_by_id(parameter_id: int):
        async with async_db() as session:
            stmt = select(Parameter).where(Parameter.id_parameter == parameter_id)
            result = await session.execute(stmt)
            parameter = result.scalars().first()
            return parameter

    @staticmethod
    async def get_all_parameters():
        async with async_db() as session:
            query = select(Parameter)
            result = await session.execute(query)
            return result.scalars().all()

    @staticmethod
    async def update(parameter_id: int, parameter_data: Parameter):
        async with async_db() as session:
            stmt = select(Parameter).where(Parameter.id_parameter == parameter_id)
            result = await session.execute(stmt)

            parameter = result.scalars().first()
            parameter.name_parameter = parameter_data.name_parameter
            parameter.moment_begin = parameter_data.moment_begin
            parameter.moment_end = parameter_data.moment_end
            parameter.id_physical_type = parameter_data.id_physical_type
            parameter.id_place_izmer = parameter_data.id_place_izmer
            parameter.id_sreda_izmer = parameter_data.id_sreda_izmer
            parameter.id_units = parameter_data.id_units

            # query = sql_update(Parameter).where(Parameter.id_parameter == parameter_id).values({
            #     "name_parameter": "123",  "id_place_izmer": 11}).execution_options(synchronize_session="fetch")
            query = update(Parameter).where(Parameter.id_parameter == parameter_id).values(
                # **parameter.dict()).execution_options(synchronize_session="fetch")
                name_parameter=parameter.name_parameter,
                moment_begin=parameter.moment_begin,
                moment_end=parameter.moment_end,
                id_physical_type=parameter.id_physical_type,
                id_place_izmer=parameter.id_place_izmer,
                id_sreda_izmer=parameter.id_sreda_izmer,
                id_units=parameter.id_units)

            await session.execute(query)
            await session.commit()
            # await db.commit_rollback()

    @staticmethod
    async def delete(parameter_id: int):
        async with async_db() as session:
            query = delete(Parameter).where(Parameter.id_parameter == parameter_id)
            await session.execute(query)
            await session.commit()
            # await db.commit_rollback()
