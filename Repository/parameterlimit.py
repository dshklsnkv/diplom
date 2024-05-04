from datetime import datetime
from Model.parameterlimit import ParameterLimit
from config import async_db
from sqlalchemy import select, update, delete
from sqlalchemy.orm import Session
from sqlmodel import SQLModel, select
from typing import List, Optional


class ParameterLimitRepository:

    @staticmethod
    async def getParameterLimits(
            idParameterLimit: Optional[List[int]] = None,
            idParameter: Optional[List[int]] = None,
            idLimitType: Optional[List[int]] = None,
            minLimit: Optional[List[int]] = None,
            maxLimit: Optional[List[int]] = None,
            momentBegin: Optional[datetime] = None,
            momentEnd: Optional[datetime] = None
    ):
        async with async_db() as session:
            query = select(ParameterLimit)
            if idParameterLimit:
                query = query.filter(ParameterLimit.id_parameterlimit.in_(idParameterLimit))
            if idParameter:
                query = query.filter(ParameterLimit.id_parameter.in_(idParameter))
            if idLimitType:
                query = query.filter(ParameterLimit.id_limit_type.in_(idLimitType))
            if minLimit:
                query = query.filter(ParameterLimit.min_limit.in_(minLimit))
            if maxLimit:
                query = query.filter(ParameterLimit.max_limit.in_(maxLimit))
            if momentBegin:
                query = query.filter(ParameterLimit.moment_begin == momentBegin)
            if momentEnd:
                query = query.filter(ParameterLimit.moment_end == momentEnd)
            result = await session.execute(query)
            return result.scalars().all()

    @staticmethod
    async def create(parameterlimit_data: ParameterLimit):
        async with async_db() as session:
            async with session.begin():
                session.add(parameterlimit_data)
            await session.commit()

    @staticmethod
    async def get_parameterlimit_by_id(parameterlimit_id: int):
        async with async_db() as session:
            stmt = select(ParameterLimit).where(
                ParameterLimit.id_parameterlimit == parameterlimit_id)
            result = await session.execute(stmt)
            parameterlimit = result.scalars().first()
            return parameterlimit

    @staticmethod
    async def get_all_parameterlimits():
        async with async_db() as session:
            query = select(ParameterLimit)
            result = await session.execute(query)
            return result.scalars().all()

    @staticmethod
    async def update(parameterlimit_id: int, parameterlimit_data: ParameterLimit):
        async with async_db() as session:
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
            query = update(ParameterLimit).where(
                ParameterLimit.id_parameterlimit == parameterlimit_id).values(
                # **parameter.dict()).execution_options(synchronize_session="fetch")
                id_parameter=parameterlimit_data.id_parameter,
                id_limit_type=parameterlimit_data.id_limit_type,
                min_limit=parameterlimit_data.min_limit,
                max_limit=parameterlimit_data.max_limit,
                moment_begin=parameterlimit_data.moment_begin,
                moment_end=parameterlimit_data.moment_end)

            await session.execute(query)
            await session.commit()

    @staticmethod
    async def delete(parameterlimit_id: int):
        async with async_db() as session:
            query = delete(ParameterLimit).where(
                ParameterLimit.id_parameterlimit == parameterlimit_id)
            await session.execute(query)
            await session.commit()
