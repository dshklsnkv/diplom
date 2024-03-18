from datetime import datetime
from Model.parameterdatasourse import ParameterDataSourse
from config import async_db
from sqlalchemy.sql import select
from sqlalchemy import select, update, delete
from sqlalchemy.future import select as future_select
from sqlalchemy.orm import Session
from typing import List, Optional


class ParameterDataSourseRepository:

    # Запрос источников данных параметра(ов)
    @staticmethod
    async def getParameterDataSourses(
            idParameterDataSourse: Optional[List[int]] = None,
            idParameter: Optional[List[int]] = None,
            idDataSourse: Optional[List[int]] = None,
            dataSourseKey: Optional[str] = None
    ):
        async with async_db() as session:
            query = select(ParameterDataSourse)
            if idParameterDataSourse:
                query = query.filter(ParameterDataSourse.id_parameterdatasourse.in_(idParameterDataSourse))
            if idParameter:
                query = query.filter(ParameterDataSourse.id_parameter.in_(idParameter))
            if idDataSourse:
                query = query.filter(ParameterDataSourse.id_data_sourse.in_(idDataSourse))
            if dataSourseKey:
                query = query.filter(ParameterDataSourse.data_sourse_key.ilike(dataSourseKey))
            result = await session.execute(query)
            return result.scalars().all()

    @staticmethod
    async def create(parameterdatasourse_data: ParameterDataSourse):
        async with async_db() as session:
            async with session.begin():
                session.add(parameterdatasourse_data)
            await session.commit()

    @staticmethod
    async def get_parameterdatasourse_by_id(parameterdatasourse_id: int):
        async with async_db() as session:
            stmt = select(ParameterDataSourse).where(
                ParameterDataSourse.id_parameterdatasourse == parameterdatasourse_id)
            result = await session.execute(stmt)
            parameterdatasourse = result.scalars().first()
            return parameterdatasourse

    @staticmethod
    async def get_all_parameterdatasourses():
        async with async_db() as session:
            query = select(ParameterDataSourse)
            result = await session.execute(query)
            return result.scalars().all()

    @staticmethod
    async def update(parameterdatasourse_id: int, parameterdatasourse_data: ParameterDataSourse):
        async with async_db() as session:
            stmt = select(ParameterDataSourse).where(
                ParameterDataSourse.id_parameterdatasourse == parameterdatasourse_id)
            result = await session.execute(stmt)

            parameterdatasourse = result.scalars().first()
            parameterdatasourse.id_parameter = parameterdatasourse_data.id_parameter
            parameterdatasourse.id_data_sourse = parameterdatasourse_data.id_data_sourse
            parameterdatasourse.data_sourse_key = parameterdatasourse_data.data_sourse_key
            parameterdatasourse.moment_begin = parameterdatasourse_data.moment_begin
            parameterdatasourse.moment_end = parameterdatasourse_data.moment_end

            # query = sql_update(Parameter).where(Parameter.id_parameter == parameter_id).values({
            #     "name_parameter": "123",  "id_place_izmer": 11}).execution_options(synchronize_session="fetch")
            query = update(ParameterDataSourse).where(
                ParameterDataSourse.id_parameterdatasourse == parameterdatasourse_id).values(
                # **parameter.dict()).execution_options(synchronize_session="fetch")
                id_parameter=parameterdatasourse_data.id_parameter,
                id_data_sourse=parameterdatasourse_data.id_data_sourse,
                data_sourse_key=parameterdatasourse_data.data_sourse_key,
                moment_begin=parameterdatasourse_data.moment_begin,
                moment_end=parameterdatasourse_data.moment_end)

            await session.execute(query)
            await session.commit()

    @staticmethod
    async def delete(parameterdatasourse_id: int):
        async with async_db() as session:
            query = delete(ParameterDataSourse).where(
                ParameterDataSourse.id_parameterdatasourse == parameterdatasourse_id)
            await session.execute(query)
            await session.commit()
