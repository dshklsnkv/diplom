from datetime import datetime
from Model.parameterlimit import ParameterLimit
from config import db
from sqlalchemy.sql import select
from sqlalchemy import update as sql_update, delete as sql_delete


class ParameterLimitRepository:

    @staticmethod
    async def create(parameterlimit_data: ParameterLimit):
        async with db as session:
            async with session.begin():
                session.add(parameterlimit_data)
            await db.commit_rollback()

    @staticmethod
    async def get_parameterlimit_by_id(parameterlimit_id: int):
        async with db as session:
            stmt = select(ParameterLimit).where(
                ParameterLimit.id_parameterlimit == parameterlimit_id)
            result = await session.execute(stmt)
            parameterlimit = result.scalars().first()
            return parameterlimit

    @staticmethod
    async def get_all_parameterlimits():
        async with db as session:
            query = select(ParameterLimit)
            result = await session.execute(query)
            return result.scalars().all()

    @staticmethod
    async def update(parameterlimit_id: int, parameterlimit_data: ParameterLimit):
        async with db as session:
            stmt = select(ParameterLimit).where(
                ParameterLimit.id_parameterlimit == parameterlimit_id)
            result = await session.execute(stmt)

            parameterlimit = result.scalars().first()
            parameterlimit.id_parameter = parameterlimit_data.id_parameter
            parameterlimit.id_limit_type = parameterlimit_data.id_limit_type
            parameterlimit.min_limit = parameterlimit_data.min_limit
            parameterlimit.max_limit = parameterlimit_data.max_limit
            parameterlimit.moment_begin = parameterlimit_data.moment_begin
            parameterlimit.moment_end = parameterlimit_data.moment_end

            # query = sql_update(Parameter).where(Parameter.id_parameter == parameter_id).values({
            #     "name_parameter": "123",  "id_place_izmer": 11}).execution_options(synchronize_session="fetch")
            query = sql_update(ParameterLimit).where(
                ParameterLimit.id_parameterlimit == parameterlimit_id).values(
                # **parameter.dict()).execution_options(synchronize_session="fetch")
                id_parameter=parameterlimit_data.id_parameter,
                id_limit_type=parameterlimit_data.id_limit_type,
                min_limit=parameterlimit_data.min_limit,
                max_limit=parameterlimit_data.max_limit,
                moment_begin=parameterlimit_data.moment_begin,
                moment_end=parameterlimit_data.moment_end).execution_options(synchronize_session="fetch")

            await session.execute(query)
            await db.commit_rollback()

    @staticmethod
    async def delete(parameterlimit_id: int):
        async with db as session:
            query = sql_delete(ParameterLimit).where(
                ParameterLimit.id_parameterlimit == parameterlimit_id)
            await session.execute(query)
            await db.commit_rollback()
