from datetime import datetime
from Model.parameterdatasourse import ParameterDataSourse
from config import db
from sqlalchemy.sql import select
from sqlalchemy import update as sql_update, delete as sql_delete


class ParameterDataSourseRepository:

    @staticmethod
    async def create(parameterdatasourse_data: ParameterDataSourse):
        async with db as session:
            async with session.begin():
                session.add(parameterdatasourse_data)
            await db.commit_rollback()

    @staticmethod
    async def get_parameterdatasourse_by_id(parameterdatasourse_id: int):
        async with db as session:
            stmt = select(ParameterDataSourse).where(
                ParameterDataSourse.id_parameterdatasourse == parameterdatasourse_id)
            result = await session.execute(stmt)
            parameterdatasourse = result.scalars().first()
            return parameterdatasourse

    @staticmethod
    async def get_all_parameterdatasourses():
        async with db as session:
            query = select(ParameterDataSourse)
            result = await session.execute(query)
            return result.scalars().all()

    @staticmethod
    async def update(parameterdatasourse_id: int, parameterdatasourse_data: ParameterDataSourse):
        async with db as session:
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
            query = sql_update(ParameterDataSourse).where(
                ParameterDataSourse.id_parameterdatasourse == parameterdatasourse_id).values(
                # **parameter.dict()).execution_options(synchronize_session="fetch")
                id_parameter=parameterdatasourse_data.id_parameter,
                id_data_sourse=parameterdatasourse_data.id_data_sourse,
                data_sourse_key=parameterdatasourse_data.data_sourse_key,
                moment_begin=parameterdatasourse_data.moment_begin,
                moment_end=parameterdatasourse_data.moment_end).execution_options(synchronize_session="fetch")

            await session.execute(query)
            await db.commit_rollback()

    @staticmethod
    async def delete(parameterdatasourse_id: int):
        async with db as session:
            query = sql_delete(ParameterDataSourse).where(
                ParameterDataSourse.id_parameterdatasourse == parameterdatasourse_id)
            await session.execute(query)
            await db.commit_rollback()
